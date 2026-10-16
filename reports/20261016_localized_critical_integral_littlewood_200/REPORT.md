# Localized critical-line integrals and Littlewood denominator 20.0

## Theorem

For every real t with |t|≥3, the Riemann zeta function has no zero in

σ > 1 − log log|t| / (20.0 log|t|).

The new ingredient is a direct bound for the complete critical-line logarithmic integral in Yang's zero-detection formula. Published finite-height sub-Weyl estimates are used only on an explicitly enclosed central window. Both infinite integration tails, including the portion crossing height zero, are paid by a separate global Euler-summation bound. No finite-height estimate is extended to infinity.

## 1. Inherited complete setup

Use Andrew Yang, *Explicit bounds on ζ(s) in the critical strip and a zero-free region*, [arXiv:2301.03165v2](https://arxiv.org/abs/2301.03165v2), in particular Lemmas 4.1–4.8, identity (4.65), and the complete derivation of (4.125). The [20.1 report](../20261016_optimized_boundary_littlewood_201/REPORT.md) records the complete local inequality, the degree-46 detector, the smoothing constants and all unchanged global interpolation witnesses. We retain those ingredients, including the isolated zero, right-shift integral, pole, far-zero remainder and the discarded count coefficient with its verified negative sign.

Write D=46, b0=1, b1≤1.747088, b=Σ(j=1,…,46)bj≤3.574410, with all bj≥0. Put

L1=log(46t+1), L2=log L1, V=L1−3.377.

Yang's (4.65) gives the exact weighted inequality

(1/b)Σ bj log(jt)≤V.                                    (1.1)

The same complete argument as in the 20.1 report gives, under the genuine zero-free rectangle and smoothing conditions,

.17996−.20523((1−β)/λ−1)
≤λ{.087π²b1(1−β)/η²+B/(2η)+c(R)λT},                    (1.2)

where c(R)≤1+10.05/R for R≥100. For the continuous witnesses 2/7≤η≤1/2,

T=b[(.891+.6079ν)V+(.7813+.58ν)L2+7.329+3.898ν]+1.8,
ν=(η^(−2)+(1−η)^(−2))/2.                                 (1.3)

Only the bound B for the left logarithmic integrals will change. The right logarithmic integrals still contribute log ζ(1+η). All old global witnesses, including the original discrete-k witnesses, remain available without alteration.

## 2. A global upper bound paying both infinite tails

At s=1/2+iy, the first Euler summation identity gives

ζ(s)=s/(s−1)−s∫₁∞{u}u^(−s−1)du.

Consequently, since |s|=|s−1|,

|ζ(1/2+iy)|≤1+2|s|≤4(1+|y|)                            (2.1)

for every real y, including y=0. This bound is used only to pay the tails, not as a competitive critical-line estimate.

Let 64≤x=logt≤215, τ=jt with 1≤j≤46, and set η=1/2. The exact integral is

I(τ)=(1/2)∫_R log|ζ(1/2+iτ+iu/π)|/cosh²u du.             (2.2)

Split it at |u|=100. On the complement, |τ+u/π|≤τ+|u| and

log|ζ(1/2+iτ+iu/π)|≤log4+log(1+τ)+log(1+|u|)
                  ≤223+|u|.

Here 1+46exp215<exp220, so log4+log(1+τ)<223. Using cosh^(−2)u≤4e^(−2|u|), the entire two-sided complement is at most

4∫₁₀₀∞e^(−2u)(223+u)du
=2e^(−200)(323.5)<10^(−80).                              (2.3)

No lower bound on ζ or deletion of the near-zero-height part is involved. Logarithmic singularities at zeros are locally integrable and only decrease the upper bound.

On |u|≤100, the displacement is less than 32, hence less than 1000. Thus the change of log height from logτ has absolute value at most

εlog=−log(1−1000exp(−64))<10^(−22).                       (2.4)

The verifier checks every numerical inequality in (2.3)–(2.4) with directed arithmetic.

## 3. Finite-table central bound and complete harmonic sum

The primary input is Patel–Yang, *An explicit sub-Weyl bound for ζ(1/2+it)*, [arXiv:2302.13444v1](https://arxiv.org/abs/2302.13444v1), Section 3.1 and Table 1. Each row is explicitly a bound throughout its closed interval:

|ζ(1/2+iy)|≤Aj y^(27/164), exp(60+5j)≤y≤exp(65+5j),
0≤j≤31.

All 32 exact decimal Aj are reproduced in the verifier and in the linked 20.1 report. They are increasing. No bound from this table is used beyond exp220.

For a rational cell [l,r]⊂[64,215], set

Z=r+log46+10^(−20).

Choose the least integer j≥0 for which Z<65+5j, and require j≤31. Put A=Aj. Every central ordinate for every harmonic lies above exp60, and its log is less than Z. Thus A is a common upper coefficient for ALL intervals intersected by all 46 central windows, even when the cell or a harmonic crosses a table endpoint. It is not a sampled coefficient at the center.

The positive central upper bound and the fact that the central kernel mass is at most one give

I(kt)≤(27/164)log(kt)+log A+10^(−20), 1≤k≤46.             (3.1)

The reserve 10^(−20) pays both (2.3) and (2.4). Multiplying by the complete nonnegative detector coefficients and using (1.1) yields

Σ bk I(kt)≤b[(27/164)V+log A+10^(−20)].                   (3.2)

There is no new k-dependent coefficient inside the aggregate 3.377 debit: A was deliberately chosen common to all harmonics. Substitution into the original complete explicit formula therefore gives a new lawful witness in (1.2), at η=1/2, with

B=b[(27/164)V+log A+10^(−20)]+logζ(3/2).                  (3.3)

## 4. Alternative affine-log critical-line witness

The previously proved standalone HPY parameter bound in the 20.1 report is

|ζ(1/2+iy)|≤(.4467 log y+4.940)y^(1/6), y≥exp50.

All central ordinates above exceed exp60. The function

G(v)=v/6+log(.4467v+4.940)

is positive, increasing and concave there, with derivative less than one. The same central/tail split gives I(kt)≤G(logkt)+10^(−20). Jensen's inequality for the full detector weights and (1.1) imply

Σ bk I(kt)≤b[G(V)+10^(−20)].

Thus another lawful η=1/2 witness is

B=b[V/6+log(.4467V+4.940)+10^(−20)]+logζ(3/2).             (4.1)

It is retained as an optional candidate; the terminal cover below does not need to accept any cell with this witness. This is a complete integral bound, not a claim that a finite-height upper estimate satisfies Yang's global integral lemma by itself.

## 5. Global contradiction and directed cover

The low-height input is the already established [classical 4.79 theorem](../20261016_littlewood_feedback_479/REPORT.md). Its proof used only earlier Littlewood bounds, not this conclusion. The high-height input remains the published Vinogradov–Korobov 55.241 theorem used in the 20.1 report.

The verifier checks

4.79 log64<20.0,
10⁶/(log10⁶)^4>(55.241/20.0)³.

The former excludes a violating zero up to exp64; the latter excludes one above exp(10⁶), with the monotonic high-height continuation. If a violation existed, the positive global infimum M of (1−β)logt/loglogt over zeros of height at least exp64 would be below 1/20.0 and attained in the remaining compact height range. At a minimizing zero set

1−β=Mlogx/x, λ=M L2/L1.

Global minimality supplies the whole rectangle t−1≤γ≤46t+1. Its possible lower sliver below exp64 is covered by the strict classical inequality. This is the same noncircular attained-minimum argument as in the preceding full proofs; no proposed new region is assumed in forming the rectangle.

The new verifier retains every globally lawful witness from 20.1 and adds only (3.3) and (4.1), restricted to their stated height range and η=1/2. Floating calculations propose a witness. Every acceptance uses directed 160-bit Arb arithmetic on the entire closed rational cell, including the exact table-interval enclosure, all smoothing inequalities, positivity of each coefficient bracket, and R≥100.

The continuum run covers [64,10⁶] with 887 accepted closed cells after 1,758 evaluations and no unresolved interval. The smallest directed lower margin exceeds 1.19182596830×10⁻⁷. The accepted cover uses 515 direct-table cells, 116 inherited global sub-Weyl cells, and 256 inherited discrete-k cells; the affine-log direct witness is not needed for acceptance. The source constants are checked at 192 bits before the main program explicitly restores 160 bits. All original global PL boundaries and complete integration-tail hypotheses for the old witnesses remain exactly those of the 20.1 report.

Inserting the hypothetical minimizing zero into its certified cell contradicts (1.2). Verified RH, the classical low-height splice, the high-height VK splice and conjugation then prove the theorem for every |t|≥3.

## Reproduction and scope

Run certify_local_critical.py with certify_hpy_constants.py alongside it in the pinned python-flint environment. The scientific summary and full witness list record all closed cells, their directed lower margins and the exact script hashes. An unresolved cell causes a nonzero exit.

This is an explicit zero-free-strip theorem. It does not assert a proportion of excluded zeros, global priority, external peer review or a proof of RH. The new finite-height input is always accompanied by a quantitative bound for both complete infinite integral tails.
