# Independent review: actual negative-band regularity and finite polynomial coverage

The complete [mathematical proof](ACTUAL_NEGATIVE_BAND_COVERAGE.md) has been independently checked, including its original closed domain, complete signed prime coefficients, true whole-band Lyapunov estimates and explicit common-radius polynomial approximation.

For every strictly positive depth and each fixed r>=0, Part I proves ||<D>^r Q_kappa||<=kappa^(-r/2-o(1)) with an explicit finite recursion. Part II preserves the entire negative-band index inside one original central interval. Part III constructs the even degree-(p-1) trial space of rank at most kappa^(-1/2-1/p-o(1)) for every fixed integer p>=2, with actual A-form approximation error kappa/4000. These are upper-cost statements; the sign of the complete signed central matrix remains unproved.

The primary realization and graph core retain their public source attribution. The proof neither replaces the original operator by a positive prime-edge comparison nor treats separately positive trial vectors as a positive full matrix. It makes no uniform critical-depth Sobolev claim, no improvement of the existing certified gap, and no new zeta-zero exclusion. Section and equation numbers below refer to the corresponding Part of the mathematical proof.

# Review of Part I: original-domain regularity

## Primary-source and normalization checks

The reviewed definitions use Fourier transform integral f(x)e^(-itx)dx and Plancherel measure dt/(2pi), with B=m b(D)m and H=B-V. The exact original source [REPORT.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/REPORT.md) was read, including its Section 9.1 operator graph-core proof. This supplies D(H)=D(B), even compact smooth operator graph core, H>=-1/2, and the bounded signed-prime perturbation and full-prime tail.

[ACTUAL_FULL_GAMMA_CERTIFICATE.md, Appendix B](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/ACTUAL_FULL_GAMMA_CERTIFICATE.md) was read for the actual zero-free holomorphic theta square root and the stated envelope on |Im z|<=1/2. Neither an arbitrary Schwartz replacement for m nor a finite-prime replacement for H is used.

## Full-prime coefficient payment

The strip L1 and L2-squared bounds 40/3 and 25 follow from the stated envelope. For a_n(x)=m(x)m(x+log n), its middle interval contributes at most 100 n^2 log n exp(-3n/2). On the two exterior rays the integral is at most 100 n^2 exp(-c)(1/c+1/c^2), c=3(1+n^2)/4>=3, hence at most 100 n^2 exp(-3n/2). Thus S_n in (3) is valid uniformly throughout the required strip.

Cauchy circles of radius 1/4 give the derivative L1 bounds. The Fourier split at |t|=1 has tail integral at most one because k=ceil(p)+2, and the normalization in (2) is correct. The estimate 2 sum alpha_n S_n <=400 sum_(n>=2)n^3 exp(-3n/2)<400(149/108), plus 25 C0<150, is below 800. This proves absolute summability of the weighted Fourier moments of the *paired coefficients*. In particular the proof never separates out the divergent series sum alpha_n.

## Uniform commutator and operator domain

Differentiating l_(s,h) and applying the two-sided Peetre inequality proves (6), including 1/2<=s<1, where s-1 is negative. With q=s-1/2, p0=|s-1|+1 and p1=p0+1/2, the first Gamma term costs c_s 7 A_p0 2^(q/2)A_q and the second costs c_s 14 2^(1/4) A_p1. These agree with (4); translations commute with L and the complete prime contribution is c_s P_p0. The log-symbol estimate b(t)<=7<t>^(1/2) is valid: b<=4+(1/2)log(1+4t^2)<=4+log(1+2|t|)<=4+2sqrt(2|t|)<=7<t>^(1/2).

For clarity the fixed-h domain justification in the manuscript can be made fully explicit without adding an assumption:

    |l_(s,h)(t)-l_(s,h)(u)|
    <=2s h^(-s-1)|t-u|<t-u>^2<u>^(-2).

