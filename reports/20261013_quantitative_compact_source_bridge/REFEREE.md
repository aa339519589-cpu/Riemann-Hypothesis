# Independent audit: quantitative compact odd negative source

## Verdict

The construction is feasible for each fixed actual supercritical eigen-source. Starting with \(P[r]=1\), hence \(W[g_o]=-\gamma\), one can choose a finite interior cutoff, correct its single independent pole moment with a fixed smooth odd source, and mollify. The result is real, odd, compactly supported, has both pole moments zero, and can retain \(W\le-\gamma/2\) with an explicit exponentially weighted \(H^2\) bound. No \(H^1\) assumption on the original source is needed.

The radius-selection algorithm below uses the exact monotone tail functions from the source-tail report. The report's asymptotic envelope statements themselves contain generic theta constants and an unspecified validity threshold. Thus the recipe is symbolically explicit in those functions, but a numerical radius requires certified numerical upper bounds for them.

## Setup and constants

Scale the source to \(P[r]=1\), and put
\[
 \gamma=\lambda-1,\quad \delta=\gamma/\lambda,\quad
 g=\psi r,\quad g_o(x)=\operatorname{sgn}(x)g(|x|),\quad
 v=g/\mu.
\]
Then \(\ell_+(g)=\int_0^\infty \sinh(x/2)g(x)\,dx=0\) and \(W[g_o]=-\gamma\). Let
\[
 U=\|\mu\|_\infty,\qquad V=\sqrt{C_{\rm ref}},\qquad B=UV,\qquad
 Q\ge q_b[g_o].
\]
The full-line \(L^2\) norm of \(g_o\) is at most \(\sqrt2 B\), and \(\|v\|_2\le V\).

For an odd full-line source \(F\), use the pole-inclusive source form
\[
 W[F]=q_b[F]-C_0\|F\|_{L^2(\mathbb R)}^2
       +p[F]-2|\ell_{\rm full}(F)|^2.
\]
This agrees with the centered source identity when the pole moment is zero; the last term is the rank-one pole contribution \(-8|\ell_+(F|_+)|^2\), since \(\ell_{\rm full}=2\ell_+\). The positive-wing mass coefficient \(-2C_0\|g\|_2^2\) is exactly the full-line term \(-C_0\|g_o\|_2^2\).

Fix a real smooth compactly supported odd source \(h_o\), supported away from zero, with \(\ell_{\rm full}(h_o)=1\), where
\[
 \ell_{\rm full}(F)=\int_{\mathbb R}e^{x/2}F(x)\,dx.
\]
Write \(Q_h=q_b[h_o]\), \(H_v=\|h_+/\mu\|_2\), and \(H_0=\|h_o\|_2\). Such an \(h_o\) exists by taking a nonnegative smooth positive-wing bump and scaling it. Since it is supported away from zero, \(H_v<\infty\).

The bounded lower-order operator in the \(v\) variable has norm at most
\[
 M_0=2C_0U^2+
 4\sum_{n\ge2}\alpha_n a_n+
 2\sum_{n\ge2}\alpha_n b_n+
 8\|e_N\|_2^2,
\]
where \(a_n=\sup_{x\ge0}\mu(x)\mu(x+d_n)\), \(b_n=\sup_{0<x<d_n}\mu(x)\mu(d_n-x)\), \(e_N(x)=\sinh(x/2)\mu(x)\), and \(d_n=\log n\). The complete sums include prime powers and converge by the theta envelope.

## Explicit cutoff radius from the eigen-source tail functions

