"""Exact fixed-interval hybrid-density and declared-growth comparison checks.
No imported analytic theorem or global-novelty claim is certified by this script.
"""
from fractions import Fraction as F
LO,HI=F(59,1000),F(33,500)
for eta in (LO,HI):
    M=(275-1592*eta)/72
    Z=(347-1736*eta)/72
    assert M==(1-2*eta-F(521,796))/F(18,199)
    assert Z==(1-eta-F(1389,1736))/F(9,217)
    assert M+eta-F(3,4)*Z==(59-872*eta)/288>0
    assert F(3,4)*Z>3*eta
    assert F(14,15)<1-eta<F(2841,3016)
    assert 39208*eta-2275>0
    assert 288/(347-1736*eta)<391/(479-2493*eta)
eta=F(3,50)
old=391*eta/(479-2493*eta)
new=288*eta/(347-1736*eta)
assert old==F(1173,16471) and new==F(432,6071)
assert old-new==F(447,7691957)
print('Hybrid transfer and table comparison: PASS; .94 saving447/7691957')

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

# All further HB vertices have delta<=delta7<LO; the unreflected part is
# ineligible. The monotone delta formula is proved in the accompanying text.
assert 1-hb(7)[0]<LO
for eta in (LO,HI):
    D=347-1736*eta
    for s,mu in points:
        # a>48/D, b>96/D excludes every ceiling q in Pintz's Remark.
        assert mu*D>48*(1-s-eta)
        assert mu*D>96*(1-s-2*eta)
        mm=mu+s-F(1,2)
        assert mm*D>48*(s-eta)
        assert mm*D>96*(s-2*eta)
Dmin=347-1736*HI
assert hb(7)[0]-F(1,2)>96/Dmin
assert F(1,2)>96/Dmin
for mult,c in ((1,48),(2,96)):
    # Global curved input: minimum ratio squared270e/169.
    assert 270*mult*LO*Dmin**2>169*c*c
    # Reflected global curve: minimum comparison at delta=1/2.
    t=c/Dmin
    assert (1-t)**2>F(45,169)
    assert F(5,169)>(t*(F(1,2)-mult*LO))**2
asym=F(317,118272)
assert asym<LO
assert F(1,2)-asym>96/Dmin
# q1>=4b>288/D; q2>=3b>288/D; q>=3>=6a>288/D.
print('Uniform declared-growth Remark comparison: PASS')
