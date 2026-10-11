"""Exact rational gap ledger; no analytic theorem or RH is checked.

Standard-library reproduction of the two Bernstein certificates and the
remaining rational margins in the balanced shifted-inverse proof.
"""
from fractions import Fraction as F
from math import comb

def add(a,b):
    return [(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0))
            for i in range(max(len(a),len(b)))]
def scale(a,c): return [c*x for x in a]
def mul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return z
def shift(a,lo,hi):
    z=[F(0)]*len(a)
    for i,c in enumerate(a):
        for k in range(i+1): z[k]+=c*comb(i,k)*lo**(i-k)*(hi-lo)**k
    return z
def bernstein(a,lo,hi):
    z=shift(a,lo,hi); n=len(z)-1
    return [sum(z[i]*F(comb(k,i),comb(n,i)) for i in range(k+1))
            for k in range(n+1)]

d=[F(5),F(2),F(-24)]
# Dp = (74 a - 120 a^2)/(3d).
dp_num=[F(0),F(74),F(-120)]
cases=[
 (F(1,8),F(1,6),[F(1,6),F(3)], [F(0)],
  [F(379,400),F(5509,7200),F(2287,3600),F(79,150)]),
 (F(1,6),F(7,40),[F(1,3),F(2)], [F(-1,9),F(2,3)],
  [F(79,150),F(20267,54000),F(122149,540000),F(4753,60000)])]
for lo,hi,D0,correction,want in cases:
    rem=add(add(D0,scale(correction,-1)),[F(-1,200)])
    polynomial=add(scale(mul(d,rem),6),scale(dp_num,-2))
    got=bernstein(polynomial,lo,hi)
    assert got==want and all(x>0 for x in got)
    print('PASS Bernstein',lo,hi,got)

# Clearing 3(6a+1) in 7/3 - [8a/(1+6a)+2-2a].
gap_num=add(mul([F(1),F(6)],[F(1),F(6)]),[F(0),F(-24)])
assert gap_num==[F(1),F(-12),F(36)]  # (6a-1)^2.
a=F(7,40)
assert (6*a-1)**2/(3*(6*a+1))==F(1,2460)
# The derivative is 2(6a-1)(6a+3)/(6a+1)^2, nonnegative for a>=1/6.
assert F(140,99)**2<2
assert F(15,64)-(7-4*F(140,99))/6==F(199,19008)>F(1,2460)
assert F(1,200)>F(1,2460)
print('ALL_EXACT_GAPS_PASS; analytic and source arguments are separate')
