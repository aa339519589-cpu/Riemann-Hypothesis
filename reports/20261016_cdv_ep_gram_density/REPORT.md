# Exponent-pair double-Gram bounds in a zeta zero detector

## 1. Quantitative statement and scope

Let
\[
N(\sigma,T)=\#\{\rho:\zeta(\rho)=0,\ \Re\rho\ge\sigma,
 0<\Im\rho\le T\},
\]
counting multiplicity, and put \(\eta=1-\sigma\). Define
\[
I_L=[873/1000,111/125],\qquad I_H=[229/250,933/1000],
\]
and
\[
y(\sigma)=
\begin{cases}
\displaystyle\max\left\{\frac{1629}{4(5831\sigma-4104)},
\frac{543}{2742\sigma-1015}\right\},&\sigma\in I_L,\\[4pt]
\displaystyle\frac{89}{1282\sigma-908},&\sigma\in I_H.
\end{cases}\tag{1}
\]
The low branches switch at \(13371/15098\), where their values agree. For every fixed
\(\sigma\in I_L\cup I_H\) and every \(\varepsilon>0\),
\[
\boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}
 T^{4(1-\sigma)y(\sigma)+\varepsilon}.}\tag{2}
\]
For example, the exponents at \(7/8,22/25,23/25\) are respectively
\[
\frac{1629}{7985},\qquad\frac{4887}{25682},\qquad
\frac{356}{3393}.\tag{3}
\]

The extra mechanism is elementary: the two self-Gram sums after the
Chen–Debruyne–Vindas (CDV) Cauchy inequality have coefficients **one**.
An exponent-pair estimate can therefore replace the double-mean-value
bound at that precise point. Both diagonal factors are retained, and
one product is absorbed only after checking a strict exponent margin.
The high interval additionally uses a shifted zero-detector contour;
the Halász kernel in the class-I argument is not shifted.

This is a refinement of established detector and exponential-sum inputs,
not a new exponent pair. The comparisons in Section 8 are with explicitly
identified results. No global optimality, worldwide novelty, effective
implied constant, finite-height count, or percentage of zeros excluded
is asserted.

## 2. Inputs and the shared critical-line split

