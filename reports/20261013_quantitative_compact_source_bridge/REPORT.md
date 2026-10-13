# Compact smooth negative source from a supercritical Green eigen-source

This note uses the completed source equation, row-tail bound, and reference estimate in the [source-tail report](../20261013_supercritical_source_tails/REPORT.md) and [reference inverse report](../20261013_full_prime_green_reference/REFERENCE_INVERSE.md). If an eigen-source is complex-valued, take a nonzero real or imaginary part and renormalize; the source operator has real coefficients.

Date: 2026-10-13. The normalization and actual source domains are those of the [source-tail report](../20261013_supercritical_source_tails/REPORT.md); the signed source identity is in [SIGNED_ZERO_PAIRING.md](../20261013_supercritical_source_tails/SIGNED_ZERO_PAIRING.md). Every prime power is retained. The construction is conditional only on the hypothesized actual supercritical eigen-source.

## Quantitative construction

Let $g=\psi r$ be an actual centered Green eigen-source with $P[r]=1$, $N[r]=\lambda$, $\lambda>1$, and put
\[
 \gamma=\lambda-1,\qquad \delta=\frac{\lambda-1}{\lambda},\qquad
 v=g/\mu,\quad \mu^2=\psi/L.
\]
Write $f=g_o$ for its odd full-line extension, $M=\|v\|_{L^2(0,\infty)}$, $Q=q_b[f]$, $U=\|\mu\|_\infty$, and $B=\|f\|_{L^2(\mathbb R)}\le\sqrt2\,UM$. The cited reference and source-form estimates give $M^2\le C_{\rm ref}$ and $Q\le C_q$. For a full odd source $F$, the convention is $\ell(F)=\int_{\mathbb R}\sinh(x/2)F(x)dx$ and
\[
\mathcal W(F)=q_b[F]-C_0\|F\|_{L^2(\mathbb R)}^2-\sum_{n\ge2}\alpha_n\bigl(\langle F,\tau_{d_n}F\rangle+\langle F,\tau_{-d_n}F\rangle\bigr)-2|\ell(F)|^2.
\]
The eigen identity gives
\[
 \mathcal W(f)=1-\lambda=-\gamma.
\]
The construction below uses the actual $M,Q$; replacing them by the cited upper bounds gives a uniform prescription for every normalized source.

Let $\alpha_n=\Lambda(n)/\sqrt n$, $a_n=\sup_{x\ge0}\mu(x)\mu(x+d_n)$, $b_n=\sup_{0<x<d_n}\mu(x)\mu(d_n-x)$, and
\[
 e_N(x)=\sinh(x/2)\mu(x),\qquad \mu_R=\sup_{x>R}\mu(x).
\]
A bound for the norm of the entire bounded lower-order source form on the weighted variable is
\[
 M_0=2C_0U^2+4\sum_{n\ge2}\alpha_na_n+
             2\sum_{n\ge2}\alpha_nb_n+8\|e_N\|_2^2.
\tag{1}
\]
The sums are over every integer label with $\Lambda(n)\ne0$, so all prime powers are included. This follows from the operator representation of the shift, reflection, and rank-one terms in the source-tail report.

The quantities in (1) use the positive wing. In the full odd-line convention the mass term is $-C_0\|F\|_{L^2(\mathbb R)}^2=-2C_0\|F_+\|_{L^2(0,\infty)}^2$, and the remaining bounded terms act on $v=F_+/\mu$.

For the kinetic cutoff define the report's complete row bound by
\[
\begin{aligned}
D_\delta(R)={}&2C_0\mu_R^2
 +8\|\mathbf1_{x>R}e_N\|_2\|e_N\|_2\\
&+2\sum_{n\ge2}\alpha_n\left(a_n^+(R)+a_n^-(R)+(1-\delta)b_n(R)\right),\\
a_n^+(R)={}&\sup_{x>R}\mu(x)\mu(x+d_n),\\
a_n^-(R)={}&\sup_{x>\max(R,d_n)}\mu(x)\mu(x-d_n),\\
b_n(R)={}&\begin{cases}
\sup_{R<x<d_n}\mu(x)\mu(d_n-x),&d_n>R,\\
0,&d_n\le R.
\end{cases}
\end{aligned}
\tag{2}
\]
and set
\[
 E_N(R)=4\pi U\mu_R,\qquad
 t_v(R)=\min\!\left\{M,\frac{M[D_\delta(R)+E_N(R)]}{2\delta}\right\}.
\tag{3}
\]
The eigen-equation tail test proves $\|\mathbf1_{x>R}v\|_2\le t_v(R)$. The interface term $E_N(R)$ is the two-boundary Carleman estimate with kernel $\kappa(u+v)\le (u+v)^{-1}$, including the full odd-line factor. Therefore
\[
 \|\mathbf1_{|x|>R}f\|_2\le\sqrt2\,\mu_Rt_v(R),\qquad
 q_b[\mathbf1_{[-R,R]}f]\le Q+8\pi U\mu_RM t_v(R).
\tag{4}
\]
The second inequality uses the nonnegative discarded exterior kinetic energy and bounds the inside/outside cross term by the Carleman operator. It does not assume any Sobolev regularity of $f$.

