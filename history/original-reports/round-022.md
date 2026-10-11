## Round 22 — the exceptional cross-block is uniformly bounded; vanishing exceptional mass is a critical near-kernel effect

The exact kernel gives one further rigorous reduction. For a fixed finite
exceptional divisor, the cross-block cannot become arbitrarily large merely
because the critical truncation grows. Hence any disappearance of exceptional
mass must occur through the small critical modes isolated in Round 21.

### I. Correctness decision

**成立 (uniform cross-block bound under the finite-exception hypothesis).**

For a fixed exceptional ordinate \(\rho=a+ib\) in the \(\gamma\)-coordinate,
and a real critical ordinate \(\gamma\), the unweighted analytic kernel is

\[
 G_t(\gamma,\rho)
 =2tK\!\left(t(\gamma-\rho)\right)
 =\frac{2\sin(t(\gamma-\rho))}{\gamma-\rho}.
\]

Since \(\gamma\in\mathbb R\),

\[
 \left|\sin(t(\gamma-a-ib))\right|
 \leq \cosh(|tb|),
\]

and therefore

\[
 |G_t(\gamma,\rho)|^2
 \leq
 \frac{4\cosh^2(|tb|)}
 {(\gamma-a)^2+b^2}.
\tag{22.1}
\]

The Riemann--von Mangoldt bound gives

\[
 \sum_{\gamma\in\Gamma_C}
 \frac{1}{1+|\gamma|^2}<\infty.
\]

Because \(b\ne0\) for an off-critical zero and \(a\) is fixed, (22.1) implies

\[
 \sup_N
 \sum_{\gamma\in\Gamma_{C,N}}
 |G_t(\gamma,\rho)|^2
 <\infty.
\tag{22.2}
\]

For finitely many exceptional ordinates, (22.2) gives a uniform
\(\ell^2\)-operator bound for \(G_{CE,N}\). The diagonal exceptional factors
\(D_E\) are fixed and finite, so the same conclusion holds for the
source-normalized cross-block after the fixed coordinate conversion.

Now let \(z_N=(c_N,e_N)\) be a normalized negative branch with
\(\lambda_N=-\varepsilon_N\to0\). From (20.2),

\[
 (G_{CC,N}+\varepsilon_ND_{C,N})c_N
 =-G_{CE,N}e_N.
\tag{22.3}
\]

If \(\|e_N\|_2\to0\), the uniform bound (22.2) forces

\[
 \left\|
 (G_{CC,N}+\varepsilon_ND_{C,N})c_N
 \right\|_2\to0.
\tag{22.4}
\]

The normalized critical component cannot vanish because Bombieri's half-mass
inequality gives \(\|c_N\|_2\geq1/\sqrt2\). Thus a pure-critical limit, if it
occurs, is necessarily a normalized near-kernel sequence of the critical
generalized Gram block; it is not produced by an exploding exceptional
forcing term.

### II. Hostile audit

The estimate (22.2) is an upper bound only. It neither implies
\(\|e_N\|_2\not\to0\) nor supplies the missing lower bound for the resolvent
direction. The critical block can have arbitrarily small eigenvalues, so
(22.4) is compatible with a unit critical component.

The estimate also depends on a fixed finite exceptional divisor. It does not
address infinitely many off-critical zeros, and it does not identify the
specific negative branch among all near-kernel sequences.

### III. Next-route decision

**Route X:** prove a transversality theorem for the actual branch: the vector
\(G_{CE,N}v_N\) selected by (20.4) must avoid the critical near-kernel modes
strongly enough to keep \(R_N(\varepsilon_N)v_N\) bounded. Equation (22.4)
shows exactly what must be ruled out.

**Route Y:** construct a nontracial source-evaluable arithmetic observer that
bypasses this finite-section transversality problem.

### IV. Ledger update

**Established:** for a fixed finite exceptional divisor, the analytic
cross-block \(G_{CE,N}\) is uniformly bounded in \(N\); if exceptional mass
vanishes, the critical component must be a normalized near-kernel sequence.

**Failure / error:** attributing exceptional-mass loss to an unbounded
cross-block, or treating the uniform cross-block bound as a lower bound.

**Still assumed / unknown:** the branch-specific transversality estimate
needed to prove (21.2).

**Next route:** analyze the projections of the explicit sine-kernel
cross-vector onto the small eigenmodes of the critical block.

**RH status:** no unconditional proof has been produced.
