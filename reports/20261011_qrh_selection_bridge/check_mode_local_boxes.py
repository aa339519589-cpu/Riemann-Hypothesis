#!/usr/bin/env python3
"""Exact mode-range inequalities; does not certify the analytic detector."""
from fractions import Fraction as F


eta = F(7, 500)
tau0 = F(1, 500)
zeta_max = F(1, 100_000)
height_limit = F(1, 50)
mode_height = eta + tau0
mellin_height = zeta_max + tau0
height_gap = height_limit - mode_height

alpha0 = F(47, 300)
p2 = 4 * alpha0 * (12 * alpha0 - 5) / (
    3 * (2 * alpha0 - 1) * (12 * alpha0 + 5)
)

assert mode_height == F(2, 125)
assert mellin_height == F(201, 100_000)
assert mode_height > mellin_height
assert height_gap == F(1, 250) > 0
assert p2 == F(611, 4429)
assert 0 < p2 < 1
assert F(3, 8) * 2 * zeta_max == F(3, 4) * zeta_max

print("PASS: all-mode height slack and center p2 are exact")
