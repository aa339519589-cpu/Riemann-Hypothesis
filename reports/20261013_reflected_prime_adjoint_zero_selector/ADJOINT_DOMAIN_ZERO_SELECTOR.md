# Exact adjoint-domain criterion for every completed-zeta zero in the full reflected-prime Hilbert energy

Date: 2026-10-13. The final objective is an **unconditional complete RH proof**. This note derives an exact operator-domain criterion, with all zero multiplicities, inside the **unchanged all-prime-power reflected theta energy**. For the first time in this repository, the completed-zeta zeros are identified with the *precise parameters at which a nontrivial, explicitly bounded energy-dual probe enters the Hilbert adjoint domain of the actual compact-core source second derivative*. At a zero of order m it generates an actual m-dimensional generalized eigenspace of that adjoint, and its m-th dual derivative fails to belong to the adjoint domain. The exact failure is a rank-one scalar equal to the m-th derivative of z³ Xi(z).

This is **not** a selfadjoint spectral proof of RH: the densely defined source derivative is already known to be nonclosable in this metric, and its Hilbert adjoint is therefore not densely defined. The recently proved theta-projected metric is also nonsymmetric. No zero location follows from the algebraic adjoint eigenvalues.

The new mathematical content is the exact adjoint-domain/eigenchain/multiplicity theorem and its quantitative cutoff blowup, not the earlier nonclosability result or the earlier entire energy-dual construction.

## 1. Exact full prime Hilbert space, differential core and holomorphic dual

Keep the original real, positive, even theta source Phi. Put
\[
\psi(x)=-\Phi'(x)>0\quad(x>0),\qquad
A:=\Xi(0)=\int_{\mathbb R}\Phi(x)dx>0,
\]
\[
\Xi(z)=\int_{\mathbb R}\Phi(x)\cos(zx)dx
=\xi(1/2+iz).
\tag{1}
\]
The true source obeys \(\psi(x)\sim 8\pi^3 e^{13x/2}e^{-\pi e^{2x}}\) as \(x\to+\infty\), and \(\psi(x)=c_\psi x+O(x^3)\) at zero.

Use **all** genuine von Mangoldt labels \(n\ge2\):
\[
d_n=\log n,\quad\alpha_n=\frac{\Lambda(n)}{\sqrt n},\qquad
N[r]=\sum_{n\ge2}\alpha_n\int_0^{d_n}
\psi(x)\psi(d_n-x)|r(x)-r(d_n-x)|^2dx.
\tag{2}
\]
Let \(\mathcal C\) be the complex smooth compactly supported ratio core on \(x\ge0\) with smooth even extension. Let \(v(r)=\nabla_Nr\) denote the complete direct-sum edge gradient, and
\[
K_N=\overline{v(\mathcal C)}^{\,N}.
\tag{3}
\]
The core gradient is injective: if \(N[r]=0\) and \(r\in\mathcal C\), choose a genuine prime power \(n=2^j\) with \(d_n\) exceeding twice the support radius. Its reflection sends the support outside itself, and positivity of its edge weight forces \(r=0\). Consequently
\[
Z_0:v(\mathcal C)\longrightarrow K_N,\quad
Z_0v(r)=v(\mathcal B_\psi r),\quad
\mathcal B_\psi r:=\frac{(\psi r)''}{\psi}
\tag{4}
\]
is a well-defined, densely defined complex-linear operator. The numerator is smooth odd through zero, so \(\mathcal B_\psi r\in\mathcal C\) with no boundary-condition substitution.

The recent [entire reflected-prime zero dual theorem](../20261013_complex_reflected_prime_zero_dual/ENTIRE_REFLECTED_PRIME_ZERO_DUAL.md) proves that, for **every** \(z\in\mathbb C\), the explicitly renormalized functional
\[
\begin{aligned}
q_z(x)&=\psi(x)\left[
\sin(zx)-\frac{z\Xi(z)}{A}\,x\right],\\
\mathcal J_z(v(r))&=\int_{\mathbb R}q_z(x)r(|x|)dx
\end{aligned}
\tag{5}
\]
extends boundedly to \(K_N\), and \(z\mapsto\mathcal J_z\) is entire in the Banach-dual operator norm. Its continuity uses honest full-prime \(N\), with an explicit finite-energy current supported on actual powers of primes 2 and 3. The functional is **complex-linear in its argument**, and the Riesz vector is anti-holomorphic in the parameter; no holomorphic Riesz vector is assumed.

The theta integral identities are exact for all complex z:
\[
\int_{\mathbb R}\psi(x)\sin(zx)dx=z\Xi(z),\qquad
\int_{\mathbb R}x\psi(x)dx=A.
\tag{6}
\]
Thus \(q_z\) has zero integral, \(q_z(0)=0\), and \(\mathcal J_z\) does descend to the edge-gradient Hilbert space. For every \(z\ne0\), \(\mathcal J_z\ne0\): the coefficient of \(x^3\) in the bracket of (5) is \(-z^3/6\).

