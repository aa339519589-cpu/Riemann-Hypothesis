# Independent review of the norm-divergence addendum

Date: 2026-10-16.

Reviewed text: [The prescribed-moment operator norms diverge](NORM_BLOWUP_ADDENDUM.md).

Reviewed SHA256:

    7a338b770dd0a7e205948fdb4c44ff9ef027f685180e7bf62bb703d988937b94

This is an independent internal mathematical review, not an external
peer-review certification. The previously published report and its review
are unchanged.

## Checked argument

1. The norm in (A1) is explicitly an extended norm tested on every bounded
   Borel input. Failure to respect the measure's null classes means that
   the norm is infinite, rather than giving an assumed bounded operator
   on a quotient. When the norm is finite, density of bounded functions
   in the finite-measure L2 space gives the stated extension.

2. For the fixed compact test h0 = phi/psi, the input norm is uniformly
   bounded. The complete past-row prime-number-theorem limits in the
   report give F_-phi >= kappa U on a fixed tail. Positivity of the
   remaining rank-one branch therefore controls q_R = a_R U/L there.
   On the fixed bounded interval, 0 <= q_R <= 1 suffices. This proves
   (A5) with constants independent of R, without stationarity, an upper
   bound a_R <= 1, or a common shape for the anchor.

3. The prescribed moments give the exact positive anchor expectation
   d = m + c^2 for f = (r-c)^2. Positivity of the past branch gives
   P_R f >= d(1-q_R). The triangle inequality then proves (A2), with
   the displayed C0 and C1 and with no reversed inequality.

4. The total mass tends to infinity while the mass on every bounded
   interval remains uniformly bounded. Boundedness and the plateau of r
   therefore give the normalized fourth-moment limit (A7). Combining it
   with (A2) proves divergence of the extended norms, including sequences
   that contain infinite norms. No convergence of operators between the
   varying L2 spaces is needed.

5. For varying anchor moments, a uniform norm bound and the same two
   tests force their expectation of (r-c)^2 to tend to zero. Probability
   Cauchy-Schwarz then gives the claimed first- and second-moment limits.
   For the actual ratio at epsilon = 1, the published ratio theorem gives
   r-c in L2 and bounded; the complete row asymptotic makes exp(-x)L^2
   bounded. Thus the fourth-moment input norm is uniformly bounded, which
   proves the stated square-root-of-mass lower bound. No rate in the
   unspecified cutoff parameter is inferred.

## Scope

The addendum strengthens the obstruction for exactly the positive
past-row plus rank-one family with the prescribed moments. The
changed-moment mean projection remains a legitimate norm-one example
outside that prescription. No estimate for the original signed prime
expression, new source-form domain, critical spectral inequality, or RH
conclusion is supplied. Within this scope, the written proof passes.
