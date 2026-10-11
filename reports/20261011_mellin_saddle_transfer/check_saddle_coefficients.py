"""Exact algebra for the theta/Gamma saddle transfer; no RH certification."""

from fractions import Fraction as F
import json


def gamma_integer_shift(z, shift):
    """Gamma(z+shift)/Gamma(z) by recurrence, for integer shift."""
    result = F(1)
    if shift >= 0:
        for j in range(shift):
            result *= z + j
    else:
        for j in range(1, -shift + 1):
            result /= z - j
    return result


def add(*polys):
    answer = {}
    for poly in polys:
        for degree, coeff in poly.items():
            answer[degree] = answer.get(degree, F(0)) + coeff
    return {degree: coeff for degree, coeff in answer.items() if coeff}


def scale(poly, factor):
    return {degree: coeff * factor for degree, coeff in poly.items() if coeff * factor}


# Gamma(k+2), Gamma(k+1) coefficients in the exact average.
# 2 k(k+1) - 3k = k(2k-1), as a polynomial identity.
assert add({2: F(2), 1: F(2)}, {1: F(-3)}) == {2: F(2), 1: F(-1)}

# Signed first logarithmic moment and the quadratic Taylor coefficient.
# A_k = 1 + O(k^-1), B_k = O(k^-1), so the k^-1 terms
# are those of Gamma(k+2); the constant q term cancels exactly.
first_log_coefficient = (F(2) - F(1, 2)) / 2
quadratic_taylor_coefficient = F(1, 4) / 2
assert first_log_coefficient == F(3, 4)
assert quadratic_taylor_coefficient == F(1, 8)
assert 2 * first_log_coefficient == F(3, 2)  # k = sigma/2
assert 2 * quadratic_taylor_coefficient == F(1, 4)

# Exponential monomial e^(r x): first correction must also agree with
# the shifted G(sigma+r)/G(sigma) calculation from the exact Mellin integral.
# Coefficients below are polynomials in r for the 1/k correction.
gamma_shift_coefficient = {2: F(1, 8), 1: F(-1, 4)}
quadratic_prefactor_coefficient = {1: F(1)}
from_shifted_G = add(gamma_shift_coefficient, quadratic_prefactor_coefficient)
from_taylor = {1: first_log_coefficient, 2: quadratic_taylor_coefficient}
assert from_shifted_G == from_taylor

# Recurrence checks use exact rational k, without Gamma floating point values.
recurrence_checks = 0
for k in (F(9, 2), F(7), F(21, 2), F(20)):
    A = 2 * (k + 1) / (2 * k - 1)
    B = 3 / (2 * k - 1)
    assert A - B == 1
    for u in range(-3, 4):
        gamma_average = (
            A * gamma_integer_shift(k + 2, u)
            - B * gamma_integer_shift(k + 1, u)
        )
        shifted_G = (
            (k + u) * (2 * (k + u) - 1)
            / (k * (2 * k - 1)) * gamma_integer_shift(k, u)
        )
        assert gamma_average == shifted_G
        recurrence_checks += 1

# c = 1/2-alpha and sigma = 2pi exp(2x): power beta=-c/2.
beta = {0: F(-1, 4), 1: F(1, 2)}
assert beta[0] + beta[1] * F(3, 8) == F(-1, 16)
assert beta[0] == F(-1, 4)

print(json.dumps({
    "normalization": "2k(k+1)-3k=k(2k-1)",
    "first_correction_q_prime": str(2 * first_log_coefficient),
    "first_correction_q_second": str(2 * quadratic_taylor_coefficient),
    "integer_gamma_recurrence_checks": recurrence_checks,
    "exact_power_order": "-1/4+alpha/2",
    "scope": "exact algebra only; analytic remainders and RH inputs not certified",
}, indent=2))
