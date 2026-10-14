"""Exact-dyadic/interval UNREPAIRED original-head Schur test.
A success is meaningful only with the complete analytic tail theorem.
No finite diagnostic eigenvalue is used in this certificate.
"""
import argparse,json,os
from fractions import Fraction
from mpmath import iv
from certify_unrepaired_head_kernel import psi_complex,b,pi,alpha2,alpha3
iv.dps=70

def exact(x):
 n,d=x.as_integer_ratio();return iv.mpf(n)/d

def interval(p):return iv.mpf([exact(p[0]).a,exact(p[1]).b])
def ceildiv(a,b):return -((-a)//b)
def center_radius(pair,Q):
 lo,hi=map(Fraction.from_float,pair)
 c=((lo+hi)*Q/2).__floor__()
 r=max(c-(lo*Q).__floor__(),(hi*Q).__ceil__()-c)
 return c,r

def structured_tail(N,M):
 om=[i*pi/b for i in range(1,N+1)]
 v=[[],[],[]];w=[[],[],[]];r7=[];r8=[]
 sb=(iv.exp(b/2)-iv.exp(-b/2))/2
 rho=iv.mpf(N)/(M+1);assert bool(rho.b<1)
 for i,A in enumerate(om,1):
  re,im=psi_complex(A);SS=im/(2*A)
  EE=sum(iv.exp(-2*b*(2*r+iv.mpf(1)/2))/((2*r+iv.mpf(1)/2)**2+A*A) for r in range(20))
  EE+=iv.mpf(['0','1e-25'])
  SW=SS-EE
  Ai=(-1)**i*A
  Bi=Ai*SW+alpha3*iv.sin(A*(iv.log(3)-b))
  ell=-iv.sqrt(2/b)*Ai*sb/(A*A+iv.mpf(1)/4)
  for r in range(3):
   v[r].append(-4/b*A**(2*r)*Bi+8*ell*iv.sqrt(2/b)*sb*(-iv.mpf(1)/4)**r)
   w[r].append(4/b*A**(2*r)*Ai)
  r7.append(4/b*A**6*abs(Bi)/(1-rho*rho)+8*abs(ell)*iv.sqrt(2/b)*sb/64)
  r8.append(6/b*A**7/(1-rho*rho))
 CN=pi+4*b/(pi*pi*N)+2*(alpha2+alpha3)+4*((iv.exp(b)-iv.exp(-b))/2-b)
 re,_=psi_complex((M+1)*pi/b)
 dm=2*(re-iv.log(pi))-CN-iv.mpf(1)/10**10
 assert bool(dm.a>0)
 # The exact complete weighted S_j gives |theta_j|<3/2 for j>M.
 assert bool((pi/4+1/((M+1)*pi/b)+alpha3).b<iv.mpf(3)/2)
 coeff=[]
 for p in range(1,7):coeff.append((b/pi)**(2*p)/((2*p-1)*iv.mpf(M)**(2*p-1)*dm))
 rr=2*sum(x*x for x in r7)*(b/pi)**14/(13*iv.mpf(M)**13*dm)
 rr+=2*sum(x*x for x in r8)*(b/pi)**16/(15*iv.mpf(M)**15*dm)
 T=[[iv.mpf(0) for j in range(N)] for i in range(N)]
 for i in range(N):
  for j in range(i+1):
   val=7*sum(coeff[2*r]*v[r][i]*v[r][j]+iv.mpf(9)/4*coeff[2*r+1]*w[r][i]*w[r][j] for r in range(3))
   if i==j:val+=7*rr
   T[i][j]=T[j][i]=val
 print('Structured scalar remainder upper:',7*rr,flush=True)
 return T,dm

def certify(k):
 N,M=k['N'],k['M'];assert N==64 and M==4096
 Q=1<<60;Q3=Q**3;J=M-N
 C=[[0]*J for _ in range(N)];R=[[0]*J for _ in range(N)]
 for i in range(N):
  for j in range(J):C[i][j],R[i][j]=center_radius(k['q_cross'][i][j],Q)
 weights=[];err=0
 for j,p in enumerate(k['high_diagonal']):
  n,d=p[0].as_integer_ratio();assert n>0
  ww=ceildiv(Q*d,n);weights.append(ww)
  cn=sum(abs(C[i][j]) for i in range(N));rn=sum(R[i][j] for i in range(N))
  err+=ww*(2*cn*rn+rn*rn)
 error=iv.mpf(err)/Q3
 print('Complete finite-cross scalar uncertainty:',error,flush=True)
 CW=[[cc*ww for cc,ww in zip(row,weights)] for row in C]
 T,dm=structured_tail(N,M)
 A=[[None]*N for _ in range(N)]
 for i in range(N):
  for j in range(i+1):
   p,q=k['q_low'][i][j],k['q_low'][j][i]
   p=[max(p[0],q[0]),min(p[1],q[1])];assert p[0]<=p[1]
   schur=sum(x*y for x,y in zip(CW[i],C[j]))
   val=interval(p)-iv.mpf(schur)/Q3-T[i][j]
   if i==j:val-=iv.mpf(1)/10**10+error
   A[i][j]=A[j][i]=val
 # Direct interval LDL, retaining every input uncertainty.
 D=[];LL=[[iv.mpf(0) for j in range(N)] for i in range(N)]
 for i in range(N):
  piv=A[i][i]-sum(LL[i][k]**2*D[k] for k in range(i))
  if not bool(piv.a>0):
   print('UNRESOLVED pivot',i,piv,flush=True);return False
  D.append(piv);LL[i][i]=iv.mpf(1)
  for j in range(i+1,N):
   LL[j][i]=(A[j][i]-sum(LL[j][k]*LL[i][k]*D[k] for k in range(i)))/piv
  print('pivot',i+1,'lower',float(piv.a),flush=True)
 print('SUCCESS: complete UNREPAIRED original head >=10^-10 I.',flush=True)
 print('Minimum pivot lower:',min(float(x.a) for x in D),flush=True)
 print('High gap:',k['first_gap'],'tail gap:',dm,flush=True)
 return True

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--kernel',default='unrepaired_head_kernel_intervals.json');a=p.parse_args()
 path=os.path.join(os.path.dirname(__file__),a.kernel)
 with open(path) as f:k=json.load(f)
 assert certify(k)
