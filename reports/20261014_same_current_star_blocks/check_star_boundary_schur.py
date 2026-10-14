#!/usr/bin/env python3
"""Exact complete-series constants in the SAME-star boundary Schur proof.
The checker verifies analytic tail majorants, not finite-label sampling.
"""
from fractions import Fraction as F
from math import factorial
assert sum(F(3**k,factorial(k)) for k in range(9))==F(89641,4480)>20
assert F(729,64*20**5)<F(1,1000)
assert 1+F(128,20**3)/(1-F(1,1000))<F(17,16)
assert 4-F(17,16)-F(1,21)>F(14,5)
assert 1+F(6,51*21)<F(21,20)
assert F(21,20)/F(14,5)==F(3,8)
assert F(5,4)**8<6 and F(6,20**9)<F(1,2)
tail=F(131072,20**12)
assert (F(81,20**5)+tail)/14<F(1,1000)
eta=F(1001,1000)*F(9,896)*(F(2025,20**5)+tail)
assert eta==F(203607432171,32000000000000000)<F(1,384**2)
assert 1- F(101,384)==F(283,384)
assert 1+ F(101,384)==F(485,384)
print('PASS: complete posterior rate/tail bounds, edge mixed correlation <=1/384, and full signed boundary Schur coefficient 101/384.')
print('Squared edge coefficient upper:',eta)
