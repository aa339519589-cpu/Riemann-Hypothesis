#!/usr/bin/env python3
"""Finite-rank linear-algebra sanity check; no RH or theta computation."""
from fractions import Fraction as F

def rank(rows):
    a = [[F(x) for x in row] for row in rows]
    if not a:
        return 0
    n = len(a[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, len(a)) if a[i][c]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        z = a[r][c]
        a[r] = [v / z for v in a[r]]
        for i in range(len(a)):
            if i != r:
                z = a[i][c]
                a[i] = [a[i][j] - z * a[r][j] for j in range(n)]
        r += 1
        if r == len(a):
            break
    return r

for d in range(1, 8):
    for extra in range(1, 8):
        M = d + extra
        matrices = [
            [[int(i == j) for j in range(M)] for i in range(d)],
            [[(i+1)**j for j in range(M)] for i in range(d)],
            [[0 for j in range(M)] for i in range(d)],
        ]
        for a in matrices:
            assert M - rank(a) >= extra

# A|_{span(e_{2j-1}+e_{2j})} has zero quadratic form,
# yet its full spectrum is contained in {-1,+1} with no zero.
for r in range(1, 10):
    sign = [s for _ in range(r) for s in (1, -1)]
    for c in ([1]*r, list(range(1, r+1))):
        v = [z for z in c for _ in range(2)]
        q = sum(sign[i]*v[i]*v[i] for i in range(2*r))
        assert q == 0 and all(s != 0 for s in sign)
print("PASS: rational rank-nullity examples and exact isotropic countermodel")
