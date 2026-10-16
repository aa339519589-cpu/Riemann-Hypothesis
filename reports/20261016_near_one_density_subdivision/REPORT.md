# A near-one zero-density corollary using subdivision

## Statement and comparison

Let
\[
N(\sigma,T)=\sum_{\substack{\zeta(\beta+i\gamma)=0\\
\beta\geq\sigma,\ 0<|\gamma|\leq T}}m(\beta+i\gamma)
\]
count the nontrivial zeros with multiplicity, on both sides of the real axis.
Changing to positive heights only changes an inessential factor of two.

**Theorem.** For every fixed
\[
\frac1{101}\leq\eta\leq\frac1{99}
\quad\left(\frac{98}{99}\leq\sigma=1-\eta\leq\frac{100}{101}\right)
\]
and every \(\varepsilon>0\),
\[
N(1-\eta,T)\ll_{\eta,\varepsilon}
T^{\frac{3\eta}{7-83\eta}+\varepsilon}.
\tag{1}
\]

This follows by combining the established Heath-Brown/Pintz large-value input with the subdivision version of Tao--Trudgian--Yang's density conversion. It strictly improves the exponent recorded in the identified current ANTEDB Table 11.1 on this interval, namely \(3\eta/(7-84\eta)\). At \(\sigma=99/100\), the comparison is
\[
\frac3{616}\quad\longrightarrow\quad\frac3{617},
\qquad
\frac3{616}-\frac3{617}=\frac3{380072}>0.
\tag{2}
\]
It is a power saving in an asymptotic upper bound. No effective constant, finite-height zero exclusion, proportion of actual zeros, or proof of RH is asserted.

## 1. Established inputs and their scopes

We use the notation \(\beta\), \(\mathrm{LV}\), \(\mathrm{LV}_\zeta\), and \(\mathrm A\) of Tao--Trudgian--Yang [2,3]. Here \(\mathrm{LV}\) concerns arbitrary bounded-coefficient Dirichlet polynomials; \(\mathrm{LV}_\zeta\) concerns the special interval sums used by the zeta zero detector. Subdivision below is applied only to the former. A bound \(\mathrm A(\sigma)\leq a\) implies the ordinary zero-density estimate with exponent \(a(1-\sigma)+\varepsilon\). The cited definition includes a small left shift of \(\sigma\); all strict input margins below survive such a shift.

Put \(b(\tau)=\tau\beta(1/\tau)\). The Heath-Brown derivative bound, as used by Pintz [1, §2] and reproduced in [3, proof of Theorem 11.35], gives, for every integer \(r\geq3\),
\[
b(\tau)\leq1+\max\left\{
\frac{\tau-r}{r(r-1)},\ -\frac1{r(r-1)},\
-\frac{2\tau}{r^2(r-1)}\right\}.
\tag{3}
\]
We require these three standard transfer statements:

1. **Montgomery's large-value theorem** [3, Theorem 7.10]: if
\(\sup_{1\leq u\leq\tau}b(u)<2\sigma-1\), then
\(\mathrm{LV}(\sigma,\tau)\leq2-2\sigma\).
For \(0\leq\tau<1\), the same conclusion follows from the mean-value theorem.
2. **Zeta-sum vanishing** [3, Corollary 8.5]: if \(\sigma>b(\tau)\), then
\(\mathrm{LV}_\zeta(\sigma,\tau)=-\infty\).
3. **Subdivision density conversion** [2, Corollary 44; 3, Corollary 11.10]: if
\[
\mathrm{LV}(\sigma,\tau)\leq2-2\sigma
\quad(0\leq\tau\leq\tau_0+\sigma-1)
\tag{4}
\]
and
\[
\mathrm{LV}_\zeta(\sigma,\tau)
\leq3(1-\sigma)\tau/\tau_0
\quad(2\leq\tau<4\tau_0/3),
\tag{5}
\]
then \(\mathrm A(\sigma)\leq3/\tau_0\).

For completeness, the elementary subdivision step in the last statement is
\[
\mathrm{LV}(1-\eta,\tau)
\leq\max\{2\eta,\ 3\eta+\tau-\tau_0\}.
\tag{6}
\]
On \(2\tau_0/3\leq\tau\leq\tau_0\), both terms are at most
\(3\eta\tau/\tau_0\), provided \(\tau_0\geq3\eta\). For the second term this is exactly
\((\tau_0-3\eta)(\tau_0-\tau)\geq0\).
The usual power-raising density conversion [3, Corollaries 11.8--11.9] then applies. No assertion of the Montgomery conjecture outside its proved range is used.

## 2. Complete input intervals

Set
\[
M=7-84\eta,\qquad Z=10-90\eta.
\]
For each \(3\leq r\leq7\), all three expressions inside the maximum in (3) are strictly below \(-2\eta\) when
\[
\tau\in I_r=
\big(r^2(r-1)\eta,\ r(1-2(r-1)\eta)\big),
\tag{7}
\]
because \(2\eta<1/[r(r-1)]\).
These intervals overlap strictly and cover \([1,M)\). Indeed the first lower endpoint is \(18\eta<1\), the last upper endpoint is \(M\), successive upper endpoints increase by \(1-4r\eta>0\), and each adjacent overlap has length
\[
r\{1-(r^2+4r-1)\eta\}>0\qquad(3\leq r\leq6).
\]
Consequently, for every sufficiently small fixed \(d>0\), compactness of \([1,M-d]\) gives a uniform strict margin below \(1-2\eta\). Montgomery's theorem yields
\[
\mathrm{LV}(1-\eta,\tau)\leq2\eta
\qquad(0\leq\tau\leq M-d).
\tag{8}
\]

