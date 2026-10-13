# Exact high-frequency band core, constructive theta-ground superoscillation, and fixed-rank sign obstruction

Date: 2026-10-13. **Ultimate target: an unconditional proof that every nontrivial zero of \(\zeta\) has real part \(1/2\).** This note works entirely with the original full even theta / complete Gamma / every-prime-power operator. It supplies a new, exact **form-core theorem for *any* arbitrarily narrow real frequency interval**, an explicit high-frequency finite-cosine construction converging in the *original maximal form norm* to the known negative ground vector, and a **uniform positive high-carrier theorem for all fixed-size clusters of complex frequencies and derivative jets, without any separation assumption**. Together these prove an actual rank-divergence mechanism and a countable one-band Gram criterion exactly equivalent to the missing RH sign.

**NO NEW UNCONDITIONAL RH THEOREM PROVED.** The explicitly negative high-frequency constructions approximate the known ground vector and are not mean-zero counterexamples. No global sign on its orthogonal complement is obtained. Novelty here means a new result relative to the files reviewed in this repository, not a literature-priority assertion.

## 1. Actual full operator, exact domain and zero selector

On the original even Hilbert space \(\mathcal H=L^2_{\rm even}(\mathbb R,dx;\mathbb C)\), retain
\[
\Phi(x)=\sum_{n\ge1}
(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})e^{-\pi n^2e^{2x}},
\quad h(x)=\cosh(x/2),\quad m^2=\frac{\Phi}{2h}.
\tag{1}
\]
The modular theta relation makes \(\Phi,m\) even, smooth, strictly positive, and superexponentially decreasing with their derivatives on both real tails. Put
\[
e_0=2mh,\quad \|e_0\|_2=1,\quad He_0=-\tfrac12e_0,
\quad H=M_m b(D)M_m-V,
\tag{2}
\]
\[
b(t)=\Re\psi(1/4+it/2)-\log\pi+C_0\ge0,\qquad
V=C_0M_{m^2}+\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
M_m(\tau_{\log n}+\tau_{-\log n})M_m .
\tag{3}
\]
The complete \(V\) is bounded selfadjoint, **including every prime power**, and \(b(t)=\log(2+|t|)+O(1)\) as \(|t|\to\infty\). All statements use the original maximal closed form domain
\[
\mathcal Q=\left\{v\in\mathcal H:
\int_{\mathbb R}b(t)|\widehat{mv}(t)|^2\,\frac{dt}{2\pi}<\infty\right\},
\quad
\|v\|_{\mathcal Q}^2=\|v\|_2^2+
\int b(t)|\widehat{mv}(t)|^2\,\frac{dt}{2\pi}.
\tag{4}
\]
This norm is equivalent to the original semibounded \(H\)-form norm because \(V\) is bounded. The original-domain foundation proves that even \(C_c^\infty(\mathbb R)\) is a **core** for (4). Set \(P_0=I-|e_0\rangle\langle e_0|\).

For \(z\in\mathbb C\), define the *actual physical probe*
\[
\psi_z(x)=m(x)\cos(zx),\qquad
\Xi(z)=\int_{\mathbb R}\Phi(x)\cos(zx)\,dx
=\xi(1/2+iz).
\tag{5}
\]
Every \(\psi_z\) lies in \(\operatorname{Dom}H\subset\mathcal Q\), and \(z\mapsto\psi_z\) is entire as a \(\mathcal Q\)-valued function. The original zero-dual result gives
\(\langle\psi_z,e_0\rangle=\Xi(z)\) for real \(z\); in fact the linear-first pairing identity holds for complex \(z\) too. In particular,
\[
P_0\psi_\gamma=\psi_\gamma-\Xi(\gamma)e_0,\qquad
\gamma\in\mathbb R.
\tag{6}
\]
At a real zero of \(\Xi\), the correction vanishes, but the core theorems below require *all* probes in an interval, not just the discrete zero-indexed ones.

## 2. Main theorem A: every open frequency band is a complete original form core

