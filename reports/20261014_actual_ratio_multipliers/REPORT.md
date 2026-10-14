# Actual Sobolev ratio plateau and unsmoothed original-domain Fourier variations

This report proves that an actual scalar supercritical Green source has a canonical ratio representative in every H^s, s<1, at fixed positive spectral depth. Consequently every bounded even Fourier multiplier yields a legal variation in the **original** P-completion after multiplication by the original theta source. In particular the exact two-prime Euler allpass difference requires no Gaussian regularizer. This does not assign a sign to its full commutator and does not prove an eigenvalue exclusion.

## Verified inputs and conventions

Use the complete P,N ratio forms and actual scalar source from the [source-tail realization](../20261013_supercritical_source_tails/REPORT.md). The [fixed-depth bootstrap](../20261013_supercritical_source_tails/BOOTSTRAP_AND_FIXED_TRANSLATIONS.md) supplies g_o,v_o in every H^s, s<1. The [actual origin transmission theorem](../20261014_actual_origin_transmission/REPORT.md) supplies the genuine linear origin expansion and complete sample identity. The [complete reflected row theorem](../20261013_reflected_markov_essential_edges/REPORT.md) supplies L(x) asymptotic to J exp(x/2), with J>0. The [complete signed endpoint pairing](../20261013_supercritical_source_tails/ENDPOINT_PRIME_PAIRING.md) supplies the pole-subtracted log-prime convolution and the unchanged source equation. Its classical near-one zero-free input is retained, not strengthened toward the critical line. The full pole coefficient is that in the [original odd source form](../20261012_localized_odd_schur/SOURCE_FORM.md).

All prime powers have their original Mangoldt coefficients. An even ratio h on the full line corresponds to the odd source psi_o h; its restriction to x>0 has original ratio P-energy P[h]. Fourier multipliers in the theorem act on the RATIO, not on the bare source g. Noncentered output sources retain the full coefficient-two pole term.

## 1. Sobolev and pointwise plateau

Retain the actual pole-centered scalar source g=psi r, depth delta>0, and P0=P[r]. Pole centering is int_0^infinity sinh(x/2)g(x)dx=0. Set

    p=psi'(0), L(x)=sum_(d_n>x) alpha_n psi(d_n-x),
    J=int_0^infinity exp(y/2)psi(y)dy,
    c_infinity=J^(-1)int_0^infinity exp(y/2)g(y)dy,
    ell(x)=exp(-x/2)L(x), d_n=log n,
    alpha_n=Lambda(n)/sqrt(n).

Then, for every s<1,

    r-c_infinity in H^s(0,infinity),
    ||r-c_infinity||_(H^s)<=C_(delta,s)sqrt(P0).        (1)

In particular its continuous representative satisfies

    lim_(x->infinity) r(x)=c_infinity.                (2)

These statements are at fixed positive depth; no uniform delta->0 bound is asserted.

### Proof of the Sobolev upgrade

Use the verified scalar bootstrap and weighted-cell interpolation to obtain g_o in H^q with every fixed exponential spatial weight for all q<1. The pole-subtracted complete log-prime convolution T has multiplier

    m(xi)=-zeta'/zeta(1-i xi)-1/(-i xi),
    |m(xi)|<=C log^2(2+|xi|),

with the removable value at zero. Consequently T:H^q(R)->H^s(R) is bounded whenever s<q<1. This is the same classical near-one zero-free input as the earlier endpoint theorem, not a new critical-strip zero-free assumption.

The half-source

    f_g(u)=1_(u<0)exp(-u/2)g(-u)

belongs to H^q for every q<1. For q<1/2 this follows from the endpoint cutoff argument. For 1/2<=q<1, the same-side Gagliardo seminorm is bounded by the weighted full-source norm. Its cross-side term is a constant times

    int_0^infinity u^(-2q)exp(u)|g(u)|^2du.

