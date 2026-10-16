"""Exact certificate for a finite-pair Halasz/local-beta density envelope.
Analytic theorem hypotheses are proved in REPORT.md, not by this script.
Uses only the Python standard library.
"""
from fractions import Fraction as F

P=[(F(13,84),F(55,84)),(F(4742,38463),F(35731,51284)),
   (F(18,199),F(593,796)),(F(2779,38033),F(58699,76066)),
   (F(89,1282),F(997,1282))]
PAIRS=P+[(l-F(1,2),k+F(1,2)) for k,l in P]
M=[((4+6*k+8*l)/(k+l),-(3+4*k+6*l)/(k+l)) for k,l in PAIRS]
MP=[(a-1,b+1) for a,b in M]
ZP=[(F(3,4)/k,F(3,4)*(1-l/k)) for k,l in PAIRS]
COMMON=(F(9),F(-6))
LOCAL=(F(210,29),F(-519,116))
LOCAL_LO,LOCAL_HI=F(111,125),F(405,454)
BREAKS=list(map(F,['4282/4923','331/380','5902/6711','65223/73649',
                  '54214373/60832876','405/454','98/107','14/15']))
LINES=[(F(2003,181),F(-4282,543)),(F(237577,21419),F(-508151,64257)),
       (F(7449,665),F(-5323,665)),(F(1438001,126161),F(-1031827,126161)),
       LOCAL,(F(1923,178),F(-681,89)),COMMON]
LO,HI=BREAKS[0],BREAKS[-1]

def val(line,s):return line[0]*s+line[1]
def require(b,msg):
    if not b:raise ArithmeticError(msg)
def tau(s):
    for a,b,line in zip(BREAKS,BREAKS[1:],LINES):
        if a<=s<=b:return val(line,s)
    raise ValueError('outside claimed interval')
def derived(s):
    mont=min(val(COMMON,s),max(val(line,s) for line in MP))
    zeta=max(val(line,s) for line in ZP)
    if LOCAL_LO<=s<=LOCAL_HI:zeta=max(zeta,val(LOCAL,s))
    return min(mont,zeta)

# Full local-beta prefix: one local row, then the global v3 pair.
xlo,xhi=F(227,601),F(12,31)
m,c=F(173,280),F(29,280)
k,l=P[3]
require(m+c/xhi==F(85,96),'local right endpoint')
require(l-k+k/xhi==F(404995,456396),'global suffix endpoint')
require(max(m+c/xhi,l-k+k/xhi)<LOCAL_LO,'strict complete-prefix overlap')
for s in (LOCAL_LO,LOCAL_HI):
    alpha=c/(s-m)
    require(xlo<=alpha<=xhi,'local root within valid alpha interval')
    require(F(3,4)/alpha==val(LOCAL,s),'local zeta cap')
require(m+c/xlo==LOCAL_HI,'local left endpoint')

# Exact envelope comparison on every affine cell, not merely a sigma grid.
all_lines=MP+ZP+[COMMON,LOCAL]+LINES
cuts=set(BREAKS+[LOCAL_LO,LOCAL_HI])
for i,(a,b) in enumerate(all_lines):
    for c,d in all_lines[:i]:
        if a!=c:
            x=(d-b)/(a-c)
            if LO<x<HI:cuts.add(x)
cuts=sorted(cuts)
for lo,hi in zip(cuts,cuts[1:]):
    for s in (lo,(lo+hi)/2,hi):
        require(tau(s)==derived(s),'complete envelope mismatch at '+str(s))
        require(tau(s)>F(3,2),'nonempty density window')
for i in range(1,len(BREAKS)-1):
    require(val(LINES[i-1],BREAKS[i])==val(LINES[i],BREAKS[i]),'piece continuity')
print('Full Montgomery prefixes, complete zeta prefixes, all envelope joins: PASS')

# Table 11.1 endpoint conventions are retained literally.
def old(s):
    if s<F(7,8):return F(3)/(2*s)
    if s<F(279,314):return F(3)/(10*s-7)
    if s<=F(9,10):return F(24)/(30*s-11)
    if s<=F(31,34):return F(3)/(10*s-7)
    if s<F(14,15):return F(11)/(48*s-36)
    return F(391)/(2493*s-2014)

gain2=F(6866845,7719178)
def claimed_gain(s):return (LO<s<F(279,314)) or (gain2<s<HI)
# On each comparator/envelope cell, the sign numerator is affine. Add all
# its possible zeroes, and test both endpoint conventions and open cells.
tab=[(LO,F(7,8),3,2,0),(F(7,8),F(279,314),3,10,-7),
     (F(279,314),F(9,10),24,30,-11),(F(9,10),F(31,34),3,10,-7),
     (F(31,34),HI,11,48,-36)]
cc=set(BREAKS+[F(7,8),F(279,314),F(9,10),F(31,34),gain2])
for pl,pr,line in zip(BREAKS,BREAKS[1:],LINES):
    for tl,tr,C,D,E in tab:
        lo,hi=max(pl,tl),min(pr,tr)
        if lo>=hi:continue
        a,b=C*line[0]-3*D,C*line[1]-3*E
        if a:
            root=-b/a
            if lo<root<hi:cc.add(root)
cc=sorted(cc)
for i,s in enumerate(cc):
    require((3/tau(s)<old(s))==claimed_gain(s),'closed comparator at '+str(s))
    require(3/tau(s)<=F(3)/(2*s),'applicable Kerr comparison')
    if i+1<len(cc):
        u=(s+cc[i+1])/2
        require((3/tau(u)<old(u))==claimed_gain(u),'open comparator at '+str(u))
        require(3/tau(u)<F(3)/(2*u),'strict interior Kerr comparison')
require(old(F(9,10))-3/tau(F(9,10))==F(127,2458),'.9 convention')
require(old(F(31,34))-3/tau(F(31,34))==F(2771,53220),'31/34 convention')
print('Exact two table-improvement intervals and Kerr comparator: PASS')
for s in (F(7,8),F(22,25),F(89,100),F(891,1000),F(9,10),F(92,100)):
    e=3*(1-s)/tau(s);o=(1-s)*old(s)
    print('sigma',s,'tau',tau(s),'new exponent',e,'table exponent',o,'saving',o-e)
