# Independent mathematical review

This is an independent internal mathematical check, not external peer review.
The reviewed `REPORT.md` has SHA-256
`97210e4e492276549194875229fce785a452a5ca483ecab8e0738045e721dded`.

The following parts were checked against the complete source normalization
and then read in the final manuscript:

- The half-line operator is `Q0/2=G-F_+-F_-+R-4 ell(.)s`.
  Its quadratic pole is `-8 ell(.)^2`, and its off-support odd Gamma
  kernel is exactly the difference in equation (3).
- The comparison cost is first defined by nonnegative reflected-edge
  squares. Expanding at finite prime cutoff and using the finite fixed
  cross term gives equation (6) without an unproved pointwise domain
  for `Rh` or a subtraction of two infinite quantities.
- A fixed interval containing `log 2` controls the unweighted wall mass
  through the prime-2 term and the `exp(y/2)` tail mass through the full
  Mangoldt prime number theorem. Local uniform convergence supplies the
  intervening compact interval.
- The two complete arithmetic test rows have the asymptotics (8).
  Their leading difference is cancelled by the entire pole in (9).
  Together with the off-support Gamma estimate this gives precisely
  `Q0 phi=O(x)` at the wall and `Q0 phi=o(exp(x/2))` at infinity.
- These endpoint estimates and the positive mass bounds justify
  absolute pairings and uniform removal of both endpoints. The weak
  equation therefore passes to the locally uniform limit. Applying
  this to any bounded-cost subsequence proves divergence of the
  extended costs, not merely unboundedness along some subsequence.
- In the actual-source application, `f=g+c psi` is strictly positive
  and comparable to `psi`, its reflected cross term is finite, and
  `Q0 f=-2 delta Wg` is nonzero by the stated nontriviality hypothesis.

The hypothesis is full weak operator neutrality, not a scalar zero of
an indefinite quadratic form. The theorem neither constructs positive
neutral approximants nor excludes all ground optimization. It supplies
no reverse bound for the actual prime correlation and no RH conclusion.
The relative mathematical dependency is the already published
[small-shift report](../20261015_actual_small_shift_gram/REPORT.md),
Section 1; its shift inequalities are not used.
