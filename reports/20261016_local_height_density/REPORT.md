# A local-height large-values estimate and a short-strip zero-density consequence

Let N(σ; T,T+H) count the nontrivial zeros β+iγ of ζ with β≥σ and T≤γ≤T+H, with multiplicity. Every parameter and positive exponent allowance below is fixed before T tends to infinity. Constants may depend on these fixed parameters. The notation ≺ allows an arbitrarily small positive power of T.

## 1. The density theorem

For (σ,a) in the union of the two closed rectangles
\[
 \mathcal R_1=[17/20,87/100]\times[5/6,23/25],\qquad
 \mathcal R_2=[87/100,9/10]\times[3/4,43/50],
\]
put η=1−σ and
\[
 B=\max\left\{
 \frac1{\sigma+1/2},\frac{2(178a+365)}{2742\sigma-1015},\frac{3a}{4\sigma}
 \right\},\qquad E=2\eta B.\tag{1}
\]
Then, for every ε>0,
\[
 \boxed{N(\sigma;T,T+T^a)\ll_{\sigma,a,\varepsilon}T^{E+\varepsilon}.}\tag{2}
\]
For example,
\[
 E(43/50,5/6)=10780/50367,\qquad
 E(43/50,9/10)=189/860,\qquad E(9/10,3/4)=1/7.
\]
This strictly improves the identified short-strip exponent 2a(1−σ) on the whole stated union. It also strictly improves the identified global coefficient 3(1−σ)/(2σ), and the specified preceding density bounds wherever their stated intervals overlap. These are bounded comparisons, not a claim of exhaustive worldwide novelty. No effective constant, finite-height exclusion, actual-zero percentage, or assertion of RH is made.

The new analytic ingredient is a local-height version of an Atkinson/Halász–Montgomery argument. It retains the one-cell contribution when the ordinate interval is shorter than a phase cell. This is then used inside the complete Möbius detector, including its unpowerable long blocks. The absolute height T and the interval length T^a remain distinct throughout.

## 2. Analytic inputs and their precise scope

We use the following already established inputs.

1. The global exponent pair (89/1282,997/1282) and its B-transform
\[
 (k,l)=(178/641,365/641).\tag{3}
\]
The pair and its provenance are recorded in [1, Section 1] and the primary exponent-pair source [2]. Its application below is to coefficient-one correlation sums for the model phase √x plus the small cubic perturbation, not to arbitrary-coefficient correlations.

2. The Atkinson upper bound, phase reduction, and removal of partial-sum maxima in de Faveri–Pandey [3, Lemmas 7.1, 7.3, Corollary 7.2 and the proof surrounding (55)–(57)]. In particular the phase reduction allows
\[
 T^{1/3}\ll N\ll TG^{-2}(\log T)^2,\quad
 N\le W\le\sqrt{TN},\quad N^{1/2}W^2\le T^{3/2}.\tag{4}
\]
We do not invoke that paper's special exponential-sum large-values theorem, its additional W≤N^(4/3) restriction, or its close-pair/Iwaniec input.

3. Lewko's translated-interval Dirichlet-polynomial large-values theorem [4]. For coefficients bounded by one, a 1-separated set in any interval of length U, at which a dyadic polynomial of length N has absolute value at least V, satisfies
\[
 R\ll_{\kappa,\varepsilon}U^\varepsilon
 \left(N^2V^{-2}+N^3U^{1/2}V^{-4}\right),\tag{5}
\]
when U^(1/3)≤N≤U and V≥N^(3/4+κ), for fixed κ>0. Its exact source declaration is `MathCollab.Density.large_values`. The earlier source comparison [5] records a substantive mathematical/source inspection, but no independent Lean build or complete kernel/foundation replay. We cite this primary theorem without upgrading that verification status.