Fix throughout \(\langle\cdot,\cdot\rangle_{K_N}\) **conjugate-linear in the first argument**. Write \(h_z^{[k]}\in K_N\) for the unique Riesz vectors
\[
\mathcal J_z^{(k)}(u)=\langle h_z^{[k]},u\rangle_{K_N},
\qquad h_z=h_z^{[0]}.
\tag{7}
\]
Every \(h_z^{[k]}\) exists because of the proven operator-norm entire dual curve.

## 2. Exact full-line integration identity and the rank-one defect

Define a linear moment on the **compact ratio core**, not on the quotient,
\[
X(r):=\int_{\mathbb R}x\psi(x)r(|x|)dx .
\tag{8}
\]
Let \(g=\psi r(|x|)\), a smooth compactly supported odd source. The source \((\psi\mathcal B_\psi r)(x)=g''(x)\) is again compact and odd. Two integrations by parts, with no boundary term, give
\[
\begin{aligned}
\mathcal J_z(v(\mathcal B_\psi r))
&=\int_{\mathbb R}\left[\sin(zx)-\frac{z\Xi(z)}A x\right]g''(x)dx\\
&=-z^2\int_{\mathbb R}g(x)\sin(zx)dx,
\end{aligned}
\tag{9}
\]
since \((\sin(zx))''=-z^2\sin(zx)\) and \(x''=0\).
Substitute the **exact** definition (5), without extending \(X\) beyond the core:
\[
\boxed{
\mathcal J_z(Z_0v(r))+z^2\mathcal J_z(v(r))
=-\frac{z^3\Xi(z)}{A}\,X(r)
\quad(r\in\mathcal C;\ z\in\mathbb C).}
\tag{10}
\]
This is the original \(N\)-energy dual, not a finite-rank prime approximation. It holds as an entire scalar identity in z and requires **no information about zeta zeros**.

There is a crucial distinction: \(\mathcal J_z\) is bounded in \(K_N^*\), but the unrenormalized moment \(X\) is not. The latter cannot be silently promoted to a bounded rank-one perturbation of an operator on \(K_N\).

## 3. The complete-prime cutoff shows the defect is genuinely unbounded

Choose real even \(\chi_R\in C_c^\infty(\mathbb R)\), equal to one on \(|x|\le R\), zero on \(|x|\ge R+1\), with \(0\le\chi_R\le1\) and uniformly bounded first two derivatives. Its positive restriction lies in \(\mathcal C\).

The **full** prime incidence bound in [reflected prime energy, (4)–(5)](../20261013_reflected_prime_energy/REPORT.md) gives
\[
N[\chi_R]=N[1-\chi_R]
\le4\int_R^\infty\psi(x)L(x)dx,\quad
L(x):=\sum_{n>e^x}\alpha_n\psi(d_n-x)
\le C(1+x)e^{x/2}.
\tag{11}
\]
Here \(N[1-\chi_R]\) is defined by the literal convergent edge integral; \(1-\chi_R\) need not belong to the compact core. For \(R\) large, the true first theta term yields
\[
\psi(x)L(x)\le C(1+x)e^{7x}e^{-\pi e^{2x}} .
\tag{12}
\]
Use \(e^{2(R+y)}\ge e^{2R}(1+2y)\) and integrate the resulting exponential majorant in \(y\ge0\). Explicitly, with \(a_R=2\pi e^{2R}-7>0\),
\[
\int_R^\infty (1+x)e^{7x}e^{-\pi e^{2x}}dx
\le e^{7R-\pi e^{2R}}
\left(\frac{1+R}{a_R}+\frac1{a_R^2}\right).
\]
Therefore for all sufficiently large R,
\[
\boxed{\|v(\chi_R)\|_{K_N}^2=N[\chi_R]
\le C(1+R)e^{5R}e^{-\pi e^{2R}}\longrightarrow0.}
\tag{13}
\]
Every prime power is included through L; no edge has been set to zero.

Yet the exact source integral converges by dominated convergence:
\[
\boxed{X(\chi_R)\longrightarrow
\int_{\mathbb R}x\psi(x)dx=A\ne0.}\tag{14}
\]
Thus \(X\) is **unbounded** with respect to the true \(K_N\)-norm, and it has no continuous extension to \(K_N\).

