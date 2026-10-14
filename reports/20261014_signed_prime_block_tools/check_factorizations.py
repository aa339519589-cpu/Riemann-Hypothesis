#!/usr/bin/env python3
"""Exact rational checks for the finite algebra and prime-two mass obstruction.

No floating-point result is used in an assertion. The finite algebra checks
are reproducible sanity checks, not substitutes for the general proofs.
The prime-two sign section supplies the rational inequalities used in the
analytic infinite-tail proof.
"""
from fractions import Fraction as F
from math import factorial
import json
import platform


def inv(matrix):
    n = len(matrix)
    z = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if z[j][i])
        z[i], z[pivot] = z[pivot], z[i]
        c = z[i][i]
        z[i] = [x / c for x in z[i]]
        for j in range(n):
            if j != i:
                c = z[j][i]
                z[j] = [x - c * y for x, y in zip(z[j], z[i])]
    return [row[n:] for row in z]


def quad(matrix, vector):
    return sum(vector[i] * matrix[i][j] * vector[j]
               for i in range(len(vector)) for j in range(len(vector)))


# Finite killed chain, with a genuine terminal conductance c[n-1].
n = 6
w = [F(j + 2, j + 5) for j in range(n)]
c = [F(j + 1, 3 * j + 7) for j in range(n)]
D = [w[j] + c[j] + (c[j - 1] if j else 0) for j in range(n)]
R = [[D[i] if i == j else (-c[min(i, j)] if abs(i-j) == 1 else F(0))
      for j in range(n)] for i in range(n)]
p = [F(1), D[0] / c[0]]
for j in range(1, n):
    p.append((D[j] * p[j] - c[j-1] * p[j-1]) / c[j])
aa = [c[j] * p[j] * p[j+1] for j in range(n)]
g = [[p[i] * p[j] * sum((1/aa[k] for k in range(max(i, j), n)), F(0))
      for j in range(n)] for i in range(n)]
assert g == inv(R)
Q = [F(-1 if j % 2 else j+1, j+2) for j in range(n)]
assert quad(g, Q) == sum(sum(p[j]*Q[j] for j in range(k+1))**2/aa[k]
                         for k in range(n))
r = [F(j-2, j+1) for j in range(n)] + [F(0)]
assert quad(R, r[:-1]) == sum(aa[j]*(r[j]/p[j]-r[j+1]/p[j+1])**2
                              for j in range(n))

# Hierarchical forward variance and two-population reflected variance.
a = F(1, 2)
q = [F(j+2, j+4)*a**j for j in range(n)]
b = [F(2*j+1, j+3)*a**j for j in range(n)]
u = [F(j*j-3, j+1) for j in range(n)]
v = [F(j+2, 2*j+3) for j in range(n)]
M, V = [], []
for m in range(n):
    mass = sum(q[m:])
    mean = sum(q[j]*u[j] for j in range(m, n))/mass
    M.append(mass)
    V.append(sum(q[j]*(u[j]-mean)**2 for j in range(m, n)))
delta = [F(1)] + [a**(-2*m)-a**(-2*(m-1)) for m in range(1, n)]
forward = sum(q[i]*q[j]*a**(-2*i)*(u[i]-u[j])**2
              for i in range(n) for j in range(i+1, n))
assert forward == sum(delta[m]*M[m]*V[m] for m in range(n))
A, B = sum(q), sum(b)
mu = sum(qj*uj for qj, uj in zip(q, u))/A
nu = sum(bj*vj for bj, vj in zip(b, v))/B
Va = sum(qj*(uj-mu)**2 for qj, uj in zip(q, u))
Vb = sum(bj*(vj-nu)**2 for bj, vj in zip(b, v))
reflection = sum(q[i]*b[j]*(u[i]-v[j])**2 for i in range(n) for j in range(n))
assert reflection == B*Va+A*Vb+A*B*(mu-nu)**2

# Geometric covariance, including the signed rank-one reflection term.
T = [[a**abs(i-j) for j in range(n)] for i in range(n)]
for sign in [-1, 1]:
    block = [[T[i][j]+sign*a*a**(i+j) for j in range(n)] for i in range(n)]
    square = (1+sign*a)*sum(a**j*u[j] for j in range(n))**2
    square += (1-a*a)*sum(sum(a**(j-m)*u[j] for j in range(m, n))**2
                           for m in range(1, n))
    assert quad(block, u) == square

# Exact elementary certificates in the proof H_2(3 log 2/4) < -2/3.
def atan_bounds(x, n):
    s = sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n+1)), F(0))
    nxt = (-1)**(n+1)*x**(2*n+3)/F(2*n+3)
    return min(s, s+nxt), max(s, s+nxt)

lo5, hi5 = atan_bounds(F(1, 5), 10)
lo239, hi239 = atan_bounds(F(1, 239), 3)
pi_lo, pi_hi = 16*lo5-4*hi239, 16*hi5-4*lo239
assert pi_lo > F(3141, 1000) and pi_hi < F(22, 7)
sq_lo, sq_hi = F(14142, 10000), F(14143, 10000)
assert sq_lo**2 < 2 < sq_hi**2
assert F(111, 25) < pi_lo*sq_lo < pi_hi*sq_hi < F(89, 20)
assert F(222, 25) < 2*pi_lo*sq_lo < 2*pi_hi*sq_hi < F(889, 100)
assert F(13, 10)**8 > 8  # 2^(3/8) < 13/10.
assert F(7, 10)**2 < F(1, 2)  # 2^(-1/2) > 7/10.
assert pi_hi**3 < 32

U0, U1, V0, V1 = F(222,25), F(889,100), F(111,25), F(89,20)
def exp_partial(x, n):
    return sum((x**k/F(factorial(k)) for k in range(n+1)), F(0))
assert exp_partial(U0, 40) > 7000
assert exp_partial(V1, 20)+V1**21/F(factorial(21))/(1-V1/F(22)) < 90
# Theta-index tail at j=0 and all translated tails j>=1.
assert 8192*2*64*F(1, 2**32) < F(1, 1000)
assert F(1, 2**11) < F(1, 1000)
upper = F(13,10)*(8*U1**3-30*U0**2+15*U1)/7000+F(2,1000)
lower = F(7,10)*(8*V0**3-30*V1**2+15*V0)/90
assert upper < F(2,3) and lower > F(4,3)
print(json.dumps({
    'status': 'all exact rational assertions passed',
    'python': platform.python_version(),
    'checks': ['finite Green prefix factorization', 'finite ground transform',
               'hierarchical forward variance', 'reflected two-population variance',
               'AR1 signed covariance', 'prime-two strict mass-imbalance bounds'],
    'prime_two_H_upper_rational': str(upper-lower),
    'prime_two_H_upper_decimal_for_display_only': float(upper-lower)
}, indent=2))
