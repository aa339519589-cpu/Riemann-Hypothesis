## Round 147 — the finite-section provenance condition is an exact Schur-complement problem

The remaining Bombieri statement can be made more precise by separating the
finite off-line coordinates from the critical-line coordinates.  Assume the
finite-exception alternative, let \(O\) be the fixed finite set of off-line
points, and write the finite Section-10 matrix in block form

\[
 H_N=
 \begin{pmatrix}
 A & R_N\\
 S_N & C_N
 \end{pmatrix},
\]

where \(C_N\) is the critical-line block.  The source's positivity lemma for
an entirely real set says that \(C_N\) is positive semidefinite, although the
full matrix and the two cross blocks need not form a Hermitian matrix.  If
\(w_N=(x_N,y_N)\) is a negative eigenvector and
\(\lambda_N=-\varepsilon_N<0\), then its two block equations are exactly

\[
 (A+\varepsilon_N I)x_N+R_Ny_N=0,\qquad
 S_Nx_N+(C_N+\varepsilon_N I)y_N=0.
\tag{147.1}
\]

Since \(C_N+\varepsilon_N I\) is invertible,

\[
 y_N=-(C_N+\varepsilon_N I)^{-1}S_Nx_N
\tag{147.2}
\]

and hence

\[
 \left[-\varepsilon_N I-A+
 R_N(C_N+\varepsilon_N I)^{-1}S_N\right]x_N=0.
\tag{147.3}
\]

Thus excluding the \(\lambda_N\to0\) branch requires a genuine lower bound
for this \(\varepsilon\)-dependent Schur complement on the off-line
subspace, together with the source mass cone
\(\lVert x_N\rVert^2\ge\tfrac12\).  This is stronger than proving that
\(S_Nx_N\) has a small high-frequency tail.

There is a useful tail estimate, but it does not supply (147.3).  From the
explicit kernel formula in Bombieri's equation (8.6), for every fixed
\(\eta\in O\) and fixed \(t\),

\[
 |H(\gamma;\eta;t)|\ll_{t,\eta}(1+|\gamma|)^{-1}
 \qquad(\gamma\in\Gamma_C,\ |\gamma|\to\infty).
\tag{147.4}
\]

The integral term is \(O(|\gamma|^{-1})\) by integration by parts, and each
boundary term has the same bound because it contains a factor
\((\tfrac12\pm i\gamma)^{-1}\).  The zero-counting estimate
\(N(T)=O(T\log T)\) therefore gives, for fixed finite \(O\),

\[
 \sum_{\substack{\gamma\in\Gamma_C\\|\gamma|>R}}
 |H(\gamma;\eta;t)|^2
 \ll_{t,\eta}\frac{\log R}{R},
\qquad
 \left\|(S_Nx_N)_{|\gamma|>R}\right\|_2
 \ll_{t,O}\sqrt{\frac{\log R}{R}}\,\lVert x_N\rVert .
\tag{147.5}
\]

Equation (147.5) only says that the forcing vector in (147.2) is tight in
the row coordinates.  It gives no bound on the response, because
\[
 \lVert(C_N+\varepsilon_N I)^{-1}\rVert
 \leq\varepsilon_N^{-1}
\]
and the critical Gram block has no known uniform lower spectral bound.  In
fact, the adjacent-frequency calculation in Round 140 gives nearly null
directions for the local exponential synthesis; the \(O(|\gamma|^{-1})\)
boundary corrections in (8.6) do not create a uniform gap at high height.

The amplification issue is not merely verbal.  Even in the Hermitian
two-by-two model

\[
 H_\epsilon=
 \begin{pmatrix}
 0&\epsilon\\
 \epsilon&\epsilon
 \end{pmatrix},
 \qquad
 C_\epsilon=[\epsilon]\succeq0,
\]

the negative eigenvalue is

\[
 \lambda_-(\epsilon)=\frac{1-\sqrt5}{2}\,\epsilon\longrightarrow0.
\tag{147.6}
\]

The off-line component of a corresponding eigenvector has a fixed positive
fraction of the normalized mass, while the critical forcing
\(S_\epsilon x=\epsilon x\) tends to zero.  This is not a zeta counterexample;
it proves that positivity of the critical block plus the tail estimate
(147.5) cannot by themselves prevent zero-collapse.  A small singular value
of \(C_N\) can keep \(y_N\) at order one while \(\varepsilon_N\to0\).

**Established:** the required finite-section provenance statement is the
explicit Schur-complement exclusion (147.3).  The available zeta-specific
row decay gives (147.5), but it does not control the inverse critical block.
The mechanism survives even for a Hermitian positive critical block.

**Remaining load-bearing statement:** prove an unconditional zeta-specific
lower bound or range/rate theorem for (147.3), or derive a different global
Weil-positivity argument that excludes the same branch.  No such bound has
been established.

**RH status:** no unconditional proof has been produced.
