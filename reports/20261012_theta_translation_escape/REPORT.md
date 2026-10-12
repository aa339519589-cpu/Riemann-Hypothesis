# True theta translations: sharp Hilbert radius and essential collapse of a prime-edge defect

Date: 2026-10-12. Goal remains a complete unconditional proof of RH. **This note establishes a new exact structural theorem for the unchanged theta/Weil operator, not RH and not a stronger zero-on-line percentage.** It supplies an explicit normalized escape sequence *inside the actual infinite-dimensional critical eigenspace* and identifies the exact Hilbert-space singularity of its theta translation generator.

No numerical zero data, hypothesis about zeta zeros, or modification of the prime/Gamma operator is used. The operator identities employed here are the original fifth-round identities already stated in the repository; they still carry the project's standing independent-review requirement.

## 1. Original Hilbert space and known exact critical vectors

Use the x scale of rounds 04–05:
\[
\Phi(x)=\sum_{n\ge1}
(4\pi^2 n^4 e^{9x/2}-6\pi n^2 e^{5x/2})e^{-\pi n^2e^{2x}},
\quad
\widehat\Phi(z)=\Xi(z).
\]
The Jacobi transformation makes Φ positive and even. Set
\[
h(x)=\cosh(x/2),\qquad m(x)=\sqrt{\Phi(x)/(2h(x))},
\quad p(x)=2\Phi(x)h(x),\quad Uq=\sqrt p\,q .
\]
The original full-even selfadjoint operator is
\[
H=ULU^{-1}-\tfrac12I=M_m(A-S)M_m,
\]
where A is the true Gamma/digamma source multiplier and S is the *complete* prime-power translation sum.

The source identity
\[
(A-S)\Phi=-h,\qquad
(A-S)\Phi^{(2r)}=-4^{-r}h
\quad(r\ge1)
\]
gives the genuine, distinct critical vectors
\[
w_r(x)=\frac{\Phi^{(2r)}(x)-4^{-r}\Phi(x)}{m(x)}
=U\bigl(\Phi^{(2r)}/\Phi-4^{-r}\bigr)(x),
\quad Hw_r=0.
\tag{1}
\]
They lie in the original closed operator domain; see round 5 §4 for its domain verification. The existence of these critical vectors uses no RH assertion.

Let \(\mathcal K=\ker H\) on the **full even** L²(dx) space. We do not assume that the vectors in (1) exhaust \(\mathcal K\).

## 2. A non-polynomial exact family of genuine critical vectors

For a real parameter t define the even theta translation defect
\[
f_t(x)=\Phi(x+t)+\Phi(x-t)-2\cosh(t/2)\Phi(x),\qquad
v_t(x)=f_t(x)/m(x).
\tag{2}
\]
Set
\[
a_*=\tfrac12\log 2 .
\tag{3}
\]

**Theorem A (sharp Hilbert radius and generator).**
For every real \(0<|t|<a_*\), \(v_t\) is a nonzero original full-even L² vector belonging to \(\mathcal K\). The map \(t\mapsto v_t\) extends to an L²-valued holomorphic function throughout the complex disk \(|t|<a_*\), with the norm-convergent expansion
\[
\boxed{
v_t=2\sum_{r\ge1}\frac{t^{2r}}{(2r)!}\,w_r,\qquad
|t|<a_* .}
\tag{4}
\]
The radius of convergence of this Hilbert-valued Taylor series is **exactly** \(a_*\), not merely at least \(a_*\). For real \(|t|\ge a_*\), \(v_t\notin L^2\). Moreover
\[
\boxed{
\lim_{t\uparrow a_*}
(a_*-t)^{5/2}\,\|v_t\|_{L^2(dx)}^2
=\frac3{128}.}
\tag{5}
\]
By evenness in t, the same asymptotic holds for \(t\downarrow-a_*\) with \(a_*-|t|\).

The closed span of the real translation vectors \(\{v_t:0<t<a_*\}\) equals the closed span of all derivative vectors \(\{w_r:r\ge1\}\). In particular, these analytic translations give a non-polynomial, single-parameter generating set for the inherited exact critical subspace.

### 2.1 Exact theta asymptotics, including the denominator

As \(x\to+\infty\), put \(r=e^{2x}\). The genuine *complete* theta sum satisfies
\[
\Phi(x)=4\pi^2e^{9x/2}e^{-\pi r}
(1+O(r^{-1})),\qquad
m(x)=2\pi e^{2x}e^{-\pi r/2}(1+O(r^{-1/2})).
\tag{6}
\]
Indeed the first theta mode has relative correction \(-3/(2\pi r)\), and every \(n\ge2\) contributes an exponentially smaller relative quantity. The factor \(2h(x)=e^{x/2}(1+e^{-x})\) supplies the second formula. Both estimates hold at negative x by true theta parity. In any fixed bounded real translation interval, the same mode estimates are uniform for \(\Phi(x\pm t)\) once \(x\) is sufficiently large.

