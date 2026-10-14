# Finite source columns with complete Gamma transfer

A finite approximation of the full rational Möbius observable can preserve the original source equation and approximate both the observable and its complete Gamma image on the same terminal half-line. The correction consists of explicitly specified linear functionals of the entire original Möbius tail. The complete forward-prime edge remains on a linear-in-observation-scale range.

This is a transfer result. It does not give a signed margin for the remaining prime/negative-source pairing, a bound for the original hard-cutoff Gamma error, or a zero exclusion.

## 1. Objects, hypotheses and statement

Use the original real even source f=mv=m²r of a fixed nonground negative eigenstate Hv=−κv, κ>0. The original operator and ground normalization are those of [the original form foundation](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/96dda0cd381bb90fac5fbde4a5a533384082ad41/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md). Write

    B(s)=∫ f(x) exp(−(s−1/2)x) dx,
    G(R)=Σ_(n≥1) μ(n)n^(−1/2) f(R−log n),
    F_N(R)=Σ_(n≤N) μ(n)n^(−1/2) f(R−log n).

Here μ and Λ are the rational Möbius and von Mangoldt functions. All prime powers are retained. The source and its fixed derivatives have double-theta envelopes, and B(0)=B(1)=0.

Put

    Γ=b(D)−C0,
    b(t)=Re ψ(1/4+it/2)−ψ(1/4),
    C0=EulerGamma+π/2+3log 2+log π,
    k(ℓ)=exp(−ℓ/2)/(1−exp(−2ℓ)), ℓ>0.

Thus Γ acts by the compensated integral with integrand k(ℓ)[2f(R)−f(R+ℓ)−f(R−ℓ)], followed by −C0f(R). Also define

    S^±h(R)=Σ_(j≥2) Λ(j)j^(−1/2)h(R±log j),
    L=Γ−S^−−S^+.

The original source equation is Lf=−κr. The operator Γ always contains its complete kernel.

We use the activated-safe continuation and strict growth bound α_q<1/2 established for this source in [Canonical Gamma energy on actual-source activity records](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/0185c43bec0c6dff5e033a4ddcf756995e2ca9b1/reports/20261013_canonical_gamma_activity/REPORT.md), Section 6 and Appendix B. In particular B/ζ and its fixed polynomial height multiples decay on a buffered line 1/2+α_q<σ1<1, and G and its fixed derivatives grow more slowly than exp((σ1−1/2)R) on the right. That report explicitly attributes α_q≤3/8 to the external [September 30 quasi-Riemann theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L106-L119). No new zero-free region is proved here, and a uniform gap is not inferred from the locations of individual zeros.

For 0<d<1/2 write

    ||h||_(d,U)²=∫_(−∞)^U exp(−2dR)|h(R)|² dR.

**Theorem.** Fix d and M>0. There are constants c,K0,K1, independent of sufficiently large U, with the following property. Freeze

    N=floor(exp(U)K0 sqrt(U+1)),   K=ceil(c(U+1)).

There are real coefficients c_j and nodes N≤t_j≤4N, j=1,…,K, specified in Section 3, for which

    C_N(R)=Σ_j c_j f(R−log t_j),   F̃_N=F_N+C_N,

satisfy

    ||F̃_N−G||_(d,U)+||ΓF̃_N−ΓG||_(d,U) ≤ exp(−MU).       (1)

Using exactly the same coefficients and translates of r gives R̃_N and the exact finite-source identity

    L F̃_N=−κR̃_N.                                         (2)

Let P̃_N be the same finite column applied to the source −xf. Then

    ||P̃_N+S^−F̃_N+RG||_(d,U) ≤ exp(−MU).                 (3)

The complete paired forward edge satisfies, with P=K1(U+1),

    Re ∫_(−∞)^U e^(−2dR) conjugate(F̃_N) S^+F̃_N dR
      =Re ∫_R e^(−2dR) conjugate(G) S^+F̃_N dR
       −Re Σ_(2≤j≤P) Λ(j)/sqrt(j)
          ∫_U^∞ e^(−2dR) conjugate(G(R))F̃_N(R+log j)dR
       +O(exp(−MU)).                                      (4)

The sum in (4) is over all integer prime powers, with zero Λ on the other integers. Constants may depend on the fixed source, d and M. Enlarging the constants slightly absorbs the displayed O term into any chosen exponential budget.

The correction coefficients are not a replacement Möbius function and do not satisfy an independently asserted Möbius logarithmic identity. No independent limit or norm bound for R̃_N is claimed.

## 2. The complete Gamma tail

For sufficiently negative x, split the Γ integral at shift 1. The local part, backward part and diagonal terms have a double-theta remainder. The only retained term is

    −∫_(x+1)^∞ k(y−x)f(y)dy.

Since B(1)=∫ f(y)e^(−y/2)dy=0, its slow first exponential can be removed at the price of another left source tail. Exactly,

    k(y−x)−exp(−(y−x)/2)
       =exp(−5(y−x)/2)/(1−exp(−2(y−x))).

Consequently

    Γf(x)=−exp(5x/2)∫_(x+1)^∞
             f(y)e^(−5y/2)/[1−exp(2x−2y)]dy
           +O(exp(−c exp(−2x))).                          (5)

Fixed exponential and polynomial factors are absorbed by decreasing c. The derivative form of the original double-theta envelope pays the local singular integral.

Set

    a_R=R−log N+1,   z_R(y)=exp(R−y).

For n>N, the lower endpoint of (5), with x=R−log n, is at most a_R. Moving it to a_R costs at most

    C exp(5x/2)∫_(−∞)^(a_R) |f(y)|e^(−5y/2)dy.

After multiplication by n^(−1/2) and absolute summation this is bounded by

    C exp(5R/2)N^(−2)∫_(−∞)^(a_R)|f(y)|e^(−5y/2)dy
       ≤C exp(R/2)exp(−cN²exp(−2R)).

The source-local remainders have the same bound. Therefore, uniformly for R≤U once N exp(−U) is sufficiently large,

    Γ(G−F_N)(R)
     =−exp(5R/2)∫_(a_R)^∞ f(y)e^(−5y/2)
          Σ_(n>N) μ(n)/[n³(1−(z_R(y)/n)²)]dy
       +O(exp(R/2)exp(−cN²exp(−2R))).                     (6)

The denominator is at least 1−exp(−2). The entire n-series is absolutely convergent. Formula (6) retains every Gamma layer through one rational resolvent; it is not a truncated infinite moment expansion.

For completeness, the ΓG on the left of (6) is the canonical Γ applied to the original full G. Indeed the absolutely convergent sum Σ μ(n)n^(−1/2)Γf(R−log n) has transform β(s)B(s)/ζ(s) on 1<Re s<3, where

    β(s)=1/2[ψ(s/2)+ψ((1−s)/2)]−log π.

The source moments remove the ±1/2 exponential tails, leaving Γf=O(exp(−5|x|/2)). Move the inverse transform to the buffered line σ1 from Section 1. The cited activated-safe quotient proof supplies the height decay; the pole of β at s=1 is canceled by the at-least-double zero of B/ζ there. There are no uncanceled quotient poles to the right of σ1. On σ1 the complete Γ kernel applied to G has an absolutely justified Laplace exchange: its future decay requires |σ1−1/2|<1/2, the actual right growth is strictly smaller than σ1−1/2, and two fixed derivatives pay the local singularity. Both expressions thus have the identical transform. This identifies the full sum with canonical ΓG and proves (6) with that meaning.

## 3. Exact tail measure and moment-matched columns

Fix a=1/16. Let x_j be the K Chebyshev roots in [a,1], with Lagrange polynomials L_j of degree K−1. Explicitly one may take

    x_j=(1+a)/2+(1−a)/2 cos((2j−1)π/(2K)).

Define the finite signed measure and coefficients

    η_N=Σ_(n>N) μ(n)n^(−3) δ_((N/n)²),
    w_j=∫ L_j(x)dη_N(x),
    t_j=N/sqrt(x_j),   c_j=w_j t_j^(5/2).                 (7)

Each series defining w_j is absolutely convergent. The values μ(n) in its complete tail are retained exactly.

The total variation of η_N is at most CN^(−2). Chebyshev interpolation has a polynomial Lebesgue bound on its node interval. Outside that interval, the Chebyshev extremal inequality gives the factor

    ρ^K,   ρ=(1+sqrt(a))/(1−sqrt(a))=5/3

on the full interval x∈[0,1]. For instance, applying this inequality separately to L_j and using their interval Lebesgue bound gives the sufficient coarse estimate

    sup_(x∈[0,1]) Σ_j |L_j(x)| ≤C K²ρ^K.

