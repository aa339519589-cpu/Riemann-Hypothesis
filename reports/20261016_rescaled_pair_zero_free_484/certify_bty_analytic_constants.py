"""Outward certificates for fixed-scale BTY analytic error constants.
Repairs the source's 138 threshold and its incorrect integral <24.
All inputs are exact decimal/rational numbers.  No zero-free theorem is asserted.
"""
from flint import arb,ctx
from fractions import Fraction
import json
from pathlib import Path
ctx.prec=192;ctx.threads=1
def B(q):
 q=Fraction(q);return arb(q.numerator)/q.denominator
th=B('1.1338');Ao=1/B('4.8594');H=B(3000000000000);T0=B(10000000000)
eta=Ao/H.log();sig=1-Ao/(16*H+T0).log();d=2*sig-1;x0=sig-B('1/2')
w0=(th*th.tan()+3*th/th.tan()-3)/(th.cos()**2)
c0=1/(th.sin()*th.cos()**2);c1=(th-th.sin()*th.cos())*th.tan()**4;c2=th.tan()**3*th.sin()**2;c3=(th-th.sin()*th.cos())*th.tan()**2
def C(nu,r):return c0*r*(c2*(r+1)**2*((-2*nu*th/th.tan()).exp()+1)+c1*r+c3*r**3)/(r*r-th.tan()**2)**2
assert d/eta>137
E=eta**2*C(B(137),B(137))/(d*d*w0);assert E<B('1/2000')
Cx=C(x0/eta,x0/eta);assert Cx<22
T2=C(sig/eta,sig/eta)/x0**3;assert T2<180
# Natural interval rectangle upper on [0,10], split at1/2.
# For y>=10, U(y)<=log(y)+1, and denominator >= y^3.
def U(y,small):
 if small:return ((16/(1+4*y*y)).log()/2+2/(1+4*y*y)+2)
 return abs((y/2).log()-2/(1+4*y*y))+2/(3*y)+1/(8*y*y)
integ=B(0);step=Fraction(1,4096)
for j in range(10*4096):
 l=j*step;r=(j+1)*step;mid=(l+r)/2;rad=(r-l)/2;y=B(mid)+arb(0,B(rad))
 val=U(y,r<=Fraction(1,2))/(x0*x0+y*y)**B('3/2')
 integ+=B(step)*val.upper()
tail=(B(10).log()+B('3/2'))/100 # twice integral_10^infty (log y+1)/y^3
integ=2*integ+tail
assert integ<36
assert 22*36/(2*arb.pi())<127
# At actual heights k*t, eta log(t)<=Ao but eta log(k*t)<=Ao+eta log16.
leading=22*Ao/(arb.pi()*x0*x0);extra=22*B(16).log()/(arb.pi()*x0*x0)
assert leading<6 and extra<80
# Globally U(x)<=6+log(1+|x|), directly from its two displayed branches.
# On either far tail y>=t-2>=H-2, |t +/- y|<=3y, so U<=8+log y.
# This avoids the source's false claim U(0)<log100.
R=H-2
I1=(R.log()/2+B('17/4'))/R**2
I3=I1
assert I1<B('1e-20') and I3<B('1e-20')
# Consequently t=0 seed error <307 eta^3; 1<=k<=16 error <6 eta^2+261 eta^3.
# They imply the requested looser623 eta^3 and14 eta^2+424 eta^3.
assert 127+180<623 and 6<14 and 261<424
out={k:str(v) for k,v in [('eta0',eta),('sigma0',sig),('pair_error_epsilon',E),('C_gamma',Cx),('T2_coefficient',T2),('U_integral_upper',integ),('high_eta2',leading),('high_logk_eta3',extra),('I1_tail',I1),('I3_tail',I3)]}
out['result']='PASS';out['repaired_seed_error_at_zero']='307 eta^3';out['repaired_seed_error_at_kt']='6 eta^2 + 261 eta^3, 1<=k<=16';out['scope']='analytic scalar error constants only; source kernel/digamma bounds are stated separately'
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