Let \(c_t=\pi(e^{-2t}-1/2)\). For \(t\uparrow a_*\), restricted to a fixed left neighborhood of \(a_*\), the term \(\Phi(x-t)\) is exponentially larger in r than \(\Phi(x+t)\) and \(\Phi(x)\) on the positive x tail. Therefore, uniformly there,
\[
v_t(x)=2\pi e^{5x/2-9t/2}
e^{-c_t e^{2x}}(1+o_{x\to\infty}(1)).
\tag{7}
\]
The error is uniform over t in that neighborhood: the discarded shifted terms have a fixed positive exponential gap, and (6) has uniform polynomial/exponential remainder. This is where retaining the actual \(m=\sqrt{\Phi/(2h)}\), instead of an arbitrary Gaussian surrogate, matters.

For \(0<t<a_*\), \(c_t>0\), so both tails of (7) are square integrable. At \(t=a_*\), \(c_t=0\), and the positive tail grows like \(2\pi e^{5x/2-9a_*/2}\). For \(t>a_*\), it grows still faster due to \(c_t<0\). Thus \(v_t\notin L^2\) for all positive \(t\ge a_*\); the negative half-line is symmetric. The exceptional parameter \(t=0\) gives the zero vector.

Because \(v_t\) is even in x, (7) and \(dx=dr/(2r)\), together with a split at a fixed large x and the substitution \(u=2c_tr\), yield
\[
\begin{aligned}
\|v_t\|_2^2
&\sim4\pi^2e^{-9t}\int_1^\infty r^{3/2}e^{-2c_tr}\,dr\\
&\sim4\pi^2e^{-9a_*}\Gamma(5/2)(2c_t)^{-5/2}.
\end{aligned}
\]
Since \(c_t\sim\pi(a_*-t)\), \(e^{-9a_*}=2^{-9/2}\) and \(\Gamma(5/2)=3\sqrt\pi/4\), the leading coefficient is
\[
4\pi^2\,2^{-9/2}\frac{3\sqrt\pi}{4}(2\pi)^{-5/2}
=\frac3{128},
\]
proving (5) by a uniform dominated-convergence scaling argument.

### 2.2 Actual Hilbert analyticity and the exact nullspace identity

Φ is holomorphic in \(|\Im z|<\pi/4\) via the genuine theta series. For every fixed \(s<a_*\), the disk \(|t|\le s\) satisfies
\[
\min\{\Re e^{2t},\Re e^{-2t}\}\ge e^{-2s}>\tfrac12.
\tag{8}
\]
For completeness, the elementary inequality \(\Re e^z\ge e^{-|z|}\) holds on \(|z|\le\log2\): put \(z=a+ib\), \(\rho=|z|\). From \(a\ge-\sqrt{\rho^2-b^2}\) follows \(a+\rho\ge b^2/(2\rho)\). Also, \(\tan u\le(4/3)u\) for \(0\le u\le\log2<1/\sqrt2\), by \(\sin u\le u,\ \cos u\ge1-u^2/2\ge3/4\), so \(\log\cos b\ge-2b^2/3\). Because \(\rho\le\log2<3/4\), the two bounds give \(a+\log\cos b\ge-\rho\). Apply this to \(z=\pm2t\).

The strict margin in (8) and (6) dominate \(v_t\), uniformly on compact subdisks, by a multiple of
\[
e^{5|x|/2}\exp[-c_s e^{2|x|}],\qquad c_s>0.
\]
The same is true for any fixed derivative in t, after adjusting its polynomial factor. Hence \(t\mapsto v_t\) is L²-holomorphic on the whole disk.

Differentiate (2) in t at zero. Odd derivatives vanish, while for r>=1,
\[
\partial_t^{2r}v_t|_{t=0}
=2(\Phi^{(2r)}-4^{-r}\Phi)/m=2w_r.
\]
This proves the Hilbert Taylor expansion (4). Each \(w_r\in\ker H\), and the kernel of the original closed selfadjoint H is closed, so **every** \(v_t\) in the disk belongs to \(\ker H\) without an unjustified complex translation of the unbounded source operator. The Fourier transform of the source is the exact identity
\[
\widehat f_t(z)=2[\cos(zt)-\cosh(t/2)]\Xi(z).
\tag{9}
\]
It shows \(v_t\ne0\) for real t !=0, since Ξ(0)>0.

The span equality follows in both directions: (4) puts every \(v_t\) in the closed derivative span, whereas all derivatives \(w_r\) are strong finite-difference limits of \(v_t\) at t=0 and hence lie in the closed translation span. Finally (5) prevents the Hilbert Taylor series from having radius larger than \(a_*\): a holomorphic L² continuation through \(a_*\) would remain locally norm bounded, contrary to (5). Thus its radius is exactly \(a_*\).

