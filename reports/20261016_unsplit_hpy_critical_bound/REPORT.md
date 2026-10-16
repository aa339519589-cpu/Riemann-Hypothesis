# Retaining the complete block square root in the critical-line estimate

## Theorem

For every t≥exp(50),

|ζ(1/2+it)| ≤ (.4467 log t + 3.036)t^(1/6).                 (A)

The new analytic step is an integral bound for the remainder of a complete positive square root in the Hiary–Patel–Yang block sum. It replaces the separate square-root bound, not any term of the underlying derivative estimate. The full small-block and Riemann–Siegel remainders remain present.

## 1. Complete block estimate and fixed parameters

The primary source is Hiary–Patel–Yang, *An improved explicit estimate for ζ(1/2+it)*, version-pinned [arXiv:2207.02366v1](https://arxiv.org/abs/2207.02366v1), abbreviated HPY. We use its Lemmas 2.1, 2.5 and 2.6 and Section 3.4, especially (3.16)–(3.25). The [optimized-boundary report](../20261016_optimized_boundary_littlewood_201/REPORT.md) gives the complete substitution of the following fixed parameters, including their admissibility:

T=exp(50), K0=T^(1/3), r0=6, ε=4/3, R*=1000.

Here ε belongs to the derivative test; it is not the horizontal shift η in the later zero-detection formula. For t≥T set

K=ceil(t^(1/3)), n1=floor(sqrt(t/(2π))), R=floor(n1/K).

The elementary floor estimates give

R≥(sqrt(T/(2π))−1)/(T^(1/3)+1)−1>1658.7043>R*,
R≤t^(1/6)/sqrt(2π).                                      (1.1)

The lower continuous expression is increasing with T. Hence r0≤R throughout the infinite height range. Define the exact real constants

W*=π(r0+1)^3, Λ=((r0+1)/r0)^3,

μ=Λ^(2/3)/2 [1+1/((1−1/K0)Λ^(1/3))],

α=1/ε+εμ/(3W*^(1/3))+μ/(3W*^(2/3))
  +32μ sqrt(ε+W*^(−1/3))/(15sqrtπ),

β=32/(3sqrt(πε))+(2−4/π)W*^(−1/3),

ρ=(1+1/R*)/(sqrt2 π^(1/6)),

κ=[α+εαT^(−1/6)ρ+εβT^(−1/6)ρ³(1+T^(−1/3))²]^(1/2),

J0=log(1+1/(2R*))+2log(1+sqrt(1+1/(R*+1/2))),

ω=−log(2π)/2+J0−2asinh(sqrt(r0−1/2)).                     (1.2)

Every block's derivative parameters are bounded by these α and β, because its W is at least W* and the HPY parameter expressions have the indicated monotonicity. The same harmonic-sum calculation as HPY (3.21)–(3.23), using R* instead of the printed smaller lower bound, gives

Σ(r=r0,…,R) 1/sqrt(r(r+1)) ≤ log t/6+ω.                  (1.3)

The right side is positive already at t=T. No isolated negative ω term is multiplied by an independently rounded upper κ; the complete positive product is retained.

HPY (3.17) gives the full large-block estimate

T2≤2t^(1/6)π^(−1/6) Σ(r=r0,…,R) sqrt(B_r/[r(r+1)]),       (1.4)

where its B_r contains all four terms of (3.16). Set

C²=βπ^(2/3)(1+1/r0)(1+T^(−1/3)), d=Ct^(−1/6),
g_r=1/sqrt(r(r+1)).

Before applying the split in HPY (3.20), the complete bounds (3.18) and (3.19) give directly

sqrt(B_r/[r(r+1)])≤sqrt(κ²g_r²+d²).                      (1.5)

This is the starting point for the new estimate.

## 2. Uniform unsplit remainder bound

For fixed positive κ,d define

j(g)=sqrt(κ²g²+d²)−κg.

This function is nonnegative and decreasing for g>0. Since g_r≥1/(r+1/2),

j(g_r)≤h(r+1/2),
h(y)=sqrt(κ²/y²+d²)−κ/y.

The function h is nonnegative and increasing for y>0. For example, differentiating it gives

h'(y)=κy^(−2)[1−κ/sqrt(κ²+d²y²)]≥0.

Consequently each h(r+1/2) is bounded by its integral over [r+1/2,r+3/2]. Adding all blocks and then extending a positive integral down to zero yields

Σ(r=r0,…,R)j(g_r)
≤∫_(r0+1/2)^(R+3/2) h(y)dy
≤∫_0^(R+3/2) h(y)dy.                                    (2.1)

There is no singularity at zero: h(y) is asymptotic to d²y/(2κ). Put

J(z)=sqrt(1+z²)−1−log((1+sqrt(1+z²))/2).

Direct differentiation and J(0)=0 show

∫_0^Y h(y)dy=κJ(dY/κ).                                  (2.2)

In particular J is increasing and nonnegative. The upper index bound in (1.1) and t≥T give

d(R+3/2)/κ
≤z* := (C/κ)[1/sqrt(2π)+(3/2)T^(−1/6)].                 (2.3)

Combining (1.3), (1.5) and (2.1)–(2.3) proves the complete uniform sum bound

Σ sqrt(B_r/[r(r+1)])≤κ[log t/6+ω+J(z*)].                (2.4)

Every discarded quantity has been nonnegative and discarded in the upper-bound direction. The integer endpoint R and both endpoint offsets are explicitly retained in (2.1)–(2.3). The resulting new large-block bound is

T2≤2t^(1/6)π^(−1/6)κ[log t/6+ω+J(z*)].                 (2.5)

## 3. Small blocks, directed constants and conclusion (A)

The small-block estimate is unchanged from HPY (3.25):

T1≤4sqrt(r0(1+T^(−1/3)))t^(1/6)+I+1.48T^(−1/4)+.127T^(−3/4).

For the integer N in I, the elementary estimate

Σ(n=1,…,N)n^(−1/2)≤2sqrtN−1

gives I≤−2. Thus the full T1+T2 estimate has coefficients

b1=κ/(3π^(1/6)),
b2=4sqrt(r0(1+T^(−1/3)))+2κπ^(−1/6)[ω+J(z*)],
b3≤−2+1.48T^(−1/4)+.127T^(−3/4).                        (3.1)

The accompanying 192-bit Arb certificate encloses all exact expressions in (1.1)–(3.1), and verifies

z*=.8953603986900335…,
J(z*)=.1842926847852761…,
b1<.446622752866<.4467,
b2<3.035201380357<3.036,
b3<−1.99999448<0.

Rounding b1 and b2 upward and dropping b3 therefore proves (A) for the complete infinite range t≥T. This improves the previously checked additive coefficient 4.940 without changing its leading coefficient or its height range.

## Reproduction and scope

Run `certify_unsplit_hpy.py` using python-flint 0.9.0 / FLINT 3.6.0. The checker uses directed 192-bit Arb arithmetic throughout; its scientific JSON pins the complete program. It verifies every fixed constant, the block-index lower bound, the positive harmonic-sum factor and the final outward rounded coefficients. The uniform sum/integral argument is the analytic proof in Sections 1–3, not a numerical sample of t.

This package establishes only the stated same-range critical-line bound. It does not assert a new zero-free denominator, a proportion of zeros, global priority, external peer review or RH.
