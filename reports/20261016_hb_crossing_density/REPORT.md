# A Heath-Brown crossing and subdivision density corollary near sigma=.773

Let \(N(\sigma,T)\) count nontrivial zeros \(\beta+i\gamma\) of the Riemann zeta function, with multiplicity, such that \(\beta\geq\sigma\) and \(0<|\gamma|\leq T\).

**Theorem.** For every fixed
\[
77/100\leq\sigma\leq1547/2000
\quad (.770\leq\sigma\leq.7735)
\]
and every \(\varepsilon>0\),
\[
\boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}
 T^{\frac{7(1-\sigma)}{29\sigma-19}+\varepsilon}.}
\tag{1}
\]
This is a subdivision consequence of established Heath-Brown large-value machinery and an established density conversion. It is not a new mean-square estimate. Section 2 supplies the analytic input directly from the published Guth--Maynard presentation of that machinery, rather than relying on an inaccessible historical paper.

At \(\sigma=.773\), the exponent is \(1589/3417\), compared with \(454/957\) in the identified Table 11.1 of [3], a saving of \(3405/363341>0\). Section 4 verifies the improvement throughout the displayed interval and compares the separate Kerr estimate recorded in [3]. The novelty assertion is limited to this explicit consequence and these identified comparisons. No exhaustive worldwide novelty, explicit implied constant, finite-height zero exclusion, percentage of actual zeros, or RH conclusion is asserted.

## 1. Exponent conventions and the conversion used

Use the large-value exponent \(\mathrm{LV}(\sigma,\tau)\) of [2]: a Dirichlet polynomial of length \(X\), with coefficients bounded by 1, has at most \(X^{\mathrm{LV}(\sigma,\tau)+o(1)}\) values of size \(X^{\sigma-o(1)}\) on a 1-separated set in an interval of length \(X^{\tau+o(1)}\). The equivalent formulation permits any fixed positive loss in the exponent. Let \(\mathrm A(\sigma)\) be the infimum of the coefficients for which
\(N(\sigma,T)\ll_{\sigma,\varepsilon}T^{\mathrm A(\sigma)(1-\sigma)+\varepsilon}\).

We use the following three established properties.

