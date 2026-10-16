# Independent internal review

Reviewed on 2026-10-16. This is an independent internal source, proof and directed-arithmetic review, not external peer review or an exhaustive priority claim.

## Pinned proof and verifier

- `REPORT.md`: SHA-256 `7fd8ccb9809b3f7d99e1268a79de47cf2d5796b6a2d38785e94c2482820efabf`.
- `certify_blockwise_hpy.py`: SHA-256 `ed57986d7da753366da6312504bda463aaa3226e02e2573ffe7647c07247dead`.

The entire report and verifier were read. The primary version-pinned Hiary-Patel-Yang paper was reopened, including Lemmas 2.1, 2.5 and 2.6 and equations (3.2), (3.5)--(3.11), and (3.16)--(3.25). An independent 192-bit run of a copied verifier returned PASS, with scientific JSON byte-identical to the author's output.

## Checks

1. The source derivative lemma allows every positive epsilon and retains the actual block index r. With K>=K0 and W>=pi(r+1)^3, the displayed block-dependent alpha_r and beta_r are lawful upper bounds. No source hypothesis forces them to be frozen at r0. The fixed choices r0=3, epsilon=7/5 and T=exp(50) satisfy the source domain.
2. All factors in alpha_r, beta_r and kappa_r have the asserted monotonicity. This proves the infinite-tail inequality analytically, independently of the finite numerical monotonicity tests. The continuous floor bound exceeds 1658.7043, so the whole finite prefix through r=999 is present.
3. The four complete terms of the source block radicand are retained. The common beta_3 bound is used only in the separate d-squared term; the other terms retain kappa_r. The remainder sqrt(kappa²g²+d²)-kappa*g decreases in kappa. This gives precisely the nonnegative finite correction S and the common unsplit remainder for all blocks.
4. The unsplit integral retains its upper endpoint R+3/2. The harmonic sum, its negative omega term, all small blocks, and the Riemann-Siegel remainder have the correct normalization. No negative term is independently replaced in an unsafe direction. The elementary integer-sum bound gives I<=-2.
5. The independent run evaluates every one of the 997 prefix corrections and obtains b1<0.403113946755, b2<3.239451590250, and b3<-1.99999448. Upward rounding to 0.40312 and 3.240, followed by discarding the negative b3, proves the displayed bound uniformly for every t>=exp(50). The numerical endpoint check is used only for explicitly proved monotone bounds, not as a substitute for the infinite-height argument.

## Conclusion

No mathematical correction is requested. The pinned files prove the standalone bound

|zeta(1/2+it)| <= (0.40312 log(t)+3.240)t^(1/6), for t>=exp(50).

This improves the preceding standalone bound throughout the stated common range. No new zero-free-region transfer, percentage of zeros, RH conclusion or global-priority claim is inferred here.
