# Quantitative decay of true critical-mode Gram minima

Date: 2026-10-12. This is a direct analytic consequence of the **original true-theta** Hilbert-valued translation family, not a generic compactness argument. The final goal is still an unconditional proof of RH. This note proves a finite-dimensional conditioning estimate useful for evaluating or rejecting threshold-preserving spectral certificates. It does not prove a new RH zero-free region.

The source identities, closed-operator critical modes, and the sharp translation singularity are stated and proved in [REPORT.md](REPORT.md). In particular \(a_*=(\log2)/2\), and
\[
v_t=\frac{\Phi(x+t)+\Phi(x-t)-2\cosh(t/2)\Phi(x)}{m(x)}
=2\sum_{r\ge1}\frac{t^{2r}}{(2r)!}w_r
\quad (|t|<a_*),
\tag{1}
\]
where \(w_r=(\Phi^{(2r)}-4^{-r}\Phi)/m\in\ker H\), with the norm asymptotic
\[
\|v_t\|_2^2\sim(3/128)(a_*-t)^{-5/2}\quad(t\uparrow a_*).
\tag{2}
\]
The original multiplier is \(m=\sqrt{\Phi/(2\cosh(x/2))}\); none of the real theta, infinite prime or Gamma input has been changed.

## Theorem: explicit finite-k singular-value decay

Let \(\mathcal W_k=\operatorname{span}\{w_1,\ldots,w_k\}\). The vectors are linearly independent, so its L² Gram matrix is positive definite. Define
\[
\mu_k^{\mathrm{src}}
=\inf_{\substack{u\in\mathcal W_k\\\|u\|_2=1}}\|mu\|_2^2,
\tag{3}
\]
and, for every fixed \(d>0,\alpha>0\),
\[
\mu_k^{\mathrm{edge}}(d,\alpha)
=\inf_{\substack{u\in\mathcal W_k\\\|u\|_2=1}}
\alpha\int m(x)m(x+d)|u(x+d)-u(x)|^2dx.
\tag{4}
\]

**Theorem.** There are finite constants \(C_0>0\) and \(C_{d,\alpha}>0\), independent of k, such that for every sufficiently large integer k,
\[
\boxed{0<\mu_k^{\mathrm{src}}\le C_0
\left(\frac{\log k}{k}\right)^{5/2},\qquad
0<\mu_k^{\mathrm{edge}}(d,\alpha)\le C_{d,\alpha}
\left(\frac{\log k}{k}\right)^{5/2}.}
\tag{5}
\]
Both minima tend monotonically to zero as \(k\to\infty\). In particular for the *actual* n=2 prime edge, take \(d=\log2,\alpha=\log2/\sqrt2\). This result is not inferred from positive finite-dimensional Ritz matrices; it supplies explicit true-nullspace trial vectors whose Rayleigh quotients vanish at a proved rate.

### Step 1. A uniform complex-circle norm estimate

For any \(s\in[a_*/2,a_*)\) the true theta series and the elementary inequality
\[
\Re(e^{\pm2z})\ge e^{-2s}>\tfrac12 \quad(|z|\le s)
\]
(see REPORT.md §2.2) yield a uniform positive-tail bound
\[
|v_z(x)|\le C e^{5|x|/2}
\exp\{-\pi(e^{-2s}-1/2)e^{2|x|}\},
\qquad x\in\mathbb R,\quad |z|\le s,
\tag{6}
\]
after enlarging C on a fixed spatial compact set. A constant independent of \(s\uparrow a_*\) exists because \(|z|\le a_*\) keeps all prefactors bounded and the theta-mode tails are uniformly dominated on each spatial half-line. Let \(c_s=\pi(e^{-2s}-1/2)\). Then \(c_s\asymp a_*-s\), and integrating the square of (6) with \(r=e^{2|x|}\) gives
\[
\boxed{M(s):=\sup_{|z|=s}\|v_z\|_2
\le C_1(a_*-s)^{-5/4}.}
\tag{7}
\]
The bound includes all theta modes and requires no numerical constant or RH input.

### Step 2. Actual derivative-space Taylor error

Let
\[
V_k(t):=2\sum_{r=1}^{k}\frac{t^{2r}}{(2r)!}w_r\in\mathcal W_k.
\]
For \(0<t<s<a_*\), the Banach-valued Cauchy integral formula on \(|z|=s\) bounds every Taylor coefficient of \(v_z\) by \(M(s)/s^n\). Since the odd coefficients vanish,
\[
\|v_t-V_k(t)\|_2
\le M(s)\frac{(t/s)^{2k+2}}{1-(t/s)^2}.
\tag{8}
\]
Choose \(\delta=a_*-t>0,\ s=a_*-\delta/2\). Then
\[
\frac ts=1-\frac{\delta}{2s},\quad
1-(t/s)^2\ge\frac{\delta}{2a_*},\quad
(t/s)^{2k+2}\le e^{-k\delta/a_*}.
\]
Using (7),
\[
\boxed{
\|v_t-V_k(t)\|_2
\le C_2\,\delta^{-9/4}e^{-k\delta/a_*}.}
\tag{9}
\]

