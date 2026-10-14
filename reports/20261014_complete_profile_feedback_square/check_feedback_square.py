#!/usr/bin/env python3
from fractions import Fraction as F
slack=F(49,50)*(F(39599,20000)-F(1,5))-F(29,22)**2
assert slack==F(816471,121000000)>0
c=F(124633,125000)
c_total=c+F(1,1100)
assert c_total==F(1372213,1375000)<1
assert 1-c_total==F(2787,1375000)
assert F(1,5500)*5==F(1,1100)
assert F(1,5)-F(1,12)-F(1,120000)-F(23,200)==F(199,120000)
print('PASS: one-budget residual allocation, exact full-feedback coefficient',c_total)
print('Strict complete-feedback margin:',1-c_total)
