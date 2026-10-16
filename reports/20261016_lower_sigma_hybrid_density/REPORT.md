# A hybrid growth-to-density corollary below sigma = .95

## Statement and comparisons

Let \(N(\sigma,T)\) count the nontrivial zeta zeros \(\beta+i\gamma\) with \(\beta\geq\sigma\) and \(0<|\gamma|\leq T\), with multiplicity. The convention using only positive heights changes an inessential factor of two.

**Theorem.** For every fixed
\[
\frac{467}{500}\leq\sigma\leq\frac{941}{1000}
\]
and every \(\varepsilon>0\),
\[
\boxed{\quad N(\sigma,T)\ll_{\sigma,\varepsilon}
T^{\frac{288(1-\sigma)}{1736\sigma-1389}+\varepsilon}.\quad}
\tag{1}
\]
This is an unconditional consequence of two established zeta-growth bounds and the established large-value/subdivision density transfers. It improves the exponent in the identified ANTEDB Table 11.1 throughout the interval. It also improves every use of Pintz's separate growth-based density theorem with the declared growth-input family specified below. At \(\sigma=47/50=.94\),
\[
\frac{1173}{16471}\ \longrightarrow\ \frac{432}{6071},\qquad
\frac{1173}{16471}-\frac{432}{6071}
=\frac{447}{7691957}>0.
\tag{2}
\]

These are asymptotic upper-bound exponent savings, not percentages of zeros, explicit finite-height exclusions, or a proof of RH. The claim is improvement of the stated comparators; no exhaustive worldwide novelty claim is made. No new exponential-sum or mean-square estimate is asserted.

## 1. Analytic inputs and complete transfer

Use \(\mathrm A\), \(\mathrm{LV}\), \(\mathrm{LV}_\zeta\), and \(\mu\) as in Tao--Trudgian--Yang [1,2]. A bound \(\mathrm A(\sigma)\leq a\) gives the ordinary density exponent \(a(1-\sigma)+\varepsilon\).

The two valid growth bounds from [2, Table 6.2] are
\[
\mu(1389/1736)\leq9/217,\qquad
\mu(521/796)\leq18/199.
\tag{3}
\]
The established transfers we use are:

- [2, Corollary 8.6]: \(\mathrm{LV}_\zeta(\sigma,\tau)=-\infty\) when \(\sigma>s+\tau\mu(s)\). We use this only for \(\tau\geq2\).
- [2, Corollary 8.13]: a growth bound \(\mu(s)\leq v\), \(v>0\), gives \(\mathrm{LV}(\sigma,\tau)\leq2-2\sigma\) through \(\tau=(2\sigma-1-s)/v\), with an arbitrarily small fixed endpoint loss allowed.
- [1, Corollary 44; 2, Corollary 11.10]: if the latter Montgomery bound holds for \(0\leq\tau\leq\tau_0+\sigma-1\), and \(\mathrm{LV}_\zeta(\sigma,\tau)\leq3(1-\sigma)\tau/\tau_0\) for \(2\leq\tau<4\tau_0/3\), then \(\mathrm A(\sigma)\leq3/\tau_0\).

Put \(\eta=1-\sigma\), so \(59/1000\leq\eta\leq33/500\). The first input in (3) gives zeta-sum vanishing for \(2\leq\tau<Z\), while the second gives the Montgomery bound through \(M\), where
\[
Z=\frac{347-1736\eta}{72},\qquad
M=\frac{275-1592\eta}{72}.
\tag{4}
\]
The key strict overlap is
\[
M+\eta-\frac34Z=\frac{59-872\eta}{288}>0
\tag{5}
\]
on the full declared interval. Moreover \(3Z/4>3\eta\).

Choose \(\tau_0=3Z/4-d\), with \(d>0\) sufficiently small. Then \(\tau_0-\eta<M\), and the entire required zeta interval is inside \([2,Z)\). Thus the subdivision theorem gives \(\mathrm A(1-\eta)\leq3/(3Z/4-d)\).
Given \(\varepsilon>0\), first choose fixed \(d\) so that the density-exponent increase relative to \(4\eta/Z\) is less than \(\varepsilon/2\), and then take the transfer loss below \(\varepsilon/2\). This proves (1). All strict margins survive the small left shift of \(\sigma\) in the definition of \(\mathrm A\); no uniform constant as \(d\to0\) is claimed.