**Theorem A.** For **every** nonempty real open interval \(I\), including arbitrarily short intervals at arbitrarily high positive frequency,
\[
\boxed{
\overline{\operatorname{span}_{\mathbb C}\{\psi_\gamma:\gamma\in I\}}
^{\ \|\cdot\|_{\mathcal Q}}=\mathcal Q,\qquad
\overline{\operatorname{span}_{\mathbb C}\{P_0\psi_\gamma:\gamma\in I\}}
^{\ \|\cdot\|_{\mathcal Q}}=\mathcal Q\cap e_0^\perp.}
\tag{7}
\]
The same is true using only the rational frequencies \(\gamma\in I\cap\mathbb Q\). This is form-norm density, much stronger than Hilbert-space \(L^2\) totality.

**Proof, first the whole real frequency axis.** By the exact positive multiplier \(b\), Plancherel and the elementary estimate
\(\log(2+|\gamma+u|)\le C+\log(2+|\gamma|)+\log(2+|u|)\), the Schwartz Fourier transform of \(m^2\) gives
\[
\|\psi_\gamma\|_{\mathcal Q}\le C\sqrt{1+\log(2+|\gamma|)}
\qquad(\gamma\in\mathbb R).
\tag{8}
\]
Indeed \(m\psi_\gamma=m^2\cos(\gamma x)\) and its Fourier transform is the sum of two translates of \(\widehat {m^2}/2\). This bounds the **full logarithmic Gamma form**, not merely the \(L^2\) norm. The bounded \(V\) does not change the norm topology.

For arbitrary even \(v\in C_c^\infty\), \(f=v/m\in C_c^\infty\) is even since \(m\) is smooth, positive and even. With \(\widehat f(\gamma)=\int f(x)e^{-i\gamma x}dx\), Fourier cosine inversion gives
\[
\boxed{v=\frac1\pi\int_0^\infty
\widehat f(\gamma)\,\psi_\gamma\,d\gamma}
\tag{9}
\]
as a **Bochner integral in \(\mathcal Q\)**. It converges absolutely in form norm by (8), since \(\widehat f\) is Schwartz. The Bochner integral equals \(v\) in \(L^2\) by ordinary Fourier inversion, so it is the same element of \(\mathcal Q\). Finite Riemann sums approximate the integral in \(\mathcal Q\). The inherited compact-smooth form core implies that the entire nonnegative-frequency probe family is form dense.

Now let \(\ell\) be any continuous complex-linear functional on \(\mathcal Q\) annihilating every \(\psi_\gamma,\gamma\in I\). The map \(z\mapsto\psi_z\) is entire into \(\mathcal Q\): each \(z\)-derivative introduces a polynomial in \(x\) multiplying \(m\cos(zx)\) or \(m\sin(zx)\), while the source \(m^2\) and all derivatives decrease faster than \(e^{-a|x|}\) for every fixed \(a\). Thus \(z\mapsto\ell(\psi_z)\) is entire. It vanishes on an interval, hence identically, and by (9) \(\ell=0\). Hahn–Banach gives the first identity (7). Continuity of \(\gamma\mapsto\psi_\gamma\) makes rational points in \(I\) sufficient.

Finally \(P_0\) is continuous in \(\mathcal Q\), since \(e_0\in\operatorname{Dom}H\) and \(|\langle v,e_0\rangle|\le\|v\|_2\); its range is precisely \(\mathcal Q\cap e_0^\perp\). Apply \(P_0\) to the dense span to obtain the second identity (7). □

## 3. Main theorem B: an **explicit** superoscillatory all-Gamma form approximation

Density in (7) can be made constructive, with no analytic-continuation existence argument. This also supplies a literal counterexample to the false inference that sufficiently high probe *frequency* forces positivity uniformly over **all** finite-rank combinations.

