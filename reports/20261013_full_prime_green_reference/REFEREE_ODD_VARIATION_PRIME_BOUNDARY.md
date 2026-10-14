# Mathematical referee report: odd variation and the reflected-prime boundary

Reviewed text: [Odd Green variation and the complete reflected-prime boundary](ODD_VARIATION_PRIME_BOUNDARY.md).

## Finding

I found no blocking mathematical error in the candidate's equations (1)–(15). The argument correctly derives a necessary covariance inequality for an actual largest supercritical Green eigen-source, and it correctly limits the compact-core construction to a failure of automatic covariance positivity. The stated scope does not imply an eigenvalue exclusion, a negative Weil test, or RH.

## Checks

The spectral step uses λ as the top Green eigenvalue: then `Qδ = P − N/λ` is nonnegative on the whole actual `P`-completion, while the eigen-equation gives `h(g,z) = −δN(g,z)`. The signed, real-even convolution tests are admissible in that completion. The source tail, absolute-kernel Cauchy–Schwarz estimate, physical `L²` bound, and `H¹` smoothing supply the required cutoff approximation; even convolution also preserves the zero pole moment.

The half-line commutator kernel and its sign agree with the definition `[R_d,C] = R_dC − CR_d`. For `a < d/4`, its support is confined to the two reflected corners. Both sides of each prime boundary and both transpose corners give exactly equation (6); grouping `t` and `−t` introduces no extra factor of two. Since `d_n ≥ log 2`, this covers every prime-power label. The local `L²` translated-load theorem justifies the full sum and the convolution identity in equation (7), without endpoint point values.

The origin estimates also have the stated scale. Odd-kernel cancellation yields `||C_ag/x||₂ ≤ C_k ||g/x||₂`; the triangle estimate is `|D_pr| ≤ C_k a A_g B_g`, with `A_g ≤ C δ⁻¹√P₀` and `B_g ≤ C√P₀`. Hence `δ|D_pr| ≤ C_k aP₀`, with the depth loss canceled as claimed. The grouped weighted pairings are legitimate by weighted Cauchy–Schwarz; no integration by parts through `V(x) ~ c/x` occurs.

For the core construction, the pole-centering coefficient is exact, the cutoff limit `b_R(r) → 2/3` is consistent with the half-Gaussian moments, and the `V = c/x + O(1)` scaling gives the leading `c r⁻² J_{1/t}` term. The support condition removes the reflected off-diagonal products for all `d_n ≥ log 2`, but correctly leaves the complete diagonal `V`, including every Mangoldt label. The constructed source is explicitly independent of the eigen-equation, so its negative variation is not an eigen-source obstruction and does not assert a negative Weil form.

I reran the exact rational-coefficient script. It returns `J_{1/t}(f_b) = 2b² − 2b − 2` and `J_{1/t}(f_{2/3}) = −22/9`. This verifies the algebraic coefficient only; it does not verify the analytic cutoff argument or any spectral conclusion.

This is a model-assisted mathematical review, not Lean verification or human peer review.
