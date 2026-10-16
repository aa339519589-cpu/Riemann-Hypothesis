#!/usr/bin/env python3
"""Exact two-variable certificate for the local-height Atkinson candidate.

Every cleared sign is a multi-affine polynomial on an exact rational rectangle,
so its four corner values certify the entire rectangle. This certifies parameter
algebra and identified comparisons only, not the new analytic local-height input.
"""
from fractions import Fraction as F
from itertools import product

S0,S1=F(17,20),F(87,100)
A0,A1=F(5,6),F(23,25)
V0,V1=F(365,2742),F(69,463)
checks=0

def require(ok,label):
    global checks
    if not ok: raise ValueError(label)
    checks+=1

def box(label,c=0,s=0,a=0,sa=0,lo=S0,hi=S1,al=A0,ah=A1,strict=True):
    # c+s*sigma+a*height_exponent+sa*sigma*height_exponent.
    vals=[F(c)+F(s)*x+F(a)*y+F(sa)*x*y
          for x,y in product((lo,hi),(al,ah))]
    require(min(vals)>0 if strict else min(vals)>=0,(label,vals))

def values(s,a):
    b1=2*(178*a+365)/(2742*s-1015)
    b2=3*a/(4*s)
    b=max(b1,b2)
    return b1,b2,b,b*(s-F(1,2))/2,2*(1-s)*b

box('D denominator',c=-1015,s=2742)
box('sigma positive',s=1)
box('eta positive',c=1,s=-1)
box('a positive',a=1)
box('a<1',c=1,a=-1)
box('B1<a',c=-730,a=-1371,sa=2742)
box('B2<a',a=-3,sa=4)
box('2B2>a',a=6,sa=-4)
box('v1>lower',c=-365+2030*V0,s=730-5484*V0,a=-178,sa=356)
box('v1<upper',c=365-2030*V1,s=5484*V1-730,a=178,sa=-356)
box('v2<upper',s=8*V1,a=F(3,2),sa=-3)
box('B1>1/(sigma+1/2)',c=1380,s=-2012,a=178,sa=356)

# Exact balance of the second LV row by B1.
AA,qq=F(543,178),F(1727,89)
require(AA-1==F(730,356),'high-row numerator constant')
require(qq/2-2==F(2742,356),'high-row denominator slope')
require(2-qq/4==F(-1015,356),'high-row denominator constant')
# First row: E-(1-6v)=B*(sigma+1/2)-1>0, already certified using B1.
# Offdiagonal: E-[a/2+(3-4sigma)*2B/3]=(2sigma/3)*(B-B2)>=0.
require(F(2,3)*F(3,4)==F(1,2),'exact offdiagonal B2 balance')

# B1/B2 equality lies inside the height rectangle for every sigma.
box('switch denominator',c=-3045,s=6802)
box('switch above amin',c=3045*A0,s=2920-6802*A0)
box('switch below amax',c=-3045*A1,s=6802*A1-2920)

# Ye gap is 2(1-sigma)*(a-B)>0 by the two B<a tests.
# Global 3(1-sigma)/(2sigma): compare B with 3/(4sigma).
box('global Kerr/table vs B1',c=-3045,s=5306,sa=-1424)
box('global Kerr/table vs B2',c=1,a=-1)

# Compare with any previous Bprev=n/(d1*sigma+d0), where Eprev=2eta*Bprev.
def prior(label,n,d1,d0,lo,hi):
    n,d1,d0=F(n),F(d1),F(d0)
    box(label+' denominator',c=d0,s=d1,lo=lo,hi=hi)
    box(label+' exceeds B1',c=-1015*n-730*d0,
        s=2742*n-730*d1,a=-356*d0,sa=-356*d1,lo=lo,hi=hi)
    box(label+' exceeds B2',s=4*n,a=-3*d0,sa=-3*d1,lo=lo,hi=hi)

# Frozen short-strip baseline on exactly its two original cells.
prior('frozen L',120,318,-125,F(775,906),F(625,726))
prior('frozen H',F(213,5),102,-35,F(625,726),F(2905,3354))
# Previous full-diagonal global D4 only where its theorem actually applies.
prior('global D4',F(1629,2),5831,-4104,F(433,500),S1)
# The newer global local-LV theorem overlaps this rectangle only at sigma=.87.
# B is increasing in a, so the amax value pays the complete endpoint segment.
require(values(S1,A1)[4]<F(780,3569),'global local-LV endpoint .87')

