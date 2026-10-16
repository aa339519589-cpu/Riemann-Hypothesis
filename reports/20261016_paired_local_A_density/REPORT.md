# Two linked zero-density corollaries from one local A-process bound

Let \(N(\sigma,T)\) count nontrivial zeta zeros \(\beta+i\gamma\), with multiplicity, satisfying \(\beta\geq\sigma\) and \(0<|\gamma|\leq T\).

**Theorem.** For every fixed \(\sigma\) in the indicated interval and every \(\varepsilon>0\), the following unconditional bounds hold:
\[
\boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}
T^{\frac{2276(1-\sigma)}{6738\sigma-4422}+\varepsilon}}
\quad\left(\frac{937}{1000}\leq\sigma\leq\frac{469}{500}\right),
\tag{1}
\]
\[
\boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}
T^{\frac{1707(1-\sigma)}{12907\sigma-10591}+\varepsilon}}
\quad\left(\frac{1937}{2000}\leq\sigma\leq\frac{969}{1000}\right).
\tag{2}
\]
Thus the intervals are respectively \([.937,.938]\) and \([.9685,.969]\). Both conclusions follow from established Huxley bounds, a complete local A-process calculation, established exponent pairs and the established subdivision density conversion. No new exponential-sum or mean-square input is asserted.

Both bounds strictly improve the identified density-table branches throughout their intervals. Bound (1) also improves the previously recorded growth-only hybrid [5]. The complete declared-growth comparisons in Section 5 show that neither bound is supplied by the pure-growth hybrid or by Pintz's separate theorem using that family.

At \(\sigma=.938\), the exponent in (1) is \(35278/474561\), with saving \(3667114/14199339681\) against [5]. At \(\sigma=.969\), the exponent in (2) is \(52917/1915883\), with saving \(5879367/6238115048\) against the identified table. These are asymptotic exponent comparisons, not percentages of actual zeros, effective constants, finite-height exclusions or RH conclusions. Worldwide novelty is not asserted.

## 1. The local inputs and the whole A-process supremum

Use the exponential-sum exponent \(\beta\), the large-value exponents \(\mathrm{LV},\mathrm{LV}_\zeta\), and the density coefficient \(\mathrm A\) of [1--4]. Put \(b(\tau)=\tau\beta(1/\tau)\).

The three adjacent Huxley rows in [1, Theorem 4.16, Table 4.2] are
\[
\begin{array}{lll}
B_0(z)=(1053z+569)/2800,
&307/761\leq z\leq143/349,\\
B_1(z)=1812z/2765+491/5530,
&143/349\leq z\leq263/638,\\
B_2(z)=(897z+113)/1345,
&263/638\leq z\leq156527/370694.
\end{array}
\tag{3}
\]
Each bounds \(\beta\). We also use the global exponent-pair bounds
\[
B_G(z)=z/2+13/84,\qquad
B_H(z)=1389z/1736+9/217\qquad(0\leq z\leq1),
\tag{4}
\]
from the pairs \((13/84,55/84)\) and \((9/217,1461/1736)\), via [2, Lemma 5.3].

Set
\[
a=307/761,\quad b=143/349,\quad c=263/638,
\quad d=209/500,\quad t=21/50.
\]
These satisfy \(a<b<c<d<t<156527/370694\). The local rows in (3) join exactly, and their positive intercepts make \((1+B_j(z))/z\) decrease across the joined interval. For any \(z_0\in[a,d]\), choose its local row \(B(z)=mz+v\), and put \(C=(1+B(z_0))/z_0\). Then \(\beta(z)\leq Cz-1\) for \(z_0\leq z\leq t\). The worst value of \(C\) is at \(d\), and
\[
\frac{1+B_2(d)}d\,t-1-B_G(t)
=\frac{670564}{147580125}>0,
\qquad \frac{1+B_2(d)}d>\frac12.
\tag{5}
\]
The global row in (4) therefore proves the same inequality for \(t\leq z\leq1\). In particular, the entire interval \([z_0,1]\), not just the local Huxley range, is controlled.

