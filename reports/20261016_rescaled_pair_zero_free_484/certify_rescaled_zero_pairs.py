from pathlib import Path
'''Outward constants for positivity of every far-ordinate actual zero pair.'''
import json
from fractions import Fraction
from flint import arb,ctx
ctx.prec=192
def B(q):
 q=Fraction(q);return arb(q.numerator)/q.denominator
pk=json.load(open(Path(__file__).with_name('rescaled_packet.json')))
th=B('1.1338');eta=B('.007163');dm=B('.986935');T=B(10**10)
w0=(th*th.tan()+3*th/th.tan()-3)/th.cos()**2
c0=1/(th.sin()*th.cos()**2);c1=(th-th.sin()*th.cos())*th.tan()**4;c2=th.tan()**3*th.sin()**2;c3=(th-th.sin()*th.cos())*th.tan()**2
r=T/eta
C=c0*r*(c2*(r+1)**2*((2*th/th.tan()).exp()+1)+c1*r+c3*r**3)/(r*r-th.tan()**2)**2
assert C<51 and w0<6 and sum(abs(B(x)) for x in pk['kappa'])<5
lead=B(pk['pair_leading']);lower=w0*dm*lead-B(30720)/T**2-B(510)*eta**2/T
assert lower>0
# All actual shifted arguments u=x+md obey |u|<=8 and Re(u/eta)>=-1.
# Pole terms use |Re W((s+dm-1)/eta)| <= eta*w0*8/H^2+51 eta^3/H^3.
H=B(3*10**12);asum=B(Fraction(2919857,828465));pole=asum*5*(w0*8/H**2+51*eta**2/H**3)*eta
assert pole<B('1e-6')
print('PASS C(-1,T/eta)<51:',C)
print('PASS far-pair bracket positive:',lower)
print('PASS all nonzero-harmonic pole terms <1e-6:',pole)
