# Independent mathematical review

Date: 2026-10-16.

Reviewed report: [Prescribed moments obstruct a stationary completion in
the critical square measure](REPORT.md).

Reviewed SHA256:

    9fa461e723472e42d02131e7cc7da8ec24122241128c5f03365471cbf77cd4bc

This records an independent internal mathematical check of the stated
theorem and its written proof, not an external peer-review certification.

## Checked proof

1. The changes of variable in (11) and (12) retain the complete Mangoldt
   measure. Their limits are respectively J_-(f) and J_+(psi), with no
   missing square-root factor. The Chebyshev bound controls the small
   scaled interval in the past row; the explicit theta-tail dyadic sum
   controls the entire infinite reflected row. Only the ordinary prime
   number theorem, not a critical-line error estimate, is used.

2. Stationarity tested against phi/psi is legitimate because this is a
   bounded continuous compact test away from the wall. Positivity permits
   discarding the anchor term. The full-row asymptotics compare F_-phi
   with U on the tail, while a_R U <= L bounds the remaining bounded
   interval. Thus B0(R) is uniformly bounded without a_R <= 1, recovery
   of a_R to one, or a fixed shape or support for t_R.

3. For each fixed cutoff, P_R is a positive Markov kernel and mu_R is a
   finite measure. Equality against all compact continuous tests
   identifies its pushforward measure with mu_R. This proves invariance
   for bounded Borel r and r^2 without assigning either an additional
   source-form domain. Their two exact moment equations are (17).

4. Fatou's lemma gives Z_R tending to infinity for every fixed
   0 < epsilon <= 1. Uniformly bounded mass on bounded intervals and the
   plateau of r give the two normalized limits c and c^2. The stationary
   moment equations give instead 0 and m > 0. These conclusions are
   incompatible. Monotonicity of the output cutoffs is not needed.

5. The contraction consequence follows by applying the claimed L2
   contraction to 1 + t h for both signs of t. The changed-moment
   condition (19) follows from the same identities. The displayed
   mean-projection example is a genuine stationary contraction once the
   two prescribed moments are changed; it meets the stated weighted
   anchor-integrability requirements.

## Dependencies and scope

The report's two relative references supply the original theta-source
normalization and the actual bounded ratio plateau. Both reference
targets and section anchors agree with the existing published reports.
The proof of the obstruction itself is written in the report, including
the arithmetic asymptotics and the measure-theoretic limiting steps.

The conclusion concerns precisely the positive past-row plus rank-one
completion with the three prescribed moments. It does not exclude
arbitrary stationary kernels or signed completions. It gives no bound or
sign for the original mixed prime expression, does not remove any of its
Gamma, pole, or cutoff terms, and does not prove the critical spectral
inequality or RH. The written proof passes within this scope.