This follows from |l'|<=s h^(-s-1)<t>^-2 and two-sided Peetre along the segment. It makes the fixed-h commutator L2-bounded even after multiplication by the logarithmic Gamma symbol. The regularized multiplier maps Schwartz into Schwartz; multiplying its output by the true m therefore gives an admissible B-domain vector. Applying the verified original operator graph core and closedness proves (7) on D(H). The use of H LQ is consequently legal before Q has been proved Sobolev regular.

## Complete quadratic kernel check

For 1/2<=rho<1, beta=2(1-rho), the bound b(t)<=G_beta<t>^beta with G_beta=4+2^beta/beta follows from the positive Gamma-series estimate and log(1+x)<=x^beta/beta. The latter follows by integrating (1+x)^(-1)<=x^(beta-1), valid for all x>0 and 0<beta<=1.

For s>=rho, q=s-rho>=0, squaring the uniform first-difference estimate contributes c_s^2 |t-u|^2<t-u>^(2|s-1|)<u>^(2s-2). Dividing the double-commutator kernel by <t>^q<u>^q and applying the two-sided Peetre inequality gives the factor 2^(q/2)<t-u>^q<u>^(-2q). Thus p=2+2|s-1|+q and the remaining input power for every translated prime coefficient is -beta. It is bounded by one. The complete normalized weighted coefficient sum is P_p, not a divergent unweighted prime sum. The actual translation phases are retained before this error estimate.

For B=m b(D)m its Fourier kernel has the intermediate integral mhat(t-z)b(z)mhat(z-u) dz/(2pi). Write k1=t-z, k2=z-u. The estimate b(z)<=G_beta 2^(beta/2)<u>^beta<k2>^beta cancels the remaining input power exactly, because 2s-2+beta-2q=0. The residual <k1+k2>^p is at most 2^(p/2)<k1>^p<k2>^p. Two normalized Young inequalities therefore give precisely

    c_s^2 2^(q/2) G_beta 2^((beta+p)/2) A_p A_(p+beta).

Adding the prime part gives (11). In particular the weighted kernel is dominated by an L1 convolution kernel, proving the H^q quadratic-form estimate (12), with no unjustified uniform L2 claim when q>0. All source normalization factors dt/(2pi) and dz/(2pi) are correct. Density and the full absolutely summable coefficient bound justify the passage to arbitrary H^q vectors and the infinite prime series.

## Domain and Lyapunov signs

For fixed h, L is bounded, maps D(H) into D(H), and [L,H] is bounded on L2 by the verified fixed-h argument. Consequently [L,[L,H]] is bounded for fixed h and the algebraic identity is valid on the original operator domain. Since H Q=-QK and X=Q L^2 Q,

    Q[L,[L,H]]Q=-XK-KX-2( LQ )*H( LQ ).

This gives the displayed identity with its stated minus sign. The lower form estimate (9) therefore implies

    (K-delta_N)X+X(K-delta_N)
    <=[2c_N L_s(T)^2+D_(s,rho) M_q^2]I.

The positive Lyapunov inverse has norm at most 1/(2a), a=kappa-delta_N>=kappa/2. The square-root recursion (13), including the factor D/2, follows. No different spectral parameters have been assigned a common eigenvalue. The uniform fixed-h bound and monotone Fourier convergence prove the entire-band conclusion at every grid exponent s=j rho.

## Interpolation and variable rho

Applying Fourier Holder to each Qv, then the endpoint operator bounds, gives (14) uniformly over the entire band. For fixed rho the j-th recursion step costs at most kappa^(-j/2-o(1)); interpolation makes the exponent r/(2rho), rather than retaining a ceiling loss.

