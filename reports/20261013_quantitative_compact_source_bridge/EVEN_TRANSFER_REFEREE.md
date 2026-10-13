# Independent audit: odd negative source to even physical negative depth

## Verdict

The transfer proof passes. I found no substantive defect in the source-to-zero correlation, the zero-free rectangle, the constants \(4800\), \(\sigma\), and \(T_{\rm tr}\), the finite-translate selection, or the physical Rayleigh quotient. The Gaussian average is taken only in the source correlation; no averaged physical norm is used. Every translated vector used after selecting \(t\) is compact smooth and in the physical domain.

I independently checked the sign in the complex zero coefficient. With the inner product conjugate-linear in its first slot, the polarized Weil formula for \(\langle G_t,LG_{-t}\rangle\) places the \(G_{-t}\) transform first. Since \(\widehat{G_t}(z)=e^{izt}\widehat G(z)\), this gives the factor \(e^{-2izt}\) in (7), as printed. Its whole-Gaussian multiplier is \(e^{-2\sigma^2z^2}\).

The scalar depth asymptotic should be stated one-sided. The available upper bound on \(D\) gives upper bounds on \(\sigma,T_{\rm tr},X\); it does not justify asymptotic equalities. With that wording, the proposed \(\exp(-C_\epsilon\gamma^{-4/3-\epsilon})\) lower bound is valid.

## Numerical and analytic checks

The source estimate \(A_G\le\sqrt6D\) follows from three Cauchy--Schwarz estimates with \(\int e^{-|x|}dx=2\). For \(|\eta|\le1/2\), applying the small-\(\nu\) \(L^1\) Fourier estimate and the large-\(\nu\) two-integration-by-parts estimate to \(e^{-\eta x}G(x)\) gives
\[
 |\widehat G(\nu+i\eta)|\le\frac{2A_G}{1+\nu^2}.
\]
The zero-count bound gives \(N_\Xi(10)<110\); the stated Stieltjes tail is below 1. Thus the sum in (10) is below 111, in particular below 200. The product estimate then gives
\[
 \sum_z j_z|\widehat G(z)\overline{\widehat G(\bar z)}|
 \le 4A_G^2\cdot200\le4800D^2=M_*.
\]
Since \(|\operatorname{Im}z|<1/2\), \(|e^{-2izt}|\le e^{|t|}\), proving (11). Also \(b_G\le M_*\) from \(C(0)=-b_G\), and \(b_G\ge b_0=\gamma/2\). Consequently \(16M_*/\gamma\ge8\) and \(32M_*/\gamma\ge16\), so the logarithms in (2) are positive.

For the zero-free box, the positive contribution on \([0,1/10]\) is at least
\[
 2(1/10)(18e^{-5})(1/2)=1.8e^{-5}.
\]
If \(|\nu|\le2\), the cosine cannot be negative before \(\pi/4>3/4\). Bounding the remaining absolute contribution by the cited theta envelope, using \(\pi>3\), \(u=e^{2x}\), \(e^{3/2}>4\), and \(u^{3/2}\le u^2\), gives
\[
 168\int_{3/4}^\infty e^{5x-3e^{2x}}dx
 \le84\int_4^\infty u^2e^{-3u}du
 =\frac{14280}{27}e^{-12}<1.8e^{-5}.
\]
Thus \(\operatorname{Re}\Xi(\nu+i\eta)>0\) throughout the closed box \(|\nu|\le2,|\eta|\le1/2\). Every zero therefore has \(|\operatorname{Re}z|>2\) and \(\operatorname{Re}(z^2)>4-1/4=15/4\). No zero-height computation is implicit.

The half-normal density \(p_\sigma\) integrates to one, and for an even \(C\), its half-line mean equals the whole \(N(0,\sigma^2)\) mean. Absolute convergence follows from (11) and the Gaussian weight, allowing the zero sum to be integrated termwise. The whole-Gaussian multiplier has modulus
\[
 |e^{-2\sigma^2z^2}|=e^{-2\sigma^2\operatorname{Re}(z^2)}
 \le e^{-15\sigma^2/2}.
\]
The first choice in (2) makes \(M_*e^{-15\sigma^2/2}\le\gamma/16=b_0/8\). Completing the square in \(p_\sigma(t)e^t\) gives the tail estimate in (14); the second choice of \(T_{\rm tr}\) makes its right side at most
\[
 2M_*e^{\sigma^2/2}
 e^{-(\sigma^2+2\log(32M_*/\gamma))/2}
 =\gamma/16=b_0/8.
\]
Also \(T_{\rm tr}\ge3\sigma\), so the half-normal mass on \([0,T_{\rm tr}]\) exceeds \(3/4\). If \(C(t)\le-b_0/2\) throughout this interval, its full mean would be at most \(-3b_0/8+b_0/8=-b_0/4\), contradicting the absolute mean bound \(b_0/8\). Therefore a finite \(t\le T_{\rm tr}\) has \(C(t)>-b_0/2\). Equation (6) then yields \(\mathcal W[E_t]<-b_0/4=-\gamma/8\).

The selected \(E_t\) is even. Both exponential moments remain zero under the translations and their linear combination, so its full-line cosh moment is zero. Hence \(E_t/m\perp e_0\). It is compact smooth and in the original domain. Its support is within \([-X,X]\), and \(\|E_t\|_2\le\|G\|_2\le B_R\). The lower bound (16) is decreasing with \(|x|\), so on the support
\[
 \|E_t/m\|_2^2\le B_R^2\pi^{-2}e^{-4X+\pi e^{2X}}.
\]
Together with \(\mathcal W[E_t]<-\gamma/8\), this gives exactly the \(\kappa_*\) in (2). The negative Rayleigh quotient and the cited finite-rank negative spectral projections imply an actual negative eigenvalue on \(e_0^\perp\).

## One-sided scalar consequence

Assume the sharpened compact-source construction supplies
\[
 D\le \exp\!\bigl(O(L/\log L)\bigr),\quad
 B_R=O(1),\quad R=O(\log L),\qquad L=\log(1/\gamma).
\]
Then
\[
 \log(16M_*/\gamma)\le L+O(L/\log L),\qquad
 \log(32M_*/\gamma)\le L+O(L/\log L),
\]
so the safe consequences are
\[
 \sigma^2\le(2/15+o(1))L,\qquad
 T_{\rm tr}\le(2/3+o(1))L,\qquad
 X\le(2/3+o(1))L.
\]
These are upper bounds; no lower bound on \(D\) is needed. For every fixed \(\epsilon>0\), they imply \(e^{2X}\le\gamma^{-4/3-\epsilon/2}\) for all sufficiently small \(\gamma\). Since \(B_R\) is bounded above and \(e^{4X}\ge1\),
\[
 \kappa_*\ge c\,\gamma\exp(-\pi\gamma^{-4/3-\epsilon/2})
 \ge \exp(-C_\epsilon\gamma^{-4/3-\epsilon})
\]
after increasing \(C_\epsilon\) and reducing the small-\(\gamma\) threshold. The constants depend on the fixed normalized source-tail bounds. This is a lower bound on the depth guaranteed by the transfer, not a new sign comparison or an eigenvalue exclusion.

The transfer theorem itself uses the fixed constants and functions already proved in the compact-source theorem. Effective numerical enclosures are needed only to produce a decimal value for \(\kappa_*\), not as an additional hypothesis for the asymptotic statement.
