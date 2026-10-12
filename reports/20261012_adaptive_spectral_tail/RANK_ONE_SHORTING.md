# Executed rank-one instance of the user's threshold shorting

This supplement verifies an actual rank-one threshold repair of the unchanged original even theta jump form. Two directed-interval programs certify

    E(q) >= (7/16) Var_nu(q)

on its complete original even form domain. The mathematical contribution is a fully executed instance of the user's finite-rank repair mechanism, including the true defect column, a signed two-Rayleigh squared-trace criterion and complete continuous tails. The construction is the user's [exact threshold shorting theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1d739d991b6ecf52ec8998431407f30814f0654c/reports/20261012_threshold_shorted_certificates/REPORT.md), with its [original review](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1d739d991b6ecf52ec8998431407f30814f0654c/reports/20261012_threshold_shorted_certificates/AUDIT.md).

The already certified [511/1024 lower bound](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/7875713d6dffef90d6538e3f2a3db25a742e3539/reports/20261012_adaptive_spectral_tail/CERTIFIED_MULTIBAND_GAP.md) is stronger. The present theorem verifies a different mechanism at epsilon=1/16; it does not improve that strongest bound, prove an all-epsilon sign result or establish RH.

## Original-domain and computational dependencies

The original source identity and complete maximal-form realization have the user's self-contained proof [ORIGINAL_FORM_FOUNDATION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/d50c8734afd4e7386a5e04e63c15a12f1067dfe8/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md). The complete prime-tail constant and explicit original theta bounds are [REPORT.md, Section 1](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/d50c8734afd4e7386a5e04e63c15a12f1067dfe8/reports/20261012_adaptive_spectral_tail/REPORT.md). All inequalities here are understood as closed-form inequalities on the full form domain.

The genuine threshold vector used below can also be obtained directly: the source identity is (a(D)-S)Phi=-cosh(x/2). Applying d^2/dx^2-1/4 gives (a(D)-S)(Phi''-Phi/4)=0. Its double-exponential theta tails put w=(Phi''-Phi/4)/m in L2 and its source in the operator domain, hence H w=0. This uses the complete original source, not a truncated equality.

The [independent review](REFEREE_RANK_ONE_SHORTING.md) covers the complete analytic argument and an independent execution of both programs at 40,000 cells. The [reproduction package](rank_one_certificate) contains both unchanged interval programs, both actual outputs and the exact manifest. It requires no binary trial input or exploratory eigenvectors. Program-level historical candidate/pending labels are retained verbatim; theorem approval is recorded in the proof and independent review.

## 1. Exact original comparison and threshold column

On the original full even L2(dx) space write

H = m b(D) m - C0 m^2 - m S m = U L U^{-1} - 1/2,

with m^2=Phi/(2 cosh(x/2)), the full positive even theta Phi, and the same
C0, b and prime-power coefficients as in the published original operator.
Take J=N=6, epsilon=1/16, and

Astar=4 pi^2 (125/121),
delta=(20 Astar/9) 49 exp(-7 pi),
lambda_j=2j+1/2 (0<=j<6),
c=sum_(j<6) (j+1/4)^{-1},
R(x)=sum_(j<6) exp(-lambda_j |x|),
p6(x)=m(x) sum_(n=2,3,4,5) alpha_n [m(x+log n)+m(x-log n)],
d(x)=epsilon-delta+(c-C0)m(x)^2-p6(x).

Here alpha_2=log2/sqrt2, alpha_3=log3/sqrt3,
alpha_4=log2/2, alpha_5=log5/sqrt5; Lambda(6)=0.
The complete omitted-prime operator has norm at most delta. Thus
K=M_d-m(R*)m <= H+epsilon.
The bounded offset A=K-epsilon does not depend on epsilon.

Use the genuine threshold column

f=Phi''-Phi/4,  w=f/m,  H w=0,
b_col=-A w=m(R*f)-(d-epsilon)w,
g=<w,b_col>>0.

The user's theorem gives F=b_col b_col*/g <= H-A, and therefore
K+F<=H+epsilon on the complete original form domain. It also gives
(K+F)w=epsilon w exactly. No assertion about exhaustion of ker H is used.

## 2. A signed two-Rayleigh squared-trace test

Assume d>=1/50, to be certified on the entire real axis. Transfer even L2(R)
unitarily to L2(0,infinity), using v -> sqrt(2)v. Put