For \(R>0\), let
\[
 \mu_R=\sup_{x>R}\mu(x),\qquad E_R=\|1_{x>R}e_N\|_2,
\]
and use the exterior row coefficients
\[
 a_n^+(R)=\sup_{x>R}\mu(x)\mu(x+d_n),\quad
 a_n^-(R)=\sup_{x>\max(R,d_n)}\mu(x)\mu(x-d_n),\quad
 b_n(R)=\sup_{R<x<d_n}\mu(x)\mu(d_n-x),
\]
with \(b_n(R)=0\) if \(d_n\le R\). Define exactly as in the published tail estimate
\[
 D_\delta(R)=2C_0\mu_R^2+8E_R\|e_N\|_2+
 2\sum_{n\ge2}\alpha_n\left(a_n^+(R)+a_n^-(R)+(1-\delta)b_n(R)\right).
\]
These are nonincreasing tail functions and tend to zero. Testing the actual auxiliary eigen-equation gives the exterior weighted-variable bound
\[
 \|1_{x>R}v\|_2\le t_R:=\min\left(V,\frac{V\left(D_\delta(R)+4\pi U\mu_R\right)}{2\delta}\right).
\]
The \(4\pi U\mu_R\) term is the two-interface Carleman bound for the odd logarithmic kinetic cross term. In particular, \(\|1_{x>R}g\|_2\le\mu_Rt_R\), and the lost full-line pole moment is bounded by
\[
 c_R:=\ell_{\rm full}(1_{[-R,R]}g_o)\quad\text{(the signed correction coefficient)},\qquad
 m_R:=2E_Rt_R\quad\text{so }|c_R|\le m_R.
\]

Let \(F_R=1_{[-R,R]}g_o\). The jump-form split across the two cutoff interfaces, \(\|\mathsf C\|_{2\to2}=\pi\) for the Carleman kernel \(1/(u+v)\), and nonnegativity of the exterior kinetic form give
\[
 q_b[F_R]\le Q_{\rm cut}(R):=
 Q+8\pi U\mu_R V t_R.
\]
The constant \(8\pi\) includes the two interfaces and the factor two from polarizing the quadratic form. This is stronger than merely saying that the sharp cutoff is bounded in the form norm; it is what makes the negative margin quantitative.

The change in the bounded lower-order form on cutting is at most \(2M_0Vt_R\). Hence
\[
 W[F_R]\le W[g_o]+(2M_0+8\pi U\mu_R)Vt_R.
\]
Correct the lost moment by \(F_R^c=F_R-c_Rh_o\). It is odd and compactly supported, and \(\ell_{\rm full}(F_R^c)=0\). For odd sources,
\[
 \int_{\mathbb R}e^{-x/2}F(x)\,dx=-\ell_{\rm full}(F),
\]
so both pole moments vanish exactly. Cauchy–Schwarz for \(q_b\), and the \(M_0\) bound on the lower-order form, give
\[
 W[F_R^c]\le -\gamma+\Omega(R),
\]
where the explicit monotone error function is
\[
 \boxed{\;
 \Omega(R)=(2M_0+8\pi U\mu_R)Vt_R
 +2m_R\!\left(\sqrt{Q_{\rm cut}(R)Q_h}+M_0VH_v\right)
 +m_R^2\!\left(Q_h+M_0H_v^2\right).\;}
\]
Choose the least integer \(R\ge2\), with \(h_o\) supported in \((-1,1)\), for which \(\Omega(R)\le\gamma/4\). Every term is defined from \(\mu\), \(e_N\), the convergent full-prime row sums, \(C_{\rm ref}\), \(Q\), \(\lambda\), and fixed \(h_o\) data; monotone upper enclosures can therefore certify this stopping rule. The limit \(\Omega(R)\to0\) proves that the rule terminates for each \(\delta>0\). At that radius \(W[F_R^c]\le-3\gamma/4\).

## Mollifier width, finite prime labels, and retained margin

Fix an even nonnegative \(\eta\in C_c^\infty([-1,1])\) of mass one and set \(\eta_\epsilon(x)=\epsilon^{-1}\eta(x/\epsilon)\). For odd compactly supported \(f\), convolution preserves oddness and
\[
 \ell_{\rm full}(\eta_\epsilon*f)
 =\left(\int\eta_\epsilon(y)e^{y/2}\,dy\right)\ell_{\rm full}(f).
\]
Evenness of \(\eta\) makes the same multiplier apply to \(e^{-x/2}\). Thus both zero pole moments are preserved. Also \(|\widehat\eta(\epsilon t)|\le1\), so \(q_b[\eta_\epsilon*f]\le q_b[f]\).