We also use Bourgain's pointwise exponent 13/84, polynomial growth of ζ on fixed vertical strips, the local zero count O(log T) in a unit interval at height comparable to T, and the ordinary smoothed Möbius detector. The detector is displayed in Ye [6, Section 2]; its smooth-block variant is also in [4, `Stronger/SmoothContour` and `Stronger/LongBlockDetection`]. No quasi-Riemann hypothesis or prime-sum application from [6] is imported.

## 3. Local-height critical-line large values

Let I be any interval of length at most C T^a contained in a fixed comparable-height range [cT,CT], where 3/4≤a≤23/25. For a 1-separated set in I on which |ζ(1/2+it)|≥T^v, write its size as R_I(v). We prove, for
\[
 v_*:=365/2742<v\le13/84,
\]
\[
 R_I(v)\prec T^{L_a(v)},\qquad
 L_a(v)=\max\left\{1-6v,\ a-1+\frac{543}{178}-\frac{1727}{89}v\right\}.\tag{6}
\]
The strict lower endpoint supplies a fixed margin; all levels used later stay a fixed distance above it.

### 3.1 Phase cells, including the first cell

Set G=T^(2v)(log T)^−100. The standard clustering and Atkinson argument in [3] produces clusters of comparable multiplicity F≥1, 2G-separated centers, and a common dyadic length N in (4). Since G≪T^a, centers and their smoothing neighborhoods remain in an interval of length O(T^a), not in an interval of length T merely by convention.

Choose W obeying (4). A phase cell has original ordinate length comparable to W√(T/N). Consequently the number of cells intersecting the localized center interval is
\[
 J\ll1+T^a\sqrt{N/T}/W.\tag{7}
\]
The coefficients within each cell may depend on the cell, as in the primary proof. Removing maxima in the summed inequality and dyadically selecting a magnitude gives a common Z and total retained count R1 with
\[
 Z\succ F(TN)^{1/4},\qquad R_1Z\succ R_I(v)(TN)^{1/4}.\tag{8}
\]
The transformed points in a cell have spacing ≫G√(N/T). Partitioning them into 1-separated sets costs
\[
 O(1+G^{-1}\sqrt{T/N})\prec G^{-1}\sqrt{T/N},\tag{9}
\]
where the last inequality uses N≲TG^(−2) up to the existing logarithmic factors. The total number of parts is therefore
\[
 \prec\frac{\sqrt{T/N}}G+\frac{T^a}{GW}.\tag{10}
\]
Neither the +1 in (7) nor the factor F in (8) has been discarded prematurely.

### 3.2 The complete correlation range

For one part of cardinality R′, Halász–Montgomery duality gives a diagonal and a correlation sum with coefficients exactly one. The phases are
\[
 \phi_\theta(x)=\sqrt{x}+\theta x^{3/2},\qquad\theta=O(N/T).
\]
For 1≤|u|≤N, the first-derivative estimate is O(N/|u|); unit spacing pays its entire row, together with the diagonal, by O(N²R′ log T) after the outer factor N. For N<|u|≤W, (3) gives
\[
 \left|\sum_{N<m\le2N}e(u\phi_\theta(m/N))\right|
 \prec |u|^k N^{l-k}.
\]
The small perturbation tends to zero in every fixed normalized derivative, uniformly over the lengths used here. Thus it suffices that
\[
 k w+(l-k)n<(1-n)/2,\qquad N=T^n,\quad W=T^w,\tag{11}
\]
to absorb the off-diagonal term using Z²/N≻F²T^((1−n)/2). The complete range N<|u|≤W is paid because its displayed upper bound increases in |u|. This is not a local bound substituted into an uncontrolled supremum.

After absorption, R′≺N²/Z². Summing (10) and then using both inequalities in (8) gives
\[
 R_I(v)\prec\frac1F\left(\frac NG+
 \frac{T^aN^{3/2}}{T^{1/2}GW}\right)
 \le\frac NG+\frac{T^aN^{3/2}}{T^{1/2}GW}.\tag{12}
\]
The first term is the retained one-cell contribution.

### 3.3 Every Atkinson length and every higher level

