# Positive box-null gauges, complete finite-mask domains, and optimal transport order

## 1. Statement and fixed objects

Let \(\Phi\) be the genuine even theta kernel, strictly decreasing on the positive half-line, and let \(\psi=-\Phi'>0\) there. Put
\[
 s(x)=\sinh(x/2),\quad
 \kappa(x)=\frac{e^{-x/2}}{1-e^{-2x}},\quad
 d_n=\log n,\quad \alpha_n=\frac{\Lambda(n)}{\sqrt n}.
\]
Use the original full-line source expression
\[
 T=a(D)-\sum_{n\ge2}\alpha_n(\tau_{d_n}+\tau_{-d_n}),
 \quad T\Phi=-\cosh(x/2),\quad T\psi=s/2,
 \quad \int_0^\infty s\psi=1/8.
\]
The exact conventions and complete source identity are those of
[the source-form foundation](../20261012_localized_odd_schur/SOURCE_FORM.md).
For an odd full-line source \(h\), write \(q[h]\) for its original polar-inclusive Weil source form, whose polar term is
\(-2|\int_{\mathbb R}sh|^2\). All prime powers have their genuine coefficients.

For \(Y>0\), define
\[
 \boxed{\quad
 w_Y(x)=\frac{\Phi(x-Y)-\Phi(x+Y)}{4\sinh(Y/2)}.
 \quad}                                                        \tag{1}
\]
This note proves:

1. \(w_Y\) is an explicit strictly positive odd null gauge with the exact original source and pole normalization.
2. Every finite even translation mask of an odd source in \(H^\sigma\), \(\sigma>1/2\), with finite original physical norm belongs to a sufficiently wide **adapted** \(P_{w_Y}\)-completion. This applies to the actual scalar supercritical sources covered by the verified bootstrap, with constants depending on fixed spectral depth and mask radius.
3. For a fixed compact smooth centered odd source \(g\), and
\(h_Y=g(\cdot-Y)+g(\cdot+Y)\),
\[
 \boxed{\quad
 P_{w_Y}[h_Y/w_Y]=e^Y A_g+2q[g]+o(1),\qquad
 A_g=\int_{\mathbb R}e^{u/2}\frac{|g(u)|^2}{\Phi(u)}du>0.
 \quad}                                                        \tag{2}
\]
This achieves the optimal exponential transport order \(e^Y\) uniformly over all positive normalized gauges. It is not a proof that the signed source form is nonnegative.

## 2. Exact positivity, nullity, and full-prime row control

For \(x,Y>0\), \(|x-Y|<x+Y\), so evenness and strict decrease of \(\Phi\) give \(w_Y(x)>0\). It is smooth and odd, with
\[
 w_Y'(0)=\frac{\psi(Y)}{2\sinh(Y/2)}>0,
 \qquad w_Y\longrightarrow\psi\quad(Y\downarrow0)
\]
locally with every derivative. The source identity for \(\Phi\) immediately gives
\[
 T w_Y=s/2.                                                    \tag{3}
\]
All shifted theta source sums converge locally normally, so this operation retains the complete prime sum.

Equivalently,
\[
 w_Y=k_Y*\psi,\qquad
 k_Y(u)=\frac{1_{[-Y,Y]}(u)}{4\sinh(Y/2)}.
\]
The exponential moment satisfies \(\int k_Y(u)e^{u/2}du=1\). Thus
\[
 \int_0^\infty s(x)w_Y(x)dx=\frac18.                           \tag{4}
\]
Also \(\int k_Y(u)e^{|u|/2}du\le2\), so, for \(j=0,1\),
\[
 \int_{\mathbb R}e^{|x|/2}|w_Y^{(j)}(x)|dx
 \le2\int_{\mathbb R}e^{|x|/2}|\psi^{(j)}(x)|dx.                \tag{5}
\]
The constant is independent of \(Y>0\).

The complete reflected row consequently satisfies the uniform bound
\[
 L_Y(x)=\sum_{d_n>x}\alpha_n w_Y(d_n-x)
 \le C_L e^{x/2}\qquad(x\ge0,\ Y>0).                          \tag{6}
\]
Indeed, Chebyshev's bound on \(\sum_{n\le X}\Lambda(n)\) bounds the total \(\alpha_n\)-mass in
\([x+k,x+k+1)\) by \(C e^{(x+k)/2}\). Sum the supremum of \(w_Y\) on each unit interval and use
\(\sup_I|f|\le\int_I(|f|+|f'|)\), followed by (5). This proof includes every prime power and is uniform in the gauge parameter.

## 3. The adapted positive forms and the unchanged signed form

For any positive odd gauge \(w\) satisfying (3)–(4), define on the original smooth compact even-extension ratio core
\[
\begin{aligned}
 P_{\Gamma,w}[r]&=\iint_{(0,\infty)^2}w(x)w(y)
 [\kappa(|x-y|)-\kappa(x+y)]|r(x)-r(y)|^2dxdy,\\
 P_{{\rm pole},w}[r]&=4\iint w(x)s(x)w(y)s(y)|r(x)-r(y)|^2dxdy,\\
 P_{F,w}[r]&=2\sum_{n\ge2}\alpha_n\int_0^\infty w(x)w(x+d_n)
 |r(x)-r(x+d_n)|^2dx,\\
 N_w[r]&=\sum_{n\ge2}\alpha_n\int_0^{d_n}w(x)w(d_n-x)
 |r(x)-r(d_n-x)|^2dx,\\
 P_w&=P_{\Gamma,w}+P_{{\rm pole},w}+P_{F,w}.
\end{aligned}                                                  \tag{7}
\]
Every component is nonnegative. The ground-source expansion, using only oddness, \(Tw=s/2\), and \(\int sw=1/8\), gives the exact identity
\[
 \boxed{\quad P_w[h/w]-N_w[h/w]=q[h].\quad}                    \tag{8}
\]
The signed source form on the right is the original one. In particular the source, the coefficient-two polar correction, and the prime coefficients have not been altered.

For a centered source \(\int_0^\infty sh=0\), the pole term is exactly
\[
 P_{{\rm pole},w}[h/w]=\int_0^\infty s\frac{|h|^2}{w}.
\]
The reflected square gives the complete estimate
\[
 N_{w_Y}[h/w_Y]\le4\int_0^\infty\frac{L_Y(x)}{w_Y(x)}|h(x)|^2dx
 \le4C_L\int_0^\infty e^{x/2}\frac{|h(x)|^2}{w_Y(x)}dx.       \tag{9}
\]

## 4. Every finite actual-source mask has an adapted completion

Let
\[
 m(x)^2=\frac{\Phi(x)}{2\cosh(x/2)}.
\]
Suppose \(g\) is odd, centered, belongs to \(H^\sigma(\mathbb R)\) for some \(\sigma>1/2\), and
\(\|g/m\|_2<\infty\). For any fixed \(A<\infty\) and \(Y>A\), every finite mask
\[
 h(x)=\sum_{j=1}^J c_j\,[g(x+a_j)+g(x-a_j)],\qquad |a_j|\le A, \tag{10}
\]
has a well-defined centered vector \([h/w_Y]\) in the actual core completion of \(P_{w_Y}\), and (8) holds there.

Here are the domain details. Choose \(0<\alpha<\sigma-1/2\), reducing \(\sigma\) below one if necessary. An odd \(H^\sigma\) function satisfies
\(|h(x)|\le C\|h\|_{H^\sigma}|x|^\alpha\). Since \(w_Y(x)\asymp_Y x\) at zero, the integrand in (9) is integrable there. On compact intervals away from zero, ordinary \(L^2\) suffices.

For large \(x\), the theta tails give
\(w_Y(x)\ge c_Y\Phi(x-Y)\). For every \(|a|\le A<Y\), both \(x+a\) and \(x-a\) exceed \(x-Y>0\); hence monotonicity gives
\(\Phi(x-Y)\ge\Phi(x\pm a)\). After a change of variable, each far-tail contribution in (9) is bounded by a fixed multiple of
\[
 e^{A/2}\int_{\mathbb R}e^{u/2}\frac{|g(u)|^2}{\Phi(u)}du
 \le e^{A/2}\|g/m\|_2^2.                                    \tag{11}
\]
Thus (9) is finite.

The signed form is controlled by the same source norms. Its logarithmic Gamma term is bounded by \(C_\sigma\|h\|_{H^\sigma}^2\). For any fixed \(b>1\),
\[
 \left|\int\bar h(x)h(x+d_n)dx\right|
 \le n^{-b/2}\int e^{b|x|}|h(x)|^2dx,

a_n:=\alpha_n n^{-b/2},\qquad\sum_n a_n<\infty.
\]
The physical norm bounds every fixed exponentially weighted \(L^2\) norm of \(g\), and finite translations preserve this property. The pole moment is controlled by the same norm. Thus the complete prime source pairing is absolute.

To identify the completion rather than merely raw finite integrals, first cut \(h\) off by even smooth cutoffs. The cutoffs converge in \(H^\sigma\), in the weighted norm in (9), and in every required exponential \(L^2\) norm. Next mollify each compact odd source by an even mollifier. On a fixed compact interval, its origin weighted convergence follows from the same \(H^\sigma\) Hölder estimate; away from zero the weights are bounded. This gives compact smooth odd sources \(h_k\) converging in all three norms. If desired, subtract their vanishing pole moments times one fixed compact smooth odd test with nonzero pole moment, making all approximants centered.

The ratios \(h_k/w_Y\) are smooth even-extension core ratios. On differences, (9) makes \(N_{w_Y}\) tend to zero, while the preceding source bounds make \(q\) tend to zero. Equation (8) then makes the nonnegative \(P_{w_Y}\)-energy tend to zero. Hence they are genuinely Cauchy in the adapted completion. The centered pole norm identifies their source limit with \(h\), and (8) passes to that limit.

For the normalized translation \(T_ag=(g(\cdot+a)+g(\cdot-a))/2\), these estimates also prove
\[
 \sup_{|a|\le A}P_{w_Y}[T_ag/w_Y]
 \le C_{A,Y,\sigma}\bigl(\|g\|_{H^\sigma}^2+\|g/m\|_2^2\bigr). \tag{12}
\]
The constants are finite for fixed parameters, not claimed uniform as \(A,Y\to\infty\).

The [actual-source bootstrap](../20261013_supercritical_source_tails/BOOTSTRAP_AND_FIXED_TRANSLATIONS.md) supplies every \(\sigma<1\) at fixed positive scalar spectral depth. The [physical source bridge](../20261014_green_band_log_cost_candidate/GREEN_BAND_LOG_COST.md) supplies the original physical norm. Thus (10) applies to those actual scalar sources without assuming smooth pointwise derivatives or changing prime coefficients.

**Completion distinction.** Arbitrarily long masks have been placed in \(P_{w_Y}\), not in the original \(P_\psi\). The old largest-eigenvalue variational inequality and its depth do not automatically hold in this changed positive metric. Only the signed source form (8) is unchanged.

## 5. Sharp full transport asymptotic

Now let \(g\ne0\) be smooth, odd, centered and supported in \([-A,A]\). For \(Y>A+1\), put
\(h_Y(x)=g(x-Y)+g(x+Y)\). On the positive half-line, set \(u=x-Y\). Then
\[
 h_Y(Y+u)=g(u),\qquad
 F_Y(u)=\Phi(u)-\Phi(u+2Y),\qquad
 w_Y(Y+u)=\frac{F_Y(u)}{4\sinh(Y/2)},\quad u>-Y.               \tag{13}
\]
On the fixed support of \(g\), \(F_Y\) stays uniformly comparable to \(\Phi\), and \(g/F_Y\to g/\Phi\) in every fixed smooth norm. Also \(0<F_Y(u)\le\Phi(u)\) for \(u>-Y\).

The scale factors in each Gamma and forward-prime square cancel exactly. Dominated convergence gives
\[
 P_{\Gamma,w_Y}[h_Y/w_Y]\longrightarrow
 E_\Gamma(g):=\iint_{\mathbb R^2}\Phi(u)\Phi(v)\kappa(|u-v|)
 \left|\frac{g(u)}{\Phi(u)}-\frac{g(v)}{\Phi(v)}\right|^2dudv, \tag{14}
\]
\[
 P_{F,w_Y}[h_Y/w_Y]\longrightarrow
 E_F(g):=2\sum_{n\ge2}\alpha_n\int_{\mathbb R}\Phi(u)\Phi(u+d_n)
 \left|\frac{g(u)}{\Phi(u)}-\frac{g(u+d_n)}{\Phi(u+d_n)}\right|^2du.
                                                                    \tag{15}
\]
For (14), the reflected Gamma subtraction \(\kappa(2Y+u+v)\) tends to zero. Drop it for domination. Near the diagonal, the uniformly compact-supported \(C^1\) ratios pay the \(1/|u-v|\) singularity. Away from the diagonal the theta weights give an integrable envelope. For (15), domination follows from the local uniform finiteness of the **complete** row
\(\sum_n\alpha_n[\Phi(u+d_n)+\Phi(u-d_n)]\) on the fixed support. No finite-prime truncation is involved.

The pole term can be expanded explicitly. Since
\[
 4\sinh(Y/2)\sinh((Y+u)/2)
 =e^Ye^{u/2}+e^{-Y}e^{-u/2}-2\cosh(u/2),
\]
and \(|g|^2/\Phi\) is even,
\[
 P_{{\rm pole},w_Y}[h_Y/w_Y]
 =e^YA_g-2A_g+o(1),\qquad
 A_g=\int_{\mathbb R}e^{u/2}\frac{|g(u)|^2}{\Phi(u)}du.        \tag{16}
\]
The omitted denominator term \(\Phi(u+2Y)\) is uniformly double-exponentially small on the fixed support, even after multiplication by \(e^Y\).

Finally, the original even-positive-ground expansion with \(T\Phi=-\cosh(x/2)\), applied to the centered odd source \(g\), gives
\[
 q[g]=\tfrac12E_\Gamma(g)+\tfrac12E_F(g)-A_g.                  \tag{17}
\]
The source pole term vanishes by centering. The complete row terms in this expansion are absolutely convergent by the theta tail. Combining (14)–(17) proves (2).

This gives both an exact leading coefficient and the first finite correction. In particular, the original signed quantity \(q[g]\) has not disappeared: it occurs as \(2q[g]\) in that correction.

## 6. Optimal exponential order and the retained signed comparison

For any positive normalized gauge \(w\), Cauchy–Schwarz gives the universal bound
\[
 P_w[h/w]\ge P_{{\rm pole},w}[h/w]
 \ge8\left(\int_0^\infty s|h|\right)^2
\]
for centered \(h\). Applied to \(h_Y\),
\[
 P_w[h_Y/w]\ge
 2e^Y\left(\int_{\mathbb R}e^{u/2}|g(u)|du\right)^2(1+o(1)). \tag{18}
\]
Together with (2), this proves optimality of the exponential order \(e^Y\). It does not claim the box profile optimizes the leading constant over all admissible gauges.

The complete reflected energy has the leading asymptotic
\[
 N_{w_Y}[h_Y/w_Y]=e^YA_g+o(e^Y).                               \tag{19}
\]
For clarity, this last statement needs only the ordinary prime number theorem, not RH. If
\(C_g(v)=\int_{\mathbb R}g(x)g(x+v)dx\), then
\[
 \int h_Y(x)h_Y(x+d)dx
 =2C_g(d)+C_g(d-2Y)+C_g(d+2Y).
\]
The last term is zero for positive \(d\) and \(Y>A\). The only moving prime window is paid exactly by
\[
 e^{-Y}\sum_n\alpha_n C_g(d_n-2Y)
 \longrightarrow\int e^{u/2}C_g(u)du
 =\left(\int e^{-x/2}g(x)dx\right)
  \left(\int e^{x/2}g(x)dx\right)=0.
\]
The Gamma and mass source terms are uniformly bounded, and both pole moments vanish. Hence \(q[h_Y]=o(e^Y)\). Equations (8) and (2) prove (19).

Therefore \(N_{w_Y}/P_{w_Y}\to1\) for these transported sources, but this leading-order match does not determine from which side the ratio approaches one. The exact remainder remains \(P_{w_Y}-N_{w_Y}=q[h_Y]\). No sign estimate for that remainder, no original-metric long-mask covariance inequality, and no zero exclusion is obtained here.
