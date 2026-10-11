## Round 19 — the exact finite-\(N\) Schur complement isolates the surviving arithmetic estimate

The previous entries show that limiting local synthesis cannot select the
representative. The finite matrix itself has one precise remaining place where
such information could survive: the Schur complement of its critical block.

### I. Correctness decision

**成立 (as an exact finite-dimensional reduction).**

For a finite truncation, order the coordinates as critical \(C_N\) followed by
exceptional \(E\), and write the matrix in block form

\[
 H_N=
 \begin{pmatrix}
 A_N & B_N\\
 B_N^\sharp & D_N
 \end{pmatrix}.
\]

Here \(A_N\) is the critical block. It is positive semidefinite because all
critical ordinates are real and its entries are the corresponding local
real-frequency Gram form. Let a negative eigenvalue be
\(\lambda_N=-\varepsilon_N<0\), and write a corresponding vector as
\(z_N=(c_N,e_N)\). Since \(A_N+\varepsilon_N I\) is positive definite, the
first block equation gives the exact identity

\[
 c_N=-(A_N+\varepsilon_N I)^{-1}B_Ne_N.
\tag{19.1}
\]

Substitution into the second block equation gives

\[
 \Bigl[D_N+\varepsilon_N I
 -B_N^\sharp(A_N+\varepsilon_N I)^{-1}B_N\Bigr]e_N=0.
\tag{19.2}
\]

No limiting argument is used in (19.1)--(19.2). The exceptional vector is
selected by this finite Schur equation, and the critical vector is the
resolvent image of it.

If \(A_Nu_{j,N}=\sigma_{j,N}^2u_{j,N}\), then (19.1) yields

\[
 \|c_N\|_2^2
 =\sum_j
 \frac{\bigl|\langle u_{j,N},B_Ne_N\rangle\bigr|^2}
 {(\sigma_{j,N}^2+\varepsilon_N)^2}.
\tag{19.3}
\]

For \(e_N\ne0\), Bombieri's critical half-mass inequality is equivalent to
\(\|c_N\|_2\geq\|e_N\|_2\). Hence an exact finite-\(N\) sufficient condition
for the required mass is

\[
 \sum_j
 \frac{\bigl|\langle u_{j,N},B_Ne_N\rangle\bigr|^2}
 {(\sigma_{j,N}^2+\varepsilon_N)^2}
 \ \geq\ \|e_N\|_2^2.
\tag{19.4}
\]

Equation (19.4) is the precise quantitative target. It requires a lower bound
on the projection of the exceptional cross-vector \(B_Ne_N\) onto the small
critical singular modes, at the scale set by
\(\sigma_{j,N}^2+\varepsilon_N\).

### II. Hostile audit

The critical block becoming increasingly ill-conditioned does not prove
(19.4). It can make the resolvent large, but \(B_Ne_N\) might be nearly
orthogonal to the corresponding small modes. Conversely, a large critical
resolvent norm alone does not prove that the particular exceptional vector
selected by (19.2) has nonzero limiting mass.

Therefore none of the following implications is valid without an arithmetic
estimate:

\[
 \sigma_{\min}(A_N)\to0
 \quad\Longrightarrow\quad
 \|c_N\|_2/\|e_N\|_2\to\infty,
\]

\[
 \lambda_N\to0
 \quad\Longrightarrow\quad
 \|e_N\|_2\not\to0,
\]

or

\[
 \text{one negative direction of }H_N
 \quad\Longrightarrow\quad
 \text{a nonzero exceptional limit}.
\]

The exact finite matrix could still contain the needed source-specific
correlation, but it must be proved through (19.2)--(19.4), not inferred from
the limiting local null equation.

### III. Next-route decision

**Route X:** prove (19.4), or a stronger invariant consequence of the exact
Schur equation, uniformly along Bombieri's selected negative branch. This is
the remaining viable Bombieri route.

**Route Y:** construct a nontracial source-evaluable arithmetic observer that
does not require (19.4). It remains the competitive bypass.

### IV. Ledger update

**Established:** the finite-\(N\) provenance problem reduces exactly to the
critical resolvent formula (19.1), the Schur equation (19.2), and the
mass-correlation inequality (19.4).

**Failure / error:** critical ill-conditioning, a negative eigenvalue, or
\(\lambda_N\to0\) alone does not establish nonzero exceptional limiting mass.

**Still assumed / unknown:** a zeta-specific lower bound on the projections
\(\langle u_{j,N},B_Ne_N\rangle\) for the selected branch, with the required
uniform dependence on \(N\) and \(\varepsilon_N\).

**Next route:** attack (19.4) from the explicit Bombieri kernel; if it cannot
be obtained, retain only the nontracial source route.

**RH status:** no unconditional proof has been produced.