Define
\[
\alpha=\frac{z_0}{1+v+mz_0},\qquad
h=\frac{(1-m+v)\alpha-v}{1+v}.
\tag{6}
\]
The exact certificate checks \(0<h<2\alpha/3\) and \(\alpha<1/2\) on all three image intervals. In the A-process [1, Lemma 4.6], the supremum variable \(h'\in[2\alpha-1,h]\) corresponds to \(z=\alpha/(1+h'-\alpha)\in[z_0,1]\). Thus
\[
(1+h'-\alpha)\beta(z)+h'\leq\alpha C+\alpha-1.
\]
The choice (6) balances
\(2\alpha-h=\alpha+(1+h-\alpha)B(z_0)\), while \(2h\leq2\alpha-h\). Every term in the full A-process maximum is therefore bounded, giving
\[
\beta(\alpha)\leq
\frac{1+m+v}{2(1+v)}\alpha+\frac{v}{2(1+v)}.
\tag{7}
\]
The resulting joined rows are
\[
\begin{array}{lll}
\widetilde B_0(\alpha)=737\alpha/1123+569/6738,
&3070/10311\leq\alpha\leq1430/4737,\\
\widetilde B_1(\alpha)=3215\alpha/4014+491/12042,
&1430/4737\leq\alpha\leq263/867,\\
\widetilde B_2(\alpha)=785\alpha/972+113/2916,
&263/867\leq\alpha\leq281105/916473.
\end{array}
\tag{8}
\]
This extends the earlier two-row calculation [6] by its preceding local row, with the whole supremum retained.

## 2. Two complete exponential-sum prefixes

For the rest of the proof let
\[
e\in[31/500,63/1000],\qquad
M=\frac{1747-5600e}{569},\qquad
Z=\frac{2316-6738e}{569}.
\tag{9}
\]
The certificate proves throughout this interval
\[
a<1/M<b,\qquad
3070/10311<1/Z<1430/4737.
\tag{10}
\]
At these points \(B_0(1/M)/(1/M)=1-2e\) and
\(\widetilde B_0(1/Z)/(1/Z)=1-e\).

The ratios of the original rows (3) decrease continuously up to \(t\), and
\[
B_G(t)/t=383/441<1-2(63/1000).
\tag{11}
\]
Consequently \(b(\tau)<1-2e\) for all \(1\leq\tau<M\), uniformly on every closed subinterval ending below \(M\).

Likewise the ratios of (8) decrease continuously up to \(u=281105/916473\), and the certificate verifies
\[
B_H(u)/u<1-63/1000.
\tag{12}
\]
Using \(B_H\) for every larger argument proves \(b(\tau)<1-e\) for all \(1\leq\tau<Z\). For the zeta vanishing criterion only \(2\leq\tau<Z\) is needed, but the prefix down to 1 is important for the second density application. These are complete prefix statements, not tests only at \(M\) and \(Z\).

## 3. Zeta-limited application: proof of (1)

Take \(\sigma=1-e\). Montgomery's large-values theorem [3, Theorem 7.10] and the first prefix give
\(\mathrm{LV}(1-e,\tau)\leq2e\) for \(0\leq\tau<M\). Below \(\tau=1\) its exponential-sum hypothesis is vacuous, or the mean-value theorem suffices.

The second prefix and [3, Corollary 8.5] give
\(\mathrm{LV}_\zeta(1-e,\tau)=-\infty\) for \(2\leq\tau<Z\). Moreover
\[
M+e-\frac34Z=\frac{20+45e}{1138}>0.
\tag{13}
\]
Choose fixed sufficiently small \(d_0>0\) and \(\tau_0=3Z/4-d_0\). The general-coefficient range then covers \(0\leq\tau\leq\tau_0-e\), and the zeta vanishing range covers \([2,4\tau_0/3)\). The established subdivision conversion [4, Corollary 44; 3, Corollary 11.10] yields \(\mathrm A(1-e)\leq3/\tau_0\), hence the limiting coefficient \(4/Z=2276/(2316-6738e)\).

Given a desired density-exponent loss \(\varepsilon>0\), first fix \(d_0\) small enough to lose less than \(\varepsilon/2\), then take the conversion loss below \(\varepsilon/2\). The strict margins persist under the small left shift in \(\sigma\) used in the definition of \(\mathrm A\). This proves (1), without asserting a uniform constant as \(d_0\to0\).

## 4. Montgomery-limited application: proof of (2)

Now take \(\eta=e/2\), \(\sigma=1-\eta\), and use the second prefix from Section 2 as the general-coefficient prefix: its threshold \(1-e\) equals \(1-2\eta\). Montgomery gives \(\mathrm{LV}(1-\eta,\tau)\leq2\eta\) for \(0\leq\tau<Z\).

For the zeta range, Heath-Brown's derivative bound [1, Theorem 4.23] gives
\[
b(\tau)\leq1+\max\left\{
\frac{\tau-r}{r(r-1)},\ -\frac1{r(r-1)},\
-\frac{2\tau}{r^2(r-1)}\right\},\qquad r\geq3.
\tag{14}
\]
For \(r=3,4,6\), all three entries are less than \(-\eta\) on the respective open intervals
\[
(9\eta,3-6\eta),\quad
(24\eta,4-12\eta),\quad
(90\eta,6-30\eta).
\tag{15}
\]
The middle-term condition is \(\eta<1/30\) for all three choices. In the present interval, the first interval contains 2 and the two joins overlap strictly. Hence the union covers \([2,Z_H)\), where \(Z_H=6-30\eta\), and Corollary 8.5 gives zeta vanishing throughout.

The certificate checks
\[
Z+\eta=\frac{2316-12907\eta}{569}<\frac34 Z_H.
\tag{16}
\]
Take \(\tau_0=Z+\eta-d_0\), with fixed sufficiently small \(d_0>0\), and apply the same subdivision conversion. The limiting coefficient is
\(3/(Z+\eta)=1707/(2316-12907\eta)\). The fixed-\(d_0\), small-left-shift and \(\varepsilon\) passage is identical to Section 3, proving (2).

## 5. Full comparisons with the declared inputs

For (1), the exact certificate verifies throughout the interval
\[
\frac{2276}{2316-6738e}
<\frac{288}{347-1736e},\qquad
\frac{2276}{2316-6738e}
<\frac{391}{479-2493e}.
\tag{17}
\]
The comparators are [5] and the identified Table 11.1 branch. For (2), it verifies
\[
\frac{1707}{2316-12907\eta}<\frac3{4-24\eta},
\tag{18}
\]
the corresponding identified table branch. Denominators are positive, and cross multiplication reduces each assertion to affine endpoint tests.

The declared growth family is all rational vertices and convex interpolation in [3, Table 6.2], the complete Heath-Brown vertex family, both curves in Theorems 6.13--6.14, and their functional-equation reflections. For a supplied bound \(\mu(s)\leq v\), its candidate for \(\lambda(p)\) is \(v/(1-s-p)\), when the denominator is positive. Put
\[
D=2316-6738e,\qquad D_M=2316-12907e/2.
\]
The certificate proves for every eligible candidate from the declared family
\[
\lambda(e)>569/D,\qquad
\lambda(e/2)>569/(2D_M),
\tag{19}
\]
where these inequalities describe the constants supplied by those upper bounds, not the true unknown growth function.

Here are the finite and infinite reductions. At each rational vertex, the comparisons are \(vD>569(1-s-e)\) and \(2vD_M>569(1-s-e/2)\), plus their reflected versions. Convex interpolation preserves these affine inequalities. The script checks Heath-Brown vertices \(n=3,\ldots,9\) individually. Their distances
\[
\delta_n=\frac{3n^2-3n+2}{n(n-1)^2(n+2)}
\]
decrease, and \(\delta_{10}<31/1000\), so the entire unreflected tail is ineligible for both parameters. The reflected tail is bounded by its positive functional-equation term. For the global curve \((2\sqrt{10}/13)\delta^{3/2}\), the unrestricted minimum ratio squared is \(270p/169\). It exceeds the squared targets in (19); the reflected curve is handled by monotonicity on \(0\leq\delta\leq1/2\). The smaller-support curve has \(\delta\leq317/118272\), so its unreflected part is ineligible and its reflected part is paid by the functional-equation term. Finally \(s\leq0\) gives a ratio at least \(1/2\). All inequalities are strict rational checks.

For (1), let \(a,b\) be constants supplied for \(\lambda(e),\lambda(2e)\). Equation (19) implies \(a,b>569/D\): increasing the parameter only shortens eligible denominators. Thus the pure-growth hybrid coefficient \(\max\{3b/(1+eb),4a\}\) exceeds \(2276/D\). Pintz's separate coefficient [7] is
\[
\max\{2qa,2b(1+1/q)\},\qquad q=\lceil b/a\rceil.
\tag{20}
\]
For \(q=1\), use \(4b\); for \(q\geq2\), use \(2qa\geq4a\). It too is larger.

For (2), the supplied constants satisfy \(a>569/(2D_M)\), \(b>569/D\). Since \(D+569\eta=D_M\), the hybrid term \(3b/(1+\eta b)\) already exceeds \(1707/D_M\). In (20), use \(4b\) for \(q=1\), \(3b\) for \(q=2\), and \(6a\) for \(q\geq3\). Each is strictly larger than \(1707/D_M\). These comparisons also allow supplied constants to be enlarged to change \(q\).

No comparison with an undeclared growth estimate or an unlocated literature result is claimed. Omission from an identified table alone is not a global novelty certificate.

## References and reproducibility

[1] Analytic Number Theory Exponent Database, [exponential-sum chapter](https://teorth.github.io/expdb/blueprint/beta-chapter.html), Lemma 4.6, Theorem 4.16/Table 4.2, and Theorem 4.23. The local rows are attributed to M. N. Huxley, *Area, Lattice Points, and Exponential Sums*, Oxford University Press, 1996, Table 19.2.

[2] The authors' [exponent-pair chapter](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html), Lemma 5.3 and the two established pairs in (4).

[3] Their [large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-chapter.html), [zeta large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-zeta-chapter.html), [zero-density chapter](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html), and [zeta-growth chapter](https://teorth.github.io/expdb/blueprint/zeta-growth-chapter.html). Numbered results are identified in the text. Checked 2026-10-16.

[4] T. Tao, T. S. Trudgian and A. Yang, *New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*, [arXiv:2501.16779v1](https://arxiv.org/html/2501.16779v1), Corollary 44.

[5] [A hybrid growth-to-density corollary below sigma=.95](../20261016_lower_sigma_hybrid_density/REPORT.md).

[6] [A local-beta refinement of a fixed-interval zero-density bound](../20261016_local_beta_density/REPORT.md).

[7] J. Pintz, *Remark on a General Zero Density Theorem*, Mathematica Pannonica 29_NS3 (2023), 238--243, Theorem 1.2. [DOI](https://doi.org/10.1556/314.2023.00025).

Run `python3 check_certificate.py`. The standard-library script certifies the stated exact arithmetic and complete parameter ranges, not the imported analytic theorems or worldwide novelty.
