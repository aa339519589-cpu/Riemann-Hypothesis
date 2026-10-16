# An optimized critical-line boundary and Littlewood denominator 20.1

## Theorem

For every real t with |t|≥3, the Riemann zeta function has no zero in

σ > 1 − log log|t| / (20.1 log|t|).

This is a consequence of published analytic estimates, a new certified parameter choice in the Hiary–Patel–Yang critical-line argument, and a whole-height interval certificate. It uses the already proved classical denominator 4.82, not any newer classical feedback theorem. No unpublished thesis bound is assumed.

The new critical-line parameter choice also gives the standalone estimate

|ζ(1/2+it)| ≤ (.4467 log t + 4.940)t^(1/6), t≥exp(50).       (A)

The finite-height sub-Weyl constants used below are explicitly stated interval bounds in Patel–Yang, not extrapolations from sampled heights. A global 66.7 bound remains in every interpolation boundary.

## 1. Published ingredients

The full explicit-formula and local zero inequality are those of Andrew Yang, *Explicit bounds on ζ(s) in the critical strip and a zero-free region*, J. Math. Anal. Appl. 534(2), 128124 (2024), DOI [10.1016/j.jmaa.2024.128124](https://doi.org/10.1016/j.jmaa.2024.128124), version-pinned [arXiv:2301.03165v2](https://arxiv.org/abs/2301.03165v2). We retain its degree-46 detector, smoothing function, isolated-zero term, complete zero-count remainder, pole and right-shift integral. The [20.4 report](../20261016_local_littlewood_204/REPORT.md) and [20.15 interpolation report](../20261016_critical_interpolation_littlewood_2015/REPORT.md) state and verify those unchanged ingredients.

Their fixed detector has b0=1, b1≤1.747088, and b=Σ(j≥1)bj≤3.574410. Its smoothing remainder satisfies c(R)≤1+10.05/R for R≥100. The present verifier repeats the same fixed-detector theta enclosure and c(R) calculation. Yang's k=4 critical-strip estimate is

|ζ(5/7+it)|≤1.546 t^(1/14)log t, t≥3.                       (1.1)

We use Hiary–Patel–Yang, *An improved explicit estimate for ζ(1/2+it)*, [arXiv:2207.02366v1](https://arxiv.org/abs/2207.02366v1), abbreviated HPY, particularly Lemmas 2.1, 2.5 and 2.6 and the complete argument in §3.4. Its already published bounds are

|ζ(1/2+it)|≤.618 t^(1/6)log t, t≥3,

|ζ(1/2+it)|≤(.478013 log t+3.853165)t^(1/6)−2.914229,
t≥10¹².                                                    (1.2)

We also use Patel–Yang, *An explicit sub-Weyl bound for ζ(1/2+it)*, version-pinned [arXiv:2302.13444v1](https://arxiv.org/abs/2302.13444v1). Theorem 1.1 gives 66.7t^(27/164) for every t≥3. Section 3.1 explicitly asserts that each row of Table 1 gives |ζ(1/2+it)|≤A t^(27/164) throughout that row's closed interval.

The low-height input is the [classical denominator 4.82](../20261016_near_zero_littlewood_482/REPORT.md). The high-height input is Mossinghoff–Trudgian–Yang's published Vinogradov–Korobov denominator 55.241, valid for |t|≥3: [Theorem 1.1](https://link.springer.com/article/10.1007/s40993-023-00498-y), [arXiv:2212.06867v1](https://arxiv.org/abs/2212.06867v1).

## 2. Complete HPY parameter substitution

Set T=exp(50), K0=T^(1/3), r=6, and ε=4/3. This ε is the parameter of HPY's third derivative test, not the horizontal shift η used later. For t≥T, take K=ceil(t^(1/3)), n1=floor(sqrt(t/(2π))) and R=floor(n1/K). A safe fixed integer lower bound is R≥R*=1000, because

(sqrt(T/(2π))−1)/(T^(1/3)+1)−1 > 1658.7043 > 1000.

The expression on the left is increasing with T; the same floor estimate therefore holds for every t≥T. In particular r≤R. Let

W*=π(r+1)³, Λ=((r+1)/r)³,

μ=Λ^(2/3)/2 [1+1/((1−1/K0)Λ^(1/3))],

α=1/ε+εμ/(3W*^(1/3))+μ/(3W*^(2/3))
     +32μ sqrt(ε+W*^(−1/3))/(15sqrtπ),

β=32/(3sqrt(πε))+(2−4/π)W*^(−1/3),

ρ=(1+1/R*)/(sqrt2 π^(1/6)),

κ=[α+εαT^(−1/6)ρ+εβT^(−1/6)ρ³(1+T^(−1/3))²]^(1/2),

J=log(1+1/(2R*))+2log(1+sqrt(1+1/(R*+1/2))),

ω=−log(2π)/2+J−2asinh(sqrt(r−1/2)).                         (2.1)

Here W* is a lower bound for every W in the relevant blocks. HPY's monotonicity gives the displayed α and β as uniform upper bounds. The estimates (3.18)–(3.24) in HPY, with J(R*) in place of the coarser 1.412, give

T2 ≤ 2t^(1/6)π^(−1/6)(log t/6+ω)κ
       +sqrt2 t^(1/6)π^(−1/3)sqrt(β(1+1/r)(1+T^(−1/3))).    (2.2)

The factor log t/6+ω is nonnegative already at t=T, as explicitly certified. Thus using an upper κ in the whole product is lawful. We do not multiply a negative ω by an independently rounded upper value and silently assume an upper direction for that isolated term.

HPY's small-block estimate gives

T1 ≤ 4sqrt(r(1+T^(−1/3)))t^(1/6)+I+1.48T^(−1/4)+.127T^(−3/4).

Its I equals 2Σ(n≤N)n^(−1/2)−4sqrtN for an integer N≥1. The elementary integral bound Σ(n≤N)n^(−1/2)≤2sqrtN−1 gives I≤−2, so the final constant is strictly negative.

Combining the complete small and large blocks proves

|ζ(1/2+it)|≤b1 t^(1/6)log t+b2 t^(1/6)+b3,

b1=κ/(3π^(1/6)),

b2=4sqrt(r(1+T^(−1/3)))+2ωκ/π^(1/6)
      +sqrt2 π^(−1/3)sqrt(β(1+1/r)(1+T^(−1/3))),

b3≤−2+1.48T^(−1/4)+.127T^(−3/4).                            (2.3)

The separate 192-bit Arb certificate gives

b1<.446622752866<.4467,
b2<4.938509002168<4.940,
b3<−1.99999448<0.

Rounding the two coefficients upward and dropping the negative constant proves (A). All HPY block, endpoint and Riemann–Siegel remainder terms have been retained.

## 3. Global boundary from the published finite sub-Weyl table

For j=0,…,31 let Lj=60+5j. The published table supplies the following Aj on exp(Lj)≤t≤exp(Lj+5), in the same order:

37.10, 38.09, 39.05, 39.98, 40.88, 41.75, 42.60, 43.41,
44.19, 44.96, 45.70, 46.41, 47.10, 47.76, 48.42, 49.05,
49.66, 50.26, 50.84, 51.39, 51.94, 52.46, 52.97, 53.47,
53.97, 54.43, 54.90, 55.33, 55.75, 56.18, 56.58, 56.98.

For a closed rational cell [l,r]⊂[64,10⁶], set Q=exp(l−5), q=27/164 and define the exact rational maximum

Ktab=max{ Aj/max(l−5,Lj) : 0≤j≤31 ; 66.7/max(l−5,220) }.   (3.1)

For every t≥exp60, the table or the full global theorem applies. Since log|Q+s|≥max(logQ,log|t|) and |s−1|≤|Q+s| on Re s=1/2, (3.1) implies

|(s−1)ζ(s)|≤Ktab |Q+s|^(1+q)log|Q+s|, Re s=1/2.           (3.2)

There is no extrapolation of the last finite row: t≥exp220 uses 66.7 throughout.

For the lower heights 3≤t≤exp60, the three intervals [3,10¹²], [10¹²,exp50] and [exp50,exp60] use respectively the first bound in (1.2), the safely rounded second bound with coefficients .478014 and 3.853166, and (A). The verifier certifies, with Δ=1/6−27/164>0,

.618 log(10¹²) exp(Δlog(10¹²))<36,
(.478014·50+3.853166)exp(50Δ)<36,
(.4467·60+4.940)exp(60Δ)<36.

Thus |ζ(1/2+it)|≤36t^q throughout these lower heights. The first table row and logQ≥59 ensure Ktab logQ≥36, since 36·60<37.10·59. This pays (3.2) there too. For |t|≤3 the elementary first Euler summation estimate gives |(s−1)ζ(s)|<20, also below the boundary right side. Negative heights follow by conjugation. Hence (3.2) is a GLOBAL vertical-boundary inequality.

## 4. Fixed-cell interpolation and all harmonic integrals

Two choices of critical boundary are now available:

(K,q)=(.4467+4.940/(l−5),1/6), or (Ktab,27/164).             (4.1)

The first choice follows from (A) when |t|≥exp50. For 3≤|t|≤exp50 the old .618 bound gives |(s−1)ζ(s)|<62exp(50·7/6). The verifier checks that this is below .4467 exp(59·7/6)·59, the new boundary right side's lower bound. For |t|≤3 use the same bound 20. Thus this choice too is global.

The other vertical boundary remains (1.1), with |(s−1)ζ(s)|≤1.546|Q+s|^(15/14)log|Q+s|. Its small-height part is checked explicitly. For t0=exp(l−2), put

v=exp(−3)+(5/7)exp(−l+2),

E=(1+v²)^(7/12)[1+log(1+v²)/(2(l−2))],

α=(14η−4)/3, β=1−α,

Y=αq+β/14, X=E K^α 1.546^β, 2/7≤η≤1/2.                 (4.2)

Yang's Phragmén–Lindelöf Lemma 3.1, applied to the entire function (s−1)ζ(s), gives

|ζ(1−η+iτ)|≤X|τ|^Ylog|τ| for EVERY |τ|≥t0.                 (4.3)

This includes the whole half-line, not just the selected cell. The factors E pay both |Q+s|/|τ| and the logarithm comparison, exactly as in the linked 20.15 proof.

Every harmonic jt of t with logt∈[l,r] satisfies jt≥exp(l)>3t0, and t0≥exp62>3×10¹². Yang's logarithmic-integral Lemma 4.1 therefore applies to all j=1,…,46 with the SAME cell-fixed X,Y,Q, giving

(1/2)∫log|ζ(1−η+ijt+2ηiu/π)|/cosh²u du
≤logX+Ylog(jt)+loglog(jt).                                 (4.4)

The estimates above cover the integration tails as well as its central heights.

## 5. Complete local inequality and genuine minimizing rectangle

Let L1=log(46t+1), L2=logL1. Under the full rectangle hypothesis

1−λ<Re s≤1, t−1≤Im s≤46t+1,

and 0<λ≤1−β≤η/2, λ(R+1)≤η, R≥100, the unchanged explicit formula with (4.4) substituted gives

.17996−.20523((1−β)/λ−1)
≤λ{.087π²b1(1−β)/η²+B/(2η)+c(R)λT},                      (5.1)

B=b[Y(L1−3.377)+L2+logX]+logζ(1+η),

T=b[(.891+.6079ν)(L1−3.377)+(.7813+.58ν)L2+7.329+3.898ν]+1.8,

ν=(η^(−2)+(1−η)^(−2))/2.                                  (5.2)

Here b1 is the detector coefficient from Section 1, not the temporary coefficient b1 in (2.3). The detector harmonic sum, the right-shift integral, pole and full far-zero remainder are unchanged. The discarded local-count coefficient 4(c−1/R)−c/η² is negative for η≤1/2.

The verifier also retains Yang's original discrete-k inequalities for 4≤k≤14, η=k/(2^k−2), with

B=b[(L1−3.377)/(2^k−2)+L2+log1.546]+logζ(1+η),

T=b[(23.99/√η−40.051)(L1−3.377)+1.2031L2−38.58
       +(2.0373L2−.5322logη)/η²]+1.8,                       (5.3)

and the original continuous formula (4.125) at η=2/7. Their hypotheses are unchanged.

Put M1=1/20.1. The verifier checks

4.82log64<20.1,
10⁶/(log10⁶)^4>(55.241/20.1)³.

The classical region pays logt≤64 and the VK region pays logt≥10⁶. If a violating zero existed, the positive global infimum M of (1−β)logt/loglogt over t≥exp64 would be below M1 and attained in the remaining finite range. At a minimizing zero put

1−β=Mlogx/x, λ=M L2/L1, x=logt.

Global minimality and monotonicity of loglogt/logt establish the whole required rectangle above exp64. The possible lower sliver below exp64 is paid by the strict classical inequality 1/(4.82·64)>M1log64/64≥λ. Thus the rectangle is obtained without assuming the proposed result.

## 6. Directed continuum certificate

The verifier uses exact rational cell endpoints. It proposes one of the two critical-line choices, with η=.50,.48,…,.30, or an unchanged discrete-k/continuous witness. Floating computations select a proposal only. Every acceptance is a directed Arb inequality on the entire closed cell.

With δ=10⁻²⁰, define λ1=M1L2/L1 and d1=(1+δ)M1logx/x. Each accepted cell verifies

.17996−.20523[(1+δ)(logx/x)/(L2/L1)−1]
 −λ1{.087π²(1.747088)d1/η²+B⁺/(2η)+(1+10.05/R)λ1T⁺}>0.

It simultaneously checks R≥100, λ1(R+1)≤η, d1≤η/2, and positivity of both brackets multiplied by b before replacing b by its outward upper bound. The finite-table maximum is taken over exact rational numbers. The HPY constant check runs separately at 192 bits, after which the continuum verifier explicitly restores 160-bit precision.

The 160-bit run accepts all 718 closed cells after 1,420 evaluations, with no unresolved interval. The smallest directed margin exceeds 1.71871365412×10⁻⁶. The accompanying scientific summary and full witness list record the complete closed cover of [64,10⁶], all accepted witnesses, directed lower margins and script hashes. Inserting the actual minimizing zero into its cell contradicts (5.1), since λ≤λ1 and 1−β≤d1 and all right-side coefficients are nonnegative. This proves the theorem.

## Reproduction and scope

Run certify_optimized.py with the pinned python-flint dependency of the base package; it imports and checks certify_hpy_constants.py first. An unresolved interval causes a nonzero exit. Keep both scripts, both summaries and the full witness file alongside this report.

The result is an explicit strip-width improvement. It does not count a percentage of excluded zeros and does not prove RH. The finite Table 1 rows and the full infinite tail remain identifiable, separate published inputs.