1. The mean-value theorem gives \(\mathrm{LV}(\sigma,\tau)\leq2-2\sigma\) for \(0\leq\tau\leq1\).
2. Subdivision gives
   \(\mathrm{LV}(\sigma,\tau')\leq\mathrm{LV}(\sigma,\tau)+\tau'-\tau\) for \(\tau'\geq\tau\).
3. Corollary 11.9 of [3] states that, if \(\tau_0>0\) and
\[
\mathrm{LV}(\sigma,\tau)\leq
  \frac{3(1-\sigma)}{\tau_0}\tau
\quad(2\tau_0/3\leq\tau\leq\tau_0),
\tag{2}
\]
with the analogous zeta-polynomial estimate for \(2\leq\tau<4\tau_0/3\), then \(\mathrm A(\sigma)\leq3/\tau_0\). In our application \(\tau_0<3/2\), so the entire zeta-polynomial condition is empty. This is the full conversion, not a pointwise large-value bound at one length.

## 2. The required second Heath-Brown estimate, with primary-source derivation

For fixed \(\sigma>3/4\), fixed positive integer \(k\), and \(\tau\geq1\), the input is
\[
\mathrm{LV}(\sigma,\tau)\leq
\max\left\{2-2\sigma,
 k\tau+k(2-4\sigma),
 \frac{2\tau}{3}+\frac{k(12-16\sigma)}3\right\}.
\tag{3}
\]
This is the final formula in [2, Lemma 7.15]. The following derivation retains its full normalization, using [1, Theorem 1.6, Lemma 6.2 and the argument (6.1)--(6.4)]. In particular, we do not invoke Proposition 6.1 outside the global length setup of that paper.

Write the polynomial length as \(X\), its ordinate interval length as \(Y\geq X\), its large-value threshold as \(V=X^\sigma\), and the cardinality as \(R\). Constants and factors \(Y^\epsilon\), for arbitrarily small fixed \(\epsilon>0\), are suppressed in this paragraph. We need only fixed \(Y=X^\tau\), with \(\tau\) in a compact interval. Fix a small \(\kappa>0\). A 1-separated set is a union of \(O(Y^{2\kappa})\) sets separated by \(Y^{2\kappa}\); it suffices to prove the estimates on each such set and finally let \(\kappa\) tend to zero. This loses only an arbitrarily small power.

Choose a fixed smooth \(w\geq1\) on \([1,2]\), supported in \([1/2,3]\), and put
\[
K_X(t)=\sum_{n\geq1}w(n/X)^2n^{it},\qquad
S_{\rm off}=\sum_{t\ne t'\in W}|K_X(t-t')|^2.
\]
The Halasz duality/Cauchy inequality, including the diagonal, gives
\[
(RV)^2\ll RX^2+XR\sqrt{S_{\rm off}}.
\tag{4}
\]
Indeed, align the phases of the large values, apply Cauchy to the polynomial coefficients divided by \(w(n/X)\), and separate the diagonal \(K_X(0)\ll X\) from the off-diagonal Gram entries. The off-diagonal absolute sum is at most \(R\sqrt{S_{\rm off}}\).

Here is the scale and cutoff content of the reflection step. Poisson summation gives \(K_X(t)=X^{1+it}\sum_m\widehat h_t(mX)\), where \(h_t(u)=w(u)^2u^{it}\). For \(|t|\geq Y^{2\kappa}\), the zero Fourier frequency is negligible by repeated integration by parts. On a dyadic difference interval \(|t|\asymp Y_0\), nonstationary phase restricts the nonzero dual labels to \(|m|\leq Y^\kappa Y_0/X\), at an arbitrarily small error. If there are no such labels, the contribution is negligible.

For completeness, the Mellin separation in the proof of [1, Lemma 6.2] uses the rapidly decaying Mellin transform of \(w^2\) on \(\Re s=1\). Truncate its imaginary part to \(|u|\leq Y^\kappa\). For positive dual labels, substitute \(v=mXz\) in the integral, after writing the support as \([1/(2m),3M/m]\), where \(M\) is the common dual cutoff. The resulting common oscillatory integral is over \([X/2,3XM]\), with phase \((t-u)\log v-2\pi v\) and amplitude \(1/v\). Its magnitude is \(\ll Y_0^{-1/2}\), up to logarithms, by the first- and second-derivative integral estimates. The negative-label side is treated in the same way. Since \(Y_0\geq Y^{2\kappa}\), the Mellin shift does not change the scale of \(t\). All cutoff errors can be made smaller than any prescribed power of \(Y^{-1}\).

Cauchy in the Mellin integral, then dyadic subdivision of the dual labels and the difference scale, therefore gives
\[
S_{\rm off}\ll Y^{O(\kappa)}
\max_{1\leq M\leq Y^{1+\kappa}/X}
\frac X M
\sum_{t,t'\in W}\left|\sum_{m\asymp M}a_m m^{i(t-t')}\right|^2,
\qquad |a_m|\leq1.
\tag{5}
\]
An immaterial absolute constant may multiply the upper limit on \(M\). In passing to a smaller dual dyadic block, the original prefactor \(X^2/Y_0\) is at most \(Y^\kappa X/M\), so (5) is an upper bound for every block. Dropping the original dyadic restriction on \(t-t'\) only enlarges a nonnegative sum. The Mellin shift is absorbed into the coefficient phases. These are exactly the reflection and dyadic operations in [1], now applied to the two-point kernel rather than its three-point trace. Changing the fixed support of \(w\) from \([1,2]\) to \([1/2,3]\) changes only absolute constants.

Raise the dual polynomial to the fixed power \(k\) and apply Holder over the at most \(R^2\) ordered pairs. Its coefficients are bounded by a divisor function, hence by \(Y^{o(1)}\); its support is a fixed-factor interval of length comparable to \(M^k\), which may be divided into finitely many dyadic intervals. The full Heath-Brown difference-set estimate as stated in [1, Theorem 1.6] gives
\[
\sum_{t,t'}|D_M(t-t')|^2
\ll Y^{o(1)}R^{2-2/k}
\left(R^2M^k+RM^{2k}+R^{5/4}Y^{1/2}M^k\right)^{1/k}.
\tag{6}
\]
There is no assumption \(M^k\leq Y\) in that theorem. Substitution in (5), followed by \(M\leq Y^{1+\kappa}/X\), yields
\[
S_{\rm off}\ll Y^{o(1)}
\left(XR^2+YR^{2-1/k}
+XR^{2-3/(4k)}Y^{1/(2k)}\right).
\tag{7}
\]
More precisely, (7) holds with any prescribed fixed positive power loss after taking \(\kappa\) sufficiently small. Combining (4) and (7) gives
\[
(RV)^2\ll Y^{o(1)}\left(
RX^2+R^2X^{3/2}
+XY^{1/2}R^{2-1/(2k)}
+X^{3/2}Y^{1/(4k)}R^{2-3/(8k)}\right).
\tag{8}
\]
The term \(R^2X^{3/2}\) is absorbed into the left side because \(\sigma>3/4\), choosing the loss sufficiently small first. Solving each of the other three terms for \(R\), and putting \(Y=X^\tau\), proves (3). Coefficient bounds \(X^{o(1)}\), a threshold \(X^{\sigma-o(1)}\), and thinning are handled by arbitrarily small exponent losses. Thus (3) holds in the exponent convention of Section 1. For \(\tau\leq1\), we will instead use the mean-value theorem.

**Normalization note.** The proof printed below [2, Lemma 7.15] first writes an inequality with an outside factor \(X\); its next exponent display omits the corresponding \(+1\). Formula (8) keeps that factor and gives the stated final formula (3). No conclusion here uses the deficient intermediate display. The historical attribution is Heath-Brown's 1979 large-values work, but our analytic verification uses the accessible primary presentation [1].

## 3. The complete length window

Put \(\eta=1-\sigma\), and define
\[
t_* =\frac{18-12\sigma}{7},\qquad
v_* =\frac{96-120\sigma}{7},\qquad
\alpha=t_*-v_* =\frac{108\sigma-78}{7},
\]
\[
\tau_0=3\eta+\alpha=\frac{3(29\sigma-19)}7,
\qquad E=\frac{3\eta}{\tau_0}=\frac{7\eta}{29\sigma-19}.
\tag{9}
\]
The exact certificate verifies throughout the theorem's interval that
\[
\alpha>0,\quad 0<E<1,\quad
2\tau_0/3<1<t_*<\tau_0<3/2,
\quad 2\eta<v_*<3\eta.
\tag{10}
\]
Use (3) with \(k=3\). The two nonconstant branches are
\[
L_1(\tau)=3\tau+6-12\sigma,\qquad
L_2(\tau)=2\tau/3+12-16\sigma.
\]
They agree at \(t_*\), with common value \(v_*\). At \(\tau=1\), both are at most \(2\eta\), since \(\sigma\geq16/21\). At the crossing,
\[
Et_*-v_*=
\frac{\alpha(3\eta-v_*)}{\tau_0}>0.
\tag{11}
\]
For \(2\tau_0/3\leq\tau\leq1\), mean square gives \(\mathrm{LV}\leq2\eta\leq E\tau\). For \(1\leq\tau\leq t_*\), each affine branch \(L_i(\tau)\) lies below the line \(E\tau\), by its two endpoint comparisons. The constant branch does also. Finally subdivision from the crossing gives
\[
\mathrm{LV}(\sigma,\tau)\leq v_*+\tau-t_*
=\tau-\alpha\leq E\tau\qquad(t_*\leq\tau\leq\tau_0),
\tag{12}
\]
where the last inequality uses \(E<1\) and equality at \(\tau=\tau_0\). This proves (2) over its whole interval. Because \(4\tau_0/3<2\), no zeta-polynomial estimate is needed. Corollary 11.9 proves (1).

All equalities above concern limiting exponents. In the finite inequalities, first fix \(\sigma\) and the requested final \(\varepsilon\), then take all analytic losses and the thinning parameter sufficiently small. The exponent definition and the subdivision/density corollaries retain arbitrarily small positive losses, so one obtains (1) with that \(\varepsilon\), not an endpoint estimate with a uniform constant or a loss-free finite bound.

The useful distinction from a Montgomery-only conversion is \(v_*>2\eta\): the crossing is not in the Montgomery range. Its value is nevertheless below \(3\eta\), which is enough for (11)--(12). At \(\sigma=41/53\), the crossing reaches \(v_*=2\eta\), the threshold occurring in the older \(m=3\) consequence recorded in [3, Lemma 11.30 and Corollary 11.31].

## 4. Identified comparisons and exact verification

The current Table 11.1 in [3] uses
\[
A_{\rm table}(\sigma)=
\begin{cases}
6/(5\sigma-1),&13/17\leq\sigma<17/22,\\
2/(9\sigma-6),&17/22\leq\sigma<41/53.
\end{cases}
\tag{13}
\]
On the first part of our interval, \(7/(29\sigma-19)<6/(5\sigma-1)\) is exactly \(\sigma>107/139\). On the second part, \(7/(29\sigma-19)<2/(9\sigma-6)\) is exactly \(\sigma<4/5\). Both are strict throughout the stated interval, including the change of table branch.

For the separate Kerr estimate recorded as [3, Proposition 11.37], explicitly attributed there to an unpublished preprint,
\[
A_K(\sigma)=\max\left\{\frac{36}{138\sigma-89},
\frac{114\sigma-79}{(1-\sigma)(138\sigma-89)}\right\},
\tag{14}
\]
its second entry alone exceeds the new coefficient throughout our interval. After multiplication by positive denominators, the difference has numerator
\[
4272\sigma^2-6046\sigma+2124>0.
\]
This polynomial is increasing on the interval and positive at its left endpoint. Thus (1) is not weaker than that additional comparator. Formula (14) is used only for comparison, not as an analytic input to the proof.

The accompanying standard-library Python script checks all affine interval conditions, the factored crossing comparison, both table branches, the complete Kerr polynomial comparison, and the exact displayed rational values. The checks certify the whole intervals through affine endpoints and explicit polynomial monotonicity, not a floating-point sample grid. They do not certify the imported analytic theorems or exhaust the literature.

## References

1. Larry Guth and James Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics 203(2) (2026), 623--675, DOI [10.4007/annals.2026.203.2.6](https://doi.org/10.4007/annals.2026.203.2.6). The accessible [author preprint v2](https://arxiv.org/html/2405.20552v2) contains Theorem 1.6, Lemma 6.2, and equations (6.1)--(6.4) used above.
2. Terence Tao, Timothy Trudgian and Andrew Yang, *New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*, [author database, large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-chapter.html), Definitions 7.1--7.3, Lemma 7.4, Theorem 7.9 and Lemma 7.15. The historical reference attached to Lemma 7.15 is D. R. Heath-Brown, *A large values estimate for Dirichlet polynomials*, J. London Math. Soc. s2-20 (1979), 8--18, DOI 10.1112/jlms/s2-20.1.8. We do not claim to have inspected that paywalled text.
3. Same authors, [zero-density chapter](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html), Definition 11.1, Corollaries 11.8--11.9, Table 11.1, Lemmas 11.29--11.30, Corollary 11.31 and Proposition 11.37; see also the [primary paper](https://arxiv.org/html/2501.16779v1). Online formulas were checked on 2026-10-16. The labels refer to the author-maintained blueprint.
