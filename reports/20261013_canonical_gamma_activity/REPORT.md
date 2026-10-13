# Canonical Gamma energy on actual-source activity records

For a fixed genuine negative eigenstate of the original even operator, the complete rational Möbius observable has Gamma energy at most its own terminal energy times a logarithm along the same activity records. The estimate includes the complete future Gamma tail. Its constant may depend on that fixed state and its negative depth.

The finite-column Gamma boundary is not included. In particular, no signed margin, zero exclusion, or coefficient-one Green comparison follows from this result.

## Original objects and theorem

Work with the original even complex L2 space, the positive theta multiplier m, and the full self-adjoint operator H=m b(D)m-V. Fix v in D(H) with Hv=-kappa v, kappa>0, and put f=mv. For the actual quotient application in Section 6, also take v orthogonal to the known ground e0=2m cosh(x/2). The source, closed domain, ground normalization and complete prime coefficients are those of [ORIGINAL_FORM_FOUNDATION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md) and [ACTUAL_NEGATIVE_BAND_COVERAGE.md, Part I](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/bf5ee119d3b6687d34cd708f1a755aea9efd9679/reports/20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md).

Throughout this paper mu(n) is the rational arithmetic Möbius function, and Lambda(n) is the rational von Mangoldt function. They are unrelated to an auxiliary source weight in the odd Green realization. Use Fourier transform hat h(t)=int h(x)exp(itx)dx and measure dt/(2pi). The even multiplier b is unchanged if the opposite Fourier sign is used.

Set

    B(s)=int_R f(x)exp(-(s-1/2)x)dx,
    G(R)=sum_(n>=1) mu(n)n^(-1/2) f(R-log n),
    g(R)=exp(-dR)G(R),
    E(U)=int_(-infinity)^U |g(R)|^2 dR.

Here G is an auxiliary rational-zeta observable: its bilateral Laplace transform is B(s)/zeta(s) on Re s>1. No identification with a physical number-field signal is assumed.

Let Gamma=b(D)-C0 be the original complete Gamma operator, with

    b(t)=Re digamma(1/4+it/2)-digamma(1/4),
    C0=EulerGamma+pi/2+3log 2+log pi,
    k(l)=exp(-l/2)/(1-exp(-2l)), l>0.

Its action on a smooth source is the compensated integral with integrand k(l)[2G(R)-G(R+l)-G(R-l)], followed by -C0 G(R). Complete prime coefficients enter the regularity proof through H; no finite-prime replacement is made.

**Theorem.** Suppose 0<d<alpha<1/2 and

    limsup_(U->infinity) log E(U)/U = Lambda = 2(alpha-d).

There are U_j tending to infinity for which

    E(U_j/2)=o(E(U_j)),
    |Re int_(-infinity)^(U_j) exp(-2dR) conjugate(G(R)) Gamma G(R)dR|
       <= C_(f,d,alpha) log(U_j+2) E(U_j).

These same records satisfy a complete future envelope specified in Section 1. In particular the displayed energy is o(U_j E(U_j)). No sign is asserted. Appendix A proves all additional fixed-state regularity used here directly from the published original realization.

Section 6 verifies the activity premise for a genuine surviving rational quotient pole. The strict uniform gap used in that application is a separate input: the main theorem of [The Quasi-Riemann Hypothesis, September 30, pinned primary statement](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L106-L119), which gives the zero-free region Re s>7/8 for the Riemann zeta function. Only the implication alpha<=3/8 is used here. This external theorem is not proved in this paper, and its uniform gap is not inferred from individual zeros having real part less than one.


## 1. Records with a complete future envelope

Choose small epsilon>0 with a=(Lambda+epsilon)/2 < c=1/2-d and epsilon<Lambda/4. Choose V_j tending to infinity with E(V_j)>=exp((Lambda-epsilon/2)V_j). Since E(V)exp(-(Lambda+epsilon)V) tends to zero, it attains a maximum on [V_j,infinity), at some U_j>=V_j. Then, for all h>=0,

 E(U_j+h)<=exp(2a h)E(U_j).

Also E(U_j)>=exp((Lambda-epsilon/2)U_j), while the global limsup upper bound at U_j/2 gives E(U_j/2)=o(E(U_j)). In particular int_(-infinity)^U R|g(R)|^2 dR >= (U/2)(E(U)-E(U/2))-C for these records; the fixed negative-half-line moment is finite by (G) below.

## 2. Actual-source absolute Gevrey budget

Appendix A below proves from the published original realization that the fixed actual negative eigenvector obeys ||exp(a0 omega2(D))v||_2<infinity for some a0>0, where omega2(t)=(1+t^2)^(1/4)-1. The original coefficient realization, graph core, strip envelope and finite-prime form lower bound are those in the linked ACTUAL_NEGATIVE_BAND_COVERAGE.md, Part I.

