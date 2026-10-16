"""Directed constants for a block-dependent HPY estimate, uniform for t>=exp(50)."""
from flint import arb,ctx
from fractions import Fraction
from pathlib import Path
import json,hashlib
ctx.prec=192

def B(q):
 q=Fraction(q);return arb(q.numerator)/q.denominator
pi=arb.pi();x0=B(50);T=x0.exp();K0=(x0/3).exp();r0=3;r1=1000;epsilon=B('7/5');Rstar=B(1000)
R_lower=((T/(2*pi)).sqrt()-1)/(K0+1)-1
assert R_lower>Rstar and Rstar>=r1 and r1>=r0
rho=(1+1/Rstar)/(B(2).sqrt()*pi**B('1/6'))
def kbeta(r):
 r=B(r);W=pi*(r+1)**3;L=((r+1)/r)**3
 mu=(L**B('2/3')+L**B('1/3')/(1-1/K0))/2
 alpha=1/epsilon+epsilon*mu/(3*W**B('1/3'))+mu/(3*W**B('2/3'))+32*mu/(15*pi.sqrt())*(epsilon+W**B('-1/3')).sqrt()
 beta=32/(3*(pi*epsilon).sqrt())+(2-4/pi)*W**B('-1/3')
 kappa=(alpha+epsilon*alpha*(-x0/6).exp()*rho+epsilon*beta*(-x0/6).exp()*rho**3*(1+(-x0/3).exp())**2).sqrt()
 return kappa,beta
kappa,beta_tail=kbeta(r1);beta=kbeta(r0)[1]
S=B(0);previous=None
for r in range(r0,r1):
 kr,br=kbeta(r)
 assert kr>kappa and br>beta_tail
 if previous is not None:assert previous>kr
 previous=kr
 S+=(kr-kappa)/(B(r)*(r+1)).sqrt()
assert 2-4/pi>0
J0=(1+1/(2*Rstar)).log()+2*(1+(1+1/(Rstar+B('1/2'))).sqrt()).log()
omega=-(2*pi).log()/2+J0-2*(B(r0)-B('1/2')).sqrt().asinh()
C=(beta*pi**B('2/3')*(1+B(1)/r0)*(1+(-x0/3).exp())).sqrt()
z=C/kappa*(1/(2*pi).sqrt()+B('3/2')*(-x0/6).exp())
root=(1+z*z).sqrt();J=root-1-((1+root)/2).log()
assert z>0 and J>0 and x0/6+omega>0 and S>0
b1=kappa/(3*pi**B('1/6'))
b2=4*(B(r0)*(1+(-x0/3).exp())).sqrt()+2/pi**B('1/6')*(kappa*(omega+J)+S)
b3_upper=-2+B('1.48')*(-x0/4).exp()+B('.127')*(-3*x0/4).exp()
assert b1<B('.40312') and b2<B('3.240') and b3_upper<0
out={'status':'PASS','precision_bits':192,'log_t0':'50','r0':r0,'r1':r1,'epsilon':'7/5','R_lower':'1000','bound_b1':'.40312','bound_b2':'3.240','prefix_terms':r1-r0,'S':str(S),'kappa_tail':str(kappa),'beta_first':str(beta),'z':str(z),'J_unsplit':str(J),'b1_ball':str(b1),'b2_ball':str(b2),'b3_upper':str(b3_upper),'continuous_R_lower':str(R_lower),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('blockwise_hpy_constants.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
