# An arbitrary-pair Halasz refinement and density near sigma=.88

Let \(N(\sigma,T)\) count nontrivial zeta zeros \(\beta+i\gamma\), with multiplicity, satisfying \(\beta\geq\sigma\) and \(0<|\gamma|\leq T\). For every fixed
\[
\frac78\leq\sigma\leq\frac{177}{200}
\]
and every \(\varepsilon>0\), the established inputs below imply
\[
\boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}
T^{\frac{1995(1-\sigma)}{7449\sigma-5323}+\varepsilon}.}
\tag{1}
\]
At \(\sigma=.88\), the exponent is \(5985/30803\), improving the identified current table's \(1/5\) by \(878/154015\). The improvement is strict throughout the stated closed interval.

This is an unconditional optimization of established exponent-pair, zeta-large-value, Halasz and subdivision inputs. The arbitrary-pair step generalizes the specific-pair calculation already written in [1, Lemma 8.16]; it is not a new exponential-sum or mean-square theorem. We compare both the identified Table 11.1 and the declared growth-only family in Section 4, without claiming exhaustive worldwide novelty. No fraction of actual zeros excluded, effective finite-height exclusion, explicit implied constant, or RH conclusion is asserted.

## 1. Retaining an arbitrary exponent pair in the Halasz calculation

Use the large-value exponents \(\mathrm{LV}\), \(\mathrm{LV}_\zeta\) and density coefficient \(\mathrm A\) of [1,2]. Write \(\eta=1-\sigma\). Let \((k,l)\) be an exponent pair with \(k>0\), and set
\[
a=\frac{k+l}{k},\qquad b=\frac{2(1+2k+2l)}k.
\]
In particular \(a>0\) and \(b>1\). We claim
\[
\mathrm{LV}(\sigma,\tau)\leq
\max\{2\eta,\ \tau+9-12\sigma,\ a\tau+b(3/2-2\sigma)\}
\quad(1/2\leq\sigma\leq1,\ \tau\geq0).
\tag{2}
\]

Here is the full elimination, rather than a substitution at one optimizing value. Put \(\rho=\mathrm{LV}(\sigma,\tau)\). The refined inequality in the proof of [1, Lemma 8.12], also used explicitly in Lemma 8.16, gives either the diagonal bound \(\rho\leq2\eta\), or, with arbitrarily small loss, some \(1/2\leq u\leq1\), \(1\leq v\leq\tau\), for which
\[
\rho\leq1-2\sigma+u+
\min\{\rho,\mathrm{LV}_\zeta(u,v)\}+o(1).
\tag{3}
\]
The short-difference case is the diagonal alternative; for \(\tau<1\) the mean-value bound already gives it. The Ivic exponent-pair bound [1, Lemma 8.11] gives, throughout this full parameter range,
\[
\mathrm{LV}_\zeta(u,v)
\leq\max\{v-6(u-1/2),\ av-b(u-1/2)\}.
\tag{4}
\]
Both entries increase with \(v\), so replace \(v\) by \(\tau\). Distributing the minimum over the maximum, and using convex combinations, bounds the minimum in (3) by the maximum of
\[
\frac56\rho+\frac\tau6-(u-1/2),\qquad
\left(1-\frac1b\right)\rho+\frac ab\tau-(u-1/2).
\]
The \(u\) term cancels in each complete expression (3). Solving the two resulting affine inequalities for \(\rho\) proves (2). The small losses are multiplied only by the fixed constants \(6\) and \(b\), so remain arbitrarily small. This controls the entire \((u,v)\) supremum; it uses neither a local-only bound nor an unproved choice of \(u\).

Consequently the Montgomery bound \(\mathrm{LV}(\sigma,\tau)\leq2\eta\) holds on the complete prefix
\[
0\leq\tau\leq M_{k,l}(\sigma),\qquad
M_{k,l}(\sigma)=\min\left\{10\sigma-7,
\frac{(4+6k+8l)\sigma-3-4k-6l}{k+l}\right\},
\tag{5}
\]
whenever the displayed endpoint is positive. Subdivision [2, Lemma 7.7] further gives
\[
\mathrm{LV}(\sigma,\tau)
\leq\max\{2\eta,2\eta+\tau-M_{k,l}(\sigma)\}.
\tag{6}
\]
Only (5), not a pointwise value at its endpoint, is used next.

## 2. Two uses of one established pair