Here is the full weighted-source consequence needed in this proof. For every fixed real b, m_b(x)=exp(bx)m(x) has integrable double-theta envelopes on Im x=+/-1/2. The original theta contour argument therefore gives |mhat_b(t)|<=C_b exp(-|t|/2). Choose 0<a1<min(a0,1/4). Since omega2 is 1-Lipschitz,

 exp(a1 omega2(t)) <= exp(a1 omega2(u))exp(a1|t-u|).

Weighted convolution and Young applied to f_b=exp(bx)f=m_b v prove ||exp(a1 omega2(D))f_b||_2<=C_b. Since omega2(t)>=c sqrt(|t|) for large |t|, its frequency moments imply

 ||f_b^(k)||_2 <= C_b A_b^k(k!)^2.

Leibniz, on two buffered lines b+delta and b-delta, followed by Cauchy against exp(-delta|x|), gives

 ||exp(bx)f^(k)||_(L1) + ||exp(bx)f^(k)||_(W11)
 <= C_b A_b^k(k!)^2.

The extra derivative and all fixed binomial factors are absorbed into A_b. Take b=-1/2. Apply the elementary integral-plus-total-variation sum bound to q_R(t)=t^(-1/2)f^(k)(R-log t), t>=1. Its integral is at most exp(R/2)||exp(-x/2)f^(k)||_1. Its total variation is bounded by the same expression with f^(k) and f^(k+1), because x<=R in the change of variables. The endpoint has the same weighted W11 bound. Hence the actual complete mu sum obeys

 sup_R exp(-R/2)|G^(k)(R)| <= C A^k(k!)^2, k>=0.       (G)

All constants concern the fixed actual state. This is only an absolute regularity budget and uses |mu(n)|<=1; it is not a Mobius cancellation estimate.

Choose fixed Gevrey-two chi, equal to one on (-infinity,1] and zero on [2,infinity), and put h_U(R)=chi(R-U)g(R). For U=U_j,

 ||h_U||_2^2<=E(U+2)<=exp(4a)E(U),
 ||h_U^(k)||_2<=C A1^k(k!)^2 exp((1/2-d)U).

Optimizing k in Plancherel therefore gives an L2 Fourier tail bounded by C exp((1/2-d)U-c1 sqrt(T)) above frequency T. The same bound, with slightly smaller c1, holds after multiplication by log(2+|frequency|). Taking T=K(U+1)^2 and K large makes that tail O(exp(-M U)) for any prescribed fixed M. Constants depend on the fixed source.

## 3. Local Gamma part

Split the Gamma integral at l=1. The |l|<=1 part conjugated by exp(-dR) has multiplier

 b_loc,d(t)=int_0^1 k(l)[2-exp(d l-it l)-exp(-d l+it l)]dl,

with the foundation Fourier convention hat h(t)=int h(R)exp(itR)dR. Thus |b_loc,d(t)|<=C_d log(2+|t|). On R<=U its action on g equals its action on h_U, because chi=1 through U+1. Section 2 then gives

 ||1_(R<=U) exp(-dR) Gamma_loc G||_2
 <=C log(U+2) sqrt(E(U))+O(exp(-M U)).

Cauchy pays the corresponding energy by C log(U+2)E(U). A fixed positive lower bound for E(U) absorbs the error for large U.

## 4. Complete far Gamma tail

All diagonal constants and past shifts l>=1 are bounded on the terminal weighted L2 space by Young. Future shifts whose output remains <=U are also bounded since k(l)exp(d l)<=C exp(-c l), c=1/2-d>0.

For the genuine future output S>U, the absolute bilinear contribution is at most

 C [int_{-infty}^U |g(R)|exp(c(R-U))dR]
   [int_U^infty |g(S)|exp(-c(S-U))dS].

The first factor is <=(2c)^(-1/2)sqrt(E(U)). Choose b with a<b<c. Integration by parts using E(U+h)<=exp(2a h)E(U) gives

 int_0^infty exp(-2b h)|g(U+h)|^2 dh<=C_(a,b)E(U).

Cauchy with the remaining exp(-(c-b)h) pays the second factor by C sqrt(E(U)). This also proves convergence of the original future Gamma tail. Therefore the complete far contribution is O(E(U)), proving the claim.

## 5. Unpaid finite-column transfer remains explicit

For F_N=sum_(n<=N)mu(n)n^(-1/2)f(R-log n), even with N=exp(U)K0 sqrt(U), this result does NOT show Gamma F_N-Gamma G is small. Its exact extra term is -Gamma(G-F_N), and it must remain in any complete finite-source identity together with the derivative, full prime, and eigen-equation terms. The present theorem supplies no relative bound for that extra term. The result cannot be used to replace the full finite-column energy by the canonical one without that boundary.

