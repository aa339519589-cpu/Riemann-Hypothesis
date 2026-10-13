"""Independent scalar comparisons for the reviewed boundary lemma, not the phone's script."""
from fractions import Fraction as F
import json

def exp_bounds(x,n=40):
    assert x>=0 and n+2>x
    t=s=F(1)
    for k in range(1,n+1):
        t*=x/k
        s+=t
    remainder=t*x/(n+1)/(1-x/F(n+2))
    return s,s+remainder

checks=[]
def check(name, statement):
    assert statement, name
    checks.append(name)

check('theta polynomial coefficient below 59',4*F(22,7)**2+6*F(22,7)<59)
check('theta strip prefactor below 100',59*F(32,31)*F(4,3)<100)
check('theta neighbor ratio below one quarter',16/exp_bounds(F(9,2))[0]<F(1,4))
check('exp two below nine',exp_bounds(F(2))[1]<9)
check('exp four below eighty one',exp_bounds(F(4))[1]<81)
check('exp three quarters above two',exp_bounds(F(3,4))[0]>2)
check('four-and-half r envelope quadratic positive',F(3)**2-4*F(3,2)*F(11,4)<0)
check('five r envelope quadratic positive',F(7,2)**2-4*F(3,2)*F(11,4)<0)
check('Gamma logarithm ratio quadratic positive',4**2-4*35*5<0)
check('coarse C0 upper bound below eight',F(53,7)<8)
check('complete prime bound below two power twenty four',F(16,3)*10000*81*2==8640000<2**24)
check('centered Gamma bound below two power twenty six',F(600**2*4*200,6)<2**26)
check('two kernel bounds total below two power twenty seven',2**26+2**24<2**27)
check('multiplicity row below two power twelve',12*17**2<2**12)
check('final product is two power thirty nine',2**27*2**12==2**39)
print(json.dumps({'arithmetic':'Python Fraction; positive exponential Taylor sum and explicit geometric remainder',
 'checks':checks,'count':len(checks),'status':'all assertions passed',
 'scope':'Independent scalar checks only. Analytic envelopes, complete tails, original domains and operator identities require the accompanying proof.'},indent=2))
