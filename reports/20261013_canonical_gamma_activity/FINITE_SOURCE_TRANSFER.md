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
