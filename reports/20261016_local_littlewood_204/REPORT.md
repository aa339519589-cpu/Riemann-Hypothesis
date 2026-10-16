# A direct local-inequality certificate for Littlewood denominator 20.4

## Theorem

For every real t with |t|≥3, the Riemann zeta function is nonzero in

σ > 1 − log log|t| / (20.4 log|t|).

All analytic inputs used here are published results or the independently checked unconditional classical region linked below. In particular, no unpublished 19.62 estimate is assumed. This is a zero-free-region result, not a claim about a proportion of zeros or a proof of RH.

## 1. Inputs and what is changed

We use Andrew Yang, *Explicit bounds on ζ(s) in the critical strip and a zero-free region*, J. Math. Anal. Appl. 534(2), 128124 (2024), DOI [10.1016/j.jmaa.2024.128124](https://doi.org/10.1016/j.jmaa.2024.128124), version-pinned [arXiv:2301.03165v2](https://arxiv.org/abs/2301.03165v2). Specifically, we retain the fixed degree-46 detector, the compact smoothing function, Lemma 4.8 and the finite-eta inequality (4.125), with all their complete zero, pole and error terms.

The change is to evaluate these two local inequalities together on finite rational height intervals, with a different lawful eta and R witness when helpful. We do not take separate global maxima for Yang's constants C1 through C11. No new critical-strip zeta bound or trigonometric detector is used.

The low-height input is the [unconditional classical denominator 4.82](../20261016_near_zero_littlewood_482/REPORT.md). The high-height input is Mossinghoff–Trudgian–Yang, *Explicit zero-free regions for the Riemann zeta-function*, Research in Number Theory 10, 11 (2024), [Theorem 1.1](https://link.springer.com/article/10.1007/s40993-023-00498-y), version-pinned [arXiv:2212.06867v1](https://arxiv.org/abs/2212.06867v1): the Vinogradov–Korobov denominator 55.241 is valid for |t|≥3.

The fixed Yang detector has D=46, b0=1, b1=1.74708744081848... and b=Σ(j≥1)bj=3.57440943022073.... We use outward upper bounds

b1≤b1⁺=1.747088,   b≤b⁺=3.574410.

The lower-bound constants .17996 and .20523 are retained exactly as rounded in Yang's local inequality, not recomputed for a changed detector.

## 2. The complete local inequalities

Write x=log t, L1=log(46t+1), L2=log L1. Suppose ρ=β+it is a zero, t≥3×10¹², and there are no zeros in

1−λ < Re s ≤1,   t−1 ≤ Im s ≤46t+1.                    (2.1)

Assume also

0<λ≤1−β≤η/2,   λ(R+1)≤η,   R≥3.                     (2.2)

For η=ηk=k/(2^k−2), integer k≥4, Yang's Lemma 4.8 states

.17996 − .20523((1−β)/λ−1)
≤ λ{ .087π² b1 (1−β)/η² + Bk/(2η) + c(R)λ Tk },       (2.3)

where

Bk = b[(L1−3.377)/(2^k−2)+L2+log1.546] + log ζ(1+η),

Tk = b[(23.99/√η−40.051)(L1−3.377)+1.2031L2−38.58
          +(2.0373L2−.5322logη)/η²] +1.8.

In this application t≥exp65 and k≤14, so the subsidiary t≥2^k requirement in the integral input, Lemma 4.2, is also satisfied.

For 2/7≤η≤1/2, the same argument using Yang's Lemmas 4.3 and 4.6 gives (2.3) with

Bη = b[(8η−1)(L1−3.377)/18+L2+1.659−4.279η] + log ζ(1+η),

Tη = b[(.891+.6079ν)(L1−3.377)+(.7813+.58ν)L2
           +7.329+3.898ν] +1.8,

ν=(η⁻²+(1−η)⁻²)/2.                                   (2.4)

This is Yang's displayed (4.125). Its derivation does not require t≥exp170.2: the two replacing lemmas require only t≥3×10¹² and 2/7≤η≤1/2. The rectangle and smoothing hypotheses (2.1)–(2.2), which are essential, remain unchanged. The complete negative local-zero-count term is discarded in the same permitted direction as in the proof of Lemma 4.8; no new term is omitted here.

## 3. An outward bound for c(R)

The fixed-detector theta is the unique solution of

sin²θ=b1(1−θcotθ),   0<θ<π/2.

The certificate checks the signs at θ=1.1326 and θ=1.1328 uniformly for b1 in [1.74708,1.74710]. This interval is much wider than the rounding in the published coefficient and encloses the same fixed-detector root, rather than defining a new detector.

Put

w0=sec²θ(θtanθ+3θcotθ−3),
c0=1/(sinθ cos³θ),
c1=(θ−sinθcosθ)tan⁴θ,
c2=tan³θ sin²θ,
c3=(θ−sinθcosθ)tan²θ.

For q=1/R, Yang's formula (4.58)–(4.60) is exactly

(c(R)−1)R
=1+(c0/w0)(1+q)²(1−tan²θ q²)⁻²
       [c2(q²+q³)(exp(2θcotθ)+1)+c1q²+c3].             (3.1)

Every factor is nonnegative and increasing in q for 0≤q≤1/100. Outward Arb evaluation at q=1/100, with the full theta interval retained, gives a value strictly below 10.05. Therefore

c(R)≤1+10.05/R   for every R≥100.                     (3.2)

Every witness used below has integer R≥100. Thus (3.2) is applicable without asymptotic truncation.

## 4. The global minimum and the required rectangle

It suffices to consider positive t. Set M1=1/20.4 and x0=65.

The classical 4.82 region implies the asserted Littlewood region whenever 3≤t≤exp65, because

4.82 log65 <20.4.                                    (4.1)

The Vinogradov–Korobov 55.241 region implies it for x=log t≥10^6, because

x/(logx)^4 ≥ 10^6/(log10^6)^4 > (55.241/20.4)^3.       (4.2)

The first inequality follows by differentiation, since logx>4. Both strict numerical comparisons are certified by the supplied verifier.

Suppose the theorem is false. Define

Z(β,t)=(1−β)log t/log log t,
M=inf{Z(β,t): ζ(β+it)=0, t≥exp65}.

Then 0<M<M1. Indeed, a violating zero gives M<M1; (4.2) excludes such values outside the finite height interval [exp65,exp(10^6)], and there are only finitely many zeros in that interval. Their real parts are strictly less than 1 by the known classical region. Consequently the infimum is attained by a zero ρ=β+it with 65≤x=log t≤10^6. In particular

1−β=M logx/x.                                       (4.3)

Set

λ=M L2/L1.                                          (4.4)

Because loglog y/log y decreases for y>exp(e), (4.3) implies λ≤1−β. The rectangle (2.1) is genuinely zero-free: for any ordinate γ between t−1 and46t+1 with γ≥exp65, the definition of the global M gives

1−β′ ≥ M loglogγ/logγ ≥ M L2/L1=λ.

If instead t−1≤γ<exp65, the classical 4.82 region gives

1−β′ ≥1/(4.82 logγ)>1/(4.82×65)
       >M1 log65/65≥λ,

where (4.1) and monotonicity were used. Thus the small lower-boundary sliver is also paid; no unproved local zero-free rectangle is assumed.

## 5. Finite scalar certificate

For each closed rational cell I=[a,b]⊂[65,10^6], the verifier selects one of the following eta witnesses:

- η=50/100,48/100,...,30/100, or 2/7, using (2.4);
- η=k/(2^k−2), k=4,...,14, using (2.3).

It also selects an integer R. Floating-point values are used only to propose witnesses. Acceptance depends exclusively on outward 160-bit Arb inequalities over the whole closed cell.

Let ε=10⁻²⁰, and define, on that entire cell,

λ1=M1 L2/L1,   d1=(1+ε)M1 logx/x,

Aleft=.17996−.20523[(1+ε)(logx/x)/(L2/L1)−1].

Let B⁺ and T⁺ be the applicable expressions in Section 2 after replacing b by b⁺. The accepted margin is

Aleft − λ1{.087π²b1⁺ d1/η² + B⁺/(2η)
                         +(1+10.05/R)λ1 T⁺}>0.      (5.1)

Each accepted cell also verifies R≥100, λ1(R+1)≤η, d1≤η/2, and positivity of the individual bracket multiplying b in BOTH B and T. This last check makes the outward replacement b≤b⁺ lawful even in the presence of the displayed negative constants. All choices satisfy the eta-domain conditions above.

For the actual minimizing zero, M≤M1 and (4.3)–(4.4) hold. The left side of (2.3) is at least Aleft. The right side is at most the subtracted quantity in (5.1), because its individual coefficients are nonnegative and λ≤λ1, 1−β≤d1. The same R remains lawful for the smaller actual λ. Thus (5.1) contradicts the complete local inequality.

The 160-bit computation accepts 1,875 closed rational cells after 3,734 evaluations, with no failed or pending cell. Its smallest directed margin is greater than 5.6155751765×10⁻⁸. The initial intervals exactly cover [65,10^6], and recursive bisection preserves that cover. The witness JSON lists every accepted interval, eta choice, R and directed margin. Together with (4.1)–(4.2), this proves the theorem for every positive height at least 3. Conjugation gives negative heights.

## 6. Reproduction and interpretation

Run `certify_littlewood.py` with the base package's pinned python-flint environment. It produces the scientific summary and the complete finite witness list. The program exits unsuccessfully if a cell is not certified. The two published local inequalities and their analytic hypotheses are explicitly stated above; the computer output is not used as a substitute for them.

The denominator change from 21.233 to 20.4 enlarges the Littlewood strip width by a factor 21.233/20.4, approximately 1.04083. This is a width comparison, not a statement that a corresponding percentage of zeta zeros has been excluded. No priority claim is made over unexamined or unpublished claims.
