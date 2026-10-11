"""Exact rational ledger for the noncubic Gauss-twist growth bound.

This checks interpolation powers and mask costs, not the automorphic theorem,
the Phragmen--Lindelof argument, or RH. All polynomial coefficients are exact.
"""
from fractions import Fraction as F


def add(a, b):
    n = max(len(a), len(b))
    return [((a[i] if i < len(a) else 0)
             + (b[i] if i < len(b) else 0)) for i in range(n)]


def scale(a, c):
    return [c*x for x in a]


def multiply(a, b):
    result = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def evaluate(a, x):
    return sum(c*x**i for i, c in enumerate(a))


# Variable is epsilon; delta=epsilon/4 and sigma_min=1/2+epsilon.
delta = [F(0), F(1, 4)]
left_modulus_power = add([F(3, 2)], scale(delta, F(2)))
strip_width = add([F(1)], scale(delta, F(2)))
right_minus_sigma = add(add([F(1, 2)], delta), [F(0), F(-1)])
assert left_modulus_power == [F(3, 2), F(1, 2)]
assert strip_width == [F(1), F(1, 2)]
assert right_minus_sigma == [F(1, 2), F(-3, 4)]

numerator = multiply(left_modulus_power, right_minus_sigma)
deficit_numerator = add(scale(strip_width, F(3, 4)),
                        scale(numerator, F(-1)))
assert deficit_numerator == [F(0), F(5, 4), F(3, 8)]
# Positive coefficients and positive strip_width prove the deficit is positive
# for every epsilon>0; this is a polynomial certificate, not a sampled grid.
assert all(c >= 0 for c in deficit_numerator)
assert all(c > 0 for c in deficit_numerator[1:])

# Over 0<epsilon<1/2 the affine endpoint bounds give height degree <=5/2,
# width <=5/4, and positive right-minus-sigma >=1/8.
assert evaluate(add([F(2)], scale(delta, F(4))), F(1, 2)) == F(5, 2)
assert evaluate(strip_width, F(1, 2)) == F(5, 4)
assert evaluate(right_minus_sigma, F(1, 2)) == F(1, 8)

mask_power = add([F(3, 4)], scale([F(1, 2), F(1)], F(-1)))
assert mask_power == [F(1, 4), F(-1)]  # <=1/4 for epsilon>=0.
assert F(3, 2) == F(1, 2)+F(1)  # primitive Fourier size times unit count.
assert F(5, 6)+F(1, 2) == F(4, 3)  # normalized/unnormalized pole shift.
print('ALL_PASS exact interpolation deficit, strip/height margins, mask cost,')
print('and normalization ledger; analytic assertions are separately reviewed.')