For rho=1-1/(2+sqrt(log(1/kappa))), the number of recursion steps for each fixed target r remains bounded. All moment indices in (11), including their ceiling-defined factorial constants, lie in a fixed bounded interval; c_s and powers of two are uniformly bounded there. The only new unbounded symbol constant is G_beta=O(sqrt(log(1/kappa))). Together with T=exp(O(sqrt(log(1/kappa)) loglog(1/kappa))), these losses are subpowers of kappa. Finally r/(2rho)=r/2+o(1), proving (15) and in particular the H2 cost kappa^(-1-o(1)).


# Review of Part II: all-column localization

## Whole-band Lyapunov identity

For Q the actual spectral band [-1/2,-kappa] with the known ground removed, K=-H|Q is bounded between kappa and 1/2. Setting A=Q chi Q gives A>=0 and ||A||=||chi Q||^2. The localization formula is exactly Bchi=Dq-Herm(AK)+Egamma. Positivity of Bchi gives AK+KA<=2(zd+E)I, with ||Dq||<=zd; the latter uses the fact that chi is an orthogonal projection.

The bounded Lyapunov inverse integral is order preserving for K>=kappa>0 and sends 2I to K^(-1). Hence A<=(zd+E)K^(-1). The displayed scalar bound follows by Young's inequality and is valid for every vector in the band, without assigning a common eigenvalue to superpositions.

## Common central image and exact pole cost

The parameter conditions give z^2<=5eta kappa/16<1. Thus J=(1-chi)|Q is bounded below and has closed injective image. The exact expanded central form is (4): -K+Herm(AK)+Dq+Egamma-Qchi Vchi Q plus the true pole term. Its coefficient bounds are legitimate since ||K||<=1/2, ||chi Vchi||<=D(R), and Q is ground perpendicular.

The bracket is at most 9/8. Young gives dz<=3eta kappa/32, and E<=eta kappa/16. Combined with the bracket times 5eta kappa/16 this is (45+12+8)eta kappa/128, strictly less than eta kappa. Equation (5) therefore holds on the entire band. This is a negative-state localization result, not a central positivity proof.


# Review of Part III: original-form finite polynomial approximation

## Original normalization and domain

For a unit original vector v in Q, localization gives Acrit[Cv]<=-(1-eta0)kappa, eta0<=1/16. Since Acrit[Cv]<0 and the pole form is positive, B[Cv]=Acrit[Cv]+<Cv,V Cv>-(1/2)|<Cv,e0>|^2<=41||Cv||^2. Thus ||Cv||_A^2<=42<81, proving the stated ||Cv||_A<9 directly. The m-strip envelope has squared maximum below 25, and Cauchy on a radius-1/4 circle proves ||m'||infinity<=20.

Each trial function is even, continuous piecewise polynomial inside [-R,R], and may have nonzero boundary trace before zero extension. Its actual source m z is compactly supported BV. The measure-derivative Fourier bound |hat(mz)(t)|<=TV(mz)/|t| pays the complete logarithmic symbol in L2, including endpoint jumps. Thus b(D)(mz) is L2, and the original associated-form criterion puts z in D(A). No false H2 assertion for these sharp trial sources is used.

## Linear interpolation and full-Gamma error

Actual H2 regularity makes nodal evaluation legal. The interpolation error vanishes at each cell endpoint, including the outer endpoints, so its zero extension is H1. Cellwise zero-mean Poincare for e', followed by Dirichlet Poincare for e, gives ||e'||<=hK2/pi and ||e||<=h^2K2/pi^2, with no factor of two after reflecting and summing both halves.

For g=me, the complete positive Gamma-series bound b(t)<=6+(1/2)log(1+t^2) and Jensen on the normalized |ghat|^2 measure give the displayed b[g] bound. Both x log(1+y/x) and the other terms are increasing in their nonnegative arguments. With ||g||<=2a0 and ||g'||<=20a0+2a1, the original A-error is bounded by

    a0^2 {25+2log[1+(10+a1/a0)^2]}.

This is exactly (6), with a1/a0=pi/h; the value at a zero norm is understood by continuity. All Fourier normalizations are original ones.

