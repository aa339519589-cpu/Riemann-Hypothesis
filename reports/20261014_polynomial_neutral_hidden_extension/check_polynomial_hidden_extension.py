#!/usr/bin/env python3
"""Rational checks for the full exponential kernel barriers and label tail."""
from fractions import Fraction as F
from math import factorial
q=F(99,100)
L=F(1,99)
def AB(a,b):
    return ((L+a*(1/q-1)+b*(1/q**2-1))/2,
            ((1/q-1)+a*(1/q**2-1)+2*b*(1/q**3-1))/2)
A,B=AB(F(5,28),F(1,126))
assert A<F(1,100) and B<F(1,100)
A1,B1=AB(F(1),F(2,9))
assert A1<F(1,50) and 4*B1<F(1,10)
assert F(1,50)<F(69,25)/30 and F(1,10)<F(621,200)/30
assert F(1,100)<F(69,25)/2 and F(1,100)<F(621,200)/2
x=F(297,100)
assert sum((x**j/F(factorial(j)) for j in range(16)),F())>19
assert F(5,19**7)<F(1,2)
tail=F(256,19**3)+F(4536,19**8)
assert tail<F(1,25)
assert F(256,8000)<F(1,16)
assert F(10,3)*(1+F(1,16))<4
print('Full continuous barriers: PASS')
print('Full posterior inverse norm bound:',tail)
print('Norm bound <1/25: PASS')
print('Complete n>=3 geometric tail: PASS')
