# Prime-logarithm recurrence forces unbounded pure-edge evaluation norms, while the full Gamma energy diverges

Date: 2026-10-12. Original problem: an unconditional proof that every nontrivial zero of \(\zeta\) has real part \(1/2\). This note proves a **new full-prime obstruction and an exact compensation mechanism** for the original operator: the dual norms of source evaluation with respect to the *pure* prime-edge energy have unbounded limsup at high real frequencies. The witnesses can be chosen in the original operator domain, with the ground moment exactly removed. Simultaneously, their **complete Gamma energy diverges** at the explicitly identified logarithmic rate. Thus prime resonance cannot be mistaken for an actual negative-H eigenstate.

This theorem refines the positive *liminf* of the pure-edge dual norm in PURE_PRIME_EDGE_EVALUATIONS.md, §7, to an infinite *limsup*. It does not use finite-prime replacements: the full sum is dominated before passing to the limit. It neither locates any zeta zero nor changes the certified existing gap. **NO NEW UNCONDITIONAL RH THEOREM PROVED.**

## 1. Actual original objects

Work on the real even subspace of \(L^2(\mathbb R,dx)\), with the full theta source and every prime power:
\[
m(x)^2=\frac{\Phi(x)}{2\cosh(x/2)},\qquad
g_0(x)=2\cosh(x/2)m(x),\qquad
H=B-V,
\]
\[
B[v]=\frac1{2\pi}\int_{\mathbb R}b(t)|\widehat{mv}(t)|^2\,dt,\quad
b(t)=\operatorname{Re}\psi(\tfrac14+it/2)-\psi(\tfrac14)\ge0,
\]
\[
V=C_0M_{m^2}+
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
M_m(\tau_{\log n}+\tau_{-\log n})M_m.
\]
The complete positive prime-edge form is
\[
\boxed{e[v]=
\sum_{n\ge2}\alpha_n\int_{\mathbb R}
m(x)m(x+d_n)|v(x+d_n)-v(x)|^2dx,\quad
\alpha_n=\Lambda(n)/\sqrt n,\ d_n=\log n.}\tag{1}
\]
The original form and its domain are established in ORIGINAL_FORM_FOUNDATION.md. The explicit theta estimate from that proof is
\[
m(x)^2\le A_*e^{4|x|-\pi e^{2|x|}},\qquad
A_*=4\pi^2\frac{125}{121}.
\tag{2}
\]
Both \(m,g_0\) are even, strictly positive, rapidly decreasing and in \(L^1\cap L^2\cap L^\infty\); \(m\) has all real derivatives in \(L^2\). The normalized \(g_0\in\operatorname{Dom}H\) satisfies \(Hg_0=-g_0/2\).

For \(\gamma\in\mathbb R\), set
\[
F_v(\gamma)=\int_{\mathbb R}m(x)v(x)e^{-i\gamma x}\,dx
\]
and define the exact ground-perpendicular pure-edge dual norm
\[
d_e(\gamma)=\sup\{|F_v(\gamma)|^2:
 v\in L^2_{\rm even}(\mathbb R),\ \langle g_0,v\rangle=0,\ e[v]\le1\}.
\tag{3}
\]
The current construction in PURE_PRIME_EDGE_EVALUATIONS.md proves \(d_e(\gamma)<\infty\) for every **fixed** real \(\gamma\); its explicit upper bound grows with \(|\gamma|\). Here we prove that nonuniformity is intrinsic.

## 2. The complete edge has summable mass

**Lemma 1.** Put \(W_n=\int_{\mathbb R}m(x)m(x+\log n)\,dx\). For every integer \(n\ge2\),
\[
\boxed{
0<W_n\le A_*e^{-\pi n}
\left(n^2\log n+\frac n\pi+\frac1{\pi^2}\right).
}\tag{4}
\]
In particular,
\[
\boxed{T_*:=\sum_{n\ge2}\alpha_nW_n<\infty.}\tag{5}
\]

