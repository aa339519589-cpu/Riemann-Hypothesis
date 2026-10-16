# Independent internal review

16 October 2026, UTC. **Pass** for the two stated sigma intervals, all
three branch cells, and the explicitly identified comparisons. This is an
internal proof audit and exact-arithmetic replay, not external peer review
or formal-kernel verification.

Reviewed report: `bfd73895c66d1a1e8e48a95f0230eda3986e7af7a72a557ab6e4dfe442b21bd7`.

Reviewed verifier: `fa52e0271c15f6e196b4341976597e6c6a358e047d39931b2a1a66585eeaf324`.

## Source and analytic checks

The complete report and standard-library verifier were read. CDV's primary
Sections 2--4 and Appendix A were reopened, including the actual two-Gram
inequality, multiset construction, the subunit contribution and the places
where its original proof used `N >= sqrt(T)`. Trudgian--Yang's primary
Lemma 5.1 was checked with both large-value terms retained. The exponent
pair and growth inputs are precisely the cited Bourgain and v4 inputs;
the proposed additional Cushing pair is not used in this report.

- The coefficient-one self-Gram estimate follows by summing the
  first-derivative bound for small differences over a separated set and
  applying the exponent-pair bound only for larger differences. The small
  range costs `R N^2`, not an unpaid `R^2 N^2`. The arbitrary detector
  coefficients are removed by the primary Cauchy/Gram inequality before
  this estimate is applied.
- Expanding both resulting factors gives all four displayed products.
  Interpolating the two original CDV lower terms at `p=1/2` or `p=1`
  independently reproduces all three count bounds. The fourth product is
  absorbed only using the explicitly verified strict exponent margin; it
  is not treated as an extra count estimate.
- The same critical-line threshold pays the high truncated sixth moment
  and low truncated q moment. The subunit contribution is separated as in
  the primary proof. No full sixth-moment estimate or questionable
  single-term conversion is imported.
- The entire detector length interval and common comparable multiset
  lengths are retained. The auxiliary set is separated, and the verified
  inequality `n+alpha2<1` pays the second Gram factor's length restriction.
  Below `sqrt(T)`, the original Heath--Brown simplification is replaced,
  not invoked. CDV Lemma 3.1 requires only the polynomial upper length
  bound here. Its subunit absorption and the later smoothing constant are
  still paid by the fixed positive lower length exponent and sufficiently
  small losses.
- The high-interval contour is genuinely shifted only in the initial
  detector. Its Gamma line remains in a fixed compact subset of `(-1,0)`.
  The additional zeta-pole residue is exponentially small above
  `log^2 T`; the discarded low zeros have logarithmic count. A fixed
  positive perturbation of y makes the remaining integral tend to zero,
  using the stated v4 growth bound and the mollifier estimate. The
  class-I Halasz kernel and its moment split remain on the critical line.
- The maximum of the three affine choices for `alpha1` is handled over
  the full length interval by convexity, while the absorption margin is
  concave. The finite endpoint tests consequently certify every length,
  not just a grid. The half factor in `delta1` pays its strict upper bound
  when the maximum is zero. The large-cardinality case and fixed-loss
  passage preserve all strict margins and include all outer endpoints.

## Exact replay and comparison scope

The verifier was independently rerun with ordinary Python and exited
successfully. Its rational-function identities, denominator signs and
power-to-Bernstein interval checks were inspected. All three closed sigma
cells, complete length-window conditions, strict absorption, branch join
and sample rational values passed.

The high-interval comparison uses the corrected normalization: the old
exponent is `eta/(3 sigma-2)`, hence the old y is
`1/[4(3 sigma-2)]`. The script proves a strict gain against this actual
quantity. The low comparison intersects every applicable prior
full-diagonal branch. The separate table comparisons and the broader
`3/(2 sigma)` coefficient are checked only in their stated scopes.

The accepted conclusions are asymptotic, with a fixed sigma and arbitrary
positive exponent loss. They are not effective finite-height counts,
percentages of individual zeros removed, an optimal envelope over all
possible inputs, or a worldwide-priority claim.