The bounded lower-order form changes under this cutoff by at most $2M_0Mt_v(R)$: write $v=v_R+v_{>R}$ and polarize the bounded self-adjoint form, using $\|v_R\|,\|v\|\le M$. Hence for $F_R=\mathbf1_{[-R,R]}f$,
\[
 \mathcal W(F_R)\le-\gamma+
    [2M_0+8\pi U\mu_R]M t_v(R).
\tag{5}
\]
Here $\mathcal W$ on compact form-domain sources includes the polar rank-one term.

For example, an even nonnegative bump $\rho$ supported in $1/4<|x|<3/4$ gives $h=x\rho/\ell(x\rho)$, since its denominator is positive. Fix once and for all an odd $h\in C_c^\infty((-1,1))$, supported away from zero, with full-line moment
\[
 \ell(h):=\int_{\mathbb R}h(x)\sinh(x/2)\,dx=1.
\]
Set $H=\|h\|_{L^2(\mathbb R)}$, $H_v=\|h/\mu\|_{L^2(0,\infty)}$, and $Q_h=q_b[h]$. The cutoff source has a small residual moment:
\[
 m_R=2\|\mathbf1_{x>R}e_N\|_2t_v(R)\ \ge
       |\ell(F_R)|,
\tag{6}
\]
because the original centered source has zero full-line sinh moment. Correct it exactly by
\[
 U_R=F_R-\ell(F_R)h.
\tag{7}
\]
Then $U_R$ is odd and both full-line pole moments vanish. Define
\[
 Q_{\rm cut}=Q+8\pi U\mu_RMt_v(R),\quad
 B_R=B+m_RH,\quad
 Q_R=(\sqrt{Q_{\rm cut}}+m_R\sqrt{Q_h})^2.
\tag{8}
\]
The kinetic, mass/prime, and rank-one changes from the correction (7) are bounded by
\[
 C_{\rm corr}(R)=
 2m_R\!\left(\sqrt{Q_{\rm cut}Q_h}+M_0MH_v\right)
 +m_R^2\!\left(Q_h+M_0H_v^2\right).
\tag{9}
\]
Thus the fully explicit cutoff error function
\[
 \Omega(R)=[2M_0+8\pi U\mu_R]Mt_v(R)+C_{\rm corr}(R)
\tag{10}
\]
satisfies $\mathcal W(U_R)\le-\gamma+\Omega(R)$. All its terms are explicit tail suprema, integrals, and complete-prime sums from the source-tail report. They decrease to zero. Choose the first integer $R\ge2$ with
\[
 \Omega(R)\le\gamma/4.
\tag{11}
\]
This is a terminating, verifiable recipe, and it gives $\mathcal W(U_R)\le-3\gamma/4$. The report's theta envelopes also yield the simpler asymptotic upper bound
\[
 R=O\!\left(1+\log\log\left(2+\frac{C}{\gamma\delta}\right)\right)
 =O\!\left(1+\log\log\left(2+C\frac{1+\gamma}{\gamma^2}\right)\right)
 \quad(\gamma\downarrow0),
\tag{12}
\]
where the fixed $C$ depends on $C_{\rm ref},C_q,M_0$ and the theta-tail constants. Formula (10), rather than this envelope, defines the actual radius.

## Mollification and final bounds

