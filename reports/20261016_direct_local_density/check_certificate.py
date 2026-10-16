"""Exact rational checks for a direct-local-beta density specialization.
Imported analytic theorems and global novelty are not certified here.
"""
from fractions import Fraction as F
LO,HI=F(33,1250),F(69,2500)
a,b,c,t=F(199,716),F(967,3428),F(120,419),F(29,100)
m1,v1=F(58,75),F(29,600)
m2,v2=F(1351,1614),F(49,1614)
m3,v3=F(235,264),F(1,66)
assert a<b<c<t<F(1424,4747)
assert m1*b+v1==m2*b+v2
assert m2*c+v2==m3*c+v3
assert min(v1,v2,v3)>0
assert F(1389,1736)+F(9,217)/t==F(6783,7192)<1-2*HI
for eta in (LO,HI):
    Q=136-1200*eta
    D=136-1171*eta
    M=Q/29
    Z=6-30*eta
    assert M==(1-2*eta-m1)/v1
    assert a<1/M<b
    assert 9*eta<2<3-6*eta
    assert 90*eta<3-6*eta
    assert eta<F(1,30)
    assert F(3,4)*Z-(M+eta)>0
    assert M+eta>max(F(3,2),3*eta)
    assert F(2211487,2274732)<1-eta<F(39,40)
    table_den=135951-1447460*eta
    assert table_den>0
    assert 87*table_den<86152*D
    # This is only a relative density-exponent comparison, not a zero fraction.
    assert 20*87*table_den<19*86152*D
print('Complete Montgomery and zeta prefixes; subdivision; table comparison: PASS')

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
assert 1-hb(11)[0]==F(83,3575)<LO
for eta in (LO,HI):
    D,Q=136-1171*eta,136-1200*eta
    for s,mu in points+[hb(n)for n in range(3,11)]:
        assert 2*mu*D>29*(1-s-eta)
        assert mu*Q>29*(1-s-2*eta)
        mr=mu+s-F(1,2)
        assert 2*mr*D>29*(s-eta)
        assert mr*Q>29*(s-2*eta)
for mult,den in ((1,2*(136-1171*HI)),(2,136-1200*HI)):
    target=29/den
    assert hb(11)[0]-F(1,2)>target
    assert F(1,2)>target
    assert 270*mult*LO*den**2>169*29**2
    # Reflected global curved bound; exact derivative and endpoint tests.
    assert (1-target)**2>F(45,169)
    assert F(5,169)>(target*(F(1,2)-mult*LO))**2
    asym=F(317,118272)
    assert asym<LO and F(1,2)-asym>target
# a>29/(2D), b>29/Q. Hybrid's Montgomery term exceeds87/D.
# Pintz q1:4b>87/D; q2:3b>87/D; q>=3:6a>87/D.
print('Full declared-growth hybrid and Pintz-Remark comparison: PASS')
eta=HI
D=136-1171*eta
new=87*eta/D
old=86152*eta/(135951-1447460*eta)
assert new==F(6003,259201)
assert (old-new)/old==F(181305554,2791335569)
assert old-new==F(4170027742,2592039808115)
print('sigma=.9724: exponent',new,'; identified-table saving',old-new)