The explicit n in (7) makes this error strictly smaller than delta. Its rounding can only decrease the bound: differentiating h^4[25+2log(1+(10+pi/h)^2)] with respect to log h gives a positive expression, since the negative derivative contribution has magnitude below 4 while the positive one is at least 100. The displayed logarithmic estimates and the rank n+1 in (8) have the correct constants and direction.

## Every fixed polynomial degree

H^p regularity in one dimension supplies all Taylor traces through order p-1. On each cell the degree-(p-1) Taylor polynomial plus its linear right-endpoint correction matches both endpoint values. The even reflection is continuous at zero; its derivative need not match there for membership in H1. The zero-extended error is therefore H1.

The integral Taylor remainder has the stated L2, derivative L2, and endpoint bounds. The linear correction has norms |r(a+h)|sqrt(h/3) and |r(a+h)|/sqrt(h). Summing these linear estimates over disjoint cells in l2 is legitimate and is dominated by F_p=2/(p-1)! in both (12) estimates. The same original-source Jensen calculation gives (13) with 1/h in place of pi/h.

For x=max(1,F_pK_p/delta), h0=(100x(1+log x))^(-1/p), p>=2, one has h0<=1 and the logarithmic bracket is below 7sqrt(1+log x). Also F_pK_p h0^p<=delta/[100(1+log x)], including the branch where x=1. Thus (14) gives error below delta. The monotonicity in h follows as above, with the positive derivative term now at least 100 and the negative one still below 4. The even continuous degree-(p-1) spline space has exactly n(p-1)+1 dimensions, proving (15).

The reviewed K_p<=kappa^(-p/2-o(1)), delta=kappa/4000, and the stated localization radius give (16) for every FIXED p. For each fixed epsilon one may choose a fixed p with 1/p<epsilon and then absorb the subpower factor for sufficiently small kappa. This does not permit an unbounded p(kappa) without paying its constants, nor does it give theta-jet representation or conditioning for free.

## Exact remaining signed matrix

With s=kappa/2, localization gives (Acrit+s)[Cv]<=-7kappa/16. The original bounded part has norm at most 41+1/2+s<=41.75. Since B>=0, direct Cauchy in the sum of B and identity forms gives |(Acrit+s)(a,b)|<=42||a||_A||b||_A. It does not require V to be positive. The interpolation error therefore changes this form by at most 42 delta(18+delta)<kappa/5. Nonnegativity of the ENTIRE raw central finite matrix on the same trial space would contradict that negative vector, proving the stated sufficient test.

The optional shifted Schur condition is stronger: A_e+s>=s-D(R)>0 follows from the old full-prime bound and pole positivity. Its Schur loss is positive, so its nonnegativity implies the raw central test. All cross terms remain complete and the inverse denominator s-D(R) is genuine; no critical exterior positivity is assumed.

For raw central matrix entries both source endpoints are in [-R,R]. A prime translation of length log n>2R therefore has exactly zero overlap, including the equality boundary up to measure zero. The central prime contribution is an exact finite sum, not a tail truncation. The full Gamma and true pole remain present. No sign computation for this growing finite matrix, no universal-in-kappa sign theorem, and no zero exclusion are included.


## Explicit common radius

Indeed D(R)=70000 y^(5/4)exp(-pi y/2) and E(R)=70 y^(3/4)exp(-pi y/2). Using pi>3, log(70000)<12, log(100)<5, and log(1+L)<=L gives

    log D(R)<18.25-150-148.75L < -log16-(3/2)L,
    log E(R)< 8.75-150-149.25L < -log128-2L.

Thus the old localization conditions D<=kappa^(3/2)/16 and E<=kappa^2/128 hold with strict margin; R>=2. In particular the exact finite central prime index cutoff is y=100(1+log(1/kappa)), genuinely O(log(1/kappa)), rather than merely a consequence of a vague O(loglog) radius. No additional unreviewed exterior estimate is required.

