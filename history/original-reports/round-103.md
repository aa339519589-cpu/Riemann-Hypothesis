## Round 103 — exact dual criterion for the Bombieri weighted range

The remaining Bombieri statement can be reduced to a precise sampling inequality. Let \(I\) be a bounded interval, let \(\Gamma_C\) be the distinct critical ordinates, and set
\[
d_\gamma=\tfrac14+\gamma^2,\qquad
(Aq)(u)=\sum_{\gamma\in\Gamma_C}
\frac{q_\gamma}{\sqrt{d_\gamma}}e^{-i\gamma u}.
\tag{103.1}
\]
Because
\[
\sum_{\gamma\in\Gamma_C}d_\gamma^{-1}<\infty
\]
by the Riemann--von Mangoldt bound, \(A:\ell^2(\Gamma_C)\to L^2(I)\) is Hilbert--Schmidt and hence bounded.

For \(g\in L^2(I)\), define its Paley--Wiener transform
\[
G_g(z)=\int_I g(u)e^{izu}\,du.
\tag{103.2}
\]
With the convention \(\langle f,g\rangle=\int_I f\overline g\), the adjoint samples satisfy
\[
\bigl|(A^*g)_\gamma\bigr|^2
=\frac{|G_g(\gamma)|^2}{d_\gamma}.
\tag{103.3}
\]
The following equivalence is an immediate Hilbert-space range theorem:
\[
h\in\operatorname{Ran}A
\quad\Longleftrightarrow\quad
\exists C_h<\infty\ \ \text{such that}\ \
|\langle h,g\rangle|^2
\le C_h\sum_{\gamma\in\Gamma_C}
\frac{|G_g(\gamma)|^2}{d_\gamma}
\quad\forall g\in L^2(I).
\tag{103.4}
\]
Indeed, the forward implication is Cauchy--Schwarz after writing \(h=Aq\). Conversely, (103.4) makes the functional \(A^*g\mapsto\langle h,g\rangle\) well-defined and bounded on \(\operatorname{Ran}A^*\); Riesz extension supplies \(q\in\ell^2\), and testing against every \(g\) gives \(h=Aq\).

For a finite exponential packet
\[
h(u)=\sum_{j=1}^m c_j e^{-i\eta_j u},
\tag{103.5}
\]
the left side of (103.4) is the squared modulus of the corresponding finite linear combination of complex evaluations \(G_g(\overline{\eta_j})\). Therefore the zero-collapse branch is not settled by ordinary completeness. It asks for, or rules out, the weighted Paley--Wiener sampling inequality
\[
\left|\sum_{j=1}^m\overline{c_j}\,G_g(\overline{\eta_j})\right|^2
\lesssim
\sum_{\gamma\in\Gamma_C}\frac{|G_g(\gamma)|^2}{\tfrac14+\gamma^2}.
\tag{103.6}
\]
If (103.6) holds, the exceptional/boundary packet is in the critical weighted range and the Bombieri \(\lambda_N\to0\) alternative is not contradictory. If it fails, a sequence \(g_n\) exists whose weighted critical samples tend to zero while its off-line evaluation stays nonzero; that sequence supplies the missing range-separation certificate.

The known completeness statement only says that \(G_g(\gamma)=0\) for every critical \(\gamma\) forces \(g=0\). It gives no uniform estimate of the form (103.6), and the compactness of \(A\) in fact makes the weighted sample map non-coercive on the full infinite-dimensional space. Thus “the critical exponentials are complete” cannot be upgraded to (103.6) without a new zeta-specific sampling theorem. The explicit integer-frequency model in Round 53 shows that even smooth finite packets plus the two boundary modes can satisfy the analogue of (103.6), so abstract functional analysis does not supply the upgrade.

**Established:** (103.4) is an exact necessary-and-sufficient reformulation of the surviving Bombieri range question; it identifies the required dual certificate without any RH assumption.

**Failure / missing step:** no unconditional estimate or counter-sequence is known here for the actual critical ordinates and the specific off-line packet.

**Route decision:** make (103.6) the load-bearing target for the Bombieri branch. Reject substitutions by density, unweighted completeness, or finite numerical residuals unless they prove this weighted complex-evaluation inequality.

**RH status:** no unconditional proof has been produced.