The full-line odd-source identity for the prime term is
\[
 p[F]=-2\sum_{n\ge2}\alpha_n\operatorname{Re}
       \int_{\mathbb R}F(x)F(x+d_n)\,dx .
\]
It follows by writing the full-line shift correlation as \(2I_{\rm same}-I_{\rm reflected}\) for an odd source. If the support radius is at most \(R+1\), only \(n\le e^{2(R+1)}\) contribute. Therefore the lower-order source form on such supports has full-line operator norm at most
\[
 J_R=C_0+2\sum_{2\le n\le e^{2(R+1)}}\alpha_n.
\]
This verifies the proposed \(2\sum\alpha_n\) coefficient in the full odd-line normalization; the positive-wing formula's separate \(-4\) and \(+2\) terms must first be combined using oddness.

Set
\[
 B_R=\sqrt2\,B+m_RH_0,\qquad
 Q_R=\left(\sqrt{Q_{\rm cut}(R)}+m_R\sqrt{Q_h}\right)^2,\qquad
 a=\frac{\gamma}{8J_RB_R}.
\]
For any \(T\ge1\), Fourier splitting gives
\[
 \|\eta_\epsilon*F_R^c-F_R^c\|_2^2
 \le \epsilon^2T^2B_R^2+\frac{4Q_R}{\inf_{|t|\ge T}b(t)}.
\]
The explicit digamma series has the lower bound
\[
 b(t)=\sum_{k\ge0}\frac{(t/2)^2}
 {(k+1/4)((k+1/4)^2+(t/2)^2)}
 \ge \frac12\log(1+4t^2).
\]
The inequality follows by lower-bounding the decreasing summand sum by its integral from \(1/4\) to infinity. Choose
\[
 T=\exp(8Q_R/a^2),\qquad
 0<\epsilon\le\min\left(\frac12,\frac{a}{2TB_R}\right).
\]
Then the high-frequency term is at most \(a^2/2\), the low-frequency term at most \(a^2/4\), and the mollification error is at most \(a\). Since the lower-order form changes by at most \(2J_RB_Ra=\gamma/4\), the final source
\[
 F=\eta_\epsilon*F_R^c
\]
satisfies \(W[F]\le-\gamma/2\). Its support is contained in \([-(R+1),R+1]\).

## Exponentially weighted \(H^2\) bound

Put \(A_1=\|\eta'\|_1\), \(A_2=\|\eta''\|_1\), and define the squared weighted derivative norm by
\[
 \|F\|_{H^2(e^{2|x|})}^2
 :=\sum_{j=0}^2\int_{\mathbb R}e^{2|x|}|F^{(j)}(x)|^2\,dx.
\]
Young's inequality and the support bound give the explicit estimate
\[
 \boxed{\quad
 \|F\|_{H^2(e^{2|x|})}^2
 \le e^{2(R+1)}B_R^2
       \left(1+A_1^2\epsilon^{-2}+A_2^2\epsilon^{-4}\right).
 \quad}
\]
Thus the norm itself is at most \(e^{R+1}B_R\sqrt{1+A_1^2\epsilon^{-2}+A_2^2\epsilon^{-4}}\). No regularity of the unsmoothed source beyond its \(q_b\)-form and \(L^2\) bounds enters.

## Referee notes

The construction is nonuniform as \(\lambda\downarrow1\), because the tail radius depends on \(\delta^{-1}\) and the retained negative margin is proportional to \(\gamma\). The abstract stopping rule is explicit once exact monotone enclosures for \(D_\delta(R)\), \(\mu_R\), and \(E_R\) are provided. The published report's generic theta constants do not, on their own, give a numerical radius. This yields a regularized negative Weil-form witness conditional on the actual eigen-source; it proves no eigenvalue exclusion or RH conclusion.

## Normalization clarification

Here $V$ bounds $\|v\|_2$ and $B=UV$ bounds the positive-wing source norm. Accordingly, the source tail is $\mu_Rt_R$ and the kinetic cutoff error is $8\pi U\mu_R Vt_R$. An earlier version of this review included an extra $U$ in those two expressions. The primary report uses the correct bounds with the actual source norm $M$ and is unchanged by this correction. The same distinction is recorded in [the even spectral transfer, section 6](EVEN_SPECTRAL_TRANSFER.md).
