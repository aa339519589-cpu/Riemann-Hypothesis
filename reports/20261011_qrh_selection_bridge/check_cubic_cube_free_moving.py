#!/usr/bin/env python3
"""Exact Fraction certificate for the cube-free Gauss interpolation ledger.

This checks the algebraic interpolation margins and the full stated epsilon
range; it does not inspect or test an implementation of the analytic argument.
"""

from fractions import Fraction as F


def add(a, b):
    n = max(len(a), len(b))
    return tuple((a[i] if i < len(a) else F(0))
                 + (b[i] if i < len(b) else F(0)) for i in range(n))


def scale(c, a):
    return tuple(c * x for x in a)


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)


def sub(a, b):
    return add(a, scale(F(-1), b))


ONE = (F(1),)
EPS = (F(0), F(1))
half = (F(1, 2),)

# theta = (b - (1/2+epsilon))/(b+h), with h=epsilon/4 and b=1+h.
h = scale(F(1, 4), EPS)
b = add(ONE, h)
sigma0 = add(half, EPS)
theta_num = sub(half, scale(F(3, 4), EPS))
width = add(b, h)
assert sub(b, sigma0) == theta_num
assert width == add(ONE, scale(F(1, 2), EPS))

# The left-boundary exponents after h=eta=epsilon/4.
a_l = add((F(3, 2),), scale(F(1, 2), EPS))
a_1 = add(half, scale(F(3, 4), EPS))
a_2 = add(ONE, scale(F(3, 4), EPS))

def deficit_numerator(target, exponent):
    # target - exponent*theta, with positive common denominator `width`.
    return sub(scale(target, width), mul(exponent, theta_num))


expected = (
    (F(3, 4), deficit_numerator(F(3, 4), a_l),
     (F(0), F(5, 4), F(3, 8))),
    (F(1, 4), deficit_numerator(F(1, 4), a_1),
     (F(0), F(1, 8), F(9, 16))),
    (F(1, 2), deficit_numerator(F(1, 2), a_2),
     (F(0), F(5, 8), F(9, 16))),
)
for _target, actual, exact in expected:
    assert actual == exact, (actual, exact)
    # Every coefficient is nonnegative and at least one positive, hence the
    # numerator is strictly positive for every epsilon in (0, 1/4).
    assert all(c >= 0 for c in actual) and any(c > 0 for c in actual)

# Exact endpoint/range checks for all 0 < epsilon < 1/4:
#   h=eta=epsilon/4 lies in (0,1/16);
#   sigma0 < b=1+h, so the interpolation interval is nonempty;
#   theta is positive; and the left gamma degree 2+4h=2+epsilon is < 3.
eps_max = F(1, 4)
assert F(0) < eps_max
assert eps_max / 4 == F(1, 16) < F(1, 8)
assert F(1, 2) - F(3, 4) * eps_max == F(5, 16) > 0  # interval and theta
assert F(2) + eps_max == F(9, 4) < F(3)
assert width[0] == F(1) and width[1] > 0
assert all(c >= 0 for a in (a_l, a_1, a_2) for c in a)

print("exact interpolation ledger verified for every 0 < epsilon < 1/4")
