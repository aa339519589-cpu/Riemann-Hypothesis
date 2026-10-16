# Classical denominator 4.79 from the established Littlewood 20.15 region

## Theorem and noncircular dependencies

For every real t with |t|≥2, the Riemann zeta function has no zero in

σ > 1 − 1/(4.79 log|t|).

The new input is the already established [Littlewood denominator 20.15 theorem](../20261016_critical_interpolation_littlewood_2015/REPORT.md). That theorem used only the earlier classical denominator 4.82, not the present conclusion. The classical seed 4.8594 used below is supplied by the stronger, unconditional [denominator 4.84 theorem](../20261016_rescaled_pair_zero_free_484/REPORT.md). No unpublished 19.62 bound or conditional classical seed is used.

We inherit the exact rational smoothing packet and complete analytic explicit-formula estimates from the 4.84 proof, and the exact degree-16 detector and its complete prime/Gamma estimates from the [detector refinement](../20261016_detector_zero_free_4825/REPORT.md). The mechanism is the same as the [4.82 near-zero refinement](../20261016_near_zero_littlewood_482/REPORT.md), but the stronger Littlewood input is applied to actual near-zero ordinates from a lower transition height. The full original packet rectangle is retained, not replaced by a narrower incidental subrectangle from that earlier computation.

## 1. Constants and original analytic rectangle

Write

H=3×10¹², T0=10¹⁰, Ao=1/4.8594, An=1/4.79,

η0=Ao/log H, σ0=1−Ao/log(16H+T0).

The inherited analytic estimates hold for 0<η≤η0 and σ0≤σ≤1, together with σ−1≥−η for the actual far-zero arguments. Put d=2σ−1. The packet remains

f(u)=ηw(ηu) p(exp(−du)), F(z)=∫₀∞ exp(−zu)f(u)du,

with precisely the rational coefficients in rescaled_packet.json, and w0=w(0). In particular f≥0 and F''≥0 on the real line. Let κ=p(1).

The detector has a0=1,

a1=1739978523793/1000001000000,

A=Σ(k≥1)ak=1756202954923/500000500000.

Its complete prime lower bound is .216ηw0. Its complete Gamma upper bound is (Aκ/2)log t−1.559. The total error is at most 104η²+6037η³. A reserve of 10⁻⁶ pays the full nonzero-harmonic real-pole terms. These are unchanged estimates, including all prime powers, zero pairs and harmonic contributions from the linked proofs.

## 2. Near-zero enclosure at two heights

For t≥H set x=log t, η=Ao/x and L=log(16t+T0).

When x≤60, choose σ=1−Ao/L. The existing classical seed puts every nonzero-harmonic near zero and its reflected mate in the paired nonnegative strip. Any near ordinate below H is covered by verified RH, as in the base proof.

When x≥60, instead choose

σ=1−log L/(20.15 L).                                      (2.1)

For 1≤k≤16 and |γ−kt|≤T0, one has

H<t−T0≤|γ|≤16t+T0.

The first inequality holds already at x=60 and is checked by the verifier. Because log v/v decreases for v>e, the established 20.15 theorem gives

β≤1−loglog|γ|/(20.15 log|γ|)≤σ.

The functional-equation mate satisfies the same bound 1−β≤σ. Thus both members of the near pair lie in the required strip 0≤Re z≤2σ−1. For k=0, every near zero has |γ|≤T0<H and is on the critical line by the retained RH verification.

All other pairs use the unchanged far-pair bound. To justify this without enlarging its domain, every accepted cell on [60,68] checks simultaneously

μ=(1−σ)/η≤1, σ≥σ0, η≤η0.                            (2.2)

The formulas also give η>0 and σ≤1. Conditions (2.2) imply d≥2σ0−1 and σ−1≥−η. Hence the complete original rectangle and actual-pair range are valid. There is no requirement here that η≤.003 or σ≥.997; those were merely convenient narrower bounds in the separate 4.82 certificate, not hypotheses of the inherited estimates.

For the first branch and actual t≥H, η≤η0, σ≥σ0 and μ=x/L<1 hold directly. Numerical overcoverage down to x=28 below log H does not assert analytic validity there and is not needed for the proof.

## 3. Full contradiction inequality

For a hypothetical zero β+it in the claimed strip, the seed and the target give

Ao≤(1−β)x≤An.

The whole isolated pair is compared at the endpoint An by F''≥0; the first argument is at most the second because β≥1/2. This is a comparison of the pair, not a deletion or separate monotonicity assertion for either root.

The complete detector-weighted explicit formula therefore implies

0≥M=a1{F(σ−1+An/x)+F(σ−An/x)}−F(σ−1)
       +1.775w0η−104η²−6037η³−10⁻⁶−Aκw0Ao/2.          (3.1)

All transforms in (3.1) use the current σ and η. Every root, pole and error convention is the one in the linked complete proofs.

The verifier starts with the two closed rational intervals [28,60] and [60,68], using the first and second σ choices respectively. On each cell it evaluates (3.1) with outward 160-bit Arb arithmetic and accepts only a strictly positive directed lower bound, together with (2.2) on the second branch. Bisection preserves the full closed cover.

The run accepts 42,007 cells after 84,012 evaluations, with no unresolved cell. The smallest directed lower bound is greater than 1.59224391089×10⁻⁸. The JSON records scientific parameters and the exact script, packet and detector hashes. This is a continuum certificate rather than a sampled height calculation.

## 4. Whole-height splice

The final handoff is

X*=exp(20.15/4.79)=67.13332614568968…<68.

Verified RH covers 2≤|t|≤H. Since 28<log H, the positive certificate covers every remaining ordinate from H through exp(X*). For x≥X*, log x/20.15≥1/4.79, so the established 20.15 Littlewood strip contains the desired classical strip. Conjugation supplies negative ordinates. This proves the theorem with no circular use of the new classical constant.

## Reproduction and scope

Run certify_feedback.py in the python-flint environment pinned in the base package. The adjacent packet and detector are unchanged. The program exits unsuccessfully if any interval remains unresolved. Its scalar certificate must be read together with the analytic domain and near-zero argument above.

This is an enlargement of an explicit zero-free strip. It does not give a proportion of excluded zeros and is not a proof of RH.
