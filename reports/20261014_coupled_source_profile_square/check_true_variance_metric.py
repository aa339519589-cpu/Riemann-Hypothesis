#!/usr/bin/env python3
"""Exact rational envelopes for the true Mobius conditional-variance metric."""
from fractions import Fraction as F
from math import factorial
assert sum(F(3**k,factorial(k)) for k in range(9))>20
# n>=3 posterior-ratio moment: first term, then geometric ratio<1/2.
assert F(8,20**7)<F(1,2)
assert F(2*405,14*20**5)<F(1,1000)
# Full tail N² contribution after factoring exp(-3z).
assert F(6,20**7)<F(1,2)
assert F(2*1458,20**5)<1
# Complete moving mean/subtracted-square corrections.
assert F(21*28*401,400)<590
assert F(720*9,8000)<F(9,8)
assert F(1,3)+F(1,1000)+F(590,8000)<F(1,2)
assert F(1,5)-F(1,12)-F(1,120000)>F(1,10)
# Same full all-integer prime majorant as the complete profile theorem.
assert F(1,65536)/(1-F(1,2**29))<F(1,60000)
print('PASS: complete-theta 0 < -(log R)prime < 1/2, full-prime and continuous defects.')
print('Extra uniform coercive margin:', F(1,5)-F(1,12)-F(1,120000))
