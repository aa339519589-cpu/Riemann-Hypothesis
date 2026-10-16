#!/usr/bin/env python3
"""Exact rational derivative/outer-power checks, with an Arb constant bound."""
from fractions import Fraction as Q
from math import prod
from flint import arb,ctx
from pathlib import Path
import json
ctx.prec=192
def B(q):
 q=Q(q);return arb(q.numerator)/q.denominator
s=Q(1,10**16);qm=Q(1,10**40);eps=Q(1,10**12)
fall=lambda x,n:prod((x-j for j in range(n)),start=Q(1))
assert min(abs(fall(Q(1,2),i)) for i in range(12))>=Q(1,4)
assert Q(13,12)**11*qm<Q(1,2)
series=32*12**11*qm
assert (1-24*s)*(1-series)>1-eps and 1+series<1+eps
kap=(Q(-1,15),Q(2,15),Q(7,30))
raw=[('main',(Q(0),Q(1),Q(1)),Q(-1,2)),('boundary',(Q(0),Q(1),Q(15,16)),Q(0)),('endpoint',(Q(-1,16),Q(17,16),Q(9,8)),Q(-7,16)),('derivative',(Q(1,24),Q(23,24),Q(19,24)),Q(7,24)),('constant',(Q(0),Q(1),Q(7,8)),Q(0))]
expected=[(Q(1,30),Q(14,15),Q(53,60)),(Q(0),Q(1),Q(15,16)),(Q(-1,30),Q(241,240),Q(491,480)),(Q(1,45),Q(359,360),Q(619,720)),(Q(0),Q(1),Q(7,8))]
rows=[]
for (name,p,h),want in zip(raw,expected):
 got=tuple(a+h*b for a,b in zip(p,kap));assert got==want
 rows.append({'name':name,'k':str(got[0]),'l':str(got[1]),'m':str(got[2])})
C=B(10**40)
coefs=[22*B(2).sqrt()+12*C**B('1/8')*B(2).sqrt(),12*C**B('1/8'),12*C**B('1/8')*B(8)**B('1/8')*B(2)**B('7/16'),12*C**B('1/8'),12*C**B('1/8')]
assert all(v<B(10**7) for v in coefs)
out={'status':'PASS','precision_bits':192,'shift_s':str(s),'series_q':str(qm),'relative_epsilon':str(eps),'series_relative_upper':str(series),'outer_rows':rows,'row_coefficients':[str(v) for v in coefs]}
Path(__file__).with_name('outer_assembly.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS: actual order-eleven and five common-length outer rows')
