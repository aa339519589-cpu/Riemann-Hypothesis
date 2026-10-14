"""Exact rational checks for the matched first-label correction theorem.

These checks supplement, and do not replace, the analytic operator/domain
proofs. No numerical prime cutoff or sampled inequality is asserted.
"""
from fractions import Fraction as Q

pi0=Q(157,50)
e0=Q(27,10)
exp3pi=e0**9*(1+Q(21,50)+Q(21,50)**2/2)
assert exp3pi>11200
assert 28/exp3pi<Q(1,400)
assert Q(336,5)*pi0/exp3pi<Q(1,50)
assert 60*pi0/exp3pi<Q(7,400)
assert (28+60*pi0)/exp3pi<Q(1,50)
# The enlarged a=1/4 envelope is z^(3/2) exp(-z/2).
assert Q(3,2)/pi0-Q(1,2)<0
assert Q(1,2)/pi0-Q(1,2)<0
assert Q(3,2)/pi0-Q(11,2)<0
# True n2 killing; log2 > 69/100 and p1 > 400/401.
assert Q(400,401)*3*Q(69,100)==Q(828,401)>2
assert Q(9,2)*Q(69,100)>Q(48521,16000)
# Complete n>=3 retained envelope, using exp(3)>16 and z>=3.
b3=Q(17820,16**8)+Q(5040,16**15)
assert b3<Q(1,200000)
assert Q(3,80)+Q(1,200000)==Q(7501,200000)
assert Q(3,80)+Q(1,50)==Q(23,400)
# Complete reflected/Gamma boundary rows and pole-error coefficient.
exp2pi=e0**6*(1+Q(7,25)+Q(7,25)**2/2)
assert 14/(pi0**2*exp2pi)<Q(3,1000)
exp88over5=e0**17*(1+Q(3,5)+Q(3,5)**2/2)
assert Q(352,3)*Q(100,99)*256/exp88over5<Q(1,1000)
assert e0**8*(1+Q(4,5)+Q(4,5)**2/2)>5000
assert Q(7,1)/(12*e0*pi0**3*exp2pi)<Q(1,70000)
assert Q(13,200)+Q(1,70000)==Q(4551,70000)
assert 4*(Q(3,1000)+Q(1,1000))==Q(2,125)
assert Q(1,3)*Q(1,250)==Q(1,750)
print('All exact correction, weighted-envelope, boundary and pole checks passed.')
