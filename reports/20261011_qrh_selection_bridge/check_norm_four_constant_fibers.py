#!/usr/bin/env python3
"""Exact norm-four fiber orthogonality, in Z[zeta_12].
The theta/cusp identification is a separate mathematical proof.
"""
from itertools import product

def mul(a,b):
 x,y=a;u,v=b
 return ((x*u-y*v)%4,(x*v+y*u-y*v)%4)
def norm(a):x,y=a;return(x*x-x*y+y*y)%4
def reduce12(v):
 z=list(v)
 for i in range(11,3,-1):
  c=z[i];z[i]=0;z[i-2]+=c;z[i-4]-=c
 return tuple(z[:4])
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
zero=(0,)*4
els=list(product(range(4),repeat=2))
unit_res=[(1,0),(0,1),(1,1)]
log3={(1,0):0,(0,1):1,(1,1):2}
for j in range(3):
 hats={}
 for t in els:
  v=[0]*12
  for A in els:
   q=norm(A)
   if q%2==0:continue
   psiexp=0 if q==1 else 6
   rhoexp=4*j*log3[(A[0]%2,A[1]%2)]
   v[(psiexp+rhoexp-3*mul(t,A)[1])%12]+=1
  hats[t]=reduce12(v)
  if t[0]%2==t[1]%2==0:assert hats[t]==zero,(j,t,hats[t])
 for c in unit_res:
  out=zero
  for t in els:
   if (t[0]%2,t[1]%2)==c:out=plus(out,hats[t])
  assert out==zero,(j,c,out)
 print('PASS: psi*rho^%d; nonunit Fourier zero; all three unit fibers sum zero'%j)
print('ALL_PASS')
