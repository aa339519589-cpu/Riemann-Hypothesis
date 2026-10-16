# Independent internal review

## Frozen files

- `REPORT.md`: `edbe22b3649d6ea1d0ead65a2b698dbe0ac9b799a87a0efc9918ff147e9dcdcc`
- `certify_global.py`: `a985da3f7b5323cd752f85a3e4e9d25f7c5108e504fc8a888220cbfaf0cf8e55`
- `dual_block.py`: `46b1d5907f9dd6c04b6446991afc20103e2f4bad0ce4e4e3b259e2ffe31e7317`
- `parameters.txt`: `388acc5cfc45acbf6e9e84b79490ba24de751d1dcef0f502b2575538d7a193ff`
- `global_subweyl_49.json`: `e38b4fc79c551a4f7e187d6e990c5efac45184a0818cbcc6ed8575ac1090b8a7`

The complete report, both source files and exact parameter cover were read. The two new local estimates were checked independently of the numerical replay. The published derivative-test statement and constants were reopened directly in Patel–Yang, Section 1.2; its weighted power-sum inequality (3.21) includes all the negative powers used here. This is independent internal review, not external peer review.

## New analytic steps checked

1. The zero-extended A-process permits every positive integer Q. Nonempty difference sums stay within the original phase interval; correlations beyond the sum length are zero. The separate original-block constraint q at most a remains certified.
2. Integrating a monotone fourth derivative gives the required monotone third derivative of each first difference. The third-derivative test, the exact factors 72/91 and 72/55, and the ceiling bounds give all four rows of (L3), with none omitted.
3. In the second local step, Q = ceil(E lambda^(-1/15)) implies j < E lambda^(-1/15) for every integer j < Q. Therefore lambda at most E^(-15/14) ensures j lambda < 1 even at the cutoff. This pays the inner estimate for every nonempty correlation, rather than presuming it for an uncontrolled derivative scale.
4. The weighted exponents 1/14, -1/14, 0 and -1/7 give exactly the constants in (L4), including 49/39 in its fourth row. Expanding the positive product gives the complete eight-row table (L5).
5. Substitution of the dual length, derivative scale and monotone partial-summation weight gives each of the eight pairs in (L6). The first dual lattice point is separately removed and paid by the unchanged E4 = 5.686 coefficient. The complementary lambda range is paid by its full trivial-length debit (L7), including the cutoff factor. Extending the other nonnegative rows over that complementary range is harmless.
6. All eight outer weighted power-sum exponents are in the published admissible range. The six additional normalized finite-height exponents were independently recomputed as exact fractions and are strictly negative. In particular the row with beta = -7/60 uses the lower q enclosure, not the upper one.
7. Every finite-cell block parameter is a specified positive quantity, not an assumed optimizer. The integer q and partition guards, complete logarithmic error, initial and middle sums, top partial block and both Riemann–Siegel terms are retained. The same q is used throughout each block's partial-summation estimate.
8. The tail uses its separately specified fixed parameters. All six extra tail exponents were independently recomputed. Only the stated row has negative spatial power, and it uses the complete lower-endpoint geometric sum. The negative q power retains the factor (1 - 1/q0). Both complementary-range tail rows and the entire logarithmic row remain present for every height beyond the cutoff.
9. The earlier Weyl and finite-table bounds pay the two low ranges. The new closed-cell cover and uniform analytic tail overlap them without a height gap. The proof keeps the original exponent 27/164 and full range of absolute heights at least 3.

## Independent replay

The frozen scripts and parameters were copied to a separate directory and run at 192-bit precision with python-flint 0.9.0 / FLINT 3.6.0. The process exited successfully and produced scientific JSON byte-for-byte identical to the frozen output.

A separate exact rational check verified the 79-cell cover [220+20j,240+20j], j = 0,...,78, and the maximum outward rounded coefficient 48.61. The infinite-tail enclosure is

45.8215821342204498800179419844228022844470946177717283, with radius at most 3.68 times 10^-53.

Both are strictly below 49. Separate rational calculations also checked all eight dual exponent pairs, all six new finite exponents and all six corresponding tail exponents against the written formulas.

## Conclusion

The frozen proof and full replay pass this internal review. They establish the claimed coefficient 49 with the named analytic dependencies. This is a function-bound improvement, not a new exponent, an excluded-zero percentage, an RH proof or an exhaustive priority claim. The local derivative hypotheses and the complete infinite tail are mathematical premises checked in the proof, not consequences inferred merely from successful finite computation.
