"""Exact interval arithmetic for two linked local-A density corollaries.
This does not certify the imported analytic theorems or worldwide novelty.
"""
from fractions import Fraction as F
LO,HI=F(31,500),F(63,1000)
a,b,c,d,t=F(307,761),F(143,349),F(263,638),F(209,500),F(21,50)
rows=[(F(1053,2800),F(569,2800)),(F(1812,2765),F(491,5530)),(F(897,1345),F(113,1345))]
assert a<b<c<d<t<F(156527,370694)
for z,(m,v),(mm,vv)in zip((b,c),rows,rows[1:]):assert m*z+v==mm*z+vv
assert all(v>0 for m,v in rows)
def image(z,m,v):return z/(1+v+m*z)
def transform(m,v):return (1+m+v)/(2*(1+v)),v/(2*(1+v))
ends=[image(z,*row)for z,row in zip((a,b,c,d),rows+[rows[-1]])]
assert ends==[F(3070,10311),F(1430,4737),F(263,867),F(281105,916473)]
newrows=[transform(*row)for row in rows]
assert newrows[0]==(F(737,1123),F(569,6738))
for z,(p,q),(pp,qq)in zip(ends[1:3],newrows,newrows[1:]):assert p*z+q==pp*z+qq
Cmin=(1+rows[-1][0]*d+rows[-1][1])/d
assert Cmin*t-1-(t/2+F(13,84))==F(670564,147580125)>0
assert Cmin>F(1,2)
for left,right,(m,v),(p,q)in zip(ends,ends[1:],rows,newrows):
    for alpha in (left,right):
        h=((1-m+v)*alpha-v)/(1+v)
        z=alpha/(1+h-alpha)
        assert 0<h<F(2,3)*alpha and alpha<F(1,2)
        assert 2*alpha-h==alpha+(1+h-alpha)*(m*z+v)
        assert (2*alpha-h)/2==p*alpha+q
assert F(1389,1736)+F(9,217)/ends[-1]<1-HI
assert F(1,2)+F(13,84)/t<1-2*HI

for e in (LO,HI):
    D=2316-6738*e
    M=(1747-5600*e)/569
    Z=D/569
    assert a<1/M<b and ends[0]<1/Z<ends[1]
    assert M==(1-2*e-rows[0][0])/rows[0][1]
    assert Z==(1-e-newrows[0][0])/newrows[0][1]
    assert M+e-F(3,4)*Z==(20+45*e)/1138>0
    assert F(3,4)*Z>max(F(3,2),3*e)
    # Zeta-limited corollary: compare published growth hybrid and current table.
    assert 2276*(347-1736*e)<288*D
    assert 2276*(479-2493*e)<391*D
    assert F(14,15)<1-e<F(2841,3016)
    # Montgomery-limited partner at eta=e/2.
    eta=e/2; DM=2316-12907*eta
    assert Z+eta==DM/569
    ZH=6-30*eta
    assert F(3,4)*ZH>Z+eta>max(F(3,2),3*eta)
    # HB r=3,4,6: every middle term is strict, and both joins overlap.
    assert eta<F(1,30)
    assert 9*eta<2<3-6*eta
    assert 24*eta<3-6*eta
    assert 90*eta<4-12*eta
    assert F(23,24)<1-eta<F(2211487,2274732)
    assert 1707*(4-24*eta)<3*DM
print('Full A supremum, both complete prefixes, both transfers, table comparisons: PASS')

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
assert 1-hb(10)[0]<LO/2
# Supplied lambda(e)>569/D and lambda(e/2)>569/(2DM).
for e in (LO,HI):
    D=2316-6738*e;DM=2316-F(12907)*e/2
    for s,mu in points+[hb(n)for n in range(3,10)]:
        assert mu*D>569*(1-s-e)
        assert (mu+s-F(1,2))*D>569*(s-e)
        assert 2*mu*DM>569*(1-s-e/2)
        assert 2*(mu+s-F(1,2))*DM>569*(s-e/2)
for param,den in ((LO,2316-6738*HI),(LO/2,2*(2316-F(12907)*HI/2))):
    target=569/den
    assert hb(10)[0]-F(1,2)>target and F(1,2)>target
    assert 270*param*den**2>169*569**2
    assert (1-target)**2>F(45,169)
    assert F(5,169)>(target*(F(1,2)-param))**2
    asym=F(317,118272)
    assert asym<param and F(1,2)-asym>target
print('Both full declared-growth hybrid and Pintz-Remark comparisons: PASS')

for e in (LO,HI):
    newZ=2276*e/(2316-6738*e)
    priorZ=288*e/(347-1736*e)
    newM=1707*(e/2)/(2316-F(12907)*e/2)
    tableM=3*(e/2)/(4-12*e)
    print('sigma',1-e,'exponent',newZ,'prior saving',priorZ-newZ)
    print('sigma',1-e/2,'exponent',newM,'table saving',tableM-newM)
