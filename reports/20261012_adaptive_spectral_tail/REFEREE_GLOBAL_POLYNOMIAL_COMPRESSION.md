# Independent review: global even-polynomial compression and actual budgets

Status: approved as an approximation-space improvement and a parameter/norm-tail certificate. No resolvent Gram entry, inertia condition or new gap is certified.

Reviewed mathematical manuscript: [GLOBAL_POLYNOMIAL_COMPRESSION.md](GLOBAL_POLYNOMIAL_COMPRESSION.md).
Reviewed executable: [certify_global_polynomial_budgets.py](certify_global_polynomial_budgets.py), SHA-256 `e29ff95b4231c295f88185f49d613936ead21e588f68f83e5d48b5328343e40d`.
Author output: [global_polynomial_budgets.json](global_polynomial_budgets.json), SHA-256 `19b3cba734ff4bf454116c8c37d6e80fd3d189da139373e8ac759b699c6612c4`.
I read the full proof and code and independently reran all parameter candidates. The four displayed budgets were reproduced with all assertions passing.

## 1. Whole-interval Taylor remainder and rank

QJ has actual Fourier support in [-2T,2T] and preserves evenness. The Taylor polynomial at zero through order 2r-1 has no odd terms, so it belongs to the r-dimensional even-polynomial space specified in the manuscript. The integral remainder on [0,R] is a Volterra convolution whose L1 kernel norm is R^{2r}/(2r)!. Young's inequality, even reflection and the exact band-limited derivative estimate give beta_r M=(2TR)^{2r}M/(2r)!. Orthogonal best approximation can only decrease the error. No derivative estimate for a moving trial polynomial or high-order Poisson input is needed.

The basis, extended by zero outside the spatial interval, is only required to lie in L2; no false operator-domain assertion is made about the basis discontinuity at the endpoints. Actual resolvent right sides remain m Q e_i and graph-core trial vectors are handled as in the preceding theorem.

Replacing the cell error by beta_r M in the already proved three-term full norm bound is valid. The factorial bound q!>=(q/e)^q gives beta_r<=2^{-2r} whenever 2r>=4eTR, so the displayed maximum condition is sufficient. This produces O(TR+log_+(c_N M^2/eta)) rank, rather than a product of cell count and degree. The signed finite-matrix and true-Gram requirements are unchanged.

## 2. Full Gamma lower bound and directed parameter selection

For fixed t, the summand (t/2)^2/[a(a^2+(t/2)^2)] is nonnegative and decreasing for a>0. The tail after j=31 is therefore bounded below by its integral from a=32+1/4 to infinity, equal to one half log(1+(t/[2(32+1/4)])^2). Thus (4) is a lower bound for the COMPLETE Gamma symbol. It does not replace that symbol in the operator.

The code evaluates the exact prime-power weights, complete omitted-prime envelope and fixed positive base conditions with outward intervals. The source norm square is upper-enclosed and rounded UP to an integer. The spatial radii are exact hundredths and the exact theta exterior envelope is decreasing on these nonnegative radii. Every tested T is accepted only after its lower-enclosed Gamma value exceeds the upper-enclosed required threshold.

The factorial remainder is evaluated with interval log and logGamma. The binary search begins at 2r>=2TR, where the consecutive-even-order remainder ratio is below one, so searching for a sufficient order is legitimate. More importantly, the selected remainder and the complete final norm-tail expression are independently reevaluated as intervals; the final strict test against eta does not rely on search heuristics. Endpoint transport uses higher precision than interval endpoints. All data deciding acceptance come from directed intervals, not the formatted decimal strings.

## 3. Independently reproduced scope

The four actual ranks are 373, 517, 858 and 17332 at depths epsilon=1/8,1/64,1/1024,1/1048576 respectively, with eta=epsilon/4. The corresponding complete norm-tail upper enclosures are below 0.01085, 0.001551, 0.00009273 and 0.00000009567 respectively. Each is strictly below its own eta. These decimal summaries are weaker than the successful exact interval comparisons.

The finite dense symmetric entry counts follow from r(r+1)/2 and are bookkeeping, not estimates of numerical conditioning, time or certified precision. The script certifies parameters and the full approximation error only. It neither solves the changed-base resolvent systems nor bounds the second eigenvalue of the resulting signed matrix. In particular the rank-373 budget is not a second proof that this new Gram has the sign needed for a three-eighths gap.
