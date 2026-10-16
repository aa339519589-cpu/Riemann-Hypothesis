# Independent internal review

Reviewed report SHA256:
`ee78f3d350bdcba31736885becdc60baf1583b9a06a5d9c619dbc16350e36b1e`

Reviewed exact checker SHA256:
`e6a1b4d1300cb1721d21ae44a7ef034c794243bef0de2303dc41b9c1ab6c8ef7`

Date: 2026-10-16 (UTC).

## Findings

The complete report and standard-library rational checker pass independent review. The checker was separately executed and all assertions passed.

1. The general derivative intervals retain all three Heath-Brown branches and their strict endpoints. Their consecutive overlaps and increasing right endpoints are correct. The short second-derivative argument fills the possible low-end gap when ell = 3; it is used only within its valid range. Thus the full Montgomery interval, rather than isolated parameter values, is available.
2. The zeta interval-sum branch covers the entire required interval starting at 2. The subdivision input is the stronger endpoint tau0 - eta, exactly as stated in the primary Corollary 11.10, not the older tau0 endpoint. Taking tau0 = min(M + eta, 3Z/4) - d proves the general conversion. The fixed-d then epsilon passage and the small left shift in sigma are properly retained.
3. The new growth specialization was checked directly against the primary Corollary 8.13 and Table 6.2. The two supplied vertices give exactly the displayed M1, M2 and D1, D2. Their strict separation from both the intermediate Montgomery threshold and the zeta ceiling holds throughout the closed interval by affine endpoint checks. Their crossover is 67/1692. At sigma = .96 the density exponent is 267/6875, with saving 333/522500 against the stated 3/76 table exponent.
4. The comparison with the separate Pintz growth-based theorem is explicitly a comparison of supplied growth bounds, not a lower bound for the unknown true growth function. The rational vertices, convex interpolation, two curved bounds, functional-equation reflections and infinite Heath-Brown tail are accounted for. The unrestricted curved-ratio minimum and the reflected-curve inequalities are correct. The three cases for the integer ceiling cover every admissible enlargement of the supplied constants, not only separately minimizing inputs.
5. The finite checker uses exact fractions. Its endpoint assertions prove the stated affine inequalities on their full interval. The general symbolic interval proof is supplied in the report and is not replaced by a finite parameter sample. The separate fixed-point calibration of the declared-growth comparator also passes.

The conclusions are asymptotic zero-density upper bounds with an arbitrary positive exponent loss. They do not provide an effective implied constant, a finite-height exclusion, a percentage of actual zeros, or RH. Attribution to the established derivative, growth and subdivision theorems is explicit. Comparison against the named table and declared growth family is verified; exhaustive worldwide priority is not claimed. These are independent internal checks, not external peer review or a formal proof-assistant verification.