a=m/sqrt(d),
z=sqrt(2)b_col/sqrt(d),
T(x,y)=a(x)a(y) sum_j [exp(-lambda_j|x-y|)+exp(-lambda_j(x+y))],
T_c=T-z z*/g.

Then K+F is congruent to I-T_c. Define

tau=<z,z>, A1=<z,Tz>,
h(x)=a(x)[1-(1477/1024)x^2],
Qplus=(<h,Th>-|<z,h>|^2/g)/<h,h>,
Qminus=A1/tau-tau/g.

The exact quantities satisfy

Tr(T_c^2)-Qminus^2=Tr(T^2)-(A1/tau)^2.

Consequently it suffices to certify

Qplus>0, Qminus<0,
Tr(T^2)-(A1/tau)^2-Qplus^2<1.                 (S)

Indeed two eigenvalues of T_c greater than 1 would, together with its negative
Rayleigh direction, supply three distinct spectral directions. Its largest
positive eigenvalue is at least Qplus, its negative extreme has magnitude at
least |Qminus|, and its second positive eigenvalue would exceed 1. Their squares
contradict (S). The two test vectors need not be orthogonal.

This argument is valid for the compact signed selfadjoint T_c. It proves that
K+F has at most one negative direction. The original known ground of H has
eigenvalue -1/2 and hence consumes that one negative direction for H+1/16.
Thus, if (S) is certified, the original mean-zero form has gap at least 7/16.
This would be a fixed-depth result, not the critical 1/2 inequality.

## 3. Full theta and derivative enclosures

For x>=0 set t=exp(2x), u_n=pi n^2 t. The exact sums are

Phi(x)=exp(x/2) sum_n (4u_n^2-6u_n) exp(-u_n),
f(x)=exp(x/2) sum_n F(u_n) exp(-u_n),
F(u)=16u^4-112u^3+164u^2-36u,
f'(x)=exp(x/2) sum_n F1(u_n) exp(-u_n),
F1(u)=-32u^5+360u^4-1056u^3+810u^2-90u.

Phi' uses P1(u)=-8u^3+30u^2-15u. Negative arguments of m are evaluated by its
true evenness. No individual theta seed is incorrectly declared even.

For j=4,6,8,10 define

Theta_j=5^j exp(-24pi)/[1-(6/5)^j exp(-11pi)].

For t>=1, the omitted normalized n>=5 sum of n^j exp[-pi(n^2-1)t]
is between 0 and Theta_j, by the ratio bound on consecutive terms.
For u>=pi, use

0<P0(u)<=4u^2, |P1(u)|<=20u^3,
|F(u)|<=74u^4, |F1(u)|<=402u^5.

The four retained terms are evaluated with outward interval arithmetic; these
bounds enclose every omitted theta term. A cell I is further enclosed by the
midpoint plus radius times the supremum of the corresponding derivative on I.
For m^2 its derivative is exactly

(m^2)'=[Phi'-(1/2)tanh(x/2)Phi]/[2cosh(x/2)].

For m^2, intersect this Taylor enclosure with the independently valid direct
positive interval enclosure. This preserves enclosure and avoids spurious
negative lower endpoints for extremely small shifted theta values.
All midpoint/radius products in the implemented bound are themselves interval
operations. This is a range enclosure, not an unbounded-order numerical
quadrature assumption.

## 4. Uniform exterior estimates

Let R0=5/2 and E(x)=exp(13x/2-(3/2)exp(2x)) for x>=0.
The elementary inequality exp(2x)>=5x gives E(x)<=exp(-x).
The exact theta bounds imply, on the entire positive half-axis,

m<=7 E, |f|<=14800 E, |w|<=5000 E.

For example sum_(n>=1) n^8 exp[-pi(n^2-1)]<2, pi<22/7 and |F(u)|<=74u^4
prove the f bound; m>=pi exp(2x-(pi/2)exp(2x)) gives the w bound.
The exponent comparisons used to replace the sharper bounds by E follow from
sup_(x>=0) 2x exp(-2x)=1/e.

Inside [0,R0], d>=1/50 is checked by the outward range enclosures. Outside it,
m(x)<=m_tail=sqrt(Astar) exp(2R0-(pi/2)exp(2R0)) and the global estimate
m<=sqrt(Astar)exp(-pi/2) give

