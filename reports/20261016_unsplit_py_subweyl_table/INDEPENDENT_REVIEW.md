# Independent internal review

The complete report, rational parameters and directed-arithmetic verifier were independently read. The finite-height sub-Weyl theorem passes this review.

Reviewed SHA-256 pins:

- `REPORT.md`: `fe7d772b667ed6d349a0235cd19913d10d05471dbb10a1307ddf51f891faabe0`.
- `certify_unsplit_py.py`: `926a2025c59e4d463ae5295ea0e73b663ceb6505445057f8fb225d77d022a29d`.
- `parameters.txt`: `f7b47ae6d87f4c20b3c5484ceb320a704d029736ac083e3766b71b6746176855`.
- `unsplit_py_bounds.json`: `d124c9cfa7702c4f8f38b98043d4959bc9bdac84868d96fa8a77f9deea97cadb`.

The explicit derivative-test recurrence, the raw transformed-phase bounds, the Poisson error and the integer A-process were checked against Patel–Yang's primary text, Sections 1.2, 2 and 3.0.1–3.0.3, together with the cited Yang derivative tests. The argument does not import the preprint's later q0 substitutions or its erroneous initial-sum factorization. The final report uses section-level derivative-test attribution, avoiding a version-dependent lemma-number mismatch.

The fifth derivative has the required monotonicity. Removing the first lattice point of each partial transformed sum permits the integer-endpoint derivative test on a subinterval wholly inside the derivative range. The cost is one before monotone-weight partial summation, and at most the maximum inverse square-root second-derivative weight afterwards. Thus the displayed change from 4.686 to 5.686 pays the endpoint issue. The two main constants remain unchanged. The full logarithmic error is retained, and empty correlations are harmless. The weighted power sums give exactly the displayed coefficients in the complete squared block bound; no termwise square-root splitting is used.

The Riemann–Siegel partition covers the entire original sum. Its middle upper block is treated as an initial partial sum, not bounded by the magnitude of an oscillatory extension. The theta3 denominator in the middle-block floor ratio is correct. All integer q and block-ratio conditions follow from the directed guards for every index up to the fixed upper counts. Extra indices are used only to enlarge positive majorants.

The normalized powers were independently recomputed: the diagonal and first main term have exponent zero, and the remaining three power rows have exponents -3/328, -27/164 and -13/123. The logarithmic row decreases after fixing its enclosing coefficients, so evaluating it at the lower log endpoint is uniform. Both middle-block exponents are negative. The initial sum and Riemann–Siegel remainders are paid in their stated directions.

An independent run from a separate copy, with 192-bit Arb arithmetic through python-flint 0.9.0 / FLINT 3.6.0, completed successfully for all 32 closed intervals. It reproduced every announced coefficient and the complete scientific JSON byte-for-byte. These are continuum bounds from the analytic monotonicity and floor enclosures, not sampled-height tests.

The conclusion is restricted to exp(60) <= t <= exp(220), with the stated row coefficients. No new global coefficient, zero-free region, critical-line proportion, or exhaustive literature-priority claim follows from this package alone.
