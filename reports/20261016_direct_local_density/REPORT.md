# A direct local-exponential-sum zero-density corollary near sigma=.973

Let \(N(\sigma,T)\) count nontrivial zeta zeros \(\beta+i\gamma\), with multiplicity, satisfying \(\beta\geq\sigma\) and \(0<|\gamma|\leq T\).

**Theorem.** For every fixed
\[
\frac{2431}{2500}\leq\sigma\leq\frac{1217}{1250}
\qquad(.9724\leq\sigma\leq.9736)
\]
and every \(\varepsilon>0\),
\[
\boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}
T^{\frac{87(1-\sigma)}{1171\sigma-1035}+\varepsilon}.}
\tag{1}
\]
The inputs are established local Huxley exponential-sum bounds, an established exponent pair, Heath-Brown's derivative estimate, and the established subdivision density conversion. No new mean-square or exponential-sum input is claimed.

Throughout the interval, the coefficient in (1) is less than \(19/20\) of the identified Table 11.1 coefficient \(86152/(1447460\sigma-1311509)\). It is also strictly better than every pure-growth hybrid conversion and every Pintz-Remark application built from the declared complete growth family in Section 3. At \(\sigma=.9724\), the new ordinary density exponent is
\[
6003/259201.
\tag{2}
\]
Its saving against the identified table exponent is \(4170027742/2592039808115>0\).

A relative reduction in an upper-bound exponent is **not** a percentage of actual zeros excluded, nor an effective finite-height exclusion. No explicit implied constant, RH conclusion, or exhaustive worldwide novelty claim is made. The comparison concerns the formulas and inputs explicitly identified here.

## 1. Complete general-coefficient large-value range

Put
\[
\eta=1-\sigma\in[33/1250,69/2500],\qquad
M=(136-1200\eta)/29.
\tag{3}
\]
Use \(\beta\), \(\mathrm{LV}\), \(\mathrm{LV}_\zeta\), and \(\mathrm A\) in the conventions of [1--4], and set \(b(\tau)=\tau\beta(1/\tau)\).

The following three Huxley rows are recorded in [1, Theorem 4.16, Table 4.1]:
\[
\begin{array}{lll}
B_1(z)=58z/75+29/600,
&199/716\leq z\leq967/3428,\\
B_2(z)=(1351z+49)/1614,
&967/3428\leq z\leq120/419,\\
B_3(z)=235z/264+1/66,
&120/419\leq z\leq1424/4747.
\end{array}
\tag{4}
\]
Each is a valid upper bound for \(\beta(z)\). The rows join exactly, and their positive intercepts imply that \(B_j(z)/z\) decreases continuously across both joins.

