# Self-audit of exact theta-translation escape and compressed prime-edge spectrum

Date 2026-10-12. This is an internal check of REPORT.md, NOT an external referee review, formal proof assistant certificate, or a proof of RH.

## Analytic dependencies checked

1. The original real-even normalization m²=Φ/(2cosh(x/2)), Uq=√(2Φ cosh(x/2))q implies mUq=Φq. The critical source is Φ^(2r)-4^(-r)Φ, consistent with the fifth-round full-prime source equation and its operator-domain claim. The present theorem inherits that domain claim; it does not independently reprove the full closed-operator realization.
2. The first theta mode gives Φ(x)~4π²e^(9x/2)e^(-πe^(2x)); the factor 2cosh(x/2)~e^(x/2) gives m(x)~2πe^(2x)e^(-(π/2)e^(2x)). This supplies the powers 5/2 and 9t/2 and the *sign* of c_t=π(e^(-2t)-1/2).
3. Squaring v_t and doubling the positive half-line, followed by r=e^(2x), leaves the gamma integral ∫r^(3/2)e^(-2c_t r)dr. Its value is Γ(5/2)(2c_t)^(-5/2), leading to the exact coefficient 4π²·2^(-9/2)·Γ(5/2)·(2π)^(-5/2)=3/128. In particular this is a **squared** L² norm singularity, not the norm itself.
4. The L² Taylor disk proof does not translate an unbounded operator by a complex parameter. It uses the genuine theta analyticity, uniform source/m tail comparison, and closedness of ker H after norm convergence of the derivative-mode series. The elementary Re exp(z) disk inequality holds for |z|≤log 2 via sin u≤u, cos u≥1-u²/2 and log2<3/4.
5. For the edge expression, both m(x-d)/m(x) and m(x+d)/m(x) are retained. At t=a* the slowest squared source tail has exponent -πe^(2|x|); after multiplying by the larger m-ratio the remaining exponent is -π(1+e^(-2d))e^(2|x|)/2, still strictly negative. This verifies dominated convergence at the non-L² endpoint.
6. The essential-spectrum claim applies to **P_(ker H) Q_(d,alpha)|_(ker H)**, NOT to Q acting invariantly on ker H. The weakly-null normalized vectors and vanishing positive Rayleigh quotient imply vanishing operator norm images by ||Tu||²≤||T||⟨u,Tu⟩. Its kernel is zero since a nonzero d-periodic L² function is impossible. This proves that zero is in the essential, not point, spectrum of the compression.
7. The nonclosed-range statement is about M_m restricted to the genuine exact H-kernel, not about a Bombieri map or an arbitrary full-space multiplier. Normalized vectors have source norms of order (a*-t)^(5/4) and no uniform inverse bound exists.

## Executed independent sanity check

The attached check_translation_numerics.py ran with Python 3.13.5 and mpmath 1.3.0, using 8 true theta modes and finite quadrature ranges. Its actual JSON output is numerical_sanity.json. Scaled squared norms at t=.3400, .3450, .3465 were approximately .02704907941464029, .025203668925383806, and .023817425811752168, converging toward the predicted 3/128=.0234375. The unnormalized n=2 edge energies were approximately .713611, .758093, .771869, remaining finite while the L² norm diverges.

These floating quadratures do NOT prove the complete infinite theta remainder, infinite-domain estimates, strict form-domain inheritance or the essential-spectrum theorem. Their role is solely independent exponent/normalization sanity checking. The mathematical claims rest on the explicit analytic estimates in REPORT.md.

## Limits

No subcritical eigenstate was excluded, and neither RH nor E>=Var/2 was proved. The exact translation boundary is a structural property of true zero modes; it cannot be silently extrapolated into a lower bound on the orthogonal complement. No claim of literature priority or external acceptance is made.