The actual origin expansion g(u)=O_delta(sqrt(P0)u) makes this finite at zero; the theta tail pays infinity. The identical statement holds for the fixed psi half-source. Thus the exact full-prime remainder identities give

    R_g(x)=exp(-x/2)F_r(x)-J c_infinity=(T f_g)(x),
    R_psi(x)=ell(x)-J=(T f_psi)(x),

on the positive half-line, and R_g,R_psi belong to H^s there for every s<1. No new point-sampling identity is needed to define these multipliers.

For x>0 define the unchanged complete half-line loads

    F_r(x)=sum_(d_n>x) alpha_n g(d_n-x),
    F_b(x)=sum_(d_n<x) alpha_n g(x-d_n),
    F_+(x)=sum_n alpha_n g(x+d_n).

Let B_o g be the positive-wing restriction of b(D)g_o, where b is the original nonnegative logarithmic Gamma multiplier, and let C0=gamma+pi/2+3log2+log pi. Write W=Lr-F_r. The unchanged full signed source equation is

    delta W=C0g+F_++F_b-F_r-B_o g.                   (3)

Each term on the right, after multiplication by exp(-x/2) and restriction to x>0, belongs to H^s for every s<1:

- The mass term follows from weighted source regularity.
- The complete future sum F_+=sum alpha_n g(x+d_n) converges absolutely in these H^s norms by the exponential weighted source bounds, with any summable fixed power n^(-B).
- For F_b-F_r use f(x)=exp(-x/2)g_o(x). The exact complete endpoint pairing is T f plus the continuous primitive of f. Pole centering gives int_R f=0. The primitive therefore has exponential tails and belongs to H^s, while T f is in H^s by choosing the input order q>s.
- The full odd Gamma term B_o g is the restriction of b(D)g_o, with b(xi)=O(log(2+|xi|)). It belongs to H^s from any q>s. Multiplication by the bounded Lipschitz weight on the positive half-line preserves H^s.

These are assertions on the positive half-line. There is no illicit zero-extension of an individual term with nonzero origin trace. It follows that w=exp(-x/2)W belongs to H^s(0,infinity), with norm C_(delta,s)sqrt(P0).

The complete row satisfies inf ell>0, sup ell<infinity, and ell is globally Lipschitz. For the last statement, the complete Chebyshev unit-shell bound gives |L'(x)|<=C exp(x/2) almost everywhere; L itself is continuous at each threshold. Thus 1/ell is bounded Lipschitz. The defining identities W=Lr-F_r and the displayed remainder formulas give exactly

    ell(x)[r(x)-c_infinity]=w(x)+R_g(x)-c_infinity R_psi(x). (4)

Multiplication by 1/ell preserves H^s for s<1, proving (1).

Choose any s>1/2. Even extension to R is bounded in H^s for s<1, so r-c_infinity is uniformly Holder-alpha for any alpha<s-1/2. A uniformly continuous L2 function on the half-line tends to zero at infinity: otherwise fixed-size disjoint intervals with a fixed positive lower bound would contradict square integrability. This proves (2). The continuous representative agrees with the original actual local representative and all previously defined prime traces.


## 2. Unsmoothed original-domain ratio filters

The strengthened plateau removes the need for an artificial Gaussian in long-range ratio variations. For every fixed 0<s<1, multiplication by the original odd theta source has the bound

    P[h] = P[(psi h)/psi] <= K_s ||h_even||_(H^s(R))^2. (5)

Here h is an even ratio, and the notation P[h] is the original ratio form, not the physical source norm. To prove (5), first take smooth compact even h. The complete reflected form satisfies

    N[h]<=4 int_0^infinity psi(x)L(x)|h(x)|^2 dx
         <=4||psi L||_infinity ||h||_2^2.

In P=N+h_source, the full Gamma multiplier is bounded above by C_s(1+|xi|^2)^s. Multiplication by the smooth bounded Lipschitz psi_o is bounded on H^s. The full weighted prime source operator is bounded on L2 of the ratio: the n-th shift has norm at most

    alpha_n sup_(x in R)|psi_o(x)psi_o(x+d_n)|,

