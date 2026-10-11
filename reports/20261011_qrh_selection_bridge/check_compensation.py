#!/usr/bin/env python3
"""Exact normalization and local support identities in COMPENSATION.md."""
from fractions import Fraction as F
import json

# Exponent vectors for q_r, q_s, X, Y, q_b in that order.
def add(*vectors):
    return tuple(sum(entries, F(0)) for entries in zip(*vectors))


def scale(c, vector):
    return tuple(F(c) * entry for entry in vector)


r, s, x, y, b = (
    tuple(F(int(i == j)) for i in range(5)) for j in range(5)
)
s0, x0, y0 = (add(v, scale(-1, r)) for v in (s, x, y))
prefactor = add(scale(F(-3, 2), r), scale(-1, y0),
                scale(F(-1, 2), add(b, s0, x0)),
                scale(F(-1, 2), s0))
common = add(scale(-1, y), scale(F(-1, 2), add(b, s, x)),
             scale(F(-1, 2), s))
assert prefactor == add(r, common)
assert add(s0, scale(-1, y0)) == add(s, scale(-1, y))
# q_m0=q_m/q_r^2; subtract common q_m from both sides.
assert add(scale(-2, r), scale(-1, b), scale(-1, s0), scale(-1, x0)) == \
       add(scale(-1, b), scale(-1, s), scale(-1, x))

# Fixed-character phase exponents: xi(r)^(1-2), chi_r(b)^(-1).
assert 1 - 2 == -1

# These are the three exhaustive valuation classes, not a finite height cut.
classes = ('v=0', 'v=1', 'v>=2')
p = (1, 0, 0)
q = (0, 0, 1)
mul = lambda a, b: tuple(x * y for x, y in zip(a, b))
assert mul(p, p) == p
assert mul(q, q) == q
assert mul(p, q) == (0, 0, 0)
signed = tuple(x - y for x, y in zip(p, q))
allowed = tuple(x + y for x, y in zip(p, q))
assert mul(signed, signed) == allowed

print(json.dumps({
    'normalization_exponents_qr_qs_X_Y_qb': [str(v) for v in prefactor],
    'extra_factor_after_common_normalization': 'q_r',
    'valuation_classes': classes,
    'marked_projection': p,
    'rescaled_projection': q,
    'cross_projection': mul(p, q),
    'signed_projection_squared': mul(signed, signed),
}, indent=2))
