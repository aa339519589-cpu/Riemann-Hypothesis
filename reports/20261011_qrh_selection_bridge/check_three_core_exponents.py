from fractions import Fraction as Q

# All functions are affine. Endpoint checks therefore cover the full intervals.
def low(a):
    gamma=(2-2*a)/5
    return {'W':a-Q(1,2), 'H':6*gamma+a-Q(5,2),
            'r':6*a-2-6*gamma, 'sixth':-6*gamma}
for a in [Q(1,8), Q(3,8)]:
    b=low(a)
    assert b['W']<=-Q(1,8)
    assert b['H']==-Q(1,10)-7*a/5<0
    assert b['r']<=-Q(5,4)
    assert b['sixth']<=-Q(3,2)

for a in [Q(3,8),Q(1,2)]:
    p=(3-a)/2
    gamma=[Q(1,2)-a/6,Q(3,4)-a/4,Q(2,3)-a/4]
    hs=[-2*a/3,(1-3*a)/4,Q(1,6)-3*a/4]
    rs=[7*a-5,(15*a-13)/2,(15*a-12)/2]
    for g,h,r in zip(gamma,hs,rs):
        assert p-5*g<0
        assert g+p-2==h<=0
        assert 6*a-2-6*g==r<=-Q(3,2)
        assert -6*g<=-Q(5,2)
    normalized=[(10-63*a)/96,(59-171*a)/192,Q(61,288)-139*a/192]
    assert max(normalized)<=-Q(41,1536)<-Q(1,512)
print('ALL_PASS exact affine endpoint checks; low -1/512; high -41/1536')
