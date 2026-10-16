# Independent internal review

The complete written argument and rational certificate were independently read and checked. The finite-pair Halasz/local-beta density envelope passes this review.

Reviewed SHA-256 pins:

- `REPORT.md`: `828b5df5d46e2adee9b9760f48851648dcd95b4c2da5f1b5de227ff8f8ff61f0`.
- `check_certificate.py`: `f3629d497d769d7c39642e87d6c38ee5af83eae83c4bc8e9ad756fd8781dd5f8`.

The arbitrary-pair Halasz elimination retains the full intermediate parameter ranges. The two convex weights lie in [0,1], cancel the intermediate real-part parameter, and yield the displayed three-term bound. The zeta large-value input is used only for height exponent at least one; the remaining short range is paid separately by mean square. Taking a maximum of finitely many complete Montgomery prefixes is lawful and does not assert a common optimizing pair at every parameter.

The five pair values and their B-transforms were checked against the author-maintained exponent-pair chapter, including the explicit global status of v3 and v4. The new local row (29+173 alpha)/280 and its entire closed validity interval [227/601,12/31] were reopened in the beta chapter's Huxley table. The root alpha_sigma stays inside that interval throughout the stated sigma range. Beyond 12/31, the global v3 row has decreasing ratio beta(alpha)/alpha and endpoint value 404995/456396 < 111/125. Together these cover the whole required prefix, not merely the neighborhood of its root. The strict tau cutoff remains valid at the closed sigma endpoints.

Corollaries 8.5, 8.7 and 11.10 were checked directly in the author-maintained source. With tau0=D-d, both complete input ranges hold strictly below their vanishing boundary, and the Montgomery range reaches tau0-(1-sigma). The fixed positive loss is chosen before the imported epsilon losses, then removed in the exponent infimum. No uniform implied constant in sigma or boundary estimate without loss is assumed.

The independent standard-library replay passed. The checker includes every intersection of the finitely many affine rows and their validity boundaries; on each resulting cell the chosen branch is affine, so endpoint and interior checks establish the entire envelope. All seven formulas, their joins and positivity were verified. The comparison likewise partitions at every possible sign change and retains the table's exact closed-endpoint conventions, including sigma=.9 and the jump at 279/314. The two claimed strict improvement intervals, the intervening non-improvement interval, the applicable 3/(2 sigma) comparator and every displayed numerical example pass exact rational checks.

The result is an asymptotic density-exponent consequence of the stated established inputs. It makes no exhaustive pair-hull or worldwide novelty claim, no effective finite-height zero exclusion, and no claim about a percentage of actual zeros. An external repository's unverified claim is not used as a mathematical premise. The comparison is against the explicitly identified table and extra proposition, with the latter's unpublished-preprint qualification retained.