require(values(F(43,50),F(5,6))[4]==F(10780,50367),'E(.86,5/6)')
require(values(F(43,50),F(9,10))[4]==F(189,860),'E(.86,.9)')
# Local Atkinson/HM length algebra, independent of the density rectangle.
k,l=F(178,641),F(365,641)
nlo,nhi=F(1,3),F(641,1371)
require((1-4*V0)==nhi,'lower v endpoint and maximal n')
require(nhi<F(3,5),'primary N<T^(3/5) phase cap')
require(k*F(641,356)==F(1,2),'w-pair balance constant')
require(-k*F(1015,356)+(l-k)==-F(1,2),'w-pair balance slope')
for n in (nlo,nhi):
    wp=(641-1015*n)/356
    wc=F(3,4)-n/4
    require(wp>=n,'w-pair >= n at affine endpoint')
    require(wc>n,'phase-cap w > n at affine endpoint')
    require(wc<=(1+n)/2,'phase-cap implies W<=sqrt(TN)')
require(F(3,2)+F(1015,356)>0,'pair length exponent increasing')
require(F(7,4)>0,'cap length exponent increasing')
require(AA-qq*V1==F(3,2)-9*V1,'pair/cap crossing')
require(qq>9,'pair dominates cap below crossing')
require(1-F(6)*V1-(A1+F(1,2)-9*V1)>0,
        'one-cell row dominates cap at crossing and above')
require(6>2 and qq>2,'truncated high2 level summation slopes')
require(F(13,84)>V1,'pointwise level above cap crossing')

print('PASS',checks,'exact identities and multi-affine rectangle signs')
print('sigma rectangle:',S0,S1,'height rectangle:',A0,A1)
print('Switch: a=2920sigma/(6802sigma-3045)')
for s,a in product((S0,S1),(A0,A1)):
    b1,b2,b,v,e=values(s,a)
    print('corner',s,a,'B',b,'v',v,'E',e,'active',1 if b1>=b2 else 2)
print('First local row is strict; second local row and offdiagonal have intentional balances.')
print('No analytic short-height moment theorem, effective bound, or zero-fraction claim.')

FIRST_RECTANGLE_CHECKS=checks

# Second rectangle, including its full declared comparator envelope.
#!/usr/bin/env python3
"""Exact parameter certificate for the retained-one-cell second rectangle.

The analytic localized large-values estimate is a separate premise. All signs
below are multi-affine, so exact four-corner checks prove the entire rectangle.
No sample-grid evidence, finite-height exclusion, or novelty claim is used.
"""
from fractions import Fraction as F
from itertools import product

S0,S1=F(87,100),F(9,10)
A0,A1=F(3,4),F(43,50)
V0,V1=F(365,2742),F(69,463)
checks=0

def require(ok,label):
    global checks
    if not ok: raise ValueError(label)
    checks+=1

def box(label,c=0,s=0,a=0,sa=0,lo=S0,hi=S1,al=A0,ah=A1,strict=True):
    require(lo<=hi and al<=ah,label+' interval')
    vals=[F(c)+F(s)*x+F(a)*y+F(sa)*x*y
          for x,y in product((lo,hi),(al,ah))]
    require(min(vals)>0 if strict else min(vals)>=0,(label,vals))

def values(s,a):
    bs=(1/(s+F(1,2)),2*(178*a+365)/(2742*s-1015),3*a/(4*s))
    b=max(bs)
    return bs,b,b*(s-F(1,2))/2,2*(1-s)*b

box('D positive',c=-1015,s=2742)
box('sigma positive',s=1)
box('eta positive',c=1,s=-1)
box('a positive',a=1)
box('a<1',c=1,a=-1)
box('B0<a',c=-1,a=F(1,2),sa=1)
box('B1<a',c=-730,a=-1371,sa=2742)
box('B2<a',a=-3,sa=4)
box('2B2>a',a=6,sa=-4)
# v=max(v0,v1,v2): B0 provides the lower bound, all branches the upper.
box('v(B0)>lower',c=-F(1,2)-V0,s=1-2*V0)
box('v(B0)<upper',c=F(1,2)+V1,s=2*V1-1)
box('v(B1)<upper',c=365-2030*V1,s=5484*V1-730,a=178,sa=-356)
box('v(B2)<upper',s=8*V1,a=F(3,2),sa=-3)
box('G shorter than ordinate interval',c=-2*V1,a=1)
box('third local row paid above crossing',c=F(1,2)+3*V1,a=-1)

AA,qq=F(543,178),F(1727,89)
require(AA-1==F(730,356),'high-row numerator constant')
require(qq/2-2==F(2742,356),'high-row denominator slope')
require(2-qq/4==F(-1015,356),'high-row denominator constant')
# E-(1-6v)=B*(sigma+1/2)-1 >=0 by B>=B0.
# E-[a/2+(3-4sigma)*2B/3]=(2sigma/3)*(B-B2)>=0.
require(F(2,3)*F(3,4)==F(1,2),'offdiagonal balance')