## 6. Actual quotient activity and the energy exponent

To make the premise directly usable, define alpha_q as the supremum of Re rho-1/2 among the actual poles of B(s)/zeta(s), counting full cancellation by multiplicity. This need not be identified with the different selection set B(rho) != 0 at a partially canceled multiple zero. If the fixed state activates an off-critical zero, then symmetry gives alpha_q>0. The application in this section assumes such activation, as supplied when invoking the original negative-state selection; the theorem above itself requires only its stated activity premise. The separately attributed 7/8 baseline gives alpha_q<=3/8<1/2.

Appendix B gives the complete rational activated-safe quotient argument needed here. On a buffered line to the right of alpha_q+1/2, the disk-Blaschke proof divides every canceled zero at full multiplicity. Applying its maximum principle to the weighted-source bound |B(s)|<=C exp(-a1 omega2(Im s)) retains that height factor: imaginary parts on each fixed-radius disk differ by O(1), while omega2 is 1-Lipschitz. The remaining zero-free factor and uncanceled distant zeros cost only a fixed power of height. Thus

 |B(s)/zeta(s)| <= C(2+|Im s|)^C exp(-a1 omega2(Im s))

on each buffered safe line, after reducing a1 if necessary. Mellin inversion and contour shift give G(R)=O_epsilon(exp((alpha_q+epsilon)R)) for R>=0; fixed derivatives have the same bound. The negative-R absolute source tail is double theta. Therefore limsup log E_d(U)/U <= 2(alpha_q-d) for 0<d<alpha_q.

For the converse, suppose this limsup were smaller. Choose b<alpha_q but larger than d plus half that smaller rate. On R>=0, Cauchy using the cumulative energy upper bound shows that int exp(-lambda R)G(R)dR converges locally uniformly for Re lambda>b. The negative half-line contributes an entire function by its double-theta tail. Consequently B(1/2+lambda)/zeta(1/2+lambda) would be holomorphic throughout Re lambda>b, contradicting an actual surviving pole with real part greater than b. No attained rightmost pole is needed. This proves the stated equality Lambda=2(alpha_q-d).

## Appendix A. A self-contained fixed-state Gevrey-two input

Only the published original realization and full-coefficient strip estimates are needed. Write H=m b(D)m-V, where V=C0 m^2+sum_(n>=2)alpha_n m(tau_log n+tau_-log n)m, alpha_n=Lambda(n)/sqrt(n). Let Hv=-kappa v, kappa>0, in the original graph domain. The published input gives b(t)<=7<t>, and, for a polynomial order j, finite exponential Fourier moments

 A_j=(1/(2pi))int <t>^j exp(|t|/4)|mhat(t)|dt,
 P_j=C0 a_j(m^2)+2sum_(n>=2)alpha_n a_j(m(x)m(x+log n)),
 a_j(c)=(1/(2pi))int <t>^j exp(|t|/4)|chat(t)|dt.

Indeed the original |Im x|<=1/2 theta strip gives exponential Fourier decay exp(-|t|/2), and the full paired-prime strip L1 sum is finite. These are exactly the complete-coefficient estimates in the published Part I, Section 2; the contour shift retains every prime power. They also hold for exp(bx)m(x) for every fixed real b, by the same double-theta strip envelope.

Put omega2(t)=(1+t^2)^(1/4)-1. It is even, smooth, nonnegative, 1-Lipschitz, and omega2(t)~sqrt(|t|). Its derivative satisfies |omega2'(t)|<=(1/2)<t>^(-1/2). The two-sided Peetre inequality, applied along the interval from u to t, gives

 |omega2(t)-omega2(u)|^2 <= <t-u>^3/<u>.             (A1)

For 0<a<=1/4 and h>0, set l_h(t)=exp(a omega2(t))/(1+h exp(a omega2(t))), L_h=l_h(D). The logarithm of l_h is a function of omega2 with derivative in [0,a], whence

 (l_h(t)-l_h(u))^2/[l_h(t)l_h(u)]
 <=a^2 |omega2(t)-omega2(u)|^2 exp(a|t-u|).          (A2)

For the Gamma Fourier kernel insert its intermediate frequency z, write k1=t-z, k2=z-u, and use b(z)<=7<z>, <z>/<u><=sqrt(2)<k2>, and <k1+k2>^3<=2^(3/2)<k1>^3<k2>^3. Its normalized double-commutator absolute kernel is at most

 28 a^2 <k1>^3<k2>^4 exp((|k1|+|k2|)/4)
          |mhat(k1)mhat(k2)|.

For each complete prime coefficient the same bound (A1), with <u>^(-1)<=1, costs a^2 P_3; translation phases have modulus one. Two normalized Young inequalities prove

 ||L_h^(-1)[L_h,[L_h,H]]L_h^(-1)|| <=D a^2,
 D=28 A_3 A_4+P_3<infinity,                        (A3)

