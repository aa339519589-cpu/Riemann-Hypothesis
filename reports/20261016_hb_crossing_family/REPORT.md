# Two further Heath-Brown crossing density corollaries

**Comparison/provenance update (16 October 2026).** A prior primary source states a stronger actual-zeta curve on this report's interval. The result here remains a correct identified-table improvement, not a best-known or all-prior-results improvement. See the [pinned prior-source comparison and verification scope](../20261016_density_prior_source_comparison/REPORT.md). The proof and arithmetic below are unchanged.

Let \(N(\sigma,T)\) count nontrivial zeta zeros \(\beta+i\gamma\), with multiplicity, satisfying \(\beta\geq\sigma\) and \(0<|\gamma|\leq T\). For each fixed \(\sigma\) in the indicated interval and every \(\varepsilon>0\), the following unconditional bounds hold:
\[
\boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}
T^{\frac{15(1-\sigma)}{89\sigma-61}+\varepsilon}}
\qquad\left(\frac{29}{38}\leq\sigma\leq\frac{13}{17}\right),
\tag{1}
\]
\[
\boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}
T^{\frac{39(1-\sigma)}{301\sigma-211}+\varepsilon}}
\qquad\left(\frac{547}{720}\leq\sigma\leq\frac{127}{167}\right).
\tag{2}
\]
They strictly improve the identified Table 11.1 of [2] on the interiors of these intervals, and agree with that table at the two outer endpoints of each interval. In (2) the table has an additional branch join at \(19/25\), which is retained in the comparison. At \(\sigma=.764\), (1) gives \(295/583\), improving the table exponent \(885/1733\) by \(4720/1010339\). At \(\sigma=.760\), (2) gives \(39/74\), improving \(9/17\) by \(3/1258\).

These are additional specializations of the established-input crossing/subdivision argument in [1], not new mean-square theorems. No percentage of actual zeros excluded, effective finite-height exclusion, explicit implied constant, RH conclusion, or exhaustive worldwide novelty is claimed. The comparison is to the stated table and the separate recorded Kerr formula below.

## 1. A general crossing lemma

The scale-general primary-source derivation in [1, Section 2] proves, for fixed \(k\in\mathbb N\), \(\sigma>3/4\), and \(\tau\geq1\),
\[
\mathrm{LV}(\sigma,\tau)\leq\max\{2\eta,
k\tau+k(2-4\sigma),
2\tau/3+k(12-16\sigma)/3\},\qquad\eta=1-\sigma.
\tag{3}
\]
It uses the full Heath-Brown difference-set theorem and the reflection proof in the primary Guth--Maynard paper [3], retaining the diagonal, every dyadic difference range, Mellin cutoff, coefficient bound, and an arbitrarily small exponent loss. The argument there applies to every fixed positive integer \(k\); its subsequent numerical specialization to \(k=3\) is not needed here.

For \(k\geq2\), define
\[
t_k=\frac{k(6-4\sigma)}{3k-2},\qquad
v_k=\frac{4k[(3k-1)-(4k-2)\sigma]}{3k-2},\qquad
\alpha_k=t_k-v_k,
\]
\[
\tau_k=3\eta+\alpha_k
=\frac{(16k^2-21k+6)\sigma-12k^2+19k-6}{3k-2}.
\tag{4}
\]
Suppose that
\[
\alpha_k>0,\quad 2\eta\leq v_k\leq3\eta,\quad
0<2\tau_k/3\leq1\leq t_k\leq\tau_k\leq3/2,
\tag{5}
\]
and that the two nonconstant branches of (3), evaluated at \(\tau=1\), are at most \(2\eta\). Then
\[
\mathrm A(\sigma)\leq\frac3{\tau_k}.
\tag{6}
\]
Here \(\mathrm A\) is the density coefficient, so the exponent of \(T\) is \((1-\sigma)\mathrm A(\sigma)\).

