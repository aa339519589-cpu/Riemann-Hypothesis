# An entire full-prime reflected-energy dual curve that detects every zeta zero and its multiplicity

Date: 2026-10-13. The unchanged objective is an **unconditional complete proof of RH**, meaning all nontrivial zeros of zeta have real part 1/2. This note establishes a new *exact, Hilbert-energy-continuous, complex-analytic* zero selector in the **actual full reflected von Mangoldt prime-power edge energy**, and an unconditional multiplicity-resolved independence theorem in that energy completion. It extends the preceding real-zero-only energy obstruction to *every complex zero*, with every derivative through its actual multiplicity. The full first-prime, higher-prime, and full Gamma source identities are untouched.

**No unconditional proof of RH is obtained.** The zero criterion below is an exact reformulation in a newly constructed energy-dual family; it is not a proof that the criterion has only real solutions.

## 1. Original objects and the precise energy topology

Use the complete original positive even theta source Phi, put psi=-Phi', and write
\[
\Xi(z)=\int_{\mathbb R}\Phi(x)\cos(zx)\,dx=\xi(\tfrac12+iz).
\tag{1}
\]
The function Phi and its derivatives have double-exponential real tails and holomorphic continuations to each closed strip \(|\operatorname{Im}x|\le\sigma<\pi/4\), with uniform double-exponential tails on those horizontal lines. Psi is odd, and the exact theta sign theorem gives
\(\psi(x)>0\) for x>0 and a simple zero at x=0. In particular
\[
A:=\Xi(0)=\int_{\mathbb R}\Phi(x)dx>0,\qquad
\int_{\mathbb R}x\psi(x)dx=A,\qquad
\int_{\mathbb R}\psi(x)\sin(zx)dx=z\Xi(z).
\tag{2}
\]
The latter two equalities follow by ordinary integration by parts, valid for every complex z.

For n>=2 set \(d_n=\log n\), \(\alpha_n=\Lambda(n)/\sqrt n\). The **original complete reflected-prime energy** on a smooth compactly supported positive-wing ratio r (with smooth even extension) is
\[
N[r]=\sum_{n\ge2}\alpha_n
\int_0^{d_n}\psi(x)\psi(d_n-x)
\left|r(x)-r(d_n-x)\right|^2dx .
\tag{3}
\]
All actual prime powers are included, although a constructive dual current below will use only the original p=2,3 prime-power channels. Let \(\mathcal H_N\) be the closed image of this compact ratio core under the exact edge-gradient map
\[
(\nabla_Nr)_n(x)=r(x)-r(d_n-x),
\quad 0<x<d_n,
\tag{4}
\]
inside the Hilbert direct sum with positive edge measures
\(\alpha_n\psi(x)\psi(d_n-x)dx\). Thus N is the squared image norm, with its exact null directions automatically quotiented. The genuine theta null jets are
\[
f_j=\Phi^{(2j+3)}-\tfrac14\Phi^{(2j+1)},\qquad
r_j=f_j/\psi,\qquad j=0,1,\ldots .
\tag{5}
\]
They have smooth even extensions across zero and lie in the **completion** \(\mathcal H_N\) via their actual gradients; this is established with explicit cutoffs in [reflected-prime energy](../20261013_reflected_prime_energy/REPORT.md), Sections 1–2. They obey the polar-inclusive original source form identity \(P(r_j,r)=N(r_j,r)\) on the compact core. We do not assume that their gradient span is dense.

## 2. The zero-mean holomorphic renormalization

Define for every \(z\in\mathbb C\) the **explicit complex source**
\[
\boxed{
q_z(x)=\psi(x)\left[\sin(zx)-
\frac{z\Xi(z)}{\Xi(0)}x\right].}
\tag{6}
\]
This source is even in x, vanishes at x=0, and has **exactly zero ordinary integral for every complex z**:
\[
q_z(-x)=q_z(x),\qquad q_z(0)=0,\qquad
\int_{\mathbb R}q_z(x)dx=0.
\tag{7}
\]
These properties are algebraic consequences of (2), not estimates and not conditional on RH. Note that \(q_0\equiv0\), but \(q_z\not\equiv0\) for every \(z\ne0\): the cubic coefficient of \(\sin(zx)\) cannot equal that of a multiple of x.

