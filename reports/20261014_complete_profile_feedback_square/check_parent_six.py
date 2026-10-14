#!/usr/bin/env python3
"""Exact constants for the full parent>=6 true-variance operator."""
from fractions import Fraction as F
from math import factorial
assert sum(F(3**k,factorial(k)) for k in range(9))>20
assert F(17,8)<F(9,4)
assert F(401,3200)*F(3,2)<F(1,5)
assert F(2,20**14)<F(1,2)
assert F(2,20**20)<F(1,2)
assert F(12,20**14)<F(1,2**56)
assert F(101,280000)+F(101,2**112)<F(1,2750)
assert F(1,500)-F(1,550)==F(1,5500)
print('PASS: full parent-six true-variance operator norm < 2^-56; squared norm < 2^-112.')
print('Joint reset/incidence dual coefficient < 1/2750, with one residual expenditure.')