For 1/3≤n≤1−4v, take, before a fixed small loss,
\[
 w(n)=\min\left\{\frac{641-1015n}{356},\ \frac34-\frac n4\right\}.\tag{13}
\]
The first entry is exactly the equality in (11), and the second pays phase truncation. Because v>365/2742, we have n<641/1371; hence both entries exceed n. Both are compatible with W≤√(TN), since the second is at most (1+n)/2 for n≥1/3. Also n≤641/1371<3/5, as required by the primary phase reduction. Shrinking W by a fixed sufficiently small power gives strict absorption and preserves every cap.

The exponent of the first term in (12) is n−2v. The second is the maximum of two affine functions in n with positive slopes. Its worst length, and that of the first term, is n=1−4v. Therefore the resulting bound is
\[
 \max\{1-6v,\ a-1+543/178-(1727/89)v,\ a+1/2-9v\}.\tag{14}
\]
The second and third entries cross at v=69/463. Below that point the second is larger. Above it, since a≤23/25 and v≥69/463,
\[
 a+1/2-9v\le1-6v
\]
with a fixed margin. Thus (14) reduces to (6). This proves the full local-height envelope through Bourgain's pointwise cutoff, not only at a chosen level. A fixed small enlargement of that cutoff is harmless, and larger levels are absent for sufficiently large T after the pointwise exponent allowance is chosen.

All fixed logarithmic factors, endpoint powers, compact comparable-height changes and normalization losses are absorbed by first choosing a small slack and then taking T large. If the Atkinson length interval is empty, the large-value alternative itself is absent; no missing length contributes.

## 4. A localized truncated moment and weighted-mean count

Both slopes of L_a are strictly less than −2. Dyadic integration of (6) over all levels above a fixed v>v_* therefore yields, uniformly for intervals I as above,
\[
 \int_I|\zeta(1/2+it)|^2\mathbf1_{|\zeta|\ge T^v}\,dt
 \prec T^{L_a(v)+2v}.\tag{15}
\]
A maximal 1-separated subset of each level set bounds its measure by a fixed multiple of its cardinality. The pointwise bound terminates the level integration. Thus (15) needs no unproved passage from a dyadic height envelope to all smaller absolute heights.

Fix a sufficiently large integer A and define
\[
 J_A(t)=\int_{\mathbb R}(1+|u|)^{-A}|\zeta(1/2+i(t+u))|\,du.
\]
Suppose a collection of zeros with ordinates in [T,T+T^a], counted with multiplicity, has J_A(γ)≥T^(v−d). Then
\[
 \#\{\rho\}\prec T^{L_a(v)+O(d)}.\tag{16}
\]
To verify the complete kernel payment, put K_A=∫(1+|u|)^−A du. Remove the part where |ζ|<T^(v−d)/(2K_A); it contributes at most half the lower bound. Weighted Cauchy–Schwarz gives
\[
 T^{2(v-d)}\ll_A\int_{\mathbb R}(1+|u|)^{-A}|\zeta(1/2+i(\gamma+u))|^2
 \mathbf1_{|\zeta|\ge T^{v-d}/(2K_A)}\,du.
\]
Sum over the original zeros. Local zero counting bounds the sum of translated kernels by O(log T), including multiplicity. On the enlarged interval [T−T^d,T+T^a+T^d], where d<a, (15) applies with length O(T^a) and the small threshold loss. Outside it, distance from every zero is at least T^d. Polynomial growth on comparable heights and the crude O(T log T) total zero count pay this portion by taking A sufficiently large after d. The farther tails are paid by the same polynomial-growth estimate and integrability at infinity. Thus no arbitrary smooth Mellin kernel is falsely assigned exponential decay, and no weighted mean lower bound is substituted for a pointwise large value.

## 5. The two-scale zero detector

