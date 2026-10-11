"""Exact scalar/exponent checks only; does not certify analytic cancellation."""

from fractions import Fraction as F
from itertools import product
import json


def add(*vectors):
    return tuple(sum(values, F(0)) for values in zip(*vectors))


def scale(k, vector):
    return tuple(k * x for x in vector)


# Physical exponents represented as (constant, coefficient of d).
Q = (F(5, 6), F(-2))
Y = (F(23, 48), F(-1))
P = (F(1, 6), F(-1))
X = (F(17, 48), F(-1))
Z = (F(1), F(0))
old = add(Q, scale(-F(3, 2), Y), scale(F(1, 2), add(Z, P, scale(-1, X))))
assert old == (F(25, 48), F(-1, 2))
gain = scale(F(1, 8), add(Z, scale(-1, Y)))
assert gain == (F(25, 384), F(1, 8))
new = add(old, scale(-1, gain))
assert new == (F(175, 384), F(-5, 8))
before_tuples = add(new, scale(-F(1, 2), Q))
assert before_tuples == (F(5, 128), F(3, 8))
compensated = add(before_tuples, (F(0), F(-1, 2)))
assert compensated == (F(5, 128), F(-1, 8))
assert F(5, 128) - (-F(3, 16)) == F(29, 128)

# Exact LCM/Mobius identity covers every local membership combination.
for in_e, in_D in product((0, 1), repeat=2):
    lcm_exponent = max(in_e, in_D)
    leftover_exponent = in_D * (1 - in_e)
    assert (-1) ** (in_e + lcm_exponent) == (-1) ** leftover_exponent

# Mertens line sigma=7/8+delta: q_L^-1 (C1/q_L)^(sigma-1).
# The q_L exponent is -sigma, so the delta sign MUST be negative.
for delta in (F(1, 10000), F(1, 1000), F(1, 20), F(31, 250)):
    sigma = F(7, 8) + delta
    kappa = 1 - sigma
    assert 0 < kappa < F(1, 8)
    assert -1 - (sigma - 1) == -F(7, 8) - delta
    # After e mass and the g cancellation, the n0 branches have weights:
    E_exponent = -2 + 4 * kappa
    F_exponent = -1 + 2 * kappa
    assert E_exponent <= -F(3, 2)
    assert F_exponent <= -F(3, 4)
    assert -5 + 6 * kappa <= -F(17, 4)

assert -2 + 4 * F(1, 8) == -F(3, 2)
assert -1 + 2 * F(1, 8) == -F(3, 4)
assert -5 + 6 * F(1, 8) == -F(17, 4)
# Decompletion tail cutoff q_a>(Z/Y')^(1/6); sum q_a^-5 ~ cutoff^-4.
assert F(4, 6) == F(2, 3) > F(1, 8)

# Common-column comparison includes the column-assigned prime-slot cost.
peak_V, peak_L, peak_P = F(13, 48), F(23, 24), F(1, 6)
assert peak_L - peak_P == F(19, 24)
unmarked_bound = peak_V / 2 - peak_L / 8
marked_bound = peak_V / 2 - (peak_L - peak_P) / 8
assert unmarked_bound == F(1, 64)
assert marked_bound == F(7, 192)
critical_kappa = (peak_V / 2) / (peak_L - peak_P)
assert critical_kappa == F(13, 76)
assert 1 - critical_kappa == F(63, 76)
assert -F(1, 32) - (-F(3, 16)) == F(5, 32)

print(json.dumps({
    "old_quadratic_S_constant_d": [str(x) for x in old],
    "gain_constant_d": [str(x) for x in gain],
    "improved_quadratic_S_constant_d": [str(x) for x in new],
    "improved_compensated_constant_d": [str(x) for x in compensated],
    "remaining_quadratic_gap_at_d0": "29/128",
    "square_layer_exponent": "-17/4",
    "peak_Mertens_bound_exponent_with_slots": str(marked_bound),
    "peak_Mertens_kappa_threshold": str(critical_kappa),
    "later_bilinear_gap": "5/32",
    "scope": "exact bookkeeping only; joint-weight and character arguments require proof",
}, indent=2))
