# Same-normalization prefix extension of the absolute cubic majorant

16 October 2026. This extends [the comparable-height lemma](DYADIC_ABSOLUTE_CUBIC_TAIL.md)
only in the real height variable. It is not a fourth-moment or spectral-tail theorem.

Fix a BV window of width lambda<theta<4/7. Choose an integer p>1 and a real
kappa<1, once and for all, so

    theta' = theta(1-1/p) > lambda,
    lambda/theta' < kappa < 1.

For L=log T, use real bins of length delta=2 pi/L, with all zeros of both
ordinate signs and |gamma|<=U, where U>=T^kappa. Define R=log U/L.
All multiplicities are retained. The normalized imaginary coordinate is
(beta-1/2)L/(2 pi), regardless of U.

## Uniform arithmetic inputs

For every fixed integer q,

    sum_i c_i^q <<_q U L (1+R)^q.                              (P1)

To prove this, choose a fixed even Tsang increment moment at least q and use
h=2 delta. On each dyadic real-height interval [V,2V], Theorem 2 of
[arXiv:2010.10675v1](https://arxiv.org/abs/2010.10675v1) applies with H=V and 0<h<1. Its moment bound and the
Riemann--von Mangoldt main increment give

    integral_[V,2V] |N(t+h)-N(t)|^q dt
      <<_q V (1+h log V)^q.

The preceding-bin injection contributes the factor delta^(-1). Sum dyadically
up to U; log V<=log U and sum V<=2U. The finitely many zeros below the fixed
threshold for the chosen moment contribute O_q(1), uniformly in bin width,
since their total multiplicity is fixed. Reflection handles negative ordinates.
The constants may depend on q, but q is chosen before T tends to infinity.

For d_i^(j) counting j<=|a|<j+1, the uniform near-line density theorem gives

    n_j(U):=sum_i d_i^(j)
       <<_theta U log U exp(-4 pi theta j R).                  (P2)

The critical-line convention at a boundary is handled by a left limit in
sigma if the source defines N(sigma,U) with a strict inequality. The density
constant is uniform in sigma. Its threshold depends on fixed theta, not j.
For j=0 use total zero counting, and beyond the strip the count is zero.

## Uniform prefix majorant

Use the discrete anchored-cycle inequality (4) of the dyadic note with
q=2p+1. The arithmetic factor is at most

    n_j(U)^(1-1/p) [sum_i c_i^(2p+1)]^(1/p)
      << U L R^(1-1/p)(1+R)^(2+1/p)
             exp(-4 pi theta' j R)
      <= U L (1+R)^3 exp(-4 pi theta' j R).                    (P3)

The Fourier cubic growth is at most C(1+j)^3 exp(4 pi lambda(j+1)). Since
R>=kappa, the remaining exponent is bounded above by
-4 pi(theta' kappa-lambda)j, with a fixed positive gap. Therefore

    sum_{|gamma_i|,|gamma_j|,|gamma_k|<=U}
       |K(z_j-z_i)K(z_k-z_j)K(z_i-z_k)|
      << U L (1+log U/L)^3,                                   (P4)

uniformly U>=T^kappa. In particular the entire prefix U=T^kappa contributes
o(T log T). This statement already includes its low-height labels; no
separate low-height estimate with an incorrectly changed logarithm is used.

## Two elementary smoothing consequences

For each fixed rapidly decreasing bounded real-height weight h, the absolute
weighted cubic sum is O_h(T log T). On the prefix |gamma|<=T, use (P4).
For max|gamma| in [2^m T,2^(m+1)T], at least one factor has rapid decay in
2^m, while (P4) grows only as 2^m T L(1+(m+1)/L)^3. The shell series is
summable. The same argument gives uniformly small far-height tails for a
family with uniform Schwartz seminorm bounds there.

If h is entire and Schwartz uniformly on a fixed horizontal strip, then

    |h((gamma-i(beta-1/2))/T)-h(gamma/T)|
      <= C_(h,M) T^(-1)(1+|gamma|/T)^(-M),

because |beta-1/2|<=1/2. Telescope the product of three height weights and
apply the preceding absolute weighted bound. The analytic-height versus
real-height cubic sums differ by O_h(log T), hence o(T log T).

The complete real sharp-boundary passage still requires specifying the
approximating family and the order of limits. On any fixed prefix |gamma|<=CT,
the count-small deletion argument from the dyadic note applies verbatim,
using (P1)--(P2). These estimates supply the needed analytic majorants but do
not themselves state a Rudnick--Sarnak trace formula or its constant.
