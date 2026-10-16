"""Exact certificates for the arbitrary-pair Halasz/subdivision corollary.
Only finite algebra and the declared-family comparison are certified here.
"""
from fractions import Fraction as F
from math import comb
LO,HI=F(7,8),F(177,200)
k0,l0=F(18,199),F(593,796)
k,l=l0-F(1,2),k0+F(1,2)
assert (k,l)==(F(195,796),F(235,398))
A,B=(k+l)/k,2*(1+2*k+2*l)/k
assert (A,B)==(F(133,39),F(4252,195))
assert B>1

def M(s):return (8114*s-5988)/665
def Z(s):return (796*s-521)/72
def tau0(s):return M(s)+1-s
def coefficient(s):return 3/tau0(s)
for s in (LO,HI):
    e=1-s
    assert M(s)==(2*e-B*(F(3,2)-2*s))/A
    assert M(s)<10*s-7
    assert M(s)>1
    assert tau0(s)==(7449*s-5323)/665
    assert F(3,2)<tau0(s)<F(3,4)*Z(s)
    assert F(3,4)*Z(s)-tau0(s)==(164543-185764*s)/63840
    assert Z(s)==(s-(l0-k0))/k0
    assert LO<=s<F(279,314)
    assert 1995*(10*s-7)<3*(7449*s-5323)
    assert coefficient(s)<F(16,9)
    assert s>F(23,29) and s>F(5323,6119)
    assert coefficient(s)<F(3)/(2*s)
assert 3*(1-F(22,25))/tau0(F(22,25))==F(5985,30803)
assert F(1,5)-F(5985,30803)==F(878,154015)
print('Pair, full prefix, zeta ceiling, subdivision and table comparison: PASS')

# The declared Table6.2 vertices, their functional reflections, the whole
# Heath-Brown family, the C delta^(3/2) curve and near-one asymptotic row.
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
points=[(F(1,2),F(13,84)),(F(1),F(0))]+[(s,p-q*s)for s,p,q in segments]
def hb(n):return 1-F(3*n*n-3*n+2,n*(n-1)**2*(n+2)),F(2,(n-1)**2*(n+2))
for s in (LO,HI):
    for x,mu in points+[hb(n)for n in range(3,7)]:
        for y,v in ((x,mu),(1-x,mu+x-F(1,2))):
            assert v*M(s)>2*s-1-y
            assert 3*v>s-y
# HB n>=7 unreflected rows are ineligible; reflected rows use mu>=0.
x7=hb(7)[0]
assert x7>HI
for s in (LO,HI):
    assert M(s)>1
    assert (x7-F(1,2))*M(s)>x7-2*(1-s)
    assert 3*(x7-F(1,2))>x7-(1-s)
# For x<=0, mu=1/2-x. The margins increase as -x increases.
for s in (LO,HI):
    assert M(s)/2>2*s-1
    assert F(3,2)>s

# Unreflected C delta^1.5, C^2=40/169, delta in[0,1/2].
# b=lambda(2eta): 6eta>1/2, so its minimum occurs at delta=1/2.
C2=F(40,169)
for s in (LO,HI):
    assert 6*(1-s)>F(1,2)
    assert C2*M(s)**2/8>(2*s-F(3,2))**2
# a=lambda(eta): the unrestricted minimum squared is27 C^2 eta/4.
assert F(27,4)*C2*(1-HI)>F(1,9)
# Reflected a curve decreases to delta=1/2 after subtracting(s-delta)/3.
assert F(9,4)*C2/2<F(4,9)
assert F(5,169)>(HI/F(3)-F(1,6))**2

# Reflected b: global delta>=0 minimum is
# 1/2-(2s-1)/M -169/270*(1-1/M)^3.
# Multiply by270 M^3. Certify cubic positivity via Bernstein coefficients.
def add(p,q):
    r=[F(0)]*max(len(p),len(q))
    for i,c in enumerate(p):r[i]+=c
    for i,c in enumerate(q):r[i]+=c
    return r
def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r
def scale(p,c):return [c*x for x in p]
def power(p,n):
    r=[F(1)]
    for _ in range(n):r=mul(r,p)
    return r
mp=[F(-5988,665),F(8114,665)]
poly=add(add(scale(power(mp,3),135),scale(mul([F(-1),F(2)],power(mp,2)),-270)),scale(power(add(mp,[F(-1)]),3),-169))
# Convert s=LO+(HI-LO)u, then ordinary powers to degree3 Bernstein basis.
u=[F(0)]*4
for i,c in enumerate(poly):
    for j in range(i+1):u[j]+=c*comb(i,j)*LO**(i-j)*(HI-LO)**j
bern=[sum(u[j]*F(comb(i,j),comb(3,j)) for j in range(i+1)) for i in range(4)]
assert min(bern)>0
print('Reflected growth-curve cubic Bernstein coefficients:',*[str(x)for x in bern])

# Any sharper asymptotic curve only available within this near-one range
# is ineligible unreflected; its reflection has mu>=1/2-delta.
asym=F(317,118272)
assert asym<1-HI
for s in (LO,HI):
    assert (F(1,2)-asym)*M(s)>2*s-1
    assert 3*(F(1,2)-asym)>s
print('Complete declared growth-family comparisons: PASS')
for s in (LO,F(22,25),HI):
    e=1-s; new=3*e/tau0(s);old=3*e/(10*s-7)
    print('sigma',s,'exponent',new,'old',old,'saving',old-new)
