# Negative original-Schur states have an exact tempered Fourier constraint

## Main theorem

Let S be the [closed true-seed original Schur operator](../20261014_original_seed_schur/CLOSED_OPERATOR.md),
including the complete Gamma, prime-power, reflected-prime, and pole terms.
For a negative eigenvector S a=-lambda a, lambda>0, put

    f=E0[1_(x>log2)C(xi a)],
    G(u)=W(log u)a(log u)/sqrt(u), u>2,
    G(u)=0 for 0<u<2,

and extend G evenly to the whole physical line. Then G_ev is a tempered
distribution. With the unitary Fourier kernel exp(-2pi iuv), it satisfies

    G_ev-Fourier(G_ev)=c(delta_0-1).

The coefficient c is exactly the retained reciprocal-Gaussian defect,
not a term assumed to vanish. Equivalently G_ev+c is Fourier-selfdual.
The theorem does not prove G in ordinary L2, c=0, or positivity of S.

The proof uses the actual complete eigenvalue equation. For every
1/2<sigma<1 and 0<epsilon<1/2, its entire causal arithmetic prefix gives

    exp(-sigma x)W(x)a(x) in H^(-epsilon)(R).

The prefix is controlled by the convergent series zeta(sigma+1/2),
not by inversion of zeta across a critical-line zero. This global bound
makes the physical Gaussian pairing a genuine tempered pairing on
Re rho>0. The local neutral-complement identity then extends and yields
the full Fourier relation above.

## Proofs and exact scopes

- [TEMPERED_FOURIER.md](TEMPERED_FOURIER.md) proves the main theorem, including
  every weighted arithmetic row, the complete prefix, physical pushforward,
  and uniqueness of even tempered distributions from Gaussian pairings.
- [PREFIX_DENSITY.md](PREFIX_DENSITY.md) proves the finite causal inverse,
  local density across the safe cut, and local operator-logarithmic
  regularity without losing a possible point-supported distribution.
- [RECIPROCAL_IDENTITY.md](RECIPROCAL_IDENTITY.md) gives the exact Gaussian
  identity for the full neutral mass complement. Its ordinary-L2 Sonine
  conclusion remains conditional on that extra norm.
- [POLE_WITNESS.md](POLE_WITNESS.md) constructs a genuine source-form
  complement vector with c=-1 and G(u) tending to1. It is not claimed
  to satisfy the negative-eigenvalue equation.
- [SAFE_SOURCE_ISOMORPHISM.md](SAFE_SOURCE_ISOMORPHISM.md) proves that the
  honest complete future C and Möbius M are inverse bounded operators on
  Y=L2((W/xi)dx), each within10^(-6) of identity. It supplies a compact
  smooth seed form core and retains the full generalized weight
  M_b^*(W/xi)M in the source eigen-equation. This is an additional domain
  tool, not a physical-L2 or sign assertion.

The [original source head inverse](../20261014_unrepaired_original_head/REPORT.md)
and [closed source-only realization](../20261014_original_seed_schur/REPORT.md)
are unchanged. The [compact negative-part theorem](../20261014_original_schur_compact_negative/REPORT.md)
does not imply that the negative part vanishes. The present theorem adds
an actual global Fourier constraint to each possible negative eigenstate;
it does not replace the unresolved full original-form sign.
