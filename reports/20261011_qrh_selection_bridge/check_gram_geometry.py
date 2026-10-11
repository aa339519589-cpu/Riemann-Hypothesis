"""Exact bookkeeping for GRAM_INTERFACE and HIGH_SIDE_SCOPE, not analytic bounds."""

from fractions import Fraction as F
import json


def add(*vectors):
    return tuple(sum(entries, F(0)) for entries in zip(*vectors))


def scale(factor, vector):
    return tuple(factor * value for value in vector)


# Exponents in X, Y, q_R. The actual arithmetic row is never replaced.
C_amplitude = (F(-1, 2), F(-2), F(0))
domain_count = (F(1), F(2), F(0))
assert add(scale(2, C_amplitude), domain_count) == (F(0), F(-2), F(0))
overlap_count = (F(1), F(2), F(-3))
assert overlap_count == add((F(0), F(1), F(-1)), (F(1), F(1), F(-2)))
lx, ly, ell = F(17, 48), F(23, 48), F(1, 6)
assert lx + 2 * ly == F(21, 16)
assert ly - 2 * ell == F(7, 48)
assert lx + ly - 4 * ell == F(1, 6)
assert -ly + F(7, 24) == F(-3, 16)
assert 2 * F(7, 24) == F(7, 12)

# Three classes v=0, v=1, v>=2 cover every nonnegative valuation.
classes = (0, 1, 2)
marked = lambda v: int(v == 0)
rescaled = lambda v: int(v >= 2)
assert all(marked(v) * rescaled(v) == 0 for v in classes)
# Different primes can satisfy opposite states: this is compatibility only.
assert marked(0) * rescaled(2) == 1

# Original positive-Delta high endpoint and its formal zero threshold.
h = F(13, 16)
assert 1 - h / 4 == F(51, 64)
threshold = -F(49, 440640) / (1 - h / 4)
assert threshold == -F(49, 351135)
assert -F(49, 440640) - F(51, 64) * threshold == 0

# Uniform marked row: exponent vectors in U, q_E, q_F, with D=EF.
marked_prefactor = (F(0), F(-1, 2), F(-1))
residual_scale = (F(1), F(-1), F(-3))
marked_piece = add(marked_prefactor, scale(F(1, 2), residual_scale))
assert marked_piece == (F(1, 2), F(-1), F(-5, 2))
assert marked_piece == add((F(1, 2), F(-1), F(-1)), (F(0), F(0), F(-3, 2)))

print(json.dumps({
    "C_squared_norm_X_Y_qR": [str(x) for x in add(scale(2, C_amplitude), domain_count)],
    "pair_support_count_X_Y_qR": [str(x) for x in overlap_count],
    "finite_domain_Gram_energy_target": "7/12",
    "resulting_low_target": "-3/16",
    "formal_high_endpoint_threshold": str(threshold),
    "uniform_marked_piece_U_qE_qF": [str(x) for x in marked_piece],
    "scope": "algebra and local support only; Gram saving and high extension unproved",
}, indent=2))
