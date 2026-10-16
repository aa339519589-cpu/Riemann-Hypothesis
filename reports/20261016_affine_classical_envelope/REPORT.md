# An affine finite-height classical zero-free envelope

## Theorem

For every real t with |t| ≥ H = 3×10¹², the Riemann zeta function has no zero in

σ > 1 − 1/(4.94 log|t| − 9.4).                              (1)

The denominator is positive throughout this domain. Together with the already established [classical 4.79 theorem](../20261016_littlewood_feedback_479/REPORT.md), this gives the zero-free strip with width

max{1/(4.79 log|t|), 1/(4.94 log|t|−9.4)}.

The affine term is stronger precisely when log|t| < 188/3. Beyond that height the existing 4.79 theorem supplies (1). This is a finite-height envelope refinement, not a replacement of 4.79 by a smaller global constant, a percentage of zeros, or a proof of RH.

## 1. Unchanged complete analytic inputs

Use the exact packet and full paired-zero explicit-formula estimates of the [4.84 base theorem](../20261016_rescaled_pair_zero_free_484/REPORT.md), and the exact degree-16 detector, prime and Gamma estimates of the [4.825 detector theorem](../20261016_detector_zero_free_4825/REPORT.md). Those reports retain every prime power, the isolated zero and its functional-equation mate, all other paired zeros, the archimedean remainder and the pole terms.

Put

Ao=1/4.8594, T0=10¹⁰, η0=Ao/log H,
σ0=1−Ao/log(16H+T0), w0=w(0), κ=p(1).

The seed 4.8594 is supplied unconditionally by the stronger published 4.84 theorem, not by an unpublished thesis estimate. The packet is exactly the adjacent rescaled_packet.json. Its Laplace transform is

F(z)=∫₀∞ e^(−zu) ηw(ηu)p(e^(−du))du, d=2σ−1.

The nonnegative packet gives F''≥0 on the real axis. The detector has a0=1,

a1=1739978523793/1000001000000,
A=Σ(k≥1)ak=1756202954923/500000500000.

The complete prime lower bound is .216ηw0, the complete Gamma upper bound is (Aκ/2)log t−1.559, and the total signed-packet error is at most 104η²+6037η³. A reserve of 10⁻⁶ pays the complete nonzero-harmonic real-pole terms. None of these coefficients is changed here.

## 2. Fixed source and height-dependent endpoint

For t≥H set

x=log t, L=log(16t+T0), η=Ao/x, σ=1−Ao/L,

An(x)=x/(4.94x−9.4).                                      (2)

The original full analytic rectangle remains valid: η≤η0, σ≥σ0 and (1−σ)/η=x/L<1. The prior classical region places all nonzero-harmonic near zeros and their reflected mates in the paired nonnegative strip; near ordinates below H, including the entire k=0 near group, use the retained verified RH range. The original far-pair estimate discards every other pair. This is exactly the base proof's near/far partition.

On 28≤x≤63, the denominator 4.94x−9.4 is positive and 4.94−9.4/x<4.8594. Thus An(x)>Ao. A hypothetical zero in (1) would satisfy

Ao≤(1−β)x≤An(x).

At each fixed x, convexity F''≥0 makes the whole isolated pair nonincreasing in the distance parameter b=(1−β)x. Consequently its lower bound is

F(σ−1+An(x)/x)+F(σ−An(x)/x).                              (3)

The first argument is at most the second because An(x)/x<1/2. No derivative with respect to x or separate monotonicity of the two roots is needed. Allowing the endpoint An to depend on height does not change the source, the zero-free rectangle or any discarded term.

## 3. Complete scalar contradiction and certificate

The full detector-weighted explicit formula, with (3), forces

0≥M(x):=a1{F(σ−1+An(x)/x)+F(σ−An(x)/x)}−F(σ−1)
       +1.775w0η−104η²−6037η³−10⁻⁶−Aκw0Ao/2.             (4)

The verifier evaluates this expression on closed rational intervals using outward 160-bit Arb arithmetic. It starts with [28,63] and bisects until the entire interval has a strictly positive directed lower bound. Stable confluent-hypergeometric expressions for the exact compact Laplace integrals are inherited unchanged from the base verifier.

The complete run accepts 350,201 closed cells after 700,401 evaluations. No unresolved interval remains. The smallest directed lower bound is greater than 4.26211388847×10⁻⁹. The scientific JSON pins the script, exact packet and detector, and records all scientific parameters and the terminal PASS. Numerical overcoverage below log H does not assert analytic validity there; only the portion x≥log H is used.

## 4. Whole stated domain

The verifier certifies 28<log H and

4.94−9.4/63>4.79.

Since 4.94−9.4/x increases with x, the established 4.79 theorem contains the affine strip for x≥63. Formula (4) excludes every remaining hypothetical zero with log H≤x≤63. Conjugation supplies negative t. This proves (1) throughout its stated domain.

The exact equality of widths occurs at

x=9.4/(4.94−4.79)=188/3.

All dependencies precede the present result. In particular, the 4.79 theorem is used only as a known seed and final handoff; it does not depend on this affine envelope.

## Reproduction

Run certify_affine.py in the pinned python-flint environment with the adjacent packet and detector. Floating conversions are used only for reporting the smallest certified margin; every interval acceptance uses an outward Arb comparison. Any unresolved interval causes a nonzero exit. The scalar PASS must be read together with the full analytic transfer above.