Fix arbitrary \(\Gamma>L>0\), choose \(0<\ell<L\), and fix any target \(z_0\in\mathbb C\). For each positive integer \(N\) put
\[
A=\frac{z_0-\Gamma}{\ell},\quad
c_{N,k}=\binom Nk
\left(\frac{1+A}2\right)^k
\left(\frac{1-A}2\right)^{N-k},\quad
\gamma_{N,k}=\Gamma+\frac{(2k-N)\ell}{N},
\quad 0\le k\le N,
\tag{10}
\]
and define the finite entire-theta physical trial
\[
\boxed{v_{N,z_0}^{\Gamma,\ell}
=\sum_{k=0}^N c_{N,k}\,\psi_{\gamma_{N,k}}.}
\tag{11}
\]
Every \(\gamma_{N,k}\) is **real** and belongs to the fixed high-frequency interval \((\Gamma-L,\Gamma+L)\), independent of N. No complex-frequency generators are hidden inside (11).

**Theorem B.** For each fixed \(\Gamma,\ell,z_0\),
\[
\boxed{
\lim_{N\to\infty}
\left(\|v_{N,z_0}^{\Gamma,\ell}-\psi_{z_0}\|_2+
\|m(v_{N,z_0}^{\Gamma,\ell}-\psi_{z_0})\|_{H^1(\mathbb R)}
\right)=0.}
\tag{12}
\]
Consequently convergence holds in the **exact original \(\mathcal Q\) norm**, including all Gamma frequency energies. The complete signed all-prime potential is paid by its boundedness; no prime or Gamma truncation is performed.

**Proof.** Set
\[
F_N(x)=\left[\cos\left(\frac{\ell x}{N}\right)
+iA\sin\left(\frac{\ell x}{N}\right)\right]^N .
\]
The **finite binomial identity** is
\[
\frac{v_{N,z_0}^{\Gamma,\ell}(x)}{m(x)}
=\frac12\left[e^{i\Gamma x}F_N(x)+
e^{-i\Gamma x}F_N(-x)\right].
\tag{13}
\]
For fixed real x,
\[
F_N(x)\longrightarrow e^{i A\ell x}
=e^{i(z_0-\Gamma)x},\qquad
F_N'(x)\longrightarrow i(z_0-\Gamma)e^{i(z_0-\Gamma)x}.
\tag{14}
\]
The limit of (13) is \(\cos(z_0x)\), including its first derivative.

Crucially the convergence is controlled on the **whole line**, not just a fixed spatial compact. For all real x, all N,
\[
|F_N(x)|\le
\left(1+\frac{|A|\ell|x|}{N}\right)^N
\le e^{|A|\ell|x|},
\qquad
|F_N'(x)|\le\ell(1+|A|)e^{|A|\ell|x|}.
\tag{15}
\]
The derivatives of \(m^2\) and \(m\) are doubly exponentially decreasing on both tails, even after multiplication by any fixed \(e^{C|x|}\). Therefore (13)–(15) permit dominated convergence both for \(m\) times the probe and for the *source* \(m^2\) times its first derivative, proving (12). Finally \(b(t)\le C(1+t^2)\), so the \(H^1\)-convergence of the source implies convergence of its full Gamma form \(\int b|\widehat{mv}|^2\); the prime potential is bounded. □

**Corollary B1 (actual full-operator negative superoscillation).** Take \(z_0=i/2\). Then \(\psi_{i/2}=m\cosh(x/2)=e_0/2\), and the exact ground identity (2) and (12) give
\[
\boxed{
\lim_{N\to\infty}H[v_{N,i/2}^{\Gamma,\ell}]
=H[e_0/2]=-\frac18.}
\tag{16}
\]
For *every fixed* \(\Gamma>L\), at least one finite, fully explicit binomial combination (11) has **negative original full H-form**, despite all its input frequencies lying in the arbitrarily narrow band \((\Gamma-L,\Gamma+L)\). Taking real parts gives a real-valued negative combination if desired, because the imaginary parts tend to zero in form norm. The quantifiers are: **first fix \(\Gamma,\ell\), then let N grow**. No uniform-in-\(\Gamma\) convergence rate or numerical N bound is asserted.

This exact negative direction is the **already known ground direction**, and its \(P_0\)-projection tends to zero. It is not a negative mean-zero direction, not an off-line zero and not a counterexample to RH.

