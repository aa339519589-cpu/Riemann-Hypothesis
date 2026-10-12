#!/usr/bin/env python3
"""Exact rational verification of the reviewed modewise detector ledger.
This checks arithmetic, not the analytic theorem.
"""
from fractions import Fraction as F

b, h, ah = F(5,6), F(1,100), F(47,300)
x, y, eta, k = F(269,200), F(1893,1000), F(7,500), 4
zeta, tau, goal = F(1,100000), F(1,500), F(79,125)
D = 2*ah*(37-60*ah)/(3*(5+2*ah-24*ah*ah))
p = 4*ah*(12*ah-5)/(3*(2*ah-1)*(12*ah+5))
assert D == F(5405,8858) and p == F(611,4429)
assert b+h == 1-ah
assert eta+tau == F(2,125) < F(1,50)
assert zeta < eta and zeta+tau < F(1,50)
assert 1+p < 2

K3x = max(F(1),x,F(2,3)*(1+x))
transition = k*(1+x-y)
pref = 4*k*h*x+k*(2*b-1)*(x-y)
ledger = {
    'initial higher low rows':D,
    'good row term':pref+1,
    'good column term':pref+max(F(0),transition),
    'good cross term':pref+F(2,3)*(1+max(F(0),transition)),
    'sharp Fejer error':-F(8,15)*y+F(2,5)+F(4,5)*K3x-F(4,5)*eta,
    'sharp lattice error':-F(8,15)*y+F(2,5)+F(4,5)*K3x-F(2,5)*x,
    'bad modes':-y/3+F(1,4)+K3x/2+3*D/8+3*p*eta/8,
    'tail Y':y/3,
    'tail pair cross':F(14,3)-3*x,
    'tail long column':6-4*x,
    'tail M/X':1-x,
}
expected = {
    'initial higher low rows':F(5405,8858),
    'good row term':F(-923,3750),
    'good column term':F(2107,3750),
    'good cross term':F(2347,3750),
    'sharp Fejer error':F(1181,1875),
    'bad modes':F(267955,425184),
    'tail Y':F(631,1000),
    'tail pair cross':F(379,600),
    'tail long column':F(31,50),
    'tail M/X':F(-69,200),
}
for name, value in expected.items():
    assert ledger[name] == value, (name,ledger[name],value)
assert max(ledger.values()) == F(379,600)
assert goal-max(ledger.values()) == F(1,3000)
paid = dict(ledger)
paid['bad modes'] += 3*zeta/4
assert max(paid.values()) < goal
# Exact endpoints for the complete polynomial K tail.
for beta in (b,b+h):
    for exponent in (k*(2*beta-3),k*(2*beta-2),k*(2*beta-F(7,3))):
        assert exponent < 0
    assert k*(3-2*beta) > 0
# Large-T extension: the trivial O(M) family count is absorbed.
assert goal+185*tau > 1
for name,value in ledger.items():
    print(f'{name}: {value}, margin={goal-value}')
print('paid maximum:',max(paid.values()))
print('ALL_PASS')
