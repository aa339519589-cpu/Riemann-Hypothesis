# Independent mathematical and computational review

This review concerns `REPORT.md`, SHA-256
`ca74a07aae5b6a1700ac0c58288272ec705e53915b50a67fb86ba6f90406aba9`,
and `certify_littlewood.py`, SHA-256
`8dd51a87754ac1d49010ad097f4a57c6875dcc778d75aec6648ade46beb727e9`.

The entire report and verifier were independently read. A separate copy of the verifier was executed at 160-bit precision. It returned PASS on all 1,875 closed rational cells after 3,734 evaluations, with smallest directed margin greater than
`5.6155751765810217821539343467110561291190481386e-8`.

The following points were checked.

1. The two complete local inequalities agree with Yang's version-pinned primary paper, Lemma 4.8 and equation (4.125). The latter uses Lemmas 4.3 and 4.6, whose hypotheses allow the stated lower height; it does not inherit an artificial height restriction from Yang's later parameter choice. The subsidiary `t >= 2^k` condition is satisfied for every witness. The local-zero-count term can be discarded because its coefficient is bounded above by `4(c-1/R)-c/eta^2 < 0` when `eta <= 1/2`.
2. The outward bounds on the fixed detector coefficients are used only after positivity of their multiplying brackets is certified. The smoothing constants are those of the published detector. The theta enclosure and the positive-factor bound `c(R) <= 1 + 10.05/R`, for `R >= 100`, agree with the exact formulas (4.50), (4.53), and (4.58)-(4.60).
3. A hypothetical violating zero produces an attained positive global minimum of the normalized zero distance. The published Vinogradov-Korobov region excludes all smaller values beyond the finite certified height range. The resulting lambda pays the complete rectangle through ordinate `46t+1`; the small sliver below `exp(65)` is separately paid by the unconditional classical denominator 4.82.
4. Every accepted cell checks the smoothing scale, zero-distance and coefficient-sign hypotheses over the entire interval. Floating-point operations only propose witnesses. Rational endpoints and outward Arb arithmetic decide acceptance. Recursive bisection preserves the initial complete cover, and the program fails if any cell remains unresolved.
5. The left-side ratio loss is retained. Monotonic comparison from the actual minimum to `M1=1/20.4` has the stated direction because all relevant right-side coefficients are nonnegative. The harmless relative slack is not used to assume attainment or a zero-free rectangle.
6. The low-height comparison `4.82 log(65) < 20.4` and the high-height comparison with the published denominator 55.241 both have the correct direction. The latter extends to every larger height by monotonicity of `x/(log x)^4`. Conjugation covers negative ordinates.

The proof and independent replay support the stated unconditional zero-free region for every `|t| >= 3`, subject to the explicitly cited published analytic inputs and the previously reviewed unconditional 4.82 result. No unpublished 19.62 estimate, zero-density conclusion, percentage of zeros, or claim of RH is used or inferred. The numerical improvement is a comparison of strip widths, not a global priority claim.