## 3. A true prime-power edge has vanishing Rayleigh quotient on normalized exact critical modes

Fix **any** shift \(d>0\) and coefficient \(\alpha>0\), and define its original weighted edge form on full even L²:
\[
\mathcal Q_{d,\alpha}[v]=\alpha\int_{\mathbb R}
m(x)m(x+d)|v(x+d)-v(x)|^2\,dx.
\tag{10}
\]
For actual prime powers use \(d=\log n,\alpha=\Lambda(n)/\sqrt n\); n=2 is already sufficient.

**Theorem B (critical-kernel essential escape).** For every fixed \(d>0,\alpha>0\),
\[
\boxed{\sup_{a_*-\eta<t<a_*}\mathcal Q_{d,\alpha}[v_t]<\infty}
\tag{11}
\]
for any sufficiently small fixed \(\eta>0\), whereas \(\|v_t\|_2^2\sim(3/128)(a_*-t)^{-5/2}\). Hence the unit vectors
\[
u_t=v_t/\|v_t\|_2\in\ker H
\]
satisfy
\[
u_t\rightharpoonup0\text{ in }L^2,\qquad
\boxed{\mathcal Q_{d,\alpha}[u_t]=O_{d,\alpha}((a_*-t)^{5/2})\longrightarrow0.}
\tag{12}
\]

Let \(Q_{d,\alpha}\) be the bounded nonnegative selfadjoint operator represented by (10), and \(P_\mathcal K\) the orthogonal projection onto the actual full-even \(\mathcal K=\ker H\). Then
\[
T_{d,\alpha}=P_\mathcal K Q_{d,\alpha}|_\mathcal K
\]
is bounded, nonnegative and **injective**, but
\[
\boxed{0\in\sigma_{\mathrm{ess}}(T_{d,\alpha}),\qquad
0\notin\sigma_{\mathrm{point}}(T_{d,\alpha}).}\tag{13}
\]
In particular the strictly positive n=2 defect form is **not coercive even when restricted to the exact full infinite-dimensional critical eigenspace**. This is stronger than merely observing it is positive definite on finite-dimensional critical spans.

### Proof of uniform edge control

Write \(f_t=m v_t\). The elementary inequality \(|A-B|^2\le2|A|^2+2|B|^2\) and a change of variables give
\[
\mathcal Q_{d,\alpha}[v_t]
\le2\alpha\int_\mathbb R |f_t(x)|^2
\left[\frac{m(x-d)}{m(x)}+\frac{m(x+d)}{m(x)}\right]dx.
\tag{14}
\]
By (6), uniformly for \(t\in[a_*-\eta,a_*]\) and \(x\to+\infty\),
\[
|f_t(x)|^2\le C_\eta e^{9x}e^{-\pi e^{2x}},
\tag{15}
\]
because the slowest true theta translate has exponential coefficient \(e^{-2a_*}=1/2\). Also, for fixed d>0, as \(x\to+\infty\),
\[
\frac{m(x-d)}{m(x)}
=e^{-2d}\exp\bigl[\tfrac\pi2(1-e^{-2d})e^{2x}\bigr](1+o(1)),
\]
\[
\frac{m(x+d)}{m(x)}
=e^{2d}\exp\bigl[-\tfrac\pi2(e^{2d}-1)e^{2x}\bigr](1+o(1)).
\tag{16}
\]
The first integrand in (14) is therefore dominated for large x by a fixed polynomial in \(e^x\) times
\(\exp[-(\pi/2)(1+e^{-2d})e^{2x}]\); the second decays even faster. The negative tail has the same estimates by parity, with the two ratios interchanged. All compact x ranges are uniformly bounded by continuity and m>0. This proves (11); indeed dominated convergence shows \(\mathcal Q_{d,\alpha}[v_t]\) has a finite endpoint limit.

On each fixed spatial compact interval \(v_t\to v_{a_*}\) in L², but its full norm diverges by (5). Thus \(u_t\to0\) locally in L². Because \(\|u_t\|_2=1\), density of compactly supported test vectors implies \(u_t\rightharpoonup0\). Equation (12) follows from (11) and (5).

The edge form (10) is bounded because m and its translates are bounded. Its kernel is trivial on all L²: zero edge energy implies \(v(x+d)=v(x)\) almost everywhere, and no nonzero periodic L² function exists. Thus \(T_{d,\alpha}\) is injective on \(\mathcal K\).

Finally
\[
\|T_{d,\alpha}u_t\|^2
\le\|T_{d,\alpha}\|\langle u_t,T_{d,\alpha}u_t\rangle
=\|T_{d,\alpha}\|\mathcal Q_{d,\alpha}[u_t]\to0.
\]
The normalized, weakly null approximate eigenvectors are a Weyl singular sequence for the **compressed** bounded selfadjoint operator, establishing (13). This argument does not falsely claim that an individual edge operator preserves \(\ker H\).