To prove (6), put \(E_k=3\eta/\tau_k<1\). The mean-value theorem controls \(2\tau_k/3\leq\tau\leq1\), since \(E_k(2\tau_k/3)=2\eta\). The two affine branches in (3) meet at \((t_k,v_k)\), and
\[
E_kt_k-v_k=\frac{\alpha_k(3\eta-v_k)}{\tau_k}\geq0.
\]
Their values at \(1\) are at most \(2\eta\leq E_k\), so each lies below \(E_k\tau\) throughout \([1,t_k]\). The constant branch does too. Subdivision gives
\[
\mathrm{LV}(\sigma,\tau)\leq v_k+\tau-t_k
=\tau-\alpha_k\leq E_k\tau\quad(t_k\leq\tau\leq\tau_k).
\]
Thus the entire interval \([2\tau_k/3,\tau_k]\) is controlled. The zeta-polynomial interval \([2,4\tau_k/3)\) is empty. Corollary 11.9 of [2] proves (6). This uses the linear-window conversion, not the stronger Montgomery-prefix hypothesis of Corollary 11.10.

## 2. Two complete parameter ranges

For \(k=4\), (4) gives
\[
\tau_4=(89\sigma-61)/5,
\]
so (6) is (1). For \(k=5\), it gives
\[
\tau_5=(301\sigma-211)/13,
\]
so (6) is (2). Every premise in (5), and both \(\tau=1\) branch comparisons, is affine in \(\sigma\). The exact checker verifies them at both endpoints of their respective intervals, hence on the full intervals. In both cases \(\tau_k<3/2\) strictly, and \(v_k=2\eta\) at the right endpoint is allowed. All denominators are positive.

For the finite-\(\varepsilon\) statement, fix \(\sigma\) and the requested loss first; choose the small losses in the reflection/mean-square input, thinning, subdivision and zero detection sufficiently small. The exponent-form conversion yields every fixed positive final loss. Neither a uniform implied constant in \(\sigma\) nor a loss-free endpoint estimate is being asserted. The closed interval endpoints remain valid because the imported exponent inequalities and the affine comparisons are non-strict where equality is used.

## 3. Complete declared comparisons

On \([29/38,13/17)\), Table 11.1 of [2] gives \(15/(13\sigma-3)\). The difference between the new and old positive denominators is
\[
(89\sigma-61)-(13\sigma-3)=76\sigma-58,
\]
positive exactly above \(29/38\). At \(13/17\), the table changes to \(6/(5\sigma-1)\), equal there to the coefficient in (1).

For (2), the table is \(15/(3+5\sigma)\) up to \(19/25\), then \(9/(8\sigma-2)\) up to \(127/167\). The respective positive-denominator comparisons are
\[
15(301\sigma-211)-39(3+5\sigma)=4320\sigma-3282,
\]
\[
9(301\sigma-211)-39(8\sigma-2)=2397\sigma-1821.
\]
The first vanishes at \(547/720\) and is positive thereafter. The second is strictly positive throughout \([19/25,127/167]\). At \(127/167\), the table changes to \(15/(13\sigma-3)\), equal there to the coefficient in (2).

Proposition 11.37 of [2] records a separate Kerr estimate, explicitly attributed there to an unpublished preprint:
\[
A_K(\sigma)=\max\left\{\frac{36}{138\sigma-89},
\frac{114\sigma-79}{(1-\sigma)(138\sigma-89)}\right\}.
\]
Its first entry already exceeds each new coefficient on the corresponding full interval. For (1), this reduces to \(\sigma>287/378\); for (2), it reduces to \(\sigma>1375/1818\). Both are strict over the stated intervals. This comparator is not an input to the proof.

The standard-library rational checker verifies all interval premises and branch comparisons, including both upper-end table changes and exact sample values. It certifies the finite algebra, not the imported analytic theorems or an exhaustive literature search.

## References

1. [A Heath-Brown crossing and subdivision density corollary near sigma=.773](../20261016_hb_crossing_density/REPORT.md), Section 2. Its primary-source derivation of (3) is valid for every fixed positive integer \(k\).
2. Terence Tao, Timothy Trudgian and Andrew Yang, [author-maintained zero-density chapter](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html), Corollaries 11.8--11.9, Table 11.1, Proposition 11.37; and [large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-chapter.html), Lemma 7.4, Theorem 7.9, Lemma 7.15. Formulas checked on 2026-10-16; labels refer to the blueprint.
3. Larry Guth and James Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics 203(2) (2026), 623--675, DOI [10.4007/annals.2026.203.2.6](https://doi.org/10.4007/annals.2026.203.2.6); [author preprint v2](https://arxiv.org/html/2405.20552v2), Theorem 1.6, Lemma 6.2, equations (6.1)--(6.4).
