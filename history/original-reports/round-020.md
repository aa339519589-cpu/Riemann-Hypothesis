## Round 20 — coordinate correction: the exact Bombieri Schur complement is generalized, not ordinary self-adjoint

Round 19 gave the correct block-elimination pattern for a self-adjoint block
matrix, but the displayed Bombieri kernel is written in a diagonally weighted
coordinate system. The exact arithmetic reduction must therefore be recorded
in the original coefficient coordinates.

### I. Correctness decision

**成立 (after the coordinate correction).**

Put

\[
 G_N(\gamma,\gamma')=2t\,K\!\left(t(\gamma-\gamma')\right),\qquad
 d_\gamma=\frac14+\gamma^2,
\]

so that Bombieri's displayed matrix is

\[
 H_N=G_ND_N^{-1},\qquad D_N=\operatorname{diag}(d_\gamma),
\]

and \(w_\gamma=d_\gamma z_\gamma\). The eigenvalue equation
\(H_Nw_N=\lambda_Nw_N\) is exactly equivalent to

\[
 G_Nz_N=\lambda_ND_Nz_N.
\tag{20.1}
\]

Split the \(z\)-coordinates into critical and exceptional parts:
\(z_N=(c_N,e_N)\). Since every critical \(\gamma\) is real,
\(D_{C,N}\) is positive diagonal and \(G_{CC,N}\) is a real symmetric
positive-semidefinite Gram matrix. If \(\lambda_N=-\varepsilon_N<0\), the
critical block of (20.1) gives

\[
 (G_{CC,N}+\varepsilon_ND_{C,N})c_N
 +G_{CE,N}e_N=0.
\tag{20.2}
\]

The first matrix in (20.2) is positive definite, so the exact elimination is

\[
 c_N=-(G_{CC,N}+\varepsilon_ND_{C,N})^{-1}G_{CE,N}e_N.
\tag{20.3}
\]

The exceptional block is consequently governed by the generalized Schur
equation

\[
 \left[
 G_{EE,N}+\varepsilon_ND_{E,N}
 -G_{EC,N}(G_{CC,N}+\varepsilon_ND_{C,N})^{-1}G_{CE,N}
 \right]e_N=0.
\tag{20.4}
\]

No limiting argument is used in (20.1)--(20.4). The exceptional vector is
selected by this finite Schur equation, and the critical vector is the
resolvent image of it.

Let \((u_{j,N},\tau_{j,N})\) be an orthonormal eigensystem of the positive
matrix \(G_{CC,N}+\varepsilon_ND_{C,N}\). Equation (20.3) gives the exact
critical coefficient norm in Bombieri's \(z\)-normalization:

\[
 \|c_N\|_2^2
 =
 \sum_j
 \frac{\left|\left\langle u_{j,N},G_{CE,N}e_N\right\rangle\right|^2}
 {\tau_{j,N}^2}.
\tag{20.5}
\]

Thus the critical half-mass requirement
\(\|c_N\|_2\geq\|e_N\|_2\) becomes

\[
 \sum_j
 \frac{\left|\left\langle u_{j,N},G_{CE,N}e_N\right\rangle\right|^2}
 {\tau_{j,N}^2}
 \geq \|e_N\|_2^2.
\tag{20.6}
\]

Equation (20.6), not the unweighted \(H_N\)-block version, is the exact
finite-\(N\) quantitative target in the source normalization.

### II. Hostile audit

The positive diagonal \(D_{C,N}\) repairs invertibility but does not prove
(20.6). The small eigenvalues \(\tau_{j,N}\) can amplify the resolvent only
when \(G_{CE,N}e_N\) has sufficient projection onto the corresponding modes.
The exceptional Schur equation (20.4) does not, by algebra alone, provide
that projection lower bound.

The coordinate distinction matters for the mass statement: a positive diagonal
similarity can preserve eigenvalues and Schur zeros while changing the
ordinary coefficient norm. Therefore an argument that proves (20.6) only after
rescaling \(z\) to \(w\) has not yet proved Bombieri's \(\ell^2\) mass
inequality.

### III. Relation to Round 19

Round 19 remains valid as an abstract block-elimination template for a
self-adjoint representation. Round 20 is the source-faithful specialization
and supersedes its ordinary-positive-block interpretation for the displayed
Bombieri coordinates.

### IV. Next-route decision

**Route X:** prove a zeta-specific lower bound in (20.6), together with the
branch selection encoded by (20.4), uniformly as \(N\to\infty\). This is the
only remaining Bombieri route.

**Route Y:** construct a nontracial source-evaluable observer avoiding this
generalized Schur selection problem.

### V. Ledger update

**Established:** the exact Bombieri finite problem is the generalized system
(20.1), with resolvent identity (20.3), Schur equation (20.4), and
source-normalized mass target (20.6).

**Failure / error:** treating \(G D^{-1}\) as ordinary self-adjoint, or proving
a coefficient inequality only after a diagonal similarity, does not establish
Bombieri's original \(\ell^2\) mass condition.

**Still assumed / unknown:** the arithmetic projection lower bound in (20.6)
for the negative branch selected by (20.4), and its uniform \(N\)-limit.

**Next route:** attack (20.4)--(20.6) with the explicit zeta-zero symmetry and
kernel; otherwise continue the nontracial source search.

**RH status:** no unconditional proof has been produced.

## Ledger erratum — logical order through Round 21

Because two append operations were anchored to a repeated status line, the
physical order of the late blocks is not chronological. The authoritative
logical reading order is Round 17, Round 18, Round 19, Round 20, then Round 21.
No earlier mathematical block is being rewritten; this index is appended to
preserve the append-only record.
