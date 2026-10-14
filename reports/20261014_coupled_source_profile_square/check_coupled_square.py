#!/usr/bin/env python3
from fractions import Fraction as F
c=F(124633,125000)
assert 1-c==F(367,125000)>0
margin=F(1,5)-F(1,12)-F(1,120000)-F(23,200)
assert margin==F(199,120000)>0
# Exact rational algebra of the scalar square completion.
for u,a,lam,sig in [(F(2),F(-3),F(7,3),F(5,2)),(F(-4,3),F(2,5),F(3),F(1,7))]:
    assert lam*sig*a*a+2*a*u == lam*sig*(a+u/(lam*sig))**2-u*u/(lam*sig)
print('PASS: coupled square coefficients367/125000 and199/120000, exact cross normalization.')
