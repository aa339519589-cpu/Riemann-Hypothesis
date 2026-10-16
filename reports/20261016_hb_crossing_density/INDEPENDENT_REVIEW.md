# Independent internal review

The full proof and exact rational checker were independently read. The analytic derivation, complete length-window conversion and stated comparisons pass this review.

- Report: `27dbac42c6897ac62b05836a8b16892e32678b1a858dc1b964f737fe6351e01b`.
- Checker: `eac2f330f735f826bd521070e1c06d24635ab792fd15502bc87c098b748a0fa1`.

## Analytic source and normalization

The accessible primary Guth–Maynard v2 text was reopened at Theorem 1.6, the complete proof of Lemma 6.2 and (6.1)–(6.4). Its difference-set estimate does not impose M^k<=Y. The report supplies the needed scale-general two-point derivation rather than applying a fixed-scale proposition outside its setup.

The smooth majorant, coefficient norm and diagonal in the Halasz inequality retain the outside polynomial-length factor. The separated-set thinning costs only an arbitrarily small power. In the reflection step, the zero Fourier mode is negligible, the Mellin shift is smaller than the separated ordinate scale, and the support-adjusted common integral has the stated first/second-derivative bound. The smaller dyadic-block prefactor is enlarged in the safe direction before taking a common maximum. Coefficient phases and fixed-power divisor bounds meet the full difference-set theorem's hypotheses.

The resulting three off-diagonal exponents, Cauchy factor and absorption for fixed sigma>3/4 were independently recomputed. They yield exactly (3), with arbitrary positive exponent loss. The deficient intermediate normalization in the database is not used. This review does not claim access to the historical paywalled 1979 text.

## Complete conversion and comparisons

For k=3, the crossing, its value, the subdivision intercept and tau0 were recomputed. All three portions of [2tau0/3,tau0] are paid: mean square below one, the complete affine envelope through the crossing, and subdivision thereafter. The crossing is above the Montgomery level, so the report correctly invokes Corollary 11.9 directly, not the stronger prefix hypothesis of 11.10. The zeta-polynomial window is empty because tau0<3/2. Fixed sigma and sufficiently small analytic losses give the stated arbitrary-epsilon density theorem.

The current author-maintained density chapter was reopened for the exact conversion, both Table 11.1 branches and Proposition 11.37. The strict table comparisons and the separate Kerr polynomial comparison hold on the full stated interval. Kerr's unpublished-preprint status is explicitly retained, and it is only a comparator. The Annals publication details and DOI for Guth–Maynard also match the publisher's record.

## Exact replay

The standard-library checker was independently executed and returned PASS. Its affine endpoint checks, factored crossing inequality and monotone quadratic comparison certify entire intervals, not a sampled grid. At sigma=773/1000 the new exponent is exactly 1589/3417, the identified table exponent is 454/957, and their difference is 3405/363341.

## Scope

This is an asymptotic density corollary of established analytic estimates and subdivision. The implied constant is not made explicit. It does not certify finite-height zero exclusion, a percentage of actual zeros, RH, exhaustive global novelty, or a new mean-square theorem. The checker supplements the full analytic proof; it does not verify imported theorems or substitute for their hypotheses.
