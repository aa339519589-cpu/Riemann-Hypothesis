'''Certify the zero-harmonic Gamma constant for the new rational packet.
Nonzero harmonics use BTY (36) with the explicit l1 error, not kappa error.'''
import json
from pathlib import Path
from fractions import Fraction
from flint import arb,ctx
ctx.prec=160
def B(q):
 q=Fraction(q);return arb(q.numerator)/q.denominator
ks=[B(s) for s in json.load(open(Path(__file__).with_name('rescaled_packet.json')))['kappa']]
kappa=sum(ks);ab=sum(abs(k) for k in ks)
c=[4,-8,2,20,-9,-34,27,91,-27,-201,32,895,1949,2389,1896,949,239]
aks=[B(Fraction(2*sum(c[j]*c[j+k] for j in range(17-k)),14912370)) for k in range(1,17)]
asum=sum(aks)
constant=kappa/2*sum(aks[j-1]*(B(j)/(2*arb.pi())).log() for j in range(1,17))
# From (36), uniformly 1<=Re z<=4.5, |Im z|>=H/2:
H=B(3*10**12);y=H/2
err=B('4.5')/(2*y*y)+1/(12*y)+B('4.5')**2/(2*y*y)
assert err<B('1e-10')
# Use the absolute coefficient sum for BOTH signs.
err_total=asum*ab*B('1e-10')/2
left=Fraction(1986935,2000000);right=Fraction(1);N=128;maxupper=None
for j in range(N):
 lo=left+(right-left)*j/N;hi=left+(right-left)*(j+1)/N
 sig=B((lo+hi)/2)+arb(0,B((hi-lo)/2))
 v=constant+sum(ks[m]*(-arb.pi().log()+((sig+(2*sig-1)*m)/2+1).digamma())/2 for m in range(7))+err_total
 assert v < -B('1.56'),(j,str(v))
 if maxupper is None or v.upper()>maxupper:maxupper=v.upper()
E2=14*ab*asum;E3=ab*(623+424*asum)
assert E2<245 and E3<10500
print('PASS Gamma constant <= -1.56; worst interval upper',maxupper)
print('PASS complete coefficient costs E2<245,E3<10500:',E2,E3)
print('Scope: base623/14/424 and BTY(36) separately justified analytically.')
