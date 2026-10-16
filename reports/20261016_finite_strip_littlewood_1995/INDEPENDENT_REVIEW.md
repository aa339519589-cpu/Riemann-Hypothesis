# Independent internal review of the finite-strip transfer

Reviewed on 2026-10-16. This is an independent internal source, proof and directed-arithmetic review, not external peer review or a claim of global priority.

## Pinned files and replay

- `REPORT.md`: SHA-256 `8b5833eefa44bc67bfe2cf855640cb9aa640f115eb1aaa8f4b840d57bcb48c58`.
- `certify_transfer.py`: SHA-256 `eb170203f08cd43b2a224a0560afc83a89f261d65a312c431f563e9d26ab7d73`.
- `certify_unsplit_hpy.py`: SHA-256 `d3c9ad62788ed945402682decc832c54fbcfec175721d46f1e460a730d41613c`.
- `interpolation_19.95.json`: SHA-256 `dac63f5cf59e774c2f7d24de07ec8a0c076277bf267d70e536505749e12deea7`.
- `interpolation_witnesses_19.95.json`: SHA-256 `b8592de64b4479860cfcd9af3ef8078060464856a06c78f92b09b12772618277`.

The complete report and both programs were read. An independent run of copies of the programs, using the official python-flint/FLINT distribution, returned PASS. The source constants were checked at 192 bits and the continuum explicitly restored 160-bit precision. It accepted 1,563 closed cells in 3,110 evaluations, with smallest directed lower margin greater than 1.48266654936e-7. The accepted modes were 208 direct HPY, 1,102 direct table and 253 discrete-k witnesses. Both scientific output files were byte-identical to the pinned files. A separate rational-endpoint check verified the gap-free cover from 64 to 1,000,000.

## Mathematical checks

1. **Source normalization.** Yang's version-pinned primary text was reopened, including the complete left/right logarithmic integrals, the exact weighted harmonic estimate (4.65), the 1.546 right-boundary theorem, and the local zero-detection inequality. The factors 1/2 in the integral and 1/(2 eta) in the local inequality are retained. Only the left-integral estimate is replaced; zero isolation, the right integral, pole, zero-count and smoothing terms remain the established complete ones.
2. **Whole strip and complete tails.** Euler summation gives the displayed uniform bound 6(1+|y|) for every real y throughout the closed strip [1/2,5/7]. Thus the tail argument does not silently use a critical-line-only bound. Both infinite tails are paid, including any passage through height zero. The resulting upper integral is less than 1e-80; logarithmic zero singularities are locally integrable and do not obstruct the upper estimate.
3. **Finite-rectangle interpolation.** The stated cosine-cosh barrier is harmonic, nonnegative on the vertical sides and at least 223 on both horizontal sides. The linear boundary envelope is nonnegative. The subharmonic maximum principle therefore proves the complete interior bound without a zero-free assumption on the rectangle. The central integral lies within distance 32 of its harmonic center; the barrier and logarithmic-center debits fit the independently checked 1e-20 reserve.
4. **Finite-height source coverage and Jensen.** The primary Patel-Yang Table 1 interval assertion was checked. One common, increasing table coefficient covers every touched interval for all 46 harmonics and the whole accepted cell. No finite row is extrapolated beyond its range. The functions G and F are increasing and concave on the used log-height range. Their common coefficients permit Jensen with the exact weighted mean debit 3.377, including log(V) on the right boundary. Positivity licenses replacing the central kernel mass by one.
5. **Directed arithmetic.** Every accepted cell checks the smoothing restrictions, R>=100 and the signs needed to replace the unknown positive minimum by its upper bound. Floating-point values only select candidate witnesses and R; the final ball inequalities, including lambda(R+1)<=eta, independently authorize acceptance. The exact cover contains no unresolved interval.
6. **Noncircular whole-height passage.** The established 4.79 theorem pays the lower range and the possible lower sliver of the minimizing-zero rectangle. The published Vinogradov-Korobov 55.241 theorem pays the high range and makes a violating positive global infimum attained. The remaining rectangle follows from that actual global minimum, not from the proposed 19.95 conclusion. The low and high splice inequalities, conjugation and retained verified-low-height input complete the all-|t|>=3 claim.

## Conclusion and scope

No mathematical correction is requested. The pinned finite-strip proof and complete certificate establish the stated Littlewood denominator 19.95 using the independently established unsplit HPY bound and the declared published inputs. This is distinct from the earlier unsuccessful global-only trial. It is a zero-free strip result, not a percentage of actual zeros, a proof of RH, or a global-priority claim.
