"""Exact arithmetic for the general-subdivision report's fixed interval.

This verifies all finite endpoint inequalities, and the stated comparison
against the declared growth-input family. It does not prove the cited
analytic theorems, identify the unknown true mu, or certify global novelty.
"""
from fractions import Fraction as F

LO, HI = F(37,1000), F(1,25)

def input_intervals(eta, count, factor):
    # factor=2: Montgomery; factor=1: zeta interval sums.
    return [(F(factor*r*r*(r-1),2)*eta,
             r*(1-factor*(r-1)*eta)) for r in range(3,count+1)]

for eta in (LO, HI):
    M, Z, D = 4-24*eta, 5-20*eta, 4-23*eta
    assert F(1,40) <= eta < F(1,24)  # ell=4 cell
    assert F(1,30) <= eta < F(1,20)  # k=5 cell
    for count,factor,start,finish in ((4,2,F(1),M),(5,1,F(2),Z)):
        rows=input_intervals(eta,count,factor)
        assert rows[0][0]<start<rows[0][1]
        assert rows[-1][1]==finish
        for r,(left,right) in enumerate(rows,3):
            assert left<right
            assert factor*eta < F(1,r*(r-1))
        for (lo,hi),(nlo,nhi) in zip(rows,rows[1:]):
            assert nlo<hi<nhi
    assert F(3,4)*Z-D == -F(1,4)+8*eta > 0
    assert D>3*eta
    D1,D2=(374-2475*eta)/89,(1334-9333*eta)/311
    assert D1>D and D2>D
    assert F(3,4)*Z>D1 and F(3,4)*Z>D2
    assert (F(187,641)-2*eta)/F(89,1282)+eta==D1
    assert (F(667,2411)-2*eta)/F(311,4822)+eta==D2
    assert F(23,24) < 1-eta < F(2211487,2274732)
    assert 3*eta/M-3*eta/D == 3*eta*eta/(M*D)>0
assert 3*HI/(4-24*HI)==F(3,76)
assert 3*HI/(4-23*HI)==F(3,77)
assert F(3,76)-F(3,77)==F(3,5852)
print('Full derivative-interval certificate: PASS')
assert 3*HI/((374-2475*HI)/89)==F(267,6875)
assert F(3,76)-F(267,6875)==F(333,522500)
cross=F(67,1692)
assert LO<cross<HI
assert (374-2475*cross)/89==(1334-9333*cross)/311
print('At sigma=.96: 3/76 -> 267/6875; saving 333/522500')

# Table 6.2: (right endpoint, intercept, positive slope).
segments=[
(F(88225,153852),F(31,84),F(3,7)),
(F(521,796),F(220633,620612),F(62831,155153)),
(F(53141,76066),F(1333,3825),F(1508,3825)),
(F(454,641),F(405,1202),F(227,601)),
(F(1744,2411),F(779,2590),F(423,1295)),
(F(951057,1298878),F(179,622),F(96,311)),
(F(1389,1736),F(157319,560830),F(251324,841245)),
(F(587779,702192),F(2841,10316),F(754,2579)),
(F(7441,8695),F(1691,6554),F(890,3277)),
(F(277,300),F(29,130),F(3,13)),
]
points=[(F(1,2),F(13,84))]
for s,a,b in segments:
    points.append((s,a-b*s))
def hb(n):
    delta=F(3*n*n-3*n+2,n*(n-1)**2*(n+2))
    return 1-delta,F(2,(n-1)**2*(n+2))
points += [hb(7),hb(8)]
# delta_n decreases. Cross-multiplication gives the positive numerator
# 2n(3n^4+3n^3+n^2+3n-2), for every integer n>=1.
assert 1-hb(9)[0] < LO
# Every subsequent unreflected vertex has delta<eta and is ineligible.

# For a=lambda(eta), b=lambda(2eta), prove all supplied values satisfy
# a > 1/(2D), b > 1/D, D=4-23eta. Each displayed test is affine in eta.
for eta in (LO,HI):
    D=4-23*eta
    for s,mu in points:
        delta=1-s
        assert 2*mu*D-(delta-eta)>0
        assert mu*D-(delta-2*eta)>0
        # Complete functional-equation reflections of these vertices.
        m,sigma=mu+s-F(1,2),1-s
        assert 2*m*D-(1-sigma-eta)>0
        assert m*D-(1-sigma-2*eta)>0
# Reflections of all remaining HB vertices are uniformly separated too.
Dmin=4-23*HI
assert hb(9)[0]-F(1,2)>1/Dmin
# For sigma<=0, the growth value 1/2-sigma has ratio >=1/2.
assert F(1,2)>1/Dmin

# The global curve C delta^(3/2), C=2sqrt(10)/13, has unrestricted
# minimum ratio squared (270/169)e at parameter e>0.
assert 1080*LO*Dmin*Dmin>169  # e=eta, target 1/(2D)
assert 540*LO*Dmin*Dmin>169   # e=2eta, target 1/D
# Its reflected ratio cannot defeat either target. On 0<=delta<=1/2,
# derivative of C delta^(3/2)-(1-t)delta is negative for t<=1/Dmin.
assert (1-1/Dmin)**2>F(45,169)
assert F(5,169)>((F(1,2)-LO)/Dmin)**2
# The sharper curve is available only at delta<=317/118272<LO.
asym=F(317,118272)
assert asym<LO
assert F(1,2)-asym>1/Dmin  # reflected small-delta part

# q=ceil(b/a): q=1 costs >=4b, q=2 costs >=3b, q>=3 costs >=6a.
# Therefore every choice supplied by the declared envelope gives A>3/D.
print('Uniform declared-growth Remark comparison: PASS')

# Fixed .96 calibration, including optimal enlargement of admissible a,b.
eta=HI
eligible=lambda e: min((mu/(1-s-e),s) for s,mu in points if 1-s>e)
a=eligible(eta)[0]; b=eligible(2*eta)[0]
assert a==F(2225,9062) and b==F(2225,6786)
assert 1<b/a<2
assert a*a<F(270,169)*eta and b*b<F(540,169)*eta
for e,t in ((eta,a),(2*eta,b)):
    assert min((mu+s-F(1,2))/(s-e) for s,mu in points)>t
    assert (1-t)**2>F(45,169)
    assert F(5,169)>(t*(F(1,2)-e))**2
    assert hb(9)[0]-F(1,2)>t
    assert F(1,2)-asym>t
remark=max(4*a,3*b)
assert remark==F(2225,2262)
assert 4*b>remark and 6*a>remark
assert remark>F(75,77)>F(267,275)
print('At sigma=.96: declared-growth Remark A=',remark,'; hybrid A=267/275')