Our detector source is B. Chen, G. Debruyne and J. Vindas,
*On the density hypothesis for L-functions associated with holomorphic
cusp forms*, Revista Matemática Iberoamericana **40** (2024), 2179–2202,
[publisher PDF](https://ems.press/content/serial-article-files/48886).
We use Section 2, the unspecialized proof in Sections 3–4, and Appendix A.
We re-run that proof rather than extrapolate its final fixed-parameter theorem.

The [primary exponent database](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html)
records Bourgain's pair
\[
(k,l)=(13/84,55/84),\tag{4}
\]
in Theorem 5.12, and the pair
\[
v_4=(89/1282,997/1282)\tag{5}
\]
in Theorem 5.22. All uses permit arbitrarily small exponent losses.
The standard B-process applied to \(v_4\) gives
\(p=(178/641,365/641)\). Trudgian–Yang,
[Lemma 5.1](https://arxiv.org/html/2306.05599v3), gives the critical-line
large-value estimate
\[
R\ll U^\epsilon(UV^{-6}+U^A V^{-q}),\qquad
 A=543/178,\quad q=1727/89.\tag{6}
\]
Here the ordinates are separated and have magnitude at most \(U\).
At the threshold where the two terms agree, dyadic level-set integration
pays a high-value sixth moment of exponent \(1+\epsilon\) and a low-value
\(q\)-moment of exponent \(A+\epsilon\). These use the **same threshold**.
The threshold is taken at the subdivided scale \(U=T_0\) when required.
As in CDV footnotes 4 and 7, the part \(|\zeta|<1\) is treated separately,
and the low dyadic split used in Case 2 is \(1\le|\zeta|<H(T_0)\).
There is no assumption of an untruncated sixth moment of exponent one.

Finally, [Corollary 6.8](https://teorth.github.io/expdb/blueprint/zeta-growth-chapter.html)
gives \(\mu(l'-k')\le k'\) for an exponent pair \((k',l')\).
Thus (5) supplies
\[
\mu(454/641)\le89/1282.\tag{7}
\]

## 3. A coefficient-one self-Gram estimate

For a 1-separated finite set \(\mathcal R\) in an interval of length
\(O(U)\), write \(R=|\mathcal R|\), and define
\[
Q(\mathcal R,N)=\sum_{t,t'\in\mathcal R}
 \left|\sum_{N<n\le2N}n^{i(t-t')}\right|^2.
\]
For \(1\le N\le U\), any exponent pair \((k,l)\) gives
\[
Q(\mathcal R,N)\ll U^\epsilon
 \left(RN^2+R^2U^{2k}N^{2(l-k)}\right).\tag{8}
\]
To see this, first let \(1\le|u|\le N\). The derivative of
\(u\log x/(2\pi)\) on \([N,2N]\) is monotone, separated from zero by a
constant times \(|u|/N\), and has magnitude below \(1/(2\pi)\).
The first-derivative estimate gives
\[
\left|\sum_{N<n\le2N}n^{iu}\right|\ll N/(1+|u|),
\]
including \(u=0\) by the trivial estimate. Unit separation implies
\(\sum_{t'}(1+|t-t'|)^{-2}\ll1\), so this whole range contributes
\(O(RN^2)\), not an \(R^2\) diagonal error. For \(|u|>N\), the exponent-pair
bound for the logarithmic phase gives
\(\ll U^\epsilon |u|^kN^{l-k}\). Equivalently, any additional
\(N/|u|\) term in the conventional formulation is absorbed here.
Summing its square proves (8). The same proof applies to an interval
inside \([N,2N]\).

The restriction to coefficients one is essential to this argument.
For a detector polynomial with \(|a_n|\le1\), CDV Lemma 4.2 first gives
\[
\sum_{t\in\mathcal R,s\in\mathcal S}
 \left|\sum_{N<n\le2N}a_n n^{i(t-s)}\right|^2
 \le Q(\mathcal R,N)^{1/2}Q(\mathcal S,N)^{1/2}.\tag{9}
\]
Indeed choose its majorizing coefficients equal to one on the dyadic
interval and zero elsewhere. We apply (8) only **after** this step;
no arbitrary-coefficient version of (8) is being claimed.

## 4. Both zero-detection alternatives and the complete length window

Take \(X=T^{\epsilon_0}\), \(Y=T^y\), and the usual short Möbius
mollifier. CDV's power parameter \(\nu=2\), dyadic subdivision and partial
summation give representative class-I polynomials with
\[
N=T^{n+O(\epsilon_0)},\qquad 4y/3\le n\le2y.\tag{10}
\]
For every multiset arising later, its corresponding length
\(N(\mathcal A)\asymp N\) is retained, precisely as in CDV (2.6).
The power is a bounded integer for fixed \(\epsilon_0>0\). Separation and
multiplicity cost only \(T^{O(\epsilon_0)}\).

On \(I_L\), keep the detector contour at real part \(1/2\).
A class-II zero forces a critical-line value at least
\(T^{-O(\epsilon_0)}Y^{\sigma-1/2}\). Equation (6) bounds its count by
\[
T^{O(\epsilon_0)}
 \left(T^{1-6(\sigma-1/2)y}+T^{A-q(\sigma-1/2)y}\right).\tag{11}
\]
Both exponents are at most \(E=4(1-\sigma)y\) for the low branches of (1).

On \(I_H\), instead shift the detector contour to a fixed
\(\chi=454/641\). If \(\rho=\beta+it\), \(\beta\ge\sigma\), the remaining integral
is bounded by
\[
T^{\mu(\chi)+O(\epsilon_0)}Y^{\chi-\sigma}.\tag{12}
\]
Here \(|M_X(\chi+iv)|\ll X^{1-\chi+\epsilon_0}\), and the Gamma kernel
has exponential vertical decay. Its real part \(\chi-\beta\) lies in a
fixed compact subinterval of \((-1,0)\), so there is no Gamma-pole issue.
As in CDV Appendix A, the additional zeta-pole residue is
\(M_X(1)Y^{1-\rho}\Gamma(1-\rho)=o(1)\) for
\(|t|\ge\log^2T\); the omitted low zeros are \(O(\log^3T)\).
Taking \(y=y(\sigma)+d\), with fixed \(d>0\), makes (12) \(o(1)\) when
\(\epsilon_0\) is sufficiently small. Thus every remaining zero is
class I. This modifies only the initial detector contour, not the
critical-line zeta kernel in CDV Lemma 3.1 or its common moment split.
The fixed \(d\) is removed into the final exponent loss in Section 7.

## 5. The complete replacement in CDV Case 2

Let \(T_0=\delta_2T\). After the unchanged CDV dyadic construction and
(9), insert (8) at scales \(T\) and \(T_0\). With \(S=|\mathcal S|\),
the four upper terms, apart from small exponent losses, are
\[
\begin{split}
&N^2R^{1/2}S^{1/2},\\
&T^kN^{1+l-k}RS^{1/2},\\
&T_0^kN^{1+l-k}R^{1/2}S,\\
&T^kT_0^kN^{2l-2k}RS.
\end{split}\tag{13}
\]
The auxiliary set \(\mathcal S\) is 1-separated and lies in an interval
of length \(O(T_0+T^{\epsilon_0})\), as in CDV Section 4.4. Our parameters
have \(N<T_0\) with a fixed exponent margin, and
\(T^{\epsilon_0}=o(T_0)\), so (8) is valid for both factors.

The two unchanged CDV lower terms interpolate to
\[
N^{2\sigma}\delta_1^{2p}\delta_2^{1-p}
 R^{2-p}S^p,\qquad p\in[1/q',1],\quad q'\ge2.\tag{14}
\]
Explicitly the endpoints are
\(N^{2\sigma}\delta_1^2RS\) and
\(N^{2\sigma}\delta_1^{2/q'}\delta_2^{1-1/q'}
 R^{2-1/q'}S^{1/q'}\); use weight
\((q'p-1)/(q'-1)\). Thus both \(p=1/2\) and \(p=1\) are lawful and
\(q'\) cancels. The first three products of (13) give
\[
\begin{split}
D_1&=\delta_1^{-1}\delta_2^{-1/2}N^{2-2\sigma},\\
D_2&=\delta_1^{-4}\delta_2^{2k}T^{2k}
 N^{2+2l-2k-4\sigma},\\
D_3&=\delta_1^{-2}\delta_2^{-1}T^{2k}
 N^{2+2l-2k-4\sigma}.
\end{split}\tag{15}
\]
Their order corresponds respectively to products one, three and two.
The last product is **not another count bound**. It is absorbed into
the first lower term only under the strict power inequality
\[
\delta_1^2N^{2\sigma}\gg T^{2k}\delta_2^kN^{2l-2k}.\tag{16}
\]
Every instance of (16) is certified below.

Combining (15) with the unchanged Case-1 argument gives
\[
R\ll T^{O(\epsilon_0)}\left(
 \delta_2^{-1}N^{2\eta}
 +\delta_1^2TN^{9-12\sigma}
 +\delta_1^2\delta_2^{A-1}T^AN^{(3-4\sigma)q/2}
 +D_1+D_2+D_3\right).\tag{17}
\]
This keeps all products and the shared detector length. The precise
hypotheses used from CDV remain \(T^{-C}\ll\delta_1<1\),
\(T^{-1}\le\delta_2\le1\), common multiset lengths, and fixed positive
length exponent. The original use of \(N\ge T^{1/2}\) to simplify the
Heath-Brown product is removed by (8). The later Cauchy smoothing constant is absorbed since
N has a fixed positive exponent and sigma>0. Its other explicit use, CDV
footnote 6, absorbs the subunit term
\(N^{3/4-\sigma}T^{O(\epsilon_0)}\); here this still tends to zero because
\(\sigma>3/4\) and \(n\) has a fixed positive lower bound. Lemma 3.1's
Gamma-tail argument needs only \(N\le T^{1+O(\epsilon_0)}\).
No bound stated only for \(N\ge\sqrt T\) is applied below that range.

## 6. An endpoint certificate for every length

Set \(E=4\eta y\), \(n_0=4y/3\), \(n_1=2y\), and
\[
\begin{split}
\alpha_2&=E-2\eta n,\\
a_0(n)&=\tfrac12[1+(9-12\sigma)n-E],\\
a_1(n)&=\tfrac12[A+(3-4\sigma)qn/2-(A-1)\alpha_2-E],\\
\alpha_1&=\max\{0,a_0(n),a_1(n)\},\\
\delta_1&=\tfrac12T^{-\alpha_1},\qquad
\delta_2=T^{-\alpha_2}.
\end{split}\tag{18}
\]
The factor \(1/2\) makes \(\alpha_1=0\) legal without using
\(\delta_1=1\). It changes no exponent and is harmless in the strict
absorption (16). The first three exponents in (17) are at most \(E\)
by the definition of \(\alpha_1\).

Write \(B=2k+(2+2l-2k-4\sigma)n\). The last three exponents and the
absorption margin are
\[
\begin{split}
d_1&=2\eta n+\alpha_1+\alpha_2/2,\\
d_2&=B+4\alpha_1-2k\alpha_2,\\
d_3&=B+2\alpha_1+\alpha_2,\\
g&=(2\sigma-2l+2k)n-2k+k\alpha_2-2\alpha_1.
\end{split}\tag{19}
\]
For fixed \(\sigma,y\), \(\alpha_1\) is the maximum of three affine
functions of \(n\), hence convex. Each \(d_j\) is convex and \(g\) is
concave. It therefore suffices to check
\[
d_j(n_0),d_j(n_1)\le E,\qquad g(n_0),g(n_1)>0.\tag{20}
\]
At each endpoint, the maximum in (18) is handled by checking each of
its three affine options separately. This proves the whole length
interval, including any internal switches, rather than a grid of lengths.

The accompanying exact rational certificate verifies (20) on each of
the three complete closed \(\sigma\)-cells in (1). It also verifies
\[
0<E<n_0<n_1<1,\quad 0\le\alpha_1<1,\quad
0\le\alpha_2\le E/3<1,\quad n+\alpha_2<1.\tag{21}
\]
For the last inequality, its left side increases with \(n\) and equals
\(n_1<1\) at \(n_1\), proving \(N<T_0\). Bounds for \(\alpha_1\) follow
from its convexity and the endpoint checks. Every denominator is checked
positive and every interval sign is proved using exact Bernstein
coefficients. There is no floating-point or sampled certificate.

## 7. Size cases and small losses

Equations (17)–(21) give \(R\ll T^{E+O(\epsilon_0)}\). If the CDV
size normalization requires \(R\le N\), an \(R>N\) set is reduced to a
subset of cardinality comparable to \(N\), still retaining the common
multiset construction. The same bound contradicts \(R'\asymp N\),
since \(n_0-E>0\) has a fixed margin. This pays all size cases.

For a prescribed final \(\varepsilon>0\), first choose the high-interval
contour margin \(d>0\), if needed, sufficiently small. At \(y=y(\sigma)\)
all the strict inequalities in (20)–(21) have positive margins. They
persist under this perturbation. Any nonstrict inequalities incur only
\(O(d)\) changes; allowing an \(O(d)\) loss in the target count exponent
pays them. Next choose all exponent-pair, moment, spacing and detector
losses \(\epsilon_0\) sufficiently small in terms of \(d\), those strict
margins and \(\varepsilon\). The parameters and the coefficients of all
rows lie in compact ranges. Endpoint perturbations in (10) also cost
only \(O(\epsilon_0)\). The total final exponent loss is less than
\(\varepsilon\). On the low interval take \(d=0\) and retain the ordinary
small losses. The low branch join and all outer endpoints are included.
Combining the two detector classes proves (2).

## 8. Precisely identified comparisons and reproducibility

On \(I_L\), (2) strictly improves the previously published
[full-diagonal CDV refinement](../20261016_cdv_full_diagonal_density/REPORT.md).
The checker intersects every one of that result's applicable branches,
including both of its interior switches. On \(I_H\), the
[finite-pair/local-beta envelope](../20261016_halasz_local_envelope/REPORT.md)
has exponent \(\eta/(3\sigma-2)\), and (2) is strictly smaller throughout.
In particular the old \(E(23/25)=2/19\) is reduced to (3).

The checker also compares against the applicable rows of the
[current density table](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html):
\[
\frac{E_{\rm old}}{\eta}=
\frac{3}{2\sigma},\quad
\frac{3}{10\sigma-7},\quad
\frac{24}{30\sigma-11},\quad
\frac{11}{48\sigma-36},
\]
on their proper ranges, including the downward switch at \(279/314\).
It separately checks \(3/(2\sigma)\) over both full intervals, retaining
that comparator regardless of its broader prior-source provenance.
These comparisons do not assert that all literature has been exhausted.

Run `python check_certificate.py`. Only the Python standard library is
required. The program proves rational identities and all stated
whole-interval signs. It does not itself prove the analytic input theorems;
their roles and the complete replacement argument are given above.
