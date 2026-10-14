#!/usr/bin/env python3
"""Exact centered star algebra and independent scalar integral checks."""
from fractions import Fraction as F
import json
import mpmath as mp
px=[F(1,2),F(1,3),F(1,6)]
py=[F(3,4),F(1,6),F(1,12)]
checked=0
for zx in [[F(1),F(3),F(-2)],[F(-2),F(1,3),F(5,2)],[F(1)]*3]:
 for zy in [[F(-1),F(2),F(4)],[F(3,2),F(-5),F(7,3)],[F(1)]*3]:
  ux=sum(p*z for p,z in zip(px,zx)); uy=sum(p*z for p,z in zip(py,zy))
  h=[z-ux for z in zx]; dp=[p-q for p,q in zip(px,py)]
  star=px[0]*(zx[0]-zy[0])**2
  for n in range(1,3):
   star+=py[n]*(zx[n]-zy[n])**2+dp[n]*(zx[n]-zy[0])**2
  diag=sum(p*(a-b)**2 for p,a,b in zip(py,zx,zy))
  row=sum(d*v*v for d,v in zip(dp,h))
  mixed=2*(ux-zy[0])*sum(d*v for d,v in zip(dp,h))
  assert star==diag+row+mixed
  assert star-(ux-uy)**2>=0
  checked+=1
mp.mp.dps=45
kap=lambda h: mp.exp(-h/2)/(-mp.expm1(-2*h))
def ratio(z,h):
 a=mp.mpf('1.5')/z
 return mp.exp(mp.mpf('4.5')*h-z*mp.expm1(2*h))*(1-a*mp.exp(-2*h))/(1-a)
beta=lambda z:(2*z-mp.mpf('.5'))/(2*z*(z-mp.mpf('1.5')))
score=lambda z:mp.mpf('4.5')+6/(2*z-3)-2*z
errors=[]
for z,w in [(mp.pi,4*mp.pi),(mp.mpf(5),mp.mpf(17)),(mp.mpf(9),mp.mpf(4))]:
 def fun(h):
  if h<mp.mpf('1e-24'): return (score(z)-score(w))/2
  return kap(h)*(ratio(z,h)-ratio(w,h))
 got=mp.quad(fun,[0,mp.mpf('.01'),mp.mpf('.1'),1,4])
 want=mp.log(w/z)/2+beta(z)-beta(w)
 err=abs(got-want); errors.append(float(err)); assert err<mp.mpf('1e-23')
for x,n in [(mp.mpf('.1'),1),(mp.mpf('.4'),2),(mp.mpf('1'),3)]:
 z=mp.pi*mp.exp(2*x)*n*n; a=mp.mpf('1.5')/z
 q=mp.exp(-4*x); b=1-q
 want=mp.exp(-x)/(2*(1-a))*(1/z**2+(1+q-a)/z+q*(q-a)*mp.exp(z*b)*mp.e1(z*b))
 got=mp.quad(lambda h:kap(2*x+h)*ratio(z,h),[0,mp.mpf('.01'),mp.mpf('.1'),1,4])
 err=abs(got-want); errors.append(float(err)); assert err<mp.mpf('1e-35')
print(json.dumps({'exact_centered_star_cases':checked,'scalar_integral_max_error':max(errors),
 'complete_signed_positivity':'NOT PROVED'},indent=2))
