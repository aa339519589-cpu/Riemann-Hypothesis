# Independent internal review

## Frozen proof and certificate

- `REPORT.md`: `35d5299710c4b57864c6f798c04e9751c087e9273a685d0abb6a30309410c860`.
- `certify_exponent.py`: `930b721bb9cea88580e04c880c4a6797cc53dc62b7c67bd21afb2ae8e3e43883`.
- `extra_dual_exponent_77_468.json`: `e0b414907f0783e74a72874b3bdac5205d61498341f3396c2219fe9d549b20c1`.

The complete proof and verifier were read. Patel–Yang's primary Lemmas 1.2, 1.4 and 2.3, the complete first-Poisson estimates and Riemann–Siegel normalization were reopened and checked. The finite unsplit-PY endpoint repair and the independently reviewed global coefficient-49 dependency were retained. This is an independent internal review, not external peer review.

## Analytic checks

1. Both arguments of each first correlation remain in its original block. This gives the exact lower and upper dual endpoints and justifies the containing interval [N,h squared N]. The Stieltjes representation is correct. Its differentiated density comparison gives the stated beta-integral ratio and uniform relative derivative loss.
2. The negative triple difference has the specified positive scale and alternating derivatives. All four lower ratios were checked independently as exact rational inequalities after squaring. Both Legendre numerator upper bounds were independently recomputed and are strictly negative. The second Poisson formula is applied to the negated triple-difference phase, as required by the primary source's decreasing-derivative convention; the transformed fourth derivative and its monotonicity retain the same absolute scales.
3. The complete second dual length, inverse-square-root weight and fourth-derivative ratio give both main terms in (9). The two power errors, logarithmic error and constant term are retained. Removing the first lattice point pays the integer-endpoint test on every partial dual sum, including a dual interval shorter than one. Monotonicity of each positive Poisson weight permits a single maximum-weight factor in partial summation.
4. The three A-process lengths K, K squared and K to the fourth have the correct diagonal coefficients. Their weighted sums have mass at most one, so the stated Jensen steps are lawful. The product-shift averages include every positive label. Negative powers retain the lower floor estimate rather than the upper one. An independent exact rational computation recovered all four C,N power pairs in (15) and their returned first-dual pairs in (17).
5. The condition on N times C to the fourth gives the full shift guard, not just a typical shift. The outer floor bounds give the independent epsilon-times-argument guard throughout every nonempty correlation. Both guards remain valid on partial sums. The good range implies N greater than one, and C is bounded by t to the three-quarters power, which pays the entire growing second-Poisson logarithm.
6. The bad range kappa less than two is bounded by the complete first-dual length plus its lattice-point debit. Its explicit R0 and both additional outer rows were rederived. No favorable probability or small-correlation subset is omitted. The first-Poisson power and logarithmic errors remain present on both ranges.
7. The outer A-process, weighted block normalization and full geometric sums use the correct floor direction for each sign of the block exponent. In particular the second-Poisson endpoint row has negative block exponent; its complete lower-endpoint sum is needed. Its normalized height exponent is minus 1/6552 at the new three-sevenths cutoff, so it decreases. The other rational height exponents are nonpositive. Both growing logarithmic factors have separately proved monotonic products with their exponential decay.
8. The initial and middle sums form a complete partition with the large blocks. The shortened top middle block is retained. Both Riemann–Siegel halves and both explicit remainder terms are included. Below exp(5800), the independently established coefficient-49 bound gives the displayed all-height splice; this is not a sampled-height assertion.

## Independent directed replay

A separate copy of the frozen verifier was run at 192-bit Arb precision. It terminated with PASS. The generated scientific JSON is byte-for-byte identical to the frozen result.

The complete analytic upper bound for every height at or above exp(5800) is enclosed by

    87.7186671713687219366872945325269898382939895355068241

with radius less than 8.35 times 10 to the minus 53. The old-bound splice is enclosed by

    89.6904955354121535524704429124930461147188691946095384

with radius less than 6.46 times 10 to the minus 53. Both are strictly below 90. The certificate checks the uniform guards, the full geometric tails, all height-exponent signs and both splice sides. No finite sample is substituted for the infinite-height inequalities.

## Finding and scope

The pinned proof and directed certificate pass for the explicit bound 90 times |t| to the power 77/468, for every |t| at least 3. The exponent difference from 27/164 is exactly 1/9594; its coefficient is larger, so the useful bound retains the minimum with the earlier coefficient-49 theorem.

This is a checked comparison with the stated explicit dependency, not a claim to the best known unrestricted asymptotic zeta exponent or exhaustive literature priority. The formal exponent-pair word alone is not used as proof. No zero-free-region transfer, zero-density consequence, critical-line proportion or Riemann-hypothesis conclusion is accepted by this review.
