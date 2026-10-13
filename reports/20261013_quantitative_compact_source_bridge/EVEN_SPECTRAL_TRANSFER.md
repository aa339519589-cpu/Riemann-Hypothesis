# Quantitative transfer from odd Green excess to even physical negative depth

Assume the complete odd Green operator has an actual eigenvalue \(\lambda>1\). The [compact-source construction](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/125fd9c46cada4157f884f1298c618df25bb7f8a/reports/20261013_quantitative_compact_source_bridge/REPORT.md) produces a real compact odd negative source, with two zero pole moments and specified size bounds. This note converts those bounds into an explicit strictly positive lower bound for the depth of a negative eigenvalue of the original even operator on its ground-orthogonal space.

The conversion keeps the full Gamma form and every prime power. It uses no bounded similarity between the odd Green completion and physical even \(L^2\), and no regularity assumption on the unsmoothed Green source. It does not exclude \(\lambda>1\), prove the coefficient-one comparison, or prove RH.

## 1. Statement using the published compact-source budgets

Use the normalization \(P[r]=1\) and put \(\gamma=\lambda-1>0\). Let \(R\), \(B_R\), and \(D\) be, respectively, the stopping radius, full-line source-norm bound, and weighted derivative-norm bound from equations (11), (8), and (20) of the cited compact-source report. Thus its real smooth odd source \(G\) satisfies
\[
\begin{gathered}
\operatorname{supp}G\subset[-R-1,R+1],\qquad
\int e^{x/2}G(x)\,dx=\int e^{-x/2}G(x)\,dx=0,\\
\mathcal W[G]\le-\gamma/2,\qquad
\|G\|_2\le B_R,\qquad
\left(\sum_{j=0}^2\int e^{2|x|}|G^{(j)}(x)|^2\,dx\right)^{1/2}\le D.
\end{gathered}                                                    \tag{1}
\]
These are upper bounds and a negative margin, not necessarily the actual norms or energy of \(G\).

Define
\[
\begin{aligned}
M_*&=4800D^2,\\
\sigma^2&=\max\left\{1,\frac{2}{15}\log\frac{16M_*}{\gamma}\right\},\\
T_{\rm tr}&=\max\left\{3\sigma,\ \sigma^2+
 \sigma\sqrt{\sigma^2+2\log\frac{32M_*}{\gamma}}\right\},\\
X&=R+1+T_{\rm tr},\\
\kappa_*&=\frac{\gamma\pi^2}{8B_R^2}
                  \exp\left(4X-\pi e^{2X}\right)>0.
\end{aligned}                                                    \tag{2}
\]
The logarithms are of positive arguments greater than one, as follows in the proof.

**Theorem.** There is a real compact smooth even physical vector \(v\perp e_0\) in the original operator domain with
\[
\frac{\langle v,Hv\rangle}{\|v\|_2^2}<-\kappa_*.
                                                                    \tag{3}
\]
Consequently the original even ground-orthogonal operator has a lowest negative eigenvalue \(-\kappa\), with \(\kappa\ge\kappa_*\).

Formula (2) is a symbolic quantitative interface. A decimal certificate requires certified values for the compact-source report's stopping rule and fixed theta integrals and tails. None is presumed here. The bound can be extremely small.

## 2. Original operator, source pairing, and the translated columns

Use the [original complete form](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md):
\[
 h(x)=\cosh(x/2),\quad m^2=\frac{\Phi}{2h},\quad e_0=2mh,\quad
 H=mLm,
\]
where, in source-pairing notation,
\[
 L=b(D)-C_0-S,\qquad
 b(t)=\sum_{j\ge0}\frac{2t^2}{a_j(a_j^2+t^2)},\quad a_j=2j+\tfrac12,
\]
\[
 C_0=\gamma_E+\frac\pi2+3\log2+\log\pi,\qquad
 S=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                 (\tau_{\log n}+\tau_{-\log n}).                    \tag{4}
\]
The physical weighted prime perturbation is bounded. No bounded unweighted source realization of \(S\) is assumed. Every source below is compact smooth, so the complete source correlations in (4) are well-defined. The Fourier convention is
\(\widehat f(z)=\int f(x)e^{izx}\,dx\), with real-line Plancherel measure \(dt/(2\pi)\).

For a source with both exponential moments zero, the complete Weil form is simply \(\mathcal W[f]=\langle f,Lf\rangle\); in general its polar correction is
\(2|\int hf|^2-2|\int\sinh(x/2)f|^2\). All scalar products are conjugate-linear in the first argument.

