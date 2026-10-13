# Updated strip input and consequences for the full selection relation

**Date:** 2026-10-13

Baiying Liu’s preprint [*Slightly improved zero-free half-planes for the quasi-Riemann hypothesis*](https://arxiv.org/abs/2610.12234) states the bound

\[
B=\frac{1507-2\sqrt{921}}{1653}=0.874957069799\ldots
\]

for the same uniform finite-order Hecke family over \(F=\mathbb Q(\sqrt{-3})\) used in the OpenAI \(7/8\) result, with its stated Dirichlet and zeta consequences. Principal poles are excluded from the nonvanishing conclusions. Set

\[
\delta=1-B=\frac{146+2\sqrt{921}}{1653}=0.125042930201\ldots,
\qquad
a=B-\frac12=\frac{1361-4\sqrt{921}}{3306}=0.374957069799\ldots,
\]

so that \(\delta=\tfrac12-a\). The exact source and version are the preprint above and its [public Lean repository at commit `7d10420de90efa2f082a06a342fc7accbd57ab37`](https://github.com/liubaiying101/Slightly-improved-zero-free-half-planes-for-the-quasi-Riemann-hypothesis/tree/7d10420de90efa2f082a06a342fc7accbd57ab37). The pinned [correspondence entry](https://github.com/liubaiying101/Slightly-improved-zero-free-half-planes-for-the-quasi-Riemann-hypothesis/blob/7d10420de90efa2f082a06a342fc7accbd57ab37/CombinedPaperVerification.lean) contains `algebraic_family_bound`, `algebraic_hecke_nonzero`, `algebraic_dirichlet_nonzero`, and `algebraic_zeta_nonzero`. It states the strict region \(\Re s>B\), with the principal pole at \(s=1\) allowed. The preprint remains the citation for the mathematical argument; the formal declarations cover specified conclusions and do not certify every sentence of the article.

## Strip translation

Write \(\Xi(z)=\xi(\tfrac12+iz)\), and let \(w=\gamma+i(\tfrac12-\beta)\) correspond to a nontrivial zero \(\rho=\beta+i\gamma\) of \(\zeta\). The zero-free half-plane gives \(\beta\le B\); the functional equation gives \(\beta\ge1-B\). Thus every zero of \(\Xi\) lies in the closed strip

\[
|\Im w|=|\tfrac12-\beta|\le B-\tfrac12=a.
\]

This is the updated strip input used below. It is a zeta-zero location statement; by itself it gives no bound on a source function or its arithmetic correlations.

## Consequences for a fixed real low state

Use the complete selection input from [the fixed source-selection identity](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/60374863affee2cb4f4f4ca636b5dfeb2cb639d6/history/source-materials/RH_%E7%A0%94%E7%A9%B6%E7%BB%AD%E7%AF%87_20261011.md): a real even low state \(Lq=\lambda q\), \(0<\lambda<\tfrac12\), with

\[
\varepsilon=\tfrac12-\lambda,\quad h(x)=\cosh(x/2),\quad g(x)=2h(x)q(x),\quad f(x)=\Phi(x)q(x),\quad a_w=\widehat f(w).
\]

For the set \(\mathcal Z\) of all distinct zeros, with each multiplicity denoted by \(n_w\), the inherited identities are

\[
\varepsilon g(x)=-\sum_{w\in\mathcal Z}n_w a_w e^{-iwx},\qquad
a_{-w}=a_w,\quad a_{\bar w}=\overline{a_w},\quad
\sum_{w\in\mathcal Z}n_w\langle\Re w\rangle^N|a_w|<\infty\quad(N\ge0),
\]

and the complete coefficient equation

\[
\varepsilon a_z+\sum_{w\in\mathcal Z}n_w M(z-w)a_w=0\quad(z\in\mathcal Z),
\qquad M=\widehat{m^2},\quad m^2=\frac{\Phi}{2h}.
\]

These are full infinite relations, not finite zero compressions. The results that follow use the strip bound together with these selection identities.

**Derivative tails.** For every fixed integer \(j\ge0\), termwise differentiation and the coefficient summability give

\[
|g^{(j)}(x)|\le C_{q,j}e^{a|x|},\qquad
|q^{(j)}(x)|\le C'_{q,j}e^{-(1/2-a)|x|}
=C'_{q,j}e^{-\delta|x|}.
\]

Indeed one may take \(C_{q,j}=\varepsilon^{-1}\sum_w n_w|a_w||w|^j\), which is finite by the stated weighted summability and the bounded imaginary parts. Also, every fixed derivative of \((2h)^{-1}\) is \(O_j(e^{-|x|/2})\), and \(q=(2h)^{-1}g\); Leibniz’s rule proves the second estimate. The exponent includes the closed strip endpoint. The constants depend on the fixed state, \(j\), and \(\varepsilon\); they are not uniform as \(\lambda\uparrow\tfrac12\), and no uniformity over all low states follows.

**Exact activity exponent.** Let

\[
\mathcal Z_q=\{w\in\mathcal Z:a_w\ne0\},\qquad
\alpha(q)=\sup_{w\in\mathcal Z_q}\Im w=\sup_{w\in\mathcal Z_q}|\Im w|,
\]

and define \(\tau(u)=\inf\{b:|u(x)|\le C e^{bx}\text{ for }x\ge0\text{ for some }C\}\). For every nonzero real low state,

\[
0<\alpha(q)\le a,\qquad \boxed{\tau(g)=\alpha(q),\quad \tau(q)=\alpha(q)-\tfrac12.}
\]

The strict lower bound follows from the inherited negative Weil identity: if only critical-line zeros were active, its zero-side sum would be nonnegative. For the exact rate, the inherited one-sided Laplace identity, initially for \(\Re s>1/2\), is

\[
\int_0^\infty e^{-sx}g(x)\,dx
=-\varepsilon^{-1}\sum_{w\in\mathcal Z}\frac{n_w a_w}{s+iw}.
\]

Its meromorphic continuation has a nonremovable pole at \(s=-iw\) for each active zero. A bound \(g(x)=O(e^{bx})\) with \(b<\alpha(q)\) would make the left side holomorphic in \(\Re s>b\), contradicting such a pole. Multiplication by \((2h)^{-1}\), whose positive-ray exponential rate is exactly \(-\tfrac12\), shifts the exponent by \(-\tfrac12\). This argument does not require the supremum defining \(\alpha(q)\) to be attained.

**Real-ray Mellin bound.** Put

\[
\mathcal M u(s)=\int_{\mathbb R}u(x)e^{(s-1/2)x}\,dx,\quad
G(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),\quad
D_f(s)=\frac{\mathcal M f(s)}{G(s)},
\]

so \(\mathcal M\Phi(s)=\xi(s)=G(s)\zeta(s)\). From \(|q(x)|\le A_q e^{-\delta|x|}\), positivity of the full theta kernel, and \(e^{-\delta|x|}\le e^{-\delta x}\), for real \(\sigma>1+\delta\),

\[
|D_{\Phi q}(\sigma)|\le A_q\frac{\xi(\sigma-\delta)}{G(\sigma)}
=A_q\pi^{\delta/2}
\frac{(\sigma-\delta)(\sigma-\delta-1)}{\sigma(\sigma-1)}
\frac{\Gamma((\sigma-\delta)/2)}{\Gamma(\sigma/2)}\zeta(\sigma-\delta).
\]

Stirling’s Gamma-ratio estimate ([DLMF §5.11](https://dlmf.nist.gov/5.11#iii)) and \(\zeta(\sigma-\delta)\to1\) yield

\[
\boxed{D_{\Phi q}(\sigma)=O_q(\sigma^{-\delta/2})\quad(\sigma\to+\infty,\ \sigma\in\mathbb R).}
\]

This is a bound on the real ray for each fixed state. It does not assert an absolute Dirichlet-series representation or a uniform half-plane bound for the Mellin quotient.

## Limits of the inference

The derivative estimate gives \(g(x)=2h(x)q(x)=O_q(e^{ax})\) for \(x\ge0\), while the exact exponent is \(\tau(g)=\alpha(q)\le a\). It does not give strict relative descent

\[
\exists\eta_q>0:\quad g(x)=O_q(e^{(\alpha(q)-\eta_q)x}),
\]

which would contradict the exact activity exponent. Thus the updated strip alone does not eliminate any nonzero low state.

The original fixed probe in the OpenAI proof retains its own low-end target; see the [fixed September 30, 2026 manuscript version](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex). Its stated estimate \(|J_\eta(Z)|\ll Z^{3/16+\epsilon}\) would need an additional \(3/8\) power saving to reach \(Z^{-3/16+\epsilon}\). The improved strip theorem supplies neither that probe estimate nor the required arithmetic correlation bound. The earlier high-end estimate was proved under \(\beta_*>7/8\), hence \(\kappa=2\beta_*-1>3/4\). If one targets \(\sigma_0<B\), a contradictory \(\beta_* > \sigma_0\) may lie in \((\sigma_0,B]\), outside that high-end range. The new zero-free boundary alone does not provide the needed principal-term bound, error savings, or uniform continuation margin there; those conclusions must come from a separate comparison theorem. This note does not modify the later [restored-observation comparison](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/56e046abb54183142813cb6f72cd6f1576ffe6e6/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md), whose own safe-line and whole signed cross-class requirements remain in force.

## Formal verification scope

The [pinned correspondence entry](https://github.com/liubaiying101/Slightly-improved-zero-free-half-planes-for-the-quasi-Riemann-hypothesis/blob/7d10420de90efa2f082a06a342fc7accbd57ab37/CombinedPaperVerification.lean) maps the rational and algebraic endpoints to explicit Hecke, Dirichlet, and zeta nonvanishing declarations. The 22 named declarations in that entry were replayed by Lean’s kernel at trust zero after restoring the missing source closure and expected module layout; their reported dependencies are only `propext`, `Classical.choice`, and `Quot.sound`. The Lean mathematical source files were unchanged. The raw public checkout does not directly contain all of the verifier’s required vendor/module layout, so this replay does not claim one-command verification from an untouched checkout. It verifies those 22 declarations, not every line of the manuscript or its broader optimality expectation.

Independent mathematical review: [REFEREE.md](REFEREE.md). The fixed-input arguments used here are the general parameter versions of Propositions 1–3 in [the original selection bridge](../20261011_qrh_selection_bridge/REPORT.md).
