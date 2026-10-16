"""Exact rational checks for REPORT.md.

This checks elementary finite inequalities, not the cited analytic theorems
or the novelty of their consequence. No third-party code is executed.
"""
from fractions import Fraction as F

etas = (F(1, 101), F(1, 99))

def check_endpoint(eta):
    M, Z = 7 - 84*eta, 10 - 90*eta
    ranges_M = [(r*r*(r-1)*eta, r*(1-2*(r-1)*eta))
                for r in range(3, 8)]
    ranges_Z = [(F(r*r*(r-1), 2)*eta, r*(1-(r-1)*eta))
                for r in range(3, 11)]
    for ranges, start, endpoint in ((ranges_M, F(1), M),
                                    (ranges_Z, F(2), Z)):
        assert ranges[0][0] < start < ranges[0][1]
        assert ranges[-1][1] == endpoint
        for (lo, hi), (nlo, nhi) in zip(ranges, ranges[1:]):
            assert lo < hi and nlo < hi and nhi > hi
        assert ranges[-1][0] < endpoint
    assert all(2*eta < F(1, r*(r-1)) for r in range(3, 8))
    assert all(eta < F(1, r*(r-1)) for r in range(3, 11))
    assert F(3, 4)*Z - (M+eta) == F(1, 2)+F(31, 2)*eta > 0
    assert M+eta > 3*eta
    assert F(1, 112) < eta < F(1, 84)  # current table's l=7 cell
    assert F(1, 110) < eta < F(1, 90)  # k=10 cell
    old, new = 3*eta/M, 3*eta/(M+eta)
    assert old-new == 3*eta*eta/(M*(M+eta)) > 0
    return old, new

for eta in etas:
    old, new = check_endpoint(eta)
    print(f"eta={eta}; sigma={1-eta}; old={old}; candidate={new}")

# Every interval-cover and side condition above is affine in eta;
# endpoint positivity therefore proves the entire closed eta interval.
eta=F(1,100)
old,new=check_endpoint(eta)
assert old==F(3,616) and new==F(3,617)
assert old-new==F(3,380072)
print("Affine interval certificate passed; exponent saving at sigma=.99 =", old-new)

# The subdivision inequality, after multiplying by positive tau0, is
# (tau0-3eta)*(tau0-tau)>=0 for its second branch. The first branch
# is bounded exactly when tau>=2tau0/3. No discretization in tau is used.
