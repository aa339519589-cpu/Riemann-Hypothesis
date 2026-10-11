#!/usr/bin/env python3
"""Exact rational certificate for a necessary coefficient; no RH conclusion."""
from fractions import Fraction as F
from math import comb
import json
N=24
zero=F(0)
def add(p,q):
 o=[zero]*max(len(p),len(q))
 for i,v in enumerate(p):o[i]+=v
 for i,v in enumerate(q):o[i]+=v
 return o
def mul(p,q):
 o=[zero]*(len(p)+len(q)-1)
 for i,v in enumerate(p):
  for j,w in enumerate(q):o[i+j]+=v*w
 return o
def scale(p,c):return [v*c for v in p]
b=[F(1)];U=[zero];S=zero
for n in range(1,N+1):
 b.append(b[-1]*F(-(2*n-1)**2,8*n));S+=F(1,(2*n-1)**2);U.append(-8*b[-1]*S)
Mom=[b]
for m in range(N+1):
 q=Mom[-1];Mom.append([q[l]+F(2*l-1,2)*(q[l-1] if l else 0) for l in range(N+1)])
def get(q,k):return q[k] if k>=0 else zero
Target=[(get(U,n)-6*get(U,n-1)+(18-6*n)*get(U,n-2))/4 for n in range(N+1)]
Cols={}
for j in range(1,N+1):
 L=N-j;A=[[zero]*(L+1) for _ in range(L+1)];B=[[zero]*(L+1) for _ in range(L+1)]
 for n in range(L+1):
  for k in range((n+1)//2,n+1):
   m=2*k-n;d=F((-1)**k*comb(j+k-1,k)*comb(k,n-k)*2**m)
   for ell in range(n,L+1):
    A[ell][n]+=d*Mom[m][ell-n];B[ell][n]+=d*Mom[m+1][ell-n]
 C=[]
 for ell in range(L+1):
  p=A[ell][:]
  if ell>=2:p=add(p,scale(A[ell-2],F(9)))
  if ell>=1:p=add(p,scale(B[ell-1],F(-6)))
  C.append(p[:ell+1])
 Cols[j]=C
D={}
for j in range(1,N+1):
 p=[Target[j]]
 for i in range(1,j):p=add(p,scale(mul(D[i],Cols[i][j-i]),F(-1)))
 assert len(p)<=j
 D[j]=p
assert D[1]==[F(1,4)]
assert D[2]==[F(-1,8),F(1,2)]
# Machin identity, alternating rational arctangent enclosures.
def atan_bounds(q,n):
 s=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),zero)
 rem=F(1,(2*n+1)*q**(2*n+1))
 return (s,s+rem) if n%2==0 else (s-rem,s)
x=atan_bounds(5,120);y=atan_bounds(239,40)
lo=16*x[0]-4*y[1];hi=16*x[1]-4*y[0]
Q=10**100
pi_lo=F((lo*Q).numerator//(lo*Q).denominator,Q)
pi_hi=F((hi*Q).numerator//(hi*Q).denominator+1,Q)
assert pi_lo<lo<hi<pi_hi
A=(2*pi_lo,2*pi_hi)
def imul(p,q):
 vals=[v*w for v in p for w in q];return min(vals),max(vals)
def peval(p,I):
 out=(zero,zero)
 for c in reversed(p):
  out=imul(out,I);out=(out[0]+c,out[1]+c)
 return out
def c_interval(j):
 num=peval(D[j],A);den=((4*A[0])**j,(4*A[1])**j)
 return imul(num,(1/den[1],1/den[0]))
intervals={j:c_interval(j) for j in range(1,N+1)}
assert all(intervals[j][0]>0 for j in range(1,24))
assert intervals[24][1]<0
# Output exact outward rounded decimal bounds, retaining rational polynomial witness.
def outward(I,places=50):
 q=10**places
 low=(I[0]*q).numerator//(I[0]*q).denominator
 high=(I[1]*q).numerator//(I[1]*q).denominator+1
 return {'lower_numerator':str(low),'upper_numerator':str(high),'denominator':str(q)}
result={'status':'EXACT_RATIONAL_CERTIFICATE_PASSED','meaning':'Necessary formal Gram coefficient c_24 is negative; mathematical asymptotic necessity is proved separately. No RH conclusion.','N':N,'pi_enclosure':outward((pi_lo,pi_hi),100),'c24_enclosure':outward(intervals[24]),'c1_to_c23_positive':True,'D24_coefficients_low_to_high':[str(v) for v in D[24]],'formula':'c_j = D_j(2*pi)/(8*pi)^j'}
print(json.dumps(result,indent=2))
