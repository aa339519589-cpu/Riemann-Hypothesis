## Round 21 — the real finite-\(N\) target is an upper bound, not the half-mass inequality

Round 20 identifies the exact generalized Schur system. A further normalization
calculation shows that its proposed lower bound is not the missing statement:
for a negative eigenvector it is already equivalent to Bombieri's known
half-mass inequality. The missing information is whether the exceptional mass
survives normalization as \(N\to\infty\).

### I. Correctness decision

**成立 (exact equivalence for the normalized Schur branch).**

For \(e_N\ne0\), define

\[
 R_N(\varepsilon_N)
 =
 (G_{CC,N}+\varepsilon_ND_{C,N})^{-1}G_{CE,N}.
\]

Write \(e_N=r_Nv_N\), where \(\|v_N\|_2=1\). Equation (20.3) becomes

\[
 c_N=-r_NR_N(\varepsilon_N)v_N.
\]

If \(z_N=(c_N,e_N)\) is normalized in Bombieri's original coefficient norm,
then

\[
 1=\|z_N\|_2^2
 =|r_N|^2\left(1+
 \|R_N(\varepsilon_N)v_N\|_2^2\right),
\]

and therefore

\[
 \|e_N\|_2^2
 =
 \frac{1}{1+\|R_N(\varepsilon_N)v_N\|_2^2},
\qquad
 \|c_N\|_2^2
 =
 \frac{\|R_N(\varepsilon_N)v_N\|_2^2}
 {1+\|R_N(\varepsilon_N)v_N\|_2^2}.
\tag{21.1}
\]

Consequently,

\[
 \|c_N\|_2\geq\|e_N\|_2
 \quad\Longleftrightarrow\quad
 \|R_N(\varepsilon_N)v_N\|_2\geq1.
\]

This is only a lower bound on the critical resolvent image. A nonzero
exceptional component in a normalized subsequential limit requires the
opposite type of estimate:

\[
 \liminf_{N\to\infty}\|e_N\|_2>0
 \quad\Longleftrightarrow\quad
 \sup_N\|R_N(\varepsilon_N)v_N\|_2<\infty
\tag{21.2}
\]

along the selected branch (after discarding finitely many indices).
If the resolvent image diverges, then \(\|e_N\|_2\to0\) and the normalized
limit can become purely critical even though every finite vector has a negative
eigenvalue and satisfies the half-mass inequality.

The Schur equation selecting the direction \(v_N\) is

\[
 \left[
 G_{EE,N}+\varepsilon_ND_{E,N}
 -G_{EC,N}R_N(\varepsilon_N)
 \right]v_N=0.
\tag{21.3}
\]

Thus the exact surviving target is a uniform upper bound for
\(R_N(\varepsilon_N)v_N\), proved using both the explicit zeta kernel and the
selected null direction (21.3).

### II. Hostile audit

The finite negative-eigenvalue theorem does not imply (21.2). Equations
(21.1)--(21.3) show why the earlier half-mass route could not close RH:
\(\|R_Nv_N\|\) may be bounded, may diverge, or may oscillate, and the sign and
inertia information alone do not distinguish these cases.

An operator-norm bound on \(R_N\) is stronger than necessary and may fail because
the critical Gram block develops small eigenvalues. What is needed is a bound
only on the exceptional direction selected by (21.3), or an invariant
equivalent to such a bound. A bound for arbitrary directions would be an
unjustified strengthening.

### III. Relation to Round 20

Round 20 remains the correct source-faithful Schur reduction. Its equation
(20.6) is a necessary finite-branch mass statement, but Round 21 identifies
(21.2) as the actual finite-to-infinite provenance condition. The two statements
must not be conflated.

### IV. Next-route decision

**Route X:** prove (21.2) for the negative branch selected by the exact
Bombieri determinant, or prove a source-specific substitute that forces a
nonzero exceptional limit. This is the precise remaining Bombieri target.

**Route Y:** construct a nontracial arithmetic observer that bypasses the
finite-branch survival problem.

### V. Ledger update

**Established:** normalized Schur eigenvectors obey the exact mass identities
(21.1); the half-mass condition is a lower bound on the critical resolvent
image, while exceptional-mass survival is equivalent to the upper bound (21.2).

**Failure / error:** treating Bombieri's finite negative eigenvalue or
half-mass inequality as proof that exceptional coordinates survive the limit.

**Still assumed / unknown:** the zeta-specific bound (21.2), or any equivalent
finite-\(N\) representative-selection invariant.

**Next route:** attack (21.2) through the explicit determinant and fourfold
zero symmetry; retain the nontracial observer as the competitor.

**RH status:** no unconditional proof has been produced.
