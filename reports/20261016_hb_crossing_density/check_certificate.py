"""Exact certificate for the k=3 Heath-Brown crossing density corollary.

The certificate proves the interval algebra, not the imported analytic
large-value and zero-detection theorems or worldwide novelty.
Run with Python 3; only the standard library is required.
"""
from fractions import Fraction as F

LO, HI = F(77, 100), F(1547, 2000)
JOIN = F(17, 22)
assert F(3, 4) < F(16, 21) < LO < JOIN < HI < F(41, 53)
assert F(25, 33) < LO and HI < F(45, 58)
assert F(107, 139) < LO and HI < F(4, 5)

def values(s):
    eta = 1-s
    D = 29*s-19
    tau = (18-12*s)/7
    v = (96-120*s)/7
    alpha = (108*s-78)/7
    tau0 = 3*D/7
    E = 7*eta/D
    return eta,D,tau,v,alpha,tau0,E

# Every order assertion below reduces to an affine inequality in s.
# The only nonaffine target-line comparison is factored exactly into
# quantities already proved positive. Endpoint checks therefore certify
# the entire closed interval, not a numerical grid.
for s in (LO, HI):
    eta,D,tau,v,alpha,tau0,E = values(s)
    a = 2*tau0/3
    assert D > 0 and alpha > 0 and 0 < E < 1
    assert 0 < a < 1 < tau < tau0 < F(3,2)
    assert tau-v == alpha and tau0 == 3*eta+alpha
    assert 3*tau+6-12*s == v == 2*tau/3+12-16*s
    assert 2*eta < v < 3*eta
    assert 9-12*s < 2*eta
    assert F(38,3)-16*s < 2*eta
    assert E*a == 2*eta
    assert E*tau-v == alpha*(3*eta-v)/tau0 > 0
    assert E*tau0 == tau0-alpha == 3*eta
    assert 4*tau0/3 < 2  # The zeta-polynomial window is empty.

# The identified Table 11.1 changes branch at 17/22.
# Cross multiplication gives these exact affine positive numerators.
for left,right,c,p,q in ((LO,JOIN,6,5,-1),
                         (JOIN,HI,2,9,-6)):
    for s in (left,right):
        D = 29*s-19
        assert p*s+q > 0
        gap_numerator = c*D-7*(p*s+q)
        assert gap_numerator > 0
        assert F(c)/(p*s+q)-F(7)/D == gap_numerator/((p*s+q)*D)

# Also compare the separate Kerr bound recorded as Theorem 11.37.
# It is a maximum; showing that its second entry exceeds the new bound
# is sufficient. The cross-product polynomial is strictly increasing
# on this interval, and positive at LO.
def kerr_numerator(s):
    return (114*s-79)*(29*s-19)-7*(1-s)*(138*s-89)
assert kerr_numerator(LO) > 0
assert 8544*LO-6046 > 0
for s in (LO, HI):
    assert kerr_numerator(s) == 4272*s*s-6046*s+2124
    assert 138*s-89 > 0 and 114*s-79 > 0

print('Complete LV window, subdivision, empty zeta window: PASS')
print('Whole-interval Table 11.1 and separate Kerr comparisons: PASS')
for s in (LO, F(773,1000), HI):
    eta,D,tau,v,alpha,tau0,E = values(s)
    old = eta*(F(6)/(5*s-1) if s < JOIN else F(2)/(9*s-6))
    print('sigma',s,'new exponent',E,'table exponent',old,'saving',old-E)
assert values(F(773,1000))[-1] == F(1589,3417)
assert F(454,957)-F(1589,3417) == F(3405,363341)
