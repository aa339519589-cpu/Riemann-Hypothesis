# Fixed-finite theta jet tail frame

## Scope and conclusion

Fix an integer \(d\ge1\). For \(j=0,\ldots,d-1\), let
\[
f_j=D^{2j}f_0,\qquad f_0=(D^3-D/4)\Phi.
\]
These are genuine odd source zero modes: the exact theta source identity is \(T\Phi=-\cosh(x/2)\), \(T\) commutes with derivatives on this theta-source class, and
\[
Tf_0=(D^3-D/4)(-\cosh(x/2))=0,\qquad Tf_j=D^{2j}Tf_0=0.
\]
This uses the source identity with the complete prime-power sum. It is not a claim that the formal source \(T\) is a closed operator on unweighted \(L^2\).

Let \(a_k=\frac12\log k\), \(U=\pi k\), \(R_k=a_k-k^{-1}\), and \(s=u-U\), \(u=\pi e^{2x}\), on the positive tail. Let \(\eta_k=1-\chi_k\), where \(\chi_k\) has the narrow-cutoff properties in ../20261012_narrow_theta_tail/NARROW_TAIL_LOWER.md: \(0\le\eta_k\le1\), \(\eta_k=0\) for \(|x|\le R_k\), and \(\eta_k=1\) for \(|x|\ge a_k\). In particular, \(\eta_k=1\) for \(s\ge0\), and \(\eta_k'\) is supported in the transition with \(\|\eta_k'\|_\infty\le Ck\).

For this fixed \(d\), there are constants \(C_d<\infty\), \(\delta_d>0\), and \(K_d\) such that, for every \(k\ge K_d\) and every \(f\in\operatorname{span}_{\mathbb C}\{f_0,\ldots,f_{d-1}\}\), the cut tail \(r=\eta_k f\) satisfies
\[
\boxed{
\|\mathbf1_{\{|x|\ge a_{k+1}\}}r\|_2^2\ge\delta_d\|r\|_2^2,\qquad
\|r\|_1^2\le\frac{C_d}{k}\|r\|_2^2,\qquad
\|r'\|_2\le C_d k\|r\|_2.
}
\tag{1}
\]
Norm constants also depend on the fixed cutoff derivative bounds. The constants may deteriorate with \(d\); no uniform-in-\(d\) assertion is made. These are tail-frame estimates, not a positivity or inverse-weighted Schur statement.

## Exact theta jets and their leading coefficients

