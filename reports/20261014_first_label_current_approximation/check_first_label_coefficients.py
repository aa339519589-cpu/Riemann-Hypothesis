#!/usr/bin/env python3
"""Exact rational checks for the full divisor/reset first-label comparison."""
from fractions import Fraction as F

score_variance_majorant = F(23328, 4096) / (1-F(36, 16**5))
assert score_variance_majorant == F(1492992,262135)
assert score_variance_majorant < 6
posterior_derivative_majorant = F(864,4096)/(1-F(27,2*16**5))
assert posterior_derivative_majorant < F(211,1000)
assert F(81,16) / 16**20 < F(1,2)
assert F(32,16**12)*2 == F(1,2**42)
assert 3*F(1,2**42) < F(13,400)
assert 4*F(1,2**42) < F(13,400)
assert F(13,600)+F(1,100) == F(19,600) < F(13,400)
print('PASS: complete rational score, divisor, and combined-energy coefficients')
print('score_variance_majorant =',score_variance_majorant)
print('posterior_derivative_majorant =',posterior_derivative_majorant)
print('combined_coefficient = 13/400')
