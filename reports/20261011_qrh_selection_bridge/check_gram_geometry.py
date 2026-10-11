"""Exact interface/marked-row bookkeeping; no analytic or RH certification."""

from fractions import Fraction as F
import json
from itertools import combinations
from math import prod


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

# Group absent/inactive marked primes BEFORE taking absolute values.
# This is a finite exact identity; simultaneous source-branch compatibility
# and the infinite cusp bounds are proved in the mathematical text.
norms = (7, 13, 19, 31)
inactive_sum = sum(
    (-1) ** len(indices) * prod(1 - F(1, norms[i]) for i in indices)
    for size in range(len(norms) + 1)
    for indices in combinations(range(len(norms)), size)
)
assert inactive_sum == F(1, prod(norms))

# Reflection exponents in U, q_rm, q_E, q_F, with D=EF.
dual_length = (F(-1), F(2), F(2), F(0))
grouped_mark = (F(0), F(0), F(-1, 2), F(-1))
reflected_piece = add(grouped_mark, scale(F(1, 2), dual_length))
assert reflected_piece == (F(-1, 2), F(1), F(1, 2), F(-1))
assert reflected_piece == add(
    (F(-1, 2), F(1), F(1, 2), F(1, 2)),
    (F(0), F(0), F(0), F(-3, 2)),
)
assert -F(1, 3) - F(1, 2) == -F(5, 6)  # ramified cusp exponent

# Old-marked Euler decompletion: balanced A^(1/3) B^(2/3).
# Vectors are exponents in U, q_D, R(m).
positive_A = (F(1, 2), F(-1), F(0))
reflected_B = (F(-1, 2), F(1, 2), F(1))
flat_balance = add(scale(F(1, 3), positive_A), scale(F(2, 3), reflected_B))
assert flat_balance == (F(-1, 6), F(0), F(2, 3))

# Affine physical exponents as (constant, coefficient of d).
row_positive = (F(5, 12), F(1, 2))
row_reflected = (F(1, 3), F(-2))
row_gain = add(row_positive, scale(F(-1), row_reflected))
assert row_gain == (F(1, 12), F(5, 2))
flat_physical = add(
    scale(F(2, 3), (F(5, 6), F(-2))),
    scale(F(-1, 6), (F(7, 6), F(-1))),
)
assert flat_physical == (F(13, 36), F(-7, 6))
absolute_slot_energy = (F(11, 6), F(-8))
source_R2_energy = (F(5, 6), F(-2))
energy_excess = add(absolute_slot_energy, scale(F(-1), source_R2_energy))
assert energy_excess == (F(1), F(-6))  # nonnegative on 0<=d<=1/6

print(json.dumps({
    "C_squared_norm_X_Y_qR": [str(x) for x in add(scale(2, C_amplitude), domain_count)],
    "pair_support_count_X_Y_qR": [str(x) for x in overlap_count],
    "finite_domain_Gram_energy_target": "7/12",
    "resulting_low_target": "-3/16",
    "formal_high_endpoint_threshold": str(threshold),
    "uniform_marked_piece_U_qE_qF": [str(x) for x in marked_piece],
    "exact_inactive_mark_sum": str(inactive_sum),
    "reflected_piece_U_qrm_qE_qF": [str(x) for x in reflected_piece],
    "old_marked_flat_balance_U_qD_R": [str(x) for x in flat_balance],
    "fixed_row_gain_constant_d": [str(x) for x in row_gain],
    "absolute_slot_energy_excess_constant_d": [str(x) for x in energy_excess],
    "scope": "algebra and local support only; Gram saving and high extension unproved",
}, indent=2))
