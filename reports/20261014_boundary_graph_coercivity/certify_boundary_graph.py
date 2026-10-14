#!/usr/bin/env python3
"""Directed-interval certificates for the central/reflected-tail graph bound.
All complete tails are analytically enclosed; compact lower rows retain only
true prime powers wholly within their moving [0,7/10] reflection window.
This does not certify the full original Q form or RH.
"""
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps=80
mp.iv.dps=60
iv=mp.iv
lo=lambda x:mp.mpf(x._mpi_[0])
hi=lambda x:mp.mpf(x._mpi_[1])
rat=lambda a,b=1:iv.mpf(a)/b
R=rat(7,10)
P=lambda z:4*z*z-6*z
C=lambda z:8*z**3-30*z*z+15*z
# At these tail arguments the m>=2 theta tail is dominated by twice m=2.
def phi_upper(x):
 z=iv.pi*iv.exp(2*x)
 assert lo(z)>12
 assert hi(rat(81,16)*iv.exp(-5*z))<rat(1,2).a
 return iv.exp(x/2)*(P(z)*iv.exp(-z)+128*z*z*iv.exp(-4*z))
def psi_upper(x):
 z=iv.pi*iv.exp(2*x)
 assert lo(z)>12
 assert hi(rat(729,64)*iv.exp(-5*z))<rat(1,2).a
 return iv.exp(x/2)*(C(z)*iv.exp(-z)+1024*z**3*iv.exp(-4*z))
phi0_lower=P(iv.pi)*iv.exp(-iv.pi)
phiR_upper=phi_upper(R)
M_lower=phi0_lower-phiR_upper
kappa2R=iv.exp(-R)/(1-iv.exp(-4*R))
h_lower=2*kappa2R*M_lower
sR=(iv.exp(R/2)-iv.exp(-R/2))/2
assert lo(h_lower-rat(94,100))>0
assert hi(sR)<mp.mpf(358)/1000
# psi is decreasing on x >= log(4)-R: all theta arguments exceed 12.
# n=2,3 are bounded separately by psi(R); n>=4 use x>=log(n)-R.
B=(iv.ln(2)/iv.sqrt(2)+iv.ln(3)/iv.sqrt(3))*psi_upper(R)
for n in range(4,17):
 B+=iv.ln(n)/iv.sqrt(n)*psi_upper(iv.ln(n)-R)
a=iv.pi*iv.exp(-2*R)
# For n>=17, log n<=n and C(z)<=8z^3, including all m,
# give 16 exp(-R/2) a^3 n^7 exp(-a n^2). The consecutive ratio <1/2.
rho=rat(18,17)**7*iv.exp(-35*a)
assert hi(rho)<mp.mpf(1)/2
outer_tail=32*iv.exp(-R/2)*a**3*17**7*iv.exp(-289*a)
B+=outer_tail
assert hi(B)<mp.mpf(1)/10
central_margin=h_lower-sR-4*B
assert lo(central_margin-rat(18,100))>0
# Published complete theta estimate gives J>507/500. Beyond R every
# Phi term has logarithmic derivative <= 13/2-2z < -35/2.
# Hence the weighted J tail is <= exp(R/2)Phi(R)*(1+1/34).
J_tail=iv.exp(R/2)*phiR_upper*rat(35,34)
assert hi(J_tail)<mp.mpf(7)/500
J_C_lower=rat(507,500)-J_tail
assert lo(J_C_lower)>1
# Exact sieve, not all-integer replacement, in the compact LOWER bound.
N=1024
sieve=[True]*(N+1);sieve[0]=sieve[1]=False
primepowers={}
for p in range(2,N+1):
 if not sieve[p]:continue
 for j in range(p*p,N+1,p):sieve[j]=False
 n=p
 while n<=N:primepowers[n]=p;n*=p
terms=[(n,iv.ln(n),iv.ln(p)/iv.sqrt(n)) for n,p in sorted(primepowers.items())]
def first_xi(y):
 z=iv.pi*iv.exp(2*y)
 return iv.exp(y/2)*C(z)*iv.exp(-z)
minimum=None;mincell=None;retained_at_min=None
for j in range(70,600):
 X=iv.mpf([j,j+1])/100
 row=iv.mpf(0);retained=0
 for n,d,alpha in terms:
  Y=d-X
  if lo(Y)<=0 or hi(Y)>=mp.mpf(7)/10:continue
  xi=first_xi(Y)
  if lo(xi)<=0:continue
  row+=alpha*xi;retained+=1
 ss=(iv.exp(X/2)-iv.exp(-X/2))/2
 margin=row-ss
 assert lo(margin)>0,('unproved compact row cell',j,str(margin))
 if minimum is None or lo(margin)<minimum:
  minimum=lo(margin);mincell=j;retained_at_min=retained
assert minimum>mp.mpf(1)/4
assert hi(iv.ln(349))<6
# Stieltjes tail with a=.91,b=1.04 and the complete I_plus<2.93.
assert 91*100-13*293==5291
assert 5291>5000
assert 18**2<349 and 291*18>5000
res={
 'status':'PASS: complete boundary graph constants and truncated reflected row',
 'central_radius':'7/10','precision_decimal':60,
 'h_lower':mp.nstr(lo(h_lower),40),'sR_upper':mp.nstr(hi(sR),40),
 'complete_Ltail_uniform_upper':mp.nstr(hi(B),40),
 'central_margin_lower':mp.nstr(lo(central_margin),40),
 'J_C_lower':mp.nstr(lo(J_C_lower),40),
 'compact_cells':530,'cell_width':'1/100','true_prime_power_cutoff':1024,
 'compact_LC_minus_s_margin':mp.nstr(minimum,40),'minimum_cell_left':str(mp.mpf(mincell)/100),
 'retained_terms_in_minimum_cell':retained_at_min,
 'analytic_tail':'LC(x)>5291 exp(x/2)/10000 > sinh(x/2) for x>=log349',
 'scope':'Boundary graph H+(1-delta)N-P only, 0<=delta<=1/3; not full Q positivity.'}
print(json.dumps(res,indent=2))
Path(__file__).with_name('boundary_graph_certificate.json').write_text(json.dumps(res,indent=2)+'\n')
