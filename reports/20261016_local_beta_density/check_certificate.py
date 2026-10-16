"""Exact interval certificate for the two-local-row A-process density corollary.
The imported exponential-sum and density theorems remain analytic inputs.
All interval checks below reduce to affine or linear-fractional monotonicity.
"""
from fractions import Fraction as F
LO, HI = F(8,125), F(129,2000)
a,b,c,t = F(143,349), F(263,638), F(209,500), F(21,50)
m1,c1 = F(1812,2765),F(491,5530)
m2,c2 = F(897,1345),F(113,1345)
assert a<b<c<t<F(156527,370694)
assert m1*b+c1==m2*b+c2
assert min(c1,c2)>0

def image(z,m,c): return z/(1+c+m*z)
def transform(m,c): return (1+m+c)/(2*(1+c)), c/(2*(1+c))
aA,bA,cA=image(a,m1,c1),image(b,m1,c1),image(c,m2,c2)
assert (aA,bA,cA)==(F(1430,4737),F(263,867),F(281105,916473))
assert bA==image(b,m2,c2)
p1,q1=transform(m1,c1);p2,q2=transform(m2,c2)
assert (p1,q1)==(F(3215,4014),F(491,12042))
assert (p2,q2)==(F(785,972),F(113,2916))
assert p1*bA+q1==p2*bA+q2

# For z0 in[a,c], (1+B(z))/z decreases across the first two rows.
# The global Bourgain row is below the required supporting ray for z>=t.
Cmin=(1+m2*c+c2)/c
assert Cmin*t-1-(t/2+F(13,84))==F(670564,147580125)>0
assert Cmin>F(1,2)
# These endpoint checks prove 0<=h<=2alpha/3 on each A-image interval.
for left,right,m,c0 in ((aA,bA,m1,c1),(bA,cA,m2,c2)):
    for alpha in (left,right):
        h=((1-m+c0)*alpha-c0)/(1+c0)
        z=alpha/(1+h-alpha)
        assert 0<h<F(2,3)*alpha and alpha<F(1,2)
        assert 2*alpha-h==alpha+(1+h-alpha)*(m*z+c0)
        assert (2*alpha-h)/2==transform(m,c0)[0]*alpha+transform(m,c0)[1]
assert F(1389,1736)+F(9,217)/cA==F(65205843,69714040)<1-HI
assert F(1,2)+F(13,84)/t==F(383,441)<1-2*HI

for eta in (LO,HI):
    M=(1906-11060*eta)/491
    Z=(2397-12042*eta)/491
    assert M==(1-2*eta-m1)/c1
    assert Z==(1-eta-p1)/q1
    assert a<1/M<b and aA<1/Z<bA
    assert M+eta-F(3,4)*Z==(433-6150*eta)/1964>0
    assert F(3,4)*Z>max(F(3,2),3*eta)
    # Both comparisons become affine after positive cross multiplication.
    D=2397-12042*eta
    assert 1964*(347-1736*eta)<288*D
    assert 1964*(479-2493*eta)<391*D
    assert F(59,1000)<eta<F(33,500)
print('A-process supremum, complete Montgomery/zeta ranges and density transfer: PASS')

# The entire declared growth family is strictly below neither of the
# required thresholds: every supplied lambda(eta)>491/D. Therefore the
# pure-growth hybrid max{3b/(1+eta*b),4a} and Pintz's Remark are worse.
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
points=[(F(1,2),F(13,84))]+[(s,p-q*s)for s,p,q in segments]
def hb(n):
    delta=F(3*n*n-3*n+2,n*(n-1)**2*(n+2))
    return 1-delta,F(2,(n-1)**2*(n+2))
assert 1-hb(7)[0]<LO
for eta in (LO,HI):
    D=2397-12042*eta
    for s,mu in points+[hb(n) for n in range(3,7)]:
        assert mu*D>491*(1-s-eta)
        assert (mu+s-F(1,2))*D>491*(s-eta)
Dmin=2397-12042*HI
assert hb(7)[0]-F(1,2)>491/Dmin
assert F(1,2)>491/Dmin
# Global curve: inf mu/(delta-eta) squared =270eta/169.
assert 270*LO*Dmin**2>169*491**2
# Reflected global curve. The difference is decreasing in delta<=1/2.
v=491/Dmin
assert (1-v)**2>F(45,169)
assert F(5,169)>(v*(F(1,2)-LO))**2
# The small-delta improved curve cannot contribute unreflected;
# its reflected functional-equation term already exceeds the target.
asym=F(317,118272)
assert asym<LO and F(1,2)-asym>491/Dmin
print('Full declared-growth hybrid and Pintz-Remark comparison: PASS')

eta=LO
new=1964*eta/(2397-12042*eta)
prior=288*eta/(347-1736*eta)
table=391*eta/(479-2493*eta)
assert new==F(15712,203289)
assert prior-new==F(1692704,1998127581)
print('sigma=.936: new exponent',new,'; prior-minus-new',prior-new,'; table',table)