Define on the compact ratio core
\[
\boxed{\mathcal J_z(r)=
\int_{\mathbb R}q_z(x)r(|x|)dx
=2\int_0^\infty q_z(x)r(x)dx.}
\tag{8}
\]
At a zeta zero \(\Xi(z)=0\), this is exactly the unrenormalized sine functional
\(2\int_0^\infty\psi(x)\sin(zx)r(x)dx\). However, the subtraction in (6) makes the functional admissible for **all** z, so it can be differentiated as a genuine energy-dual-valued holomorphic curve rather than only pointwise at isolated zeros.

**Theorem 1 (entire energy-dual curve).** Every \(\mathcal J_z\) extends uniquely to a bounded complex-linear functional on \(\mathcal H_N\). The map
\[
\boxed{z\longmapsto\mathcal J_z\in\mathcal H_N^*}
\tag{9}
\]
is entire in operator norm: for every compact \(K\subset\mathbb C\),
\[
\sup_{z\in K}\|\mathcal J_z\|_{\mathcal H_N^*}<\infty,
\]
and all its z derivatives can be taken in the operator norm. Each functional has an exact finite-norm current using only the **actual** \(2^j\) and \(3^j\) reflected edges, with no artificial edge replacements and no prime truncation of N.

### Proof: an admissible-source current lemma, including complex coefficients

The previous real-zero reflected-energy result constructed a current for \(q=\psi\sin(\gamma\cdot)\). Here we verify **every hypothesis**, as well as holomorphy and uniform compact-z bounds, for (6). A convenient general source class consists of complex-valued even q with the following properties:

(i) q(0)=0 and \(\int_{\mathbb R}q=0\);

(ii) q extends holomorphically to \(|\operatorname{Im}x|<\pi/4\), and for one fixed strip width \(\sigma=1/6\), its shifted horizontal-line L1 norms are finite, yielding \(|\widehat q(t)|\le C_qe^{-\sigma|t|}\);

(iii) on both real tails, for some finite \(R,k\) depending on q,
\[
|q(x)|\le C_q(1+|x|)^k e^{R|x|}\psi(|x|)
\qquad(|x|\ \hbox{large}),
\tag{10}
\]
with the same bound locally after finitely many real derivatives.

All properties hold for \(q_z\) and all its z derivatives. Uniformly over any compact set of z, one may choose the same exponent R and degree k for a fixed derivative order, with a single finite constant. Indeed \(|\sin(zx)|\le e^{|\operatorname{Im}z||x|}\) on the real axis and \(\Xi(z)\) is bounded on compact sets. The original theta and psi strip estimates control horizontal-line integrals even with these exponential factors. The zero-integral and zero-at-origin identities persist after any number of z derivatives by (7).

For completeness, build the currents rather than appealing merely to a general functional-analytic bound. Let \(d=\log2\), \(a=\log3\), and periodize \(h(s)=\sum_{l\in\mathbb Z}q(s+ld)\). The periodization has zero mean. Solve
\[
j(s-a)-j(s)=h(s),\quad
\widehat j_k=\frac{\widehat q(2\pi k/d)/d}
{e^{-2\pi ika/d}-1}\quad(k\ne0),\quad
\widehat j_0=0.
\tag{11}
\]
These denominators are nonzero by unique factorization. More quantitatively, choosing the integer l nearest \(k\log3/\log2\) gives, for every nonzero integer k,
\[
|e^{-2\pi ika/d}-1|\ge\frac{2}{d\,3^{|k|}}.
\tag{12}
\]
With \(\sigma=1/6\),
\(2\pi\sigma/d>\log3\), so (10)–(12) make the Fourier series for j **and its first derivative** absolutely convergent. They converge uniformly for z on every compact set, and are holomorphic in z there.

