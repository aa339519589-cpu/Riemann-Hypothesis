## Round 203 — A/B result: the semilocal spectral-descent manuscript removes essential hypotheses

**Source inspected:** the six-page manuscript
work/semilocal-claimed-proof.pdf, together with the cited primary papers
<https://arxiv.org/abs/2511.22755> and
<https://arxiv.org/abs/2511.23257>.

The manuscript labels its Theorem 1 as unconditional.  The cited primary
paper's Theorem 1.1 instead begins with the assumptions that the smallest
eigenvalue \(\epsilon_N\) is simple and that its eigenvector \(\xi\) is even.
The same paper's Section 8 explicitly lists proving these two properties as
one of the two essential steps still missing for an RH proof.  The cited
Connes--van Suijlekom theorem likewise assumes a simple isolated extremal
eigenvalue and the required symmetry; it is not an unconditional theorem
that every truncation has the claimed real-zero structure.

The positivity inference also changes the form.  If
\(\epsilon_N\) is the smallest eigenvalue of \(Q_{W,\lambda}^N\), then
\[
Q_{W,\lambda}^N-\epsilon_N I\ge0
\]
holds by definition.  This does not imply
\[
Q_{W,\lambda}^N\ge0;
\]
the latter would additionally require \(\epsilon_N\ge0\), which is not
proved.  The primary Theorem 5.10 uses the shifted form
\(Q_{W,\lambda}^N-\epsilon_N I\) to construct a self-adjoint operator.  The
manuscript's sum-of-squares conclusion for the unshifted Weil form therefore
does not follow from the cited theorem.

The finite spectral parameters are also not identified with zeta zeros.
The primary paper proves, under its hypotheses, that the zeros of the
Fourier transform of a truncation eigenvector are real.  Its abstract and
Section 8 state that convergence of those finite spectra to the zeros of
\(\zeta(1/2+is)\) remains to be proved and that such a proof would establish
RH.  The manuscript supplies no determinant identity or zero-divisor
argument replacing this missing identification.

Finally, support stabilization of the prime terms for a fixed compactly
supported test function does not transfer positivity between the varying
\((N,\lambda,S)\) truncations.  The manuscript neither proves positivity of
the unshifted target form at each stage nor proves a compatible limit of the
finite spectral sums to that form.  Its numerical table cannot supply either
missing theorem.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
