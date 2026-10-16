# Independent internal review of the near-zero Littlewood refinement

Reviewed report SHA256: e60e17945156bd32fb4c577d0d2a4c488983bb64a50ec42301dfcae47326c494.

Reviewed verifier SHA256: 6625bf0dca52b05b1bcfc7115f7752ecde747c360de6b0e9f21ed6ecf50f8a56.

Date: 2026-10-16 (UTC).

The complete written proof and the new scalar verifier pass independent review. An independent 160-bit Arb replay completed successfully. The conclusion is the stated unconditional classical zero-free denominator 4.82 for absolute height at least 2, with the numerical trust base and previously proved analytic inputs explicitly retained.

## Analytic checks

For log(t) at least 76, all nonzero-harmonic near ordinates lie between t - T0 and 16t + T0 and hence above the verified low-height endpoint. The published 21.233 Littlewood theorem applies to each ordinate. The function log(v)/v is decreasing for v > e, so evaluation at log(16t + T0) supplies a common upper enclosure for both real parts beta and 1 - beta. The zero-harmonic near ordinates remain inside the verified RH range. This use is independent of the new classical region being proved and is not a circular bootstrap.

The unchanged scale eta = Ao/log(t) is positive. On every accepted cell in the new branch, the verifier checks mu <= 1, sigma >= 0.997 and eta <= 0.003, and separately verifies that these last bounds lie strictly inside the original exact rectangle. In particular sigma - 1 >= -eta remains available for the actual far-pair argument. Neither the smoothing domain nor the horizontal positivity domain is enlarged.

The exact rational packet and detector are byte-identical to the accepted dependencies. The detector-dependent Gamma and prime constants, complete remainder costs, and real-pole reserve are unchanged. The two retained zero terms are compared together by convexity of the Laplace transform; their arguments and the factor a1 agree with the complete explicit-formula normalization. The prior full-zero convergence and reflected-pair grouping are retained, not replaced by a truncated zero sum.

## Independent replay and height cover

The verifier was read in full and executed independently at its default 160-bit precision. It accepted 57,779 closed rational cells after 115,556 evaluations, with no failed or pending cell. The smallest directed scalar lower bound was greater than 3.2730292126948e-9. Both closed branches include log(t) = 76, so the change of sigma leaves no gap.

The unchanged packet hash is 0cab19992748abf3d4c80789517b9220957f356a25847785e7f1fbbb618c0cef. The unchanged detector hash is 5bce21a50b06a0eec005a6c58bd99a7e76f149d521a3588968afeaccce5e46e2.

The high-height crossover is exp(21.233/4.82) = 81.87442917246075... in the variable log(t), below the certified upper endpoint 82. The lower endpoint 28 is below log(3e12). Thus verified low heights, the complete scalar cover, and the published Littlewood region overlap and cover the asserted range. Negative heights follow by conjugation. The weaker 4.8594 seed is supplied by the already established unconditional 4.84 result, not by a conditional unpublished input.

This is an independent internal mathematical and interval-arithmetic review. It is not external peer review, a proof-assistant check, a claim about a percentage of zeros, a proof of RH, or a priority claim over unexamined external work.