Subdivision is used only for general-coefficient large values. No subdivision assertion for the special zeta interval sums is required.

## 2. Exact comparison with the identified table

The whole interval lies inside the current Table 11.1 branch
\[
\mathrm A(\sigma)\leq\frac{391}{2493\sigma-2014}
=\frac{391}{479-2493\eta}.
\]
Both denominators are positive. Cross-multiplication shows that (1) is strictly stronger precisely when
\[
39208\eta>2275,
\tag{6}
\]
which holds throughout the declared interval. Equations (4)--(6) and the interval containment are affine inequalities, and the accompanying exact script checks both endpoints. The computation in (2) is exact rational arithmetic.

## 3. The separate Pintz growth-density comparator

Pintz [3, Theorem 1.2] gives, with supplied constants \(a=\lambda(\eta)\), \(b=\lambda(2\eta)\), and \(q=\lceil b/a\rceil\), the coefficient
\[
\max\{2qa,\ 2b(1+1/q)\}.
\tag{7}
\]
Supplied constants come from minimizing the declared upper-growth values \(\mu(1-\delta)/(\delta-e)\) over \(\delta>e\). They are not the unknown optimal constants of the true growth function.

The declared comparison family is [2, Table 6.2 and Theorems 6.13--6.14]: all its rational vertices and convex interpolation, the full Heath-Brown tail, both curved bounds, and the functional-equation reflections. Set \(D=347-1736\eta\). The exact checker proves throughout the interval that every supplied pair satisfies
\[
a>48/D,\qquad b>96/D.
\tag{8}
\]
Consequently, (7) exceeds \(288/D\): for \(q=1\) use \(4b\), for \(q=2\) use \(3b\), and for \(q\geq3\) use \(6a\). This also covers enlarging the supplied constants to change the ceiling \(q\).

Here is the complete reduction behind the finite certificate:

1. At a rational vertex \((s,v)\), (8) follows from \(vD>48(1-s-\eta)\) and \(vD>96(1-s-2\eta)\). These are affine in \(\eta\), so endpoint checks prove the interval. Convex interpolation preserves them, even when an individual vertex is outside \(\delta>e\).
2. The Heath-Brown parameters are \(\delta_n=(3n^2-3n+2)/(n(n-1)^2(n+2))\), \(v_n=2/((n-1)^2(n+2))\). Already \(\delta_7=32/567<59/1000\), and \(\delta_n\) decreases. The positive numerator of \(\delta_n-\delta_{n+1}\), after cross-multiplication, is \(2n(3n^4+3n^3+n^2+3n-2)\). Thus all these unreflected tail vertices are ineligible; their reflected values are uniformly bounded below by \(s-1/2\), which the script checks against both targets.
3. For the global curve \((2\sqrt{10}/13)\delta^{3/2}\), the unrestricted minimum ratio at parameter \(e\) has square \(270e/169\). The script checks this against the targets in (8), together with its full reflected curve. The other curve is confined to \(\delta\leq317/118272\), so its unreflected part is ineligible and its reflected part is harmless by the same \(s-1/2\) comparison.
4. The region \(s\leq0\) supplied by the functional equation has growth \(1/2-s\); its defining ratio is at least \(1/2\), also larger than the targets.

Thus this is a comparison against the entire declared family, not just the two vertices used in the proof of (1). It does not rule out other input theorems or unlocated literature.

## References and reproducibility

[1] T. Tao, T. S. Trudgian and A. Yang, *New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*, [arXiv:2501.16779v1](https://arxiv.org/html/2501.16779v1), Corollary 44.

[2] The authors' Analytic Number Theory Exponent Database: [zeta large values](https://teorth.github.io/expdb/blueprint/largevalue-zeta-chapter.html), [zero density](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html), and [zeta growth](https://teorth.github.io/expdb/blueprint/zeta-growth-chapter.html), checked 2026-10-16. The numbered statements are identified above.

[3] J. Pintz, *Remark on a General Zero Density Theorem*, Mathematica Pannonica 29_NS3 (2023), 238--243. [DOI](https://doi.org/10.1556/314.2023.00025), Theorem 1.2; [full-text reproduction inspected](https://www.researchgate.net/publication/375980496_Remark_on_a_General_Zero_Density_Theorem).

Run `python3 check_certificate.py`. The script uses only Python's standard library and reproduces the exact elementary inequalities. It does not prove the imported analytic theorems or certify global novelty.