The pair
\[
(k_0,l_0)=\left(\frac{18}{199},\frac{593}{796}\right)
\]
is established in [3, Theorem 5.20], by the Sargos process applied to Bourgain's pair. Its \(B\)-transform is
\[
(k,l)=\left(\frac{195}{796},\frac{235}{398}\right).
\]
For this transformed pair, \(a=133/39\), \(b=4252/195\). On our interval the smaller branch in (5) is
\[
M(\sigma)=\frac{8114\sigma-5988}{665}<10\sigma-7,
\tag{7}
\]
since \(\sigma<1333/1464\). In particular \(M>1\).

Use the original pair separately in the zeta-vanishing bound [1, Corollary 8.7]. It gives
\[
\mathrm{LV}_\zeta(\sigma,\tau)=-\infty
\quad\hbox{for}\quad
\tau<Z(\sigma):=\frac{796\sigma-521}{72}.
\tag{8}
\]
The complete required height ceiling is valid because
\[
\frac34Z-(M+\eta)=\frac{164543-185764\sigma}{63840}>0
\tag{9}
\]
throughout \([7/8,177/200]\). At the upper endpoint this margin is \(7093/3192000\). Both \(M+\eta>3/2\) and every denominator used here are strictly positive.

Choose a fixed small \(d>0\) and put \(\tau_0=M+\eta-d\). Equation (5) supplies the Montgomery bound through \(\tau_0-\eta=M-d\), while (8)--(9) supply vanishing on every \(2\leq\tau<4\tau_0/3\). Corollary 11.10 of [2] therefore gives
\[
\mathrm A(\sigma)\leq\frac3{M+\eta-d}.
\]
Letting the fixed loss \(d\downarrow0\) yields
\[
\mathrm A(\sigma)\leq\frac3{M+\eta}
=\frac{1995}{7449\sigma-5323},
\]
which proves (1). More explicitly, for each fixed \(\sigma\) and requested final \(\varepsilon\), first choose \(d\) sufficiently small and then choose the losses in the imported large-value and zero-detection estimates. This gives (1) with that positive final loss. No uniform implied constant in \(\sigma\), or loss-free estimate at a vanishing boundary, is claimed. The strict ceiling margin makes the same argument valid at both interval endpoints.

## 3. Identified table comparison

The whole interval lies in \([7/8,279/314)\), where [2, Table 11.1] gives the coefficient \(3/(10\sigma-7)\). Comparing positive denominators, the new coefficient is smaller exactly when
\[
1995(10\sigma-7)<3(7449\sigma-5323),
\]
which reduces to \(\sigma>668/799\). This is strict on our interval. Some exact exponent comparisons are
\[
\begin{array}{c|c|c|c}
\sigma&\text{new}&\text{identified table}&\text{saving}\\\hline
7/8&1995/9559&3/14&747/133826\\
22/25&5985/30803&1/5&878/154015\\
177/200&45885/253873&69/370&539787/93933010
\end{array}
\]
Proposition 11.37 of [2], explicitly attributed there to an unpublished Kerr preprint, also records the coefficient $3/(2\sigma)$ for $\sigma\geq23/29$. This comparator does apply here, and the new coefficient strictly improves it because $\sigma>5323/6119$ throughout our interval. The other two-entry bound in that proposition has a disjoint applicability interval. Neither Kerr bound is an input. These are exponent comparisons, not percentages of the zeros.

## 4. Comparison with a declared complete growth-only family

To distinguish (1) from a missed pure-growth substitution, also compare the following explicit family of supplied upper bounds \(m(s)\) for the zeta growth exponent. The family consists of all affine segments and vertices in [4, Table 6.2], the entire Heath-Brown sequence
\[
s_n=1-\frac{3n^2-3n+2}{n(n-1)^2(n+2)},\qquad
m(s_n)=\frac2{(n-1)^2(n+2)}\quad(n\geq3),
\]
the curve \(m(s)=\frac{2\sqrt{10}}{13}(1-s)^{3/2}\) on \([1/2,1]\), any sharper nonnegative near-one row restricted to \(1-s\leq317/118272\), their functional-equation reflections, convex interpolants, and the trivial outer extensions. The checker lists every rational vertex explicitly.

