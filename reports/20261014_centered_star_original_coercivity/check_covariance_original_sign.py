#!/usr/bin/env python3
"""Directed scalar checks for the full correlated original q0 block.
All omitted Gamma, theta and prime terms are paid analytically in the note.
"""
from fractions import Fraction as Q
import json
from mpmath import iv
iv.dps=55
I=lambda x:iv.mpf(str(x))
pi=iv.pi;a=I(7)*pi/5
lo=lambda x:float(x.a)
hi=lambda x:float(x.b)
def psi_lower(w):return iv.log(w)-1/(2*w)-1/(12*w*w)
minimum=None;worst=None
for k in range(1000):
    left=I(3)*k/10000;right=I(3)*(k+1)/10000
    val=(psi_lower(I('.25')+a*iv.exp(2*left))+psi_lower(I('.25')+a))/2-iv.log(pi)
    val+=sum(iv.exp(-(2*a+2*j+I('.5'))*right)/(2*a+2*j+I('.5')) for j in range(20))
    assert val.a>I('.5').b,(k,val)
    if minimum is None or val.a<minimum.a:minimum=val;worst=k
psi0=-iv.euler-pi/2-3*iv.log(2)
C0=iv.log(pi)-psi0
term=iv.exp(-8);H=I(0);P=I(0)
for k in range(1,61):
    term*=I(8)/k;H+=1/(I(k)-I('.75'));P+=term*H/2
far=-C0+(psi_lower(I('8.25'))-psi0)/2+P
assert far.a>I(43).b/50
assert pi.a>I(157).b/50
assert iv.exp(I(3)/5).a>I(91).b/50
assert iv.exp(I(3)/5).b<I(11).a/6
assert Q(7,5)*Q(157,50)*Q(91,50)>8
assert iv.exp(1).a>I(19).b/7
assert iv.exp(3).a>I(20).b
assert iv.exp(I(161)/110).a>I(25).b/6
# Reflected main lattice and its complete n<t/2 tail.
ref=Q(14,19)*Q(401,399)+Q(28,19)/20**4
assert ref<Q(149,200)
# Future and past rows each <1/1000.
future=Q(2,20**4)/(1-Q(3,2)/20**7)
past=Q(28,19)/20**4
assert future<Q(1,1000) and past<Q(1,1000)
assert ref+Q(2,1000)<Q(3,4)
# Entire compact reflected tail starts at n=3.
near_ref=Q(3,25)+Q(6,20**4)
assert near_ref+Q(2,1000)<Q(1,8)
pole=Q(40,567)
assert 1-Q(1,4)-pole>Q(1,10)
assert Q(43,25)-Q(3,2)-pole>Q(1,10)
report={
 'near_gamma_cells':1000,'near_gamma_min_lower':lo(minimum),
 'near_gamma_worst_cell':worst,'far_gamma_lower':lo(far),
 'reflected_lattice_majorant':str(ref),
 'pole_majorant':str(pole),
 'final_far_gap':str(Q(43,25)-Q(3,2)-pole),
 'certified_original_q0_gap':'1/10',
 'status':'all directed scalar and exact rational checks passed'}
print(json.dumps(report,indent=2))
