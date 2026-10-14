# A global tempered Fourier constraint for negative original-Schur states

This is an actual negative-eigenvector consequence of the complete source
equation. It strengthens the local reciprocal-Gaussian identity to a full
tempered-distribution Fourier identity. It does **not** assert ordinary
physical L2, remove the elementary pole mode, or establish an original
quadratic-form sign.

Use the closed true-seed operator and neutral space in
[CLOSED_ORIGINAL_SCHUR_IN_TRUE_SEED_MASS.md](../20261014_original_seed_schur/CLOSED_OPERATOR.md),
and the independently verified complete prefix equation in
[NEGATIVE_SCHUR_EIGENVECTOR_COMPLETE_PREFIX_DENSITY.md](PREFIX_DENSITY.md).
Let

    S a=-lambda a, lambda>0,
    f=E0[1_(x>b)C(xi a)], b=log2,
    Qf be the FULL original source distribution.

Thus Qf contains the Gamma multiplier, both prime orientations, and the
whole pole. It vanishes on the head, and its tail satisfies

    C_b^*(Qf)=-lambda W a,
    C_b^*H(x)=sum_(n<=exp(x-b))n^(-1/2)H(x-log n).     (1)

The source graph and complete future estimates give

    ||f||_G^2:=integral_0^infinity exp(2x)|f(x)|^2dx<infinity. (2)

The compact head/collar in (2) uses ordinary source L2; only the far wing
uses the mass estimate. No unproved original P norm is used.

## 1. The complete source distribution has a global exponential weight

For every

    1/2<sigma<1,  0<epsilon<1/2,

one has

    exp(-sigma x)1_(x>b)Qf in H^(-epsilon)(R),
    ||exp(-sigma x)1_(x>b)Qf||_H^(-epsilon)
                                  <=C_(sigma,epsilon)||f||_G. (3)

All prime powers are retained in this assertion. Here is a direct proof.
Write alpha_n=Lambda(n)/sqrt(n) and put

    Z_sigma=sum_(n>=2)Lambda(n)n^(-sigma-1/2)<infinity,
    A_pr=sum_(n>=2)Lambda(n)n^(-3/2)<infinity.

The three positive-wing arithmetic rows have the following genuine
weighted L2 bounds, by Minkowski and a change of variable:

    ||exp(-sigma x) sum_n alpha_n f(x+log n)||_2
                                             <=A_pr ||f||_G,
    ||exp(-sigma x) sum_(log n<x)alpha_n f(x-log n)||_2
                                             <=Z_sigma ||f||_G,
    ||exp(-sigma x) sum_(log n>x)alpha_n f(log n-x)||_2
                                             <=Z_sigma ||f||_G. (4)

For the first row the n-th shifted L2 norm is at most n^(-1)||f||_G.
For the second it is n^(-sigma)||exp(-sigma x)f||_2.
For the third it is at most n^(-sigma)||exp(sigma x)f||_2;
the restriction sigma<1 pays this last norm by (2).
Thus every complete series in (4) converges in the displayed norm.

The pole coefficient ell(f)=integral sinh(x/2)f(x)dx is finite by (2),
and exp(-sigma x)sinh(x/2) belongs to L2(0,infinity) because sigma>1/2.
The full Gamma multiplier has logarithmic growth, so its action on the
odd L2 source f_o belongs to H^(-epsilon)(R). Multiplication by a smooth
bounded extension of exp(-sigma x) from x>=b is bounded on this Sobolev
space. The sharp restriction to x>b is also bounded when |epsilon|<1/2.
These facts, together with (4), prove (3). They do not replace the Gamma
operator by an ordinary L2 function or remove any of its local singularity.

## 2. The WHOLE causal prefix is bounded in the same weighted topology

Extend 1_(x>b)Qf by zero to the left. Its weighted causal prefix is the
absolutely convergent Sobolev-space series

    exp(-sigma x)C_b^*(Qf)(x)
       =sum_(n>=1)n^(-sigma-1/2)
          [exp(-sigma .)1_(.>b)Qf](x-log n).          (5)

Indeed translations are isometries on H^(-epsilon), and

    sum_(n>=1)n^(-sigma-1/2)=zeta(sigma+1/2)<infinity.

On compact intervals the series is locally finite as a distribution,
so it agrees with the exact prefix in (1). Consequently

    h_sigma(x):=exp(-sigma x)1_(x>b)W(x)a(x)
                                      belongs to H^(-epsilon)(R),
    ||h_sigma||_H^(-epsilon)
       <=lambda^(-1)zeta(sigma+1/2)C_(sigma,epsilon)||f||_G. (6)

