# Independent audit: generalized zero pairing (50)

## Disposition

**Pass, conditional on the cited source-tail, global-current, and additive Weil-form reports.** I found no fatal sign, factor, closure, or convergence defect in the route from the weak eigen-source equation to the absolutely convergent signed zero identity. In particular, the argument does not turn that identity into a sign-definite zero sum and does not prove RH.

The substantive new step is the weighted kinetic estimate. Its IMS sign is correct, the error is controlled uniformly in the saturation parameter, and the reflected and forward prime cross terms are summable over all integer labels with \(\Lambda(n)\ne0\). The final presentation includes the precision points checked below.

## Weighted eigen-equation test

Write \(V=L/\psi\), \(g=\psi r=\mu v\), and let
\[
\phi_R=\frac{R\phi}{R+\phi},\qquad F_R=\phi_R^2,\qquad
X_R^2=\int_0^\infty V\phi_R^2|g|^2.
\]
The endpoint and theta bounds imply \(V>0\), \(V\sim c/x\) at zero, and \(V\ge c_*>0\) globally. For each fixed \(R\), \(F_R\) is even, bounded, smooth, and Lipschitz. It preserves the transformed ratio core, and the displayed jump-form multiplier estimate extends it to the closed kinetic form domain. Thus \(F_Rg\) is an admissible source test. The rank term is zero on this test because its first factor is the centered eigen-source \(m(g)=0\).

