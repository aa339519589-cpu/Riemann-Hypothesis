# Compactness and spatial escape of genuine critical theta modes

Date: 2026-10-12. This is a continuation of REPORT.md. All operators are the unchanged full-prime, full-Gamma, full-theta operators of round 5. The result is a structural theorem about the actual critical nullspace, not a proof of RH.

## 1. A compact source map on the entire exact nullspace

Let \(H=M_m b(D)M_m-V\) act on the full even \(L^2(\mathbb R)\), with \(m=\sqrt{\Phi/(2\cosh(x/2))}>0\), \(V=C_0 M_{m^2}+S_m\) bounded selfadjoint, and \(b\ge0\) the original Gamma Fourier symbol. Define \(\mathcal K=\ker H\). Round 5 establishes the selfadjoint domain and infinitely many linearly independent exact critical vectors.

**Theorem 1.** The bounded operator \(M_m|_{\mathcal K}:\mathcal K\to L^2_{\rm even}\) is compact and injective. The Hilbert-space range is not closed. It has no bounded inverse onto that range.

**Proof.** Set \(B=M_m b(D)M_m\ge0\), so \(H=B-V\), with \(\operatorname{Dom}H=\operatorname{Dom}B\) by bounded perturbation. For \(v\in\mathcal K\), \(\|v\|_2\le1\), we have \(Bv=Vv\) and therefore
\[
\int b(\xi)|\widehat{mv}(\xi)|^2\,d\xi/(2\pi)
=\langle v,Bv\rangle=\langle v,Vv\rangle\le\|V\|.
\tag{1}
\]
The exact symbol \(b(\xi)=\sum_{j\ge0}(\xi/2)^2/[a_j(a_j^2+(\xi/2)^2)]\), \(a_j=j+1/4\), tends to \(+\infty\): for \(a_j\le|\xi|/2\) each summand is at least \(1/(2a_j)\), and the resulting harmonic partial sum diverges.

Consequently \(g=mv\) has uniformly small high-frequency tails over the unit ball of \(\mathcal K\). It also has uniformly small spatial tails:
\[
\int_{|x|>R}|g(x)|^2dx\le\sup_{|x|>R}m(x)^2\longrightarrow0.
\tag{2}
\]
The bounded Fourier norm and high-frequency cutoff imply uniform translation continuity of g in \(L^2\): for each cutoff T,
\[
\|g(\cdot+h)-g\|_2^2
\le T^2h^2\|g\|_2^2+4\int_{|\xi|>T}|\widehat g(\xi)|^2d\xi/(2\pi).
\]
Kolmogorov-Riesz now makes \(\{mv:\|v\|\le1,v\in\mathcal K\}\) relatively compact. Since m>0 almost everywhere, the map is injective. Since \(\dim\mathcal K=\infty\), a compact injective operator cannot have a bounded inverse on its image; by the closed-range theorem for bounded injective maps, its range is not closed. \(\square\)

## 2. Every fixed real prime edge becomes compact on the true nullspace

Fix d>0, α>0 and define the genuine edge form
\[
q_{d,\alpha}[v]=\alpha\int m(x)m(x+d)|v(x+d)-v(x)|^2dx.
\]
Its bounded positive operator on even \(L^2\) is **exactly**
\[
Q_{d,\alpha}=M_{\alpha m(x)[m(x+d)+m(x-d)]}
-\alpha M_m(\tau_d+\tau_{-d})M_m.
\tag{3}
\]
Let \(P_{\mathcal K}\) be orthogonal projection and \(T_{d,\alpha}=P_{\mathcal K}Q_{d,\alpha}|_{\mathcal K}\).

**Theorem 2.** \(T_{d,\alpha}\) is compact, positive and injective on the full \(\mathcal K\). Its nonzero spectrum is an infinite decreasing sequence of positive eigenvalues (counted with multiplicity) converging to zero. In particular, zero is in its essential spectrum, but is not an eigenvalue.

**Proof.** Factor the diagonal term restricted to \(\mathcal K\) as
\[
M_{\alpha m(x)[m(x+d)+m(x-d)]}|_{\mathcal K}
=M_{\alpha[m(x+d)+m(x-d)]}(M_m|_{\mathcal K}),
\]
and the off-diagonal terms as \((M_m\tau_{\pm d})(M_m|_{\mathcal K})\). All outside factors are bounded, while the right factor is compact by Theorem 1. Thus \(Q_{d,\alpha}|_{\mathcal K}\), and then \(T_{d,\alpha}\), are compact.

If \(q_{d,\alpha}[v]=0\), positivity of m yields \(v(x+d)=v(x)\) a.e.; a periodic \(L^2(\mathbb R)\) function must vanish. Hence \(T_{d,\alpha}\) is injective. Apply the compact selfadjoint spectral theorem on the infinite-dimensional \(\mathcal K\). \(\square\)