It follows that

    Σ_j |w_j|≤C N^(−2)K²ρ^K,
    Σ_j |c_j|≤C N^(1/2)K²ρ^K.                            (8)

In particular the coefficients are real, all nodes lie in [N,4N], and the exact matched moments are

    Σ_j c_j t_j^(−5/2−2h)
      =Σ_(n>N) μ(n)n^(−3−2h),   h=0,…,K−1.              (9)

There is no assertion that Σ_j c_j vanishes or has a sign.

## 4. Approximation of the full resolvent

For 0≤r≤exp(−2), let F_r(x)=1/(1−rx). Its exact degree-(K−1) interpolation remainder is

    F_r(x)−Σ_j L_j(x)F_r(x_j)
       =r^K ∏_j(x−x_j)/[(1−rx)∏_j(1−rx_j)].             (10)

For x∈[0,1], every |x−x_j|≤1 and every denominator factor is at least 1−exp(−2). Thus

    |F_r(x)−Σ_j L_j(x)F_r(x_j)|≤Cq^K,
    q=1/(e²−1)<1.

Integration against η_N gives

    |Σ_(n>N) μ(n)n^(−3)/[1−r(N/n)²]
          −Σ_j w_j/(1−rx_j)|≤C N^(−2)q^K.               (11)

This bound covers the part of the original measure with x<a. It is not an assumption that the measure is supported on the node interval.

Apply the source-level formula (5) separately to the finite correction columns. Moving each lower endpoint to a_R is legitimate since t_j≥N. Its retained integral is the one in (6), with the n-series replaced by Σ_j w_j/[1−(z_R(y)/t_j)²]. The source-local errors and endpoint movements are bounded using (8). Since polynomial factors in N exp(−R) are absorbed into the double-theta exponential, their total is at most

    C K²ρ^K exp(R/2)exp(−cN²exp(−2R)).                   (12)

On y≥a_R put r=(z_R(y)/N)²≤exp(−2), and use (11). The fixed integral ∫|f(y)|e^(−5y/2)dy is finite. Equations (6), (11) and (12) give

    |Γ(F̃_N−G)(R)|
       ≤C exp(5R/2)N^(−2)q^K
         +C K²ρ^K exp(R/2)exp(−cN²exp(−2R)), R≤U.       (13)

The actual tail G−F_N and the finite correction C_N themselves satisfy the second type of bound in (13). It also holds for their moment-source counterparts, with fixed polynomial losses absorbed into a smaller c.

The first term of (13) has weighted terminal L² norm at most

    C q^K exp((5/2−d)U)N^(−2)
       ≤C q^K exp((1/2−d)U)/(U+1).                      (14)