Choose once and for all \(b>a+2\) with neither b nor b+a in \(d\mathbb Z\). Define
\[
J_3(x)=j(x)\mathbf1_{[b,b+d)}(x),\quad
q_3(x)=J_3(x-a)-J_3(x),\quad
u=q-q_3,
\]
\[
J_2(x)=\sum_{l\ge1}u(x+ld)
=-\sum_{l\le0}u(x+ld).
\tag{13}
\]
The equality follows from the zero d-periodization of u; all sums converge absolutely at each x. The telescope is exact:
\[
q(x)=J_2(x-d)-J_2(x)+J_3(x-a)-J_3(x).
\tag{14}
\]
Make the reflected antisymmetric currents
\[
K_p(x)=\tfrac12[J_p(x)-J_p(-x-d_p)],
\quad d_2=d,\ d_3=a.
\tag{15}
\]
Because q is even, (14) remains valid with the J's replaced by the K's, and
\(K_p(-x-d_p)=-K_p(x)\). This is **complex-linear**, since no complex conjugation occurs in the symmetrization.

The positive x tails of K2 satisfy
\[
|K_2(x)|\le C_{q}(1+x)^k e^{Rx}\psi(x+d)
\quad(x\gg1).
\tag{16}
\]
This follows directly from (13), which becomes a sum of q(x+ld) over l>=1 on the positive tail and a sum over l<=0 on the negative tail. The complete theta double-exponential ratios make the l=1 term dominate up to a finite bound. K3 has compact positive support. At x=0, the compact support of J3 gives \(J_3(-a)=J_3(0)=0\), while q(0)=0 yields \(J_2(-d)=J_2(0)\); hence
\(K_2(0)=K_2(-d)=0\). Both vanish at least linearly in their respective one-sided endpoint neighborhoods because the lift J2 is C1 there. This verifies the crucial crossing-edge integrability and does not assume the currents are globally C1 at the artificial compact-lift endpoints.

The exact path decomposition of the same-side shifts into reflected edges of powers of 2 and 3 is algebraic. With
\[
I_{p,j}=[(j-2)d_p,(j-1)d_p),\qquad j\ge2,
\]
the currents on **genuine edges** are
\[
c_{p,1}(t)=-K_p(-t),\ 0<t<d_p;
\quad c_{p,2}(t)=-2K_p(t),\ t\in I_{p,2};
\]
\[
c_{p,j}(t)=2[K_p(t-d_p)-K_p(t)],
\quad t\in I_{p,j},\ j\ge3.
\tag{17}
\]
Indeed when \(x\in I_{p,j}\) the intermediate point \(y=jd_p-x\) lies in \([d_p,2d_p]\), and
\(r(x+d_p)-r(x)=[r(y)-r(x)]+[r(x+d_p)-r(y)]\).
The first bracket uses edge p^j and the second p^(j+1). Adjacent contributions collect into (17). The crossing shift uses p^1. This derivation involves all n through the **unchanged** norm (3), while the dual test only needs the two available prime-power families.

The cost is
\[
\mathscr C(q)=
\sum_{p=2,3}\left\{
\int_0^{d_p}\frac{|c_{p,1}(t)|^2}
{\alpha_p\psi(t)\psi(d_p-t)}dt+
\sum_{j\ge2}\int_{I_{p,j}}
\frac{|c_{p,j}(t)|^2}
{\alpha_{p^j}\psi(t)\psi(jd_p-t)}dt
\right\}.
\tag{18}
\]
For j>=2 and t in I_pj, \(jd_p-t\in[d_p,2d_p]\) and
\(\alpha_{p^j}^{-1}\le (p/d_p)e^{t/2}\).
Using \(|u-v|^2\le2(|u|^2+|v|^2)\), the routed portion obeys the explicit bound
\[
\sum_{j\ge2}\int_{I_{p,j}}\frac{|c_{p,j}(t)|^2}
{\alpha_{p^j}\psi(t)\psi(jd_p-t)}dt
\le \frac8{d_pm_p}\int_0^\infty e^{x/2}|K_p(x)|^2
\left[\frac p{\psi(x)}+\frac{p^{3/2}}{\psi(x+d_p)}\right]dx,
\tag{19}
\]
where \(m_p=\min_{[d_p,2d_p]}\psi>0\). Formula (16) implies finiteness of the right side even with the factor \((1+x)^{2k}e^{2Rx}\), because
\(\psi(x)\sim8\pi^3e^{13x/2}e^{-\pi e^{2x}}\), and \(\psi(x+d_p)\) is even smaller. The crossing costs are finite from the first-order endpoint zeros of K2 and the vanishing crossing support of K3. Hence
\[
\boxed{\mathscr C(q)<\infty.}
\tag{20}
\]
The same estimates give a uniform bound for q=q_z with z in a compact set, as well as for every fixed z derivative. Dominated convergence across all edge channels makes the resulting current holomorphic in the edge Hilbert space, locally uniformly in norm.

