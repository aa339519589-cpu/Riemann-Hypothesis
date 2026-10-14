#!/usr/bin/env python3
"""Exact finite arithmetic checks. Analytic hypotheses are proved in the notes."""
from fractions import Fraction as F
from math import factorial

def ok(name, condition):
    assert condition, name
    print(name + ': PASS')

exp3lo=sum((F(3)**k/F(factorial(k)) for k in range(9)), F(0))
exp3sum=sum((F(3)**k/F(factorial(k)) for k in range(13)), F(0))
exp3hi=exp3sum+(F(3)**13/F(factorial(13)))/(1-F(3,14))
ok('20 < exp(3) < 25', exp3lo>20 and exp3hi<25)
e942=F(27,10)**9*(1+F(21,50)+F(21,50)**2/2)
ok('exp(471/50) > 11200', e942>11200)
e628=F(27,10)**6*(1+F(7,25)+F(7,25)**2/2)
ok('exp(157/25) > 500', e628>500)
ok('full score derivative below 10/3', F(17,8)+F(7500,6724)<F(10,3))
ok('shifted score derivative below 9/4', F(17,8)+F(12,21**2)<F(9,4))
ok('normalized log derivative below 3/z', F(1,4)+F(15,14)+F(3,4)==F(29,14)<3)
j=(F(3,6)+F(3,36)+F(2,216))/2
ok('normalized Schur coefficient 8/27', j==F(8,27))
ok('normalized killing leaves full a+beta', F(69,200)>j)
ok('true child feedback squared below 4/9', F(4,3)**2*F(1,4)==F(4,9))
ok('epsilon physical Lipschitz below 1/15', F(224)*F(22,7)/11200==F(11,175)<F(1,15))
ok('incoming extra Gamma coefficient below 1/400', F(1,150)/F(8,3)==F(1,400))
ok('full probability source coefficient below 1/200', F(1,401)+F(1,400)<F(1,200))
ok('complete contrast norm below 23/10', 2+F(4,14)<F(23,10))
ok('strong source inverse coefficient', 1-F(23,200)==F(177,200))
ok('critical theta polynomial at4 positive', 36*4**2-162*4+F(179,2)>0)
ok('critical forcing total below 1/22', F(159,3500)+F(1,200000)<F(1,22))
ok('same-tail feedback below 1/40000', F(531441,4)*10/(11200**2*500)==F(531441,25088000000)<F(1,40000))
ok('strong graph central and far margins', F(9,50)/2>F(1,100) and F(291,10000)>F(1,100))
ok('strong graph compact margin', F(1,4)/25==F(1,100))
print('All exact coefficient checks passed; no original-source sign conclusion is tested.')
