#!/usr/bin/env python3
from fractions import Fraction as F
import json

def fac(n):
 f={};d=2
 while d*d<=n:
  while n%d==0:f[d]=f.get(d,0)+1;n//=d
  d+=1
 if n>1:f[n]=f.get(n,0)+1
 return f

def mu(n):
 f=fac(n)
 return 0 if any(v>1 for v in f.values()) else (-1)**len(f)
def a(n,N):return 1-mu(n)*(n<=N)
primes=[p for p in range(2,101) if fac(p)=={p:1}]
cases=0
for N in [2,3,4,5,7,11,19,37,61,101,211]:
 for p in primes:
  for m in range(1,251):
   j=F(a(p*m,N)-a(p,N))-F(a(2*p,N)-a(p,N),2)*a(m,N)
   assert abs(j)<=1
   if m<=2 or p>N:assert j==0
   jf=F(1-mu(p*m)-(1-mu(p)))-F((1-mu(2*p))-(1-mu(p)),2)*(1-mu(m))
   if p*m<=N:assert j==jf
   assert abs(j-jf)<=2
   if j:assert p*m>=6
   cases+=1
  # Every higher prime-power parent profile is constant1.
  for k in [2,3]:
   assert all(a(p**k*m,N)==1 for m in range(1,31))
# Exact finite covariance and positive-union formula on arbitrary posterior.
weights=[F(1,2**n) for n in range(1,9)]
sumw=sum(weights);weights=[w/sumw for w in weights]
for N in range(2,13):
 vals=[F(mu(m)*(m<=N)) for m in range(1,9)]
 mean=sum(w*v for w,v in zip(weights,vals))
 var=sum(w*v*v for w,v in zip(weights,vals))-mean*mean
 assert 0<mean<1
 for p in [2,3,5,7,11,13]:
  par=[F(mu(p*m)*(p*m<=N)) for m in range(1,9)]
  gamma=-(sum(w*x*y for w,x,y in zip(weights,vals,par))-mean*sum(w*y for w,y in zip(weights,par)))
  missing=sum(weights[m-1]*mu(m)**2*(1-mean*mu(m)) for m in range(1,9) if m<=N and (m%p==0 or p*m>N))
  assert var-gamma==missing and 0<=gamma<=var
print(json.dumps({'affine_incidence_cases':cases,'first_possible_parent':6,'status':'all exact checks passed'},sort_keys=True,indent=2))
