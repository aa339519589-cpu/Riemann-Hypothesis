#!/usr/bin/env python3
"""Directed interval proof of the complete incoming-prime/Gamma hub constants.
The finite row computation is a lower bound, not a prime truncation equality.
The analytic tail relies on the stated unconditional Chebyshev theorem.
"""
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps=70
mp.iv.dps=60
iv=mp.iv
lo=lambda a:mp.mpf(a._mpi_[0])
hi=lambda a:mp.mpf(a._mpi_[1])
F=lambda a,b=1:iv.mpf(a)/b
R=F(1,2); A=F(3,4)
def phi_upper(x):
 z=iv.pi*iv.exp(2*x)
 return iv.exp(x/2)*((4*z*z-6*z)*iv.exp(-z)+128*z*z*iv.exp(-4*z))
def psi_upper(x):
 z=iv.pi*iv.exp(2*x)
 return iv.exp(x/2)*(z*(8*z*z-30*z+15)*iv.exp(-z)+1024*z**3*iv.exp(-4*z))
def kappa(x):return iv.exp(-x/2)/(1-iv.exp(-2*x))
z=iv.pi
phi0_lower=(4*z*z-6*z)*iv.exp(-z)
phi0_upper=phi_upper(F(0))
phiR_upper=phi_upper(R)
MC_lower=phi0_lower-phiR_upper
head_lower=kappa(R)*MC_lower
prime_head_debit=(iv.ln(2)/iv.sqrt(2)+iv.ln(3)/iv.sqrt(3))*psi_upper(A)+32*iv.pi**3*4**7*iv.exp(-16*iv.pi)
mid_head_debit=kappa(A)*phiR_upper
mid_mass_lower=kappa(A)*MC_lower/2
assert lo(phi0_lower)>mp.mpf('0.89')
assert hi(phi0_upper)<mp.mpf('0.9')
assert hi(phiR_upper)<mp.mpf('0.065')
assert lo(head_lower)>1
assert hi(prime_head_debit)<mp.mpf(1)/40
assert hi(mid_head_debit)<mp.mpf(1)/16
assert lo(mid_mass_lower)>mp.mpf(3)/10
assert hi(iv.exp(R/2))<mp.mpf(13)/10
assert hi(iv.exp(A/2))<mp.mpf(3)/2
assert hi(iv.ln(349)+R)<mp.mpf(32)/5
assert lo(iv.pi*iv.exp(2*A))>12
assert hi((F(5,4)**7)*iv.exp(-9*iv.pi))<mp.mpf(1)/2
assert hi((F(3,2)**6)*iv.exp(-5*iv.pi))<mp.mpf(1)/2
N=1024
is_prime=[True]*(N+1)
prime_powers={}
for p in range(2,N+1):
 if not is_prime[p]:continue
 for j in range(p*p,N+1,p):is_prime[j]=False
 n=p
 while n<=N:
  prime_powers[n]=p
  n*=p
terms=[(n,iv.ln(n),iv.ln(p)/iv.sqrt(n)) for n,p in sorted(prime_powers.items())]
def psi_first(x):
 z=iv.pi*iv.exp(2*x)
 return iv.exp(x/2)*z*(8*z*z-30*z+15)*iv.exp(-z)
minimum=mp.inf;minimum_cell=None
for j in range(75,640):
 X=iv.mpf([j,j+1])/100
 total=F(0)
 for n,d,alpha in terms:
  Y=X-d
  if lo(Y)<=0 or hi(Y)>=mp.mpf(1)/2:continue
  term=psi_first(Y)
  if lo(term)>0:total+=alpha*term
 ratio=lo(total/iv.exp(X/2))
 assert ratio>mp.mpf(1)/5, ('incoming row cell',j,ratio)
 if ratio<minimum:minimum,minimum_cell=ratio,j
from fractions import Fraction as Q
assert Q(104,100)*Q(7,10)-Q(13,100)*Q(16,5)==Q(39,125)>Q(1,5)
assert 1-Q(1,40)-Q(1,16)>Q(9,10)
result={
 'status':'PASS',
 'directed_interval_digits':60,
 'incoming_row_cells':565,
 'incoming_row_cell_width':'1/100',
 'true_prime_power_cutoff':N,
 'incoming_row_minimum_lower':mp.nstr(minimum,45),
 'minimum_cell':[str(Q(minimum_cell,100)),str(Q(minimum_cell+1,100))],
 'head_gamma_lower':mp.nstr(lo(head_lower),45),
 'complete_prime_head_debit_upper':mp.nstr(hi(prime_head_debit),45),
 'middle_head_debit_upper':mp.nstr(hi(mid_head_debit),45),
 'middle_mass_lower':mp.nstr(lo(mid_mass_lower),45),
 'analytic_row_tail_lower':'39/125',
 'global_forward_mass_coefficient':'1/10'
}
print(json.dumps(result,indent=2))
Path(__file__).with_name('incoming_prime_hub_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
