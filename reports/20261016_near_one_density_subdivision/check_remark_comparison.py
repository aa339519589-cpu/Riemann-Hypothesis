"""Exact comparison to Pintz's growth-based Remark, not to unknown true mu.

The declared input envelope is ANTEDB Table 6.2 (read 2026-10-16),
with its full Heath-Brown tail, plus the curved bounds in Theorem 6.13.
This cannot certify absence of every result elsewhere in the literature.
"""
from fractions import Fraction as F
# (right endpoint, intercept, positive slope) of mu <= intercept-slope*sigma.
segments=[
(F(88225,153852),F(31,84),F(3,7)),
(F(521,796),F(220633,620612),F(62831,155153)),
(F(53141,76066),F(1333,3825),F(1508,3825)),
(F(454,641),F(405,1202),F(227,601)),
(F(1744,2411),F(779,2590),F(423,1295)),
(F(951057,1298878),F(179,622),F(96,311)),
(F(1389,1736),F(157319,560830),F(251324,841245)),
(F(587779,702192),F(2841,10316),F(754,2579)),
(F(7441,8695),F(1691,6554),F(890,3277)),
(F(277,300),F(29,130),F(3,13)),
]
pts=[(F(1,2),F(13,84))]
for s,a,b in segments: pts.append((s,a-b*s))
# The infinite HB sequence has decreasing delta; once delta<=eta,
# every subsequent point is outside the defining domain delta>eta.
for eta in (F(1,100), F(1,50)):
 p=pts[:]
 n=7
 while True:
  delta=F(3*n*n-3*n+2,n*(n-1)**2*(n+2))
  if delta<=eta:break
  p.append((1-delta,F(2,(n-1)**2*(n+2))))
  n+=1
 # On every affine segment mu/(1-sigma-eta) is monotone or constant.
 eligible=[(mu/(1-s-eta),s,mu) for s,mu in p if 1-s>eta]
 best=min(eligible)
 # Functional-equation reflection to sigma<1/2 cannot improve the f bound.
 mirrored=[((mu+s-F(1,2))/(s-eta),1-s,mu+s-F(1,2)) for s,mu in p]
 assert min(mirrored)[0]>best[0]
 # Best unrestricted delta for (2 sqrt(10)/13) delta^(3/2) is 3eta.
 # Its ratio minimum squared is (270/169)*eta, worse here.
 assert best[0]**2 < F(270,169)*eta
 # The sharper asymptotic curved bound is only valid below this delta.
 assert F(317,118272)<eta
 print('eta',eta,'best declared growth ratio',best,'last HB index',n-1)
 if eta==F(1,100):a=best[0];assert a==F(50,437)
 else:b=best[0];assert b==F(175,1033)
# Ceiling q=2 at the best supplied constants.
assert 1<b/a<2
A=max(4*a,3*b)
assert A==F(525,1033)>F(300,616)>F(300,617)
# Enlarging admissible constants cannot improve this minimum.
# q=1 costs >=4b; q>=3 requires b'>(q-1)a and costs >=2q*a>=6a.
assert 4*b>A and 6*a>A
print('Pintz Remark best from declared inputs: A=',A,'; E at .99=',A/100)
print('Compared density coefficients: old',F(300,616),'new',F(300,617))