**Proof.** For \(d=\log n\), write \(u(x)=e^{|x|+|x+d|}\). AM–GM applied to the two exponents in (2) gives
\[
m(x)m(x+d)\le A_*u(x)^2e^{-\pi u(x)}.
\tag{6}
\]
On \([-d,0]\), \(u=n\), contributing at most \(A_*n^2e^{-\pi n}d\). On \(x\ge0\), \(u=ne^{2x}\); the substitution \(y=e^{2x}\) gives
\[
\int_0^\infty m(x)m(x+d)\,dx
\le\frac{A_*n^2}{2}\int_1^\infty ye^{-\pi ny}dy
=\frac{A_*}2e^{-\pi n}\left(\frac n\pi+\frac1{\pi^2}\right).
\]
The region \(x\le-d\) has the same upper bound. Summing the three regions proves (4). Since \(\Lambda(n)\le\log n\), the summand in (5) is bounded by a polynomial-logarithmic factor times \(e^{-\pi n}\). Hence (5), with **every prime power retained**. □

## 3. Simultaneous near-resonance for all prime powers

**Lemma 2.** There are positive **integers** \(\gamma_j\to+\infty\) such that
\[
\boxed{e^{i\gamma_j\log n}\longrightarrow1
\quad\text{for every fixed integer }n\ge2.}\tag{7}
\]
Consequently the genuinely all-prime positive trigonometric series
\[
T(\gamma)=\sum_{n\ge2}\alpha_nW_n
|e^{i\gamma\log n}-1|^2
\tag{8}
\]
satisfies \(T(\gamma_j)\to0\).

**Proof.** For any finite list of real frequencies \(\theta_1,\dots,\theta_k\), the pigeonhole form of simultaneous Dirichlet approximation supplies positive integers q with
\(\max_r\|q\theta_r\|_{\mathbb R/\mathbb Z}\) arbitrarily small. Such q can be chosen arbitrarily large. Indeed if a sequence of improving approximants were bounded, a fixed positive q would be an exact common period, and its unbounded integer multiples would be exact periods instead. Apply this to
\(\theta_p=(\log p)/(2\pi)\) for the finitely many primes \(p\le j\); choose \(\gamma_j>j\) such that
\(\max_{p\le j}|e^{i\gamma_j\log p}-1|<j^{-2}\).
Every fixed integer n has finitely many prime factors, so its phase in (7) tends to one by multiplicativity. The summand in (8) is bounded by \(4\alpha_nW_n\), which is summable by Lemma 1. Dominated convergence on the counting measure proves \(T(\gamma_j)\to0\). There is no assumption about rational independence beyond the ordinary finite-dimensional pigeonhole argument. □

## 4. Genuine original-domain witnesses

Fix a real even \(\chi\in C_c^\infty(\mathbb R)\) such that \(0\le\chi\le1\), \(\chi=1\) on \([-1,1]\), and \(\chi=0\) outside \([-2,2]\). Let \(\chi_R(x)=\chi(x/R)\). Choose any sequence \(R_j\to\infty\), say \(R_j=j\), and put
\[
z_j(x)=\chi_{R_j}(x)\cos(\gamma_jx),\qquad
\beta_j=\frac{\langle g_0,z_j\rangle}{\|g_0\|_2^2},\qquad
\boxed{v_j=z_j-\beta_jg_0.}\tag{9}
\]

**Theorem 3 (unbounded dual norms, all primes paid).** The vectors \(v_j\) are real even members of \(\operatorname{Dom}H\cap g_0^\perp\) and obey
\[
\boxed{
e[v_j]\longrightarrow0,\qquad
F_{v_j}(\gamma_j)\longrightarrow
\frac12\int_{\mathbb R}m(x)\,dx>0.}\tag{10}
\]
Therefore
\[
\boxed{\limsup_{\gamma\to+\infty}d_e(\gamma)=+\infty.}\tag{11}
\]
In particular no fixed finite constant \(C\) can satisfy
\(|F_v(\gamma)|^2\le C e[v]\) for **all** ground-perpendicular even v and **all** real \(\gamma\), despite the valid per-frequency current construction.

