"""Exact finite norm-character and Gauss-transform checks in Z[omega]/(4).

This verifies the finite interface and residue projection, not the imported
automorphic continuation theorem or a complete RH probe estimate.
"""
from itertools import product

RESIDUES = list(product(range(4), repeat=2))
I_POWERS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
OMEGA_POWERS = [(1, 0), (0, 1), (-1, -1)]


def ring_product(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c-b*d)


def residue_product(x, y):
    return tuple(v % 4 for v in ring_product(x, y))


def norm_character(x):
    a, b = x
    value = (a*a-a*b+b*b) % 4
    return 0 if value % 2 == 0 else (1 if value == 1 else -1)


def gauss(h, trace=False):
    result = [0, 0]
    for u in RESIDUES:
        value = norm_character(u)
        a, b = ring_product(h, u)
        exponent = (2*a-b) if trace else b
        re, im = I_POWERS[exponent % 4]
        result[0] += value*re
        result[1] += value*im
    return tuple(result)


def cubic_exponent(x):
    a, b = (v % 2 for v in x)
    return {(1, 0): 0, (0, 1): 1, (1, 1): 2}[(a, b)]


for x, y in product(RESIDUES, repeat=2):
    assert norm_character(residue_product(x, y)) == (
        norm_character(x)*norm_character(y))
assert norm_character((1, 0)) == 1
assert norm_character((1, 2)) == -1  # lambda=1+2*omega; primitive mod (4).

units = [x for x in RESIDUES if norm_character(x)]
assert len(units) == 12
for h in RESIDUES:
    assert gauss(h) == (4*norm_character(h), 0)
    assert gauss(h, trace=True) == (-4*norm_character(h), 0)

matrix = [[gauss((c, d))[0] for c in range(4)] for d in range(4)]
assert matrix == [[0, 4, 0, 4], [4, 4, -4, -4],
                  [0, -4, 0, -4], [4, -4, -4, 4]]

# Every cubic character on (O/(4))^* descends to F_4^*, hence the primitive
# quadratic character is orthogonal to it. Coefficients use Z[omega], not floats.
for k in range(3):
    total = [0, 0]
    for h in units:
        a, b = OMEGA_POWERS[(k*cubic_exponent(h)) % 3]
        value = norm_character(h)
        total[0] += value*a
        total[1] += value*b
    assert total == [0, 0]

# Pairwise cancellation on each fixed nonzero residue class modulo (2).
for x in [(1, 0), (0, 1), (1, 1)]:
    assert sum(norm_character(h) for h in units
               if tuple(v % 2 for v in h) == x) == 0

print('Exact checks passed: 16 Gauss classes, primitive support, both additive')
print('conventions, and all three cubic finite-character projections.')
