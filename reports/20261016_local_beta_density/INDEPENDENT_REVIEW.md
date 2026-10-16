# Independent internal review

Report SHA256: e6e7df901d56043a2bda03dae0f34fbb2449cfc6f151c11d18c5a58f3b1273e9.

Certificate SHA256: fb210c4af4455024c611590270a5d98fdba97c12512ae1d64880a96911d2195e.

Date: 2026-10-16 (UTC).

The complete report and standard-library exact-arithmetic certificate pass independent review and replay. The stated result is an unconditional asymptotic density bound on the fixed interval 0.9355 <= sigma <= 0.936.

## Analytic and algebraic checks

1. The two local Huxley rows and their complete validity intervals were checked against Theorem 4.16 and Table 4.2 of the cited exponential-sum chapter. The second row is valid through 156527/370694, not merely to the smaller endpoint where it stops being the displayed best envelope. The two global affine bounds used outside those local intervals come from genuine exponent pairs and their global duality statement.

2. The A-process proof controls its whole supremum. The supporting ray beta(z) <= C z - 1 covers every z from z0 to 1. The exact positive margin at z = 21/50 pays the global final segment. The transformations, both image intervals, balance identity, and competing 2h term were checked independently. No local beta row is asserted to be a global exponent pair.

3. The Montgomery argument controls the complete interval of frequencies required by its supremum, and the zeta argument controls all 2 <= tau < Z. The adjacent transformed row and the global final bound genuinely fill the intervening ranges. The strict endpoint inequalities and the positive margin M + eta - 3Z/4 hold throughout the closed eta interval.

4. The subdivision conversion is applied with fixed tau0 = 3Z/4 - d. The general-coefficient interval ends at tau0 - eta, and the zeta interval ends below Z. The subsequent fixed-d and epsilon passage does not assume uniform implied constants as d tends to zero. The small left shift in sigma is paid by the strict margins.

5. All stated table and preceding-report comparisons were checked by exact rational cross multiplication. The stronger comparison remains limited to the declared supplied growth family. Its finite vertices, convex interpolation, initial Heath-Brown cases n=3,4,5,6, infinite tail, curved bounds, and reflected bounds are covered. The proof does not give a lower bound for the unknown true growth function. The separate cases for the ceiling in Pintz's formula are valid even if supplied constants are enlarged.

The independent certificate run printed PASS for the complete A-process/density transfer and for the declared-growth comparison. At sigma = 117/125 it reproduced the exponent 15712/203289 and the saving 1692704/1998127581 against the preceding corollary.

The review confirms the stated mathematical specialization and its bounded comparisons. It is not external peer review, formal proof-assistant verification, a worldwide priority claim, a finite-height zero certificate, a percentage of zeros, or RH. The cited analytic theorems remain inputs; exact arithmetic verifies the supplied transformations and ranges rather than proving those external theorems anew.
