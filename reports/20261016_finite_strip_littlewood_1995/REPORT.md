# Finite-strip logarithmic interpolation and Littlewood denominator 19.95

## Theorem

For every real t with |t|≥3, the Riemann zeta function has no zero in

σ > 1 − log log|t| / (19.95 log|t|).

The new ingredient is a finite-rectangle harmonic barrier. It transfers finite-height critical-line bounds to the full horizontal range needed by the zero-detection formula, without claiming a global vertical bound from a finite table. Both infinite logarithmic-integral tails are retained and paid separately. The source estimate is the [unsplit HPY theorem](../20261016_unsplit_hpy_critical_bound/REPORT.md), whose proof is independent of this zero-free conclusion.

## 1. Complete inherited zero-detection inequality

Use Andrew Yang, *Explicit bounds on ζ(s) in the critical strip and a zero-free region*, [arXiv:2301.03165v2](https://arxiv.org/abs/2301.03165v2), Lemmas 4.1–4.8, identity (4.65) and the derivation of (4.125). The [20.0 localized-integral report](../20261016_localized_critical_integral_littlewood_200/REPORT.md) records the full unchanged detector, isolated zero, paired terms, pole, right integral, zero-count term and smoothing remainder. The [20.1 boundary report](../20261016_optimized_boundary_littlewood_201/REPORT.md) records the unchanged global interpolation and discrete-k witnesses.

Write D=46, b0=1, b1≤1.747088 and b=Σ(j=1,…,46)bj≤3.574410, with bj≥0. Put

L1=log(46t+1), L2=log L1, V=L1−3.377.

Yang's exact detector sum gives

(1/b)Σ bj log(jt)≤V.                                      (1.1)

Under the genuine zero-free rectangle

1−λ<Re s≤1, t−1≤Im s≤46t+1,

and 0<λ≤1−β≤η/2, λ(R+1)≤η, R≥100, the complete local inequality is

.17996−.20523((1−β)/λ−1)
≤λ{.087π²b1(1−β)/η²+B/(2η)+c(R)λT},                     (1.2)

where c(R)≤1+10.05/R. For 2/7≤η≤1/2,

T=b[(.891+.6079ν)V+(.7813+.58ν)L2+7.329+3.898ν]+1.8,
ν=(η^(−2)+(1−η)^(−2))/2.                                  (1.3)

Only the left-logarithmic-integral bound B is improved below. The right integrals still contribute log ζ(1+η). The count coefficient discarded in deriving (1.2) remains negative on this entire η range. The exact old discrete-k formula remains unchanged.

## 2. Uniform Euler bound on the whole strip

For 1/2≤σ≤5/7, Euler summation gives

ζ(s)=s/(s−1)−s∫₁∞{v}v^(−s−1)dv.

Using |s|≤1+|Im s|, |s−1|≥2/7 and σ≥1/2 gives the convenient uniform estimate

|ζ(σ+iy)|≤6(1+|y|), all real y.                           (2.1)

This holds through height zero and does not depend on any zero-free hypothesis. The strip contains no pole.

For 64≤x=logt≤215, every τ=jt, 1≤j≤46, satisfies

log6+log(1+τ+1000)<223.                                   (2.2)

The complete logarithmic integral is

Iη(τ)=(1/2)∫_R log|ζ(1−η+iτ+2ηiu/π)|/cosh²u du.          (2.3)

On |u|>100, since 2η≤1, (2.1) gives an upper envelope 223+|u|. Therefore both entire tails together contribute at most

4∫₁₀₀∞ e^(−2u)(223+u)du
=2e^(−200)(323.5)<10^(−80).                               (2.4)

No zero-height portion of the integral is removed. Logarithmic singularities at zeros are locally integrable and decrease the upper bound.

## 3. Finite rectangle with an explicit harmonic barrier

Fix τ and consider the rectangle

1/2≤σ≤5/7, |y−τ|≤1000.

Its width is 3/14 and midpoint is 17/28. Suppose C_L and C_R are nonnegative constants bounding log|ζ| on its two vertical sides. Let L(σ) be their linear interpolation, and define

H(σ,y)=sqrt2·223·cos(a(σ−17/28)) cosh(a(y−τ))/cosh(1000a),
a=7π/3.                                                   (3.1)

H is harmonic. On each horizontal side cos(a(σ−17/28))≥1/sqrt2, so H≥223. On the vertical sides H≥0. Equations (2.1)–(2.2) and the nonnegativity of L therefore give log|ζ|≤L+H on the entire boundary. The maximum principle for the subharmonic function log|ζ| gives the same inequality inside. Equivalently, zeros may be handled by the usual subharmonic formulation; they introduce no lower-bound assumption.

For |y−τ|≤32,

0≤H(σ,y)≤2sqrt2·223·exp(−968a)<10^(−1000).               (3.2)

Every central ordinate in (2.3), |u|≤100, lies in this smaller rectangle, because 100/π<32.

All heights τ±1000 are above exp60. Their log heights differ from logτ by at most

εlog=−log(1−1000exp(−64))<10^(−22).                       (3.3)

These inequalities, including (2.2)–(3.3), are certified by the accompanying directed program.

## 4. Two critical boundary choices and the complete harmonic sum

Let [l,r]⊂[64,215] be a closed rational log-height cell. The published Patel–Yang bounds, [arXiv:2302.13444v1](https://arxiv.org/abs/2302.13444v1), Section 3.1 and Table 1, give Aj y^(27/164) throughout each closed interval exp(60+5j)≤y≤exp(65+5j), j=0,…,31. The coefficients are increasing.

Choose the least j such that

r+log46+10^(−20)<65+5j,

and set A=Aj. The program requires j<32. This is a COMMON upper coefficient for every table interval touched by every one of the 46 rectangles and the entire certificate cell. The finite table is never extrapolated past exp220.

Put q=27/164 and

G_A(v)=qv+logA,
G_H(v)=v/6+log(.4467v+3.036),
F(v)=v/14+log v+log1.546.                                 (4.1)

G_A comes from the finite table; G_H comes from the independent unsplit HPY theorem for heights at least exp50. F comes from Yang's bound |ζ(5/7+iy)|≤1.546 y^(1/14)log y. All three functions are positive and increasing on v≥60; all are concave and have derivative at most one there. For either choice G, the vertical constants in Section 3 may therefore be taken as

C_L=G(logτ+εlog), C_R=F(logτ+εlog).

Let α=(14η−4)/3, so 0≤α≤1. On the central integration window, the full bound from Section 3 is

log|ζ(1−η+iτ+2ηiu/π)|
≤αG(logτ)+(1−α)F(logτ)+εlog+10^(−1000).                  (4.2)

The upper bound is positive, so replacing the central kernel mass by one is lawful. Combining (4.2) with both complete tails (2.4), the program verifies that the total reserve is less than 10^(−20).

Now use the SAME G and A for every harmonic. By (1.1), positivity of bj, and Jensen's inequality for the increasing concave functions G and F,

Σ bj Iη(jt)≤b[αG(V)+(1−α)F(V)+10^(−20)].                 (4.3)

In particular the right-boundary logarithm is log V, not an independently substituted log L1. The aggregate 3.377 debit is exact and is not applied to varying unrecorded table coefficients.

Adding the unchanged right integrals yields the new complete local witness

B=b[αG(V)+(1−α)F(V)+10^(−20)]+logζ(1+η).                 (4.4)

The certificate uses (4.4) only within 64≤x≤215 and 2/7≤η≤1/2. Outside this range it retains the previously checked global interpolation or discrete-k witnesses. The global HPY boundary witnesses may also use the improved additive coefficient 3.036; their low-height boundary payment is unchanged, since it used only the retained leading coefficient .4467. Every global sub-Weyl witness still retains all 32 interval rows and the 66.7 infinite tail.

## 5. Whole-height contradiction

The previously established [classical 4.79 theorem](../20261016_littlewood_feedback_479/REPORT.md) supplies the lower heights because

4.79 log64<19.95.

The published Mossinghoff–Trudgian–Yang Vinogradov–Korobov denominator 55.241 supplies the high tail because

10^6/(log10^6)^4>(55.241/19.95)^3,

and x/(log x)^4 is increasing there. See [Theorem 1.1](https://link.springer.com/article/10.1007/s40993-023-00498-y), [arXiv:2212.06867v1](https://arxiv.org/abs/2212.06867v1).

If the theorem failed, the positive global infimum M of (1−β)logt/loglogt over zeros with t≥exp64 would be less than 1/19.95 and attained in the remaining compact height range. At a minimizing zero put

1−β=Mlogx/x, λ=M L2/L1.

Global minimality supplies the full rectangle t−1≤γ≤46t+1. Its possible lower sliver below exp64 is covered by the strict classical inequality. No proposed new zero-free region is assumed in choosing λ.

The directed verifier substitutes the worst allowed value M=1/19.95, with its inherited 10^(−20) relative slack. On every accepted closed cell it checks all smoothing inequalities, R≥100, both coefficient-bracket signs, and strict positivity of the complete margin in (1.2). The finite-table choice and harmonic-barrier guards are checked explicitly. Floating approximations only propose a witness; they cannot authorize acceptance.

The run terminates with PASS: 1,563 accepted closed cells after 3,110 evaluations, no unresolved interval, and smallest directed lower margin greater than 1.48266654936×10^(−7). The accepted modes are {'direct_hpy': 208, 'direct_table': 1102, 'k': 253}. The exact rational endpoints form a gap-free cover of [64,10^6].

The contradiction at the minimizing zero, the low and high splices, verified RH in the retained low-height range, and conjugation prove the stated region for all |t|≥3.

## Reproduction and scope

Run certify_transfer.py with certify_unsplit_hpy.py alongside it. The latter checks source constants at 192 bits; the continuum explicitly restores 160 bits. The summary and full scientific witness JSON record exact program hashes and all rational cells. An unresolved cell causes a nonzero exit.

This result concerns a zero-free strip. It does not count a percentage of zeros, claim global priority or external peer review, or prove RH. The finite-height inputs always retain a quantitative payment for the whole unbounded logarithmic integral.
