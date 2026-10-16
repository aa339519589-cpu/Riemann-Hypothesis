# Independent internal review

## Frozen files reviewed

- `REPORT.md`: `eb89ec25d0a9a9a3ddd8951fb1aaef26d50f12ce8960345236ca5cdccfac758c`
- `check_certificate.py`: `625808e2944a76f355a4af73d121dd66c6e22d9a72d67ee61e4589df172d72db`

The complete report and exact checker were read. The checker was independently run and passed every branch and comparison. CDV Sections 2–4 and its zeta appendix were read directly, with the untouched double-mean-value factor and interpolation on printed pages 2193–2195 rechecked for this refinement. Trudgian–Yang Lemma 5.1, the common truncated-moment derivation and the stated pair provenance were also checked. This is an independent internal review, not external peer review.

## Analytic derivation

1. The two-term critical-line large-value bound gives the common threshold H(U) and both truncated moments. The split is taken at the appropriate subdivision scale. The proof does not assert an untruncated sixth moment of exponent one, and it does not use a questionable full-moment simplification from an adjacent source paragraph.
2. The variable detector length, powering parameter two and common-length multiset construction give the entire interval [4y/3,2y], with the stated small exponent losses. Both detected zero classes are retained. Class II uses both terms of the separate Bv4 critical-line estimate.
3. Before the source's length-based simplification, its first double-mean-value factor is bounded by the sum N^(3/2) R^(1/2) + N R^(5/8) T^(1/4), for R at most N. Both pieces are retained here. No lower bound on R is used to remove a diagonal.
4. The source's two lower powers of the auxiliary cardinality interpolate with weight (q'p-1)/(q'-1). For each of p = 1/2, 1 and 5/8, this weight is admissible because q' is at least two. The interpolated monomial has exactly the stated powers of N, delta1, delta2, R and S, and q' cancels.
5. Each of the two first-factor pieces is combined with each of the three second-factor pieces. An independent exact rational monomial calculation recovered all six rows (16)–(17), including the delta2^(1/4) factor from T0 in the 5/8 rows. Together with Case 1 these are the complete nine terms, not a selected favorable subset.
6. All four moment/length branches use admissible delta parameters below n*. At and above n*, the direct Section-3 estimate replaces the dichotomy bound, so delta1 greater than one is never introduced. The R below target and R greater than N cases are covered separately. In the latter case a subset of size comparable to the common base length can be chosen within every comparable polynomial length supplied by the detector.
7. No final fixed-parameter threshold from CDV is silently applied outside its range. The preceding primary arguments are rerun with the displayed size and length conditions. The final small losses are chosen before T tends to infinity and are paid by the strict parameter/size margins and the allowed arbitrary final exponent loss. This also covers the closed branch joins.

## Exact continuum certificate

The rational-function implementation, polynomial cancellation and exact Bernstein conversion were read. Positive denominator certificates and nonnegative or positive numerator certificates are sufficient on each entire closed interval; they are not sampled grid checks.

The independent replay passed all four sigma branches, the complete lower-length windows and their row slopes, the direct-estimate transitions, both class-II rows, and all three exact branch joins. It also passed the identified table comparisons on both sides of its jump, the intersecting published local-envelope pieces, the separate 3/(2 sigma) comparator and the no-regression comparison with the frozen earlier detector calculation.

At sigma = 22/25 the new exponent is 1264/6607. At the three joins the neighboring formulas agree exactly. The proof correctly states that its improvement over the frozen two-branch calculation is strict only below the second join and is equality thereafter.

## Conclusion and limits

The frozen four-branch theorem and its full exact certificate pass this review on [433/500,89/100]. The analytic contribution is the retention of the full primary double-mean-value factor followed by explicit parameter optimization; the arithmetic certificate is a check of that derivation, not a replacement for it.

The conclusion is an asymptotic zero-density exponent with constants allowed to depend on fixed sigma and the positive final loss. It gives no effective finite-height count or percentage of actual zeros excluded. The comparisons are the explicit identified ones, not an exhaustive novelty or global-optimality claim, and do not claim an independent kernel replay of prior formal implementations.