Write \(b_0=\gamma/2\) and \(b_G=-\mathcal W[G]\ge b_0\). For finite real \(t\), set
\[
 G_t(x)=G(x-t),\qquad E_t=\frac{G_t-G_{-t}}2,\qquad
 C(t)=\langle G_t,LG_{-t}\rangle.                                  \tag{5}
\]
Oddness of \(G\) makes \(E_t\) even. Its two pole moments remain zero. Each \(E_t/m\) is compact smooth, belongs to the original even operator domain, and is orthogonal to \(e_0\). This is a domain statement for each finite \(t\), not a bounded physical translation group.

Translation invariance of the complete source pairing and polarization give
\[
 \mathcal W[E_t]=\langle E_t/m,H(E_t/m)\rangle
       =-\frac{b_G}{2}-\frac{C(t)}2.                               \tag{6}
\]
The function \(C\) is real and even; \(C(0)=-b_G\).

## 3. Uniform control of the complete zero correlation

Let \(z\) run through all genuine zeros of \(\Xi(z)=\xi(1/2+iz)\), with distinct points weighted by their multiplicities \(j_z\). Both signs of the ordinates are included, and \(|\operatorname{Im}z|<1/2\). The complete polarized explicit formula, with the zero pole moments in (1), gives
\[
 C(t)=\sum_z j_z\widehat G(z)\overline{\widehat G(\overline z)}
                         e^{-2izt}.                               \tag{7}
\]
This is the full Guinand--Weil source formula in the normalization also used in [FINITE_HEIGHT_GAP.md, Part I, Section 4](../20261012_adaptive_spectral_tail/FINITE_HEIGHT_GAP.md). It does not restrict the zero sum to critical-line or simple zeros.

