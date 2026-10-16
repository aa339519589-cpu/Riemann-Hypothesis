# A full-diagonal mixed-moment refinement for zeta zero density

## 1. The four-branch result

Count nontrivial zeros with multiplicity by
\[
N(\sigma,T)=\#\{\rho:\zeta(\rho)=0,\ \Re\rho\ge\sigma,
 0<\Im\rho\le T\}.
\]
Put \(\eta=1-\sigma\), and define
\[
c_1=\frac{8751}{10033},\qquad
c_2=\frac{2589}{2923},\qquad
c_3=\frac{136744872}{153875459}.
\tag{1}
\]
For \(433/500\le\sigma\le89/100\), let
\[
y(\sigma)=
\begin{cases}
\dfrac{1629}{4(5831\sigma-4104)},&433/500\le\sigma\le c_1,\\[3pt]
\dfrac{948}{11929\sigma-8119},&c_1\le\sigma\le c_2,\\[3pt]
\dfrac{111885}{1415129\sigma-964637},&c_2\le\sigma\le c_3,\\[3pt]
\dfrac{543}{2742\sigma-1015},&c_3\le\sigma\le89/100.
\end{cases}
\tag{2}
\]
Adjacent branches agree at their endpoints. For every fixed \(\sigma\) in this closed interval and every \(\varepsilon>0\),
\[
\boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}
 T^{4(1-\sigma)y(\sigma)+\varepsilon}.}
\tag{3}
\]

This is a parameter refinement of the complete Chen–Debruyne–Vindas (CDV) zero detector and mixed-moment dichotomy. Its additional point is to keep **both** the diagonal and off-diagonal pieces of the Heath-Brown double mean value factor until after interpolation. No new exponential-sum theorem is asserted.

The exponent strictly improves the identified current density table, including its applicable \(3(1-\sigma)/(2\sigma)\) comparator, throughout the closed interval. It also improves the previously published finite-pair/local-beta envelope wherever that envelope is defined. Representative values are
\[
\begin{array}{c|c}
\sigma&4(1-\sigma)y(\sigma)\\\hline
433/500&109143/472823\\
87/100&7059/32299\\
7/8&3792/18551\\
22/25&1264/6607\\
111/125&447540/2607121\\
89/100&1086/6479.
\end{array}
\tag{4}
\]
These are asymptotic exponents, not percentages of zeros excluded. No effective implied constant, finite-height zero count, global optimality, or worldwide novelty claim is made.

## 2. Primary inputs and the common moment split

