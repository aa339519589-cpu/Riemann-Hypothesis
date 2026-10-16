# Independent internal review

The complete report and exact rational checker were independently read. The final checker was rerun successfully.

- `REPORT.md`: `70bba8afba8e7fd32e450f9337f95fbbf5f71a213254a46495f2d088b92e4d2f`
- `check_certificate.py`: `380a2dad2cf9031eb63cc7d35f82f2c85d0d74fe0be0a97f178732bb10aa6b03`

## Analytic checks

1. The author-maintained [large-value chapter for zeta partial sums](https://teorth.github.io/expdb/blueprint/largevalue-zeta-chapter.html) was reopened. The minimum with the original large-value exponent is explicitly retained in the proof of Lemma 8.12 and used in Lemma 8.16. The report's arbitrary-pair convex combinations cancel the entire auxiliary u variable and control every v between 1 and tau. The weights are in [0,1], and the fixed multipliers of the arbitrarily small losses are harmless.
2. The exponent-pair input in Lemma 8.11 has exactly the coefficients used in the report. It is only applied at v >= 1 here. No conclusion for zeta partial sums at v < 1 is imported from that displayed lemma; the report instead uses the ordinary mean-value bound for the original large-value exponent below tau=1.
3. The original pair (18/199,593/796), its Sargos/Bourgain derivation in [Theorem 5.20](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html), and its B-transform were checked. The transformed pair supplies the complete Montgomery prefix, while the original pair supplies the distinct zeta-vanishing ceiling through Corollary 8.7. These uses are not interchanged.
4. [Corollary 11.10](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html) requires the prefix through tau0+sigma-1 and the complete zeta interval from 2 to 4 tau0/3. Both are paid with the fixed positive loss d. The strict ceiling holds throughout the closed interval, including both endpoints. Choosing d before the imported exponent losses gives the claimed final epsilon estimate.

## Arithmetic and comparison checks

The standard-library replay passed the exact pair arithmetic, affine interval premises, height ceiling and all displayed exponent fractions. At sigma=22/25, it gives exponent 5985/30803, with saving 878/154015 against the identified table exponent 1/5.

The declared growth-family comparison was also checked, including all listed rational vertices and reflections, the finite and infinite Heath-Brown parts, both curved branches, the near-one restriction and outer extensions. The reflected-curve cubic has four strictly positive exact Bernstein coefficients. The infimum comparison concerns the supplied upper-bound family, not a lower bound on the true growth exponent.

One comparator correction was made before this final pin: the unpublished Kerr proposition's 3/(2 sigma) branch does apply on this interval. The final report now states this and proves that the new coefficient strictly improves it; only that proposition's other branch has a disjoint range. The checker includes this comparison. No Kerr result is used as an input.

No further correction is requested. The accepted scope is an unconditional asymptotic density-exponent improvement on 7/8 <= sigma <= 177/200 from the stated established inputs, with the explicitly bounded table and supplied-family comparisons. It is not an effective finite-height exclusion, a percentage of zeros excluded, or an exhaustive worldwide novelty claim.
