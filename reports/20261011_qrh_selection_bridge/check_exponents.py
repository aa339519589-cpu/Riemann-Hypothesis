#!/usr/bin/env python3
"""Exact rational identities in REPORT.md; no numerical zero tests."""
from fractions import Fraction as F
import json


def add(*polys):
    """Affine polynomials in (b, ell, d), stored as (1, b, ell, d)."""
    return tuple(sum(values, F(0)) for values in zip(*polys))


def scale(value, poly):
    return tuple(F(value) * coefficient for coefficient in poly)


one, b, ell, d = (
    tuple(F(int(i == j)) for i in range(4)) for j in range(4)
)
lx = scale(F(1, 2), add(one, scale(-1, b), scale(-1, ell)))
h = add(one, ell, scale(-1, lx))
boundary = add(one, scale(F(-1, 6), h), scale(F(1, 12), b))
assert boundary == add(scale(F(11, 12), one), scale(F(-1, 4), ell))

# Each boundary excess is a positive multiple of the named length condition.
shortest_length = add(lx, scale(-1, ell))
shortest_boundary = add(scale(F(5, 6), one), scale(F(1, 12), b))
assert add(boundary, scale(-1, shortest_boundary)) == scale(F(1, 6), shortest_length)
base_boundary = add(scale(F(2, 3), one), scale(F(1, 4), b))
assert add(boundary, scale(-1, base_boundary)) == scale(F(1, 2), lx)

fixed_b, fixed_h, fixed_ell = F(1, 8), F(13, 16), F(1, 6)
fixed_lx, fixed_ly = F(17, 48), F(23, 48)
assert 2 * fixed_lx + fixed_b + fixed_ell == 1
assert fixed_ly == fixed_lx + fixed_b
assert fixed_h == 1 + fixed_ell - fixed_lx
low = fixed_lx / 2 + fixed_b / 12
signal_offset = fixed_lx / 2 - 1 + fixed_h / 6
assert low == F(3, 16)
assert signal_offset == F(-11, 16)
assert F(7, 8) + signal_offset == low
critical_low = F(1, 2) + signal_offset
assert critical_low == F(-3, 16)
assert low - critical_low == F(3, 8)

energy_a = add(scale(F(3, 8), one), scale(-1, d))
energy_b = add(scale(F(5, 6), one), scale(-2, d))
cs = scale(F(1, 2), add(energy_a, energy_b))
assert cs == add(scale(F(29, 48), one), scale(F(-3, 2), d))
target = add(scale(F(11, 48), one), scale(F(-1, 2), d))
saving = add(cs, scale(-1, target))
assert saving == add(scale(F(3, 8), one), scale(-1, d))
q_inverse_half = add(scale(F(-5, 12), one), d)
total = add(q_inverse_half, target, d, scale(F(-3, 2), d))
assert total == scale(F(-3, 16), one)
assert F(3, 8) - fixed_ell == F(5, 24)

strip = F(7, 8) - F(1, 2)
tail_decay = F(1, 2) - strip
mellin_decay = tail_decay / 2
assert tail_decay == F(1, 8)
assert mellin_decay == F(1, 16)

print(json.dumps({
    "exact_affine_identities": "verified over Q[b, ell, d]",
    "tail_decay": str(tail_decay),
    "mellin_decay": str(mellin_decay),
    "existing_low_exponent": str(low),
    "critical_low_exponent": str(critical_low),
    "required_total_saving": str(low - critical_low),
    "correlation_saving_range": [str(F(5, 24)), str(F(3, 8))],
}, indent=2))