Moreover \(\mathcal J_z(v(\chi_R))\to0\) for every z by the boundedness already proved in (5). Consequently (10) gives
\[
\boxed{\lim_{R\to\infty}
\mathcal J_z(Z_0v(\chi_R))=-z^3\Xi(z).}
\tag{15}
\]
For each fixed \(z\ne0\) with \(\Xi(z)\ne0\), (13) and (15) even yield the explicit large-R blowup
\[
\boxed{
\frac{|\mathcal J_z(Z_0v(\chi_R))|}
{\|v(\chi_R)\|_{K_N}}
\ge c_z(1+R)^{-1/2}
\exp\!\left[\frac\pi2e^{2R}-\frac52R\right]
\longrightarrow\infty.}
\tag{16}
\]
This double-exponential lower bound is a **nonzero-dual-on-vanishing-input** assertion, not a claim that \(Z_0\) has a spectral gap. It applies equally to the actual unmodified all-prime form.

A convenient exact arithmetic test is \(z=i/2\). Since \(\Xi(i/2)=\xi(0)=1/2\), (15) gives \(\lim_R\mathcal J_{i/2}(Z_0v(\chi_R))=i/16\). At a genuine zero, the same limit is zero.

## 4. Theorem A: exact zeta-zero criterion as a Hilbert-adjoint **domain** condition

Let \(Z_0^*\) denote the Hilbert adjoint of the densely defined operator (4). Although \(Z_0\) is nonclosable, its adjoint is well-defined and closed; its domain is not dense. For any \(h\in K_N\),
\[
h\in\operatorname{Dom}Z_0^*
\quad\Longleftrightarrow\quad
u\longmapsto\langle h,Z_0u\rangle
\text{ is bounded in }\|u\|_{K_N}
\text{ on }D(Z_0).
\tag{17}
\]
No graph closure, imposed boundary condition or selfadjoint extension is introduced here.

**Theorem A (all complex strip and all complex-plane parameters).** For every nonzero \(z\in\mathbb C\),
\[
\boxed{\Xi(z)=0\quad\Longleftrightarrow\quad
0\ne h_z\in\operatorname{Dom}Z_0^*,}
\tag{18}
\]
and at every such zero,
\[
\boxed{Z_0^*h_z=-\overline{z}^{\,2}h_z.}\tag{19}
\]

**Proof.** Equation (10) and the already-proved norm-boundedness of \(\mathcal J_z\) show that \(u\mapsto\mathcal J_z(Z_0u)\) is bounded precisely when its scalar coefficient \(z^3\Xi(z)/A\) multiplying the unbounded \(X\) vanishes. For \(z\ne0\) this is equivalent to \(\Xi(z)=0\). Riesz representation (7) and (17) identify this boundedness with \(h_z\in\operatorname{Dom}Z_0^*\). At a zero, (10) reduces on the entire dense core to \(\mathcal J_z(Z_0u)=-z^2\mathcal J_z(u)\). Since the inner product is conjugate-linear in the first slot, (19) follows with the complex conjugate on z. The functional is nonzero for z≠0 by the cubic coefficient noted after (6). □

The exceptional point z=0 is explicitly excluded: \(\Xi(0)>0\) but \(\mathcal J_0=0\), so \(h_0=0\) is trivially in every operator domain and cannot detect a zero. This is a *genuine* operator-domain characterization of completed-zeta zeros, not an eigenvalue claim for any selfadjoint Hilbert–Pólya operator.

## 5. Theorem B: zero multiplicity is exactly the length of an adjoint-domain jet

For \(k\ge0\), put \(\mathcal J_z^{(-1)}=\mathcal J_z^{(-2)}=0\). Differentiate (10) k times in z, which is legal **in the dual norm** for the \(\mathcal J\) terms. The exact identity on the compact core is
\[
\boxed{\begin{aligned}
&\mathcal J_z^{(k)}(Z_0v(r))
+z^2\mathcal J_z^{(k)}(v(r))
+2kz\mathcal J_z^{(k-1)}(v(r))\\
&\quad+k(k-1)\mathcal J_z^{(k-2)}(v(r))
=-\frac{[z^3\Xi(z)]^{(k)}}A X(r).
\end{aligned}}\tag{20}
\]
Here \([z^3\Xi(z)]^{(k)}\) denotes the ordinary k-th complex derivative of the entire scalar product, not a derivative of an undefined operator.