This is a global bound on the COMPLETE prefix, but in a negative Sobolev
space with a strictly decaying weight. It is not the unweighted L2 bound
needed for the stronger physical-L2 conclusion.

## 3. The physical representative is a tempered distribution

For u>2 put

    G(u)=W(log u)a(log u)/sqrt(u),

and set G(u)=0 for 0<u<2. The already proved local prefix density makes
G a locally square-integrable function, including the endpoint u=2.
Let G_ev denote its even extension to the whole physical line.

For a Schwartz test phi on the positive physical line, the exact change
of variable u=exp(x) reads, first for compactly supported tests,

    <G,phi>=<h_sigma, exp[(sigma+1/2)x]phi(exp(x))>.    (7)

The function on the right belongs to H^epsilon(R), after an optional
smooth left cutoff below b. Its norm is bounded by finitely many Schwartz
seminorms of phi: at positive infinity the rapid decay of phi dominates
every exponential in x, while at negative infinity the factor
exp[(sigma+1/2)x] decays. The same statement holds for its first derivative,
which already suffices since epsilon<1.

Therefore (7) extends continuously to Schwartz tests. Applying it to
phi(u)+phi(-u) proves

    G_ev belongs to S'(R), is even, and vanishes on (-2,2). (8)

The extension agrees with the original function on compact tests. We do
not claim that every Schwartz pairing is an absolutely convergent integral
of |G phi|; (7) specifies the correct tempered extension.

## 4. Exact full Fourier parity, with the elementary pole defect retained

A negative eigenvector is mass-orthogonal to the entire neutral kernel
space K. The reciprocal-complement theorem
[NEUTRAL_COMPLEMENT_RECIPROCAL_GAUSSIAN_IDENTITY.md](RECIPROCAL_IDENTITY.md)
therefore applies. Initially, for Re rho>1/2, define the absolutely
convergent integral

    F(rho)=integral_2^infinity G(u)exp(-pi rho u^2)du,
    H_B(t)=exp(t/2)F(exp(2t)), c=4H_B'(0).

It gives, where both original integrals converge,

    F(rho)-rho^(-1/2)F(1/rho)
                             =(c/2)(1-rho^(-1/2)).   (9)

By (8), there is now a genuine holomorphic extension to Re rho>0:

    F(rho)=(1/2)<G_ev,exp(-pi rho u^2)>.              (10)

Holomorphy follows in the Schwartz topology of the Gaussian test family.
On Re rho>1/2 this is the original integral, so uniqueness continues (9)
to the whole right half-plane, with its holomorphic principal square root.
Unlike the general mass-complement case, this continuation is supplied by
an actual tempered representative, not only a formal reciprocal formula.

Use the unitary full-line Fourier transform with kernel exp(-2pi iuv).
Its Gaussian formula and (9) imply, for every real rho>0,

    <G_ev-Fourier(G_ev),exp(-pi rho u^2)>
                                    =c(1-rho^(-1/2)).

These Gaussian pairings determine an even tempered distribution uniquely.
For completeness, derivatives in rho show that a distribution annihilating
them also annihilates all even monomials times a fixed Gaussian. Oddness of
the tests is harmless because the distribution is even. All derivatives
at zero of its convolution with a Gaussian therefore vanish. That
convolution is an entire function (by the usual Schwartz-seminorm bounds
for the complex translated Gaussian), hence is identically zero. Fourier
transformation and the everywhere nonzero Gaussian multiplier then show
that the original distribution is zero.

Thus the exact conclusion is

    G_ev-Fourier(G_ev)=c(delta_0-1) in S'(R).          (11)

Equivalently G_ev+c is Fourier-selfdual, with value c on the physical
gap (-2,2), in the distributional sense. The constant c is not forced
to vanish. The audited pole-mode witness has c=-1 and satisfies exactly
this normalization. Subtracting a fixed gap pole carrier leaves a
selfdual tempered gap distribution, not automatically an L2 Sonine vector.

Equation (11) is specific to a negative original-Schur eigenstate through
the global prefix estimate (6). The missing unweighted physical range
remains integral W(x)^2|a(x)|^2dx<infinity. No sign of S, no vanishing of
its negative spectrum, and no identification K=ker S is inferred.
