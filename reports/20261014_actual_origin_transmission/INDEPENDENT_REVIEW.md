# Independent mathematical review

The reviewed `REPORT.md` has SHA-256
`5dc721d7d915612e9ea11adab57502425c082bf5aeaeaf05c2ce994ddfb9e202`.
The input source realization and fixed-depth bootstrap are those at commit
`675b83e872ce91ec31f9deab7f98516208faf78b`.

## Scope and conclusion

The proof is correct for an actual scalar, pole-centered supercritical Green source at fixed positive spectral depth. It proves the origin ratio trace, its complete arithmetic averaging identity, a genuine first derivative of the odd source at zero, and the stated higher-order bound for the complete prime collar. Its estimates are not asserted uniformly as the depth tends to zero. It proves neither a full covariance sign nor exclusion of a supercritical source.

## Checks

1. The weighted Sobolev passage uses a strict exponent gap: local uniform H^q control with s<q<1 is interpolated with the actual double-exponential L2 tail. This pays every fixed exponential spatial weight. The central Lipschitz weight is admissible because s<1.

2. The complete translated load series converges absolutely in H^s near zero: extracting the n^(-1) weight leaves the convergent sum of Lambda(n)n^(-3/2). No prime powers are omitted. For s>1/2 the resulting continuous representatives and their Holder bounds justify the individual point evaluations and their absolutely convergent sum.

3. The logarithmic Gamma multiplier maps the known H^q source into H^s for q>s. Its odd continuous representative vanishes at zero. The exact local source equation therefore gives L(0)r(0)=sum alpha_n g(log n), with the common positive depth factor cancelling. Division by the smooth positive L also supplies the stated H^s regularity of the ratio. The arithmetic average has total weight one and converges absolutely even though no unweighted uniform bound on the ratio at infinity is assumed.

4. The expansion g_o(x)=psi'(0)r(0)x+O(|x|^(1+alpha)) follows for every alpha<1/2. It proves differentiability at this one point, not a derivative trace at every prime knot or a global H^1 endpoint.

5. For smooth even mass-one masks, the constant-load times linear-source contribution cancels exactly. The remaining integrand has order t^(1+alpha); the triangular area and kernel scale give t^(2+alpha). Signed profiles are allowed with profile-dependent constants. The arithmetic trace determines the linear coefficient, while the elementary constant-linear cancellation itself is a consequence of even convolution, not a positivity argument.

6. The raw line formula retains its factor 1/2 and both complete-load evaluations. The new every-fixed-translation P-norm continuity extends the previously almost-everywhere identity to every sufficiently small fixed parameter. The same cancellation then proves the stated a^(2+alpha) bound.

The potential covariance, its prime-knot terms, the full Gamma contribution, and the pole payment remain part of the unresolved signed comparison. The report explicitly preserves these limitations.