### 3.1 Exact edge-rate constant and nonclosed true-source range

The domination used in (14)–(16) is uniform up to the endpoint \(t=a_*\). The limit function \(v_{a_*}=f_{a_*}/m\) is continuous but not L²; nevertheless its **weighted edge integral** (10) is finite for each fixed d and α. By dominated convergence,
\[
q^*_{d,\alpha}:=\lim_{t\uparrow a_*}\mathcal Q_{d,\alpha}[v_t]
=\mathcal Q_{d,\alpha}[v_{a_*}]<\infty.
\]
This number is strictly positive: a zero value would force the continuous \(v_{a_*}\) to be d-periodic, contradicting its unbounded positive-tail asymptotic (7) with \(c_t=0\). Consequently (5) sharpens (12) to the **exact asymptotic**
\[
\boxed{
\lim_{t\uparrow a_*}(a_*-t)^{-5/2}
\mathcal Q_{d,\alpha}[u_t]
=\frac{128}{3}\,q^*_{d,\alpha}\in(0,\infty).}
\tag{17}
\]

There is also a separate, explicit ill-conditioning theorem for the *original* source embedding:
\[
M_m:\mathcal K\longrightarrow L^2(\mathbb R).
\]
It is bounded and injective because \(m>0\) and bounded, but **its range is not closed**. Indeed \(m u_t=f_t/\|v_t\|_2\). The theta translations \(f_t\) depend continuously on real \(t\in[0,a_*]\) in the Schwartz topology, so
\[
\|f_t\|_2\longrightarrow\|f_{a_*}\|_2\in(0,\infty).
\]
Combining with (5),
\[
\boxed{
\lim_{t\uparrow a_*}(a_*-t)^{-5/4}
\|m u_t\|_2
=\sqrt{\frac{128}{3}}\|f_{a_*}\|_2\in(0,\infty).}
\tag{18}
\]
Thus the source map is not bounded below on the **true critical eigenspace**. A bounded injective operator from a Hilbert space has closed range if and only if it is bounded below; (18) proves the failure without assuming any off-axis zeta zeros. In particular any attempted inversion that assumes a uniform constant \(\|v\|_2\le C\|mv\|_2\) on all true zero modes is demonstrably invalid. This is about the genuine H-nullspace, not the different compact Bombieri sampling map.

## 4. Consequences for the actual RH spectral route

1. The exact θ critical eigenspace contains an explicit analytic continuum of non-polynomial modes whose Hilbert norm has the sharp boundary singularity (5). It has concrete shift coordinates rather than only high-order derivative polynomial coordinates.
2. The operator penalizing the true n=2 edge has *strictly positive* energy on each nonzero vector but **zero essential spectral threshold on the true critical subspace**. Finite-dimensional energy minima need not admit an infinite-dimensional positive limit. Equation (13) proves this collapse on an explicit normalized family instead of assuming it.
3. For each fixed finite number of Gamma terms, the omitted positive Gamma form also has a finite unnormalized value on \(v_t\) as \(t\uparrow a_*\): \(m v_t=f_t\) is a uniformly Schwartz family for real t in a compact interval, and the true digamma symbol grows only logarithmically. The same uniformity holds for every *fixed finite* set of prime edges. It does NOT automatically hold for the infinite prime sum or for the separate tail scalar \(\delta_N\|v_t\|^2\); these limits must not be interchanged.
4. The already published finite-rank shorting constructions can use real translations \(v_t\) as concrete critical columns. The radius (3) and singular scaling (5) impose a quantifiable conditioning constraint near the boundary. No finite or infinite selection is asserted to certify the critical half-gap.

The theorem does not rule out a sign-preserving spectral proof. It also does not supply an estimate on the unknown subcritical eigenstates of H, prove \(\mathcal E(q)\ge\tfrac12\mathrm{Var}_\nu(q)\), or exclude any hypothetical off-line zeta zeros.

**Final acceptance:** genuine auxiliary kernel geometry and essential-spectrum theorem for a true weighted prime edge; **NO NEW UNCONDITIONAL RH THEOREM PROVED**.

## Provenance and verification

- Inherited original source identities and critical modes: rounds/05/REPORT-pages-01-05.txt and rounds/05/REPORT-pages-06-10.txt §4.
- Existing diagonal-prime obstruction: reports/20261012_diagonal_prime_threshold_no_go/REPORT.md.
- Existing rank-optimal finite shorting: reports/20261012_threshold_shorted_certificates/REPORT.md.
- The L²-holomorphic translation radius, exact blowup constant and weakly-null essential-spectrum proof are given here analytically. No formal proof-assistant, interval computation or external referee certification is claimed.