Finally exact telescoping and (17) yield
\[
\int_{\mathbb R}q(x)r(|x|)dx
=\sum_{p=2,3}\sum_{j\ge1}\int c_{p,j}(t)
[r(t)-r(jd_p-t)]dt,
\tag{21}
\]
where j=1 is integrated on (0,d_p) and j>=2 on I_pj. Cauchy–Schwarz in (3) gives
\[
\boxed{|\mathcal J_z(r)|^2\le\mathscr C(q_z)N[r].}
\tag{22}
\]
This extends to the closure, and the locally norm-holomorphic currents prove (9). The argument uses absolute values throughout, so it applies to genuinely complex z without assuming a hypothetical zero is real. This completes the proof of Theorem 1. □

## 3. Exact jet moments and multiplicity theorem

**Theorem 2 (a single genuine theta jet detects all nonzero zeta zeros in the N-dual family).**
For the real theta jets (5), the exact entire moments are
\[
\boxed{\begin{aligned}
\mathcal J_z(r_0)&=z^3\Xi(z),\\
\mathcal J_z(r_j)&=(-1)^j z^{2j+1}
 (z^2+\tfrac14)\Xi(z),\qquad j\ge1.
\end{aligned}}
\tag{23}
\]
Therefore for every \(z\ne0\),
\[
\boxed{
\Xi(z)=0\quad\Longleftrightarrow\quad
\mathcal J_z(r_0)=0
\quad\Longleftrightarrow\quad
\mathcal J_z(r_j)=0\ \text{for every }j\ge0.}
\tag{24}
\]
In particular, the zero test is an equality between **bona fide bounded functionals in the actual reflected prime energy** and the vectors obtained as limits of the genuine theta jet edge gradients, not a formal Fourier pairing between an unbounded test and an unspecified inverse Laplacian.

### Proof

The exact source identities give, for all complex z,
\[
\int_{\mathbb R}f_j(x)\sin(zx)dx
=(-1)^j z^{2j+1}(z^2+\tfrac14)\Xi(z).
\tag{25}
\]
Also, integration by parts twice or more gives
\[
\int_{\mathbb R}x f_0(x)dx=\Xi(0)/4,\qquad
\int_{\mathbb R}x f_j(x)dx=0\quad(j\ge1).
\tag{26}
\]
Insert r_j=f_j/psi into (8). Equations (25)–(26) yield (23), since for j=0 the subtraction precisely cancels \(z\Xi(z)/4\). The compact cutoff sequence for r_j converges in N-energy by the inherited theta-jet completion theorem. Its pairings with q_z converge to the displayed source integrals by the pointwise theta tail majorants; by continuity they equal the true extended energy-dual values. Because \(\Xi(0)>0\), z=0 is the sole explicit spurious factor in the first formula, and (24) follows. □

**Theorem 3 (all complex zeros and every multiplicity jet).** Let \(z_0\ne0\) be any zero of the entire completed Xi of multiplicity \(r\ge1\), with no assumption that z0 is real. For every \(0\le k<r\) define
\[
\mathcal J_{z_0,k}
=\left.\frac{d^k}{dz^k}\mathcal J_z\right|_{z=z_0}
\in\mathcal H_N^*.
\tag{27}
\]
These are **nonzero** and satisfy
\[
\boxed{
\mathcal J_{z_0,k}(r_j)=0\quad
\text{for every }j\ge0,\quad 0\le k<r.}
\tag{28}
\]
They have the explicit original source representation
\[
\boxed{
\mathcal J_{z_0,k}(r)
=2\int_0^\infty\psi(x)\,
x^k\sin(z_0x+k\pi/2)\,r(x)dx,}
\tag{29}
\]
where the derivative of the compensating term in (6) vanishes exactly through order r−1. This includes every hypothetical off-critical zeta zero and its multiplicity, without postulating one exists.

