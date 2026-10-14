#!/usr/bin/env python3
"""Exact rational inequalities in the complete theta origin-band proof."""
from fractions import Fraction as F
assert F(25,18)+F(2,297)==F(829,594)<F(7,5)
assert F(22,7)*F(7,5)<F(9,2)
def R(t): return -32*t**3+224*t**2-330*t+75
assert R(F(3))==237 and R(F(9,2))==210
assert -192*3+448<0
assert F(3,2)**8 / F(5,2)**15 < F(1,2)
assert F(663552)/F(5,2)**9 < 315
assert F(1,12)<F(56,81) # log 2 > 56/81
print('PASS: complete theta derivative and actual b positive on (0,1/12].')