Put
\[
 A_G=\int e^{|x|/2}\bigl(|G|+|G'|+|G''|\bigr)\,dx.
\]
Cauchy--Schwarz, \(\int e^{-|x|}\,dx=2\), and the three derivative terms give
\[
 A_G\le\sqrt6\,D.                                                  \tag{8}
\]
Two integrations by parts, or the bound with no integration by parts at small ordinate, give uniformly for \(|\eta|\le1/2\)
\[
 |\widehat G(\nu+i\eta)|\le\frac{2A_G}{1+\nu^2}.                   \tag{9}
\]
For example, differentiate \(e^{-\eta x}G(x)\) twice; its \(L^1\) norm is bounded by \(A_G\), since \(2|\eta|\le1\) and \(\eta^2\le1\).

The elementary complete count from [FINITE_HEIGHT_GAP.md, Part I, Section 2](../20261012_adaptive_spectral_tail/FINITE_HEIGHT_GAP.md) is
\[
 N_\Xi(T)\le 2[10+(T+5)\log(T+5)],\qquad
 N_\Xi(T)\le8T\log T\quad(T\ge10).
\]
It follows from the original theta envelopes and Jensen's formula and is unconditional. In particular \(N_\Xi(10)<110\), while Stieltjes integration gives
\[
 \sum_{|\operatorname{Re}z|>10}j_z|\operatorname{Re}z|^{-4}
 \le32\int_{10}^\infty\frac{\log t}{t^4}\,dt<1.
\]
Hence
\[
 \sum_z\frac{j_z}{(1+(\operatorname{Re}z)^2)^2}<200.                \tag{10}
\]
Equations (8)--(10) imply
\[
 \sum_z j_z|\widehat G(z)\overline{\widehat G(\overline z)}|
       \le800A_G^2\le M_*,\qquad |C(t)|\le M_*e^{|t|}.              \tag{11}
\]
In particular \(b_0\le b_G\le M_*\), verifying the logarithms in (2).

For completeness, a small zero-free rectangle needed for the Gaussian estimate follows directly from the same theta bounds. On \(x\ge0\),
\[
 2\pi^2e^{9x/2-\pi e^{2x}}\le\Phi(x)
                    \le84e^{9x/2-\pi e^{2x}},
\]
and \(\Phi(x)\ge18e^{-5}\) on \([0,1/10]\). If \(|\nu|\le2\) and \(|\eta|\le1/2\),
\[
 \operatorname{Re}\Xi(\nu+i\eta)
    =2\int_0^\infty\Phi(x)\cos(\nu x)\cosh(\eta x)\,dx.
\]
The contribution of \([0,1/10]\) is at least \(1.8\exp(-5)\), since \(\cos(1/5)>1/2\). Negative contributions occur only beyond \(\pi/4>3/4\). Their total absolute value is at most
\[
\begin{aligned}
168\int_{3/4}^\infty e^{5x-3e^{2x}}\,dx
 &\le84\int_4^\infty u^2e^{-3u}\,du\\
 &=\frac{14280}{27}\exp(-12)<1.8\exp(-5).
\end{aligned}
\]
Here \(u=e^{2x}\), \(e^{3/2}>4\), and \(u^{3/2}\le u^2\) for \(u\ge4\). Thus every genuine zero satisfies
\[
 |\operatorname{Re}z|>2,\qquad \operatorname{Re}(z^2)>15/4.          \tag{12}
\]
No large-height zero computation is used in (12).

## 4. A finite translated negative direction

Let
\[
 p_\sigma(t)=\sqrt{2/\pi}\,\sigma^{-1}e^{-t^2/(2\sigma^2)},\qquad t\ge0.
\]
Real evenness of \(C\) identifies its half-Gaussian average with the whole-Gaussian average. Equation (11) permits absolute termwise integration in (7). The whole-Gaussian multiplier is \(e^{-2\sigma^2z^2}\), so (12) gives
\[
 \left|\int_0^\infty p_\sigma(t)C(t)\,dt\right|
 \le M_*e^{-15\sigma^2/2}\le b_0/8.                               \tag{13}
\]
Completing the square in the \(M_*e^t\) upper bound and using the elementary Gaussian Chernoff bound gives, for \(T=T_{\rm tr}\),
\[
\begin{aligned}
 \int_T^\infty p_\sigma(t)|C(t)|\,dt
 &\le2M_*e^{\sigma^2/2}
          e^{-(T-\sigma^2)^2/(2\sigma^2)}\\
 &\le b_0/8.                                                     \tag{14}
\end{aligned}
\]
Also \(T\ge3\sigma\) implies \(\int_0^T p_\sigma>3/4\). If \(C(t)\le-b_0/2\) for every \(t\in[0,T]\), its full average would be at most
\(-3b_0/8+b_0/8=-b_0/4\), contradicting (13). Therefore some finite \(t\le T\) obeys \(C(t)>-b_0/2\). Equation (6) then gives
\[
 \mathcal W[E_t]<-b_G/2+b_0/4\le-b_0/4=-\gamma/8.                  \tag{15}
\]
Only the source correlation was averaged. A Gaussian average of physical translated norms is not asserted or needed and may diverge. The physical norm is estimated after selecting this finite \(t\).

## 5. Physical norm and the spectral conclusion

For the selected \(t\), \(\operatorname{supp}E_t\subset[-X,X]\) and
\(\|E_t\|_2\le\|G\|_2\le B_R\). The original theta lower bound gives
\[
 m(x)^2\ge\pi^2\exp(4|x|-\pi e^{2|x|}).                            \tag{16}
\]
Its right side decreases as \(|x|\) increases. Thus
\[
 \|E_t/m\|_2^2\le\frac{B_R^2}{\pi^2}
                          \exp(-4X+\pi e^{2X}).                   \tag{17}
\]
Equations (15)--(17) prove (3).

The original operator is semibounded, its ground \(e_0\) is separated off, and its spectral projections on every interval bounded away from zero on the negative side have finite rank; see [ACTUAL_NEGATIVE_BAND_COVERAGE.md](../20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md). A strictly negative ground-orthogonal Rayleigh quotient therefore yields an actual lowest negative eigenvalue. This proves the theorem, with every physical vector used in the variational step in the original domain.

For fixed normalization data, (2) gives a quantitative relationship between a hypothetical odd Green excess and even physical negative depth. It supplies no favorable sign for the even actual-eigenstate low/tail mixed form and does not cancel its inverse-depth costs.

## 6. Interface conventions in the compact-source input

This note uses the primary `REPORT.md` at the fixed commit 125fd9c46cada4157f884f1298c618df25bb7f8a, where \(M=\|g/\mu\|_{L^2(0,\infty)}\), \(B=\|g_o\|_{L^2(\mathbb R)}\), and
\[
 Q_{\rm cut}=Q+8\pi U\mu_R M t_v(R),\qquad
 \|1_{|x|>R}g_o\|_2\le\sqrt2\,\mu_Rt_v(R).
\]
The companion `REFEREE.md` at that commit uses different letters \(V=\sqrt{C_{\rm ref}}\), \(B=UV\). In its cutoff discussion it prints \(8\pi U\mu_R B t_R\) and a positive-wing tail \(U\mu_Rt_R\). The corresponding bounds needed there are \(8\pi U\mu_R Vt_R\) and \(\mu_Rt_R\), respectively. The extra \(U\) is not used here. The primary report already states the correct variables and bounds; its construction and equations (1)--(20) require no change for the present transfer.
