#!/usr/bin/env python3
"""Directed complete-theta certificate for one genuine prime2 Gamma routing.
This does NOT compare the complete prime form with Gamma.
"""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=65
mp.iv.dps=55
iv=mp.iv
lo=lambda v:mp.mpf(v._mpi_[0])
hi=lambda v:mp.mpf(v._mpi_[1])
F=lambda a,b=1:iv.mpf(a)/b
R=F(1,2); D=iv.ln(2); alpha=D/iv.sqrt(2)
def poly(q):return 8*q**3-30*q*q+15*q
def psi_lower(x):
 z=iv.pi*iv.exp(2*x)
 return iv.exp(x/2)*(poly(z)*iv.exp(-z)+poly(4*z)*iv.exp(-4*z))
def psi_upper(x):
 z=iv.pi*iv.exp(2*x)
 return iv.exp(x/2)*(poly(z)*iv.exp(-z)+1024*z**3*iv.exp(-4*z))
def phi_upper(x):
 z=iv.pi*iv.exp(2*x)
 return iv.exp(x/2)*((4*z*z-6*z)*iv.exp(-z)+128*z*z*iv.exp(-4*z))
def kappa(t):return iv.exp(-t/2)/(1-iv.exp(-2*t))
z0=iv.pi
J=(4*z0*z0-6*z0)*iv.exp(-z0)-phi_upper(R)
assert lo(J)>mp.mpf('0.83')
assert lo(iv.pi*iv.exp(F(6,5)))>10
assert lo(D)>mp.mpf('0.69') and hi(D)<mp.mpf('0.70')
# Full theta tails: positive omitted n>=3; upper n>=2 uses first term
# bounded by512 z^3 exp(-4z), followed by a ratio below1/2.
assert hi(F(3,2)**6*iv.exp(-5*iv.pi))<mp.mpf(1)/2
# Eight positive exponential rows of kappa, with certified lower moments.
NM=8; NA=10000
mom=[iv.mpf(0) for _ in range(NM)]
for j in range(NA):
 X=iv.mpf([j,j+1])/(2*NA)
 p=max(mp.mpf(0),lo(psi_lower(X)))
 base=iv.exp(X/2); step=iv.exp(2*X)
 for k in range(NM):
  mom[k]+=iv.mpf(p)*base/(2*NA)
  base*=step
M=[iv.mpf(lo(v)) for v in mom]
assert lo(M[0])>mp.mpf('0.9')
max_ratio=mp.mpf(0);cell=None
NX=6000
for j in range(NX):
 X=iv.mpf([j,j+1])/10000
 Y=X+D
 lower=sum(M[k]*iv.exp(-(F(1,2)+2*k)*Y) for k in range(NM))
 value=hi(alpha*psi_upper(X)/lower)
 assert value<mp.mpf(3)/2,(j,str(value))
 if value>max_ratio:max_ratio=value;cell=j
# Beyond x=.6, e^(x/2)psi(x) decreases termwise because q>=10,
# q*poly'(q)<=4poly(q), and its log derivative is <=9-2q<0.
q=iv.mpf([10,11])
assert lo(8*q*q-60*q+45)>0
far=hi(D*iv.exp(F(3,10))*psi_upper(F(3,5))/J)
assert far<mp.mpf(3)/2
# On y>=log2, psi(y)/kappa(y) decreases by the same termwise estimate,
# plus at most2/3 from1-exp(-2y). All n>=1 have q>=4pi>12.
assert lo(4*iv.pi)>12
path=hi(alpha*psi_upper(D)*kappa(D-R)/(J*kappa(D)*kappa(R)))
assert path<mp.mpf(1)/12
out={'theorem':'single prime2 routing only','moment_cells':NA,'source_cells':NX,
     'moments_lower':[mp.nstr(lo(v),45) for v in M],
     'central_mass_lower':mp.nstr(lo(J),45),
     'incoming_ratio_upper':mp.nstr(max_ratio,45),'worst_cell':cell,
     'far_ratio_upper':mp.nstr(far,45),'return_path_ratio_upper':mp.nstr(path,45),
     'form_coefficient':'11/4','all_theta_tails_retained':True}
print(json.dumps(out,indent=2))