## 4. Main theorem C: **all fixed-size complex zero-probe clusters** become positive at high ordinate

The most recent high-zero-probe result in this repository proved positivity for a fixed jet at one zero and for an entire conjugate two-plane. The next theorem includes **arbitrary off-diagonal interactions between any fixed number of distinct nearby zeros and all their jets**, uniformly even as their ordinates and strip coordinates approach each other. There is **no frequency separation hypothesis**.

**Theorem C.** Fix integers \(r\ge1\) and a real \(L>0\). There exist \(c_{r,L}>0\) and \(\Gamma_{r,L}<\infty\) such that the following holds for every \(\Gamma\ge\Gamma_{r,L}\): choose any complex offsets \(u_1,\ldots,u_J\) with \(|u_j|\le L\), and any jet orders \(r_j\ge1\) with \(\sum_jr_j\le r\). Let
\[
\mathcal U_{\Gamma,\mathbf u,\mathbf r}
=\operatorname{span}_{\mathbb C}\{
\partial_z^k\psi_z|_{z=\Gamma+u_j}:
1\le j\le J,\ 0\le k<r_j\}.
\]
Then, for **every** \(v\in\mathcal U_{\Gamma,\mathbf u,\mathbf r}\),
\[
\boxed{H[v]\ge c_{r,L}\log\Gamma\ \|v\|_2^2.}
\tag{17}
\]
The constants are independent of all node separations, include collisions/confluent derivatives, and control the **entire complex coefficient space**. No Xi-zero or RH assumption is needed. If these offsets correspond to actual Xi zeros, the known zero selector puts their entire jets (up to their true zero multiplicity) in the genuine theta-mode complement, yet they remain high-ordinate **positive**.

