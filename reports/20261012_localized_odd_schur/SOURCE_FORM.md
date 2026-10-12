# Exact odd source form and its neutral theta mode

Use the complete theta kernel and source identity proved in
[ORIGINAL_FORM_FOUNDATION.md](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md).
With \(\widehat f(t)=\int f(x)e^{itx}\,dx\), put
\[
a(t)=\operatorname{Re}\psi(1/4+it/2)-\log\pi=b(t)-C_0,
\quad C_0=\gamma+\pi/2+3\log2+\log\pi,
\]
\[
b(t)=\sum_{j\ge0}\frac{(t/2)^2}
 {(j+1/4)((j+1/4)^2+(t/2)^2)}\ge0,
\quad \kappa(u)=\frac{e^{-u/2}}{1-e^{-2u}}\quad(u>0),
\quad \alpha_n=\frac{\Lambda(n)}{\sqrt n}.
\]
The maximal Gamma form is
\[
\mathfrak g[f]=\frac1{2\pi}\int b(t)|\widehat f(t)|^2dt
 =\frac12\iint\kappa(|x-y|)|f(x)-f(y)|^2dxdy.
\]
For odd complex functions supported in \((-a,a)\), define the closed
polar-inclusive source form
\[
\begin{split}
\mathfrak A_a[f]={}&\mathfrak g[f]-C_0\|f\|_2^2
-2\sum_{2\le n<e^{2a}}\alpha_n\operatorname{Re}
 \int\overline{f(x)}f(x+\log n)dx\\
&-2\left|\int\sinh(x/2)f(x)dx\right|^2.
\end{split}                                                   \tag{1}
\]
Its natural domain is the maximal finite-Gamma-energy domain with this
support and parity. The prime sum is finite and every term is bounded;
the polar functional is bounded on this fixed window. Consequently (1)
is a closed semibounded form with a self-adjoint associated operator.
Write \(A_{k+1}\) for that operator when
\(a=a_{k+1}=\frac12\log(k+1)\). The coefficient of the polar term is
exactly \(2\). These definitions specify the operator used below;
the repository's original even weighted operator \(H\) is a distinct
realization.

On the theta-source class the complete source expression is
\[
T=a(D)-S,\qquad Sf(x)=\sum_{n\ge2}\alpha_n
 \{f(x+\log n)+f(x-\log n)\},\qquad
T\Phi=-\cosh(x/2).
\]
Here \(a(D)\) means the Fourier multiplier with symbol \(a(t)\).
No global closed unweighted \(L^2\) realization of \(T\) is asserted.
The source sums converge locally normally on each fixed theta
derivative. Thus the real odd function
\[
f_0=\Phi'''-\tfrac14\Phi'
\]
satisfies \(Tf_0=0\), since the same differential polynomial annihilates
\(\cosh(x/2)\). It is nonzero, smooth, and has double-exponential tails.
Integration by parts also gives
\[
\int\sinh(x/2)f_0(x)dx=0.
\]

Fix a real even smooth cutoff family with \(0\le\chi_k\le1\), equal
to one on \(|x|\le a_k-1/k\), zero on \(|x|\ge a_k\), and fixed bounds
\(\|\chi_k^{(j)}\|_\infty\le C_j k^j\). Set
\(g_k=\chi_kf_0\), \(r_k=(1-\chi_k)f_0\). For these particular functions,
the complete prime correlations and mixed pairings converge absolutely:
a large shift forces a factor into a double-exponential tail. Therefore
the symmetric source form may be paired with \(f_0=g_k+r_k\); the exact
null identity implies
\[
q_T[g_k]=q_T[r_k].                                      \tag{2}
\]
Although the compact-support form (1) has only its finite nonzero prime
sum, the full tail form and the null-identity pairings in (2) retain
every prime power. Their convergence uses the theta tails, not merely
membership in the Schwartz class.

The quantitative energy bounds for (2) are proved in
[the narrow-tail report](../20261012_narrow_theta_tail/REPORT.md).
The exact old/collar domain decomposition is proved in
[SHARP_WINDOW_DOMAIN.md](SHARP_WINDOW_DOMAIN.md).
