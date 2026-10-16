# A general subdivision refinement of Pintz's density conversion

## Results and attribution

Let
\[
N(\sigma,T)=\sum_{\substack{\zeta(\beta+i\gamma)=0\\
\beta\geq\sigma,\ 0<|\gamma|\leq T}}m(\beta+i\gamma)
\]
count the nontrivial zeros with multiplicity. Counting positive heights only changes a constant. We use the density coefficient \(\mathrm A\) of Tao--Trudgian--Yang [2,3]: an upper bound \(\mathrm A(\sigma)\leq a\) implies
\(N(\sigma,T)\ll_{\sigma,\varepsilon}T^{a(1-\sigma)+\varepsilon}\) for each fixed \(\varepsilon>0\).

**Theorem 1.** Let \(k\geq4\) and \(\ell\geq3\) be integers, and suppose
\[
\frac1{k(k+1)}\leq\eta<\frac1{k(k-1)},\qquad
\frac1{2\ell(\ell+1)}\leq\eta<\frac1{2\ell(\ell-1)}.
\tag{1}
\]
Put
\[
M=\ell\bigl(1-2(\ell-1)\eta\bigr),\qquad
Z=k\bigl(1-(k-1)\eta\bigr).
\]
Then
\[
\boxed{\quad \mathrm A(1-\eta)\leq
\max\left\{\frac3{M+\eta},\frac4Z\right\}.\quad}
\tag{2}
\]
Thus for every fixed admissible \(\eta\) and every \(\varepsilon>0\), the corresponding density exponent is \(\eta\) times the right side of (2), plus \(\varepsilon\).

The earlier Pintz conversion [1, Theorem 1; 3, Theorem 11.35] has \(M\), rather than \(M+\eta\), in the first denominator. Formula (2) follows from the same established exponential-sum input by using the stronger, already established subdivision conversion [2, Corollary 44; 3, Corollary 11.10]. No new exponential-sum estimate is claimed. The previously published narrow specialization near \(\sigma=.99\) is unchanged; this report provides the general conversion and a separate interval comparison.

**Corollary 2.** For
\[
\frac{37}{1000}\leq\eta\leq\frac1{25}
\quad\left(\frac{24}{25}\leq\sigma\leq\frac{963}{1000}\right)
\]
and every \(\varepsilon>0\),
\[
N(1-\eta,T)\ll_{\eta,\varepsilon}
T^{\eta\min\left\{\frac{267}{374-2475\eta},\frac{933}{1334-9333\eta}\right\}+\varepsilon}.
\tag{3}
\]
On this entire interval, (3) improves both the exponent in the identified ANTEDB Table 11.1 and every use of Pintz's separate growth-based density theorem [4] using the declared growth inputs specified in Section 4. At \(\sigma=.96\), the table comparison is
\[
\frac3{76}\ \longrightarrow\ \frac{267}{6875},\qquad
\frac3{76}-\frac{267}{6875}=\frac{333}{522500}>0.
\tag{4}
\]
The optimized declared-growth comparator at this point is slightly better than the table but still weaker than (3): its density coefficient is \(2225/2262\), compared with \(267/275\) in (3). The additional refinement in (3) uses the same current growth input through the direct large-value transfer [3, Corollary 8.13], instead of only through Pintz's separate density theorem.

These are asymptotic upper-bound improvements. There is no claimed effective constant, finite-height zero exclusion, proportion of actual zeros, or proof of RH. Improvement of the stated comparators is not an exhaustive worldwide novelty claim.

## 1. Established analytic inputs

Write \(b(\tau)=\tau\beta(1/\tau)\), in the notation of [2,3]. The Heath-Brown derivative estimate used in Pintz's proof gives, for every integer \(r\geq3\),
\[
b(\tau)\leq1+\max\left\{
\frac{\tau-r}{r(r-1)},\ -\frac1{r(r-1)},\
-\frac{2\tau}{r^2(r-1)}\right\}.
\tag{5}
\]
The classical second-derivative bound also gives \(b(\tau)\leq\tau/2\) for \(1\leq\tau\leq2\).

We use three transfer statements with their original scopes:

