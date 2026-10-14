# Hidden Gamma energy controls a shifted tail in the original source metric

## Results

The certified safe-ray Gamma/divisor comparison retains more than its scalar
mass gap. Using exactly the same cap h and exactly the same head-weighted
constant c, it gives

    E_hidden[a] >= E_h[a]/2 + 8*10^(-6) M[a],
    M[a]=integral_(log2)^infinity W(x)xi(x)|a(x)-c|^2 dx.

Here E_h contains ALL transformed Gamma edges, including head/tail mixed
edges. This is one joint budget, not two independently spendable estimates.
The exact rational argument is in [RETAINED_GAMMA.md](RETAINED_GAMMA.md).

For every fixed B>log2, the complete future lift

    f_B=1_(x>B) C[xi(a-c)]

is a genuine original-P source and satisfies

    q_b[(f_B)_odd]+integral V|f_B|^2 <= C_B E_hidden[a],
    P[f_B/psi]+N[f_B/psi]+|Q_delta[f_B]| <= C'_B E_hidden[a],
                                                     0<=delta<=1.

[SHIFTED_TAIL.md](SHIFTED_TAIL.md) proves this in the original metric,
including the complete primes, reflected potential and pole. A moving
logarithmic Hardy window pays the sharp source cutoff without assuming a
trace. The true all-integer lift is summed with Gaussian bounds; the
complete original inverse-theta potential is paid as well. The constants
are finite and specified by weight suprema and convergent series, but no
numerical values for C_B or C'_B are certified here. They need not stay
bounded as B decreases to log2.

The full mixed tail-to-head map at the same shifted cut is bounded using
M alone. For an ACTUAL positive-depth top source g, its exact head Schur
equation therefore gives

    P[g/psi] <= C_(delta,B) M[a] <= C'_(delta,B) E_hidden[a],
    a=(Mg)/xi on the safe ray.

[MIXED_OBSERVABILITY.md](MIXED_OBSERVABILITY.md) retains every original
mixed Gamma, prime, reflected-prime and pole term. The constant uses the
strictly positive but non-effective actual head gap. This is actual-source
observability, not an unconditional coercivity assertion for all sources.

## Exact prerequisites for the actual head step

The proof of the actual head inverse is supplied, rather than assumed:

- [COMPACT_DEVIATION.md](COMPACT_DEVIATION.md) compares the COMPLETE prime
  Laplace transform with the separated Gamma row. Residues at the trivial
  zeta zeros leave delta times each compact-source moment, excluding an
  eventually constant nonzero actual ratio. The unchanged c psi forcing
  has poles only at 0 and 1. The compact-L2 version is stated explicitly.
- [ACTUAL_HEAD.md](ACTUAL_HEAD.md) gives original-P closure, compact
  resolvent and the actual head gap. A head-null vector is promoted to a
  full Q_delta-null source by global form positivity, then excluded by the
  compact-deviation theorem. At any finite enlarged cut, only finitely
  many internal correlations are added while the complete V is retained.

The underlying definitions and already established bounds are linked to:

1. [The complete safe-xi hidden comparison](../20261014_safe_xi_hidden_comparison/REPORT.md),
   its [cap](../20261014_safe_xi_hidden_comparison/CAPPED_COMPLETION.md),
   [divisor residual](../20261014_safe_xi_hidden_comparison/DIVISOR_STAR.md)
   and [complete integer-row bulk estimates](../20261014_safe_xi_hidden_comparison/BULK_TAIL.md).
2. [The actual source equation and bounded complete normalized prime operators](../20261013_supercritical_source_tails/REPORT.md).
3. [The original P/N gradient completions](../20261013_reflected_prime_energy/REPORT.md).
4. [Actual origin transmission](../20261014_actual_origin_transmission/REPORT.md)
   and [the bounded ratio/plateau theorem](../20261014_actual_ratio_multipliers/REPORT.md).

No new numerical certificate is used in this package. Existing rational
and interval certificates remain in the linked hidden-comparison package.

## Scope

The same constant c is used throughout each hidden budget and source lift.
It is not silently changed to the origin anchor or plateau gauge; changed
pole moments are retained. The endpoint cut B=log2 is NOT included in the
shifted embedding. The actual observability statement requires delta>0
and genuine global Q_delta positivity and stationarity.

These results pay an original-domain and boundary-norm obstruction. They
do not sign the remaining dynamic transport/reflection/pole remainder,
exclude a positive-depth source, or prove RH. In particular they preserve
the neutral-jet counterexample to universal remainder positivity.