Fix σ>3/4 and B<a with 2B>a. Take Y=T^B and X=T^δ for sufficiently small fixed δ>0, and set
\[
 M_X(s)=\sum_{d\le X}\mu(d)d^{-s},\qquad
 b_X(n)=\sum_{d\mid n,\ d\le X}\mu(d).
\]
The usual Gamma identity at a zero ρ gives a smoothed tail Σ_(n>X)b_X(n)n^(−ρ)e^(−n/Y) and a critical-line integral bounded by
\[
 C_A\sqrt X\,Y^{1/2-\beta}J_A(\gamma).
\]
The pole at 1 has exponentially small Gamma residue at γ≥T. Truncation at Y(log T)² is negligible. Consequently either the integral is large or one of O(log T) smooth dyadic tail blocks is large.

For every block of length M>√Y, move its smooth Mellin representation to the critical line. This bounds its magnitude by
\[
 C_A\sqrt X\,M^{1/2-\beta}J_A(\gamma)+O(T^{-100}).\tag{17}
\]
For a fixed compactly supported dyadic cutoff w, the weights w(x)e^(−qx), q=M/Y≥0, have uniformly bounded Mellin-decay seminorms of every fixed order: their support stays away from zero and q^j e^(−cq) is bounded. The ζ-pole residue is rapidly small in γ. The entire polynomial-decay J_A kernel is retained, not truncated at a logarithmic height. Since |M_X(1/2+it)|≪√X, this proves (17) with the complete original pole and contour.

Both the initial integral and every large block above √Y force
\[
 J_A(\gamma)\ge T^{B(\sigma-1/2)/2-O(\delta)-o(1)}.
\]
Thus (16) pays them by exponent L_a(B(σ−1/2)/2) plus arbitrarily small losses.

For a remaining block X/C≤M≤√Y, Fourier inversion in log(n/M) moves β to the common fixed line σ. The kernels are uniformly Schwartz for β−σ∈[0,1−σ]. Truncating shifts at T^d is legitimate after sufficiently many integrations by parts. Extracting zeros 4T^d apart costs O(T^d log T), including multiplicities; their shifted large values remain 1-separated in an interval of length at most 2T^a and use the same fixed block polynomial.

Write M=T^m and choose j=ceil(2B/(3m)). Every 0<m≤B/2 satisfies
\[
 2B/3\le jm\le B.\tag{18}
\]
For m≤B/3 this follows from jm<2B/3+m≤B; for B/3<m≤B/2 one has j=2. Since M≥X/C, j is bounded before T. Raising to these bounded integer powers, splitting product supports dyadically and normalizing divisor-bounded coefficients costs only an arbitrarily small fixed power. The resulting lengths cover the complete interval T^(2B/3−o(1))≤N≤T^(B+o(1)), with large-value threshold N^(σ−o(1)). Fixed κ>0 in (5) remains available because σ>3/4.

The strict length margins B<a and 2B>a give (2T^a)^(1/3)≤N≤2T^a. Applying (5) pays every short block by
\[
 \max\{2\eta B,\ a/2+(3-4\sigma)2B/3\}.
\]
We have therefore proved the complete transfer
\[
 N(\sigma;T,T+T^a)\prec
 T^{\max\{2\eta B,\ a/2+(3-4\sigma)2B/3,\ L_a(B(\sigma-1/2)/2)\}}.\tag{19}
\]
The long-block split is essential: arbitrary lengths between √Y and Y^(2/3) cannot be powered into [Y^(2/3),Y]. All losses δ,d, coefficient bounds and correlation slacks are chosen sufficiently small, after fixing σ,a,B, before T. Their total is absorbed into the prescribed ε.

## 6. Exact specialization and bounded comparisons

For B in (1), set v=B(σ−1/2)/2. The accompanying rational certificate proves, on both complete two-variable rectangles,
\[
 B<a,\quad2B>a,\quad365/2742<v<69/463,\quad B\ge1/(\sigma+1/2).
\tag{20}
\]
The second branch in (1) is exactly the solution of
\[
 a-1+543/178-(1727/89)v=2\eta B.
\]
The first branch in (1) and the last inequality in (20) make 1−6v≤2ηB. The third branch in (1) ensures
\[
 a/2+(3-4\sigma)2B/3\le2\eta B.
\]
Thus (19) proves (2). Where either the one-cell or short off-diagonal comparison is an equality, take B+ξ for an arbitrarily small fixed ξ>0, preserving all strict ranges, and then absorb the change of 2ηB into ε. The same fixed-loss passage pays coefficient normalizations and all count/contour endpoint losses. No endpoint limit is taken before the analytic estimates are available.