For any finite collection of distinct zeros \(z_\ell\) modulo \(z\leftrightarrow-z\), all the corresponding \(r_\ell\) functionals \(\mathcal J_{z_\ell,k}\) are linearly independent. Consequently, for every finite set Z of zeros with distinct representatives modulo sign,
\[
\boxed{
\operatorname{codim}_{\mathcal H_N}
\overline{\operatorname{span}}\{\nabla_Nr_j:j\ge0\}
\ge \sum_{z_\ell\in Z}\operatorname{mult}_{z_\ell}\Xi .}
\tag{30}
\]
The lower bound is unconditional for the known on-line zeros, and its logical extension covers any hypothetical off-line zeros as well. Hardy's classical infinitude of distinct on-line zeros already implies infinite codimension. The new information beyond that older result is the **complete complex-zero/multiplicity structure, and an entire energy-dual curve** encoding it.

### Proof

Theorem 1 permits differentiation in the dual norm. Since \(\Xi\) vanishes to order r at z0, all derivatives of \(z\Xi(z)\) through k<r are zero, leaving (29) without compensation. Differentiating the exact moments (23) proves (28). The source function in (29) is nonzero for z0≠0 and all finite k, and psi is strictly positive for x>0. A compact bump on an interval where that complex analytic function is nonzero proves its functional is nonzero.

For independence, suppose a finite linear combination of (29) vanishes on every smooth compact ratio test. Divide its continuous density by positive psi on x>0. The resulting finite exponential polynomial consists of the functions
\(x^k\sin(z_\ell x+k\pi/2)\).
For distinct nonzero \(z_\ell\) modulo sign, these are linearly independent: decompose the sines into \(x^k e^{\pm iz_\ell x}\), with pairwise distinct exponents after identifying ±, and apply constant-coefficient differential annihilators or standard exponential-polynomial independence. Thus the original functionals are independent on the compact core, hence on \(\mathcal H_N\). Their Riesz representatives are independent vectors orthogonal to the theta-jet gradient closure; (30) follows. No completeness of the full family of all such representatives is asserted. □

## 4. Exact bearing on the remaining RH problem

The completely explicit operator-norm entire family (8) satisfies
\[
\forall z\ne0:\quad
\mathcal J_z(r_0)=0\iff
\xi(\tfrac12+iz)=0.
\tag{31}
\]
Every such zero yields genuine, finite **original reflected-prime energy** dual directions that annihilate all the known odd source-null jets; multiplicities give corresponding linearly independent derivatives, even off the critical line. This is a verified new structural interface connecting a full positive prime-power energy to the actual entire completed zeta function, while retaining its completed Gamma factor through Xi and the theta source.

**The missing sign remains missing.** The original polar-inclusive source form is \(A=P-N\). The \(N\)-energy complement is not known to be a negative subspace for A; it may contain vectors with either sign, and P must be retained. Equation (31) supplies a correct spectral/functional language in which to test proposed RH rigidity principles, but its zeros are exactly the unknown zeta zeros and the theorem does not constrain their imaginary parts. The new all-complex current and jet-multiplicity theorem is **not a proof of RH**, not a claim of zero exclusion, and not an improved auxiliary gap.

**Acceptance scope: exact all-complex holomorphic full-prime dual construction, moment identity (23), and multiplicity-resolved full-energy obstruction (30). NO NEW UNCONDITIONAL RH THEOREM PROVED.**

Sources retained: the original complete theta/Weil normalization in ../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md; the odd source, positive psi, reflected energy, two-prime current construction, theta jets, and completion in ../20261013_reflected_prime_energy/REPORT.md; full complex zero/multiplicity source probes in ../20261013_theta_zero_dual_complement/ZETA_ZERO_DUAL_PROBES.md; known fixed-order eigenstate and N-metric limitations in ../20261013_odd_operator_domains/REPORT.md. No original research files are edited.
