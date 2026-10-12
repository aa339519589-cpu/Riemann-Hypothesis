# Essential negative spectral level after shorting the full true RH threshold kernel

Date: 2026-10-12. Status: rigorous analytic obstruction for a **fixed-(J,N) canonical lower comparator** of the original, unchanged full theta/Gamma/all-prime operator. Not an RH proof or a claim about negative spectrum of the true operator.

## Theorem

Use the original full even Hilbert space and selfadjoint operator
\[
H=B-V,\quad B=M_m b(D)M_m\geq0,\quad
\mathfrak b[u]=\int b(t)|\widehat{mu}(t)|^2dt/(2\pi),
\]
where \(m^2=\Phi/(2\cosh(x/2))\), \(m>0\) is bounded and decays to zero at infinity, \(V\) is the complete bounded prime/theta potential, and \(b\ge0\) is even, increasing for positive arguments, and unbounded. These exact statements, including the common operator domain, come from the original-operator report, not from RH.

Fix \(J\ge1,N\ge2\), and retain the **canonical** tail allowance
\[
\delta_N=\frac{20A_*}{9}(N+1)^2e^{-\pi(N+1)}>0,
\quad A_*=4\pi^2\frac{125}{121}.
\]
Put
\[
\begin{split}
c_J&=\sum_{j=0}^{J-1}(j+1/4)^{-1},\\
R_J(x)&=\sum_{j=0}^{J-1}e^{-(2j+1/2)|x|},\\
p_N(x)&=m(x)\sum_{n=2}^N\frac{\Lambda(n)}{\sqrt n}
                  [m(x+\log n)+m(x-\log n)],\\
T&=(c_J-C_0)M_{m^2}-M_{p_N}-M_m(R_J*)M_m,\\
A&=-\delta_NI+T,\qquad D=H-A.
\end{split}\tag{1}
\]
The exact prior defect identity, which pays for every omitted prime power and Gamma summand, gives \(D\succeq(\delta_N/4)I\) as a closed quadratic form. This follows from \(\|S_{>N}\|\le(3/4)\delta_N\) for the canonical allowance.

Let \(W\) be **any closed subspace of \(\ker H\)**, in particular \(W=\ker H\), with orthogonal projection \(P\) and inclusion \(i:W\to L^2_{\rm even}\). The zero-mode restriction is bounded:
\[
C=Di=\delta_N i-Ti,\quad
E=PC=\delta_N I_W-PTi\succeq(\delta_N/4)I_W.
\]
Define the bounded exact defect-shorting operator
\[
F_W=CE^{-1}C^*,\qquad K_{\varepsilon,W}=\varepsilon I+A+F_W.
\tag{2}
\]
As an exact energy projection, \(0\preceq F_W\preceq D\) on the original form domain, and \(F_Ww=Dw\) for all \(w\in W\). Thus \(K_{\varepsilon,W}\preceq H+\varepsilon I\), with equality on each selected true threshold mode.

**New result.** For every fixed \(J,N\), every closed \(W\subseteq\ker H\), and every real \(\varepsilon\),
\[
\boxed{F_W-\delta_N P\ \text{is compact},\qquad
\varepsilon-\delta_N\in\sigma_{\rm ess}(K_{\varepsilon,W}).}
\tag{3}
\]
The spectral assertion also holds for the compression to
\(W^\perp\cap g_0^\perp\), where \(g_0=\sqrt{2\Phi\cosh(x/2)}\) and
\(Hg_0=-g_0/2\). Hence for **each fixed \(J,N\)** and
\(0<\varepsilon<\delta_N\), the lower comparison has *infinite negative spectral index* even after correcting the **entire actual zero eigenspace** and removing the ground state. No such negative spectral conclusion is made for the true \(H\).

## Proof: compactness of the entire true kernel

Let \(P_0=P_{\ker H}\). For \(w\in\ker H\), \(\|w\|\le1\), the exact operator identity \(Bw=Vw\) implies
\[
\int b(t)|\widehat{mw}(t)|^2\,\frac{dt}{2\pi}
=\langle Vw,w\rangle\le\|V\|.\tag{4}
\]
Thus, uniformly over unit kernel vectors,
\[
\int_{|t|>T_0}|\widehat{mw}(t)|^2\,\frac{dt}{2\pi}
\le\frac{\|V\|}{b(T_0)}\longrightarrow0.\tag{5}
\]
The spatial tails also vanish uniformly:
\[
\int_{|x|>R}|mw|^2dx\le\sup_{|x|>R}m(x)^2\longrightarrow0.
\tag{6}
\]
Finally Plancherel gives
\[
\|mw(\cdot+h)-mw\|_2^2\le
h^2T_0^2\|m\|_\infty^2+\frac{4\|V\|}{b(T_0)}.\tag{7}
\]
Choose \(T_0\) large, then \(h\) small. Uniform spatial tightness, Fourier translation continuity, and \(L^2\) boundedness invoke the Kolmogorov-Riesz compactness criterion. Therefore \(M_mP_0\) is compact; consequently \(M_mP\) is compact for **every** closed \(W\subset\ker H\). This applies to the complete true kernel without any frame-completeness assumption.