# Pairwise branch crossings. These give an exact max-envelope partition;
# no inequality in the certificate assumes a branch order.
# B0=B1: a=(1006sigma-690)/(178sigma+89).
# B0=B2: a=4sigma/[3(sigma+1/2)].
# B1=B2: a=2920sigma/(6802sigma-3045).
sstar=F(1035,1153)
astar=F(2760,3223)
bs=values(sstar,astar)[0]
require(bs[0]==bs[1]==bs[2],'triple crossing')
require(S0<sstar<S1 and A0<astar<A1,'triple crossing in rectangle')

# A prior exponent Eprev=2eta*n/(d1*sigma+d0).
def prior(label,n,d1,d0,lo=S0,hi=S1):
    n,d1,d0=F(n),F(d1),F(d0)
    box(label+' denominator',c=d0,s=d1,lo=lo,hi=hi)
    box(label+' exceeds B0',c=n/2-d0,s=n-d1,lo=lo,hi=hi)
    box(label+' exceeds B1',c=-1015*n-730*d0,
        s=2742*n-730*d1,a=-356*d0,sa=-356*d1,lo=lo,hi=hi)
    box(label+' exceeds B2',s=4*n,a=-3*d0,sa=-3*d1,lo=lo,hi=hi)

# Ye 2a eta follows directly from B<a.
prior('Kerr coefficient',F(3,4),1,0)
# Identified primary density table, on its actual sigma cells.
prior('table below 7/8',F(3,4),1,0,S0,F(7,8))
prior('table 7/8..279/314',F(3,2),10,-7,F(7,8),F(279,314))
prior('table 279/314..9/10',12,30,-11,F(279,314),S1)
# The finite-pair/local-beta seven-piece envelope.
for label,lo,hi,n,d1,d0 in [
 ('envelope1',S0,F(331,380),F(1629,2),6009,-4282),
 ('envelope2',F(331,380),F(5902,6711),F(192771,2),712731,-508151),
 ('envelope3',F(5902,6711),F(65223,73649),F(1995,2),7449,-5323),
 ('envelope4',F(65223,73649),F(54214373,60832876),F(378483,2),1438001,-1031827),
 ('envelope5',F(54214373,60832876),F(405,454),174,840,-519),
 ('envelope6',F(405,454),S1,267,1923,-1362),
]: prior(label,n,d1,d0,lo,hi)
# Full-diagonal CDV report on its four actual cells.
c1,c2,c3=F(8751,10033),F(2589,2923),F(136744872,153875459)
for args in [
 ('CDV D4',F(1629,2),5831,-4104,S0,c1),
 ('CDV H4',1896,11929,-8119,c1,c2),
 ('CDV H3',223770,1415129,-964637,c2,c3),
 ('CDV I4',1086,2742,-1015,c3,F(89,100)),
]: prior(*args)
# EP-Gram low interval. Both expressions can be compared on the full interval;
# this is stronger than comparing only their maximum.
prior('EP D4',F(1629,2),5831,-4104,F(873,1000),F(111,125))
prior('EP I4',1086,2742,-1015,F(873,1000),F(111,125))
# Newer global local-LV on its two actual cells.
prior('local-LV L',90,661,-468,S0,F(696,797))
prior('local-LV H',F(639,2),2227,-1557,F(696,797),F(219,250))

require(values(F(9,10),F(3,4))[3]==F(1,7),'E(.9,.75)')
require(F(1,7)<F(3,20),'example vs Ye')
require(F(1,7)<F(178,1229),'example vs global envelope')
print('PASS',checks,'exact identities and whole-rectangle signs')
print('sigma:',S0,S1,'height:',A0,A1)
print('Triple crossing:',sstar,astar)
for s,a in product((S0,S1),(A0,A1)):
    bs,b,v,e=values(s,a)
    print('corner',s,a,'B',b,'v',v,'E',e,'active',bs.index(b))
print('Intentional balances require B+xi before exponent-loss absorption.')
print('Arithmetic only: the localized analytic input remains a separate gate.')

# The first rectangle also meets the first Halasz cell below sigma=.87.
# Retain its different height range explicitly rather than relying on transitivity.
lo,hi=F(4282,4923),F(87,100)
al,ah=F(5,6),F(23,25)
n,d1,d0=F(1629,2),F(6009),F(-4282)
box('first rectangle Halasz denominator',c=d0,s=d1,lo=lo,hi=hi,al=al,ah=ah)
box('first rectangle Halasz vs B0',c=n/2-d0,s=n-d1,lo=lo,hi=hi,al=al,ah=ah)
box('first rectangle Halasz vs B1',c=-1015*n-730*d0,s=2742*n-730*d1,
    a=-356*d0,sa=-356*d1,lo=lo,hi=hi,al=al,ah=ah)
box('first rectangle Halasz vs B2',s=4*n,a=-3*d0,sa=-3*d1,
    lo=lo,hi=hi,al=al,ah=ah)
print("TOTAL PASS",FIRST_RECTANGLE_CHECKS+checks,"exact checks across both rectangles")
