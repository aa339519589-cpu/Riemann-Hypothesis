# Independent internal review

16 October 2026, UTC. **Pass** for the two-branch asymptotic zero-density
theorem on `87/100 <= sigma <= 219/250`, with the stated multiplicity
convention and an arbitrary positive exponent loss. This is an internal
mathematical and computational audit, not external peer review or
formal-kernel verification.

## Exact reviewed files

- `REPORT.md`: `62f75e367ca35c4d013f021057aabec9505df638ef05955635c81049431694d2`.
- `check_certificate.py`: `ef1da774ea1a2194e4a18810162ccc5b9dcd63b4a191d7a4d42291a6297817b6`.

Both files were read in full. A separate frozen copy of the standard-library
checker was executed with ordinary, non-optimized Python. It passed all
181 density interval-sign checks, the complete beta/phase-range checks,
the continuous moment-envelope identities and the additional predecessor
comparison below `.873`. Its polynomial reduction and Bernstein conversion
were checked at source level; denominators are separately strictly signed.
This is a continuum certificate, not a sample grid.

## Primary inputs and analytic audit

1. The stated Huxley rows and their complete valid intervals were checked
   in the author-maintained exponent database, together with its model-phase
   definition and reflection theorem. The global pair and its B-transform
   agree with the previously reviewed detector input. These established
   statements are inputs; this review does not claim a new reconstruction
   of Huxley's original proofs or a new global exponent pair.

2. I directly read de Faveri--Pandey v1, Section 7 and the reduction in
   Section 9 through (57). The present level range satisfies the short
   second-moment scale conditions and `N <= T^(3/5)`. Corollary 7.2 requires
   exactly the two retained W caps. The additional `W <= N^(4/3)` condition
   belongs to their later special large-value input, which is not used here.
   Thus the reduction is not an application of their final large-value
   theorem outside its range.

3. Removal of partial-sum maxima is performed on the summed inequality.
   The two retained inequalities involving F, Z and R1 have their correct
   direction. The number of transformed one-spaced parts includes
   `max(1, G^(-1) sqrt(T/N))`; the Atkinson upper length pays this maximum
   up to the allowed small loss. Halasz--Montgomery duality gives a
   coefficient-one correlation kernel. Its small-difference harmonic row
   and diagonal yield `N^2 R' log T`. The full large-difference bound is
   absorbed only with a fixed power margin. Combining these facts gives
   the favorable factor `1/F` in (10), which may safely be dropped.

4. The square-root phase with its shrinking perturbation is a model phase
   after multiplication by two. The reflected local beta bounds are paid
   over every intermediate difference, not only at the endpoint. The
   joins at `102/335`, `87/275` and `423/1295`, positive normalized
   derivatives, lower-length global-pair branch, all phase caps and the
   monotonicity in the full Atkinson length range were independently
   checked. A fixed loss in W supplies strict absorption, including at
   the exact joins; neighboring global rows pay the arbitrarily small
   endpoint length losses.

5. The resulting two local large-value rows join continuously and meet
   the original global envelope at their outer endpoints. Positive affine
   intercepts give radial closure, while the slope bounds give both
   required level-integral monotonicities. These are different conditions,
   and both are used. They justify the same-threshold high second and low
   twenty-fourth truncated moments on the full height interval. The
   subunit contribution is retained. No improved full moment is inferred.

6. The general moment premise in CDV (3.3) permits positive moment
   exponents and orders at least two, so the high second moment is lawful
   even though its height exponent is below one. The threshold is chosen
   after the fixed length/subdivision parameters and is evaluated at T0.
   Both Case-1 expressions reduce to (21), including the essential outer
   `+alpha2`. The complete coefficient-one Gram product and its strict
   absorption row remain unchanged; Case 2 admits both interpolation
   choices for orders two and twenty-four.

7. On every length subwindow the maximum-affine alpha1 makes the count
   rows convex and the absorption margin concave. The certified endpoint
   inequalities therefore cover all lengths, with both definitions at
   the cuts. The branch join where one subwindow has zero length leaves
   no gap. All threshold, common-length, subdivision and strict-absorption
   margins are paid before taking arbitrarily small losses. Both Class-II
   terms use the established global two-term large-value input, not an
   unjustified local substitution.

8. The published detector source closures and common multiset-length
   condition are retained. No original Heath-Brown length simplification
   is applied below its range. The subunit-zeta split and all required
   smoothing/separation losses remain. The final dyadic-height sum gives
   the stated positive-ordinate count with multiplicity.

## Result and comparison scope

The reviewed exponents are

- `180(1-sigma)/(661 sigma-468)` on `[87/100, 696/797]`;
- `639(1-sigma)/(2227 sigma-1557)` on `[696/797, 219/250]`.

They agree at the common endpoint. At `sigma = 7/8`, the exponent is
`639/3133`, below the identified double-Gram predecessor by exactly
`1242/25017005`. The complete interval comparisons include the correct
earlier full-diagonal branch below `.873`, the stated density-table rows
on their ranges and the broader `3/(2 sigma)` comparator. No claim of
exhaustive worldwide priority or optimality is reviewed.

The result concerns asymptotic density exponents with unspecified implied
constants. It is not an effective finite-height exclusion, an increase
in the percentage of actual zeros known on the line, or RH. The exact
checker verifies the finite algebra; the primary reductions and analytic
arguments above are essential independent parts of the proof.