Similarly, for \(3\leq r\leq10\), all three expressions inside the maximum in (3) are strictly below \(-\eta\) on
\[
J_r=
\big(r^2(r-1)\eta/2,\ r(1-(r-1)\eta)\big),
\tag{9}
\]
since \(\eta<1/[r(r-1)]\). These intervals cover \([2,Z)\): the first lower endpoint is \(9\eta<2\), the first upper endpoint exceeds 2, successive upper endpoints increase by \(1-2r\eta>0\), and their adjacent overlaps have length
\[
r\{1-(r^2+4r-1)\eta/2\}>0\qquad(3\leq r\leq9).
\]
Thus
\[
\mathrm{LV}_\zeta(1-\eta,\tau)=-\infty
\qquad(2\leq\tau<Z).
\tag{10}
\]
Every finite side condition here is affine in \(\eta\); checking the two declared endpoints proves the entire closed interval. The accompanying exact-rational script verifies all of them, rather than sampling interior parameter values.

## 3. Density transfer and epsilon passage

Choose
\[
\tau_0=M+\eta-d=7-83\eta-d.
\]
Then the general-coefficient endpoint in (4) is
\(\tau_0+\sigma-1=M-d\), precisely the range in (8).
The zeta endpoint in (5) lies inside (10), because
\[
\frac34Z-(M+\eta)=\frac12+\frac{31}2\eta>0.
\tag{11}
\]
Also \(\tau_0>3\eta\) for small \(d\). The density conversion therefore gives
\[
\mathrm A(1-\eta)\leq\frac3{7-83\eta-d}.
\]
Given the \(\varepsilon\) in (1), first choose a fixed \(d>0\) so small that
\[
\frac{3\eta}{7-83\eta-d}-\frac{3\eta}{7-83\eta}<\varepsilon/2,
\]
and then use the cited transfer with its exponent loss less than \(\varepsilon/2\). This proves (1); no constant uniform in \(d\) is claimed.

## 4. Baseline and attribution

The declared interval lies strictly inside both Pintz parameter cells
\[
\frac1{112}<\eta<\frac1{84},\qquad
\frac1{110}<\eta<\frac1{90}.
\]
Thus Pintz's original Theorem 1 and [3, Theorem 11.35] apply with
\(\ell=7,k=10\). Their coefficient is
\(\max\{3/M,4/Z\}=3/M\), since (11) is stronger than \(3Z/4>M\).
The difference between the recorded exponent and (1) throughout the interval is
\[
\frac{3\eta^2}{(7-84\eta)(7-83\eta)}>0.
\]
The refinement is the replacement of the weaker density conversion by its already established subdivision form. It is not a new exponential-sum estimate.

The original Pintz author PDF and the current author database were checked on 2026-10-16; both retain the denominator \(7-84\eta\). Pintz's separate growth-based *Remark on a General Zero Density Theorem* [4], when optimized using the current declared zeta-growth envelope [3, Table 6.2 and Theorem 6.13], gives at \(\eta=.01\) the weaker coefficient \(525/1033\). The optional script `check_remark_comparison.py` certifies that specific comparison. It does not assert a value or lower bound for the unknown true zeta-growth function.

We have not found the displayed specialization in the primary sources checked. The precise claim is improvement of the identified table by an unconditional consequence of established inputs, not an assertion of an exhaustive worldwide novelty search. Moving near-one strips, effective finite-height constants, and proportions of critical-line zeros are distinct questions.

## References and reproducibility

[1] J. Pintz, *Density theorems for Riemann's zeta-function near the line Re s=1*, Acta Arithmetica 208 (2023), 1--13. DOI: [10.4064/aa210824-10-5](https://doi.org/10.4064/aa210824-10-5). [Author PDF](https://real.mtak.hu/164181/1/PJ_Density230311-3.pdf).

[2] T. Tao, T. S. Trudgian and A. Yang, *New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*, [arXiv:2501.16779v1](https://arxiv.org/html/2501.16779v1), Corollary 44.

[3] The same authors' Analytic Number Theory Exponent Database, [large values](https://teorth.github.io/expdb/blueprint/largevalue-chapter.html), [zeta large values](https://teorth.github.io/expdb/blueprint/largevalue-zeta-chapter.html), [zero density](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html), and [zeta growth](https://teorth.github.io/expdb/blueprint/zeta-growth-chapter.html), accessed 2026-10-16. The exact numbered inputs are stated above.

[4] J. Pintz, *Remark on a General Zero Density Theorem*, Mathematica Pannonica 29_NS3 (2023), 238--243. DOI: [10.1556/314.2023.00025](https://doi.org/10.1556/314.2023.00025), Theorem 1.2. [Full-text reproduction inspected](https://www.researchgate.net/publication/375980496_Remark_on_a_General_Zero_Density_Theorem).

Run `python3 check_certificate.py` for the finite rational inequalities and exact saving. Run `python3 check_remark_comparison.py` for the optional declared-envelope comparison. Both use only Python's standard library; neither script proves the cited analytic theorems or certifies global novelty.
