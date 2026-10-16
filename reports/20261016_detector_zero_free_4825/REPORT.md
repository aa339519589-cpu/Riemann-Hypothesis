# A detector refinement of the rescaled-pair region

This proof uses the [published rescaled-pair theorem and analytic estimates](../20261016_rescaled_pair_zero_free_484/REPORT.md). It changes only the nonnegative degree16 detector and uses the sharper remainder estimates already proved there. The smoothing packet, its exact positivity cone, the scale rectangle, and all external inputs are unchanged.

## Claim

For |t|≥2, ζ(σ+it)≠0 whenever σ>1−1/(4.825 log|t|).

The high-height input is the published Littlewood constant21.233. No19.62 input is used.

## Exact detector and its positivity

Write D=1000001000000 and define P(v)=D⁻¹Σ(j=0,…,16)n_j cos(jv), where

n=(1000001000000,1739978523793,1124906488989,503087299762,
123830409873,0,0,11530633557,6502748667,0,0,1437249199,
882564430,0,0,168666173,81325403).

Thus every Fourier coefficient a_j is nonnegative and a_0=1. Exact rational Sturm arithmetic verifies that the polynomial Σa_j T_j(X) has no root in[−1,1] and has positive value atX=0. Therefore P is strictly positive for every real v. This is a complete positivity certificate, not positivity at the numerical optimization grid.

The coefficient sum is A=Σ(j≥1)a_j=1756202954923/500000500000, smaller than the original detector sum2919857/828465. The first coefficient is a_1=1739978523793/1000001000000. All detector coefficients are stored exactly in detector.json.

## All changed finite inequalities

The unchanged rational smoothing packet p, convolution seed w and constantsκ,w0,L retain the meanings in the base proof. On exactly its rectangle, use its same outward rational lower weights for primes2,3,5,7 and powers1 through8. The complete Arb phase-cover certificate now gives respective lower bounds

0.2128, 0.0482, 0.0073, 0.00207.

Their logarithm-weighted sum exceeds0.21623176310627268. All omitted terms remain nonnegative, so the prime contribution is at least0.216ηw0.

The full signed Gamma calculation, with absolute coefficient norm used on every error, gives

Σ(k=0,…,16)a_k Σ(m=0,…,6)k_m[−½logπ+½ReψΓ((σ+md+ikt)/2+1)]
≤ (Aκ/2)log t−1.559.

The worst outward zero-harmonic-plus-constant bound is less than−1.5594484600604. The nonzero-harmonic errors are included. The unchanged base bounds307η³ at height zero and6η²+261η³ at nonzero harmonics give complete costs

6LA=103.9555114040158…<104,
L(307+261A)=6036.429103656113…<6037.

Since A is no larger than the original detector sum, its nonzero-harmonic pole reserve10⁻⁶ also remains valid. The zero-harmonic pole F(σ−1) is retained exactly. The detector has the same maximum degree16, so the near-zero height enclosure16t+10¹⁰ and every log(k) remainder are unchanged.

## Complete scalar transfer and all heights

The established unconditional4.84 theorem implies the weaker seed4.8594. Accordingly set Ao=1/4.8594, An=1/4.825, x=log t, η=Ao/x, and σ=1−Ao/log(16exp(x)+10¹⁰). This is not an appeal to BTY's conditional4.8594 result. The entire old scale rectangle is preserved.

The base proof's complete near/far paired-zero partition and both-root monotonicity therefore imply that a zero in the claimed new strip would force

Mdet=a_1{F(σ−1+An/x)+F(σ−An/x)}−F(σ−1)
     +1.775w0η−104η²−6037η³−10⁻⁶−Aκw0Ao/2≤0.

The verifier certify_detector_scalar.py proves Mdet>0 on the entire interval[28,81.51], using50,967 accepted closed rational intervals at160-bit Arb precision. Its smallest directed cell lower bound exceeds2.6552×10⁻⁹. Since28<log(3×10¹²) and exp(21.233/4.825)=81.501527439…<81.51, this covers the entire required finite-height range. The final certificate is a complete interval cover, not exploratory point sampling.

The lower range is covered by verified RH through3×10¹², including2≤|t|<3 as in the base proof. Above the Littlewood crossover the published21.233 region is at least as wide. Conjugation supplies negative heights. The positive scalar certificate therefore proves the claim on the same global range|t|≥2.

## Reproduction and scope

Use the base package's pinned Python requirements. The only new proof inputs are detector.json and the three scripts certify_detector_prime.py, certify_detector_gamma.py, and certify_detector_scalar.py. The packet file is byte-identical to the published smoothing packet. These scripts certify positivity, the entire phase covers, full Gamma/error costs, and the all-height scalar cover; exploratory optimization is not a proof input.

No claim about the proportion of zeros or RH is made. This is an explicit enlargement of a zero-free strip.