and the sum of these norms is finite by the genuine theta tails (the two wings give exponential decay in n). The negative scalar mass and coefficient-two pole square may be omitted for this upper bound only; they remain in every exact identity. This proves (5) on the core. Even compact smooth approximation in H^s proves the original P-domain assertion and bound for general h. The pole functional is continuous as well because psi(x)sinh(x/2) is in L2.

Let h=r-c_infinity be the actual even ratio from (1). Every bounded real even Fourier multiplier C acts boundedly on H^s. Consequently

    u=psi C h,    w=psi C^2 h                            (6)

are in the original P-completion, with P-energies bounded by K_s ||C||^2||h||_(H^s)^2 and K_s ||C||^4||h||_(H^s)^2, respectively. They need not be pole-centered. They may be centered by subtracting their constant-ratio psi component, or used directly with the unchanged coefficient-two pole term.

In particular, let A_p be the real part of the finite-Euler unitary allpass multiplier, with the exact expansion

    A_p=-a_p I+(1-a_p^2)sum_(k>=1)a_p^(k-1)T_(k log p),
    a_p=p^(-1/2),  ||A_p||<=1, A_p1=1.

Then C=A_2-A_3 and C^2 in (6) are legal WITHOUT Gaussian smoothing. C1=0 makes the output independent of the chosen constant-ratio gauge. Every mixed sum/difference prime-power label remains in C^2. This does not make their complete signed commutator nonnegative or negative, but it removes an otherwise extraneous regularizer and its associated limiting question.

More generally, any finite signed even translation measure acts on this same actual H^s ratio at arbitrary propagation radius. Its original P cost is bounded by (5) times the square of the measure's total variation, not by the largest translation label. This is a weighted RATIO variation psi C h; it is not a claim that the corresponding bare translated source Cg belongs to the original P-domain.

For a concrete complete arithmetic example, define q_n=alpha_n psi(d_n)/L(0) and Q0=sum_n q_n T_(d_n). Then Q0 is a symmetric Markov convolution and C_boundary=I-Q0 annihilates constants. The actual origin transmission gives (C_boundary h)(0)=0. Thus the unsmoothed source psi C_boundary h is legal and has origin order O(x^(1+alpha)), alpha<1/2. Its complete prime-load trace is nevertheless -L(0)[(I-Q0)^2 h](0), not automatically zero. The full Gamma, reflected-prime and polar terms must remain in a proposed signed test.

## 3. A concise warning about summing squared prime-knot coefficients

Let r0=r(0), f=g-r0 psi and A_n=alpha_n p/psi(d_n). Pointwise cancellation gives

    A_n^2 |f(d_n)|^2=p^2 alpha_n^2 |r(d_n)-r0|^2.

The pointwise plateau and the unconditional PNT imply

    sum_(d_n<=R) A_n^2 |f(d_n)|^2
       =(p^2/2)|c_infinity-r0|^2 R^2+o(R^2).          (7)

Indeed sum_(n<=X)Lambda(n)^2/n is asymptotic to (log X)^2/2: higher prime powers have finite total mass, and partial summation of the prime PNT handles primes. The nonnegative weighted Cesaro principle then gives (7). If c_infinity differs from r0, the squared-knot sum diverges. If they are equal, (7) gives only o(R^2), not summability. Thus no termwise infinite sum of local cusp coefficients is justified by the source's theta tail alone. This warning does not enter the ratio-multiplier domain proof.

## 4. Scope of the signed conclusion

The theorem supplies honest original-domain variations for the same actual source, including exact unsmoothed arithmetic filters. It does not transfer positivity to a new gauge or metric, make bare source translations legal at arbitrary range, or replace the full signed commutator by a Markov contraction. A complete comparison still has to retain Gamma, both prime directions, the coefficient-two output pole term, and any common-neutral projection cost.
