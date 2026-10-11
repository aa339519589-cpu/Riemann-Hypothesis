## Round 113 — the new Suzuki numerical realization proves only the easy implication

I audited Kim--Hong--Kim--Choi's numerical realization of Suzuki's
Weil-quadratic-form operator ([arXiv:2607.24830](https://arxiv.org/html/2607.24830)).
It is useful as a consistency check, but its own scope statement rules out an
unconditional RH proof.

The paper studies a finite-element approximation of a finite-interval Weil
quadratic form and numerically observes that a residual associated with a zero
on the critical line remains bounded, whereas an artificially injected
off-line term grows like \(e^{2a\delta}\).  The calculation is the expected
identity
\[
 \rho-s=i(\gamma-\xi),\qquad
 |X^{\rho-s}|=1
\]
when \(\rho=\tfrac12+i\gamma\).  It does not establish that the actual zeta
residual is bounded without first assuming this critical-line form of every
zero.

The logical split is exact:

1. **RH \(\Rightarrow\) bounded residual:** under RH, the displayed exponential
   factors have modulus one, and the paper derives the bounded/equidistributed
   behavior (with additional numerical truncation).
2. **Bounded residual \(\Rightarrow\) RH:** this would require proving the
   boundedness for the actual, unmodified zeta data.  The paper does not prove
   that implication; it explicitly says that the proof assumes RH in its first
   line and that removing that assumption collapses the subsequent argument.

The same manuscript records an independent numerical limitation.  Its lowest
finite-element eigenvalues that appear positive at larger interval sizes scale
like discretization error under refinement and are therefore not certificates
of global Weil positivity.  A positive finite-element Rayleigh quotient is an
upper bound for the true infimum; it cannot exclude a limiting zero or negative
value.  The paper consequently labels the operator realization experimental
and states that it does not prove or advance RH.

**Established:** the finite-element experiment reproduces the easy,
RH-conditioned residual behavior and provides a hostile control against
misreading discretization artifacts as positivity.

**Failure / missing step:** no unconditional boundedness theorem for the
actual zeta residual, no uniform \(a\to\infty\) spectral limit identifying all
zeros, and no global positive-semidefinite theorem.  The construction does not
address the Bombieri inequality (103.6).

**Route decision:** use this only as an audit of the finite-interval/operator
route; retain the direct weighted range/nonmembership problem as the active
load-bearing route.

**RH status:** no unconditional proof has been produced.
