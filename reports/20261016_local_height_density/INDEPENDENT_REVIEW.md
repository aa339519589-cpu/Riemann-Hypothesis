# Independent internal review

## Verdict and pins

I read the complete report and exact checker, rechecked the primary analytic interfaces, and independently replayed an unchanged separate copy of the checker. The submitted local-height large-values estimate, truncated moment, weighted detector transfer and stated union of density rectangles pass this internal review.

- `REPORT.md`: SHA256 `29e6fa3ddeec8f6273107c8ee9789c59e97e4584302bbc5ad9034b6ee0c148b8`.
- `check_certificate.py`: SHA256 `6b2a812c38ba3d3499eff74b92ee0d1124e1f2bc7eee4062eadb7957bb867038`.

The conclusion is (1)–(2) on the union of the two complete closed rectangles: sigma in [17/20,87/100], a in [5/6,23/25]; and sigma in [87/100,9/10], a in [3/4,43/50]. All three branches in B are retained. Every parameter is fixed before the height limit, with an arbitrary positive exponent allowance. No larger parameter domain is granted by this review.

## Primary localization and the retained first cell

I reopened [de Faveri–Pandey, arXiv:2610.01035v1](https://arxiv.org/html/2610.01035v1), Lemmas 7.1 and 7.3, Corollary 7.2, and the proof around (54)–(57). Clustering a set contained in a length-H interval leaves its centers and smoothing neighborhoods in a length-O(H+G) interval. The maxima-removal lemma applies to arbitrary finite cell sets and preserves coefficient magnitudes. Thus localization changes the number of occupied phase cells without changing the absolute-height phase assumptions or the summed magnitude relations. The latter retain both inequalities involving F, Z and R1; a pointwise common-size assertion is not substituted for them.

The primary phase reduction requires N<=T^(3/5), W<=sqrt(TN), and N^(1/2)W^2<=T^(3/2). The extra W<=N^(4/3) condition belongs to the later special large-values application, which is not used here. Neither its close-pair refinement nor its Iwaniec input is imported.

The change of lower height exponent from 5/6 to 3/4 introduces no new source hypothesis: throughout the higher-level integration, a >= 3/4 remains strictly larger than twice the pointwise level 13/84, with room for fixed losses. Thus H dominates G. Phase restrictions are still expressed in the absolute height T, not H. Cap-row dominance only uses the unchanged upper bound a <= 23/25.

The local cell count has its necessary initial 1. Combining it with the complete transformed-spacing partition and then the two summed magnitude inequalities gives both terms in (12), with the favorable factor 1/F before it is dropped. In particular the N/G term is not suppressed when the whole height interval fits in one phase cell.

## Correlations, all lengths and all higher levels

The Halasz–Montgomery correlation kernel has coefficients one after duality, although the detected polynomials may have arbitrary bounded coefficients. The derivative estimate pays every difference up to N, including the harmonic spacing loss and diagonal. The global exponent pair pays the complete larger-difference interval because its upper bound increases with the difference magnitude. The square-root phase perturbation tends to zero in every required fixed normalized derivative.

I checked the balance for w(n), its two separate phase caps, the strict margin above w=n for fixed v>365/2742, and the monotonicity in every permitted Atkinson length. Both the pair-limited and phase-cap-limited branches are retained before taking the worst length. Above v=69/463 the cap branch is indeed dominated by the retained one-cell row for the full stated a interval. The envelope therefore covers all higher levels needed for the moment, through the pointwise cutoff with a small fixed allowance. It is not an estimate proved only at the subsequently optimized detector level.

Both affine slopes of the resulting envelope are below -2. A maximal unit-separated subset bounds the measure of a level set by a fixed multiple of its cardinality. Dyadic integration then proves the localized truncated high-second moment. This is a moment on comparable absolute heights; it does not require an unproved radial extension to smaller heights.

## Weighted means and the complete detector

The proof of (16) first subtracts the low-value part using the total mass of the full kernel and then applies weighted Cauchy–Schwarz. Local zero counting pays the sum of translated kernels while preserving multiplicity. The enlarged height interval has length O(T^a). Outside its T^d collar, a sufficiently large fixed polynomial-decay order pays the entire remainder; the more distant tails are paid separately by the same growth/integrability estimate. This argument does not falsely assign exponential decay to a smooth dyadic Mellin transform.

The ordinary Gamma detector and every smooth block longer than sqrt(Y) retain their full critical-line integrals and pole residues. Uniform transform seminorms of w(x)exp(-qx), q>=0, justify the common J_A bound. These long blocks force precisely the common threshold used in the localized moment. They are not incorrectly included in a universal short-block powering assertion.

For the shorter blocks, the Fourier real-part transfer preserves a common fixed polynomial within each cohort. A small-power shift cutoff and zero extraction pay the full decay and separation losses. The bounded integer powers cover every initial short length, and common dyadic product pieces have divisor-bounded coefficients. Normalization leaves the fixed margin above exponent 3/4 and the full translated large-values length range. The resulting two short-block terms maximize at the stated opposite length endpoints. All three terms of (19) are therefore retained before optimization.

The registered primary `MathCollab.Density.large_values` quantifiers were directly rechecked in this audit sequence, including arbitrary translated intervals. Its citation has exactly the mathematical/source verification scope previously recorded; no independent Lean build or kernel/foundation replay was performed or is claimed here.

## Exact replay, endpoints and comparisons

The unchanged separate-copy standard-library execution terminated with `TOTAL PASS 241 exact checks across both rectangles`. I checked the cleared denominators and the multi-affine structure, so the corner tests certify full rectangles, not sample points. The checks include all three max branches, the exact triple crossing, full level and length ranges, all three examples, the complete length/cap algebra, and the declared comparisons on their actual overlaps. In the first rectangle B1 strictly exceeds B0, so retaining the third branch does not change its previous formula. The extra direct Halasz comparison on [4282/4923,.87] uses that first rectangle's own height range. The table jump at 279/314 is explicitly partitioned; no sampling or unverified extrapolation pays it.

The possible equalities in both the retained one-cell balance and the short-block off-diagonal balance are handled lawfully by first using B+xi, keeping all other strict ranges, and only then absorbing the arbitrarily small exponent change. The same order of fixed choices pays the Fourier, coefficient and correlation losses. No interchange with the height limit is assumed.

The Ye comparison uses its above-5/6 coefficient and correctly adjusts its strict-beta convention with a nearby real-part parameter. The global Lewko/Kerr curve, the actual overlaps of all four full-diagonal branches, the finite-pair Halasz envelope, both applicable low EP-Gram expressions, the two global local-LV branches, and the supplementary global-moment detector baseline are distinguished accurately. I checked their rational normalizations against the cited reports, including the conversion Eprev = 2(1-sigma)Bprev. The second rectangle's example at sigma=.9 and a=.75 gives exactly 1/7. The proof claims neither exhaustive priority nor an effective count, zero-free region, percentage of actual zeros or RH.

This is an internal analytic/source and reproducibility review, not external peer review. The finite checker certifies the stated parameter algebra; the new localization, moment and detector arguments were checked separately as described above.
