"""Exact full-window certificate for the k=4 and k=5 crossing corollaries.
Only rational arithmetic is used. Imported analytic theorems and exhaustive
literature novelty are not certified by this program.
"""
from fractions import Fraction as F

CASES = [(4,F(29,38),F(13,17)),(5,F(547,720),F(127,167))]
def quantities(k,s):
    eta=1-s
    t=F(k)*(6-4*s)/(3*k-2)
    v=F(4*k)*((3*k-1)-(4*k-2)*s)/(3*k-2)
    alpha=t-v
    tau0=3*eta+alpha
    D=(16*k*k-21*k+6)*s-12*k*k+19*k-6
    assert tau0==D/(3*k-2)
    return eta,t,v,alpha,tau0,D

for k,lo,hi in CASES:
    # All these conditions are affine in s, so both endpoint checks
    # establish them on the whole closed interval.
    for s in (lo,hi):
        eta,t,v,alpha,tau0,D=quantities(k,s)
        assert F(3,4)<s<1
        assert alpha>0 and 2*eta<=v<=3*eta
        assert 0<2*tau0/3<1<t<tau0<F(3,2)
        assert 3*k-4*k*s<=2*eta
        assert F(2,3)+F(k)*(12-16*s)/3<=2*eta
        assert k*t+k*(2-4*s)==v==2*t/3+F(k)*(12-16*s)/3
        E=3*eta/tau0
        assert 0<E<1 and E*(2*tau0/3)==2*eta
        assert E*t-v==alpha*(3*eta-v)/tau0>=0
        assert E*tau0==tau0-alpha==3*eta
        assert 4*tau0/3<2
        if k==4:
            assert 3/tau0==15/(89*s-61)
            assert F(127,167)<lo<hi==F(13,17)
            assert 89*s-61>=13*s-3>0
            assert 89*lo-61==13*lo-3
            assert 15/(89*hi-61)==6/(5*hi-1)
            assert 15*(138*s-89)<36*(89*s-61)
        else:
            assert 3/tau0==39/(301*s-211)
            assert F(7,10)<lo<F(19,25)<hi==F(127,167)
            assert 39*(138*s-89)<36*(301*s-211)
            assert 39/(301*hi-211)==15/(13*hi-3)

# k=5 crosses the table join 19/25. Positive denominator clearing
# leaves affine expressions; equality occurs only at the left endpoint.
lo,mid,hi=F(547,720),F(19,25),F(127,167)
for s in (lo,mid):
    assert 15*(301*s-211)-39*(3+5*s)>=0
assert 15*(301*lo-211)-39*(3+5*lo)==0
for s in (mid,hi):
    assert 9*(301*s-211)-39*(8*s-2)>0

print('General crossing identities and both complete length windows: PASS')
print('Full table intervals, branch endpoints and separate Kerr comparison: PASS')
for k,s in ((4,F(191,250)),(5,F(19,25))):
    eta,t,v,alpha,tau0,D=quantities(k,s)
    new=3*eta/tau0
    old=eta*(15/(13*s-3) if k==4 else 9/(8*s-2))
    print('k',k,'sigma',s,'new exponent',new,'table exponent',old,'saving',old-new)
assert 3*quantities(4,F(191,250))[0]/quantities(4,F(191,250))[4]==F(295,583)
assert 3*quantities(5,F(19,25))[0]/quantities(5,F(19,25))[4]==F(39,74)
