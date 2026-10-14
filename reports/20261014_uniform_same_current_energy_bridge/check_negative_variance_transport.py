#!/usr/bin/env python3
"""Directed intervals for the actual negative current-storage bound b_- <= 2 psi exp(x/2)."""
import json
from pathlib import Path
from fractions import Fraction as Q
import mpmath as mp
mp.mp.dps=60;mp.iv.dps=50;iv=mp.iv
lo=lambda a:mp.mpf(a._mpi_[0]);hi=lambda a:mp.mpf(a._mpi_[1]);F=lambda a,b=1:iv.mpf(a)/b
pi=iv.pi
phi0hi=(4*pi*pi-6*pi)*iv.exp(-pi)+128*pi*pi*iv.exp(-4*pi)
theta0hi=iv.exp(-pi)+2*iv.exp(-4*pi);K0hi=3*phi0hi+theta0hi/2
M=[]
for j in range(3):
 a=F(4*j+1,2);integ=F(0)
 for k in range(500):
  x=iv.mpf([k,k+1])/500;z=pi*iv.exp(2*x)
  val=iv.exp((F(1,2)-a)*x)*(4*z*z-6*z)*iv.exp(-z)
  integ+=iv.mpf(lo(val))/500
 M.append(hi(phi0hi-a*integ))

assert M[0]<mp.mpf(4)/5 and M[1]<mp.mpf(1)/2 and M[2]<mp.mpf(1)/3
N=2048;isp=[True]*(N+1);pp={}
for p in range(2,N+1):
 if not isp[p]:continue
 for k in range(p*p,N+1,p):isp[k]=False
 n=p
 while n<=N:pp[n]=p;n*=p
terms=[(iv.ln(n),iv.ln(p)/iv.sqrt(n)) for n,p in pp.items()]
a=pi*iv.exp(-12);N0=N+1
tail=256*iv.exp(-3)*a**3*N0**7*iv.exp(-a*N0*N0)
assert hi(tail)<mp.mpf('1e-24')
assert lo(a*N0*N0)>12
assert hi((F(N0+1,N0)**7)*iv.exp(-a*(2*N0+1)))<mp.mpf(15)/16
def psiup(x):
 z=pi*iv.exp(2*x)
 return iv.exp(x/2)*((8*z**3-30*z*z+15*z)*iv.exp(-z)+1024*z**3*iv.exp(-4*z))
def bound(l,r):
 X=iv.mpf([lo(F(l.numerator,l.denominator)),hi(F(r.numerator,r.denominator))]);z=pi*iv.exp(2*X)
 # each coefficient below is nonnegative; interval dependency retained
 H=iv.exp(-X)*((1-iv.exp(-6*X))*F(4,5)+(iv.exp(-2*X)-iv.exp(-6*X))/2+(iv.exp(-4*X)-iv.exp(-6*X))/3+iv.exp(-6*X)*K0hi)
 L=tail
 for d,al in terms:
  Y=d-X
  if hi(Y)<=0:continue
  if lo(Y)<0:Y=iv.mpf([0,hi(Y)])
  L+=al*psiup(Y)
 Klo=iv.exp(X/2-z)*(3*(4*z*z-6*z)+F(1,2))
 val=H+iv.exp(-X/2)*L+2*X*iv.exp(-X/2)*psiup(X)-(1-iv.exp(-X))/4-2*iv.exp(-X/2)*Klo
 return hi(val)
maximum=-mp.inf;count=0;worst=None
stack=[(Q(1,12),Q(9,100))]+[(Q(j,100),Q(j+1,100)) for j in range(9,600)]
while stack:
 l,r=stack.pop();v=bound(l,r)
 if v>=2:
  assert r-l>Q(1,100000),(l,r,v)
  mid=(l+r)/2;stack.extend([(l,mid),(mid,r)]);continue
 count+=1
 if v>maximum:maximum=v;worst=(l,r)
assert hi(K0hi)<3
assert hi(iv.ln(349))<6
z1=pi*iv.exp(2)
assert lo(z1)>20
phi1_upper=iv.exp(F(1,2))*((4*z1*z1-6*z1)*iv.exp(-z1)+128*z1*z1*iv.exp(-4*z1))
assert hi(iv.exp(F(1,2))*phi1_upper/33)<mp.mpf(1)/100
assert hi(iv.exp(F(1,2)))<mp.mpf(5)/3
assert Q(9,10)+(Q(5,12)+Q(1,100))/2<Q(6,5)
assert Q(16*20**4)/Q(5,2)**20<Q(1,10)
assert Q(3,349)<Q(1,100)
tail_bound=Q(104,100)*Q(6,5)+Q(13,100)*Q(293,100)+Q(1,100)+Q(1,10)
assert tail_bound<2
result={'status':'PASS','directed_interval_digits':50,
'compact_cells':count,'compact_maximum_upper':mp.nstr(maximum,45),
'maximum_cell':[str(t) for t in worst],
'laplace_moment_upper_enclosures':[mp.nstr(t,45) for t in M],
'complete_omitted_prime_tail_upper':mp.nstr(hi(tail),45),
'prime_power_prefix':N,'analytic_tail_upper':str(tail_bound),
'actual_negative_transport_coefficient':'2'}
print(json.dumps(result,indent=2))
Path(__file__).with_name('negative_variance_transport_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
