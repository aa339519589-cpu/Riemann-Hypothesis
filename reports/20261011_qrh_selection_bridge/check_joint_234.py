"""Exact certificate for the low-bin cubic--quadratic joint budget.
All mathematical comparisons use integers and fractions.Fraction.
This verifier reads a fixed rational covering; no search or floating-point
optimization is needed or performed.
"""
from fractions import Fraction as F
from math import lcm
from functools import reduce
from pathlib import Path
import json
K=F(13,16)
goal=F(-1,512)
def max_min(groups,lo,hi):
    raw=list(dict.fromkeys(line for group in groups for line in group))
    den=reduce(lcm,[c.denominator for line in raw for c in line],1)
    lines=[(int(a*den),int(b*den)) for a,b in raw]
    inds=[[raw.index(line) for line in g] for g in groups]
    pset={(lo.numerator,lo.denominator),(hi.numerator,hi.denominator)}
    for i,(a,b) in enumerate(lines):
      for c,d in lines[:i]:
        if a==c:continue
        p,q=d-b,a-c
        if q<0:p,q=-p,-q
        if lo.numerator*q<=p*lo.denominator and p*hi.denominator<=hi.numerator*q:
          from math import gcd
          z=gcd(p,q);pset.add((p//z,q//z))
    best=None;pt=None
    for p,q in pset:
      vals=[a*p+b*q for a,b in lines]
      num=min(max(vals[i] for i in g) for g in inds)
      val=F(num,den*q)
      if best is None or val>best:best,pt=val,F(p,q)
    return best,pt
def kl(m,v,u):return min(v+max(m,u,2*(m+u)/3),m+max(v,u))
def exact_density(m,v,a,x,y):
 c=m+v;J2=kl(m,v,c/2);J4=kl(m,v,c);kx=kl(m,v,x)
 tail,_=max_min([[(2*a-1,m+v),(2*a,v),(2*a-F(1,3),v+2*m/3)],[(2*a-1,m+v),(2*a,m)]],x,y)
 f2=(a-F(1,2))*y+(J2+kx)/2;f4=F(4,3)*((a-F(1,2))*y+J4/4+kx/2)
 return min(c,max(f2,tail),max(f4,tail))
def bound(m,v,r,a,ks=16,ls=12):
 c=m+v;mg=[[(a,F(0))]]
 for k in range(1,ks+1):
  mg.extend([[(a,(m-r)/(2*k)),(a-F(1,2),(m+v-r)/(2*k))],[(a,(v-r)/(2*k)),(a-F(1,2),(m+v-r)/(2*k)),(a-F(1,6),(v+2*m/3-r)/(2*k))]])
 sg=[[(1-a,F(0))],[(-a,c/2)]]
 for l in range(1,ls+1):
  first=(F(1,2)-a,(m+v-r)/(2*l))
  sg.extend([[first,(1-a,(m-r)/(2*l))],[first,(-a,c/2+(m-r)/(2*l))],[first,(1-a,(v-r)/(2*l)),(F(5,6)-a,(v+2*m/3-r)/(2*l))],[first,(-a,c/2+(v-r)/(2*l)),(F(1,6)-a,c/3+(v+2*m/3-r)/(2*l))]])
 mm,p=max_min(mg,F(0),F(1,6));bb,s=max_min(sg,F(0),c)
 return -F(29,96)-F(11,16)*a+r+mm+bb,(p,s)
if __name__=='__main__':
 rows=[list(map(F,x)) for x in json.loads(Path(__file__).with_name('joint_234_rational_rectangles.json').read_text())]
 endpoints=sorted({F(1,8),F(3,8)}|{a for r in rows for a in r[:2]})
 assert endpoints[0]==F(1,8) and endpoints[-1]==F(3,8)
 for lo,hi in zip(endpoints,endpoints[1:]):
  mid=(lo+hi)/2
  ranges=sorted((vl,vh) for al,ah,vl,vh,*_ in rows if al<mid<ah)
  cur=F(0)
  for vl,vh in ranges:
   assert vl==cur and vh>vl, ('coverage',lo,hi,cur,vl,vh)
   cur=vh
  assert cur==K/3, ('coverage_end',lo,hi,cur)
 worst=None
 for i,(al,ah,vl,vh,x,y,r,saved) in enumerate(rows,1):
  assert F(1,8)<=al<ah<=F(3,8) and F(0)<=vl<vh<=K/3 and 0<=x<=y
  m=(K-3*vl)/2;v=vh
  true_r=exact_density(m,v,ah,x,y)
  assert true_r<=r, ('density',i,true_r,r)
  val,_=bound(m,v,r,al)
  assert val==saved and val<=goal, ('budget',i,val,saved,goal)
  worst=val if worst is None else max(worst,val)
 print('ALL_PASS',len(rows),'rectangles; complete rational coverage; maximum',worst)