The second has norm at most

    C K²ρ^K exp((1/2−d)U)exp(−c'K0²(U+1)).              (15)

First choose c in K=ceil(c(U+1)) to pay the desired exponent in (14), then choose K0 to pay (15) and every specified source-tail/pairing budget. These are fixed constants. This proves (1).

## 5. The source equation and the complete D package

Every term in F̃_N is a finite real translate of the same original source. Translation commutation of the complete source operator gives (2), with no infinite convolution of r. The two moments B(0)=B(1)=0 are separately retained by each translate.

For the infinite original Möbius column, all fixed-R source and past-prime exchanges are absolute by the left double-theta tail. Hence the exact identity μ*Λ=−μ log gives

    P+S^−G=−RG,
    P(R)=Σ_(n≥1) μ(n)n^(−1/2)[−xf](R−log n).             (16)

The original n>N moment-source tail is exponentially small on the terminal interval after the choice of K0. For its past-prime tail, group the absolute double sum by k=jn. Its coefficient is bounded by

    Σ_(j|k)Λ(j)=log k.

The resulting source sum Σ_(k>N) log(k)k^(−1/2)|f(R−log k)| has the same double-theta terminal bound, with only fixed polynomial losses.

The correction moment P_C is also terminal-small. The complete S^−C_N is terminal-small because its extra shifts move every node farther into the original left tail. Thus (16) proves (3).

In particular the correction of the original joint source package has the exact sign

    ΓC_N−S^+C_N+κR_C=S^−C_N,
    D_C=P_C+S^−C_N.                                      (17)

The right side is terminal-small. The individual S^+C_N and κR_C need not be small and may not be deleted. They jointly retain the nonlocal defect of the original hard cutoff. Equations (2), (3) and (17) do not assert a Möbius coefficient identity for the new real nodes.

## 6. The complete short-prime edge

For any finite column A(R)=Σ_l a_l f(R−log t_l) with 1≤t_l≤4N, Chebyshev summation and the source envelope give

    |S^+A(R)|≤C exp(−R/2)Σ_l |a_l|sqrt(t_l).

For F̃_N, (8) yields

    Σ_l |a_l|≤C sqrt(N)K²ρ^K,
    Σ_l |a_l|sqrt(t_l)≤C N K²ρ^K.                        (18)

Together with the pointwise version of the first error in (1), these bounds pay replacement of the first F̃_N column by G in the terminal pairing. At R→−∞ the double-theta error pays the weight, without an independent L² assertion for the complete future operator.

For R>U and j>P, provided P exp(U)/(4N) is large, the positive source tail gives

    |F̃_N(R+log j)|
       ≤C sqrt(N)K²ρ^K exp(−c(j exp(R)/(4N))²).

Use the absolute envelope |G(R)|≤C exp(R/2). Writing Y=4N exp(−R), Chebyshev gives

    Σ_(j>P)Λ(j)j^(−1/2)exp(−c(j/Y)²)
       ≤C sqrt(Y)exp(−c'(P/Y)²).

Consequently the omitted complete prime edge is at most

    C N K²ρ^K exp(−c''(P exp(U)/(4N))²),                 (19)

with a smaller c'' absorbing the remaining R integral. The fixed weight exp(−2dR) only improves this bound for U>0. Take P=K1(U+1) and choose K1 after c,K0,M. The exponential in (19) then pays its complete prefactor. This proves (4). No prime power is omitted from the retained sum.

## 7. Canonical energy and Hilbert-valued use

On any of the activity records from the cited canonical Gamma theorem, (1) also permits the finite-column pairing to inherit the canonical relative bound:

    |Re ∫_(−∞)^U e^(−2dR) conjugate(F̃_N) ΓF̃_N dR|
       ≤C log(U+2)E_d(U)+O(exp(−MU)),
    E_d(U)=∫_(−∞)^U e^(−2dR)|G(R)|²dR.

For this paired statement, carry out construction (1) with the stronger fixed budget M′=M+1. The original source and activated-safe Gamma bounds give ||G||_(d,U)+||ΓG||_(d,U)≤C exp((1/2−d)U); Cauchy therefore pays the extra products of an approximation error with these norms. Enlarging U absorbs the fixed constants. The stronger construction still implies (1) with budget M. This does not provide a sign or a relative bound for the rest of the full D package.

The same construction and proof apply to a fixed Hilbert-space-valued source whenever its norm and fixed derivatives have the stated double-theta envelopes, its two moment vectors vanish, and the same activated-safe canonical Γ identification is available. All tail estimates use norms and Bochner integrals; the scalar coefficients (7) are unchanged. If the source equation is LF=−K R for a fixed bounded operator K on that Hilbert space, the finite corrected equation is LF̃_N=−K R̃_N. No trace assumption, common lower spectral depth, or summation of individual scalar error constants is used.

For example, the compact-filter negative-band source F(R)=P[m(x)ell(R−x)], with fixed smooth compactly supported ell, has its required tail and derivative bounds directly by projection contraction and the original theta multiplier. Its two moments vanish when P annihilates the ground vectors m exp(±x/2) after evenization. When this example is used, its own safe-quotient hypothesis must still be supplied. The differentiated source is −R F(R), including the first moment of ell; it cannot be replaced by ell*(−xf) without that term.

The remaining carrying estimate concerns the complete forward-prime, moment and negative-source package with every correction retained. No bound for that signed package is claimed here.

## 8. Direct columns with the retained H factor

There is also a direct retained-factor version; it does not form H*r. Let H(s)=Σ_(ν≥1)h(ν)ν^(−s) have an absolutely convergent Dirichlet series on every Re s>1/2, and suppose the same buffered activated-safe line is available for H(s)B(s)/ζ(s). Define

    a=h*μ,   c_H=−(h log)*μ,
    G0(R)=Σ_n a(n)n^(−1/2)f(R−log n),
    J0(R)=Σ_n c_H(n)n^(−1/2)f(R−log n).

Replace μ(n) by a(n) in F_N and in the tail measure (7), using the same original source f. If h is complex, the new coefficients w_j,c_j are complex; equations (2) and (17) remain valid by complex linearity and every estimate uses absolute values.

Set H1=Σ_ν|h(ν)|/ν. Direct convolution gives

    Σ_(n≤X)|a(n)|
       ≤Σ_(ν≤X)|h(ν)| floor(X/ν) ≤H1 X.

Abel summation therefore gives Σ_(n>N)|a(n)|n^(−3)≤C H1 N^(−2), and Σ_(n≤N)|a(n)|n^(−1/2)≤C H1 sqrt(N). Every tail-measure, source and complete-prime bound above retains its original N price, multiplied only by a fixed H1-dependent constant. The canonical Gamma identification in Section 2 now has transform βHB/ζ; the absolute H series on the same safe line pays the contour and height bounds. In particular the same N, O(U) correcting nodes in [N,4N], and linear prime range P=K1(U+1) give (1), (2) and (4) directly for G0.

For the moment identity, coefficientwise differentiation and μ*Λ=−μ log give

    (a*Λ)(n)=−a(n)log n−c_H(n).

Consequently (3) becomes

    ||P̃0,N+S^−F̃0,N+RG0+J0||_(d,U)≤exp(−MU).            (20)

All sums are paid on the original source before any limit involving r. The extra logarithmic norm Σ|h(ν)|log(ν)/ν is finite by choosing any absolute line strictly between 1/2 and 1. This also pays the J0 tail and the full common-output difference. No strict coefficient-one moment inequality is transferred merely by comparing two norms.

For specificity, the fixed half-damped factor used with the auxiliary rational-zeta observable is defined by the local formula in [HALF_DAMPED_PROBE.md, Section 3](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/853672f432aa1bbcdfe05b7b8afd6fda2f043ab4/reports/20261011_qrh_selection_bridge/HALF_DAMPED_PROBE.md). Its ideal-prime parameters remain those of that formula: P=Np, a fixed unit-modulus character value κ(p), and a fixed finite excluded set S. In the notation x=P^(−s), y=κ(p)P^(2−6s), it is

    H_p(s)=(1−P^(−2))[1−(1−P^(−1))x−y/P]
              /[(1−y)(1−x)],
    H(s)=∏_(p outside S) H_p(s).

This is a scalar Dirichlet series with positive integer norm delays; it does not identify the rational μ with an ideal Möbius function. On Re s=σ>1/2, expand both denominators geometrically. The absolute coefficient norm of H_p−1 is

    O_σ(P^(−2)+P^(−1−σ)+P^(2−6σ)),

summable over the ideal primes. This proves the required absolute H series directly, not just pointwise convergence of the Euler product. Furthermore

    |(1−P^(−1))x+y/P|
       ≤(1−P^(−1))P^(−σ)+P^(1−6σ)<1.

Thus every numerator is nonzero. Expanding the reciprocal numerator gives the same summable local-defect bound for H_p^(−1)−1. Hence H and H^(−1) both have absolute Dirichlet series on every buffered half-plane Re s≥1/2+δ. The product is nowhere zero there. Any fixed finite factors from the cited convention can be retained explicitly with their own convergent geometric series; the argument requires and uses their corresponding buffered nonvanishing.

It follows that H creates no extra surviving quotient poles. Weighted causal Young for H and its inverse shows E_d(G0;U) comparable to E_d(G;U), with constants independent of U, for each fixed d>0. For the canonical Gamma energy bound, apply the cited record argument directly to G0: its weighted derivative budget is that of G multiplied by Σ|h(ν)|/ν, and its left double-theta tail is preserved by positive delays. The resulting records are G0's own records; they are not presumed to equal a previously selected sequence for G. Combining that bound with the direct finite construction proves the analogue of Section 7 for the retained-factor columns, without an infinite H*r operation.


## 9. Complete prime-density extraction and the centered transition

The continuous prime density can be extracted from the complete finite-column pairing with an exact favorable sign. On the same activity records, the canonical part of the remaining centered boundary is o(UE(U)). The actual shifted finite-column difference remains in the final formula.

Write F=F̃_N for the complete column constructed above, including every original coefficient and moment correction. Let G denote its canonical bare observable, or the retained-H observable G0 of Section 8, and put Δ=F−G. Use G's own activity exponent and future-envelope records:

    0<d<α≤3/8,
    E(U)=||G||_(d,U)²,
    E(U+h)≤e^(2ah)E(U), h≥0,
    α−d<a<1/2−d.

The bound α≤3/8 and the global zero bound Re ρ≤7/8 used below are the separately attributed external inputs from the pinned quasi-Riemann theorem cited in Section 1. An activity exponent α smaller than 3/8 does not improve that global bound for the centered prime multiplier. Every statement below is for these same records and this same canonical observable.

### 9.1. The entire continuous density

Define, on the finite column,

    C^+F(R)=∫_1^∞ t^(−1/2)F(R+log t)dt,
    C^-F(R)=e^(−R/2)∫_(−∞)^R e^(x/2)F(x)dx.

The source moment B(0)=0 gives exactly

    ∫_R e^(x/2)F(x)dx=B(0)Σ_l A_l sqrt(t_l)=0.

All of these integrals are paid by the finite source tails. Changing variables in C^+ therefore gives

    C^+F=−C^-F.                                          (P1)

Set g=e^(−dR)F, λ_c=d+1/2 and h=e^(−dR)C^-F. Then h′+λ_c h=g and h(−∞)=0. Integration by parts on the terminal interval proves

    −Re〈F,C^+F〉_(d,U)
      =Re〈F,C^-F〉_(d,U)
      =λ_c∫_(−∞)^U |h(R)|²dR+|h(U)|²/2≥0.              (P2)

Its value is at most λ_c^(−1)||F||_(d,U)². Causal Young and endpoint Cauchy give

    ||C^-(F−G)||_(d,U)≤λ_c^(−1)||F−G||_(d,U),
    |e^(−dU)C^-(F−G)(U)|≤(2λ_c)^(−1/2)||F−G||_(d,U).

Thus (1), with a stronger fixed exponential budget before pairing as in Section 7, transfers (P2) to the corresponding canonical causal expression Re〈G,C^-G〉_(d,U)≥0, with arbitrarily small exponential error. This never defines C^+G by a generally divergent ordinary future integral. The favorable contribution is O(E(U)); it alone does not provide a margin η(U)UE(U) with η(U)U→∞.

### 9.2. The centered finite-prime multiplier

Take P to be a half-integer and set

    Q_P u(R)=Σ_(j<P)Λ(j)j^(−1/2)u(R+log j)
                −∫_1^P t^(−1/2)u(R+log t)dt.             (P3)

Every rational prime power is retained. After conjugation by e^(−dR), the multiplier for the convention hat u(τ)=∫u(R)e^(iτR)dR is

    M_(P,d)(τ)=Σ_(j<P)Λ(j)j^(d−1/2−iτ)
                  −∫_1^P t^(d−1/2−iτ)dt.

For a fixed sufficiently small ε>0 and |τ|≤T,

    |M_(P,d)(τ)|
      ≤C_(d,ε) P^(3/8+d+ε)log³(P+T+2).                  (P4)

Here is the arithmetic proof. Put w=d−1/2−iτ and T_ζ(s)=−ζ′(s)/ζ(s). Truncated Perron on the initial line Re(z−w)=2 represents the finite sum by the integral of T_ζ(z−w)P^z/z. Move the z line to c=3/8+d+ε, with 0<ε<1/8. The line z−w has real part 7/8+ε. The only crossed pole is z=1+w: all zero poles are strictly to the left of the new line, while z=0 and the trivial-zero poles are farther left.

For clarity, the needed logarithmic-derivative bound follows from the absolutely convergent Hadamard difference for ξ(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/2. With s0=2+i Im s,

    ξ′/ξ(s)−ξ′/ξ(s0)
      =Σ_ρ [(s−ρ)^(−1)−(s0−ρ)^(−1)],

where multiplicities are retained. For 7/8+ε≤Re s≤2, zeros within unit height cost at most C_ε log(2+|Im s|) by their unit-height count and horizontal separation. Far height shells have the convergent reciprocal-square bound and the same total order. At s0 the absolutely convergent zeta derivative and the Gamma factor give O(log(2+|Im s|)). The elementary completed factors therefore give

    |T_ζ(s)−(s−1)^(−1)|≤C_ε log(2+|Im s|).

In particular the weaker bound C_ε log²(2+|Im(z−w)|) suffices on the new line and horizontal segments, which avoid the explicit pole at s=1. Choose Perron height H=(P+T+2)^A with a sufficiently large fixed A. Since P is a half-integer, |P−n|≥1/2 for every integer n. Splitting the truncation error into n comparable to P and the two remaining ranges pays it, as well as the horizontal integrals, by a fixed inverse power of P+T. The vertical integral is at most C P^c log³(P+T+2). The residue is P^(1+w)/(1+w); the continuous integral subtracted in M equals this residue minus 1/(1+w), whose modulus is bounded in terms of d. This proves (P4). No zero spacing or lower bound for ζ′ at a zero is used.

### 9.3. The canonical components on the same record

In the following application, P and Q are fixed positive multiples of U+1, with P rounded to a half-integer. Cut e^(−dR)G(R) smoothly just after U+log P. Its L² norm is at most C P^aE(U)^(1/2) by the common future envelope. The actual fixed-source Gevrey-two estimate in Section 2 of the cited canonical Gamma report, multiplied by a fixed Gevrey-two cutoff, bounds the Fourier tail beyond T=K_*(U+1)² by any prescribed exponential error after K_* is chosen sufficiently large. The Section 8 summatory coefficient estimate gives that same absolute Gevrey budget for G0.

The trivial multiplier bound C P^(d+1/2) pays this discarded Fourier tail. On retained frequencies apply (P4). Terminal Cauchy gives

    |Re〈G,Q_PG〉_(d,U)|
      ≤C P^(3/8+a+d+ε)log³(U+2)E(U)+O(e^(−MU)).          (P5)

The cutoff equals one through the largest shifted argument, so it changes no term in the terminal pairing. Any pairing cost against the absolute norm of G is paid by first choosing a stronger fixed exponential tail budget.

Similarly set V=U+log Q, and cut the second column just after V+log P. Both Cauchy factors use the same record U, and E(V)≤Q^(2a)E(U). Consequently

    |Re∫_U^V e^(−2dR)conjugate(G(R))Q_PG(R)dR|
      ≤C Q^(2a)P^(3/8+a+d+ε)log³(U+2)E(U)
         +O(e^(−MU)).                                    (P6)

Choose d sufficiently close to α, then a sufficiently close to α−d, and ε sufficiently small, so that

    θ_c=3/8+3a+d+ε<1.                                    (P7)

This is possible since α≤3/8. The canonical upper-band contribution in (P6) is therefore O(U^θ_c log³(U+2)E(U))=o(UE(U)). The global 3/8 in (P4) has not been replaced by the possibly smaller activity exponent α.

### 9.4. The full centered edge and its retained transition

On the genuine finite column define S_c^+=S^+−C^+. The whole-minus-edge proof of (4) also applies to the continuous measure dt: its tails satisfy the same Gaussian estimates as the prime measure. Hence, with P=K1(U+1)+O(1) a half-integer,

    Re〈F,S_c^+F〉_(d,U)
      =Re∫_R e^(−2dR)conjugate(G(R))S_c^+F(R)dR
       −Re∫_U^∞ e^(−2dR)conjugate(G(R))Q_PF(R)dR
       +O(e^(−MU)).                                      (P8)

Every whole-axis future pairing has the finite column F in its future slot. The complete finite-column moment cancellation (P1) is retained; no independent canonical future operator is introduced.

To bound the upper extent, take Q=K2(U+1) and V=U+log Q, with K2 chosen after c,K0,K1 and every earlier budget. Recall

    t_l≤4N,   Σ_l|A_l|sqrt(t_l)≤C N K²(5/3)^K,
    N=floor(e^U K0 sqrt(U+1)),   K=ceil(c(U+1)).

For R≥V, write Y=4Ne^(−R), which is small for sufficiently large U. Complete Chebyshev summation and elementary integration give

    Σ_(j≥2)Λ(j)j^(−1/2)e^(−c(j/Y)²)
       +∫_1^∞ t^(−1/2)e^(−c(t/Y)²)dt
      ≤C sqrt(Y)e^(−c′/Y²).

It follows that

    |S_c^+F(R)|+|Q_PF(R)|
      ≤C N K²(5/3)^K e^(−R/2)
          exp[−c0(e^R/(4N))²].                           (P9)

Multiply by |G(R)|≤Ce^(R/2) and e^(−2dR), then integrate R≥V. The result is at most

    C N K²(5/3)^K e^(−2dV)
          exp[−c1 Q²/(K0²(U+1))].

Choosing K2 last makes this O(e^(−MU)). This is a bound for the actual finite-column upper edge, including every correction, rather than for an infinite canonical-canonical edge.

Use F=G+Δ only on the retained finite band, and apply (P6). Then

    Re∫_U^∞ e^(−2dR)conjugate(G(R))Q_PF(R)dR
      =Re∫_U^V e^(−2dR)conjugate(G(R))Q_PΔ(R)dR
       +O(U^θ_c log³(U+2)E(U))+O(e^(−MU)).                (P10)

Equations (P1), (P2), (P8) and (P10) preserve the same finite-source equation. In particular its carrying expression is exactly

    P_F+ΓF−S^+F+κR_F
      =P_F+ΓF−S_c^+F+C^-F+κR_F.

The positive causal term (P2) remains. The source-moment column P_F, full κR_F, whole centered pairing in (P8), and actual Δ transition in (P10) still require a joint signed comparison. There is no proved sign or relative bound for that complete package. The terminal approximation in (1) cannot be applied to shifted points R+log j beyond U in the transition.

If the error in (P10) is absorbed separately into a proposed margin η(U)UE(U), it must be dominated at that scale, for example by η(U)U/[U^θ_c log³(U+2)]→∞. A fixed or inverse-logarithmic fractional margin suffices. The weaker condition η(U)U→∞ for an undivided full joint expression cannot be reused after discarding the larger extracted error in (P10).


## 10. A polynomial-in-K bound for the actual canonical correction multiplier

This estimate concerns the prescribed canonical correction itself, not an alternative finite approximation. Its proof, and the fixed-jet proof in Section 11, do not use the external 7/8 input. It keeps all original signed tail data. On a fixed spectral window its polynomial K cost replaces the total-variation coefficient budget; no sign or source-relative bound for the complete transition package follows.

### 10.1. Exact prescribed multiplier

Use exactly the finite-source transfer construction in Section 3: a=1/16, K Chebyshev roots x_j in [a,1], Lagrange polynomials L_j, and

 eta_N=sum_(n>N) mu(n)n^(-3) delta_((N/n)^2),
 w_j=integral L_j d eta_N,
 t_j=N/sqrt(x_j), c_j=w_j t_j^(5/2).

Here mu is the genuine rational Möbius function. The real nodes and coefficients are unchanged. For s=σ+iτ let

 beta=(3-s)/2, b=Re beta=(3-σ)/2,
 p_(K,s)(x)=sum_j x_j^(-beta)L_j(x).

The true corrected multiplier is exactly

 Mtilde_N(s)=sum_(n<=N)mu(n)n^(-s)
   +N^(3-s) sum_(n>N)mu(n)n^(-3)
                                  p_(K,s)((N/n)^2).       (M1)

All tail series in (M1) converge absolutely, since p is a finite polynomial. Equation (M1) follows directly from sum_j c_j t_j^(1/2-s)=sum_j w_j t_j^(3-s). It retains all signed original tail data.

### 10.2. Statement

For 0<=σ<=1, |τ|<=T and K>=2, put v=(1-σ)/2=b-1 and

 F_v(K)=(K^v-1)/v if v>0, F_0(K)=log K.

There is an explicit permissible height budget

 C_T=C(1+T)^2 exp(pi T/2)                                 (M2)

with an absolute C such that

 |Mtilde_N(s)|
 <=A_σ(N)+C_T N^(1-σ)[K^v+F_v(K)],                       (M3)

where

 A_σ(N)=1+(N^(1-σ)-1)/(1-σ) if σ<1,
 A_1(N)=1+log N.

In particular, for any fixed δ>0 and 0<=σ<=1-δ,

 |Mtilde_N(σ+iτ)|<=C_δ C_T (N sqrt(K))^(1-σ).              (M4)

Thus on every fixed compact height/real-part window strictly left of one the prescribed multiplier has only polynomial K cost. The former total-variation estimate exp(K log(5/3)) is unnecessary at these particular spectral evaluation points. No Möbius cancellation is used to establish (M3).

### 10.3. Complete Chebyshev coefficient bound

Map x=(17+15y)/32, y=cos θ. Put r=3/5. The exact factorization is

 x=(25/64)(1+r exp(iθ))(1+r exp(-iθ)).

For q_n=(beta)_n/n!, the absolutely convergent binomial series gives

 x^(-beta)=(25/64)^(-beta)
 [sum_(n>=0)(-1)^n q_n r^n exp(inθ)]
 [sum_(n>=0)(-1)^n q_n r^n exp(-inθ)].                    (M5)

Write its Chebyshev series as sum_(k>=0) d_k T_k(y), with the constant coefficient convention absorbed into d_0. Then

 |d_k|<=C_T r^k(k+1)^(b-1), k>=0.                       (M6)

Here is a direct uniform budget. Writing w=Im beta, 1<=b<=3/2,

 |q_n|=[(b)_n/n!] product_(l=0)^(n-1)
                                  sqrt(1+w²/(b+l)²).

The first factor is at most C(n+1)^(b-1), uniformly in b. The sum of logarithms in the second factor is bounded by a first term plus its decreasing integral. Using integral_0^infinity log(1+w²/t²)dt=pi|w| gives

 |q_n|<=C(1+|w|)exp(pi|w|/2)(n+1)^(b-1).

The coefficient of exp(ikθ) in (M5) is

 (25/64)^(-beta)(-1)^k r^k
                       sum_(n>=0) q_(n+k)q_n r^(2n).

Since (n+k+1)^(b-1)<=(k+1)^(b-1)(n+1)^(b-1) and 0<=2b-2<=1, the remaining r^(2n) sum is uniformly finite. As |w|=|τ|/2, this proves (M6) with (M2). The factor two for nonconstant Chebyshev coefficients is harmless.

This proof does not take an unproved uniform-in-height singularity asymptotic. It supplies the displayed exponential height cost explicitly.

### 10.4. Extrapolation and every root-alias term

The K interpolation nodes are the zeros of T_K, so their angles are θ_j=(2j-1)pi/(2K). At these nodes every T_n aliases either to zero (when n is an odd multiple of K) or to plus/minus T_k with 0<=k<K. In particular its interpolant has degree below K and is exactly one such signed Chebyshev polynomial. The absolutely convergent expansion (M5) may be interpolated termwise.

For x in [0,1], the transformed y=(32x-17)/15 lies in [-17/15,1]. Put rho=5/3. Then

 |T_k(y)|<=rho^k.

The sum of all aliased terms n>=K is therefore at most

 C_T rho^K sum_(n>=K) r^n(n+1)^(b-1)
 <=C C_T K^(b-1).                                      (M7)

This includes every alias and every sign; none is dropped. It already suffices for its eventual weighted tail sum.

For the unaliased terms k<K one has the more useful x-dependent estimate

 |sum_(k<K)d_k T_k((32x-17)/15)|
 <=C C_T min(K^b,x^(-b)),                               (M8)

with the x=0 convention given by K^b. To prove it for 0<=x<=a, set

 R(x)=exp(arccosh((17-32x)/15)).

Then |T_k|<=R(x)^k, R(0)=rho, and

 d/dx log R(x)=-32/sqrt((17-32x)^2-225)<=-4.

Hence r R(x)<=exp(-4x). Summing (M6) gives (M8). For a<=x<=1, |T_k|<=1 and the r^k sum is bounded by a constant; min(K^b,x^(-b))>=1, so (M8) remains true.

Combining (M7)-(M8), the full prescribed interpolant satisfies

 |p_(K,s)(x)|
 <=C C_T [min(K^b,x^(-b))+K^(b-1)], 0<=x<=1.            (M9)

The endpoint x=0, which lies outside the node interval, is paid explicitly. A Lebesgue constant on [a,1] alone would not justify this estimate.

### 10.5. The actual Möbius-tail summation gains one K power

Insert x=(N/n)^2 into (M9). For n<=N sqrt(K) the minimum is (n/N)^(2b); for larger n it is K^b. Therefore

 sum_(n>N)n^(-3) min(K^b,(n/N)^(2b))
 <=C N^(-2)[K^(b-1)+F_(b-1)(K)].                       (M10)

For b>1 this follows by summing N^(-2b)n^(2b-3) from N to N sqrt(K), and then K^b n^(-3). At b=1 the first sum is harmonic and gives log K. Integral-plus-endpoint estimates make the constant uniform for 1<=b<=3/2 and N>=1. The extra alias term in (M9) contributes only

 K^(b-1) sum_(n>N)n^(-3)<=C N^(-2)K^(b-1).              (M11)

Use |mu(n)|<=1 only at this final estimate. Multiplication by |N^(3-s)|=N^(3-σ) in (M1), and the elementary bound for the original partial multiplier, proves (M3). For σ<=1-δ, v>=δ/2, so F_v(K)<=2K^v/δ, and A_σ(N)<=C_δ N^(1-σ). This proves (M4).

### 10.6. Consequences and strict scope

For the original scales N≈exp(U)sqrt(U+1), K≈U+1, (M4) has the shape

 |Mtilde_N(s)|<=C_(δ,T) [exp(U)(U+1)]^(1-Re s)           (M12)

on a fixed compact spectral window left of one. All coefficients remain the actual canonical coefficients, including the complete genuine μ tail. This is a genuine improvement in the finite-window arithmetic multiplier bound.

It is not a signed or source-relative estimate. The factor N^(1-Re s) remains, and no same-record bound by the actual canonical energy has been proved. The height budget (M2) is exponential in T, so a fixed-window statement cannot be substituted for a growing-height or full-zero expansion estimate. In particular it is not paid by a square-root-exponential source tail on its own. The actual Delta transition, the whole centered pairing, P and kappa R must still be retained jointly. No new zero exclusion or coefficient-one margin follows from (M3).


## 11. Fixed true jets of the same prescribed multiplier

The coefficients and nodes remain exactly those of Sections 3 and 10. The result below covers fixed derivative orders, including all jets in any fixed finite zero set; no growing multiplicity or height budget is implicit.

### 11.1. Fixed derivative statement

For each δ>0, T<infinity and fixed nonnegative integer q, there is a finite constant C_(δ,T,q) such that, for 0<=σ<=1-δ, |τ|<=T, N>=1 and K>=2,

 |(d/ds)^q Mtilde_N(σ+iτ)|
 <=C_(δ,T,q) (N sqrt(K))^(1-σ)
                    [1+log N+log(K+2)]^q.               (J1)

The constant may depend on q. No uniform statement for growing zero multiplicity or a growing spectral window is asserted. In particular (J1) may be used for all the finitely many true jets in a fixed finite set, but not for a full unbounded zero expansion without a new budget.

### 11.2. A buffered coefficient lemma

The proof of the Section 10 value theorem's Chebyshev coefficient and interpolation estimates also works uniformly on

 -1/2<=Re s<=1-δ/2, |Im s|<=T+1.

Indeed b=Re((3-s)/2) then lies in a fixed compact interval inside (1,7/4]. The only changed binomial sum is sum_n r^(2n)(n+1)^(2b-2), which remains uniformly finite. Its x-dependent interpolation estimate is still

 |p_(K,s)(x)|<=C_(δ,T)
                    [min(K^b,x^(-b))+K^(b-1)], 0<=x<=1. (J2)

This buffer pays small Cauchy circles even at the endpoint σ=0; it is not silently assumed that such circles remain in the Section 10 theorem's [0,1] strip.

### 11.3. Cauchy is applied before the N factor

For a point s=σ+iτ in (J1), set

 epsilon=min(δ/4,1/4,1/log(K+2)).

Every point s+z with |z|<=epsilon belongs to the buffered strip. Put b=Re((3-s)/2), b'=Re((3-s-z)/2). Then |b'-b|<=epsilon/2.

Split 0<=x<=1 into x<=1/K and x>=1/K. In the first interval min(K^(b'),x^(-b'))=K^(b'); in the second it equals x^(-b'). In both intervals

 min(K^(b'),x^(-b'))<=K^(epsilon/2) min(K^b,x^(-b)),
 K^(b'-1)<=K^(epsilon/2)K^(b-1),
 K^(epsilon/2)<=exp(1/2).

Cauchy's derivative estimate applied to the entire-in-s polynomial p_(K,s)(x), using (J2), consequently gives

 |(d/ds)^q p_(K,s)(x)|
 <=C_(δ,T,q)[1+log(K+2)]^q
                    [min(K^b,x^(-b))+K^(b-1)].           (J3)

The radius is never applied to the complete product N^(3-s). Doing so would introduce an unnecessary N^epsilon loss. Instead differentiate that explicit factor separately.

### 11.4. The same genuine tail sum

Differentiate the exact formula

 Mtilde_N(s)=M_N(s)+N^(3-s)
                 sum_(n>N)mu(n)n^(-3)p_(K,s)((N/n)^2).

Every derivative may pass under this absolutely convergent series: each fixed derivative of p is still a finite polynomial in x and its node values are entire functions of s. Insert (J3) into the unchanged split at n=N sqrt(K), exactly as in Sections 10.4--10.5. It costs at most

 C_(δ,T,q)N^(-2)K^((1-σ)/2)[1+log(K+2)]^q.

Leibniz with N^(3-s) adds powers of log N, bounded by the bracket in (J1). The original finite Dirichlet polynomial has

 |M_N^(q)(s)|<=sum_(n<=N)(log n)^q n^(-σ)
 <=C_δ N^(1-σ)[1+log N]^q.

These estimates prove (J1).

### 11.5. Scope

The improvement removes the artificial exponential-in-K coefficient price when the original canonical correction is tested at a fixed spectral point or fixed finite jets. It retains the N^(1-Re s) scale, gives no favorable sign, and does not compare the complete actual transition with the same-record G energy. The whole centered/P/kappa R compensation remains mandatory.


## 12. Genuine Mertens cancellation in the prescribed canonical multiplier

The original Chebyshev nodes and complete signed Möbius tail remain unchanged. A power bound for the genuine Mertens function improves the fixed-window exponent from 1−Re s in Section 10 to theta−Re s, including fixed true jets. Sections 12.1–12.6 prove this transfer. Sections 12.7–12.10 supply the standard analytic implication from the explicitly attributed external zero-free half-plane; this is not a new zero-free theorem. The whole source/prime transition still has no proved favorable joint sign or same-record relative margin.

### 12.1. Hypothesis and exact objects

Let 0<theta<1 and suppose the genuine rational Mertens function obeys

 M(x)=sum_(n<=x)mu(n),  |M(x)|<=C_M x^theta, x>=1.         (MT1)

Use the exact prescribed correction from Sections 3 and 10 of this report: a=1/16, K Chebyshev roots x_j in [a,1], Lagrange polynomials L_j,

 eta_N=sum_(n>N)mu(n)n^(-3)delta_((N/n)^2),
 w_j=integral L_j d eta_N,
 t_j=N/sqrt(x_j), c_j=w_j t_j^(5/2).

For s=σ+iτ, beta=(3-s)/2, b=Re beta, put

 p_(K,s)(x)=sum_j x_j^(-beta)L_j(x).

The actual multiplier is exactly

 Mtilde_N(s)=M_N(s)+N^(3-s)
                   sum_(n>N)mu(n)n^(-3)p_(K,s)((N/n)^2),
 M_N(s)=sum_(n<=N)mu(n)n^(-s).                           (MT2)

Put X=N sqrt(K). Here N>=1 and K>=2. No signed sum is replaced by a different coefficient sequence.

### 12.2. Conclusions

For every fixed δ>0 and finite T, uniformly on 0<=σ<=theta-δ, |τ|<=T,

 |Mtilde_N(s)|<=C_(theta,delta) C_M
                  (1+T)^3 exp(pi T/2) X^(theta-σ).        (MT3)

The assertion is empty if the indicated strip is empty. At the boundary σ=theta,

 |Mtilde_N(theta+iτ)|
 <=C_(theta,T) C_M[1+log N+log K].                       (MT4)

For each fixed derivative order q, the interior strip also has

 |partial_s^q Mtilde_N(s)|
 <=C_(theta,delta,T,q) C_M X^(theta-σ)
                         [1+log N+log(K+2)]^q.            (MT5)

Constants in (MT5) may depend on q. No growing-height or growing-multiplicity estimate is implied. No decay assertion for σ>theta is made: in that region an unremoved value 1/zeta(s) need not vanish.

### 12.3. Localized complete root-alias and derivative estimates

The elementary coefficient proof in Section 10 above gives, for 0<=σ<=1 and |τ|<=T,

 x^(-beta)=sum_(n>=0)d_n T_n((32x-17)/15),
 |d_n|<=C_T r^n(n+1)^(b-1),
 r=3/5, C_T=C(1+T)^2 exp(pi T/2).                        (MT6)

Its binomial factorization is x=(25/64)(1+r exp(iu))(1+r exp(-iu)); the full coefficient and height budget is already proved there. Here we sharpen the treatment of every alias and its x derivative.

The Chebyshev-root interpolant of T_n is either zero or plus/minus T_m with 0<=m<K. Let A_K(x) denote the sum of all aliased terms n>=K. For 0<=x<=a/2 set

 R(x)=exp(arccosh((17-32x)/15)).

Then R(x) stays uniformly above one, R(0)=5/3, and

 rR(x)<=exp(-4x).

The exact hyperbolic formulas for T_m and U_(m-1), together with the bounded change-of-variable derivative, give

 |T_m((32x-17)/15)|<=R(x)^m,
 |d/dx T_m((32x-17)/15)|<=C m R(x)^m.

Therefore summing all n>=K using (MT6) yields

 |A_K(x)|<=C C_T K^(b-1) exp(-4Kx),
 |A_K'(x)|<=C C_T K^b exp(-4Kx), 0<=x<=a/2.              (MT7)

No alias is omitted: the uniform bounds R(x)^K and C K R(x)^K pay each of its possible degrees m<K before summing the entire geometric n tail.

For a/2<=x<=1, choose the fixed R_*=R(a/2)<5/3. The elementary uniform polynomial derivative bound gives

 |T_m|<=R_*^m,
 |dT_m/dx|<=C m^2 R_*^m

through this whole interval, including the points where the transformed y enters [-1,1]. Thus

 |A_K(x)|<=C C_T K^(b-1)(rR_*)^K,
 |A_K'(x)|<=C C_T K^(b+1)(rR_*)^K.                       (MT8)

The unaliased sums, using (MT6) and the same split at a/2, satisfy

 |sum_(n<K)d_n T_n|<=C C_T min(K^b,x^(-b)),
 |d/dx sum_(n<K)d_n T_n|
                     <=C C_T min(K^(b+1),x^(-b-1)).      (MT9)

For example, in the first interval these are the sums of (n+1)^(b-1) exp(-4nx) and n(n+1)^(b-1) exp(-4nx). In the second interval the fixed geometric ratio rR_*<1 pays all derivatives uniformly.

The localized aliases in (MT7) absorb into the respective envelopes in (MT9): split at x=1/K. For x>=1/K, the ratios to x^(-b) and x^(-b-1) are at most

 C K^(-1)(Kx)^b exp(-4Kx),
 C K^(-1)(Kx)^(b+1) exp(-4Kx),

and for x<=1/K the comparison with K^b and K^(b+1) is immediate. The bounds (MT8) are uniformly bounded and the respective envelopes are at least one. We have proved the full estimates

 |p_(K,s)(x)|<=C C_T min(K^b,x^(-b)),
 |p_(K,s)'(x)|<=C C_T min(K^(b+1),x^(-b-1)), 0<=x<=1.   (MT10)

At x=0 use the finite K values. In particular

 |p_(K,s)(x)|+x|p_(K,s)'(x)|
                 <=C C_T min(K^b,x^(-b)).               (MT11)

It is essential to retain the localization (MT7). The old uniform alias bound K^(b-1), on its own, would leave an avoidable extra K^((1-theta)/2) in the signed Abel estimate.

### 12.4. Abel summation with the genuine signed Mertens function

For fixed s define H_s(t)=t^(-3)p_(K,s)((N/t)^2), t>=N. Its ordinary derivative is

 H_s'(t)=-t^(-4)[3p_(K,s)(x)+2x p_(K,s)'(x)],
 x=(N/t)^2.                                             (MT12)

By (MT11),

 |H_s'(t)|<=C C_T t^(-4)
                      min(K^b,(t/N)^(2b)).              (MT13)

The exact Stieltjes/Abel formula, including its N endpoint, is

 sum_(n>N)mu(n)H_s(n)
 =-M(N)H_s(N)-integral_N^infinity M(t)H_s'(t)dt.          (MT14)

The upper endpoint vanishes because theta<1<3 and p is a finite polynomial. Formula (MT14) holds with the same n>N convention whether N is integral or not. Since p_(K,s)(1) is uniformly O(C_T), its endpoint costs C C_M C_T N^(theta-3).

Insert (MT1) into (MT14), multiply by N^(3-σ), and split the integral at X=N sqrt(K). Recalling 2b=3-σ, the two exact powers are

 N^(3-σ)N^(-2b) integral_N^X t^(theta-4+2b)dt
 =integral_N^X t^(theta-σ-1)dt,                          (MT15)

 N^(3-σ)K^b integral_X^infinity t^(theta-4)dt
 =X^(theta-σ)/(3-theta).                                (MT16)

For σ<theta, (MT15) is (X^(theta-σ)-N^(theta-σ))/(theta-σ); for σ=theta it is log(X/N)=(1/2)log K. Thus the complete signed correction has precisely the effective scale X and no extra K power.

The original finite Dirichlet polynomial has the separate exact Abel formula

 M_N(s)=M(N)N^(-s)+s integral_1^N M(t)t^(-s-1)dt.         (MT17)

For σ<=theta-δ this is O(C_M(1+|s|/δ)N^(theta-σ)); at σ=theta it is O(C_M(1+|s|log N)). Combining (MT14)-(MT17) proves (MT3)-(MT4). The harmless factor (1+T) beyond C_T pays (MT17).

### 12.5. Fixed true jets with the same signed estimate

The coefficient and localized derivative proof extends to a buffered real strip -1/2<=Re s<=1-delta_0, with delta_0>0, since b stays in a fixed compact interval inside (1,7/4]. Every geometric series above remains uniformly finite there.

For s in the interior strip of (MT3), take a Cauchy radius

 epsilon=min(δ/4,1/4,1/log(K+2)).

The enlarged points still have real part below theta-δ/2<1 and at least -1/4. Apply Cauchy separately to p_(K,s)(x) and its x derivative, using (MT10). Splitting x at 1/K shows that changing b by at most epsilon/2 multiplies either envelope by at most K^(epsilon/2)<=exp(1/2). Therefore, for each fixed j,

 |partial_s^j p|+x|partial_s^j p'|
 <=C_(theta,delta,T,j)[1+log(K+2)]^j
                                   min(K^b,x^(-b)).      (MT18)

Differentiate only this polynomial data by Cauchy. The explicit factor N^(3-s) in (MT2) is differentiated separately, so no N^epsilon loss occurs. Derivatives may pass under the absolutely convergent tail series. Apply the same Abel identity (MT14) to each derivative polynomial; (MT18) pays the derivative of H exactly as before. Leibniz adds only the displayed powers of log N and log K.

For the original finite polynomial, Abel summation of (log t)^q t^(-s) pays its derivative by C_(q,delta)N^(theta-σ)[1+log N]^q; the endpoint at t=1 is harmless, including q=0. This proves (MT5).

### 12.6. What a 7/8 application must say

Sections 12.7–12.10 establish (MT1) from the explicitly attributed external zero-free half-plane, with theta=7/8+epsilon<1. Consequently, for every fixed 0<ε<1/8 and fixed spectral window satisfying 0<=Re s<=7/8 the value and fixed-jet bounds become

 |partial_s^q Mtilde_N(s)|
 <=C_(epsilon,T,q) (N sqrt(K))^(7/8+epsilon-Re s)
                         [1+log N+log(K+2)]^q.            (MT19)

Here δ may be chosen as epsilon. This corollary uses genuine signed Möbius cancellation; unlike the earlier absolute-coefficient theorem it depends on that Mertens input. The implication from a zero-free half-plane to (MT1) must not be justified merely by a crude fixed-polynomial reciprocal-zeta height bound. The needed subpower-height/log-zeta step is supplied in full in Sections 12.7–12.9 below.

Even when (MT19) is applicable, it uses the global arithmetic exponent rather than the actual source activity, keeps exponential height constants, and supplies no one-sided estimate for the Delta/whole-centered/P/kappa R joint. It does not by itself provide a same-record relative bound, a full-height sum, or any new zero exclusion.

### 12.7. Hypothesis and conclusion

Assume a fixed theta_0 in (0,1) such that zeta(s) has no zero in Re s>theta_0. Then for every epsilon>0,

 M(x):=sum_(n<=x) mu(n)=O_epsilon(x^(theta_0+epsilon)).       (ZF1)

For the RH research application, theta_0=7/8 is supplied solely by the separately attributed external September 30 theorem, not by the original-source eigen-equation or by the new Chebyshev interpolation calculation. The pinned primary source is OpenAI, The Quasi-Riemann Hypothesis, main theorem:
https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L106-L119
The existing project audit of that external theorem is retained. Nothing here strengthens its zero-free region.

### 12.8. Subpower reciprocal bounds in a strict inner half-plane

Remove the pole without introducing a zero:

 Z(s)=(s-1)zeta(s)/(s+1).

At s=1 take the removable value 1/2. The only new possible pole is s=-1, outside the half-plane. The hypothesis makes Z holomorphic and zero-free on the simply connected half-plane Re s>theta_0. Hence it has a holomorphic logarithm F(s)=log Z(s), normalized by continuation from the real axis to the right of 1.

For Re s=2, F is uniformly bounded. Indeed the absolutely convergent logarithmic Euler product gives a bounded branch of log zeta there, and log((s-1)/(s+1)) has a uniformly bounded branch on Re s>=2. Their sum agrees with F.

Fix theta_0<L<sigma_*<2. Standard fixed-strip polynomial growth of zeta gives

 Re F(s)=log|Z(s)|<=C log(3+|Im s|)

on every fixed closed strip inside Re s>theta_0. Apply Borel--Caratheodory on disks centered at 2+it, using a radius slightly larger than 2-L but still smaller than 2-theta_0. The center value F(2+it) is bounded, and the real-part upper bound holds on each disk. This gives

 |F(s)|<=C_L log(3+|Im s|),  L<=Re s<=2.                    (ZF2)

The bounded-height part follows from compactness. This step bounds the actual holomorphic logarithm, not only its real part.

For a fixed real t, apply the bounded-strip three-lines theorem to

 F_t(s)=F(s) exp((s-it)^2),  L<=Re s<=2.

On the left boundary its supremum is O_L(log(3+|t|)); on the right boundary it is O(1). The Gaussian factor makes both suprema finite and pays all distant imaginary heights. At s=sigma+it, sigma_*<=sigma<=2, three-lines therefore yields

 |F(sigma+it)|<=C_(L,sigma_*) [log(3+|t|)]^a,
 a=(2-sigma_*)/(2-L)<1.                                  (ZF3)

Consequently, for every eta>0,

 |1/zeta(sigma+it)|<=C_(sigma_*,eta)(3+|t|)^eta,
 sigma_*<=sigma<=2.                                      (ZF4)

The factor (s-1)/(s+1) in 1/zeta=(s-1)/((s+1)Z) is bounded on this strip; the removable zero at s=1 causes no problem. Equation (ZF4), rather than a fixed polynomial-height bound, is the input needed below.

### 12.9. Truncated Perron with its full error

It suffices to treat small epsilon with theta_0+epsilon<1; larger epsilon follows from |M(x)|<=x. Replace x by y=floor(x)+1/2, so M(x)=M(y) and y is at distance at least 1/2 from every integer. Take

 c=1+1/log y, T=y^2,
 sigma_*=theta_0+epsilon/2, eta=epsilon/8.

For large y, c<=2. The absolutely convergent Dirichlet series 1/zeta(s)=sum mu(n)n^(-s) and the usual truncated Perron kernel give

 M(y)=(1/(2pi i)) integral_(c-iT)^(c+iT) y^s/[s zeta(s)] ds
       +O(y log y/T).                                   (ZF5)

For clarity, the absolute kernel error is bounded by

 sum_n (y/n)^c min(1, 1/(T |log(y/n)|)).

On y/2<=n<=2y, use |log(y/n)|>=c_1|y-n|/y and |y-n|>=1/2 to obtain O(y log y/T). On either outside range, |log(y/n)| is bounded below; the elementary sums at c=1+1/log y give the same bound. Thus no cancellation or unproved short-interval estimate is hidden in (ZF5).

Shift the finite rectangle to Re s=sigma_*. Its interior is zero-free for zeta and avoids s=0, while 1/zeta is holomorphic at s=1. Hence no residue is crossed. Equation (ZF4) bounds the vertical integral by

 C y^(sigma_*) [1+integral_1^T t^(eta-1)dt]
 <=C y^(sigma_*) T^eta
 =C y^(theta_0+3epsilon/4).                              (ZF6)

Each horizontal edge is at most

 C y^c T^(eta-1)=O(y^(-1+epsilon/4)),                     (ZF7)

since y^c=e y. The Perron error is O(log y/y). Combining (ZF5)--(ZF7) proves (ZF1), with room in the exponent.

### 12.10. Permitted use in the canonical correction

For any chosen theta>7/8, this supplies the genuine estimate |M(x)|<=C_theta x^theta. It can be inserted into Abel summation of the *same* true-mu canonical tail. The canonical coefficient construction remains unchanged.

The interpolation proof in Sections 12.3–12.5 retains the x-localized root-alias error and controls x p'(x); replacing it by its uniform K^(b-1) bound loses an extra K^((1-theta)/2). That interpolation estimate is a distinct step from this standard dependency lemma. No original-source sign, activity-relative bound, or full P/kappa R/transition margin follows from (ZF1).

### 12.11. The original retained-H columns

The same signed estimate applies to the exact retained-factor columns of Section 8. Suppose theta>1/2 and (MT1) holds. For a=h*mu and c_H=-(h log)*mu, the finite convolution identities give

 sum_(n<=x)a(n)=sum_(nu<=x)h(nu)M(x/nu),
 sum_(n<=x)c_H(n)=-sum_(nu<=x)h(nu)log(nu)M(x/nu).

Consequently their partial sums are bounded, respectively, by

 C_M x^theta sum_nu |h(nu)|nu^(-theta),
 C_M x^theta sum_nu |h(nu)|log(nu)nu^(-theta).

Both coefficient sums are finite. Section 8 proves absolute convergence of H on every line strictly right of 1/2; choose a line strictly between 1/2 and theta to absorb the extra logarithm. Apply the same prescribed nodes and interpolation correction directly to a or c_H. The proof (MT12)–(MT18) uses only the displayed partial-sum bound and the unchanged polynomial data, so it gives the same effective power (N sqrt(K))^(theta-Re s) and fixed-jet logarithmic factors, multiplied by these fixed H-dependent constants. No infinite H*r convolution, replacement record sequence, or signed relative margin is introduced.


## 13. Exact self-resonance at the effective scale N sqrt(K)

The prescribed correction remains unchanged. This section uses only the localized all-alias interpolation estimates in Section 12.3, not the Mertens hypothesis or the external 7/8 theorem. It computes the complete regular Taylor coefficients of the local Perron kernel and its fixed genuine-zero residue block. It does not estimate the remaining contour or the whole signed source joint.

### 13.1. Exact kernel and its regular Taylor coefficients

Write the actual interpolant as

 p_(K,s)(x)=sum_(k=0)^(K-1) p_k(s)x^k,
 beta=(3-s)/2, b=Re beta,

with the same K Chebyshev roots in [1/16,1]. For 0<=Re s<=1 and fixed |Im s|<=T, define

 Q_K(s,w)=sum_(k<K) p_k(s)/(3+2k-w),
 K_K(s,w)=1/(w-s)+Q_K(s,w).

For Re w<3, the finite sum gives exactly

 Q_K(s,w)=(1/2) integral_0^1 x^((1-w)/2)p_(K,s)(x)dx.      (RL1)

The regular Taylor coefficient at w=s is therefore

 c_(K,j)(s):=[(w-s)^j]Q_K(s,w)
   =sum_(k<K) p_k(s)/(3+2k-s)^(j+1)
   =[1/(2^(j+1) j!)] integral_0^1
              x^(beta-1)(-log x)^j p_(K,s)(x)dx.          (RL2)

All integrals converge because b>=1. For every fixed nonnegative integer j,

 c_(K,j)(s)=( (1/2)log K )^(j+1)/(j+1)!
                   +O_(T,j)((1+log K)^j),               (RL3)

uniformly on the stated fixed strip. In particular,

 Q_K(s,s)=(1/2)log K+O_T(1).                             (RL4)

### 13.2. Proof with the complete alias retained

Use the proved coefficient bound d_n=O_T(r^n(n+1)^(b-1)), r=3/5, and write the interpolant as its first K Chebyshev terms plus all root aliases. The following are the localized estimates already proved in Section 12.3 above:

 |p_(K,s)(x)|<=C_T min(K^b,x^(-b)),                       (RL5)

and, for 0<=x<=a/2, a=1/16, the complete alias A_K satisfies

 |A_K(x)|<=C_T K^(b-1)exp(-4Kx).                         (RL6)

On a/2<=x<=1 the alias is exponentially small in K, up to a fixed polynomial. The unaliased infinite Chebyshev series equals x^(-beta) for every 0<x<=1. This follows by analytic continuation from [a,1], since its exterior terms converge whenever rR(x)<1, where R(x)=exp(arccosh((17-32x)/15)); the only excluded real point in [0,1] is x=0.

For 0<x<=a/2 the unretained series tail obeys

 |sum_(n>=K)d_n T_n((32x-17)/15)|
 <=C_T sum_(n>=K)(n+1)^(b-1)exp(-4nx)
 <=C_T x^(-b)exp(-2Kx).                                 (RL7)

The last inequality takes exp(-2Kx) out and bounds the remaining full exponential sum. On a/2<=x<=1 the series tail is exponentially small in K. Thus p-x^(-beta) is the difference of the retained full alias and the full unretained series tail, with both errors accounted for.

For sufficiently large K, split (RL2) at x=1/K. The inner interval, by (RL5), has absolute value at most a constant times

 K^b integral_0^(1/K) x^(b-1)|log x|^j dx
 <=C_j(1+log K)^j.                                     (RL8)

On x>=1/K, replace p by x^(-beta). The error from (RL7), after multiplication by x^(beta-1)(-log x)^j, is bounded by

 C_T integral_(1/K)^(a/2) x^(-1)|log x|^j exp(-2Kx)dx
 <=C_(T,j)(1+log K)^j.                                 (RL9)

Use u=Kx to see the last bound; the exponential pays every fixed power of |log u|. The error from (RL6) is at most C_(T,j)K^(-1)(1+log K)^j, by the same substitution. The remaining interval [a/2,1] is exponentially small and harmless. The finitely many smaller K are absorbed in the constants.

The surviving main integral is exact:

 [1/(2^(j+1)j!)] integral_(1/K)^1 (-log x)^j dx/x
   =((1/2)log K)^(j+1)/(j+1)!.

This proves (RL3), including all aliases. No incomplete-gamma profile or asymptotic spacing of nodes is assumed.

### 13.3. Exact local Perron block at a true simple zero

For nonintegral N, the exact finite/tail Perron identities on 1<c<3 give

 Mtilde_N(s)=Perron integral_(Re w=c)
                 N^(w-s) K_K(s,w)/zeta(w) dw/(2pi i),   (RL10)

for Re s<c. The Perron integral is taken in its usual symmetric limiting sense; it is not claimed absolutely convergent. One can instead work with any finite admissible rectangle and retain its full remainder. The nonintegral N convention avoids half-weight endpoint terms.

Let rho be a fixed simple genuine zero, 0<Re rho<1. The residue of the integrand in (RL10), with s=rho, at w=rho is exactly

 [log N+Q_K(rho,rho)]/zeta'(rho)
                   -zeta''(rho)/(2 zeta'(rho)^2).       (RL11)

Thus its local block is

 log(N sqrt(K))/zeta'(rho)
                   -zeta''(rho)/(2 zeta'(rho)^2)
                   +O_rho(1).                          (RL12)

The coefficient of the full resonant logarithm is one. This is not an asymptotic for the whole Mtilde_N(rho): other residues and the entire remaining contour still occur in (RL10).

### 13.4. Fixed multiple-zero block

More generally let rho have fixed order m, and write

 1/zeta(rho+h)=sum_(j=-m)^infinity a_j h^j,
 L=log N, ell=(1/2)log K.

Equation (RL3) says that the regular Taylor coefficients of K_K(rho,rho+h) through any fixed order agree with those of exp(ell h)/h up to O_rho((1+ell)^j) at coefficient h^j. Taking the local residue gives

 Res_(w=rho) [N^(w-rho)K_K(rho,w)/zeta(w)]
 =sum_(j=0)^m a_(-j)(L+ell)^j/j!
       +O_rho((1+L+ell)^(m-1)).                         (RL13)

Only finitely many coefficients are involved, so (RL13) is a finite Taylor calculation. Constants may depend on the fixed zero and its true multiplicity. It is not uniform in a growing cluster or in multiplicity. When the actual integrand also includes a genuine source numerator B(w), multiply its true w-Taylor jet into this local expression before taking the residue. A numerator independent of w would have a different role; no B/zero cancellation is ignored.

### 13.5. Meaning for the signed program

The original canonical correction creates an additional half-log K delay in the local self-resonance; it does not lower the resonant coefficient. This matches, rather than bypasses, the boundary logarithm in the Mertens transfer estimate. A proposed one-sided gain must still retain the matching future-prime, kappa R and source-derivative blocks, as well as the full same-record remainder. No such joint sign or remainder estimate is proved here.
