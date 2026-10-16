#!/usr/bin/env python3
"""Exact rational checks for the local mixed logarithmic-dual lemma."""
from fractions import Fraction as Q
from math import prod
import json
from pathlib import Path

s=Q(1,10**12); qmax=Q(1,10**30); eps=Q(1,10**10); K=10**6
fall=lambda x,n:prod((x-j for j in range(n)),start=Q(1))
rise=lambda x,n:prod((x+j for j in range(n)),start=Q(1))
assert min(abs(fall(Q(1,2),i)) for i in range(6))>=Q(1,4)
assert Q(8,7)**9*qmax<Q(1,2)
series=32*7**9*qmax
assert series<13*10**8*qmax
assert (1-8*s)*(1-series)>1-eps
assert 1+series<1+eps
bounds=[]
for a in range(4):
 for b in range(4):
  v=rise(Q(3,2),a)*rise(Q(1,2),b)/8
  assert v*(1+eps)<4
  bounds.append({'a':a,'b':b,'upper_fraction':str(v*(1+eps))})
xx=Q(15,512)*(1-eps); yy=Q(3,512)*(1-eps)
det=(45*(1-eps)**2-9*(1+eps)**2)/(1024*256)
assert xx>Q(1,K) and yy>Q(1,K) and det>Q(1,K)
result={'status':'PASS','arithmetic':'exact rational','s':str(s),'qmax':str(qmax),'relative_epsilon':str(eps),'K':K,'series_relative_upper':str(series),'xx_lower':str(xx),'yy_lower':str(yy),'det_lower':str(det),'derivative_bounds':bounds}
out=Path(__file__).with_name('mixed_derivative_constants.json')
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print('PASS: all exact rational mixed-derivative bounds')
