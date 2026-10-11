## Round 124 — the infinite off-line branch is not closed by growing negative inertia

Bombieri's introduction explicitly separates the finite-exception and
infinite-exception possibilities: after the RH alternative, one possibility is
infinitely many nontrivial zeros off the critical line, and the other is a
limiting local linear relation among the zero monomials.  This distinction
matters for the finite-section argument.

Let \(H_N\) denote the finite Section-11 matrix on the first \(N\) zero
coordinates.  The finite symmetric-set theorem gives a negative direction for
each off-line conjugate/reflection block, so if infinitely many zeros are
off-line the negative inertia of the finite matrices is unbounded (with the
source's multiplicity convention).  The implication

\[
 n_-(H_N)\longrightarrow\infty
 \quad\Longrightarrow\quad
 \text{a fixed negative eigenvalue of an infinite Weil operator}
 \tag{124.1}
\]

is not automatic.  It would require a common Hilbert-space operator, a
closed form domain, and a self-adjoint compression/interlacing theorem with
uniform control of the eigenvectors.  The off-line Section-11 matrices are
not ordinary Hermitian Gram matrices in the standard coefficient inner
product, as shown in Round 122; their real eigenvalue theorem does not supply
that missing structure.

There are therefore two spectral subcases for the source-selected negative
branch.  If a subsequence has
\[
 \lambda_N\leq-\delta<0,
\]
then the absolute-summability/compactness argument of Round 45 gives a
nonzero limiting eigenvector and a genuine negative infinite operator value.
That would be the desired RH obstruction.  If instead
\[
 \lambda_N\longrightarrow0,
\]
the negative directions can escape into the growing coordinate tail.  The
finite negative inertia does not prevent this, and the source's limiting
equation becomes a local linear relation whose coefficient class and
off-line mass must still be analyzed.

In the infinite-off-line case the latter relation is harder than the finite
packet problem.  It has infinitely many off-line terms, and ordinary
linear independence of distinct monomials is not applicable to a merely
convergent series on a bounded interval.  The exact weighted range criterion
in (103.4) controls a prescribed \(\ell^2\) coefficient class, but no
zeta-specific theorem has been proved that excludes all such infinite
relations.  Positive-density theorems for critical-line zeros likewise do
not exclude a residual infinite off-line set.

Thus the infinite branch can be closed only by a new uniform spectral
estimate, a complete local-series uniqueness theorem in the source's actual
coefficient topology, or direct positivity of the full Weil form.  Counting
negative eigenvalues, finite numerical spectra, and nested coordinate sets
provide none of these.

**Established:** unbounded finite negative inertia records the presence of
many off-line finite blocks, but does not by itself produce a tight negative
limit or a global Weil witness.

**Remaining load-bearing statement:** rule out both the bounded-away-from-zero
subsequence and the zero-collapse infinite local-relation branch, with the
source normalization and convergence proved.

**RH status:** no unconditional proof has been produced.