1. Montgomery's theorem [3, Theorem 7.10]: a strict bound \(\sup_{1\leq u\leq\tau}b(u)<1-2\eta\) implies \(\mathrm{LV}(1-\eta,\tau)\leq2\eta\). The mean-value theorem supplies the same conclusion for \(0\leq\tau<1\).
2. Zeta interval-sum vanishing [3, Corollary 8.5]: if \(b(\tau)<1-\eta\), then \(\mathrm{LV}_\zeta(1-\eta,\tau)=-\infty\).
3. Subdivision density conversion [2, Corollary 44; 3, Corollary 11.10]: if \(\mathrm{LV}(1-\eta,\tau)\leq2\eta\) through \(\tau=\tau_0-\eta\), and
\[
\mathrm{LV}_\zeta(1-\eta,\tau)\leq3\eta\tau/\tau_0
\quad(2\leq\tau<4\tau_0/3),
\tag{6}
\]
then \(\mathrm A(1-\eta)\leq3/\tau_0\).

We also use [3, Corollary 8.13]: if \(\mu(s)\leq v\), \(v>0\), and \(1-2\eta>s\), then the Montgomery conclusion holds through \((1-2\eta-s)/v\). A fixed small endpoint loss may be inserted throughout.

Subdivision applies to the general-coefficient large-value exponent, not to \(\mathrm{LV}_\zeta\). The decisive endpoint shift is \(\tau_0-\eta\). In particular, the subdivided bound
\[
\mathrm{LV}(1-\eta,\tau)\leq
\max\{2\eta,\ 3\eta+\tau-\tau_0\}
\]
is at most \(3\eta\tau/\tau_0\) on \([2\tau_0/3,\tau_0]\) when \(\tau_0\geq3\eta\). The second branch is checked by
\((\tau_0-3\eta)(\tau_0-\tau)\geq0\).

## 2. Proof of the general conversion

### 2.1 Full Montgomery interval

For \(3\leq r\leq\ell\), (5) is strictly below \(1-2\eta\) on
\[
I_r=\bigl(r^2(r-1)\eta,\ r(1-2(r-1)\eta)\bigr).
\tag{7}
\]
The middle term is strict because \(2\eta<1/[\ell(\ell-1)]\leq1/[r(r-1)]\). Successive upper endpoints increase by \(1-4r\eta>0\). Each overlap between \(I_r\) and \(I_{r+1}\) has length
\[
r\{1-(r^2+4r-1)\eta\}>0.
\]
Indeed, for \(r\leq\ell-1\),
\[
r^2+4r-1\leq\ell^2+2\ell-4
<2\ell(\ell-1),
\]
where the final difference is \((\ell-2)^2>0\). Hence the intervals cover \((18\eta,M)\).

If \(18\eta\geq1\), fill \([1,18\eta]\) using \(b(\tau)\leq\tau/2\leq9\eta<1-2\eta\). Here \(\eta<1/12\) by (1), and \(18\eta<3/2\), so the second-derivative bound is used only in its valid range. If \(18\eta<1\), the intervals already cover \([1,M)\). Their first upper endpoint is greater than 2. Consequently, for every sufficiently small fixed \(d>0\), there is a uniform strict margin on \([1,M-d]\), and
\[
\mathrm{LV}(1-\eta,\tau)\leq2\eta
\qquad(0\leq\tau\leq M-d).
\tag{8}
\]

### 2.2 Full zeta-sum interval

For \(3\leq r\leq k\), (5) is strictly below \(1-\eta\) on
\[
J_r=\bigl(r^2(r-1)\eta/2,\ r(1-(r-1)\eta)\bigr).
\tag{9}
\]
The middle term is strict because \(\eta<1/[k(k-1)]\). Successive upper endpoints increase by \(1-2r\eta>0\), and adjacent overlaps have length
\[
r\{1-(r^2+4r-1)\eta/2\}>0.
\]
For \(r\leq k-1\), the same calculation uses
\(2k(k-1)-(k^2+2k-4)=(k-2)^2>0\).
The first lower endpoint \(9\eta\) is below 2 and its upper endpoint exceeds 2. Thus the intervals cover \([2,Z)\), giving
\[
\mathrm{LV}_\zeta(1-\eta,\tau)=-\infty
\qquad(2\leq\tau<Z).
\tag{10}
\]