The exact certificate checks on the whole interval (3) that
\[
199/716<1/M<967/3428,
\qquad B_1(1/M)/(1/M)=1-2\eta.
\tag{5}
\]
Thus (4) controls every \(z\) from \(1/M\) through \(29/100\). For the rest of \([29/100,1]\), use the global bound
\[
\beta(z)\leq1389z/1736+9/217,
\tag{6}
\]
which follows from the established exponent pair \((9/217,1461/1736)\) and exponent-pair duality [2]. Its ratio is decreasing and at \(z=29/100\) equals
\[
6783/7192<1-2(69/2500).
\tag{7}
\]
Therefore, for every fixed \(M'<M\),
\(\sup_{1\leq\tau\leq M'}b(\tau)<1-2\eta\).
The Montgomery large-values theorem [3, Theorem 7.10] proves
\[
\mathrm{LV}(1-\eta,\tau)\leq2\eta\qquad(0\leq\tau<M).
\tag{8}
\]
For \(\tau<1\), its condition is vacuous, or the mean-value theorem suffices. This is a complete prefix argument, not a bound at \(\tau=M\) alone.

## 2. Complete zeta range and density transfer

Heath-Brown's derivative estimate [1, Theorem 4.23] gives, for each integer \(r\geq3\),
\[
b(\tau)\leq1+\max\left\{
\frac{\tau-r}{r(r-1)},\ -\frac1{r(r-1)},\
-\frac{2\tau}{r^2(r-1)}\right\}.
\tag{9}
\]
All three entries are less than \(-\eta\) if
\[
\frac{r^2(r-1)}2\eta<\tau<r-r(r-1)\eta,
\qquad\eta<\frac1{r(r-1)}.
\tag{10}
\]
For \(r=3\) and \(r=6\), the open intervals are
\[
(9\eta,3-6\eta),\qquad(90\eta,6-30\eta).
\]
On (3), the first begins below 2 and ends above 2; the intervals overlap because \(\eta<1/32\). Also \(\eta<1/30\) pays the middle term in (9) for both choices of \(r\). Consequently
\[
b(\tau)<1-\eta\qquad(2\leq\tau<Z),\qquad Z=6-30\eta.
\tag{11}
\]
The zeta partial-sum vanishing criterion [3, Corollary 8.5] gives \(\mathrm{LV}_\zeta(1-\eta,\tau)=-\infty\) throughout this full interval.

The exact certificate verifies \(M+\eta<3Z/4\). Choose
\[
\tau_0=M+\eta-d=(136-1171\eta)/29-d
\]
with fixed sufficiently small \(d>0\). Then (8) holds through \(\tau_0-\eta\), while \([2,4\tau_0/3)\) lies strictly inside the zeta range in (11). Apply the established subdivision conversion [4, Corollary 44; 3, Corollary 11.10] to obtain \(\mathrm A(1-\eta)\leq3/\tau_0\).
Given \(\varepsilon>0\), choose fixed \(d\) making the density-exponent change relative to \(87\eta/(136-1171\eta)\) less than \(\varepsilon/2\), then choose the transfer loss below \(\varepsilon/2\). The strict inequalities also persist under a sufficiently small left shift in \(\sigma\). This proves (1) without a uniform constant as \(d\to0\).

## 3. Table and full declared-growth comparisons

The whole interval lies in Table 11.1's branch \(86152/(1447460\sigma-1311509)\). Put
\[
D=136-1171\eta,\qquad Q=136-1200\eta.
\]
Both denominators, and the table denominator, are positive. The checker proves at both endpoints the affine inequalities
\[
87(135951-1447460\eta)<86152D,
\quad
20\cdot87(135951-1447460\eta)<19\cdot86152D.
\tag{12}
\]
Thus they hold throughout the interval. The latter is the stated relative exponent comparison, not a zero-count percentage.

The declared growth family consists of all rational vertices and convex interpolation in [3, Table 6.2], the complete Heath-Brown family, both curved bounds in Theorems 6.13--6.14, and their functional-equation reflections. For constants \(a,b\) supplied for \(\lambda(\eta),\lambda(2\eta)\) from that family, the certificate proves
\[
a>29/(2D),\qquad b>29/Q.
\tag{13}
\]
These are lower bounds on the constants obtainable from the declared **upper-growth bounds**, not on the true unknown growth function.

Here is the complete finite/infinite reduction. For a vertex \(\mu(s)\leq v\), the tests are the affine inequalities
\(2vD>29(1-s-\eta)\) and \(vQ>29(1-s-2\eta)\), together with the reflected versions. Convex interpolation preserves them. The checker includes the individual Heath-Brown vertices \(n=3,\ldots,10\); for the rest,
\[
\delta_n=\frac{3n^2-3n+2}{n(n-1)^2(n+2)}
\]
is decreasing and \(\delta_{11}=83/3575<33/1250\), so the unreflected tail is ineligible for both parameters. Its reflected contribution is bounded by its positive functional-equation term. The global curve \((2\sqrt{10}/13)\delta^{3/2}\) has minimum ratio squared \(270e/169\) at parameter \(e\); this beats both squared targets in (13). Its reflected curve is checked by monotonicity. The other curve is supported on \(\delta\leq317/118272\), so its unreflected part is ineligible and its reflected part is paid by the functional-equation term. The region \(s\leq0\) has ratio at least \(1/2\). The certificate gives the corresponding exact rational inequalities.

The pure-growth hybrid coefficient \(\max\{3b/(1+\eta b),4a\}\) is larger than \(87/D\), since \(b>29/Q\) and \(Q+29\eta=D\). For Pintz's separate coefficient [5],
\[
\max\{2qa,2b(1+1/q)\},\qquad q=\lceil b/a\rceil,
\]
use \(4b\) when \(q=1\), \(3b\) when \(q=2\), and \(6a\) when \(q\geq3\). Equation (13) makes each strictly larger than \(87/D\). This also handles enlarging supplied constants to change \(q\).

Other input estimates or unlocated literature are not excluded by this comparison. In particular, omission of this specialization from a table does not establish global novelty.

## References and reproducibility

[1] Analytic Number Theory Exponent Database, [exponential-sum chapter](https://teorth.github.io/expdb/blueprint/beta-chapter.html), Theorem 4.16/Table 4.1 and Theorem 4.23. The local rows are attributed to M. N. Huxley, *Area, Lattice Points, and Exponential Sums*, Oxford University Press, 1996, Table 17.1.

[2] The authors' [exponent-pair chapter](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html), Lemma 5.3 and the pair \((9/217,1461/1736)\).

[3] Their [large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-chapter.html), [zeta large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-zeta-chapter.html), [zero-density chapter](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html), and [zeta-growth chapter](https://teorth.github.io/expdb/blueprint/zeta-growth-chapter.html). Numbered inputs are specified above. Checked 2026-10-16.

[4] T. Tao, T. S. Trudgian and A. Yang, *New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*, [arXiv:2501.16779v1](https://arxiv.org/html/2501.16779v1), Corollary 44.

[5] J. Pintz, *Remark on a General Zero Density Theorem*, Mathematica Pannonica 29_NS3 (2023), 238--243, Theorem 1.2. [DOI](https://doi.org/10.1556/314.2023.00025).

Run `python3 check_certificate.py`. This standard-library certificate checks the exact interval arithmetic and comparisons, not the imported analytic theorems or worldwide novelty.