Ye [6, Theorem 1.2/(1.3)] gives exponent 2aη in the present σ range. His β>σ convention is converted to β≥σ by applying it at a fixed σ′<σ and absorbing the continuous coefficient change into ε. The strict inequality B<a proves the claimed improvement. The certificate also proves 4σB/3<1, hence improvement over the identified global Lewko/Kerr exponent 3η/(2σ). On every applicable interval it also checks the correctly switched identified density table, the seven-piece Halász envelope [8], all four branches of the full-diagonal CDV theorem [7], both low-interval EP-Gram expressions [9], and both branches of the newer global local-LV density theorem [1]. Each comparison is restricted to that predecessor’s actual stated interval; no gap at the table jump σ=279/314 is omitted.

For a transparent supplementary comparison, the certificate also checks the global-height-moment detector baseline E_old=2ηB_old, where B_old=120/(318σ−125) on [775/906,625/726] and B_old=213/[5(102σ−35)] on [625/726,2905/3354]. The present result strictly improves that expression over its stated rectangle. This supplementary baseline is a consequence of the global-height moment transfer, not an additional external literature claim. None of these comparisons converts an exponent saving into a percentage of actual zeros.

## References

[1] [Local critical-line large values and a length-adapted density refinement](../20261016_local_zeta_lv_density/REPORT.md), published commit 4cbb53f654fca761d5d5493352d4107c2283410d. Its full global-height Atkinson/HM derivation is the predecessor of the localization here.

[2] [Analytic Number Theory Exponent Database, exponent-pair chapter](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html), pair (89/1282,997/1282), together with the B-process. The exact pair and source provenance were independently checked in [1].

[3] Alexandre de Faveri and Mayank Pandey, *The sixth moment of the Riemann zeta function*, arXiv:2610.01035v1, Sections 7 and 9. https://arxiv.org/html/2610.01035v1 . Only the displayed Atkinson/phase/maxima machinery is used, not the later special large-value theorem or close-pair estimate.

[4] Mark Lewko, *Zero-density estimates from an improved large-values bound*, registered source commit ee2a8a32be49a4f73c7386e9dffdea24d7e3d8c0. https://github.com/mrklwk/zeta-density-39-over-17-lean/tree/ee2a8a32be49a4f73c7386e9dffdea24d7e3d8c0 . Exact declaration: `lean/MathCollab/Density/LargeValues.lean`, `MathCollab.Density.large_values`.

[5] [Prior-source comparison and verification scope](../20261016_density_prior_source_comparison/REPORT.md), published commit 41fdc78261048f8448180104f6d9ebe5de035b3b. No independent Lean build or full kernel/foundation replay is claimed here.

[6] Yangbo Ye, *Zero density in short strips and short-interval bounds toward Hypothesis S*, arXiv:2610.15989v2, Section 2 and Theorem 1.2. https://arxiv.org/html/2610.15989v2 . Only the unconditional detector and identified short-strip comparator are used.

[7] [Full-diagonal CDV density refinement](../20261016_cdv_full_diagonal_density/REPORT.md), published commit f2489298e295c5d03cfd4639e6962ebf4a38bc0e.

[8] [Finite-pair/local-beta Halász envelope](../20261016_halasz_local_envelope/REPORT.md), published commit 62323ad62b68c70a8e5538414dd349197c0dda68.

[9] [Coefficient-one EP-Gram density refinement](../20261016_cdv_ep_gram_density/REPORT.md), published commit 1c49e1247f459458632d83ceb5cde1eb657042fc.
