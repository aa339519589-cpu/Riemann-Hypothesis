#!/usr/bin/env python3
from fractions import Fraction as F
A=F(399,400);B=F(25,32)*F(401,400)**2
assert A>B
assert (3*A-4*B)*F(7,10)+F(23,200)==F(1157,102400)>0
assert F(1,5)-F(1,12)-F(1,120000)>F(23,200)
assert F(4374)/(44*F(69,100)*20**5)==F(729,16192000)<F(1,20000)
assert F(4,3)**7/20**7<F(1,2)
assert F(4,401)*F(8,25)*F(20001,20000)<F(2,625)
assert 4*F(8,25)*F(1,20000)==F(1,15625)
t=F(11,4);a=F(32,25);b=F(2,625);c=F(997,1000)
r=c*(1+t)-a*t-b
assert r==F(4311,20000)>0
assert r*r-4*a*b*t==F(562321,400000000)>0
assert c+F(1,15625)==F(124633,125000)<1
print('All exact projected-source allocation checks pass; coefficient124633/125000, margin367/125000.')