### 2.3 Conversion and finite-epsilon passage

Set
\[
D=\min\{M+\eta,3Z/4\},\qquad \tau_0=D-d.
\]
Then \(\tau_0-\eta\leq M-d\), and \(4\tau_0/3<Z\). Also \(M>\ell-1\), \(Z>k-1\), and \(\eta<1/12\); hence \(\tau_0>3\eta\) for small \(d\). Inputs (8) and (10) therefore give
\(\mathrm A(1-\eta)\leq3/(D-d)\).

For a prescribed density-exponent loss \(\varepsilon>0\), choose a fixed \(d>0\) with \(3\eta/(D-d)-3\eta/D<\varepsilon/2\), and then take the transfer's exponent loss below \(\varepsilon/2\). This proves (2) and its ordinary \(N\)-estimate. No uniformity in \(d\) is needed. The strict upper boundaries in (1) also allow the small left shift of \(\sigma\) occurring in the definition of \(\mathrm A\); the lower cell boundaries were not used in the strict estimates.

## 3. The interval .96 through .963

Take \(\ell=4\), \(k=5\), and \(37/1000\leq\eta\leq1/25\). Both cells in (1) hold. Here
\[
M=4-24\eta,\quad Z=5-20\eta,\quad
\frac34Z-(M+\eta)=-\frac14+8\eta>0.
\]
Theorem 1 therefore already gives the intermediate exponent \(3\eta/(4-23\eta)\).

We strengthen its Montgomery input using the current valid growth vertices
\[
\mu(454/641)\leq89/1282,\qquad
\mu(1744/2411)\leq311/4822.
\tag{13}
\]
Corollary 8.13 gives Montgomery endpoints
\[
M_1=\frac{374-2564\eta}{89},\qquad
M_2=\frac{1334-9644\eta}{311}.
\]
Set
\[
D_1=M_1+\eta=\frac{374-2475\eta}{89},\qquad
D_2=M_2+\eta=\frac{1334-9333\eta}{311},\qquad
D_* =\max\{D_1,D_2\}.
\tag{14}
\]
On the entire interval, both \(D_i>4-23\eta\) and both \(D_i<3Z/4\). These are strict affine inequalities, checked exactly at both endpoints in the accompanying certificate. Apply the same subdivision conversion with \(\tau_0=D_*-d\). Its Montgomery endpoint is \(\max(M_1,M_2)-d\), while its zeta interval is inside \([2,Z)\). The finite-epsilon argument in Section 2.3 proves (3).

The two branches cross at \(\eta=67/1692\): \(D_2\) is larger below that value and \(D_1\) above it. The whole interval is inside the Table 11.1 branch \(3/(24\sigma-20)=3/(4-24\eta)\). Since \(D_*>4-23\eta>4-24\eta\), the improvement is strict throughout. At \(\eta=1/25\), \(D_*=275/89\), giving (4).

All fixed-interval cover and side inequalities are affine in \(\eta\), so the exact endpoint certificate proves the closed interval, not merely a numerical sample. The general conversion is not asserted to be optimal, and no stronger-baseline claim is inferred merely from a table's omission. In particular, the intermediate bound alone is beaten by the growth-based comparator at \(\sigma=.97\); our stated interval and full comparison avoid that issue.

## 4. Comparison with the separate growth-based density theorem

Pintz's theorem [4, Theorem 1.2] permits supplied growth constants \(a=\lambda(\eta)\), \(b=\lambda(2\eta)\), with \(q=\lceil b/a\rceil\), and gives the coefficient
\[
\max\{2qa,\ 2b(1+1/q)\}.
\tag{11}
\]
Here the constants are obtained from growth upper bounds by minimizing \(\mu(1-\delta)/(\delta-e)\) over \(\delta>e\). The comparison below concerns the **supplied bounds**, not the unknown true growth function.

