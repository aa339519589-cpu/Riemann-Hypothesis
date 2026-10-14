#!/usr/bin/env python3
from fractions import Fraction as F
from math import factorial
assert sum(F(3**k,factorial(k)) for k in range(9))>20
assert F(401,400*20**9)<F(1,1000)
assert F(377,1200)**2>F(7,75)
c0=F(401,40000)
assert F(32481,3200000)<F(1,90)
incidence=F(5,3)*(1+c0/7)**2*F(8101,8100)
assert incidence==F(70770984800989,42336000000000)<F(169,100)
assert F(8,24300)<F(1,55**2)
assert 2*(F(13,10)+F(1,55))==F(29,11)
assert 2-2*c0==F(39599,20000)
assert F(9,10)*(F(39599,20000)-F(1,25))-F(29,22)**2==F(202111,24200000)>0
assert F(49,50)*(F(39599,20000)-F(1,5))-F(29,22)**2==F(816471,121000000)>0
reset=F(401,400)**2*(F(17820,20**5)+F(5040,20**12))/16
assert reset==F(45847581130130463,131072000000000000000)<F(1,2800)
print('PASS: complete incidence, rare-root reduction, residual allocation and true-metric reset.')