d>=epsilon-delta-|c-C0|m_tail^2
    -2sqrt(Astar)exp(-pi/2)(sum alpha_n)m_tail>1/50.

Also |d-epsilon|<100 follows globally from |c-C0|<1, delta<1,
m<3/2 and sum alpha_n<3. Since the folded R kernel is at most 12,

|b_col|<=10^7 E, |z|<=10^8 E, a<=50 E,
|h|<=150 E, |Tz|<=3*10^12 E, |Th|<=5*10^6 E.       (E)

The h estimate follows from x^2<=exp(2x), using the sharper m envelope before
passing to E. For the convolutions use integral E<=1 and the folded bound 12.

At R0 the inequalities E(R0)<10^-89 and
3exp(2R0)-13/2>400 hold by directed scalar checks. If |v(y)|<=C E(y), then for
0<=x<=R0 the omitted y>R0 part of the complete folded R convolution is bounded by

12 C E(R0)/[3exp(2R0)-13/2].

The largest C needed in this document is 5*10^9, for a z. Hence every omitted
convolution tail is <10^-76, far below the implemented symmetric 10^-45 error.
For scalar products use

integral_(R0,infinity) E(y)^2 dy
 <= E(R0)^2/[6exp(2R0)-13].

The constants in (E) show that all discarded tails of g,tau,A1,<h,h>,<h,Th>,
<z,h> are also less than 10^-45. The additional factor 2 in the full-line g
integral is explicitly included. These are bounds for the actual full-line
columns, not definitions of truncated replacement columns.

## 5. Interval integration and full squared trace

On NC equal cells of [0,R0], all integrals are enclosed by cell length times
outward enclosures of their integrands. For each lambda and a cell I_j,
complete folded convolution is split into y<I_j, y>I_j, and y in I_j:

2 exp(-lambda x) integral_(0,left I_j) cosh(lambda y)v(y)dy
+2 cosh(lambda x) integral_(right I_j,R0) exp(-lambda y)v(y)dy
+integral_(I_j) [exp(-lambda|x-y|)+exp(-lambda(x+y))]v(y)dy.

The same-cell kernel is enclosed by
DX([exp(-lambda DX),1]+exp(-2lambda I_j)).
Signed prefix and suffix enclosures are accumulated independently. No interval
sum-minus-itself operation or unjustified cancellation is used.

For the positive squared trace, on x>y the kernel square is

4 a(x)^2 a(y)^2 sum_(j,k) exp[-(lambda_j+lambda_k)x]
                              cosh(lambda_j y)cosh(lambda_k y).

The two half-planes supply factor 8 for distinct cells; a whole same-cell square
has factor 4 and area DX^2. The 21 unordered pairs have multiplicity 2 off the
j=k diagonal. Thus the code encloses the entire square, including cell edges.
The omitted exterior square is at most

144[2 A_inside A_tail+A_tail^2],
A_inside=integral_0^R0 a^2,
A_tail <= Astar exp[-pi exp(2R0)]
          [exp(2R0)/pi+1/pi^2]/(2 d_tail).

Every expression entering (S) is therefore an interval containing its exact
full-theta, full-line value. The actual author run with NC=40000 passed the exact rational assertions

 d_min>1/50, 64<g<66, Qplus>389/100, Qminus<−47/100,
 Tr(T^2)-(A1/tau)^2-Qplus^2<99/100.

The computed last upper endpoint is approximately 0.9710045641225; that decimal
is only a display. The certificate uses the directed-interval comparison with
the exact rational 99/100. These assertions prove (S). The independently reviewed
complete analytic and executed arithmetic chain, together with Section 2,
gives E(q)>= (7/16) Var_nu(q) on the unchanged original even form domain.

Reproduce in [rank_one_certificate](rank_one_certificate) with Python 3.12.14 and mpmath 1.3.0:

    python check_rank_one_exterior_constants.py
    python certify_rank_one_threshold_shorting.py 40000

The corresponding persisted outputs are exterior_constants.json and
interval_rank1_40000.json. The latter contains no timing-dependent data.
No exploratory eigensolver output is needed. This certificate demonstrates the
user's exact threshold repair at a fixed depth; it does not claim to be the
strongest depth attainable by the separate full-Gamma resolvent method.