This holds for each individual prime power \(d=\log n,\alpha=\Lambda(n)/\sqrt n\); it does **not** assert uniform estimates as n grows or compactness for a non-norm-convergent family.

## 3. Exact Gamma-law of the non-polynomial theta escape family

Let \(a_*=(\log2)/2\). The translation report proves that
\[
v_t(x)=\frac{\Phi(x+t)+\Phi(x-t)-2\cosh(t/2)\Phi(x)}{m(x)}
\in\mathcal K,\quad 0<t<a_*,
\]
and that \(\|v_t\|_2^2\sim(3/128)(a_*-t)^{-5/2}\). Put \(\delta=a_*-t\), \(u_\delta=v_{a_*-\delta}/\|v_{a_*-\delta}\|_2\).

**Theorem 3.** For every bounded continuous test function \(\varphi:[0,\infty)\to\mathbb C\),
\[
\boxed{\lim_{\delta\downarrow0}\int_{\mathbb R}
\varphi(\delta e^{2|x|})|u_\delta(x)|^2dx
=\frac{(2\pi)^{5/2}}{\Gamma(5/2)}
\int_0^\infty\varphi(y)y^{3/2}e^{-2\pi y}dy.}
\tag{4}
\]
Thus the spatial mass escapes to \( |x|=\frac12\log(1/\delta)+O(1)\), with rescaled coordinate converging to a Gamma distribution of shape \(5/2\) and rate \(2\pi\).

**Proof.** On x→+∞, uniform for t near \(a_*\), the original complete theta series gives
\[
v_t(x)=2\pi e^{5x/2-9t/2}
\exp[-\pi(e^{-2t}-1/2)e^{2x}](1+o(1)).
\tag{5}
\]
The negative tail is its mirror, since \(v_t\) is even. On a fixed compact x interval, the normalized probability mass tends to zero. For x≥X with X large fixed, substitute \(y=\delta e^{2x}\). Because \(\pi(e^{-2t}-1/2)/\delta\to\pi\),
\[
\frac{\delta^{5/2}}{2y}
\left|v_{a_*-\delta}(\tfrac12\log(y/\delta))\right|^2
\to2\pi^2e^{-9a_*}y^{3/2}e^{-2\pi y}
\quad(y>0).
\]
The exact positive n=1 theta mode and the exponentially small remaining modes furnish the uniform bound \(Cy^{3/2}e^{-cy}\) for all \(y\ge\delta e^{2X}\), where c>0. Dominated convergence applies even for bounded nondecaying test functions. Doubling by evenness and dividing by \(\delta^{5/2}\|v_t\|_2^2\to3/128\), the normalizing factor is \(4\pi^2 e^{-9a_*}/(3/128)=(2\pi)^{5/2}/\Gamma(5/2)\), giving (4). \(\square\)

## 4. Sharp collapse rate for a fixed prime edge

The existing translation report established that each fixed edge has a finite nonzero limiting *unnormalized* form
\[
q^*_{d,\alpha}
:=\int\alpha\,m(x)m(x+d)|v_{a_*}(x+d)-v_{a_*}(x)|^2dx
\in(0,\infty),
\tag{6}
\]
where \(v_{a_*}\) is pointwise defined but not in \(L^2\). The integral is nevertheless finite: use \(|v(x+d)-v(x)|^2\le2(|v(x+d)|^2+|v(x)|^2)\) and the exact theta tails; the integrands are \(O(e^{9|x|}\exp[-c_de^{2|x|}])\). Positivity follows because an unbounded continuous function \(v_{a_*}\sim2\pi e^{5|x|/2-9a_*/2}\) cannot be periodic.

Uniform domination and norm asymptotics then give
\[
\boxed{\lim_{\delta\downarrow0}\delta^{-5/2}q_{d,\alpha}[u_\delta]
=\frac{128}{3}\,q^*_{d,\alpha}\in(0,\infty).}
\tag{7}
\]
The source map has an analogous precise collapse,
\[
\boxed{\lim_{\delta\downarrow0}\delta^{-5/4}\|m u_\delta\|_2
=\sqrt{128/3}\,\|f_{a_*}\|_2\in(0,\infty),}
\tag{8}
\]
where \(f_t=m v_t\) and \(f_t\to f_{a_*}\) in ordinary \(L^2\).

## 5. Scope and verification

Theorem 1 isolates a compact source embedding *restricted to the actual zero eigenspace*. Theorem 2 turns the earlier Weyl escape argument into the full compact spectral theorem for each fixed prime edge. Theorems 3–4 give exact asymptotic constants, rather than an unsupported qualitative bound.

None of these conclusions excludes off-critical zeta zeros. The exact RH acceptance condition remains that every nontrivial ζ zero satisfies \(\Re\rho=1/2\); this is not achieved here. Results rely on the round-5 theta source/domain identity, and are not presented as independently refereed or machine-certified. No old file is changed.
