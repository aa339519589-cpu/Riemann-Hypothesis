#!/usr/bin/env python3
"""Exact interpolation ledger only; does not test theta identities or RH.

Uses the user's conductor-balanced interpolation idea from 7a7c2dec,
with an extra moving-U exponent supplied by the exact j=4 transform.
"""
from fractions import Fraction as F

def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]
def scale(a,c):return [c*x for x in a]
def mul(a,b):
    ans=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return ans

# epsilon variable, h=eta=epsilon/4.
width=[F(1),F(1,2)]
weight_numerator=[F(1,2),F(-3,4)]
left_L=[F(3,2),F(1,2)]
left_U=[F(1,2),F(3,4)]
L_deficit=add(scale(width,F(3,4)),scale(mul(weight_numerator,left_L),-1))
U_deficit=add(scale(width,F(1,4)),scale(mul(weight_numerator,left_U),-1))
assert L_deficit==[0,F(5,4),F(3,8)]
assert U_deficit==[0,F(1,8),F(9,16)]
# Strict positivity holds for every epsilon>0. For 0<epsilon<1/4,
# the interpolation weight is between0 and1 and height degree2+epsilon<3.
for e in [F(1,10000),F(1,100),F(1,10),F(249,1000)]:
    theta=(F(1,2)-F(3,4)*e)/(1+e/2)
    assert 0<theta<1
    assert theta*(F(3,2)+e/2)<F(3,4)
    assert theta*(F(1,2)+F(3,4)*e)<F(1,4)
    assert 2+e<3
    # A hole d adds moving norm d^1/4 but its extracted coefficient is d^-sigma.
    assert F(1,4)-(F(1,2)+e)==-F(1,4)-e
print('PASS: fixed bad-period exponent <=3/4; moving cubic exponent <=1/4')
print('PASS: exact deficits 5epsilon/4+3epsilon^2/8 and epsilon/8+9epsilon^2/16')
print('PASS: polynomial height degree3 and negative hole exponent')
print('ALL_PASS')
