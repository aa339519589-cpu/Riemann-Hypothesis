#!/usr/bin/env python3
"""Exact actual C13 and common-length outer ledger for the double-partial-dual candidate."""
from fractions import Fraction as Q
from math import prod
from pathlib import Path
from flint import arb,ctx
import json
ctx.prec=192
def B(q):
 q=Q(q);return arb(q.numerator)/q.denominator
s=Q(1,10**30);qmax=Q(1,10**80);eps=Q(1,10**25)
fall=lambda x,n:prod((x-j for j in range(n)),start=Q(1))
assert min(abs(fall(Q(1,2),i)) for i in range(14))>=Q(1,4)
assert Q(16,15)**13*qmax<Q(1,2)
series=32*15**13*qmax
assert (1-500*s)*(1-series)>1-eps and (1+500*s)*(1+series)<1+eps
raw=[('main',Q(7,10),Q(3,10),Q(1,10)),('bx',Q(3,4),Q(1,4),Q(0)),('by',Q(3,4),Q(0),Q(1,4)),('inverse2',Q(4,5),Q(-1,20),Q(3,20)),('cap',Q(7,8),Q(-1,8),Q(0)),('short',Q(0),Q(1),Q(1,2)),('constant',Q(0),Q(1),Q(0)),('derivative2',Q(5,6),Q(0),Q(0)),('log2',Q(1,2),Q(0),Q(0)),('inverse1',Q(-1,2),Q(1),Q(1)),('derivative1',Q(1,3),Q(1),Q(0))]
rows=[]
for name,k,l,m in raw:
 h=7*k/8
 out=(k/8-h*Q(7,89),(7+l-k)/8+h*Q(14,89),(7+m-2*k)/8+h*Q(23,89))
 if name=='main':assert out==(Q(7,178),Q(82,89),Q(155,178))
 coeff=12*B(10**100)**B('1/8')
 if k<0:coeff*=B(8)**B('1/8')*B(2)**B(-h)
 if name=='main':coeff+=22*B(2).sqrt()
 assert coeff<10**16
 rows.append({'name':name,'raw_k':str(k),'raw_l':str(l),'raw_m':str(m),'k':str(out[0]),'l':str(out[1]),'m':str(out[2]),'coefficient_upper':str(coeff)})
out={'status':'PASS','precision_bits':192,'shift_s':str(s),'series_q':str(qmax),'relative_error':'1e-25','series_relative_bound':str(series),'outer_rows':rows,'common_coefficient':'1e16','outer_log_power':'1/2'}
Path(__file__).with_name('double_outer.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS: actual C13 derivative range and all eleven common-length outer rows')