**Proof: uniform companion-matrix observability.** Every proposed vector has the exact form
\[
v(x)=\frac{m(x)}2
[e^{i\Gamma x}g(x)+e^{-i\Gamma x}g(-x)],\quad
g(x)=\sum_{j,k}a_{jk}(ix)^k e^{iu_jx}.
\tag{18}
\]
Set \(W=\int m^2|g|^2dx\). The exponential polynomial g solves a constant-coefficient ODE
\[
P(D_x)g=0,\qquad
P(\lambda)=\prod_{j=1}^J(\lambda-iu_j)^{r_j},
\quad d=\deg P=\sum_jr_j\le r.
\tag{19}
\]
The coefficients of monic P lie in a fixed compact subset of \(\mathbb C^d\), since \(|u_j|\le L\). Let \(\mathsf A\) be its standard d-by-d companion matrix in derivative coordinates
\(y=(g,g',\ldots,g^{(d-1)})^T\), and \(e_1=(1,0,\ldots,0)^T\). Thus \(g(x)=e_1^Te^{x\mathsf A}y(0)\). For every such companion matrix the finite interval observation Gram
\[
\mathsf G_{\mathsf A}
=\int_{-1}^{1}e^{x\mathsf A^*}\overline{e_1}e_1^T
e^{x\mathsf A}dx
\tag{20}
\]
is **strictly positive definite**: if its quadratic form vanishes, the analytic solution g vanishes on an interval, so its first d derivatives at zero, hence y(0), all vanish. The set of all companion matrices with the indicated uniformly bounded coefficients is contained in a compact family, and every companion in its closure retains this elementary observability. Continuity of the Gram therefore supplies a strictly positive *uniform* smallest eigenvalue for every \(1\le d\le r\).

Since \(\min_{|x|\le1}m^2(x)>0\), this gives a uniform bound for \(\|y(0)\|\) by \(C_{r,L}W^{1/2}\). Bounded matrix exponentials and derivatives now yield, for every fixed integer k,
\[
\boxed{|g^{(k)}(x)|\le
C_{r,L,k}e^{C_{r,L}|x|}W^{1/2}
\quad\text{for all real }x.}\tag{21}
\]
Importantly, the constant does *not* contain any inverse Vandermonde separation factor.

**Uniform source concentration and Fourier remainders.** From (21), the double-exponential weight m permits a single finite \(R=R(r,L)\) with
\[
\int_{|x|>R}m^2|g|^2dx\le W/2.
\]
As m is positive on the compact interval,
\[
\boxed{\int m^4|g|^2dx\ge
\kappa_{r,L}W,\quad
\kappa_{r,L}:=\frac12\min_{|x|\le R}m^2(x)>0.}\tag{22}
\]
Equations (21) also bound in \(L^1\), uniformly after division by W, all x derivatives of
\(m^{2k}(x)g(x)\overline{g(-x)}\) for \(k=1,2\). Integration by parts in the \(2\Gamma\) Fourier factors gives, for each fixed N,
\[
\|v\|^2=\tfrac12 W+O_{r,L,N}(\Gamma^{-N})W,\qquad
\|mv\|^2=\tfrac12\int m^4|g|^2dx
+O_{r,L,N}(\Gamma^{-N})W.
\tag{23}
\]
In particular \(\|mv\|^2\ge(\kappa_{r,L}/4)W\) for all sufficiently high \(\Gamma\).

The **exact, untruncated** Gamma multiplier b has
\(b(t)-\log\Gamma=O(1)\) for \(|t-\Gamma|\le\Gamma/2\), and the same on the corresponding negative carrier window. Outside those windows the full logarithmic symbol grows only as \(O(1+\log(2+\Gamma+|u|))\). By (21) the normalized source envelopes \(m^2g(x)\), \(m^2g(-x)\) have uniformly bounded Schwartz seminorms; Plancherel plus a split into those near and remote frequency regions gives
\[
\boxed{
\big|\langle mv,b(D)mv\rangle-\log\Gamma\|mv\|^2\big|
\le C_{r,L}W .}\tag{24}
\]
No finite Gamma replacement was used. The full signed potential satisfies
\(|\langle v,Vv\rangle|\le\|V\|\|v\|^2\le\|V\|W\)
(the final inequality follows directly from (18) and evenness of m). Equations (22)–(24) give
\[
H[v]\ge
\left[\frac{\kappa_{r,L}}4\log\Gamma-C_{r,L}-\|V\|\right]W .
\]
For a sufficiently high threshold this is at least
\((\kappa_{r,L}/8)\log\Gamma\,W\ge
(\kappa_{r,L}/8)\log\Gamma\,\|v\|^2\).
This proves (17), uniformly even under arbitrary node collisions. □

The fixed-rank quantifier is indispensable. The observation constant in (20) is not uniform when the ODE degree d grows without bound. Theorem B proves a **literal full-operator counterexample** to such an all-dimension upgrade.

## 5. An exact countable Gram criterion for RH and two rank-divergence statements

For real \(s,t\) put \(w=m^2=\Phi/(2h)\), \(f_s=w(x)\cos(sx)\), \(S f=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}(\tau_{\log n}+\tau_{-\log n})f\) on this actual doubly-exponentially decaying source class, and
\[
\boxed{\mathsf K(s,t)=
\langle f_s,(b(D)-C_0-S)f_t\rangle
+\frac12\Xi(s)\Xi(t).}
\tag{25}
\]
The shift pairing series is absolutely convergent because the two complete theta source factors jointly suppress large \(\log n\); this is exactly the bounded full-prime term in (3). Formula (25) is a real-symmetric exact analytic kernel, retaining the **whole original Gamma symbol**, full signed prime-power series, and the exact ground projection. Its fundamental meaning is
\[
\boxed{\mathsf K(s,t)=\mathfrak h[P_0\psi_s,P_0\psi_t],}\tag{26}
\]
because \(He_0=-e_0/2\) and \(\langle\psi_s,e_0\rangle=\Xi(s)\) for real s.

The established even Weil positivity criterion in the archive (round 05 §2 and §7) is
\[
\mathrm{RH}\iff\mathfrak h[v]\ge0
\quad\text{for all }v\in\mathcal Q\cap e_0^\perp.
\tag{27}
\]
Combining (7), form continuity, (26) and (27) gives the **precise one-band reformulation**:
\[
\boxed{
\text{For any *one fixed* nonempty real interval }I,\quad
\mathrm{RH}
\iff
[\mathsf K(s_i,s_j)]_{i,j=1}^N\succeq0
\quad\text{for every }N\ge1\text{ and }
s_1,\ldots,s_N\in I\cap\mathbb Q.}
\tag{28}
\]
No new RH proof follows from merely naming this criterion: *every dimension* is required. The use of rational frequencies makes the family countable and completely specified, not a finite certificate.

Fix any \(L>0\) and let \(I_\Gamma=(\Gamma-L,\Gamma+L)\), \(\Gamma>L+2\). Define \(n_{\rm all}(\Gamma)\) as the minimum number of distinct real frequencies in \(I_\Gamma\) that admit a negative H-form linear combination of the unprojected \(\psi_s\). Define \(n_0(\Gamma)\) analogously with \(P_0\psi_s\), and put \(n_0=\infty\) when there is no such mean-zero negative combination.

**Theorem D (actual rank-divergence obstruction).**
\[
\boxed{n_{\rm all}(\Gamma)<\infty\ \text{for every }\Gamma>L+2,
\qquad \lim_{\Gamma\to\infty}n_{\rm all}(\Gamma)=+\infty.}
\tag{29}
\]
Both assertions are **unconditional** about the original exact full operator. The finite witness comes from the explicit binomial ground approximants in Theorem B. The divergence follows from Theorem C for each fixed r.

In the actual **mean-zero** RH-bearing space:
\[
\boxed{
\mathrm{RH}\Longleftrightarrow n_0(\Gamma)=\infty
\text{ for any (equivalently every) fixed }\Gamma>L+2.}
\tag{30}
\]
If RH is false, then for every fixed Γ the core theorem supplies a finite negative mean-zero combination, but Theorem C forces
\[
\boxed{n_0(\Gamma)<\infty\text{ for all }\Gamma,\qquad
n_0(\Gamma)\longrightarrow\infty\quad(\Gamma\to\infty).}\tag{31}
\]
These implications use the already proved original Weil equivalence (27). The existence of any off-line zero is *not* assumed or inferred.

The precise failure mechanism is thus mathematical, not rhetorical: **a frequency band can be arbitrarily high and arbitrarily narrow, every fixed-size probe cluster in it eventually has positive full H-form, yet arbitrarily many probes collectively approximate the actual negative ground with negative full H-form.** Removing the ground turns the all-rank sign into *exactly the unproved RH problem*. One cannot infer the required all-rank sign from finitely many local high-zero probes, their conjugate planes, or a bounded-degree jet theorem.

**Acceptance scope: unconditional original-form analytic band core, explicit form-convergent superoscillations, uniform fixed-rank all-node high-carrier positivity, exact countable RH Gram equivalence and actual full-operator rank divergence. NO NEW UNCONDITIONAL RH THEOREM PROVED.**

### Dependencies and audit scope

The exact theta, maximal form core, source multiplier, full bounded prime potential and ground identity are from [ORIGINAL_FORM_FOUNDATION.md](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md). The complex-zero selector and its multiplicity jets are from [ZETA_ZERO_DUAL_PROBES.md](../20261013_theta_zero_dual_complement/ZETA_ZERO_DUAL_PROBES.md). The fixed one-zero and conjugate-pair high-ordinate positivity and its limitations are in [HIGH_ZERO_PROBE_TWO_PLANE.md](../20261013_high_zero_probe_positivity/HIGH_ZERO_PROBE_TWO_PLANE.md). The classical original even RH equivalence is recorded in rounds/05/REPORT-pages-01-05.txt, equations (8)–(10), with its complete-inertia proof in round 05 §7. Theorem A uses the inherited compact-smooth form core, with every new passage to interval cores proved above. An independent-in-task line-by-line proof audit accompanies this manuscript. No outside referee or formal proof-assistant certification is claimed.
