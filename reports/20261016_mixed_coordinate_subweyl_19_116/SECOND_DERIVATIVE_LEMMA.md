# Explicit two-dimensional second-derivative lemma

Status: complete local lemma independently checked; its global application is proved in the accompanying report. This does not use an implicit-constant multidimensional theorem. Every boundary and Fourier-tail row is retained. Its application is to a coordinate difference of the actual first dual logarithmic phase, not to the relatively degenerate undifferenced phase.

## 1. Statement

Let M,N>=2, F>=1, K>=1. Let f be real and C^6 on a closed rectangle of side lengths M,N. For all 1<=a+b<=6 with a<=3,b<=3 (also pure derivatives up to3), assume

|partial_x^a partial_y^b f| <= K F M^(-a) N^(-b).

Assume |f_xx|>=F/(K M²), |f_yy|>=F/(K N²), and

|det Hess f| >= F²/(K M²N²).

In addition assume either the Hessian is everywhere positive or negative definite, or its two diagonal entries have opposite signs. Then the proposed explicit lattice sum bound, uniformly for every subrectangle, is

|sum exp(2 pi i f(m,n))| <= 20000 K^4 log(2+K²F) [F+M+N+MN/F].       (1)

The constants refer to the displayed original rectangle. Arbitrary endpoint conventions change at most2(M+N)+4 points, which the right side absorbs. This is deliberately not a sharp constant.

## 2. Integral bound independent of the linear frequency

Scale to coordinates X,Y in a rectangle inside[0,1]². Write Phi=f(MX,NY)-pX-qY. Its Hessian entries are bounded byKF, diagonal absolute values below byF/K, and determinant below byF²/K. The gradient map is injective:

- for a definite Hessian, use strict monotonicity of grad Phi or its negative;
- for opposite diagonal signs, after changing overall sign if needed, (Phi_X,-Phi_Y) is strictly monotone, since the off-diagonal terms cancel in its quadratic differential.

Thus area substitution through grad Phi has density at mostK/F². Its image has area at most2K²F², by the upper determinant bound. These assertions hold on every subrectangle and for every p,q.

Put a=sqrt(F). Choose the radial Lipschitz cutoff chi(r)=0 forr<=a, (r-a)/a fora<r<2a, and1 forr>=2a. The omitted part of the integral has absolute value at most4pi K/F. For V=chi(|grad Phi|) grad Phi/|grad Phi|²,

|div V| <= 2KF/(a r) 1_(a<r<2a) +6KF/r² 1_(r>a).

The first integral is at most4pi K²/F by gradient substitution. For the second, radial rearrangement over a set of area<=2K²F² gives

integral_(gradient image,r>a) r^(-2) <= pi log(1+2K²F).

Each straight boundary edge satisfies

integral |V| <= 2K/F [1+log(1+K sqrt(F))],

using the monotonic relevant tangential gradient component and its derivative>=F/K. The divergence identity with exp(2pi i Phi) therefore gives the safe uniform bound

|integral_rect exp(2pi i Phi)| <= 100 K² F^(-1) log(2+K²F).            (2)

Approximation of the Lipschitz radial cutoff is legitimate; all displayed estimates are integrable. Rescaling multiplies(2) byMN.

## 3. Exact smoothing and central Fourier rectangle

If the integer points of one axis interval run from m0 through m1, retain m0+2 through m1−2. Use unit quintic transitions on[m0+1,m0+2] and[m1−2,m1−1], and the intervening plateau, which may be a single point. Both transitions lie strictly inside the original axis interval. If m1−m0<4, discard that entire thin subrectangle: at most four rows are lost, covered by the same perimeter allowance. Applying this construction in both axes gives a product cutoff w(x)v(y), with values1 at all retained lattice points, values0 at all other lattice points, and support inside the original rectangle. The quintic step10t³-15t⁴+6t⁵ gives

0<=w,v<=1; integral|w'|,integral|v'|<=2;
integral|w''|,integral|v''|<=8;
integral w<=M, integral v<=N.

The discarded strip contains at most4(M+N)+16 points, also absorbed in(1). Integration by parts in both cutoff variables and(2) bound every Fourier coefficient by

400 K² MN/F log(2+K²F).                                             (3)

Poisson summation is exact for this C² compactly supported amplitude; the absolute Fourier convergence is also proved by the tail estimates below.

Take Bx=2KF/M+2 and By=2KF/N+2. The central rectangle |k|<=Bx, |l|<=By has at most(4KF/M+5)(4KF/N+5) lattice frequencies. Its total is at most

400 K² log(2+K²F) [16K²F+20K(M+N)+25MN/F].                          (4)

## 4. One far frequency

Let phi=f-kx-ly, |k|>Bx, delta_x=|k|/2. Then |phi_x|>=delta_x>=KF/M+1. Define T_x a=partial_x(a/phi_x). Twice integrating by parts gives

T_x² w = w''/phi_x² -3w'f_xx/phi_x³ -w f_xxx/phi_x³ +3w f_xx²/phi_x⁴.

Its absolute x integral is <=18 delta_x^(-2): the four contributions are bounded by8,6/M,1/M,3/M times delta_x^(-2). Consequently the Fourier coefficient is <=4N/k² after the factor(2pi)^(-2). Summing |k|>Bx and |l|<=By gives at most

8N(4KF/N+5)/(2KF/M+1) <=16M+40N.

The symmetric one-far range gives at most40M+16N. No oscillation in the other variable is discarded without this complete frequency count.

## 5. Both far frequencies

Write b=T_x² w. Since |partial_y^j phi_x|<=delta_x N^(-j) forj=1,2, and the mixed derivative bounds hold, the product rule gives

integral_x |b| <=18 delta_x^(-2),
integral_x |b_y| <=62 delta_x^(-2)/N,
integral_x |b_yy| <=350 delta_x^(-2)/N².

For clarity, the denominator derivative factors for P^(-s), P=phi_x, are1,s,s(s+2). The four terms of b contribute, after x integration:

j=0: 8+7/M+3/M;
j=1: 16+28/M+18/M;
j=2: 64+154/M+132/M.

For B=b v, integrating in both variables gives

integral|B_yy|<=742 delta_x^(-2),
integral|B_y|<=98 delta_x^(-2),
integral|B|<=18N delta_x^(-2).

If |l|>By and delta_y=|l|/2, apply T_y² to B. The four contributions total at most

(742+294+18+54) delta_x^(-2)delta_y^(-2)=1108 delta_x^(-2)delta_y^(-2).

The factor(2pi)^(-4) is less than1/1108. Hence the coefficient is at most16/(k²l²). Its sum over both far ranges is at most64. This proves the claimed absolute Fourier convergence and pays the full double tail.

Combining(4), both one-far estimates, the double tail and discarded lattice rows proves(1), subject to independent checking of the hypotheses and endpoint construction.

## 6. Scope and missing application

For a monomial F X^alpha Y^beta, the scaled Hessian determinant is alpha beta(1-alpha-beta) F² X^(2alpha-2)Y^(2beta-2). The coordinate-differenced leading phase r^(-1/2)nu^(1/2) has opposite-sign diagonal entries and nonzero determinant. By contrast the undifferenced sqrt(r nu) model has determinant0.

A zeta application still needs the actual mixed-derivative comparison after finite differences, the complete curved-domain or rectangle partition, the multidimensional A recurrences and all small-parameter complements. None is supplied by this local screen, and no new zeta bound is claimed.
