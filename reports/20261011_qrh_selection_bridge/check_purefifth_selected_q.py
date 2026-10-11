"""Exact exponent certificate; this is not a verification of the analytic inputs."""
from fractions import Fraction as F
from math import comb


def evaluate(coefficients, x):
    return sum(c * x**i for i, c in enumerate(coefficients))


def add(*polynomials):
    size = max(map(len, polynomials))
    out = [sum(p[i] if i < len(p) else 0 for p in polynomials)
           for i in range(size)]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(p, c):
    return [c*x for x in p]


def multiply(p, q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return out


def derivative(p):
    return [i*p[i] for i in range(1, len(p))]


def bernstein(coefficients, lo, hi):
    degree = len(coefficients) - 1
    power = [
        sum(coefficients[j] * comb(j, k) * lo**(j-k) * (hi-lo)**k
            for j in range(k, degree+1))
        for k in range(degree+1)
    ]
    return [sum(power[k] * F(comb(j, k), comb(degree, k))
                for k in range(j+1)) for j in range(degree+1)]


def density(a):
    if a <= F(1, 3):
        return (216*a*a - 90*a + 1) / (144*a*a - 24*a - 14)
    return (14*a - 3) / (12*a - 2)


def old_exponent(a):
    return -F(29, 96) + F(13, 80) * (
        density(a) + (1-a)/2 + max(6*a-2, 0)
    ) - F(25, 48)*a


def new_exponent(a, subset_length):
    return old_exponent(a) - F(1, 48) + (F(1, 8)-a)*subset_length


lo, mid, hi = F(1, 8), F(1, 3), F(1, 2)
target = -F(209, 960)

# The inherited first-branch derivative is -p/(480*(72a^2-12a-7)^2).
p = list(map(F, [-10877, 172104, -401328, -499392, 1498176]))
n1 = list(map(F, [1, -90, 216]))
b = list(map(F, [-7, -12, 72]))
den = scale(b, 2)
det = add(multiply(derivative(n1), den),
          scale(multiply(n1, derivative(den)), -1))
assert add(scale(det, 39), scale(multiply(b, b), -578)) == scale(p, -2)
assert bernstein(p, lo, mid) == [
    F(240361, 64), F(220293, 32), F(54167, 8), F(15921, 4), F(1899)
]
assert all(c > 0 for c in bernstein(p, lo, mid))
assert old_exponent(lo) == -F(16641, 75520) < -F(63, 320)

# On the second branch, G+63/320=(2a-1)*(1074a-101)/(960*(6a-1)).
# Each factor has a fixed sign on [1/3,1/2].
assert 2*mid-1 < 0 and 2*hi-1 == 0
assert 1074*mid-101 > 0 and 6*mid-1 > 0
assert old_exponent(hi) == -F(63, 320)
n2 = list(map(F, [-3, 14]))
six_a_minus_one = list(map(F, [-1, 6]))
second_identity = add(scale(n2, 78), scale(six_a_minus_one, -335),
                      multiply([F(0), F(358)], six_a_minus_one))
assert second_identity == multiply([F(-1), F(2)], [F(-101), F(1074)])

# The exact subset coefficient is nonpositive for every allowed zero bin.
assert F(1, 8)-lo == 0 and F(1, 8)-hi < 0
assert new_exponent(hi, F(0)) == target
assert target + F(5, 12) == F(191, 960)
assert -F(3, 16)-target == F(29, 960)

# Independent polynomial bookkeeping in the compensation subset length d.
x_scale = [F(17, 48), F(-1)]
y_scale = [F(23, 48), F(-1)]
p_scale = [F(1, 6), F(-1)]
q_scale = add(x_scale, y_scale)
assert q_scale == [F(5, 6), F(-2)]
normalized_prefactor = add(scale(q_scale, F(1, 2)),
                          scale(y_scale, -F(3, 2)),
                          [F(0), -F(1, 2)])
assert normalized_prefactor == [-F(29, 96)]
assert add([F(1)], p_scale, scale(x_scale, -1)) == [F(13, 16)]
assert add(y_scale, [F(-1)]) == [-F(25, 48), F(-1)]
assert scale(p_scale, -F(1, 8)) == [-F(1, 48), F(1, 8)]
raw_to_compensated = add(scale(q_scale, -F(1, 2)),
                         [F(0), -F(1, 2)])
assert raw_to_compensated == [-F(5, 12), F(1, 2)]
# Consequently a uniform compensated cap gives raw <= 191/960-d/2.
# At a=1/2 the sharper fixed-d endpoint is not asserted to be the bin maximum.
d_endpoint = F(1, 6)
assert new_exponent(hi, d_endpoint)+F(5, 12)-d_endpoint/2 == (
    F(191, 960)-F(7, 8)*d_endpoint)

# Density/physical-tail margins inherited from the exact all-n proof.
f_num = [F(17, 3), F(-75), F(180), F(-72)]
assert add(n1, scale(multiply([F(1, 3), F(1, 2)], den), -1)) == f_num
assert all(c < 0 for c in bernstein(den, lo, mid))
assert all(c < 0 for c in bernstein(f_num, lo, mid))
# Thus F(a)-5/6=f_num(a)/den(a)>0 on the first branch.
assert density(mid)+(1-mid)/2 == F(7, 6)
# On the second branch, F'=8/(12a-2)^2-1/2 >= 0.
assert F(8)/(12*hi-2)**2-F(1, 2) == 0

# The first-flat scale exponent beta=(F+(6a-2)_+)/5-a is unchanged.
quad = list(map(F, [-13, -76, 264]))
assert add(n1, multiply([F(2), F(-11)], b)) == scale(
    multiply([F(-1), F(3)], quad), -1)
assert all(c < 0 for c in bernstein(quad, lo, mid))
# On the first branch beta+1/10 has the sign of
# -(3a-1)*(264a^2-76a-13)/(10*(72a^2-12a-7)).
assert 3*lo-1 < 0 and 3*mid-1 == 0
assert all(c < 0 for c in bernstein([F(-7), F(-12), F(72)], lo, mid))
assert mid*(6*mid-5)/(10*(6*mid-1)) == -F(1, 10)
# On the second branch beta' has numerator 36*(a-1/6)^2+4 > 0.
assert add(scale(multiply([F(-1, 6), F(1)],
                          [F(-1, 6), F(1)]), 36), [F(4)]) == [F(5), F(-12), F(36)]
assert -2 - 6*(-F(1, 10)) == -F(7, 5) < -1

print('Exact exponent checks passed: normalized', target,
      '; raw', F(191, 960), '; threshold margin', F(29, 960))
