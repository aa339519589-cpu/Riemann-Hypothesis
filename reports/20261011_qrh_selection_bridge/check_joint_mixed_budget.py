"""Exact rational verification of the finite certificate in QUADRATIC_DUAL_N1.md, Part XVIII B.
Only the displayed analytic majorants are checked; analytic inputs and physical
transfer are proved in the companion manuscripts. All mathematical comparisons
below use Python integers or fractions.Fraction.
"""
from fractions import Fraction as F
from math import lcm
from functools import reduce
from pathlib import Path
A=F(1,8);K=F(13,16);target=F(-1,6)

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

def bound(v,w,r,ks=16,ls=12):
 c=v+w
 mg=[[(A,F(0))]]
 for k in range(1,ks+1):
  mg.append([(A,(w-r)/(2*k)),(A-F(1,2),(v+w-r)/(2*k))])
  mg.append([(A,(v-r)/(2*k)),(A-F(1,2),(v+w-r)/(2*k)),(A-F(1,3),(v+5*w/6-r)/(2*k)),(A-F(1,12),(v+w/3-r)/(2*k))])
 sg=[[(1-A,F(0))],[(-A,c/2)]]
 for l in range(1,ls+1):
  first=(F(1,2)-A,(v+w-r)/(2*l))
  sg.extend([[first,(1-A,(w-r)/(2*l))],[first,(-A,c/2+(w-r)/(2*l))],
    [first,(1-A,(v-r)/(2*l)),(F(2,3)-A,(v+5*w/6-r)/(2*l)),(F(11,12)-A,(v+w/3-r)/(2*l))],
    [first,(-A,c/2+(v-r)/(2*l)),(F(1,3)-A,c/6+(v+5*w/6-r)/(2*l)),(F(1,12)-A,5*c/12+(v+w/3-r)/(2*l))]])
 m,p=max_min(mg,F(0),F(1,6));b,s=max_min(sg,F(0),c)
 return -F(29,96)-F(11,128)+r+m+b,(p,s,m,b)

def row(w,reg):
 v=(K-5*w)/3
 if reg==0:return w+2*v/5
 if reg==1:return 3*v/10+11*w/10
 if reg==2:return max(21*v/22+w/2,3*v/8+15*w/16)
 return v+F(55,118)*(w+v/6)

if __name__=='__main__':
 regions=[(F(7,100),F(13,128),0),(F(13,128),F(13,124),1),(F(13,124),F(91,800),2),(F(91,800),F(3,25),3)]
 todo=regions[:];out=[];n=0
 while todo:
  lo,hi,j=todo.pop();v=(K-5*lo)/3;w=hi;r=max(row(lo,j),row(hi,j))
  val,det=bound(v,w,r);n+=1
  if val<=target:
   out.append((lo,hi,j,val));print('PASS',str(lo),str(hi),j,str(val),flush=True)
  elif hi-lo<=F(1,200000):
   print('FAIL',lo,hi,j,val,det,flush=True);raise SystemExit(1)
  else:
   mid=(lo+hi)/2;todo.extend([(mid,hi,j),(lo,mid,j)])
 else:
  print('ALL_PASS',len(out),'tested',n,flush=True)
  with Path(__file__).with_name('joint_mixed_rational_intervals.txt').open('w') as f:
   for x in sorted(out):f.write(' '.join(map(str,x))+'\n')
