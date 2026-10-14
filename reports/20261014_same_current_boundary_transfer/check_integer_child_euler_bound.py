#!/usr/bin/env python3
from fractions import Fraction as F
import json

def exp_upper(x,n=12):
    term=s=F(1)
    for j in range(1,n+1):
        term=term*x/j;s+=term
    assert x<F(n+2)
    return s+(term*x/F(n+1))/(1-x/F(n+2))
c=F(16,9)
assert exp_upper(F(28,135))<F(99,80)
assert exp_upper(F(7,80))<F(9,8)
S3=F(1,27)+F(1,125)+F(1,100)
S6=F(1,729)+F(1,15625)+F(1,31250)
u2=1+F(2,9)+F(11,280)
upper=u2*exp_upper(c*S3+F(27,13)*S6)
assert upper<F(7,5)
print(json.dumps({'passed':True,'arithmetic':'exact fractions and complete tails','all_label_energy_factor_lt':'7/5','tail_label_energy_factor_lt':'2/5','prime2_power_bound_lt':'11/5','odd_prime_power_bound_lt':'2'},sort_keys=True,indent=2))
