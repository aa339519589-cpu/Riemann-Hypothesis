# A local-beta refinement of a fixed-interval zero-density bound

Let \(N(\sigma,T)\) count the nontrivial zeta zeros \(\beta+i\gamma\), with multiplicity, satisfying \(\beta\geq\sigma\) and \(0<|\gamma|\leq T\). Restricting to positive ordinates changes only a factor of two.

**Theorem.** For every fixed
\[
\frac{1871}{2000}\leq\sigma\leq\frac{117}{125}
\qquad(.9355\leq\sigma\leq.936)
\]
and every \(\varepsilon>0\),
\[
\boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}
 T^{\frac{1964(1-\sigma)}{12042\sigma-9645}+\varepsilon}.}
\tag{1}
\]
This follows unconditionally from established local exponential-sum bounds, the classical A-process, and established density transfers. It is stronger on this interval than the identified ANTEDB density table, the preceding growth-only corollary [5], and every application of the pure-growth hybrid conversion or Pintz's separate theorem using the declared growth family in Section 4. No new exponential-sum estimate is imported or conjectured; the local A-process specialization is proved below.

At \(\sigma=117/125=.936\), the density exponent is
\[
\frac{15712}{203289},
\quad\text{rather than}\quad
\frac{768}{9829}\ \text{from [5], or}\ \frac{3128}{39931}\ \text{from the table}.
\]
The saving against [5] is \(1692704/1998127581>0\). These statements concern asymptotic upper-bound exponents, not fractions of actual zeros, effective constants, finite-height exclusions, or RH. The comparison is explicitly bounded to the stated inputs and formulas; exhaustive worldwide novelty is not asserted.

## 1. Input notation

Write \(\eta=1-\sigma\), so
\[
\eta\in[8/125,129/2000].
\tag{2}
\]
Use the exponential-sum function \(\beta\), the large-value functions \(\mathrm{LV},\mathrm{LV}_\zeta\), and the density coefficient \(\mathrm A\) of [1,2]. Set \(b(\tau)=\tau\beta(1/\tau)\).

The local inputs are the following two adjacent Huxley bounds, recorded in [1, Theorem 4.16, Table 4.2]:
\[
B_1(z)=\frac{1812}{2765}z+\frac{491}{5530},
\quad \frac{143}{349}\leq z\leq\frac{263}{638},
\tag{3}
\]
\[
B_2(z)=\frac{897}{1345}z+\frac{113}{1345},
\quad\frac{263}{638}\leq z\leq\frac{156527}{370694}.
\tag{4}
\]
Both are upper bounds for \(\beta\). We also use the global bounds
\[
B_0(z)=z/2+13/84,
\qquad B_3(z)=1389z/1736+9/217
\tag{5}
\]
for \(0\leq z\leq1\). These follow from the established exponent pairs \((13/84,55/84)\) and \((9/217,1461/1736)\), via the exponent-pair duality in [2, Lemma 5.3]. In particular, (5) is used as a global exponent-pair bound, not as a local row extended beyond its range.

## 2. A-process with its whole supremum

Set
\[
a=143/349,\quad b=263/638,\quad c=209/500,\quad t=21/50.
\]
Thus \(a<b<c<t<156527/370694\). The two local rows join at \(b\). Their intercepts are positive, so \((1+B_j(z))/z\) decreases on each row and across their join.

For any \(z_0\in[a,c]\), put \(B=B_1\) or \(B_2\), according to the row containing \(z_0\), and
\[
C=(1+B(z_0))/z_0.
\]
Equations (3)--(4) give \(\beta(z)\leq Cz-1\) for \(z_0\leq z\leq t\). For \(t\leq z\leq1\), use \(B_0\): the worst value of \(C\) is attained at \(c\), and the exact inequality
\[
\frac{1+B_2(c)}{c}\,t-1-B_0(t)
=\frac{670564}{147580125}>0
\tag{6}
\]
together with \(C>1/2\) proves the same bound throughout this remaining interval. Consequently
\[
\beta(z)\leq Cz-1\qquad(z_0\leq z\leq1).
\tag{7}
\]