For the jump form, direct expansion gives
\[
\operatorname{Re}q_b[g_o,F_Rg_o]
=q_b[\phi_Rg_o]-I_R,
\quad
I_R=\frac12\iint\kappa(|x-y|)(\phi_R(x)-\phi_R(y))^2
                 \operatorname{Re}(g_o(x)\overline{g_o(y)})\,dxdy.
\]
This verifies the minus sign in (6). On the region \(|x|\ge |y|\), monotonicity and \(|\phi_R'|\le C_a\phi_R\) give, with \(u=|x-y|\),
\[
\frac{|\phi_R(x)-\phi_R(y)|^2}
     {\phi_R(x)\sqrt{V(|x|)}}
\le C_a\rho_a(|x|)u.
\]
For \(u\le1\), use the derivative bound and \(u^2\le u\); for \(u>1\), use \(|\phi_R(x)-\phi_R(y)|\le\phi_R(x)\). Consequently the kernel controlling \(I_R\) is bounded by \(C_a\rho_a(|x|)u\kappa(u)\), whose Hilbert--Schmidt norm is finite because both factors are in \(L^2\). The full-line weighted norm is \(\sqrt2X_R\), absorbed into the constant. This yields \(|I_R|\le C_aX_R\|g\|_2\), uniformly in \(R\); it does not rely on an unproved uniform bound for the multiplier norm of \(F_R\).

For each forward edge \(X=x+d_n\ge d_n\), and for each reflected edge \(X=\max(x,d_n-x)\ge d_n/2\). Since \(F_R\) is increasing in \(|x|\), either test endpoint has weight at most \(\phi_R(X)^2\), and
\[
\phi_R(X)^2|g(X)g(Y)|
=[\sqrt{V(X)}\phi_R(X)|g(X)|]
 [\rho_a(X)|g(Y)|].
\]
Cauchy--Schwarz on each edge gives \(C_aX_R\|g\|_2\) times respectively \(\sup_{X\ge d_n}\rho_a(X)\) or \(\sup_{X\ge d_n/2}\rho_a(X)\). The double-exponential decay of \(\rho_a\) makes the sums against \(\alpha_n\le\log(n)/\sqrt n\) converge. This checks both correlation orientations in \(p[g,F_Rg]\), the reflected cross term in \(\mathscr N\), and inclusion of all prime powers.

Taking the real part of the weak equation therefore gives
\[
q_b[\phi_Rg_o]+2\delta X_R^2
\le C_aX_R\|g\|_2+2C_0\int\phi_R^2|g|^2+C_a\|g\|_2^2.
\]
On a fixed compact interval the mass term is bounded by \(C_{a,\delta}\|g\|_2^2\). Outside a sufficiently large interval, \(2C_0\le\delta V\), so it is at most \(\delta X_R^2\). This leaves \(q_b[\phi_Rg_o]+\delta X_R^2\) on the left; Young's inequality absorbs the linear term. Thus (10) is uniform in \(R\), with the stated allowed dependence on \(a,\delta\). The factor \(2\) in the diagonal part of \(\mathscr N\) is needed for this absorption and is handled correctly.

As \(R\uparrow\infty\), monotone convergence first gives \(\int V\phi_a^2|g|^2<\infty\). Since \(V\ge c_*>0\), this also gives strong \(L^2\) convergence \(\phi_Rg_o\to\phi_ag_o\). Closedness of \(q_b\) and the uniform form bound then put \(\phi_ag_o\) in its form domain. Multiplication by the bounded Lipschitz ratio \(e^{a|x|}/\phi_a(x)\) gives the claimed exponential weighted form regularity. The final report explicitly uses \(V\ge c_*\) to justify this closure limit.

## Entire transform and continuous sampling

For any \(a>0\), weighted \(L^2\) implies weighted \(L^1\) after choosing a slightly larger exponent, so \(G(z)=\int g_o(x)e^{izx}dx\) is entire. For \(|\eta|\le3/4\), take \(a>3/4\) and apply the multiplier estimate to \(e^{-\eta x-a|x|}\) acting on \(e^{a|x|}g_o\). The multiplier and its Lipschitz norm are bounded uniformly in \(\eta\), giving (11) from \(b(t)\asymp\log(2+|t|)\) at high frequency and the \(L^2\) term at low frequency.

Fix \(r<1/4\). The zeros lie in \(|\operatorname{Im}z|<1/2\), so all submean disks of radius \(r\) lie in the strip covered by (11). The needed local count is the short-interval Riemann--von Mangoldt estimate \(N(T+1)-N(T)=O(\log(2+T))\), with multiplicity, and its negative-ordinate reflection. It bounds the number of zero centers within distance \(r\) of each \(w\) by \(C\log(2+|\operatorname{Re}w|)\). Summing the submean inequality for \(|G|^2\), counting repeated zeros by \(j_z\), and then applying Tonelli proves (13). No separation or conjugate-pair assumption is used at this stage. The report cites the short-interval consequence of the full Riemann--von Mangoldt remainder. The weaker global statement \(N(T)=O(T\log T)\) alone would not imply the local bound.

## Extension of the full Weil identity

For compact odd smooth \(f\), the additive formula applied to \(f*\widetilde f\) has transform \(\widehat f(z)\overline{\widehat f(\bar z)}\). The pole values are \(-2|\int_{\mathbb R}\sinh(x/2)f(x)dx|^2\), hence \(-8|\int_0^\infty\sinh(x/2)g(x)dx|^2\) for an odd source. The gamma term is equivalently \(q_b[f]-C_0\|f\|_{L^2(\mathbb R)}^2\) or \(q_b[f]-2C_0\|g\|_{L^2(0,\infty)}^2\). The complete prime term follows from
\[
\int_{\mathbb R}\overline{f(x)}f(x+d)dx
=2\operatorname{Re}\int_0^\infty\overline{g(x)}g(x+d)dx
-\int_0^d\overline{g(x)}g(d-x)dx,
\]
so the signs and factors in the candidate agree with the source normalization.

For the generalized source, take \(a>1\), choose the smooth weight \(\omega_a=\phi_a\), and approximate \(\omega_ag_o\) in the closed \(q_b+L^2\) norm by odd compact-smooth \(f_k\). Then \(g_k=\omega_a^{-1}f_k\) is compact-smooth odd and converges to \(g_o\) in the weighted norm. The ordinary gamma and mass terms converge by the bounded-multiplier estimate; the pole moments converge by weighted Cauchy--Schwarz. For the primes, for every \(d>0\),
\[
|H_f(d)|\le e^{-ad}\|e^{a|x|}f\|_2^2,
\qquad \sum_n\alpha_ne^{-ad_n}
=\sum_n\Lambda(n)n^{-a-1/2}<\infty.
\]
Polarization gives convergence of the full prime series. For the zero side, apply the sampling bound to differences: uniformly in \(|\eta|\le3/4\), \(e^{-\eta x}/\omega_a\) is bounded Lipschitz, so (3) makes the sampled \(\ell^2(j_z)\) norm of \(G_k-G\) tend to zero. Cauchy--Schwarz then passes the zero products, including the conjugate argument, because the zero multiset and multiplicities are invariant under conjugation. The zero sum is absolutely convergent. This validates (14) for the generalized source without making an original-operator-domain claim.

The source/current pairing in (15) should be understood as a weighted duality extension, not as applying a compact-test distribution directly to the noncompact \(g_o\). With \(V=L/\psi\), the cited current bound and the source bound give
\[
\int_0^\infty|Wg|\,dx
\le\left(\int_0^\infty\frac{|W|^2}{V}\,dx\right)^{1/2}
    \left(\int_0^\infty V|g|^2\,dx\right)^{1/2}<\infty.
\]
On core sources the weighted sesquilinear pairing is \(\langle W_o,g_o\rangle=2\int\overline Wg=N[r]\); the displayed bound and the closed edge-form limit extend this identity to the eigen-source. The report inserts this Cauchy--Schwarz justification before using \(\mathfrak A_s[g_o]=-\delta N[r]\), making the pairing domain explicit.

## Orbit signs and conclusion

The auxiliary operator and all its coefficients are real. If an eigenvector is complex, one of its real or imaginary parts is a nonzero eigenvector for the same real eigenvalue; thus a real source can be chosen. For real odd source, \(G(-z)=-G(z)\) and \(\overline{G(z)}=G(-\bar z)\). Each critical pair contributes \(2j_\gamma|G(\gamma)|^2\). For an off-critical quartet represented by \(z=\gamma-i\beta\), the four actual terms \(G(w)\overline{G(\bar w)}\) add to \(-4j_z\operatorname{Re}(G(z)^2)\). Thus the sign in (17) and the rearrangement (18) check. The sums should be read over distinct orbit representatives, with the common zero multiplicity \(j\) attached; this avoids double-counting while preserving the Weil multiset convention.

Because a nonzero \(\lambda>1\) eigenvector has \(N[r]=\lambda P[r]>0\), (18) forces a positive aggregate real off-line contribution. Since each \(\operatorname{Re}G(z)^2\le|G(z)|^2\), the lower bound (19) follows. There is no termwise lower sign, and the finite absolute sampling estimate does not imply an upper comparison. The candidate correctly stops short of an eigenvalue exclusion or RH conclusion.

## Final presentation checks

The report states \(V\ge c_*>0\), cites the short-interval zero-count input, explicitly extends the current-source pairing by weighted Cauchy--Schwarz, and fixes real-source and distinct-orbit multiplicity conventions. These clarifications preserve the signed identity. The full-line mass coefficient is \(-C_0\|f\|_2^2\), and all prime powers and conjugate-zero arguments remain present. No positivity or eigenvalue exclusion follows from the audited identity alone.