The principal source is B. Chen, G. Debruyne and J. Vindas, *On the density hypothesis for L-functions associated with holomorphic cusp forms*, Revista Matemática Iberoamericana **40** (2024), 2179–2202, [publisher PDF](https://ems.press/content/serial-article-files/48886). We use its Section 2 zero detector and common-length construction, Section 3 subdivision, Sections 4.2–4.5 dichotomy and double mean value argument, and Appendix A's zeta adaptation. We re-run the displayed proof with the parameters below; we do not apply its final fixed-parameter theorem outside its stated range.

The exponent pairs
\[
v_3=(2779/38033,58699/76066),\qquad
v_4=(89/1282,997/1282)
\]
are available up to arbitrarily small exponent losses; see the primary author database's [Theorems 5.20 and 5.22](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html). The first also appears in Trudgian–Yang, [Lemma 1.1](https://arxiv.org/html/2306.05599v3). The standard \(B\)-process gives
\[
p_3=(10333/38033,43591/76066),\qquad
p_4=(178/641,365/641).
\tag{5}
\]
For an exponent pair \((k,l)\), write
\[
A=(k+l)/k,\qquad q=2(1+2k+2l)/k.
\]
Trudgian–Yang [Lemma 5.1](https://arxiv.org/html/2306.05599v3), restating Ivić's theorem, bounds a 1-separated set of ordinates \(|t_r|\le U\) at which \(|\zeta(1/2+it_r)|\ge V\) by
\[
R\ll U^\epsilon(UV^{-6}+U^A V^{-q}).
\tag{6}
\]
The two terms are equal at
\[
H(U)=U^{l/(2+4l-2k)}.
\]
Above this threshold the first term dominates, and below it the second dominates. Dyadic level-set integration, with the usual arbitrarily small losses, therefore supplies the **same-split** estimates
\[
\int_0^U|\zeta_0(1/2+it)|^6dt\ll U^{1+\epsilon},\qquad
\int_0^U|\zeta_1(1/2+it)|^qdt\ll U^{A+\epsilon},
\tag{7}
\]
where \(\zeta_0=\zeta1_{|\zeta|\ge H(U)}\) and
\(\zeta_1=\zeta1_{|\zeta|<H(U)}\). This is also the exponent-pair input described on CDV p. 2196. On a subdivided interval the threshold uses its subdivided scale, as in CDV footnote 4. Before the Case-2 dyadic decomposition, remove the subunit portion $|\zeta|<1$ and handle it separately exactly as CDV does (including its footnote 7); the remaining low split is $1\le|\zeta|<H(U)$ and still satisfies (7). No untruncated sixth moment of exponent one is assumed, and incompatible moment truncations are never combined.

For the first two branches of (2) use \(p_4\) in (7); for the last two use \(p_3\). Thus
\[
(A_4,q_4)=(543/178,1727/89),\qquad
(A_3,q_3)=(64257/20666,204580/10333).
\tag{8}
\]
Class II always uses (6) with \(p_4\). The analytic input is the two-term large-value theorem, not a full-moment interpolation claimed in an adjacent discussion.

## 3. Both detected classes and the complete length interval

Take \(Y=T^y\) and the short mollifier \(X=T^{\epsilon_0}\), with \(y\) from (2). The extra polar term in the zeta detector is negligible for ordinates at least \(\log^2T\); the discarded low zeros contribute \(O(\log^3T)\), as in CDV Appendix A.

Use powering parameter \(\nu=2\). For each initial dyadic length \(M\le Y\log^2Y\), choose \(j\ge2\) with \(M^j\le Y^{2+O(\epsilon_0)}<M^{j+1}\). Dyadic subdivision and partial summation yield bounded-coefficient polynomials with
\[
T^{n_0-O(\epsilon_0)}\le N\le T^{n_1+O(\epsilon_0)},\qquad
n_0=4y/3,\quad n_1=2y.
\tag{9}
\]
For **every multiset** occurring in the dichotomy, its corresponding polynomial length \(N(\mathcal A)\asymp N\), exactly CDV (2.6). This common-length property is retained throughout; an arbitrary large-values set is not silently substituted for the detector set.

Set \(E=4\eta y\). A class-II zero gives a shifted critical-line value at least \(T^{-O(\epsilon_0)}Y^{\sigma-1/2}\). Taking representatives \(T^{\epsilon_0}\)-separated keeps their \(O(\log^2T)\) shifts separated. Equation (6) with \(p_4\) gives
\[
|R_2|\ll T^{O(\epsilon_0)}
\left(T^{1-6(\sigma-1/2)y}+T^{A_4-q_4(\sigma-1/2)y}\right).
\tag{10}
\]
Both exponents are at most \(E\) on every branch of (2). The second condition is precisely
\[
y\ge543/(2742\sigma-1015).
\tag{11}
\]
The exact whole-interval signs, including the first term, are certified below.

## 4. Keeping the full double mean value factor

Write \(R\) for the number of representative class-I zeros, initially with \(R\le N\). The upper estimate in CDV Section 4.4, before its simplification using the lower length bound, contains
\[
N(RN+R^2+R^{5/4}T^{1/2})^{1/2}
 (SN+S^2+S^{5/4}T_0^{1/2})^{1/2},\qquad T_0=\delta_2T.
\tag{12}
\]
Since \(R\le N\), its first factor is bounded by a constant times
\[
N^{3/2}R^{1/2}+NR^{5/8}T^{1/4}.
\tag{13}
\]
We retain **both** summands. There is no assumption here that
\(R^{1/4}N^{-1}T^{1/2}\ge1\), and no use of a lower bound on \(R\) to discard a diagonal.

After eliminating CDV's auxiliary dyadic parameters, its two lower terms have the form
\[
N^{2\sigma}\delta_1^2RS
 +N^{2\sigma}\delta_1^{2/q'}\delta_2^{1-1/q'}
 R^{2-1/q'}S^{1/q'},\qquad q'\ge2.
\tag{14}
\]
For each upper term with \(S\)-exponent \(p\in\{1/2,1,5/8\}\), interpolate the lower terms using weight
\((q'p-1)/(q'-1)\). The resulting lower expression is exactly
\[
N^{2\sigma}\delta_1^{2p}\delta_2^{1-p}R^{2-p}S^p.
\tag{15}
\]
In particular, \(q'\) cancels; it need not be confused with the selected mixed-moment exponent in (8).

The three terms from the first summand of (13) therefore give
\[
\begin{split}
D_1&=\delta_1^{-1}\delta_2^{-1/2}N^{2\eta},\\
D_2&=\delta_1^{-4}N^{3-4\sigma},\\
D_3&=\delta_1^{-10/7}\delta_2^{-1/7}
 N^{(12-16\sigma)/7}T^{2/7}.
\end{split}
\tag{16}
\]
The three terms from its second summand give
\[
\begin{split}
H_1&=\delta_1^{-8/7}\delta_2^{-4/7}
 N^{(12-16\sigma)/7}T^{2/7},\\
H_2&=\delta_1^{-16/3}N^{(8-16\sigma)/3}T^{2/3},\\
H_3&=\delta_1^{-5/3}\delta_2^{-1/6}
 N^{(4-8\sigma)/3}T^{2/3}.
\end{split}
\tag{17}
\]
For example the \(p=5/8\) terms also carry \(T_0^{1/4}=\delta_2^{1/4}T^{1/4}\); retaining it produces the displayed \(\delta_2\) powers.

Combining with the complete Case-1 row from CDV Section 4.3 yields
\[
R\ll T^{O(\epsilon_0)}
\left(\delta_2^{-1}N^{2\eta}
 +\delta_1^2TN^{9-12\sigma}
 +\delta_1^2\delta_2^{A-1}T^A N^{(3-4\sigma)q/2}
 +D_1+D_2+D_3+H_1+H_2+H_3\right).
\tag{18}
\]
All nine terms have the same common length. The parameter conditions are
\(T^{-C}\ll\delta_1<1\) and \(T^{-1}\le\delta_2\le1\), with fixed \(C\). Equations (12)–(18) are a direct re-run of the primary proof, not an extrapolation of CDV's final fixed-parameter range.

## 5. Paying every length, including the direct-estimate transition

Write \(n=\log N/\log T\), and initially ignore only the already retained \(O(\epsilon_0)\) losses. Set
\[
\alpha_2=E-2\eta n,\qquad
\alpha_1=\frac{A+(3-4\sigma)qn/2-(A-1)\alpha_2-E}{2}.
\tag{19}
\]
Define
\[
C=(3-4\sigma)q/2+2(A-1)\eta<0,
\qquad n_*=-A(1-E)/C.
\tag{20}
\]
On all four branches,
\[
0<E<n_0<n_*<n_1<1,\qquad
0<\alpha_1(n_0)<1,\qquad0\le\alpha_2\le E/3<1.
\tag{21}
\]
For \(n_0\le n<n_*\), use \(\delta_j=T^{-\alpha_j}\) in (18). Its nine exponents are
\[
\begin{array}{ll}
L_1=2\eta n+\alpha_2,&L_2=1+(9-12\sigma)n-2\alpha_1,\\
L_3=A+(3-4\sigma)qn/2-2\alpha_1-(A-1)\alpha_2,\\
L_4=2\eta n+\alpha_1+\alpha_2/2,&L_5=(3-4\sigma)n+4\alpha_1,\\
L_6=(12-16\sigma)n/7+2/7+10\alpha_1/7+\alpha_2/7,\\
L_7=(12-16\sigma)n/7+2/7+8\alpha_1/7+4\alpha_2/7,\\
L_8=(8-16\sigma)n/3+2/3+16\alpha_1/3,\\
L_9=(4-8\sigma)n/3+2/3+5\alpha_1/3+\alpha_2/6.
\end{array}
\tag{22}
\]
The first and third equal \(E\). The second increases with \(n\) but satisfies \(L_2(n_*)<E\). Each of the other six decreases with \(n\), so it suffices to check its value at \(n_0\).

The constraints giving the first two branches are particularly transparent. With \((A,q)=(A_4,q_4)\),
\[
\begin{split}
E-L_4(n_0)&=\frac{4(5831\sigma-4104)y-1629}{1068},\\
E-L_7(n_0)&=\frac{4((11929\sigma-8119)y-948)}{1869}.
\end{split}
\tag{23}
\]
Thus the diagonal controls first, and then the off-diagonal controls. With \((A,q)=(A_3,q_3)\),
\[
E-L_7(n_0)=
\frac{4((1415129\sigma-964637)y-111885)}{216993}.
\tag{24}
\]
The change of mixed-moment pair is exact, since
\[
\frac{948}{11929\sigma-8119}
-\frac{111885}{1415129\sigma-964637}
=\frac{2349(2923\sigma-2589)}
 {(11929\sigma-8119)(1415129\sigma-964637)}.
\tag{25}
\]
The last branch is the class-II threshold (11). All the remaining signs in (21)–(22), as well as both class-II signs, hold throughout their respective closed intervals. They are checked as rational-function inequalities by the exact certificate, with the displayed formulas as its input. The certificate clears denominators, checks identities polynomially, and proves interval signs through exact Bernstein coefficients. It uses no sampled optimization or numerical grid to certify a continuum.

For \(n\ge n_*\), do not use \(\delta_1>1\). Apply instead CDV Section 3's direct three-term subdivision, using \(\delta_2=T^{-\alpha_2}\). These are the first three rows of (22) with \(\alpha_1=0\). Row 1 equals \(E\); row 3 minus \(E\) is \(C(n-n_*)\le0\); row 2 decreases from its already paid value at \(n_*\), because \(9-12\sigma<0\). This pays the entire upper portion of (9).

## 6. Size cases, losses, and comparison

If \(R<T^E\), the desired estimate is immediate. Otherwise the argument above applies when \(R\le N\). If \(R>N\), take a subset of size comparable to \(N\), retaining CDV's common-length multiset construction. Equations (18)–(22) give a contradiction to \(R'\asymp N\), because \(n_0>E\) has a fixed positive margin. This covers every size case.

For a prescribed final \(\varepsilon>0\), choose the exponent-pair, moment, spacing and dyadic losses sufficiently small first. All relevant exponents and parameters remain in compact ranges; the strict size and parameter margins survive. An \(O(\epsilon_0)\) perturbation of the length endpoints or \(n_*\) costs only \(T^{O(\epsilon_0)}\). At \(n_*\) use the direct estimate. Equalities at the three branch joins are allowed, with the final exponent loss retained. Combining classes I and II proves (3).

For reproducibility, the exact checker compares with these identified rows of the [current density table](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html):
\[
\frac{3}{2\sigma}\quad(\sigma<7/8),\qquad
\frac{3}{10\sigma-7}\quad(7/8\le\sigma<279/314),\qquad
\frac{24}{30\sigma-11}\quad(279/314\le\sigma\le89/100).
\tag{26}
\]
These are coefficients of \(1-\sigma\). Both sides of the downward table jump are checked. The applicable global \(3/(2\sigma)\) coefficient in the database's Proposition 11.37, whose source is described there as an unpublished Kerr preprint, is also checked on the whole interval. The separately inspected Lewko density source's \(3/(2\sigma)\) curve is consequently not overlooked as a comparator; it is not used as an input to this proof.

The [published finite-pair/local-beta envelope](../20261016_halasz_local_envelope/REPORT.md) is checked on each of its intersecting affine cells. Below its left endpoint, the comparison uses \(3/(2\sigma)\), not an extrapolated envelope. The improvement is strict on the entire present interval. The accepted earlier two-branch detector calculation is preserved as a frozen baseline: on its overlap \([7/8,89/100]\), the present bound is strictly better below \(c_2\) and equal from \(c_2\) onward. We do not mistake changing a moment pair for an improvement at every point.

The claims are bounded by these explicit comparisons. The theorem supplies no percentage of actual zeros, effective finite-height exclusion, or unverified strengthening of an imported analytic result.