**Proof.** For every n and every x, inserting \(z=\chi_R\cos(\gamma\cdot)\) and splitting the difference gives
\[
|z(x+d_n)-z(x)|^2
\le2|e^{i\gamma d_n}-1|^2+
 2|\chi_R(x+d_n)-\chi_R(x)|^2 .
\tag{12}
\]
Define the true (not truncated-prime) spatial-cutoff error
\[
J(R)=\sum_{n\ge2}\alpha_n\int_{\mathbb R}
m(x)m(x+d_n)|\chi_R(x+d_n)-\chi_R(x)|^2dx.
\]
For every fixed n,x both cutoff values converge to one as \(R\to\infty\). Their difference has absolute value at most one, and the total dominating edge mass is \(T_*<\infty\). Dominated convergence on the exact counting-times-Lebesgue measure gives
\[
J(R)\to0,\qquad
e[z_j]\le2T(\gamma_j)+2J(R_j)\to0.
\tag{13}
\]

Since \(g_0\in L^1\), \(\chi_{R_j}\to1\) in \(L^1(g_0\,dx)\), and \(\gamma_j\to\infty\), the Riemann–Lebesgue lemma gives
\[
\beta_j\to0.
\tag{14}
\]
The full form e is nonnegative and \(e[g_0]<\infty\), so the triangle inequality for its square root yields
\[
\sqrt{e[v_j]}\le\sqrt{e[z_j]}+
|\beta_j|\sqrt{e[g_0]}\to0.
\tag{15}
\]
Both \(z_j\in C_c^\infty\) and \(g_0\in\operatorname{Dom}H\). For \(z_j\), \(mz_j\in C_c^\infty\), hence \(b(D)(mz_j)\in L^2\) because \(b(t)=O(\log(2+|t|))\); the original operator-form realization therefore gives \(z_j\in\operatorname{Dom}B=\operatorname{Dom}H\). Orthogonality in (9) is exact.

For the source evaluation, evenness gives
\[
F_{z_j}(\gamma_j)
=\int m\chi_{R_j}\cos^2(\gamma_jx)dx
=\frac12\int m\chi_{R_j}dx+
\frac12\int m\chi_{R_j}\cos(2\gamma_jx)dx
\longrightarrow\frac12\int m .
\tag{16}
\]
The second integral tends to zero by
\(\|m\chi_{R_j}-m\|_1\to0\) and Riemann–Lebesgue. The correction
\(|\beta_jF_{g_0}(\gamma_j)|\le|\beta_j|\int mg_0\to0\).
This proves (10).

Every nonzero v with e[v]=0 would have \(v(x+\log2)=v(x)\) almost everywhere, by the strictly positive n=2 weight. A nonzero \(L^2(\mathbb R)\) function cannot be periodic. Thus e[v_j]>0 for all sufficiently large j because its source evaluation tends to a positive number. Scaling v_j by \(e[v_j]^{-1/2}\) is an admissible competitor in (3), giving
\[
d_e(\gamma_j)\ge |F_{v_j}(\gamma_j)|^2/e[v_j]\to+\infty.
\]
The whole-prime limit preceded scaling, so no omitted-power or small-penalty inference is hidden. □

## 5. Full Gamma resolves the apparent near-zero edge energy

The preceding vectors are **not** candidate low-energy states of H. The original unbounded Gamma part sees their rapid oscillations even when all tested prime phases are close to one.

**Theorem 4 (sharp logarithmic Gamma cost).** For the *same* original-domain vectors \(v_j\),
\[
\boxed{
\lim_{j\to\infty}\frac{B[v_j]}{\log\gamma_j}
=\lim_{j\to\infty}\frac{\langle v_j,Hv_j\rangle}{\log\gamma_j}
=\frac12\|m\|_2^2>0.
}\tag{17}
\]
In particular \(H[v_j]\to+\infty\), while \(e[v_j]\to0\).

