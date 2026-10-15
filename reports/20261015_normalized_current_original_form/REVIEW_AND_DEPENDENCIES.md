# Mathematical review and dependency record

## Statement and scope

The report proves that the normalized amplitude of the SAME actual
finite/full Mobius covariance current gives an original-form test
L_cur=psi A_cur. The proof uses the complete actual projected equation,
not bounded amplitude alone. The optional two-source Gram statement is
conditional on the same-gauge canonical test L_can already belonging to
P; this report does not replace that separate canonical-domain proof.

The publication corrects an operator identification: an auxiliary
Liouville-character term -K_l is not the actual projected prime term.
The genuine equation has +K_theta with 0<=theta_p<=1. The report carries
that plus sign through the normalized conjugation and recomputes the
whole original-form remainder R_theta. This is a substantive convention
correction, not an assertion that the two operators coincide.

## Mathematical checks

1. **Actual projection and all boundaries.** The finite profile is
   a_N=1-mu 1_(n<=N), equal to one beyond N. The off-site projected
   covariance has a plus attenuated-prime term. Every prime power remains
   in the original diagonal and source; the complete source-gradient,
   reset residual and finite-divisor boundary stay in f.
2. **Normalized conjugation.** The isometry is
   F1=psi A_cur/sqrt(2z), with
   ell1=z^(-1/4) exp(2z)/(sqrt(2) pi^(1/4) R).
   The continuous generator is G_3, the scalar shift is (log 3)/2,
   and the prime coefficient is
   log(p) sqrt(p) exp[-3(p^2-1)z] R(p^2z) theta_p(p^2z)/R(z).
   The latter is a bounded perturbation with its actual plus sign.
3. **Generator domain.** The complete forcing envelope and the lower
   bound R(z)>=R(pi)exp[-(z-pi)/2] suffice for the transformed forcing
   to be L2. The zero-extension argument keeps the full Carleman row
   and excludes an endpoint-supported discrepancy in H^(-epsilon),
   epsilon<1/2. No artificial boundary condition is imposed on the
   future Gamma generator.
4. **Return to original P.** The proof explicitly compares the z and x
   logarithmic kernels, pays the intermediate-distance logarithmic
   moment, includes the odd-wall term, and supplies origin/far cutoff
   approximations. Bounded A_cur controls the remaining complete
   theta-weighted potential, prime, reflection and pole rows.
5. **Original density.** The exact source operator is
   P_theta=D0+F_theta+beta+kappa. Consequently R_theta includes
   -F_theta and -omega^(-1)[D0+F_theta,omega], together with the full
   backward, raw crossing, delta W and pole terms. Raw crossing and
   pole-completed crossing are not conflated. All brackets keep their
   common cutoff grouping; no unnecessary separated operator domain
   is claimed.
6. **Stronger metric.** The new forcing pairing is
   integral psi^2 A_cur f/sigma^2. It differs from the older
   true-variance pairing integral psi^2 A_cur f. Prior quantitative
   contraction constants do not transfer to this stronger metric.

The result is an original-domain upgrade. It gives neither a favorable
sign for R_theta nor an independent bound for the ordered arithmetic
collar, critical negative-wing norm, K<=1, or RH. In particular, the
actual first-slot stationarity is not counted as a new energy estimate.

## Published dependencies

The report reuses the following existing public results rather than
copying their estimates or counting their energy budgets a second time.

- [Finite arithmetic projection](../20261014_coupled_source_profile_square/FINITE_PROJECTION.md):
  the actual off-site coefficients and complete finite boundary.
  SHA-256: `eb30e24bec7bce8c9f45f2c3340fcd1a958386730dab100c9270efbcce7ef780`.
- [Reset facts and complete forcing](../20261014_coupled_source_profile_square/RESET_FACTS.md):
  bounded actual amplitude, score envelopes, and the grouped forcing
  bounds, including the origin scale.
  SHA-256: `5fef9a2bfdd2ebfe2e093cd3e5d89fbbc5bf1f0306455cc4388d0be348431d2c`.
- [True-variance metric](../20261014_coupled_source_profile_square/TRUE_VARIANCE_METRIC.md):
  the full-posterior bound 0<-R'/R<1/2 and the exact plus-prime
  projected conjugation. Its older metric is not substituted for the
  stronger pairing in the present report.
  SHA-256: `0033e63a6f1669cf90d6e17b3484042a0263a659a80defb7d3e8b8d41b1a0fc0`.
- [Centered profile](../20261014_centered_mobius_profile/CENTERED_PROFILE.md),
  [uncentered profile](../20261014_centered_mobius_profile/UNCENTERED_PROFILE.md),
  and [exact residual cross](../20261014_centered_mobius_profile/RESIDUAL_CROSS.md):
  the same-current construction and its existing profile/form scope,
  as referenced by the reset facts. These do not by themselves supply
  the new unweighted scalar original-P conclusion.

## Report pin

`REPORT.md` SHA-256:
`5b9a43b8956e71ab84d57c0cd67913619d909476a7ba82307b1178323a2b30ad`.

This report is analytic. It introduces no numerical certification or
new computational checker; the existing finite arithmetic and tail
proofs remain in the linked public dependencies.
