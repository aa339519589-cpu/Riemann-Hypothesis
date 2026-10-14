#!/usr/bin/env python3
"""Exact rational checks for the complete theta-prime tail contraction.
No finite-prime numerical approximation is used in the theorem certificate.
"""
from fractions import Fraction as F
from math import factorial

# e^4 exceeds its positive Taylor partial sum, which already exceeds 50.
taylor=sum((F(4**j,factorial(j)) for j in range(8)),F())
assert taylor>50
# Successive k-terms k^11 exp[-4(k^2-1)] have this uniform upper ratio.
r=F(3,2)**11/F(50**5)
assert 0<r<1
# The first term is bounded using e^12=(e^4)^3>50^3.
full_row=F(512,23)*F(2**11,50**3)/(1-r)
assert full_row<F(3,8)
# The source polynomial divided by z^3 at z=4 is 23/16.
assert F(8)-F(30,4)+F(15,16)==F(23,16)
# Verify c'(z)-c(z), including its constant derivative term.
c0={3:F(8),2:F(-30),1:F(15)}
diff={}
for j,a in c0.items():
    diff[j-1]=diff.get(j-1,F())+j*a
    diff[j]=diff.get(j,F())-a
assert diff=={3:F(-8),2:F(54),1:F(-75),0:F(15)}
# Verify c(z)-z c'(z)+z c(z) coefficient-by-coefficient.
c={3:F(8),2:F(-30),1:F(15)}
p={}
for j,a in c.items():
    p[j]=p.get(j,F())+(1-j)*a
    p[j+1]=p.get(j+1,F())+a
p={j:a for j,a in p.items() if a}
assert p=={4:F(8),3:F(-46),2:F(45)}
print('Exact all-integer contraction certificate passed.')
print('Taylor e^4 lower bound:',taylor)
print('Complete prime row / theta upper bound:',full_row)
print('Certified margin: 1/2 - row > 1/8.')
