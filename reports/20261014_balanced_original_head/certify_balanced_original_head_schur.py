"""Exact-dyadic/interval Schur certificate for the balanced-load original head.
Consumes independently generated interval coefficients, not sampled matrices.
All large matrix products use Python integers and a common dyadic denominator.
"""
import argparse,json,os,math
from fractions import Fraction
from mpmath import iv
iv.dps=45

def exact(x):
 n,d=x.as_integer_ratio();return iv.mpf(n)/d

def interval(p):
 return iv.mpf([exact(p[0]).a,exact(p[1]).b])

def ceildiv(a,b):return -((-a)//b)

def center_radius(pair,Q):
 lo,hi=map(Fraction.from_float,pair)
 c=((lo+hi)*Q/2).__floor__()
 r=max(c-(lo*Q).__floor__(),(hi*Q).__ceil__()-c)
 return c,r

def certify(kernel,load):
 N,M=kernel['N'],kernel['M'];assert N==48 and M==4096
 assert load['basis']=='sqrt(2/log 2) sin(k*pi*x/log 2)'
 assert load['endpoint_zero_exact'] is True
 assert load['ibp_constants_upper_enclosures'][0][1]<2
 assert load['ibp_constants_upper_enclosures'][1][1]<3
 Q=1<<48;Q3=Q**3;J=M-N
 C=[[0]*J for _ in range(N)];R=[[0]*J for _ in range(N)]
 for i in range(N):
  for k in range(J):C[i][k],R[i][k]=center_radius(kernel['q_cross'][i][k],Q)
 wi=[];err=0
 for k,p in enumerate(kernel['high_diagonal']):
  n,d=p[0].as_integer_ratio();assert n>0
  w=ceildiv(Q*d,n);wi.append(w)
  cn=sum(abs(C[i][k]) for i in range(N));rn=sum(R[i][k] for i in range(N))
  err+=w*(2*cn*rn+rn*rn)
 print('Certified cross interval scalar error upper',iv.mpf(err)/Q3,flush=True)
 CW=[[c*w for c,w in zip(row,wi)] for row in C]
 U=[interval(x['interval']) for x in load['coefficients_U']]
 V=[interval(x['interval']) for x in load['coefficients_V']]
 assert len(U)==len(V)==N
 assert all(x['k']==i+1 for tag in ['coefficients_U','coefficients_V'] for i,x in enumerate(load[tag]))
 tail=exact(kernel['schur_tail'][1]);error=iv.mpf(err)/Q3
 A=[[None]*N for _ in range(N)]
 for i in range(N):
  for j in range(i+1):
   q1=kernel['q_low'][i][j];q2=kernel['q_low'][j][i]
   q=[max(q1[0],q2[0]),min(q1[1],q2[1])];assert q[0]<=q[1]
   schur=sum(x*y for x,y in zip(CW[i],C[j]))
   val=interval(q)+U[i]*U[j]+V[i]*V[j]-iv.mpf(schur)/Q3
   if i==j:val-=iv.mpf(1)/100+tail+error
   A[i][j]=A[j][i]=val
 # Interval LDL: every pivot enclosure must be strictly positive.
 D=[];LL=[[iv.mpf(0) for j in range(N)] for i in range(N)]
 for i in range(N):
  piv=A[i][i]-sum(LL[i][k]**2*D[k] for k in range(i))
  assert bool(piv.a>0),('nonpositive or unresolved pivot',i,piv)
  D.append(piv);LL[i][i]=iv.mpf(1)
  for j in range(i+1,N):
   LL[j][i]=(A[j][i]-sum(LL[j][k]*LL[i][k]*D[k] for k in range(i)))/piv
 print('SUCCESS: all',N,'interval LDL pivots positive.',flush=True)
 print('Minimum pivot lower:',min(float(v.a) for v in D),flush=True)
 print('High first gap:',kernel['first_gap'],'omitted Schur upper:',kernel['schur_tail'][1],flush=True)
 return {'N':N,'M':M,'minimum_pivot_lower':min(float(v.a) for v in D),'cross_error_upper':float(error.b),'omitted_schur_upper':kernel['schur_tail'][1]}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--kernel',default='original_head_kernel_intervals.json');p.add_argument('--load',default='balanced_head_coefficients.json');a=p.parse_args()
 here=os.path.dirname(__file__)
 with open(os.path.join(here,a.kernel)) as f:k=json.load(f)
 with open(os.path.join(here,a.load)) as f:l=json.load(f)
 # The original kernel used the loss20/N. Balanced tails4/N and9/N
 # require the one-time loss26/N, so subtract exactly6/N from every gap.
 from certify_original_head_kernel import psi_complex,pair,b,pi,alpha3
 iv.dps=45
 N,M=k['N'],k['M'];extra=iv.mpf(6)/N
 k['high_diagonal']=[pair(interval(p)-extra) for p in k['high_diagonal']]
 k['first_gap']=k['high_diagonal'][0]
 alpha2=b/iv.sqrt(2)
 CN=pi+4*b/(pi*pi*N)+2*(alpha2+alpha3)+4*((iv.exp(b)-iv.exp(-b))/2-b)
 re,_=psi_complex((M+1)*pi/b)
 dm=2*(re-iv.log(pi))-CN-iv.mpf(26)/N-iv.mpf(1)/100
 Ci=[1+4*alpha3/(pi*(1-iv.mpf(N)/(M+1)))+6*b/(pi*pi*i) for i in range(1,N+1)]
 k['schur_tail']=pair(sum(t*t for t in Ci)/(M*dm))
 certify(k,l)
