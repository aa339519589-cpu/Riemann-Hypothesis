"""Exact algebraic replay of (13) in ODD_VARIATION_PRIME_BOUNDARY.md.

This checks one Gaussian coefficient, not the analytic cutoff argument,
an actual Green eigen-source, the Weil sign, or RH. Uses only the stdlib.
"""

from fractions import Fraction
from math import factorial


def add(p, q, factor=1):
    out = dict(p)
    for term, coefficient in q.items():
        out[term] = out.get(term, Fraction(0)) + factor * coefficient
    return {term: value for term, value in out.items() if value}


def multiply(p, q):
    out = {}
    for (x, b), value in p.items():
        for (y, c), other in q.items():
            term = (x + y, b + c)
            out[term] = out.get(term, Fraction(0)) + value * other
    return out


def gaussian_derivative(p):
    """e^(x^2) d/dx [p(x,b)e^(-x^2)] = p' - 2xp."""
    out = {}
    for (x, b), value in p.items():
        if x:
            out[(x - 1, b)] = out.get((x - 1, b), Fraction(0)) + x * value
        out[(x + 1, b)] = out.get((x + 1, b), Fraction(0)) - 2 * value
    return {term: value for term, value in out.items() if value}


def main():
    p = {(1, 0): Fraction(1), (3, 1): Fraction(-1)}
    derivatives = [p]
    for _ in range(4):
        derivatives.append(gaussian_derivative(derivatives[-1]))
    numerator = add(multiply(derivatives[2], derivatives[2]),
                    multiply(p, derivatives[4]), factor=-1)
    integral = {}
    for (x_power, b_power), value in numerator.items():
        exponent = x_power - 1  # Divide the numerator by x.
        assert exponent >= 1 and exponent % 2 == 1
        j = (exponent - 1) // 2
        # Integral_0^infty x^(2j+1) exp(-2x^2) dx.
        moment = Fraction(factorial(j), 2 ** (j + 2))
        integral[b_power] = integral.get(b_power, Fraction(0)) + value * moment
    integral = {power: value for power, value in integral.items() if value}
    assert integral == {0: Fraction(-2), 1: Fraction(-2), 2: Fraction(2)}
    b = Fraction(2, 3)
    result = sum(value * b ** power for power, value in integral.items())
    assert result == Fraction(-22, 9)
    # The half-Gaussian moments, after division by sqrt(pi), are 1/4 and 3/8.
    assert Fraction(1, 4) / Fraction(3, 8) == b
    print("Exact coefficient: J(b) = 2*b^2 - 2*b - 2")
    print("At b = 2/3: J =", result)
    print("Scope: algebraic coefficient only; no eigen-source or RH verification.")


if __name__ == "__main__":
    main()
