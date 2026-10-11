## Round 122 — why nested Section-11 truncations do not give eigenvalue monotonicity

The original Section 11 source [Bombieri, *Remarks on Weil's quadratic
functional in the theory of prime numbers, I*](https://www.bdim.eu/item?fmt=pdf&id=RLIN_2000_9_11_3_183_0)
says to apply the finite problem to \(\Gamma_N\) and retain the negative
eigenvalue \(\lambda_N<0\) “largest in absolute value.”  It is tempting to
identify this with the bottom eigenvalue of a nested self-adjoint principal
submatrix and then invoke interlacing.  That identification is not valid in
the off-line problem.

The displayed Section-11 matrix has entries

\[
 K_{\gamma,\gamma'}
 =\int_E e^{i\gamma' u}e^{-i\gamma u}\,du
 =\int_E e^{i(\gamma'-\gamma)u}\,du.
 \tag{122.1}
\]

For complex \(\gamma,\gamma'\), its ordinary Hermitian adjoint has entries

\[
 \overline{K_{\gamma',\gamma}}
 =\int_E e^{i(\overline{\gamma'}-\overline{\gamma})u}\,du,
 \tag{122.2}
\]

which is not \(K_{\gamma,\gamma'}\) in general.  The off-line zero
coordinates are non-real in the usual \(s=\tfrac12+iz\) parametrization.
The source's fourfold zero symmetry can force the finite eigenvalues to be
real, but real spectrum is weaker than ordinary self-adjointness and does not
provide a positive Rayleigh quotient or Courant--Fischer interlacing.

The failure is visible in a two-dimensional nested example.  For
\(0<\varepsilon<1\), take

\[
 H_1=[-1-\varepsilon],\qquad
 H_2=
 \begin{pmatrix}
 -1-\varepsilon&1\\
 -1&1-\varepsilon
 \end{pmatrix}.
 \tag{122.3}
\]

The eigenvalues of \(H_2\) are both \(-\varepsilon\), since its trace is
\(-2\varepsilon\) and its determinant is \(\varepsilon^2\), whereas the
one-dimensional principal section \(H_1\) has eigenvalue
\(-1-\varepsilon\).  Thus even the negative eigenvalue of largest absolute
value can move toward zero when a non-Hermitian coordinate is added.  No
interlacing contradiction is available.

Accordingly, the fact that the sets \(\Gamma_N\) are nested does not prove
that Bombieri's selected \(\lambda_N\) is bounded away from zero.  The
nonzero-branch compactness argument in Round 45 remains valid as a separate
operator statement: if a selected branch has a nonzero limiting eigenvalue,
absolute summability of the full matrix yields tightness and an infinite
eigenvector.  What nesting cannot do is eliminate the zero-collapse branch.
That branch still requires a source-specific estimate on the selected
eigenvectors or a complete positivity/range theorem.

**Established:** “largest negative eigenvalue in absolute value” in the
source is not a self-adjoint bottom-eigenvalue selection for complex
off-line coordinates; nested truncation alone supplies no monotonicity.

**Failure / missing step:** no argument has been found that prevents the
source-selected negative branch from satisfying \(\lambda_N\to0\) when the
critical block develops near-kernels.

**RH status:** no unconditional proof has been produced.