Choose a fixed even, nonnegative $\eta\in C_c^\infty((-1,1))$ with $\int\eta=1$, and let $\eta_\varepsilon(x)=\varepsilon^{-1}\eta(x/\varepsilon)$. Even convolution preserves oddness and multiplies the full-line sinh moment by $\int\eta_\varepsilon(x)\cosh(x/2)\,dx$, so both moments of $\eta_\varepsilon*U_R$ remain zero. Also
\[
 q_b[\eta_\varepsilon*U_R]\le q_b[U_R]\le Q_R.
\tag{13}
\]
For full odd sources supported in $[-R-1,R+1]$, only labels $d_n\le2(R+1)$ enter the prime correlations. The finite full-line shift operator has norm at most $2\sum\alpha_n$, so a Lipschitz constant for the nonkinetic centered form is
\[
 J_R=C_0+2\sum_{n\le e^{2(R+1)}}\alpha_n.
\tag{14}
\]
Thus, for $G_\varepsilon=\eta_\varepsilon*U_R$,
\[
 \mathcal W(G_\varepsilon)
 \le\mathcal W(U_R)+J_R(\|G_\varepsilon\|_2+\|U_R\|_2)
                   \|G_\varepsilon-U_R\|_2,
\tag{15}
\]
because their kinetic difference is nonpositive by (13), and both rank-one terms vanish.

Set
\[
 a=\frac{\gamma}{8J_RB_R},\qquad
 T=\exp\!\left(\frac{8Q_R}{a^2}\right),\qquad
 \varepsilon=\min\!\left\{\frac12,\frac{a}{2TB_R}\right\}.
\tag{16}
\]
The explicit digamma series gives
\[
 b(t)=\sum_{k=0}^\infty
 \frac{(t/2)^2}{(k+1/4)((k+1/4)^2+(t/2)^2)}
 \ge\int_{1/4}^\infty\frac{(t/2)^2}{u(u^2+(t/2)^2)}\,du
 =\frac12\log(1+4t^2).
\tag{17}
\]
The summand is decreasing in $u$, which justifies the integral lower bound. Splitting at $|t|=T$, using $|\widehat\eta(\varepsilon t)-1|\le\varepsilon|t|$ at low frequencies and $|\widehat\eta-1|\le2$ at high frequencies, yields
\[
 \|G_\varepsilon-U_R\|_2^2
 \le(\varepsilon T)^2B_R^2+\frac{4Q_R}{b(T)}
 \le a^2.
\tag{18}
\]
The last inequality follows from $\varepsilon T B_R\le a/2$, $b(T)\ge\log(2T)$, and the definition of $T$. Equations (14)--(16) and (18) give a lower-order loss at most $\gamma/4$, so
\[
 \mathcal W(G_\varepsilon)\le-\gamma/2.
\tag{19}
\]
Taking $G=G_\varepsilon$ gives a compact smooth odd negative source with both pole moments zero, support in $[-R-1,R+1]$, and the requested lower bound.

For the weighted $H^2$ norm, $\|U_R\|_2\le B_R$ and $\operatorname{supp}G\subset[-R-\varepsilon,R+\varepsilon]\subset[-R-1,R+1]$. Young's inequality gives the explicit bound
\[
 \left(\int_{\mathbb R}e^{2|x|}
       \sum_{j=0}^2|G^{(j)}(x)|^2\,dx\right)^{1/2}
 \le e^{R+1}B_R
 \sqrt{1+\|\eta'\|_1^2\varepsilon^{-2}
          +\|\eta''\|_1^2\varepsilon^{-4}}.
\tag{20}
\]
The parameters in (16) make the dependence on $\gamma$, the normalized source norms $M,Q,B$, and the support cutoff $R$ explicit. Under $P[r]=1$, $M,Q,B$ are uniformly bounded by the cited reports. For a source with $P[r]=P_0$, first rescale it by $P_0^{-1/2}$, apply the normalized construction, and rescale the resulting $G$ by $P_0^{1/2}$; the Weil lower bound becomes $(\lambda-1)P_0/2$, while its weighted $H^2$ norm scales by $P_0$ after squaring. The stopping rule (11) uses the explicitly defined functions (1)--(10); no unspecified asymptotic constant enters that rule. Evaluating it at supplied numerical source bounds requires certified enclosures for the fixed theta integrals, suprema and complete-prime tails. Such a decimal certificate is not supplied here. The big-O radius estimate (12) is only a simpler asymptotic summary.

This is a compact-source consequence of a hypothetical supercritical eigenvector. It does not rule out $\lambda>1$.

## Sharper smoothing bound

The [exact-symbol smoothing appendix](SYMBOL_MOLLIFICATION.md), with its [independent audit](SYMBOL_MOLLIFICATION_REFEREE.md), replaces the mollification step above by a compact signed kernel whose Fourier multiplier lies in $[0,1]$. It preserves the same negative margin and pole moments. Under $P[r]=1$, its weighted $H^2$ norm is at most $C_\theta(\lambda-1)^{-\theta}$ for every fixed $\theta>0$ near threshold; the radius rule (11) is unchanged. This is an analytic bound, not a decimal enclosure certificate or an eigenvalue exclusion.