Set
\[
\delta_k=\frac{5a_*\log k}{k},
\qquad t_k=a_*-\delta_k
\quad(k\ \text{sufficiently large}).
\tag{10}
\]
Then
\[
\|v_{t_k}-V_k(t_k)\|_2
\le C_2\,\delta_k^{-9/4}k^{-5}
=O\bigl(k^{-11/4}(\log k)^{-9/4}\bigr)=o(1).
\tag{11}
\]
Meanwhile (2) gives \(\|v_{t_k}\|_2\ge c\,\delta_k^{-5/4}\to\infty\). Therefore
\[
\|V_k(t_k)\|_2\ge \frac c2\delta_k^{-5/4}
\tag{12}
\]
for all sufficiently large k. Thus each \(V_k(t_k)\) is a **concrete finite linear combination of the exact derivative zero modes**, not an unspecified element in their closure.

### Step 3. Uniform source and fixed-edge energies

The functions \(f_t=mv_t\) are uniformly Schwartz for \(t\) in the compact real segment \([0,a_*]\). Hence
\[
\sup_{0\le t\le a_*}\|m v_t\|_2
=\sup_{0\le t\le a_*}\|f_t\|_2<\infty.
\tag{13}
\]
For each fixed \(d,\alpha\), the full theta tail calculation in REPORT.md §3 proves
\[
\sup_{a_*-\eta\le t\le a_*}
\mathcal Q_{d,\alpha}[v_t]<\infty,
\tag{14}
\]
where the endpoint is understood through its finite weighted edge integral despite \(v_{a_*}\notin L²\).

The multiplication \(M_m\) and the nonnegative edge operator \(Q_{d,\alpha}\) are bounded on even L². Thus (11)–(14) give
\[
\|mV_k(t_k)\|_2\le C,\qquad
\mathcal Q_{d,\alpha}[V_k(t_k)]\le C_{d,\alpha}
\tag{15}
\]
uniformly in k, using the triangle inequality for \(Q_{d,\alpha}^{1/2}\). Divide by (12) squared and use \(\delta_k^{5/2}=(5a_*)^{5/2}(\log k/k)^{5/2}\). This proves both upper estimates in (5). Strict positivity of each finite-dimensional minimum follows from m>0 and from the fact that zero fixed-edge energy would make a nonzero L² vector d-periodic. Monotonicity follows from \(\mathcal W_k\subset\mathcal W_{k+1}\). □

## Matrix and numerical-certificate meaning

Let \(G_k=(\langle w_i,w_j\rangle)_{i,j\le k}\), \(S_k=(\langle mw_i,mw_j\rangle)_{i,j\le k}\), and \(E_k=(\langle w_i,Q_{d,\alpha}w_j\rangle)_{i,j\le k}\). All are positive definite, and
\[
\mu_k^{\mathrm{src}}=\lambda_{\min}(G_k^{-1/2}S_kG_k^{-1/2}),\quad
\mu_k^{\mathrm{edge}}=\lambda_{\min}(G_k^{-1/2}E_kG_k^{-1/2}).
\tag{16}
\]
The Rayleigh quotients on \(w_1\) give *strictly positive, k-independent* lower bounds on the corresponding largest generalized eigenvalues. Hence their generalized condition numbers grow at least like
\[
\boxed{\kappa_{\mathrm{src}}(k),\ \kappa_{\mathrm{edge}}(k)
\ \ge c\left(\frac{k}{\log k}\right)^{5/2}.}
\tag{17}
\]
Here the constants may depend on the fixed edge, and no bound on the condition number of the unrelated signed Birman–Schwinger matrix is claimed.

This gives a quantified reason why passing an arbitrary *fixed-dimensional* threshold correction or proving a positive edge Gram on each finite derivative span does not yield a uniform threshold estimate as the span grows. It does not prohibit a correctly renormalized moving-rank construction or prove anything about the sign of H on its true kernel's orthogonal complement. **No complete RH proof, no new unconditional off-line-zero exclusion.**

## Reproducibility and scope

This is a self-contained analytic proof from the already submitted exact theta-translation theorem; the numerical sanity program accompanying REPORT.md is a check of the underlying singular scaling and finite edge, **not** a certification of (5). The exponent 5/2 comes from the real theta tail and the controlled complex Taylor approximation, not a fit to finite Gram eigenvalues. All gamma and arithmetic terms stay in the inherited true operator. No external or formal proof-assistant certification is claimed.
