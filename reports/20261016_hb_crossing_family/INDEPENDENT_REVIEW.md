# Independent internal review

Reviewed on 2026-10-16. This is an independent internal mathematical and certificate review, not external peer review or a claim of exhaustive literature priority.

## Pinned files

- `REPORT.md`: SHA-256 `4726f28b59e5633a35563c59fa395c411c7120a5247fb78e6962503d3f8fc2a3`.
- `check_certificate.py`: SHA-256 `3801bbbd1b9159f34c31a98c5ae8f48c40bfa583d12d3c0effe6d8bc542a23d6`.

The complete report and checker were read. The standard-library rational checker was independently executed and returned PASS for both complete parameter windows, their table comparisons, and the exact example exponents.

## Checks

1. The analytic input is the scale-general large-values inequality proved in Section 2 of the preceding crossing report. Its proof is for every fixed positive integer k, not only the earlier k=3 specialization. The present report introduces no unproved extension of that input.
2. The crossing formulas for t_k, v_k, alpha_k and tau_k are correct. Since alpha_k>0, E_k=3(1-sigma)/tau_k is less than one. Mean value pays the interval up to tau=1; the two affine branches are controlled at both endpoints of [1,t_k]; subdivision pays [t_k,tau_k]. Thus the complete required length window is covered, not only its corner values.
3. The author-maintained primary blueprint's Corollary 11.9 was reopened. Its hypotheses match this linear-window argument, and the zeta-polynomial interval is empty because tau_k<3/2. No Montgomery-prefix premise from Corollary 11.10 is substituted.
4. Every stated interval premise is affine in sigma and is verified at both rational endpoints. Equality v_k=2(1-sigma) at the upper endpoints is harmless. The exponent formulation and choice of sufficiently small input losses justify every fixed positive final epsilon, without a uniform-in-sigma constant or a loss-free endpoint claim.
5. Table 11.1 and Proposition 11.37 were reopened. The k=4 and k=5 comparisons retain the upper-end table changes and the k=5 join at 19/25. The separate Kerr expression is explicitly an unpublished-preprint comparator, not an input. The exact sample exponents and differences agree with the report.

## Conclusion and scope

No mathematical correction is requested. The pinned files establish the two stated asymptotic zero-density corollaries and their declared comparisons. They do not certify a finite-height zero exclusion, a percentage of actual zeros, an explicit implied constant, RH, or an exhaustive global novelty claim.
