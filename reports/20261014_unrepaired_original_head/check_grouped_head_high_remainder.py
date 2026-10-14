"""Exact rational checks for the grouped ORIGINAL-head high-column remainder.
No floating eigenvalue or finite matrix is used as a proof.
"""
from fractions import Fraction as Q

assert Q(11,14)+Q(1,4)+Q(2,3)<Q(7,4)
assert Q(11,14)+Q(1,24)+Q(2,3)<Q(3,2)
assert 32*3**8>200000
rho=Q(1,64)
coef=(7+6*rho)/(3*(1-rho*rho))+Q(1,200000)
assert coef<Q(5,2)
N,M=64,4096
assert M+1>=64*N and M>=7
rem=Q(175,52)*Q(sum(i**12 for i in range(1,N+1)),M**13)
assert rem==Q(140456698917930754513175,148433760041419827630061740822747494183805648896)
assert rem<Q(1,10**24)
assert rem/Q(1,10**6)<Q(1,10**12)
# The logarithmic bound b<3/4 follows from this partial exponential sum.
assert sum(Q(3,4)**k / __import__('math').factorial(k) for k in range(4))>2
print('PASS: grouped coefficient <5/2 and full factor-seven N64/M4096 remainder <10^-24/d_*')
print('Exact residual:',rem)
