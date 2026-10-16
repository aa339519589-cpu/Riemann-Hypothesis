# Feeding the published Littlewood region into the near-zero enclosure

## Result and inherited estimates

For |t|≥2, ζ(σ+it)≠0 whenever σ>1−1/(4.82 log|t|).

This uses only the published21.233 Littlewood theorem, verified RH through H=3×10¹², and the already established unconditional4.84 region. The19.62 thesis input is not used.

Use the exact rational smoothing packet and analytic estimates of the [base rescaled-pair proof](../20261016_rescaled_pair_zero_free_484/REPORT.md), and the exact degree16 detector and changed prime/Gamma bounds of the [detector refinement](../20261016_detector_zero_free_4825/REPORT.md). In particular:

- The detector has a0=1, a1=1739978523793/1000001000000 and A=Σ(k≥1)ak=1756202954923/500000500000.
- The complete prime lower bound is .216ηw0.
- The complete Gamma upper bound is (Aκ/2)log t−1.559.
- The complete error is at most104η²+6037η³, and the nonzero-harmonic real-pole reserve is10⁻⁶.

The paired-transform positivity and all these estimates hold on the original rectangle, with the additional actual-pair requirement σ−1≥−η for the far-zero bound. The new calculation explicitly retains those conditions.

## The new near-zero choice

Put x=log t, Ao=1/4.8594 and An=1/4.82. The unconditional4.84 theorem supplies the weaker4.8594 seed; this does not invoke the conditional BTY4.8594 theorem. Keep η=Ao/x, K=16 and T0=10¹⁰.

For x≤76 use the original choice

σ=1−Ao/L,  L=log(16t+T0).

For x≥76 instead use

σ=1−log L/(21.233 L).                                    (1)

This is the published Littlewood theorem applied to the near-zero ordinates themselves, not merely at the final high-height splice.

To justify(1), let 1≤k≤16 and |γ−kt|≤T0. Then |γ|≥t−T0>H, while |γ|≤16t+T0. The function log v/v is decreasing for v>e. Therefore the Littlewood theorem gives

β≤1−loglog|γ|/(21.233 log|γ|)≤σ.

Applying the same theorem to the reflected mate gives1−β≤σ. Consequently both members of every such near pair lie in the paired nonnegative strip0≤Re z≤2σ−1. For k=0, every near zero has|γ|≤T0<H and remains on the critical line by verified RH.

Every other zero pair is handled by the unchanged far-pair bound. For this step it is essential that μ=(1−σ)/η≤1. On every accepted Littlewood-branch interval the new verifier certifies simultaneously

μ≤1,  σ≥.997,  η≤.003.

It also certifies that .997 exceeds the original exact σ0 and .003 is below its exact η0. Hence no smoothing-scale or horizontal rectangle has been enlarged. The pointwise formulas ensureσ≤1 andη>0.

## Complete contradiction and height cover

With F always formed from the chosenσ,η and unchanged rational packet, the nonnegative detector and the full explicit formula give, for a hypothetical zero in the new strip,

0≥M=a1{F(σ−1+An/x)+F(σ−An/x)}−F(σ−1)
     +1.775w0η−104η²−6037η³−10⁻⁶−Aκw0Ao/2.               (2)

The isolated-root comparison is still the monotonicity of the whole pair fromF''≥0, with Ao≤(1−β)x≤An. No individual root contribution or pole term has been dropped.

The interval verifier starts with the two closed ranges[28,76] and[76,82]. It uses the prior-regionσ on the first and(1) on the second, subdivides rational intervals, and accepts a cell only when the directed lower bound for(2) is positive and all applicable domain guards hold. The complete160-bit Arb replay accepts57,779 closed cells after115,556 evaluations, with smallest directed cell lower bound greater than3.2730×10⁻⁹. The scientific JSON records its result and hashes. This covers the whole continuum, not a discrete sample of heights.

The Littlewood handoff for the target4.82 is

X*=exp(21.233/4.82)=81.87442917246075…<82.

Since28<log H, the positive scalar cover rules out every proposed new zero fromH through exp(X*). Verified RH covers2≤|t|≤H. Above exp(X*) the same published Littlewood theorem is at least as wide as the claimed classical strip. This proves the stated global result.

## Reproduction and scope

Run certify_near_littlewood.py with the pinned requirements in the base package. Its packet and detector JSON are unchanged from the two linked accepted proofs. The only new numerical certificate is the two-part scalar cover and the explicit Littlewood-branch domain guards; the near-zero monotonicity argument above supplies its analytic justification.

This result enlarges a specified zero-free strip. It does not state a proportion of zeros excluded, and it does not prove RH.