# Review of Appendix A: actual count and Schatten size

The complete direct corollary was independently reviewed separately from its author. Its fixed-error injection and spectral-calculus consequences use only Parts I–III.

1. Setting the already reviewed interpolation tolerance to 1/4 gives x=4K2 and n=ceil[20R sqrt(K2(1+log(4K2)))]. Hence the finite target dimension is at most the exact displayed expression (3).
2. The whole-band localization is uniform on arbitrary vectors, not merely each eigenvector: ||(1-C)Q||^2<=5kappa/256. Orthogonality of C therefore gives the stated positive lower bound for ||Cv||, and the interpolation error yields (2). Its bracket remains positive at the endpoint kappa=1/2.
3. Actual H2 regularity makes the nodal map a linear, well-defined map on the entire band. The positive lower norm bound proves injectivity, including if the band were initially infinite-dimensional. Its finite-dimensional image therefore bounds the band dimension without assuming finite rank in advance.
4. The explicit K2 upper cost and R=.5log[100(1+log(1/kappa))] give the exponent 1/2+o(1). A fixed error suffices for counting. The stronger kappa-proportional error used for a conditional sign contradiction is not needed here. The fixed-epsilon uniform bound on all depths follows from small-depth asymptotics and monotonicity on the remaining compact depth range.
5. The original ground is an exact reducing eigenvector. The pole-corrected Acrit is zero on it and agrees with H on its orthogonal complement. Thus the positive spectral projections of T=(-Acrit)_+ at every positive threshold are exactly the Q_kappa used here, with their multiplicities and the inclusive endpoint convention intact.
6. The finite-rank approximants TQ_kappa converge in operator norm with error at most kappa. This proves compactness of the actual negative part, rather than assuming it. The positive layer-cake identity and epsilon<a-1/2 then give the displayed finite trace of T^a. The quasi-Schatten interpretation for 1/2<a<1 and the absence of an endpoint S_(1/2) claim are accurate.

No mathematical correction is required. This is a dimension/summability theorem for possible negative spectrum. It neither proves that the negative part is zero nor supplies the missing signed central matrix sign, and it changes no certified spectral-gap value.

# Review of Appendix B: scope relative to the earlier adaptive theorem

The fixed public [POLYNOMIAL_ACCURACY_TAIL.md, Sections 1, 5 and 7](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/bf5ee119d3b6687d34cd708f1a755aea9efd9679/reports/20261012_adaptive_spectral_tail/POLYNOMIAL_ACCURACY_TAIL.md) gives the stated positive base with the original form domain, the form lower comparison, and a finite-rank signed approximation with every prescribed polynomial accuracy. Taking epsilon=kappa/2 and eta=epsilon/4 satisfies its hypotheses and gives rank kappa^(-o(1)).

The direction of the form comparison is essential and correct: a subspace on which H+epsilon is strictly negative is also strictly negative for its lower comparison. The map A_epsilon^(1/2) is defined and injective on that subspace because it lies in the common form domain and A_epsilon>=epsilon/2. A subspace of dimension greater than rank F_epsilon must then intersect ker F_epsilon after this map. There I-K_epsilon is positive by the norm error eta<1, a contradiction. This argument needs no lower bound on a Birman–Schwinger eigenvalue margin and no computed finite-matrix sign.

It follows that each true Q_kappa is finite rank with the subpower upper count (B3). The exact pole correction removes only the known reducing ground; therefore T=(-Acrit)_+ has these positive spectral projections. The norm convergence TQ_kappa->T and the layer-cake integral with delta<a prove T in every S_a, a>0. Possible negative eigenvalues are not excluded.

Appendix A is a correct weaker direct Sobolev corollary. Appendix B makes clear that the earlier adaptive theorem already implies the stronger count and summability. This is a scope clarification, not a correction to the validity of Parts I–III or Appendix A, and it supplies no new zero exclusion.