For this supplied family define
\[
\lambda(y)=\inf_{s<1-y}\frac{m(s)}{1-y-s},
\qquad a_g=\lambda(\eta),\quad b_g=\lambda(2\eta).
\]
These are values calculated from the declared upper-bound family, not lower bounds on the true growth exponent. We verify
\[
a_g\geq\frac13,\qquad b_g>\frac1{M(\sigma)}.
\tag{10}
\]
For all rational vertices and their reflections, (10) follows from the linear inequalities
\[
3m(s)>\sigma-s,\qquad M(\sigma)m(s)>2\sigma-1-s.
\tag{11}
\]
Each is affine in \(\sigma\), and the checker verifies both interval endpoints. For the infinite Heath-Brown family, \(n=3,4,5,6\) are checked individually. All \(n\geq7\) unreflected points have \(s_n>177/200\) and hence are ineligible. For their reflections, \(m(1-s_n)\geq s_n-1/2\); the two margins in (11) increase with \(s_n\), so checking \(s_7\) suffices. Affine interpolation and convexification preserve (11).

For clarity, the irrational curve comparison is also certified exactly. Put \(C^2=40/169\), \(\delta=1-s\), and \(t=1/M\). On the unreflected curve, minimizing \(C\delta^{3/2}/(\delta-\eta)\) gives squared minimum \(27C^2\eta/4>1/9\). For \(b_g\), the critical point \(\delta=6\eta\) is beyond \(1/2\), so the minimum occurs at \(\delta=1/2\); the required comparison is
\[
C^2M^2/8>(2\sigma-3/2)^2.
\]
On the reflected curve, the \(a_g\) comparison decreases to \(\delta=1/2\), where it is positive. For the \(b_g\) comparison, the unrestricted minimum over \(\delta\geq0\) of
\[
\frac12-t(2\sigma-1)-(1-t)\delta+C\delta^{3/2}
\]
is
\[
\frac12-t(2\sigma-1)-\frac{169}{270}(1-t)^3.
\]
After multiplication by \(270M^3\), positivity reduces to the cubic
\[
135M^3-270(2\sigma-1)M^2-169(M-1)^3>0.
\]
The checker verifies all four exact Bernstein coefficients on our interval are positive. The very-near-one rows are ineligible unreflected; their reflections satisfy \(m\geq1/2-317/118272\), sufficient for (11). The outer trivial extensions are checked directly. The strict margins and compactness of these declared pieces, with their explicit limiting endpoints, justify the strict infimum assertion in (10).

The established growth-only subdivision specialization gives coefficient
\[
\max\left\{\frac{3b_g}{1+\eta b_g},4a_g\right\}.
\]
Its first entry alone is strictly greater than \(3/(M+\eta)\), by (10). Pintz's separate Remark formula [5, (1.8)] is
\[
\max\{2qa_g,2b_g(1+1/q)\},\qquad q=\lceil b_g/a_g\rceil.
\]
For \(q=1\), its second entry is \(4b_g\); for \(q=2\), it is \(3b_g\). Both exceed the new coefficient. For \(q\geq3\), it is greater than \(2a_g(q-1/q)\geq16/9\), whereas the new coefficient is below \(16/9\) throughout the interval. Thus (1) also improves both these conversions when fed the entire declared growth family. This does not exclude stronger undeclared growth inputs or other published density methods.

## References and reproduction

1. Tao, Trudgian and Yang, [author-maintained zeta-large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-zeta-chapter.html), Lemmas 8.11, 8.12 and 8.16 (including their written proofs), Corollary 8.7. Lemma 8.11 attributes its exponent-pair input to Ivic, *The Riemann Zeta-Function*, Theorem 8.2.
2. [Zero-density chapter](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html), Corollary 11.10 and Table 11.1; [large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-chapter.html), Lemma 7.7. The source is also available as [arXiv:2501.16779](https://arxiv.org/abs/2501.16779). Blueprint labels and formulas were checked on 2026-10-16.
3. [Exponent-pair chapter](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html), Theorem 5.20 and Proposition 5.9, including the displayed Sargos/Bourgain proof of the original pair.
4. [Zeta-growth chapter](https://teorth.github.io/expdb/blueprint/zeta-growth-chapter.html), Table 6.2 and the declared curved/asymptotic bounds. The growth-only conversion is proved in the earlier [general subdivision report](../20261016_density_general_subdivision/REPORT.md).
5. J. Pintz, *Remark on a General Zero Density Theorem*, Mathematica Pannonica 29_NS3 (2023), 238--243, Theorem 1.2, formula (1.8), [DOI](https://doi.org/10.1556/314.2023.00025). Only the explicitly declared growth inputs above are used in this comparison.

Run `python3 check_certificate.py`. The standard-library rational checker verifies the pair arithmetic, whole interval premises, height ceiling, exact table comparisons and the full declared-growth comparison. It does not replace verification of the imported analytic theorems or claim an exhaustive literature search.
