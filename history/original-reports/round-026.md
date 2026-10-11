## Round 26 — finite-section stability turns the Bombieri gap into an exact range test

Round 25 characterized the ideal weighted range, but the Bombieri argument uses
nested finite critical sections. The following lemma makes the relation between
the two levels exact.

### I. Correctness decision

**成立 (finite-section stability theorem).**

Let \(P_N\) be the coordinate projection onto the first \(N\) critical
ordinates, let

\[
 A_N=A P_N,
 \qquad
 \varepsilon_N>0,
\]

and, for \(h\in L^2(I)\), define the regularized minimum-norm coefficients

\[
 x_N(h)
 =
 A_N^*(A_NA_N^*+\varepsilon_N I)^{-1}h.
\tag{26.1}
\]

The singular-value calculus gives

\[
 \left\|A_N^*(A_NA_N^*+\varepsilon_N I)^{-1}\right\|
 \leq \frac1{2\sqrt{\varepsilon_N}},
\tag{26.2}
\]

\[
 \left\|A_N^*(A_NA_N^*+\varepsilon_N I)^{-1}A_N\right\|
 \leq 1,
\qquad
 \left\|\varepsilon_N(A_NA_N^*+\varepsilon_N I)^{-1}\right\|
 \leq 1.
\tag{26.3}
\]

There are two complementary implications.

#### Necessity

Assume

\[
 \sup_N\|x_N(h)\|_2<\infty,
 \qquad
 \|h-A_Nx_N(h)\|_{L^2(I)}\longrightarrow0.
\tag{26.4}
\]

Extend \(x_N(h)\) by zero outside \(P_N\ell^2\). A subsequence converges
weakly in \(\ell^2\) to some \(x\). Since \(A\) is compact,

\[
 A_Nx_N(h)=Ax_N(h)\longrightarrow Ax
\quad\text{strongly in }L^2(I).
\]

Together with (26.4), this gives

\[
 h=Ax.
\tag{26.5}
\]

Thus bounded weighted coefficient cost plus vanishing finite-section residual
forces \(h\in\operatorname{Ran}A\). The same conclusion holds for a sequence
\(h_N\to h\): if \(x_N(h_N)\) is bounded and
\(\|h_N-A_Nx_N(h_N)\|\to0\), then \(h\in\operatorname{Ran}A\).

#### Sufficient direction with the exact missing rate

If \(h=Aq\), put

\[
 \delta_N=\|A(I-P_N)q\|_{L^2(I)}.
\]

Writing \(h=A_NP_Nq+\bigl(h-A_NP_Nq\bigr)\) and using (26.2)--(26.3) yields

\[
 \|x_N(h)\|_2
 \leq
 \|q\|_2+\frac{\delta_N}{2\sqrt{\varepsilon_N}},
\tag{26.6}
\]

and, because

\[
 h-A_Nx_N(h)
 =
 \varepsilon_N(A_NA_N^*+\varepsilon_NI)^{-1}h,
\]

\[
 \|h-A_Nx_N(h)\|_{L^2(I)}
 \leq
 \frac{\sqrt{\varepsilon_N}}2\|q\|_2+\delta_N.
\tag{26.7}
\]

Consequently,

\[
 \delta_N=O(\sqrt{\varepsilon_N})
\tag{26.8}
\]

is sufficient for both bounded coefficients and the
\(O(\sqrt{\varepsilon_N})\) residual required by the Schur argument. Exact
range membership alone does not imply (26.8), because the compact range is
nonclosed and the coordinate tail can decay more slowly than the selected
eigenvalue scale.

### II. Direct identification with the Bombieri generalized block

For the critical/exceptional split in Round 20, let \(S_{C,N}\) be the
critical synthesis, \(D_{C,N}\) the diagonal matrix with entries
\(d_\gamma=1/4+\gamma^2\), and set

\[
 A_N=S_{C,N}D_{C,N}^{-1/2},
 \qquad
 q_N=D_{C,N}^{1/2}c_N,
 \qquad
 h_N=S_Ee_N.
\]

The critical block equation at \(\lambda_N=-\varepsilon_N\) is exactly

\[
 (A_N^*A_N+\varepsilon_NI)q_N=-A_N^*h_N,
\tag{26.9}
\]

so

\[
 q_N=-x_N(h_N),
 \qquad
 h_N+A_Nq_N
 =
 \varepsilon_N(A_NA_N^*+\varepsilon_NI)^{-1}h_N.
\tag{26.10}
\]

Therefore, along any finite-exception subsequence for which
\(e_N\to e\), hence \(h_N\to h=S_Ee\), the following implication is rigorous:

\[
 \sup_N\|D_{C,N}^{1/2}c_N\|_2<\infty,
 \qquad
 \|h_N+A_ND_{C,N}^{1/2}c_N\|\to0
 \quad\Longrightarrow\quad
 h\in\operatorname{Ran}A.
\tag{26.11}
\]

Its contrapositive is the usable exclusion statement:

\[
 h\notin\operatorname{Ran}A
 \quad\Longrightarrow\quad
 \|D_{C,N}^{1/2}c_N\|_2\to\infty
\]

along every subsequence that approximates \(-h\) with vanishing residual.
This is a genuine finite-section obstruction, not a restatement of ordinary
local density.

### III. Hostile audit

The theorem does not prove that an exceptional waveform is outside
\(\operatorname{Ran}A\), and it does not prove the weighted coefficient bound
\(\sup_N\|D_{C,N}^{1/2}c_N\|<\infty\). The Bombieri normalization controls
\(\|c_N\|\), not the weighted norm; high critical ordinates can make the latter
diverge while the former stays bounded.

Likewise, the half-mass inequality controls the unweighted split
\(\|c_N\|/\|e_N\|\). It supplies neither (26.8) nor (26.11). Finally, this
argument is conditional on a finite exceptional packet and leaves the
infinite-exception case untouched.

### IV. Route decision and ledger update

**Route X remains selected:** determine weighted range membership for the
exceptional waveform, then prove the tail estimate (26.8) at the actual
\(\varepsilon_N\) scale. The new theorem shows exactly why these are the only
remaining analytic inputs for this branch.

**Route Y:** an independent arithmetic observer could bypass the compact-range
problem, but no such observer has yet supplied a closed inequality.

**已确认事实:** the finite-section bounded-cost/vanishing-residual condition
implies ideal weighted range membership, and ideal membership plus the explicit
tail rate implies finite-section stability.

**成立点:** the Bombieri critical block is precisely the regularized
least-squares system (26.9), after the \(D^{1/2}\) change of variables.

**失败 / 错误点:** using \(\|c_N\|\), half mass, or an \(o(1)\) residual as a
substitute for the weighted norm and the \(\sqrt{\varepsilon_N}\)-scale tail.

**仍属假设:** finiteness of the exceptional packet and convergence of its
coefficient direction along the selected subsequence.

**未知 / 待验证:** whether the actual exceptional exponential packet belongs
to \(\operatorname{Ran}A\), and whether (26.8) holds for its representing
coefficients.

**下一步路线:** test the exact range condition for
\(h(u)=\sum_{\rho\in E}e_\rho e^{-i\rho u}\) using the critical zero set; if
membership holds, establish (26.8), and if it fails, use (26.11) to exclude
the finite-exception Bombieri branch.

**RH status:** no unconditional proof has been produced.
