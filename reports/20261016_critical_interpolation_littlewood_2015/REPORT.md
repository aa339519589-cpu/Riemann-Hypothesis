# Complementary published critical-line bounds give Littlewood denominator 20.15

## Theorem

For every real t with |t|≥3, the Riemann zeta function has no zero in

σ > 1 − log log|t| / (20.15 log|t|).

This theorem uses published analytic inputs and the previously checked unconditional classical denominator 4.82. It does not assume the unpublished 19.62 estimate. It is a zero-free-region result, not a proportion-of-zeros statement or a proof of RH.

## 1. Published inputs

We retain Andrew Yang's fixed degree-46 detector and compact smoothing function from *Explicit bounds on ζ(s) in the critical strip and a zero-free region*, J. Math. Anal. Appl. 534(2), 128124 (2024), DOI [10.1016/j.jmaa.2024.128124](https://doi.org/10.1016/j.jmaa.2024.128124), version-pinned [arXiv:2301.03165v2](https://arxiv.org/abs/2301.03165v2). The local zero inequality, complete zero-count remainder, and smoothing constant are retained from Lemma 4.8 and the derivation of (4.125).

The [denominator 20.4 report](../20261016_local_littlewood_204/REPORT.md) states these inequalities and certifies the unchanged fixed-detector bounds

b0=1, b1≤1.747088, b=Σ(j≥1)bj≤3.574410,

c(R)≤1+10.05/R, R≥100.

The present verifier independently repeats the same theta enclosure and c(R) certificate. The numbers .17996 and .20523 remain the published rounded constants for the unchanged detector.

We use two complementary critical-line estimates.

