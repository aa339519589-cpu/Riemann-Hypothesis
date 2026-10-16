# Independent internal mathematical review

Reviewed report SHA256:

`6dd94c8dce588007e2fb36edaf9e6d99305681c3c26b6c5666dc99f15b586253`

Date: 2026-10-16 (UTC).

## Result and scope

The complete written proof and its finite certificates pass this independent internal review. The unconditional conclusion is the classical zero-free region with denominator 4.84 for absolute height at least 2. The 4.795 conclusion is separately conditional on the stated 19.62 Littlewood-region input. Neither conclusion is RH, a critical-line proportion, or a count of excluded zeros. The comparison is with the explicitly identified 4.896 classical baseline; no priority assertion is made against unexamined external claims.

## Analytic checks

1. The compact seed is nonnegative and decreasing by its explicit symmetric-decreasing convolution construction. The exact rational packet has the required positivity and monotonicity, and the common factor d in all shifted denominators permits the stated rescaling before sign separation. The paired rational boundary inequality, rather than sampled positivity, is certified on its entire half-line.
2. The explicit-formula normalization distinguishes f(0) = kappa eta w(0) from the prefactor eta w(0) multiplying the signed shifted Gamma sum. The compact-source remainder is applied to the unmodulated seed before the finite signed shifts are combined; it is not incorrectly applied to a modulated function with nonzero derivative at zero.
3. The full Gamma bounds use the absolute coefficient sum where errors are unsigned. The source's problematic intermediate integral and rectangle bounds are not imported: the replacement integral, derivative, height-zero and nonzero-harmonic estimates were independently checked. The printed final numerical Lemma 14 is not used.
4. The finite-prime lower bound retains the actual seed weights, all powers in the selected packet, and nonnegativity of omitted terms. The complete four-prime interval certificates and their monotone rectangle comparison were checked.
5. The zero-pair argument retains both functional-equation partners, including the half-weight convention for self-pairs. The scale eta is fixed by the previously established region, not identified with the hypothetical zero's distance from one. Convexity of the real Laplace transform gives the stated endpoint comparison for the two retained roots. The actual paired high-ordinate asymptotic has a positive leading coefficient; no positivity of its individual summands is asserted.
6. Grouping the zero terms is legitimate: their real parts have an absolutely summable quadratic ordinate bound, so finite grouped cuts pass to the full sum. The nonzero-harmonic pole estimate is a real-part estimate, not an unsupported inference from a complex modulus.
7. The finite-height scalar inequality has the correct trigonometric coefficient and all error debits. The low-height RH input, closed interval covers, and Littlewood crossover overlap. The extension from height 3 to height 2 uses the verified RH range and a boundary strictly to the right of one half. Negative heights follow by conjugation.

## Independent computation and final package checks

The exact packet/Sturm certificate, replacement analytic constants, full finite-prime interval certificate, signed Gamma certificate, zero-pair and pole estimates, and both full-height Arb covers were independently read and replayed during this review. The unconditional cover accepted 27,071 closed cells on [28,81], with directed lower margin exceeding 1.4544e-7. The conditional cover accepted 26,396 closed cells on [28,61], with directed lower margin exceeding 2.0710e-8. These are whole-cell interval enclosures, not grid samples.

The final portable scripts were compared with the reviewed mathematical calculations. Their final serialization changes replace the packet path by its basename and remove timing metadata without changing arithmetic. The final runner explicitly checks the generated scalar status fields, in addition to subprocess completion. The package's full seven-script replay also passed after these changes. Its SHA256SUMS pins the report, scripts, exact inputs and mathematical outputs; this review is an additional file rather than an alteration of those pinned calculations.

The numerical trust base is the stated exact rational arithmetic and outward Arb/FLINT arithmetic, together with the ordinary software and hardware assumptions. This is not a Lean formalization or an integer-only verification of every analytic theorem.

## Primary-source verification

The 4.896 input was checked against Bellotti--Trudgian--Yang, arXiv:2603.21490v1, Theorem 1, and the relevant compact-source lemmas. Yang's version-pinned arXiv:2301.03165v2 has the title *Explicit bounds on zeta(s) in the critical strip and a zero-free region* and explicitly states the unconditional 21.233 constant. The cited publisher metadata matches that title, JMAA 534(2), article 128124, DOI 10.1016/j.jmaa.2024.128124. The Platt--Trudgian verified-height input was also checked. The separate 19.62 thesis input has not been verified as an unconditional published theorem and remains a hypothesis.

These checks support release of the stated theorem and reproducible certificates. They do not replace external peer review.