**Proof.** Write \(a_R=m\chi_R\) and \(f_{R,\gamma}=a_R\cos(\gamma x)\). The complete theta source gives
\[
\|a_R-m\|_2\to0,\qquad
\sup_{R\ge1}(\|a_R\|_2+\|a_R'\|_2)<\infty.
\tag{18}
\]
For the Fourier transform with Plancherel measure \(dt/(2\pi)\),
\[
\widehat{f_{R,\gamma}}(t)=
\tfrac12[\widehat a_R(t-\gamma)+\widehat a_R(t+\gamma)].
\]
The bounded derivative norm implies that its Fourier \(L^2\) mass on
\(|t|<\gamma/2\) is \(O(\gamma^{-2})\), uniformly in R. It also gives
\[
\int_{|t|>2\gamma}
b(t)|\widehat f_{R,\gamma}(t)|^2\frac{dt}{2\pi}
=O(\log\gamma/\gamma^2).
\tag{19}
\]
For the latter bound, each shifted source frequency \(s=t\pm\gamma\) has
\(|s|\ge|t|/2\ge\gamma\), while \(b(t)\ll\log(2+|s|)\) and
\(\sup_{|s|\ge\gamma}\log(2+3|s|)/s^2\ll\log\gamma/\gamma^2\); apply Parseval to \(a_R'\). On the remaining band \(\gamma/2\le|t|\le2\gamma\), the exact complete Gamma symbol obeys
\[
b(t)=\log\gamma+O(1)
\tag{20}
\]
uniformly (the classical digamma asymptotic), and \(b\ge0\) everywhere. Hence
\[
B[z_j]=b[mz_j]=(\log\gamma_j)\|mz_j\|_2^2+o(\log\gamma_j).
\]
But
\(\|mz_j\|_2^2=\int a_{R_j}^2\cos^2(\gamma_jx)dx
\to\frac12\|m\|_2^2\):
use \(a_{R_j}^2\to m^2\) in \(L^1\) and Riemann–Lebesgue. Thus \(B[z_j]/\log\gamma_j\to\|m\|_2^2/2\).

The ground correction does not change the leading Gamma energy:
\[
|\sqrt{B[v_j]}-\sqrt{B[z_j]}|
\le|\beta_j|\sqrt{B[g_0]}\to0
\]
since \(B[g_0]<\infty\) and \(\beta_j\to0\).

Finally, the complete signed bounded potential has uniformly bounded expectation on v_j. Indeed \(\sup_j\|v_j\|_\infty<\infty\), since \(|z_j|\le1\), \(\beta_j\to0\), \(g_0\in L^\infty\). The scalar \(m^2\) is in \(L^1\), and the absolute all-prime shift cost is bounded by
\[
2\|v_j\|_\infty^2\sum_{n\ge2}\alpha_nW_n
=2\|v_j\|_\infty^2 T_*.
\tag{21}
\]
Therefore \(|\langle v_j,Vv_j\rangle|=O(1)\) independent of j, and (17) follows from \(H=B-V\). No high-frequency deletion of Gamma or signed primes is used. □

## 6. Exact impact on the unconditional RH program

This proves a specific **failure mechanism** for a tempting completion of the pure-prime current argument: a uniform-in-height evaluation dual bound cannot be true on the full original ground-perpendicular space. The instability already occurs for smooth genuine domain vectors, and all omitted prime powers have been rigorously paid.

The same witnesses establish why this does not provide an RH counterexample: the full unbounded Gamma multiplier contributes the positive diverging term \(\frac12\|m\|_2^2\log\gamma_j\), so the original H-form is eventually strictly positive. The near-zero *pure-prime* edge alone has no spectral sign implication for H. A full proof still requires control of the actual negative/critical spectral complement and exclusion of every off-line zeta zero.

**Acceptance: unbounded limsup of true pure-edge evaluation norm and sharp simultaneous full-Gamma compensation; NO NEW UNCONDITIONAL RH THEOREM PROVED.**

Dependencies: ORIGINAL_FORM_FOUNDATION.md (exact real-even H domain, m envelope, complete prime edge); PURE_PRIME_EDGE_EVALUATIONS.md (fixed-height dual bound and its finite positive high-height liminf); EFFECTIVE_GAMMA_EIGENSTATE_TAIL.md (true Theta Sobolev and digamma growth). All new statements and proofs are on this page. No outside review or formal verification is claimed.