uniformly in h. This concerns the full original H, not a finite-prime substitute.

All identities first hold on the published compact smooth graph core. For fixed h, l_h-1/h and all its positive derivatives are Schwartz symbols. A two-sided Peetre bound for l_h(t)-l_h(u), with its rapidly decreasing derivative, and the displayed coefficient Fourier moments show [H,L_h] is bounded on L2. Thus L_h maps the original graph domain into itself by graph-core approximation and closedness. The bounded fixed-h double commutator and (A3) can consequently be applied to v before taking h to zero.

Choose N with the original complete prime norm tail delta_N<kappa/4, and T with b(T)>=c_N, c_N=C0+2sum_(n<=N)alpha_n. The published original form lower bound is

 H[w]>=-c_N||P_T m w||_2^2-delta_N||w||_2^2.        (A4)

It follows directly by retaining the positive full-Gamma part above T and bounding only the complete omitted-prime operator by delta_N. The low-frequency convolution estimate, using omega2 Lipschitz, is

 ||P_T m L_h|| <= A_0 exp(a omega2(T)).              (A5)

The exact eigenvector identity is

 2H[L_h v]=-2kappa||L_h v||^2-<v,[L_h,[L_h,H]]v>.

Combine (A3)--(A5), and choose a>0 small enough that a<=1/4 and D a^2<=kappa/2. Then

 (kappa-delta_N-D a^2/2)||L_h v||^2
 <=c_N A_0^2 exp(2a omega2(T))||v||^2,

whose left coefficient is at least kappa/2. Monotone convergence as h decreases to zero proves ||exp(a omega2(D))v||_2<infinity. This is precisely the fixed-state input used in Section 2. No full-band theorem, quasianalytic uniqueness, or unproved zero exclusion enters this appendix.

## Appendix B. Rational activated-safe lines, including canceled zeros

Suppose B is entire, has the fixed-strip source bound |B(s)|<=C exp(-a omega2(Im s)), and F=B/zeta is holomorphic on Re s>a_star, where 1/2<a_star<=1. For fixed delta>0 and a finite right endpoint, we prove that F has a polynomial-height loss times the same square-root exponential decay on Re s>=a_star+delta. It suffices to consider real parts at most 3; further right use the absolutely convergent Euler product. Reduce delta so 0<delta<1/4.

At height t put z0=3+it and Z(s)=(s-1)zeta(s). Use radii

 Rb=3-a_star+delta,
 Rlo=3-a_star+delta/4,  Rhi=3-a_star+delta/2,
 r=3-a_star-delta/2.

The standard fixed-strip polynomial bound for zeta gives |Z|<=(2+|t|)^C on the outer disk, while the Euler product at its center gives |Z(z0)|>=(2+|t|)^(-C). Jensen on Rb bounds, with multiplicity, the number of zeros within Rhi by O(log(2+|t|)). Choose R strictly between Rlo and Rhi with no zero on the circle. Factor all zeros in that disk with the disk Blaschke factors b_rho:

 Z(s)=Q(s) product_rho b_rho(s),  |b_rho|=1 on |s-z0|=R.

The zero-free Q obeys |Q|<=(2+|t|)^C on the boundary and |Q(z0)|>=(2+|t|)^(-C), because each interior Blaschke factor has center modulus at most one. Harnack applied to C log(2+|t|)-log|Q| gives |Q(s)|>=(2+|t|)^(-C') on radius r. The fixed ratios r/Rlo and Rhi/Rb keep all constants independent of height.

Call zeros with Re rho>a_star good. Holomorphy of F makes each good zero a zero of B with at least its full multiplicity. Thus B/product_good b_rho is holomorphic on the disk. On its boundary it has the same modulus as B, so maximum principle bounds it by C exp(-a omega2(t)); the height changes by only O(1) across the disk and omega2 is Lipschitz. There is no price depending on the number or clustering of good zeros.

For a target s=sigma+it with a_star+delta<=sigma<=3, each bad zero Re rho<=a_star is at distance at least delta. The explicit disk factor satisfies |b_rho(s)|>=delta/(2R). There are only O(log(2+|t|)) such factors, so their reciprocal product is polynomial in height. Combining this with the Q lower bound and F=(s-1)B/Z proves

 |F(s)|<=C(2+|t|)^C exp(-a omega2(t)).

Bounded heights follow from compactness and holomorphy. This proof makes no zero-spacing assumption and removes all canceled zeros with their full multiplicity. It justifies the contour shifts and derivative bounds used in Section 6. The standard zeta strip growth, Euler product and Jensen/Harnack facts here do not use RH or the separately quoted 7/8 theorem; that external theorem is used only to know the strict uniform upper gap alpha_q<=3/8.
