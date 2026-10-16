# Independent internal review

16 October 2026. The complete written proof and both arithmetic source files were read independently. A separate 192-bit replay completed successfully; this is an internal mathematical and computational cross-check, not external peer review.

## Frozen inputs

- `REPORT.md`: `6dde88f25b7006f7aaa9e13156cf334d22baad078ff2db2cae6a1e6d7bafe879`.
- `certify_global.py`: `87a28db4275e40be79a6be74427e4b23a490e6424d13329d27cd43b203b38245`.
- `adaptive_block.py`: `94b78fae8b6ca77de45ecb6e6af09fcd9d2fecfb53d6544f65dd9930f533fc33`.
- `parameters.txt`: `2e541eb475b3b98b0173778293fd13a4ec934bc9cc8d2ffec5ce2a5ed7d9e5ae`.
- `global_subweyl_57.json`: `9031b869066609da2300d89bbf7b94e94aee9c032d8a5e8ca80dbe92ff805bb9`.

## Analytic checks

The change from the accepted raw-block lemma is lawful: each block may choose its own positive, cell-fixed theta and integer q. No step of the derivative test, Poisson summation or partial summation requires equal q in different blocks. Within a block the same q is retained for every partial sum. The first-dual-lattice-point repair remains present through E4=5.686 sqrt(pi) h^(3/2).

The explicit theta rule is a definition, not an unproved numerical optimality assertion. For every block the lower floor enclosure Q-minus is positive and the upper q/a enclosure is less than one. Since q is an integer these inequalities give 1 <= q <= a. The upper partition counts, positive A-minus, endpoint ordering, and 1<h,h3<2 are all checked. Additional positive terms for nonexisting blocks only enlarge the upper bound.

Every row of the unsplit normalized square root is retained, including both derivative-test terms, the repaired Poisson endpoint row, the cubic error and the entire logarithmic error. The logarithmic row decreases in log t because its bracket derivative is at most (5/pi)(7/41), while its bracket is at least 6 and 6(27/82) exceeds that derivative bound. Thus its left-cell evaluation is lawful. The initial, finite middle, truncated top middle and Riemann--Siegel rows remain unchanged from the checked dependency.

The infinite tail is separately proved with fixed parameters, not extrapolated from the finite adaptive rule. The uniform q0 and p0 implications, lower floor comparison, positive- and negative-power geometric sums, and all height exponents were rechecked. In particular the secondary normalized exponent is exactly zero; the other displayed error exponents are negative. The full logarithmic row is paid by a constant times x^(3/2) exp(-27x/164), decreasing for x>=1800. The initial and middle sums and both Riemann--Siegel terms are included.

The low-height splice uses the published .618 Weyl bound on [3,exp(60)], whose normalized upper is below 41.890, and the accepted 32-row finite table on [exp(60),exp(220)], whose maximum is 46.49. The four ranges are closed and overlap at their endpoints.

## Independent replay

The verifier and block module were copied into a separate replay directory and run with python-flint 0.9.0 / FLINT 3.6.0 at 192 bits. It completed with exit code zero. All 79 closed cells passed, with maximum outward-rounded coefficient 56.42. The infinite-tail enclosure was

    54.4508231534270621010361225603757317976884101363741865 +/- 4.28e-53,

strictly below 57. The generated scientific JSON is byte-identical to the frozen output. Its exact consecutive endpoints were also checked separately: the cells are precisely [220+20j,240+20j], 0<=j<=78, covering [220,1800] without gaps.

## Conclusion and scope

The proof and directed computation support |zeta(1/2+it)| <= 57 |t|^(27/164) for all |t|>=3, with the stated previously checked dependencies. This improves the global coefficient at the same exponent and range. It is not a percentage of zeros excluded, a new critical-line proportion, an RH proof, or an exhaustive priority claim. No mathematical correction is requested.