For a row \(B(z)=mz+v\), define
\[
\alpha=\frac{z_0}{1+v+mz_0},\qquad
h=\frac{(1-m+v)\alpha-v}{1+v}.
\tag{8}
\]
The certificate verifies \(0<h<2\alpha/3\) and \(\alpha<1/2\) on both complete image intervals. For the A-process supremum in [1, Lemma 4.6], its variable \(h'\in[2\alpha-1,h]\) corresponds exactly to
\(z=\alpha/(1+h'-\alpha)\in[z_0,1]\). Equation (7) therefore gives
\[
(1+h'-\alpha)\beta(z)+h'\leq\alpha C+\alpha-1.
\]
Thus every term in that supremum is controlled, including the part with \(z>1/2\). The balance in (8) yields
\[
2\alpha-h=\alpha+(1+h-\alpha)B(z_0),\qquad
2h\leq2\alpha-h.
\]
Applying the A-process proves
\[
\beta(\alpha)\leq
\frac{1+m+v}{2(1+v)}\alpha+\frac{v}{2(1+v)}.
\tag{9}
\]
In particular the two joined resulting rows are
\[
\begin{array}{ll}
\beta(\alpha)\leq3215\alpha/4014+491/12042,
 &1430/4737\leq\alpha\leq263/867,\\[2mm]
\beta(\alpha)\leq785\alpha/972+113/2916,
 &263/867\leq\alpha\leq281105/916473.
\end{array}
\tag{10}
\]
This argument does not substitute a local estimate into a supremum without controlling its other arguments.

## 3. Complete parameter intervals and density transfer

Define
\[
M=\frac{1906-11060\eta}{491},\qquad
Z=\frac{2397-12042\eta}{491}.
\tag{11}
\]
The exact certificate proves, throughout (2),
\[
a<1/M<b,\quad 1430/4737<1/Z<263/867.
\tag{12}
\]

**General-coefficient large values.** On \([1/M,t]\), the joined rows (3)--(4) have decreasing ratios \(B_j(z)/z\), starting at \(1-2\eta\). On \([t,1]\), (5) gives
\[
B_0(z)/z\leq B_0(t)/t=383/441<1-2\eta.
\]
It follows that, for every fixed \(M'<M\),
\(\sup_{1\leq\tau\leq M'}b(\tau)<1-2\eta\).
Montgomery's theorem [3, Theorem 7.10] gives \(\mathrm{LV}(1-\eta,\tau)\leq2\eta\) for all \(0\leq\tau<M\); the condition below \(\tau=1\) is vacuous, or follows from the mean-value theorem.

**Zeta partial sums.** For \(\alpha\in[1/Z,281105/916473]\), the two ratios from (10) decrease continuously, starting at \(1-\eta\). For larger \(\alpha\leq1/2\), use \(B_3\), since at the joining point
\[
\frac{B_3(281105/916473)}{281105/916473}
=\frac{65205843}{69714040}<\frac{1871}{2000}\leq1-\eta.
\tag{13}
\]
Hence \(b(\tau)<1-\eta\) for every \(2\leq\tau<Z\). The zeta large-value vanishing criterion [3, Corollary 8.5] applies on that **whole** interval.

Finally,
\[
M+\eta-\frac34Z=\frac{433-6150\eta}{1964}>0.
\tag{14}
\]
Choose \(\tau_0=3Z/4-d\), where \(d>0\) is fixed and sufficiently small. Then \(\tau_0-\eta<M\), and the entire required zeta interval \([2,4\tau_0/3)\) is contained in \([2,Z)\). The established subdivision conversion [4, Corollary 44; 3, Corollary 11.10] gives \(\mathrm A(1-\eta)\leq3/\tau_0\).
For any prescribed exponent loss \(\varepsilon>0\), first choose fixed \(d\) making the change from \(4\eta/Z\) less than \(\varepsilon/2\), then choose the transfer loss below \(\varepsilon/2\). All strict margins persist under the small left shift in \(\sigma\) used in the definition of \(\mathrm A\). This proves (1), without asserting any uniform constant as \(d\to0\).

## 4. Comparisons and their exact scope

The certificate verifies on the full interval
\[
\frac{1964}{2397-12042\eta}
<\frac{288}{347-1736\eta}
<\frac{391}{479-2493\eta}.
\tag{15}
\]
These compare respectively with [5] and the identified Table 11.1 branch. Positive-denominator cross multiplication reduces the assertions to affine endpoint checks.

A stronger comparison concerns the declared upper-growth family: all rational vertices and convex interpolation in [3, Table 6.2], the complete Heath-Brown tail, both curves in Theorems 6.13--6.14, and their functional-equation reflections. For a supplied upper bound \(\mu(s)\leq v\), put \(\delta=1-s\). The checker proves
\[
\frac{v}{\delta-\eta}>\frac{491}{D},
\qquad D=2397-12042\eta,
\tag{16}
\]
whenever \(\delta>\eta\), uniformly over that family. This concerns supplied bounds, not a lower bound on the unknown true growth function.

For completeness, the reduction of the infinite family is as follows. At each rational vertex, (16) is the affine inequality \(vD>491(\delta-\eta)\); convex interpolation preserves it. For Heath-Brown's vertices, \(\delta_n=(3n^2-3n+2)/(n(n-1)^2(n+2))\) decreases and already \(\delta_7=32/567<8/125\), making the unreflected tail ineligible; the finite initial cases \(n=3,4,5,6\) are checked individually. The reflected tail is bounded using its positive functional-equation term. The global curve \((2\sqrt{10}/13)\delta^{3/2}\) has unrestricted minimum ratio squared \(270\eta/169\), which exceeds the square of the right side of (16). Its reflected curve is checked by monotonicity on \(0\leq\delta\leq1/2\). The sharper small-\(\delta\) curve is confined to \(\delta\leq317/118272\), so its unreflected part is ineligible and its reflected part is paid by the functional-equation term. The region \(s\leq0\) has ratio at least \(1/2\). All numerical inequalities are strict rational checks in the script.

Let \(a\) and \(b\) be constants supplied for \(\lambda(\eta)\) and \(\lambda(2\eta)\) by this family. Equation (16) implies both \(a,b>491/D\). The growth-only hybrid conversion has coefficient
\(\max\{3b/(1+\eta b),4a\}>1964/D\), because its zeta ceiling is at most \(1/a\). Pintz's separate coefficient [6] is
\(\max\{2qa,2b(1+1/q)\}\), \(q=\lceil b/a\rceil\).
If \(q=1\), use \(4b\); if \(q\geq2\), use \(2qa\geq4a\). It too is strictly larger. Enlarging supplied constants to change \(q\) cannot evade the comparison.

This does not claim superiority over every possible large-value argument or every unlocated paper. In particular it does not identify omission from a table with global novelty.

## References and reproducibility

[1] Analytic Number Theory Exponent Database, [exponential-sum chapter](https://teorth.github.io/expdb/blueprint/beta-chapter.html), Lemma 4.6 and Theorem 4.16/Table 4.2. The local rows are attributed there to M. N. Huxley, *Area, Lattice Points, and Exponential Sums*, Oxford University Press, 1996, Table 19.2.

[2] The same authors' [exponent-pair chapter](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html), Lemma 5.3 and the established pairs stated in Section 1.

[3] The authors' [large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-chapter.html), [zeta large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-zeta-chapter.html), [zero-density chapter](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html), and [zeta-growth chapter](https://teorth.github.io/expdb/blueprint/zeta-growth-chapter.html). Numbered results are identified in the text. Sources checked 2026-10-16.

[4] T. Tao, T. S. Trudgian and A. Yang, *New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*, [arXiv:2501.16779v1](https://arxiv.org/html/2501.16779v1), Corollary 44.

[5] [A hybrid growth-to-density corollary below sigma=.95](../20261016_lower_sigma_hybrid_density/REPORT.md), including its complete declared-growth comparison.

[6] J. Pintz, *Remark on a General Zero Density Theorem*, Mathematica Pannonica 29_NS3 (2023), 238--243, Theorem 1.2. [DOI](https://doi.org/10.1556/314.2023.00025).

Run `python3 check_certificate.py`. The standard-library script certifies the exact algebra and complete stated parameter ranges; it does not prove the cited analytic inputs or certify worldwide novelty.
