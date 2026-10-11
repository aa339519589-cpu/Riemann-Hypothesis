from fractions import Fraction as F
from pathlib import Path
import json
K=F(13,16);GOAL=-F(3,16)-F(1,16384)
def ko(v,w,z):return min(w+max(v,z),v+max(w,z,5*w/6+z/3,w/3+5*z/6))
def density(v,w,a):
 c=v+w;d=3*a/(1+a);rr=[c,w+d*(v+w/3)]
 if a<=F(1,4):
  D=1-a-4*a*a;xA=(v+(1-3*a)*w)/D;xB=((2+a)*v+(3-a)*w)/(2-4*a*a)
  rr += [a/(1+a)*(v+4*w+2*max(xA,xB)),(ko(v,w,c/2)+2*c)*2*a/(1+2*a),(min(v+2*w,11*v/6+7*w/6)+4*c)*a/(1+a)]
 return min(rr)

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(t,x):return (t*x[0],t*x[1])
def k_groups(v,w,z):
 c=v+w
 return [[(F(0),c),add((F(0),w),z)],[(F(0),c),add((F(0),v),z),add((F(0),v+5*w/6),mul(F(1,3),z)),add((F(0),v+w/3),mul(F(5,6),z))]]
def smooth_groups(v,w,r,a,L=16):
 c=v+w;groups=[[(1-a,F(0))],[(-a,c/2)]]
 for l in range(1,L+1):
  l=F(l);base=(F(1,2)-a,-r/(2*l))
  for z in [(l,F(0)),(-l,l*c)]:
   for g in k_groups(v,w,z):groups.append([add(base,mul(1/(2*l),line)) for line in g])
   if l<2:continue
   groups.append([add(base,mul(1/(2*l),line)) for line in [(F(0),2*c),z]])
   zd=add((F(0),2*c),mul(-1,z))
   for kg in k_groups(v,w,zd):
    dg=[z]+[mul(F(1,2),add(add((F(0),r),z),line)) for line in kg]
    groups.append([add(base,mul(1/(2*l),line)) for line in dg])
 return groups

def covered(groups,level,lo,hi):
 intervals=[]
 for gi,group in enumerate(groups):
  l,h=lo,hi
  for a,b in group:
   if not a:
    if b>level:l,h=F(1),F(0);break
   elif a>0:h=min(h,(level-b)/a)
   else:l=max(l,(level-b)/a)
   if l>h:break
  if l<=h:intervals.append((l,h,gi))
 intervals.sort();cur=lo
 for l,h,_ in intervals:
  if l>cur:return False
  cur=max(cur,h)
  if cur>=hi:return True
 return cur>=hi

def certify(al,ah,wl,wh):
 v=(K-5*wl)/3;w=wh;c=v+w;r=density(v,w,ah)
 outside=-F(29,96)-F(11,16)*al+(al-F(1,8))/6+r
 return covered(smooth_groups(v,w,r,al),GOAL-outside,F(0),c),r

if __name__=='__main__':
 rows=[list(map(F,row)) for row in json.loads(Path(__file__).with_name('pair_qslot_rational_rectangles.json').read_text())]
 edges=sorted({F(1,8),F(1,4)}|{a for row in rows for a in row[:2]})
 assert edges[0]==F(1,8) and edges[-1]==F(1,4)
 for lo,hi in zip(edges,edges[1:]):
  mid=(lo+hi)/2;parts=sorted((wl,wh) for al,ah,wl,wh,*_ in rows if al<mid<ah);cur=F(0)
  for wl,wh in parts:assert wl==cur and wh>wl;cur=wh
  assert cur==K/5
 for n,(al,ah,wl,wh,rr) in enumerate(rows,1):
  assert F(1,8)<=al<ah<=F(1,4) and F(0)<=wl<wh<=K/5
  ok,r=certify(al,ah,wl,wh);assert ok and r==rr,(n,ok,r,rr)
 print('ALL_PASS',len(rows),'rational rectangles; complete S sublevel covers; goal',GOAL)
