# A block-dependent critical-line estimate

## Theorem

For every t≥exp(50),

|ζ(1/2+it)| ≤ (.40312 log t+3.240)t^(1/6).                 (1)

The new step retains the dependence of the derivative-test constants on each block index. The first 997 corrections are paid by an exact finite sum; only the remaining tail uses a common constant. This is combined with the complete unsplit-square-root integral bound, not with a deletion of its remainder.

## 1. Source and fixed parameters

Use Hiary–Patel–Yang, *An improved explicit estimate for ζ(1/2+it)*, [arXiv:2207.02366v1](https://arxiv.org/abs/2207.02366v1), Lemmas 2.1, 2.5 and 2.6 and Section 3.4. The complete block normalization and the uniform unsplit integral are also recorded in the independently proved [unsplit HPY report](../20261016_unsplit_hpy_critical_bound/REPORT.md). All endpoint and Riemann–Siegel remainder terms in that source are retained here.

Set T=exp(50), K0=T^(1/3), ε=7/5, r0=3, r1=1000 and R*=1000. For every t≥T let

K=ceil(t^(1/3)), n1=floor(sqrt(t/(2π))), R=floor(n1/K).

As in the source floor bounds,

R≥(sqrt(T/(2π))−1)/(T^(1/3)+1)−1>1658.7043>1000,
R≤t^(1/6)/sqrt(2π).                                      (2)

The lower continuous expression is increasing in T. Hence all of the first 997 indices r=3,…,999 occur in the sum, and the tail beginning at r1 is nonempty throughout the stated range.

For every integer r≥r0, define

W_r=π(r+1)^3, Λ_r=((r+1)/r)^3,

μ_r=[Λ_r^(2/3)+Λ_r^(1/3)/(1−1/K0)]/2,

α_r=1/ε+εμ_r/(3W_r^(1/3))+μ_r/(3W_r^(2/3))
     +32μ_r sqrt(ε+W_r^(−1/3))/(15sqrtπ),

β_r=32/(3sqrt(πε))+(2−4/π)W_r^(−1/3),

ρ=(1+1/R*)/(sqrt2 π^(1/6)),

κ_r=[α_r+εα_r T^(−1/6)ρ
          +εβ_r T^(−1/6)ρ³(1+T^(−1/3))²]^(1/2).          (3)

These are blockwise upper parameters, not newly chosen derivative-test assumptions. Each source block has W≥W_r and its derivative ratio at most Λ_r. The original monotonicity argument giving a uniform α and β therefore applies separately to each r and gives exactly (3). The common ε is fixed at 7/5 throughout.

All α_r, β_r and κ_r are nonincreasing in r: W_r increases, Λ_r decreases, and μ_r is explicitly increasing in Λ_r. Every coefficient in (3) is positive, including 2−4/π. This also proves the required infinite-tail monotonicity, rather than inferring it from the finite numerical checks.

## 2. Complete block sum with a finite correction

Let κ*=κ_(r1), and put

C²=β_(r0)π^(2/3)(1+1/r0)(1+T^(−1/3)),
d=Ct^(−1/6), g_r=1/sqrt(r(r+1)).

HPY (3.17)–(3.19), retaining all four terms of its B_r, gives

T2≤2t^(1/6)π^(−1/6)Σ(r=r0,…,R)sqrt(B_r/[r(r+1)]),

sqrt(B_r/[r(r+1)])≤sqrt(κ_r²g_r²+d²).                   (4)

The use of the common β_(r0) only in C is an upper bound for every block. The remaining three contributions retain κ_r rather than freezing it at r0.

For fixed g,d>0, the function

j_κ(g)=sqrt(κ²g²+d²)−κg

is nonnegative and decreasing in κ. If r<r1, then κ_r≥κ*, and

sqrt(κ_r²g_r²+d²)
≤κ_r g_r+j_(κ*)(g_r).

If r≥r1, monotonicity instead gives

sqrt(κ_r²g_r²+d²)
≤sqrt((κ*)²g_r²+d²)=κ*g_r+j_(κ*)(g_r).

Consequently the ENTIRE sum in (4) is bounded by

κ*Σ(r=r0,…,R)g_r + S + Σ(r=r0,…,R)j_(κ*)(g_r),           (5)

where the exact finite correction is

S=Σ(r=3,…,999)(κ_r−κ*)/sqrt(r(r+1)).                      (6)

No correction is omitted from a t-dependent prefix: (2) guarantees that all of (6) is present, and including the whole positive sum would in any case be an upper bound.

## 3. Infinite-height remainder and small blocks

Define

J0=log(1+1/(2R*))+2log(1+sqrt(1+1/(R*+1/2))),
ω=−log(2π)/2+J0−2asinh(sqrt(r0−1/2)).

The source harmonic-sum estimate gives Σg_r≤log t/6+ω. Its right side is positive at t=T. The uniform unsplit integral proved in the linked report gives

Σj_(κ*)(g_r)≤κ*J(z*),

J(z)=sqrt(1+z²)−1−log((1+sqrt(1+z²))/2),
z*=(C/κ*)[1/sqrt(2π)+(3/2)T^(−1/6)].                    (7)

For clarity, this bound retains the endpoints: g_r≥1/(r+1/2), the corresponding increasing function h(y)=sqrt((κ*)²/y²+d²)−κ*/y is integrated up to R+3/2, and the index estimate (2) gives exactly z*. Thus (7) holds for every t≥T, not only at the endpoint.

Equations (5)–(7) give

T2≤2t^(1/6)π^(−1/6){κ*[log t/6+ω+J(z*)]+S}.             (8)

The small-block and Riemann–Siegel estimate remains

T1≤4sqrt(r0(1+T^(−1/3)))t^(1/6)
       +I+1.48T^(−1/4)+.127T^(−3/4).

The exact integer sum in I obeys I≤−2 by Σ(n≤N)n^(−1/2)≤2sqrtN−1. Combining T1 and T2 yields

|ζ(1/2+it)|≤b1t^(1/6)log t+b2t^(1/6)+b3,

b1=κ*/(3π^(1/6)),
b2=4sqrt(r0(1+T^(−1/3)))
       +2π^(−1/6){κ*[ω+J(z*)]+S},
b3≤−2+1.48T^(−1/4)+.127T^(−3/4).                         (9)

Only whole positive expressions are upper-bounded before final coefficient evaluation. In particular the negative ω term is never separately rounded in an unjustified direction.

## 4. Directed certificate

The accompanying 192-bit Arb computation evaluates all 997 terms in (6), the exact expressions (2)–(9), and the final outward rounded coefficients. It gives

S=.3453925229884326…,
κ*=1.4635494160805249…,
z*=1.0531948174464386…,
J(z*)=.2484297988389344…,

b1<.403113946755<.40312,
b2<3.239451590250<3.240,
b3<−1.99999448<0.

The program also verifies the fixed index lower bound and all finite-prefix positivity and monotonicity checks; the infinite-tail monotonicity is proved analytically in Section 1. Rounding b1,b2 upward and dropping the negative b3 proves (1).

Run `certify_blockwise_hpy.py` with python-flint 0.9.0 / FLINT 3.6.0. The scientific JSON pins the exact program. No floating approximation or sampled t value authorizes an assertion.

## Scope

This is a complete same-range critical-line bound. It is not by itself a new zero-free-region theorem, a proportion of excluded zeros, a global-priority claim, external peer review or RH.
