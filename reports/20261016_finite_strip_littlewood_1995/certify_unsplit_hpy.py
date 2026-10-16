"""Directed constants for the unsplit HPY Section 3.4 argument at t0=exp(50)."""
from flint import arb,ctx
from fractions import Fraction
from pathlib import Path
import json,hashlib
ctx.prec=192

def B(q):
 q=Fraction(q);return arb(q.numerator)/q.denominator
pi=arb.pi();x0=B(50);t0=x0.exp();K0=(x0/3).exp();r=B(6);eta=B('4/3');R0=B(1000)
# The displayed continuous lower bound is below the exact floor bound.
r_lower=((t0/(2*pi)).sqrt()-1)/(K0+1)-1
assert r_lower>R0 and R0>=r
W=pi*(r+1)**3;lam=((r+1)/r)**3
mu=lam**B('2/3')/2*(1+1/((1-1/K0)*lam**B('1/3')))
alpha=1/eta+eta*mu/(3*W**B('1/3'))+mu/(3*W**B('2/3'))+32*mu/(15*pi.sqrt())*(eta+W**B('-1/3')).sqrt()
beta=32/(3*(pi*eta).sqrt())+(2-4/pi)*W**B('-1/3')
rho=(1+1/R0)/(B(2).sqrt()*pi**B('1/6'))
kappa=(alpha+eta*alpha*(-x0/6).exp()*rho+eta*beta*(-x0/6).exp()*rho**3*(1+(-x0/3).exp())**2).sqrt()
J=(1+1/(2*R0)).log()+2*(1+(1+1/(R0+B('1/2'))).sqrt()).log()
omega=-(2*pi).log()/2+J-2*(r-B('1/2')).sqrt().asinh()
b1=kappa/(3*pi**B('1/6'))
C=(beta*pi**B('2/3')*(1+1/r)*(1+(-x0/3).exp())).sqrt()
z=C/kappa*(1/(2*pi).sqrt()+B('3/2')*(-x0/6).exp())
root=(1+z*z).sqrt()
J_unsplit=root-1-((1+root)/2).log()
assert z>0 and J_unsplit>0
b2=4*(r*(1+(-x0/3).exp())).sqrt()+2*kappa/pi**B('1/6')*(omega+J_unsplit)
assert x0/6+omega>0
assert b1<B('.4467') and b2<B('3.036')
# I_N=2 sum_{n<=N} n^-1/2-4sqrt(N)<=-2 by the elementary integral bound.
b3_upper=-2+B('1.48')*(-x0/4).exp()+B('.127')*(-3*x0/4).exp()
assert b3_upper<0
out={'status':'PASS','precision_bits':192,'log_t0':'50','r0':'6','eta':'4/3','R_lower':'1000','bound_b1':'.4467','bound_b2':'3.036','z':str(z),'J_unsplit':str(J_unsplit),'b1_ball':str(b1),'b2_ball':str(b2),'b3_upper':str(b3_upper),'continuous_R_lower':str(r_lower),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('unsplit_hpy_constants.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