**Theorem B (exact first exit from the adjoint domain).** For every \(z\in\mathbb C\) and \(k\ge0\),
\[
\boxed{
h_z^{[k]}\in\operatorname{Dom}Z_0^*
\quad\Longleftrightarrow\quad
[z^3\Xi(z)]^{(k)}=0.}\tag{21}
\]
Let \(z_0\ne0\) be a zero of \(\Xi\) of *exact multiplicity* \(m\ge1\). Then
\[
\boxed{
h_{z_0}^{[0]},h_{z_0}^{[1]},\ldots,h_{z_0}^{[m-1]}
\in\operatorname{Dom}Z_0^*,
\qquad
h_{z_0}^{[m]}\notin\operatorname{Dom}Z_0^*.}\tag{22}
\]
These m vectors are linearly independent, and their m-dimensional span is invariant under the actual adjoint:
\[
\boxed{
Z_0^*h_{z_0}^{[k]}=
-\overline{z_0}^{\,2}h_{z_0}^{[k]}
-2k\overline{z_0}\,h_{z_0}^{[k-1]}
-k(k-1)h_{z_0}^{[k-2]},
\quad0\le k<m.}\tag{23}
\]
The nilpotent part is a **single Jordan block of length m**, since
\[
(Z_0^*+\overline{z_0}^{\,2}I)^{m-1}h_{z_0}^{[m-1]}
=(-2\overline{z_0})^{m-1}(m-1)!\,h_{z_0}^{[0]}\ne0
\]
and the m-th power vanishes on this invariant finite-dimensional span.

**Proof.** In (20), every term except \(\mathcal J_z^{(k)}\circ Z_0\) and the multiple of \(X\) is bounded on \(K_N\). The unboundedness (13)–(14) therefore makes its composition bounded exactly when the indicated scalar derivative vanishes. This proves (21). If the zero order is m, the product \(z^3\Xi(z)\) has the same order m at \(z_0\ne0\); its m-th derivative equals \(z_0^3\Xi^{(m)}(z_0)\ne0\). Equations (22) and (23) follow from (21), (20) and the conjugate-linearity of the first Hilbert slot.

For k<m, all derivatives through order k of \(z\Xi(z)\) vanish at \(z_0\). Hence the source of \(\mathcal J_{z_0}^{(k)}\) is exactly \(\psi(x)x^k\sin(z_0x+k\pi/2)\), with no hidden subtraction. The functions \(x^k\sin(z_0x+k\pi/2)\), \(0\le k<m\), are linearly independent on every real open interval when \(z_0\ne0\): express them as exponential polynomials with distinct exponents \(\pm iz_0\). Their functionals on compact core ratios, and therefore their Riesz vectors in \(K_N\), are independent. This proves the nilpotent/Jordan assertion. □

At k=m the failure is quantitative, not just formal:
\[
\mathcal J_{z_0}^{(m)}(Z_0v(\chi_R))
\longrightarrow-z_0^3\Xi^{(m)}(z_0)\ne0
\qquad\text{while }\|v(\chi_R)\|_{K_N}\to0.
\tag{24}
\]
A repeated zero thus produces exactly m bounded dual generalized eigenvectors and a **first unbounded dual derivative at order m**.

## 6. Adversarial cross-check with the previously known nonclosability mechanism

The odd source report already proved
\[
\mathcal B_\psi1=\psi''/\psi=\frac14-r_0,\quad
r_0=\frac{\Phi'''-\frac14\Phi'}{\psi},\quad
Z_0v(\chi_R)\longrightarrow-v(r_0)\ne0.
\tag{25}
\]
The entire zero-dual report independently proved
\[
\mathcal J_z(v(r_0))=z^3\Xi(z).
\tag{26}
\]
Pair (25) with its bounded Riesz functional: the limit is \(-z^3\Xi(z)\), exactly (15). Thus the rank-one differential integration by parts, the theta-jet Fourier moment, and the full-prime cutoff graph limit independently agree on the **same sign, factor, and power z³**.

The known theta jets satisfy \(\mathcal B_\psi r_j=r_{j+1}\) **exactly**, because \(f_{j+1}=f_j''\); thus the derivative preserves their algebraic span. For a zero of order m, the functional jets (22) annihilate that span and its closure by continuity. Consequently (23) also gives **weak left generalized eigenchains** of the theta-projected core *relation*, without assuming that the projected graph defines a single-valued operator. This is consistent with [the newer full-projection nonsymmetry theorem](../20261013_projected_metric_obstruction/REPORT.md): no selfadjoint or symmetric projected generator has been constructed.

**Precisely why RH remains open:** the location of \(-\overline z^{\,2}\) cannot be constrained by the spectral theorem because \(Z_0\) is nonclosable. Its adjoint has a nondense domain, and the projected relation is nonsymmetric even after removing the known theta jets. The chain construction identifies Xi zeros in a genuine Hilbert-adjoint domain but does not establish any positivity or symmetry of the actual Weil operator \(H\) on the unknown complement. For a hypothetical off-line z, a nonreal adjoint eigenvalue is mathematically allowed.

**Acceptance: exact all-complex zero-to-adjoint-domain criterion, multiplicity Jordan-chain theorem, and quantitative cutoff failure mechanism, conditional on the stated and previously audited entire two-prime energy-dual theorem. NO NEW UNCONDITIONAL RH THEOREM PROVED.** No literature priority or independent third-party review is claimed.