In (1), \(p_N/m=\sum_{n=2}^N(\Lambda(n)/\sqrt n)[m(x+\log n)+m(x-\log n)]\) is bounded; \(R_J*\) is bounded with norm \(c_J\). Every summand of \(TP\) factors on the right through \(M_mP\), so \(TP\) and its adjoint \(PT\) are compact. Accordingly
\[
C=\delta_N i+\text{compact},\quad
E=\delta_N I_W+\text{compact},\quad
E^{-1}=\delta_N^{-1}I_W+\text{compact}.
\]
For the inverse use \(E^{-1}-\delta_N^{-1}I_W=\delta_N^{-1}E^{-1}(\delta_NI_W-E)\). Multiplication yields
\[
F_W=CE^{-1}C^*=\delta_N P+\text{compact}.
\tag{8}
\]
No compactness of \(P\) itself is asserted.

## Proof: an escaping Weyl sequence not captured by kernel shorting

For \(j\ge1\), let
\(I_j=(3j,3j+1)\cup(-3j-1,-3j)\).
The even functions supported in any fixed \(I_j\) form an infinite-dimensional Hilbert space. On **that fixed shell**, \(1/m\) is bounded, so
\(M_{\mathbf1_{I_j}}P=M_{\mathbf1_{I_j}/m}(M_mP)\) is compact, and by adjoints so is \(PM_{\mathbf1_{I_j}}\). An orthonormal sequence inside the shell is weakly null; its image under this compact operator tends to zero. Hence choose a normalized even \(u_j\) in shell \(I_j\) with
\[
\|Pu_j\|\le1/j.\tag{9}
\]
The different supports make \(u_j\) orthonormal and weakly null. For fixed \(J,N\), all the coefficients of \(T\) vanish on escaped inputs, and
\[
\|Tu_j\|\le |c_J-C_0|\sup_{I_j}m^2
+\sup_{I_j}|p_N|
+c_J\|m\|_\infty\sup_{I_j}m\longrightarrow0.\tag{10}
\]
Equation (8), compactness and (9) show \(\|F_Wu_j\|\to0\). Independently, this follows without (8): \(C^*u_j=\delta_NPu_j-PTu_j\to0\), then
\(\|F_Wu_j\|\le\|C\|\|E^{-1}\|\|C^*u_j\|\to0\).

It follows that
\[
[K_{\varepsilon,W}-(\varepsilon-\delta_N)I]u_j
=(T+F_W)u_j\longrightarrow0.\tag{11}
\]
Weyl's criterion for the bounded selfadjoint comparison proves the essential-spectral inclusion in (3). Since \(g_0\perp W\), and \(g_0\in L^2\) has vanishing mass in the escaping shells, the normalized projections of \(u_j\) to \(W^\perp\cap g_0^\perp\) differ from \(u_j\) by \(o(1)\). They are a singular sequence for the corresponding **compression**. A negative essential spectral point forces an infinite-dimensional negative spectral projection.

## Scope and audit

This fills a specific unclosed point in the existing countable-shorting discussion: for the **fixed** global-prime-tail comparison, the possible essential level \(-\delta_N\) really survives, even with shorting the whole true kernel. It is **not** a no-go theorem for \(N=N(\varepsilon)\) satisfying \(\delta_{N(\varepsilon)}\le\varepsilon\), a spatially localized tail allowance, or the sign-preserving full-prime Birman-Schwinger construction.

Checks: (i) the sign of the scalar comparator term is \(-\delta_NI\); (ii) \(E^{-1}\) acts only on the bounded zero-mode restriction, not on unbounded \(D\); (iii) compactness is derived for *all* \(w\in\ker H\) directly from \(Bw=Vw\); (iv) the bound for \(1/m\) is used separately on each fixed shell, never uniformly at infinity; (v) the weakly-null Weyl sequence proves **essential** rather than merely point spectrum; (vi) the compression is not asserted to reduce \(K\); (vii) no limits in \(N\) are exchanged with shell escape. All factors remain the exact original theta, full Gamma symbol, and complete prime terms in \(H\).

Sources inspected at main commit \`faff22f760ef85bb183e566b26d5504402a1fae5\`: \`reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md\`, \`ESSENTIAL_SPECTRUM.md\`, \`reports/20261012_diagonal_prime_threshold_no_go/REPORT.md\`, \`reports/20261012_threshold_shorted_certificates/COUNTABLE_CORRECTION.md\` and \`REFEREE_COUNTABLE_CORRECTION.md\`. Existing files remain untouched. No external referee or formal verification is claimed.

**NO NEW UNCONDITIONAL RH THEOREM PROVED.**
