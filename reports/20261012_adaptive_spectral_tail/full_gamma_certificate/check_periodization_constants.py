from fractions import Fraction as F
from math import factorial

def exp_lower(x,n):
    return sum((x**j/F(factorial(j)) for j in range(n+1)), F(0))
assert exp_lower(F(3),8)>20
assert exp_lower(F(1),3)>=F(8,3)
assert exp_lower(F(1,2),2)>F(8,5)
# Upper e^(1/2)<5/3: first 3 terms plus geometric majorant for j>=3.
assert sum((F(1,2)**j/F(factorial(j)) for j in range(3)),F(0))+F(1,48)/(1-F(1,8))<F(5,3)
assert F(2000,49)/20<F(9,4)
assert 100*F(16,9)/(F(8,3)**2)==25
assert 20*F(16,15)+F(3,2)*F(16,7)==F(520,21)<25
assert F(3,2)*F(64,15)<7
assert F(34000,49*18*27)<F(36,25)
assert 15*25+3*F(8,5)+F(6,5)*7<389
assert 15*F(8,5)==24
print('ALL_PASS')
print('real_m_square_upper',F(100,49))
print('nonfrequency_derivative_upper',F(520,21))
print('weighted_m_L2_square_upper',F(34000,49*18*27))
print('Cf_A0_upper',15*25+3*F(8,5)+F(6,5)*7)
