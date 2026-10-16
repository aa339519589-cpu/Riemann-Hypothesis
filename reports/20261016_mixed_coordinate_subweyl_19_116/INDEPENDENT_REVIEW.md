# Independent internal review

16 October 2026, UTC. **Pass** for
`|zeta(1/2+it)| <= 10000000 |t|^(19/116) (log |t|)^(33/58)`,
for `|t| >= 3`. This is an internal mathematical and computational audit,
not external peer review or formal-kernel verification.

## Reviewed bytes

- `REPORT.md`: `758d886b9f8ec47bdfa3c5cab4a99e1f7619357a5901381a9ed66521eab6f81c`.
- `SECOND_DERIVATIVE_LEMMA.md`: `bcf7c34ba1c9a9c1f60bcd323dfdee8487641abd144d597edcff2d942cba32ca`.
- `MIXED_A_AND_CUTOFF.md`: `7056143dcafe1405ede7ccb85aedae005443be8d165c9cc29306689220b56850`.
- `ACTUAL_MIXED_DERIVATIVES.md`: `b2499226b792dc95e60882093563a0f27ba674c9cd85813f998f3223fce69a7e`.
- `certify_anisotropic_mixed_bound.py`: `333fe30f49931f7740c4f2c67b4fbbe7dcf9e979199c736851e38ebcefbec88e`.
- `anisotropic_mixed_bound.json`: `6cdf5afd6619734a3b1ec5292f3d114c5c59f713d6306ea2f38d2e4e03e7c0bc`.
- `certify_mixed_derivative_constants.py`: `b4798455eae95cf7d70d504e3d2ace94acfd520118a0f7be605488eb1d51559a`.
- `mixed_derivative_constants.json`: `ad6e7bd07a73fbfa4795a94dff8a9f1467329e22e4160114d1ac390f52a58617`.

The complete report, three local appendices and both verifiers were read.
The primary Patel--Yang v1 derivative recurrence, complete Poisson Lemma
2.3 and raw logarithmic-correlation errors were checked directly. The
Riemann--Siegel setup and remainder are retained. The previously reviewed
coefficient-110 theorem is used solely for the lower-height splice, and
its published relative-link target was verified. This proof does not
require the separate balanced mixed-coordinate global theorem.

## Analytic audit

1. The rectangular second-derivative lemma was checked from its gradient
   map and oscillatory integral through the exact smoothing, central
   frequencies and every one-/two-far Fourier tail. Its definite and
   opposite-diagonal cases have valid injectivity arguments. Thin lattice
   rectangles and all removed boundary rows are explicitly paid.
2. Both mixed-coordinate A words retain all inclusive-lattice diagonal
   terms, floors and inverse-row harmonic sums. The corrected total-shift
   guard keeps the two same-coordinate shifts inside the actual phase
   domain. Separable Fourier cutoff twists vanish at the terminal mixed
   difference, uniformly in their frequency. The finite Fejer error pays
   exact lattice equalities; the amplitude's complete two-variable Abel
   norm is bounded by five times its supremum.
3. The differentiated actual phase series through total order nine,
   finite-difference averages, signed model derivatives and definite
   Hessian lower bound were checked. The exact rational certificate agrees
   with the analytic majorants. No nondegeneracy is asserted for the
   undifferenced square-root phase.
4. The new argument lawfully retains the transposed one-word estimate
   before the geometric mean. Substitution of the three dual scales gives
   exactly `c^(9/22) R^(29/22) a^(-3/11)` in the weighted main row. The
   signed outer correlation is preserved until this complete curved-domain
   estimate is applied. The three bins and at most five monotone pieces
   cover all stationary labels with their original endpoint convention.
5. For the new integer choice of q, every changed scale guard was
   reconstructed independently. The relevant exponents are `-1/203` for
   the shift ratio, `341/203` for the inverse-row guard, `-132/203` for the
   phase series, and `137/203`, `50/203` for the two logarithmic scales.
   The lower bound on the unfloored q is increasing above the stated
   starting height. All complementary labels retain their full trivial
   first-dual length and the once-reserved endpoint debit.
6. Dividing the squared weighted block by
   `a^(1/29) t^(9/29) x^(33/29)` gives exactly the two constant main/diagonal
   rows and four decreasing corrections displayed in the report. In
   particular the small-r, endpoint, derivative and logarithmic exponents
   are respectively `-1/28`, `-19/116`, `-61/609`, and `-66/203`.
   Both original Poisson power errors and its full logarithm remain.
7. The positive block power `a^(1/58)` permits the complete geometric sum
   ending below `sqrt(t/(2 pi))`. The resulting factor
   `(2 pi)^(-1/116)/(1-2^(-1/58))` includes the shortened last block.
   Initial and middle sums retain the published derivative-test factor,
   both complete geometric rows, both Riemann--Siegel halves and both
   remainder terms.
8. The normalized infinite-tail corrections are decreasing. The full
   lower-height interval is paid by the coefficient-110 theorem using
   exactly `229/1392 - 19/116 = 1/1392` and `log 3 > 1`. Conjugation pays
   negative heights. No sampled-height cover replaces these arguments.

## Independent replay and scope

The exact rational derivative verifier and the anisotropic global verifier
were independently replayed from separate copies with non-optimized
Python. The latter used official python-flint 0.9.0 / FLINT 3.6.0 at
192-bit precision. Both exited successfully, and both scientific JSON
outputs matched the frozen files byte for byte.

The directed enclosures give:

- normalized squared large-block coefficient below `87404247.805`,
  strictly below `10^8`;
- complete infinite-tail coefficient below `1657082.677`, strictly below
  `10^7`;
- lower-splice coefficient below `144985.413`;
- ratio to the prior coefficient-110 bound below `0.458200` at
  `log t = 25000`, decreasing thereafter.

The result supplies a complete explicit bound with a classical exponent.
It is not a new unrestricted exponent record, an exhaustive priority
claim, a zero-free region, or a zero proportion. The useful envelope
retains the minimum with earlier estimates. All three local appendices
are necessary scientific parts of a standalone release.
