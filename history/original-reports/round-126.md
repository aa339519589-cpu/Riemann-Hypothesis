## Round 126 — a concrete finite-dimensional obstruction to transferring weighted to unweighted branches

The normalization distinction between Bombieri's Sections 8--10 and Section
11 is not cosmetic.  A positive diagonal weight changes generalized
eigenvectors, even when the underlying finite matrix is held fixed.

Take

\[
 K=\begin{pmatrix}1&2\\2&1\end{pmatrix},
 \qquad
 D=\begin{pmatrix}1&0\\0&4\end{pmatrix}.
 \tag{126.1}
\]

The ordinary eigenproblem \(Kz=\mu z\) has negative eigenvalue
\(\mu=-1\) with direction \(z=(1,-1)\).  The generalized problem

\[
 Kz=\lambda Dz
 \tag{126.2}
\]

has characteristic equation

\[
 \det(K-\lambda D)
 =(1-\lambda)(1-4\lambda)-4
 =4\lambda^2-5\lambda-3,
\]

so its negative eigenvalue is
\(\lambda=(5-\sqrt{73})/8\), with direction

\[
 z_2=-\frac{1-\lambda}{2}z_1,
\]

which is not the ordinary negative direction \((1,-1)\).  The change persists
after any of the natural normalizations \(z\mapsto D^{1/2}z\) or
\(z\mapsto Dz\); those maps change the coefficient mass being compared.

In Bombieri's notation the Sections 8--10 problem has the diagonal factor
\(d_\gamma=\tfrac14+\gamma^2\) and a boundary-corrected energy matrix, while
Section 11 has the pure local Gram matrix and the unweighted normalization.
The finite example (126.1)--(126.2) proves that positivity of \(D\) alone
does not identify their selected directions, their exceptional/critical mass
ratios, or their limiting branches.  A valid transfer would require an
additional source-specific statement such as

\[
 U^{-1}H_{\rm weighted}U
 =a\,H_{\rm Section\,11}+bI
 \tag{126.3}
\]

on the exact finite spaces, together with convergence of \(U\), preservation
of the source normalization, and control of the boundary terms.  No such
intertwining identity is present in the source, and the two displayed
problems use different kernels before the weighting is even introduced.

**Established:** a positive diagonal weight does not preserve the
finite-eigenvector branch or its mass cone; the two Bombieri variational
problems cannot be merged by a square-root change of variables alone.

**Remaining load-bearing statement:** prove an explicit intertwining and
normalization theorem, or analyze the Section-11 unweighted branch directly.

**RH status:** no unconditional proof has been produced.

## Ledger erratum — placement of Round 128

Round 128 was inserted at an earlier matching end-marker anchor rather than
at the physical end of this append-only file.  Its text is unchanged.  For
chronological reading, treat it as following Round 127 and before this
erratum; this entry records the actual end-of-file location.
