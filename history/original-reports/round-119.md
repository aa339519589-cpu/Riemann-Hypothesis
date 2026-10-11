## Round 119 — the Krein--Marchenko appendix does not identify the zeta zeros

The same preprint adds an alleged independent check using inverse
Sturm--Liouville theory.  It takes the real ordinates \(\gamma_n=\Im\rho_n\)
and declares spectral data such as

\[
 E_n=\frac14+\gamma_n^2,\qquad
 \alpha_n=\frac{\pi}{\gamma_n\log\gamma_n}.
\tag{119.1}
\]

Even granting every claimed Krein--Marchenko summability condition, (119.1)
contains no information about \(\beta_n=\Re\rho_n\).  For a general zero
\(\rho_n=\beta_n+i\gamma_n\), the quantity naturally paired with the
functional equation is

\[
 \rho_n(1-\rho_n)
 =\beta_n(1-\beta_n)+\gamma_n^2
   +i\gamma_n(1-2\beta_n),
\tag{119.2}
\]

which is real exactly when \(\beta_n=\tfrac12\) (apart from the irrelevant
case \(\gamma_n=0\)).  Replacing (119.2) by the real number in (119.1)
therefore discards precisely the horizontal displacement that RH asks to
exclude.

A self-adjoint operator whose spectrum is prescribed to be the real sequence
\(E_n\) can at most certify that sequence is real.  To infer RH one would need
an independently proved spectral correspondence identifying the complete
zero divisor with a transformation of the operator spectrum, including
\(\beta_n\), multiplicities, and the characteristic/determinant identity.
The preprint supplies none of these.  Its asserted \(J\)-symmetry is a
property of the newly constructed operator and does not reconstruct the
discarded real parts of the zeta zeros.

**Established:** a real sequence of ordinates can be used as input data for an
inverse spectral construction, subject to its actual hypotheses.

**Failure / missing step:** (119.1) is not spectral data encoding the full
complex zeros, and no determinant or divisor identity links the constructed
operator back to \(\xi(s)\).  Self-adjointness consequently has no RH-bearing
conclusion here.

**Route decision:** reject this appendix as an independent RH proof or as a
bridge to the valid Weil constraint.  The primary source-faithful Bombieri and
global Weil positivity gaps remain unchanged.

**RH status:** no unconditional proof has been produced.
