# Coherent all-prime ray bridges and the original signed comparison

## Verified results

This package constructs one shared-noise field for the complete original-theta
Gamma-plus-prime forward process. It proves:

1. The operational process includes the genuine origin holding current. The
   same actual source has uniformly finite current variance, including the
   origin. Its common-noise covariance is explicit.
2. All prime-power perturbations of the coupled distance are paid by the
   continuous Gamma drift on the physical tail z,w>=4. The exact rational
   all-integer bound is

       prime distance row/theta_c
         <=5368709120000/14719995925619<3/8.

   Consequently the complete pair-distance drift is at most
   `-(1/8)int_min^max theta_c`. Compact entrance is handled by an actual
   Poisson stopping time. Infinite physical clock and the stopped coalescence
   compensator then prove finite almost-sure coalescence for every fixed pair.
3. Current differences are honest finite pre-coalescence path integrals in
   L2. Weighted pair distances extend this statement to every fixed finite
   theta-jet neutral repair, even when the individual polynomial currents
   diverge. The exact mixed neutral noise and projection cost remain.
4. Every original ordered edge measure and the weak continuous pair adjoint
   are explicit in physical coordinates. The Gamma wall becomes a product
   Cauchy kernel, while reflected primes lie on product curves. Their diffuse
   incoming rows and diagonal absorption are retained.

These are nonlocal all-prime constructions and a genuine quantitative tail
coupling inequality. They do NOT prove positivity of the original signed
source form or K<=1. The final signed variance/covariance comparison below
is still open.

## Conventions and prior proved inputs

Let psi=-Phi' be the original odd theta source, positive on x>0, and write

    z=pi exp(2x),
    c(z)=8z^3-30z^2+15z,
    theta_c(z)=sum_(n>=1)c(n^2z)exp(-n^2z),
    psi(x)=exp(x/2)theta_c(z).

The complete theta_c, not an individual signed summand, is the jump weight.
It is positive for z>pi and vanishes simply at pi. Put
`alpha_n=Lambda(n)/sqrt(n)`, `d_n=log n`,
`kappa(t)=exp(-t/2)/(1-exp(-2t))`, and `s(x)=sinh(x/2)`.

The [actual ratio theorem](../20261014_actual_ratio_multipliers/REPORT.md)
proves, for the actual source g=psi r at each fixed positive depth,

    u=r-c_infinity in H^s(0,infinity), every s<1,
    c_infinity=U(g)/U(psi),
    U(f)=int_0^infinity exp(x/2)f(x)dx.

Thus u is bounded, tends to zero, and is exactly the lawful U=0 constant-null
representative. The [forward-ray theorem](../20261014_positive_reflected_storage/FORWARD_RAYS.md)
proves its finite full-prime current and the interior occupation estimates.
The [complete current form](../20261014_positive_reflected_storage/CURRENT_FORM.md)
proves the original adjoint pairing and all polar/reflected normalizations.
These existing complete proofs are dependencies, not replaced by a bare
positivity assertion for a Markov semigroup.

No normalized finite-time filter, strong original-P tangent, or special
choice of neutral repair coefficients is needed to prove this package's
bridge extension. Any fixed finite combination of the known theta jets is
allowed, and its full original cost remains.

## Reading order and complete proofs

- [Coherent operational currents](COHERENT_OPERATIONAL_RAY_CURRENTS.md):
  entrance law, shared full Poisson construction, uniform current variance,
  exact common bracket, and full original covariance identity.
- [Full-prime contraction and coalescence](FULL_PRIME_TAIL_CONTRACTION_AND_COALESCENCE.md):
  complete drift certificate, lawful compact entrance, compensator proof of
  actual meeting, and finite current-square formula.
- [Polynomial neutral bridges](POLYNOMIAL_NEUTRAL_CURRENT_BRIDGES.md):
  fixed-degree weighted drift and bracket estimates, terminal L2 passage,
  finite neutral repair, and all-finite signed variance formula.
- [Physical pair kernel and adjoint](PHYSICAL_PAIR_KERNEL_AND_ADJOINT.md):
  all five original ordered edge measures, common-cutoff pair adjoint,
  product-Cauchy reduction, and reflected-prime diffuse incoming rows.

## Exact full-form comparison retained

For the bounded actual ratio, let J(x)=Var(I_x) and
C(x,y)=Cov(I_x,I_y) for the SAME coherent current field. Let P_coh,H_coh,N_coh
integrate E|I_x-I_y|^2 against the original pole, Gamma-wall, and reflected
prime edge measures. Put K0=3Phi+Theta/2 and L=F_r psi. Then exactly

    Q_delta[g]
      =P_coh-H_coh-(1-delta)N_coh
       +2int psi[2K0-2x psi-delta L]J
       +8C_P-2C_H-2(1-delta)C_N.                       (1)

The three covariance edge integrals are defined in the coherent-current
proof; the coefficients in (1) retain every full pole term. For the actual
top source Q_delta[g]=0. Positive semidefiniteness of C implies C_P,C_H>=0
but does not sign C_N or their complete combination.

The [published actual-depth storage theorem](../20261014_positive_reflected_storage/ACTUAL_DEPTH_STORAGE.md)
proves a positive lower bound for the entire storage functional in (1),
for 0<=delta<=1/2. That nonlocal bound is compatible with (1), but its added
J row is exactly matched by the edge-variance debit. It is not a second
independent budget that can be spent again.

For a finite polynomial neutral repair v, individual J and C need not exist.
Use only the L2 pair bridge B_v. If P_B,H_B,N_B integrate E|B_v|^2, and
V_P,V_H,V_N integrate Var(B_v), the all-finite identity is

    Q_delta[psi v]
      =P_B-H_B-(1-delta)N_B+2int psi^2 Gamma_psi[v]
                              +V_H+(1-delta)V_N-V_P.  (2)

The finite common-neutral Schur cost is still subtracted from (2). The
corrected source equation retains its full neutral forcing; it is not
replaced by an unforced top-kernel equation. Equations (1)-(2), not tail
Wasserstein contraction alone, are the remaining signed comparison target.

## Exact reproducible check

Run in this directory:

    python check_full_prime_tail_contraction.py

The checker uses only Python's standard library and exact fractions. It
checks both source-polynomial identities, the rational Taylor lower bound,
and the complete geometric majorant. No external prime table, numerical
prime truncation, installation log, or floating-point sign test is needed.
