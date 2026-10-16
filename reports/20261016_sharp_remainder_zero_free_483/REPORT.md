# A sharper unconditional classical denominator: 4.83

This is a refinement of the [published rescaled-pair theorem with denominator 4.84](../20261016_rescaled_pair_zero_free_484/REPORT.md). It does not modify that proof or its certificates.

## Claim

For |t|≥2, ζ(σ+it) is nonzero when σ>1−1/(4.83 log|t|).

All external inputs are the same published inputs as for 4.84. In particular, the Littlewood handoff uses 21.233, not the unpublished 19.62 input.

## Exact improvement of the remainder

Section 4 of the base proof and its independently replayed analytic-constant certificate already establish the following bounds for the compact source gη(u)=ηw(ηu), uniformly throughout the original rectangle with Amax=1/4.8594:

- At height zero, each shifted-source remainder is at most 307η³.
- At heights kt, 1≤k≤16, each shifted-source remainder is at most 6η²+261η³.

The original theorem deliberately rounded these upward to 623η³ and 14η²+424η³ before summing the packet and detector. Here retain the sharper proved numbers. With the same packet norm L and detector sum A, exact interval arithmetic gives

6LA = 104.311135045887… < 105,
L(307+261A) = 6051.898732077512… < 6052.

Thus the complete remainder is at most 105η²+6052η³. No sign or subset of a remainder has been discarded. The prime lower bound .213ηw0, Gamma gain 1.56ηw0, and real-pole reserve 10⁻⁶ are unchanged.

## Prior theorem, scale, and height splice

The already established 4.84 theorem implies the weaker classical seed 4.8594, so set Ao=1/4.8594 and An=1/4.83. This is an unconditional use of a proved weaker region, not an appeal to the conditional BTY 4.8594 theorem. The fixed scale and shift remain

η=Ao/x,  σ=1−Ao/log(16exp(x)+10¹⁰),  x=log t.

Consequently the entire old rectangle remains valid. The paired-transform positivity, near/far zero partition, both-root convexity, and all finite-prime/Gamma estimates from the base proof apply literally. The hypothetical zero therefore forces

Msharp = a1{F(σ−1+An/x)+F(σ−An/x)}−F(σ−1)
         +1.773w0η−105η²−6052η³−10⁻⁶−Aκw0Ao/2 ≤ 0.

The certificate `certify_sharp_scalar.py` proves Msharp>0 on every x∈[28,82], using 31,061 accepted closed rational intervals at160-bit Arb precision. The smallest directed cell lower bound exceeds2.5951×10⁻⁸. The script also certifies the two exact combined-error inequalities above.

Since log(3×10¹²)>28 and exp(21.233/4.83)=81.131090896…<82, the base proof's verified-low-height, finite-interval, and published-Littlewood splice proves the claim on the same height range |t|≥2.

## Reproduction and interpretation

The only new numerical step is the scalar certificate with the sharper summed remainder. Run `python certify_sharp_scalar.py` with the base package's pinned requirements. Its adjacent `rescaled_packet.json` is byte-identical to the base packet. All other mathematical and numerical inputs are precisely those of the base proof.

Relative to the accepted4.896 classical denominator, the strip width increases by4.896/4.83−1≈1.366%. This is a width improvement, not a percentage of zeros and not a proof of RH. The separate19.62-dependent tier is not used here.