1. Hiary–Patel–Yang, *An improved explicit estimate for ζ(1/2+it)*, version-pinned [arXiv:2207.02366v1](https://arxiv.org/abs/2207.02366v1), Theorem 1.1 and the last display of §3.4, prove respectively

   |ζ(1/2+it)|≤.618 t^(1/6)logt, t≥3,

   |ζ(1/2+it)|≤.478013 t^(1/6)logt+3.853165 t^(1/6)−2.914229, t≥10^12.

   We safely increase the two positive coefficients to .478014 and 3.853166 and discard the negative constant.

2. Patel–Yang, *An explicit sub-Weyl bound for ζ(1/2+it)*, version-pinned [arXiv:2302.13444v1](https://arxiv.org/abs/2302.13444v1), Theorem 1.1, proves

   |ζ(1/2+it)|≤66.7 t^(27/164), t≥3.

Yang's Theorem 1.1 at k=4 supplies |ζ(5/7+it)|≤1.546 t^(1/14)logt for t≥3. The far-height input is the published Mossinghoff–Trudgian–Yang Vinogradov–Korobov denominator 55.241, valid for |t|≥3: [Theorem 1.1](https://link.springer.com/article/10.1007/s40993-023-00498-y), [arXiv:2212.06867v1](https://arxiv.org/abs/2212.06867v1). The low-height input is the [unconditional classical denominator 4.82](../20261016_near_zero_littlewood_482/REPORT.md).

## 2. A finite-cell critical-strip interpolation

Let [l,r] be a closed rational cell in [65,10^6], and set

Q=exp(l−5), t0=exp(l−2),

v=(Q+5/7)/t0=exp(−3)+(5/7)exp(−l+2),

E=(1+v²)^(7/12) [1+log(1+v²)/(2(l−2))].              (2.1)

Two alternative boundary pairs are available. Write (K,q) for either

K=.478014+3.853166/(l−5), q=1/6,                     (2.2H)

or

K=66.7/(l−5), q=27/164.                              (2.2S)

For f(s)=(s−1)ζ(s), these give the GLOBAL vertical-boundary estimates

|f(s)|≤K |Q+s|^(1+q)log|Q+s|, Re s=1/2,

|f(s)|≤1.546 |Q+s|^(15/14)log|Q+s|, Re s=5/7.       (2.3)

Here is an explicit check that no low-height boundary is omitted. For |t|≥10^12, (2.2H) follows from the sharper HPY bound, |s−1|≤|Q+s|, log|Q+s|≥logQ and log|t|≤log|Q+s|. For 3≤|t|≤10^12, the .618 bound gives |f(s)|<4×10^15. This is less than .478014 exp(70)·60, a lower bound for the right side of (2.3) since Q≥exp60. For |t|≤3 and 1/2≤Re s≤5/7, the first Euler summation formula gives

|f(s)|≤1+|s−1|/2+|s(s−1)|/(2 Re s)<20.

This also lies below every boundary right side. The sub-Weyl branch for |t|≥3 follows from log|Q+s|≥logQ; its low-height right side is at least 66.7 exp(60·191/164)>20. The 5/7 boundary for |t|≥3 is Yang's theorem, and its low-height right side is at least 1.546 exp(60·15/14)·60>20. Negative heights follow by conjugation.

Apply Yang's Phragmén–Lindelöf Lemma 3.1 to the entire function f(s). Its growth hypothesis holds by the ordinary polynomial vertical growth of ζ on this fixed strip. For 2/7≤η≤1/2, put

α=(14η−4)/3, β=1−α,

Y=αq+β/14, X=E K^α 1.546^β.                         (2.4)

Then for every |τ|≥t0,

|ζ(1−η+iτ)|≤X |τ|^Y log|τ|.                         (2.5)

Indeed, the interpolated power of |Q+s| is 1+Y≤7/6. Division by |s−1|≥|τ| and comparison |Q+s|≤|τ|sqrt(1+v²) gives the first factor of E; comparison of logarithms gives the second. This proves (2.5) on the WHOLE required half-line, not merely at the selected zero ordinate.

For a zero ordinate t with logt in [l,r], every harmonic jt, 1≤j≤46, satisfies jt≥exp(l)>3t0, since exp2>3. Also t0≥exp63>3×10^12, η≥2/7>(jt)^−1, and the integral shift 2η/π≤1/π<1/2. Therefore all hypotheses of Yang's integral Lemma 4.1 hold. It yields

(1/2)∫ log|ζ(1−η+ijt+2ηiu/π)| / cosh²u du
≤logX+Ylog(jt)+loglog(jt).                           (2.6)

The parameter Q is fixed for the cell, and the same X,Y are used for all its harmonics. Thus there is no inconsistency from changing a bound inside an integral.

## 3. Complete local zero inequality with the new main term

Let L1=log(46t+1), L2=logL1. Assume a zero β+it satisfies

0<λ≤1−β≤η/2, λ(R+1)≤η, R≥100,

and the full rectangle 1−λ<Re s≤1, t−1≤Im s≤46t+1 is zero-free. Retain Yang's entire proof of the local inequality, replacing ONLY its left-shift logarithmic integral by (2.6). The detector estimate

Σ(j≥1)bj log(jt)≤b(L1−3.377)

is unchanged. Since Y>0, the resulting necessary inequality is

.17996−.20523((1−β)/λ−1)
≤λ{.087π²b1(1−β)/η²+B/(2η)+c(R)λT},                (3.1)

where

B=b[Y(L1−3.377)+L2+logX]+logζ(1+η),

T=b[(.891+.6079ν)(L1−3.377)+(.7813+.58ν)L2
       +7.329+3.898ν]+1.8,

ν=(η^−2+(1−η)^−2)/2.                                (3.2)

The complete far-zero estimate remains Yang's Lemma 4.6. The right-shift logarithmic integral, pole, smoothing error, and isolated zero terms remain unchanged. The local zero-count coefficient is nonpositive because 4(c−1/R)−c/η²<0 for η≤1/2, so its removal is in the same valid direction as in the original proof. No stronger estimate for it is assumed.

For η=k/(2^k−2), 4≤k≤14, we also retain Yang's original Lemma 4.8 exactly, with

B=b[(L1−3.377)/(2^k−2)+L2+log1.546]+logζ(1+η),

T=b[(23.99/√η−40.051)(L1−3.377)+1.2031L2−38.58
       +(2.0373L2−.5322logη)/η²]+1.8.                (3.3)

The subsidiary t≥2^k condition is satisfied throughout the certified range. The verifier may also use the unchanged continuous-η formula (4.125) at η=2/7.

## 4. Whole-height contradiction and genuine rectangle

Put M1=1/20.15. Outward arithmetic verifies

4.82 log65<20.15,                                   (4.1)

10^6/(log10^6)^4>(55.241/20.15)^3.                   (4.2)

Thus the classical region proves the theorem when 3≤t≤exp65. The VK region proves it when logt≥10^6, since x/(logx)^4 is increasing for logx>4.

If the claimed region contained a zero, define M as the infimum of (1−β)logt/loglogt over zeros with t≥exp65. A violating zero gives M<M1. The high-height comparison excludes all values below M1 beyond exp(10^6). There are only finitely many zeros in the remaining compact height range, and the classical region makes their distances from 1 strictly positive. Consequently 0<M<M1 is attained by a zero with x=logt in [65,10^6]. Set

1−β=M logx/x, λ=M L2/L1.                            (4.3)

Monotonicity of loglogy/logy gives λ≤1−β. For any zero ordinate γ between t−1 and46t+1 with γ≥exp65, global minimality gives 1−β′≥Mloglogγ/logγ≥λ. The possible lower sliver γ<exp65 is paid by

1−β′>1/(4.82·65)>M1log65/65≥λ.

Hence the FULL local rectangle required in Section 3 is established, rather than assumed. The same argument applies independently to whichever cell contains x.

## 5. Outward continuum certificate

The verifier uses 160-bit Arb arithmetic. For each rational cell it proposes either (2.2H), (2.2S), an unchanged discrete-k witness, or the unchanged continuous witness η=2/7. Interpolation η choices are .50,.48,...,.30. R is an integer. Floating-point scores propose choices only; all acceptance decisions use directed interval bounds on the entire closed cell.

With ε=10^−20, set

λ1=M1L2/L1, d1=(1+ε)M1logx/x,

Aleft=.17996−.20523[(1+ε)(logx/x)/(L2/L1)−1].

The certified margin is

Aleft−λ1{.087π²(1.747088)d1/η²+B⁺/(2η)
               +(1+10.05/R)λ1T⁺}>0,               (5.1)

where B⁺,T⁺ use b⁺=3.574410. Every cell also verifies R≥100, λ1(R+1)≤η, d1≤η/2, and positivity of each bracket multiplied by b before replacing b by b⁺. The interpolation boundary checks and both height splices are verified as well.

All 1,602 closed cells were accepted after 3,188 evaluations, with no pending cell. The smallest directed margin exceeds 4.1949176584×10^−7. The witness list gives exact rational endpoints, branch, η, R, and lower margin. The initial intervals cover [65,10^6] exactly; bisection preserves that cover.

For the actual minimizing zero, λ≤λ1 and 1−β≤d1. The complete right side of (3.1) is bounded above by the quantity subtracted in (5.1), because all involved coefficients are nonnegative. Its left side is at least Aleft. This contradicts (5.1), completing the proof. Conjugation gives negative ordinates.

## 6. Reproduction and scope

Run `certify_interpolation.py` in the pinned python-flint environment of the base zero-free package. It writes the scientific summary and complete witness list and exits unsuccessfully if any cell is unresolved. The analytic interpolation and rectangle proof above are necessary alongside the numerical certificate.

The comparison 21.233/20.15 is a factor in Littlewood strip width, not a percentage of zeros. The theorem uses no unexamined 2026 critical-line claim or unpublished thesis estimate. No claim of global priority is made over results whose hypotheses or proofs have not been checked.
