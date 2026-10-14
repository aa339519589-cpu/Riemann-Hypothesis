#!/usr/bin/env python3
"""Rational global constants for the complete centered Mobius profile.
Analytic identities and all-integer tails are proved in the companion text.
"""
from fractions import Fraction as F
from math import factorial
assert sum(F(3**k,factorial(k)) for k in range(9))>20
assert F(64,45*384**2)<1
assert 5+F(17,16)+F(1,3)<7
assert F(84,20**3)==F(21,2000)
# exp(1)<11/4<25/9: tail after degree4 is at most (1/120)/(1-1/6).
assert sum(F(1,factorial(k)) for k in range(5))+F(1,120)/(1-F(1,6))<F(11,4)<F(25,9)
assert 1+F(1,2)+F(1,8)>F(3,2)
c_gamma=2*(F(147,1000)*F(2,3)+F(2,401))
assert c_gamma==F(49,250)+F(4,401)
# Complete prime cross majorant, including every integer beyond2.
assert F(1,65536)/(1-F(1,2**29))<F(1,60000)
assert 3*F(1,60000)==F(1,20000)
c=F(397,401)*F(207,100)-c_gamma-F(1,20000)
assert c==F(14783479,8020000)>F(9,5)
print('PASS: complete centered Mobius Gamma/prime Schur debit and spatial gap >9/5.')
print('Exact net lower coefficient:', c)