The declared family consists of the affine pieces and all Heath-Brown vertices in [3, Table 6.2 and Theorem 6.14], their convex interpolation, both curved bounds in [3, Theorem 6.13], and their functional-equation reflections. The rational data are reproduced in `check_certificate.py`. Write \(D=4-23\eta\). That script proves uniformly on the whole interval that every constant supplied by this family satisfies
\[
a>\frac1{2D},\qquad b>\frac1D.
\tag{12}
\]
For transparency, the complete finite/infinite reduction is as follows.

- At a rational vertex \((s,\mu)\), (12) reduces to
  \(2\mu D>1-s-\eta\) and \(\mu D>1-s-2\eta\). Each is affine in \(\eta\), so both interval endpoints suffice. The inequalities are preserved by convex interpolation, including vertices whose denominator would be nonpositive.
- Only the Heath-Brown vertices \(n=7,8\) need adding to the finite table: \(\delta_9=109/3168<37/1000\), and \(\delta_n=(3n^2-3n+2)/(n(n-1)^2(n+2))\) decreases. Cross-multiplication gives the positive numerator \(2n(3n^4+3n^3+n^2+3n-2)\) for \(\delta_n-\delta_{n+1}\). All later unreflected vertices are ineligible.
- For the global curve \(\mu(1-\delta)\leq(2\sqrt{10}/13)\delta^{3/2}\), the unrestricted ratio minimum at parameter \(e\) has square \(270e/169\). Exact rational comparisons at the stated parameter bounds prove (12). Restricting its domain can only increase that minimum.
- The sharper curved estimate is available only for \(\delta\leq317/118272<37/1000\), so its unreflected part is ineligible. The script separately checks all finite reflected vertices, bounds the infinite reflected tail by \(s-1/2\), and checks the reflected global curve. Thus no negative-real-part extension of the supplied family is silently omitted.

If \(q=1\), (11) is at least \(4b>3/D\). If \(q=2\), it is at least \(3b>3/D\). If \(q\geq3\), it is at least \(6a>3/D\). Thus the comparator is already worse than the intermediate bound, and a fortiori worse than (3), because \(D_*>D\). This proves the claimed comparison for **every** admissible enlargement of the supplied constants, not just the ceiling value obtained from their separately minimal choices.

At \(\eta=1/25\), the minimizing declared inputs are
\[
a=\frac{2225}{9062},\qquad b=\frac{2225}{6786},\qquad q=2,
\]
and (11) equals \(2225/2262>75/77>267/275\). The script also checks the curve and reflected alternatives for this calibration.

This is a comparison against a precisely identified current input family. It does not rule out a stronger application using additional growth information, a different density theorem, or an unlocated publication.

## References and reproducibility

[1] J. Pintz, *Density theorems for Riemann's zeta-function near the line Re s=1*, Acta Arithmetica 208 (2023), 1--13. [DOI](https://doi.org/10.4064/aa210824-10-5), [author PDF](https://real.mtak.hu/164181/1/PJ_Density230311-3.pdf).

[2] T. Tao, T. S. Trudgian and A. Yang, *New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*, [arXiv:2501.16779v1](https://arxiv.org/html/2501.16779v1), Corollary 44.

[3] The authors' Analytic Number Theory Exponent Database: [large values](https://teorth.github.io/expdb/blueprint/largevalue-chapter.html), [zeta large values](https://teorth.github.io/expdb/blueprint/largevalue-zeta-chapter.html), [zero density](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html), and [zeta growth](https://teorth.github.io/expdb/blueprint/zeta-growth-chapter.html), checked 2026-10-16. Numbered inputs are specified above.

[4] J. Pintz, *Remark on a General Zero Density Theorem*, Mathematica Pannonica 29_NS3 (2023), 238--243. [DOI](https://doi.org/10.1556/314.2023.00025), Theorem 1.2; [full-text reproduction inspected](https://www.researchgate.net/publication/375980496_Remark_on_a_General_Zero_Density_Theorem).

Run `python3 check_certificate.py`. It uses only Python's standard library and verifies exact rational side inequalities, the fixed-interval exponent saving, and the declared-input comparison. The general analytic proof is in Section 2; the script is not a replacement for the cited theorems or a global novelty certificate.
