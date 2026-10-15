"""Complete augmented original-head Schur certificate for t=Cphi.
Requires the complete analytic mixed-column and endpoint/variation proofs.
No finite Galerkin eigenvalue is used as a substitute for the infinite tail.
"""
import os,json,argparse
from mpmath import iv
import certify_unrepaired_head_schur as h
from certify_unrepaired_head_kernel import pi,b,alpha3,psi_complex
iv.dps=80;base=os.path.dirname(__file__)
p=argparse.ArgumentParser();p.add_argument('--columns',default='filtered_mixed_columns_intervals.json');p.add_argument('--endpoint',default='filtered_main_force_endpoint.json');args=p.parse_args()
k=json.load(open(os.path.join(base,'unrepaired_head_kernel_intervals.json')))
f=json.load(open(os.path.join(base,args.columns)))
ep=json.load(open(os.path.join(base,args.endpoint)))
assert f['N']==4096
cols=f['mixed'];N=64;M=4096;nn=65
fb=h.interval(ep['complete_endpoint'])
assert bool(fb.a>iv.mpf('.00005099343444')) and bool(fb.b<iv.mpf('.00005099343502'))
Q=1<<60;Q3=Q**3;J=M-N
rows=k['q_cross']+[cols[N:M]]
C=[[0]*J for _ in range(nn)];R=[[0]*J for _ in range(nn)]
for i in range(nn):
 for j in range(J):C[i][j],R[i][j]=h.center_radius(rows[i][j],Q)
weights=[];err=0
for j,dd in enumerate(k['high_diagonal']):
 n,d=dd[0].as_integer_ratio();assert n>0
 ww=h.ceildiv(Q*d,n);weights.append(ww)
 cn=sum(abs(C[i][j]) for i in range(nn));rn=sum(R[i][j] for i in range(nn))
 err+=ww*(2*cn*rn+rn*rn)
eta=iv.mpf(1001)/1000;error=eta*iv.mpf(err)/Q3
print('Complete finite-cross scalar uncertainty:',error,flush=True)
CW=[[x*w for x,w in zip(row,weights)] for row in C]
T,dm=h.structured_tail(N,M);TA=[[iv.mpf(0) for j in range(nn)] for i in range(nn)]
for i in range(N):
 for j in range(N):TA[i][j]=2*T[i][j]
I1=(b/pi)**2/(M*dm);vs=-iv.sqrt(2/b)*fb;sb=(iv.exp(b/2)-iv.exp(-b/2))/2
for i in range(1,N+1):
 om=i*pi/b;im=psi_complex(om)[1]
 S=im/(2*om)-sum(iv.exp(-2*b*(2*r+iv.mpf(1)/2))/((2*r+iv.mpf(1)/2)**2+om*om) for r in range(20))-iv.mpf(['0','1e-25'])
 Ai=(-1)**i*om;Bi=Ai*S+alpha3*iv.sin(om*(iv.log(3)-b));ell=-iv.sqrt(2/b)*Ai*sb/(om*om+iv.mpf(1)/4)
 v0=-4/b*Bi+8*ell*iv.sqrt(2/b)*sb
 TA[i-1][N]=TA[N][i-1]=iv.mpf(21)/2*I1*v0*vs
Rsource=(2/b)*100*(b/pi)**4/(3*iv.mpf(M)**3*dm)
TA[N][N]=iv.mpf(21)/2*I1*vs**2+116*Rsource+3*iv.mpf('5e-15')**2/dm
print('Complete source infinite-column debit:',TA[N][N],flush=True)
source_floor=iv.mpf('3e-9')-iv.mpf('1.71e-10');target=iv.mpf('1e-9')
A=[[None]*nn for _ in range(nn)]
for i in range(nn):
 for j in range(i+1):
  if i<N and j<N:
   p1,p2=k['q_low'][i][j],k['q_low'][j][i]
   val=h.interval([max(p1[0],p2[0]),min(p1[1],p2[1])])
  elif i==N and j<N:val=h.interval(cols[j])
  else:val=source_floor-target
  sc=sum(x*y for x,y in zip(CW[i],C[j]))
  val-=eta*iv.mpf(sc)/Q3+TA[i][j]
  if i==j:val-=error+(iv.mpf('1e-10') if i<N else 0)
  A[i][j]=A[j][i]=val
D=[];L=[[iv.mpf(0) for j in range(nn)] for i in range(nn)]
for i in range(nn):
 dd=A[i][i]-sum(L[i][j]**2*D[j] for j in range(i))
 print('pivot',i+1,'lower',float(dd.a),'upper',float(dd.b),flush=True)
 if not bool(dd.a>0):raise RuntimeError('UNRESOLVED complete augmented pivot')
 D.append(dd);L[i][i]=iv.mpf(1)
 for j in range(i+1,nn):L[j][i]=(A[j][i]-sum(L[j][r]*L[i][r]*D[r] for r in range(i)))/dd
print('SUCCESS: complete original-source S0[Cphi] >= 1e-9.',flush=True)
print('This is one exact non-neutral test, not a uniform sign on the neutral complement.',flush=True)