Set \(u=\pi e^{2x}\). There are polynomials \(\mathcal F_j\) such that
\[
f_j(x)=e^{x/2}\sum_{m\ge1}\mathcal F_j(m^2u)e^{-m^2u}.
\tag{2}
\]
For \(j=0\),
\[
\mathcal F_0(u)=F_1(u)=-32u^5+360u^4-1056u^3+810u^2-90u.
\]
If \(D_x\{e^{x/2}P(u)e^{-u}\}=e^{x/2}(\mathscr DP)(u)e^{-u}\), then
\[
\mathscr DP=\tfrac12P+2u(P'-P),\qquad \mathcal F_{j+1}=\mathscr D^2\mathcal F_j.
\]
Each application of \(\mathscr D\) raises degree by one and multiplies the leading coefficient by \(-2\). Thus
\[
\deg\mathcal F_j=5+2j,\qquad
\mathcal F_j(u)=-32\,4^j u^{5+2j}+O_d(u^{4+2j}).
\tag{3}
\]
For \(u\) large, \(\mathcal F_0(u)\ne0\) and all the \(\mathcal F_0(m^2u)\) summands have the tail sign already established in the lower-bound note.

Write
\[
\Theta_j(u)=\sum_{m\ge1}\mathcal F_j(m^2u)e^{-m^2u},
\qquad
R_j(u)=\frac{\mathcal F_j(u)}{\mathcal F_0(u)}.
\]
For each fixed \(d\) and every fixed derivative order \(q\),
\[
\frac{f_j(x)}{f_0(x)}
=R_j(u)+\epsilon_j(u),\qquad
|\epsilon_j^{(q)}(u)|\le C_{d,q}u^{M_{d,q}}e^{-3u}
\quad(u\ge U_d).
\tag{4}
\]
Indeed, factor out the \(m=1\) exponential in (2). The remaining \(m\ge2\) terms contain \(e^{-(m^2-1)u}\le e^{-3u}\), and their polynomial factors and any fixed number of derivatives are summable uniformly after factoring out a fixed power of \(u\). Also \(\mathcal F_0(u)\asymp u^5\), so division by the \(m=1\) denominator preserves this exponential error.

From (3),
\[
R_j(u)=4^j u^{2j}+O_d(u^{2j-1}),
\quad
\frac{R_j^{(\ell)}(U)}{\ell!}
=4^j\binom{2j}{\ell}U^{2j-\ell}
 +O_d(U^{2j-\ell-1})
\tag{5}
\]
for \(0\le j,\ell\le d-1\). If \(\ell>2j\), the displayed binomial coefficient is zero and the stated error remains valid. The matrix
\[
B_{\ell j}=4^j\binom{2j}{\ell},\qquad 0\le\ell,j\le d-1,
\tag{6}
\]
is invertible: after nonzero column scaling by \(4^j\), it is the evaluation matrix of the degree-\(\ell\) polynomials \(\binom{x}{\ell}\) at the distinct nodes \(x=0,2,\ldots,2d-2\). Equivalently, its determinant is a nonzero scaled Vandermonde determinant.

## Normalized polynomial tail basis

Define the \(d\times d\) Taylor matrix
\[
M(U)_{\ell j}=\frac{R_j^{(\ell)}(U)}{\ell!}.
\]
By (5),
\[
M(U)=\operatorname{diag}(U^{-\ell})\,
       (B+O_d(U^{-1}))\,
       \operatorname{diag}(U^{2j}).
\tag{7}
\]
It is therefore invertible for all sufficiently large \(U\). For each \(\ell=0,\ldots,d-1\), choose
\[
c^{(\ell)}(U)=M(U)^{-1}e_\ell.
\]
Then \(c_j^{(\ell)}(U)=O_d(U^{\ell-2j})\), and the rational m=1 profile
\[
\phi_{\ell,U}(s)=\sum_{j=0}^{d-1}c_j^{(\ell)}(U)R_j(U+s)
\]
has the exact Taylor jet \(\phi_{\ell,U}^{(q)}(0)/q!=\mathbf1_{\{q=\ell\}}\) for \(0\le q\le d-1\).

The combinations can be arranged to have coefficients polynomial in \(U=\pi k\). For clarity, put
\[
\mathcal Q(U)_{\ell j}
=\mathcal F_0(U)^{\ell+1}M(U)_{\ell j}.
\]
Every entry of \(\mathcal Q(U)\) is polynomial in \(U\), since the \(\ell\)-th derivative of \(\mathcal F_j/\mathcal F_0\) has denominator at most \(\mathcal F_0^{\ell+1}\). Its determinant is nonzero for large \(U\), by (7). The polynomial vector
\[
p^{(\ell)}(U)
=\operatorname{adj}(\mathcal Q(U))\,\mathcal F_0(U)^{\ell+1}e_\ell
\]
satisfies \(M(U)p^{(\ell)}(U)=(\det\mathcal Q(U))e_\ell\). Thus the polynomial-coefficient combination \(\sum_jp_j^{(\ell)}(U)f_j\), after division by the common scalar \(\det\mathcal Q(U)\), has m=1 profile with Taylor jet \(s^\ell\). Rescaling basis vectors by this nonzero scalar does not change their span.

For completeness, these normalized profiles converge on the whole exponentially weighted tail, not only on bounded \(s\)-intervals. On \(s\ge-2\pi\), for \(s\le U/2\), Taylor's formula and the derivative bounds
\[
|R_j^{(q)}(v)|\le C_{d,q}v^{2j-q}\qquad(v\ge U/2)
\]
give
\[
|\phi_{\ell,U}(s)-s^\ell|
 \le C_d U^{\ell-d}|s|^d,\qquad
|\phi_{\ell,U}'(s)-\ell s^{\ell-1}|
 \le C_d U^{\ell-d}|s|^{d-1},
\tag{8}
\]
with the derivative target interpreted as \(0\) for \(\ell=0\). For \(d=1\), \(R_0\equiv1\) and the derivative assertion is immediate; for \(d\ge2\) it is the Taylor remainder for \(\phi_{\ell,U}'\). Since \(\ell\le d-1\), the right sides are \(O_d(U^{-1})\) times fixed powers of \(s\). On \(s\ge U/2\), the coefficient estimate and rational growth give
\[
|\phi_{\ell,U}^{(q)}(s)|\le C_d U^\ell(1+s/U)^{2d+2},
\qquad q=0,1,
\]
which is polynomial in \(U,s\) and hence negligible in all the indicated norms against \(e^{-s}\) or \(e^{-2s}\). The true full-theta profile differs from \(\phi_{\ell,U}\), with its first \(s\)-derivative, by at most
\[
C_d U^{M_d}(1+s/U)^{M_d}e^{-3(U+s)}
\]
for \(s\ge-2\pi\), after increasing \(M_d\) if needed. This follows from (4), the coefficient bounds, and \(u=U+s\); the polynomial factor is harmless against the exponential. Consequently, for each fixed polynomial weight exponent \(A\),
\[
\frac{g_{\ell,U}(x)}{f_0(x)}
\longrightarrow s^\ell
\]
in \(L^2([-2\pi,\infty),(1+s_+)^A e^{-2s}ds)\), in \(L^1([-2\pi,\infty),(1+s_+)^A e^{-s}ds)\), and for the first \(s\)-derivative in the analogous \(L^2\) space. Here \(g_{\ell,U}=\sum_jc_j^{(\ell)}(U)f_j\), \(s_+=\max(s,0)\). The convergence is uniform over bounded coefficient vectors in this fixed \(d\)-dimensional frame.

## Full-theta Gram matrices and the exterior tail fraction

The lower transition endpoint corresponds to
\[
s_R=Ue^{-2/k}-U=\pi k(e^{-2/k}-1)>-2\pi,
\qquad s_R\longrightarrow-2\pi.
\tag{9}
\]
The exterior endpoint \(x=a_{k+1}=\frac12\log(k+1)\) corresponds exactly to
\[
u=\pi(k+1)=U+\pi,\qquad s=\pi.
\tag{10}
\]
For \(x\) corresponding to \(u=U+s\), the full theta asymptotic (3) gives
\[
|f_0(x)|^2\,dx
=C_* U^{19/2}e^{-2U}
 (1+s/U)^{19/2}e^{-2s}(1+o_d(1))\,ds,
\quad C_*=\frac{512}{\sqrt\pi},
\tag{11}
\]
uniformly on bounded \(s\)-intervals. On all \(s\ge s_R\), its normalized density is bounded by
\[
C_d(1+s_+)^{19/2}e^{-2s}.
\tag{12}
\]
Similarly, the \(L^1\) density \(|f_0(x)|dx\), after division by \(U^{17/4}e^{-U}\), converges locally to a positive constant times \(e^{-s}ds\) and is bounded by \(C_d(1+s_+)^{17/4}e^{-s}\).

Let \(g_{\ell,U}\) be the normalized full-theta basis above and write any \(f\) in the jet span as
\[
f=\sum_{\ell=0}^{d-1}\beta_\ell g_{\ell,U},\qquad
P_\beta(s)=\sum_{\ell=0}^{d-1}\beta_\ell s^\ell.
\]
The weighted profile convergence and (11)–(12) show that, after dividing positive-tail squared norms by \(U^{19/2}e^{-2U}\), the full-tail Gram matrix on \(x\ge R_k\) converges to
\[
C_*\left(\int_{-2\pi}^{\infty}s^{\ell+m}e^{-2s}\,ds\right)_{\ell,m<d}.
\]
The Gram matrix on \(x\ge a_{k+1}\) converges to
\[
C_*\left(\int_{\pi}^{\infty}s^{\ell+m}e^{-2s}\,ds\right)_{\ell,m<d}.
\]
Both matrices are positive definite: a nonzero polynomial cannot vanish almost everywhere on either interval. Since \(d\) is fixed, their eigenvalues vary continuously and the unit coefficient sphere is compact. Therefore there is \(\delta_d>0\) such that, for all sufficiently large \(k\),
\[
\int_{a_{k+1}}^\infty |f(x)|^2\,dx
\ge \delta_d\int_{R_k}^\infty |f(x)|^2\,dx
\qquad(f\in\operatorname{span}\{f_0,\ldots,f_{d-1}\}).
\tag{13}
\]
Oddness doubles both sides for the two-sided tails.

For \(r=\eta_k f\), \(\eta_k=1\) on \(|x|\ge a_k\), so \(r=f\) on \(|x|\ge a_{k+1}\); and \(0\le\eta_k\le1\) with support in \(|x|\ge R_k\). Hence
\[
\|\mathbf1_{\{|x|\ge a_{k+1}\}}r\|_2^2
\ge\delta_d\|r\|_2^2,
\tag{14}
\]
which is the exterior-frame assertion in (1). We also need the two-sided comparison
\[
\|r\|_2^2
\ge \|\mathbf1_{\{|x|\ge a_{k+1}\}}f\|_2^2
\ge \delta_d\|\mathbf1_{\{|x|\ge R_k\}}f\|_2^2,
\qquad
\|r\|_2^2\le\|\mathbf1_{\{|x|\ge R_k\}}f\|_2^2.
\tag{14a}
\]
The first inequality uses \(r=f\) on the exterior; the last uses \(0\le\eta_k\le1\).

## Uniform \(L^1/L^2\) and \(H^1/L^2\) bounds for cut combinations

The same finite-frame convergence gives, uniformly over \(f\) in the fixed jet span,
\[
\|f\|_{L^1(|x|\ge R_k)}
\le C_d U^{17/4}e^{-U}\|\beta\|_{\mathbb C^d},
\qquad
\|f\|_{L^2(|x|\ge R_k)}
\ge c_d U^{19/4}e^{-U}\|\beta\|_{\mathbb C^d}.
\tag{15}
\]
The first estimate follows from the weighted \(L^1(e^{-s})\) profile bound; the second follows from positive definiteness of the full-tail Gram matrix. Because \(|r|\le|f|\) on the tails and (14a) supplies \(\|r\|_2^2\ge\delta_d\|f\|_{L^2(|x|\ge R_k)}^2\),
\[
\|r\|_1^2
\le C_d U^{17/2}e^{-2U}\|\beta\|^2
\le \frac{C_d}{U}\|r\|_2^2
\le\frac{C_d}{k}\|r\|_2^2.
\tag{16}
\]

For derivatives, \(f=f_0 P_{k,\beta}(s)\), where \(P_{k,\beta}\) and its first \(s\)-derivative have uniformly bounded weighted profile norms relative to \(\|\beta\|\). On \(x\ge R_k\),
\[
\frac{|f_0'(x)|}{|f_0(x)|}\le C u,\qquad \frac{ds}{dx}=2u.
\]
Thus
\[
f'(x)=f_0'(x)P_{k,\beta}(s)
       +2u f_0(x)P_{k,\beta}'(s),
\]
and the weighted profile bounds imply
\[
\|f'\|_{L^2(|x|\ge R_k)}
\le C_d U^{23/4}e^{-U}\|\beta\|
\le C_d k\,\|f\|_{L^2(|x|\ge R_k)}.
\tag{17}
\]
For the cutoff \(r=\eta_kf\),
\[
\|r'\|_2
\le\|f'\|_{L^2(|x|\ge R_k)}
   +\|\eta_k'\|_\infty\|f\|_{L^2(R_k\le|x|\le a_k)}
\le C_d k\,\|r\|_2,
\tag{18}
\]
using \(\|\eta_k'\|_\infty\le Ck\), the finite-frame tail comparison, and (14a) to compare \(\|r\|_2\) below by the full-tail norm of \(f\). Equations (14), (16), and (18) prove (1).

## Limits of the finite-frame result

For each fixed \(d\), the first \(d\) true theta jets have a polynomial tail frame with positive exterior fraction, \(L^1/L^2\) concentration at scale \(k^{-1}\), and \(H^1/L^2\) scale \(k\). The constants \(\delta_d,C_d\) depend on the finite-dimensional polynomial Gram matrices and may deteriorate as \(d\to\infty\). No infinite-jet frame, infinite-dimensional tail compactness, sign control for arbitrary jet combinations, positivity of the full form, inverse-weighted coupling, or RH conclusion is asserted.
