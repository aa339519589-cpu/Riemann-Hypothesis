#!/usr/bin/env python3
"""Exact rational checks for the SAME-current bridge allocation.
This checks constants only. The complete kernel identities, original
source domains and unconditional arithmetic inputs remain in the proofs.
"""
from fractions import Fraction as Q

# Normalized multiplier and residual potential; pi>3 and log2>2/3.
assert Q(17,8)+Q(12,21**2)<Q(13,6)
assert Q(2,5)*12-Q(9,2)-Q(6,21)==Q(1,70)
assert Q(1,4)+Q(15,14)+Q(65,96)==Q(1343,672)<2
assert Q(1,6)+Q(1,72)<Q(1,5)
assert Q(3,10)*Q(2,3)==Q(1,5)
T=Q(5,4); K=Q(1,2)
assert T*K==Q(5,8)
R=1/(1-T*K)
assert R==Q(8,3) and R-1==Q(5,3)

# All square-root enclosures are checked by squaring positive rationals.
assert Q(2,5)<Q(19,30)**2
assert Q(25,9*401)<Q(1,12)**2
assert Q(100,9*200)<Q(17,72)**2
field=Q(19,30)+Q(1,12)+Q(17,72)
assert field==Q(343,360) and field**2<Q(10,11)
assert Q(401,441)-Q(10,11)==Q(1,4851)>0

# Alternative central-mean hub allocation spends the same edges once.
assert 1-19*Q(1,40)==Q(21,40)
assert Q(21,40)>Q(19,100)*Q(13,10)
assert Q(3,5)>Q(19,100)*Q(3,2)
assert Q(19,20)*Q(1,5)==Q(19,100)

bridge=1+2/Q(19,100)
assert bridge==Q(219,19)<12
forward_error=Q(13,400)*bridge
original_error=Q(4551,70000)*bridge
assert forward_error==Q(2847,7600)<Q(3,8)
assert original_error==Q(996669,1330000)<Q(3,4)
assert bridge/50==Q(219,950)
print('PASS: normalized 5/4, exact reference cancellation allocation, SAME-V field contraction, 219/19 energy bridge, and actual-only error constants.')
