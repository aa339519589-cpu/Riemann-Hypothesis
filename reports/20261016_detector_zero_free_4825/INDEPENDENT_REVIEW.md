# Independent internal review of the detector refinement

Reviewed report SHA256: c14df353ad87082fb354c0b950acf3d651b0f165c18a27890ac1fe7be56d6f4c.

Reviewed exact detector SHA256: 5bce21a50b06a0eec005a6c58bd99a7e76f149d521a3588968afeaccce5e46e2.

Date: 2026-10-16 (UTC).

The complete written theorem and all three new certificate scripts pass independent review and replay. The result is the unconditional classical denominator 4.825 for absolute height at least 2, using the previously established 4.84 theorem and the published 21.233 Littlewood-region input.

## Changed mathematical inputs

The exact degree-16 Chebyshev polynomial has no root on [-1,1] and positive value at zero. Its Fourier coefficients are nonnegative and its constant coefficient equals one. Thus the full nonnegative detector argument remains valid; neither grid sampling nor positivity of the smoothing packet substitutes for this separate check.

The new a1 isolated-zero factor and the sum A of nonzero-harmonic coefficients are used consistently. Every detector-dependent term is recomputed: the retained four-prime packet, all signed zero-harmonic Gamma terms, the nonzero-harmonic Gamma constants, and both summed remainder coefficients. The maximum harmonic remains 16, so the near-zero enclosure and the log(k) error bounds are unchanged. The prior nonzero-harmonic real-pole estimate depends on A through a common upper bound; therefore the checked A <= old A inequality is sufficient, without a componentwise comparison of detector coefficients.

The smoothing packet, common-d paired-transform positivity, complete zero-pair convergence and grouping, and both-root convexity are unchanged from the base proof. The unconditional 4.84 theorem supplies the weaker 4.8594 seed; no conditional thesis input enters this argument.

## Independent replay

The three scripts were separately read and executed at their stated outward precision. The prime script additionally checks the exact detector and smoothing-polynomial positivity assertions.

- The complete prime phase covers give a logarithm-weighted lower bound greater than 0.21623176310627268, hence the retained coefficient 0.216.
- The signed Gamma certificate gives a worst upper constant below -1.5594484600604, hence -1.559.
- The full absolute remainder sums are below 104 eta^2 + 6037 eta^3.
- The scalar certificate accepts all 50,967 closed rational cells covering [28,81.51], after 101,933 evaluations, with no failed or pending cell. Its smallest directed lower bound exceeds 2.655216005e-9. The published-Littlewood crossover is 81.5015274393..., below 81.51.

The verifier hashes are:

- Gamma: 74a916f3950b9a3070da970785005e7d6ef2330a523eba2e2b23703d0a52ee9d.
- Prime: 38360b8e166be6e8b776ee7bdfff795f025564d0e4d46ab407509172c9f80490.
- Scalar: c4adfdf114438ed721d4fe31daead29c6cb60944f49798258f74cb00337dd3de.

The packet remains byte-identical to the base packet, SHA256 0cab19992748abf3d4c80789517b9220957f356a25847785e7f1fbbb618c0cef. The low-height, finite-height and high-height ranges overlap as claimed, and negative heights follow by conjugation.

This is a complete internal mathematical and interval-arithmetic check of the stated refinement, not external peer review, formal proof-assistant verification, a percentage of zeros, or RH. It does not establish priority over unexamined external work. The numerical trust base remains the exact arithmetic and outward Arb/FLINT implementation stated in the base package.
