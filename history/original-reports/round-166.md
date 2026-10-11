## Round 166 — exact finite Guinand--Weil dictionaries do not supply global positivity

I also audited Akiva Groskin's latest version of *A finite Guinand--Weil
dictionary and archimedean tail order for the truncated Weil quadratic form*
(arXiv:2607.02828v3):

<https://arxiv.org/abs/2607.02828>

The paper gives a useful finite theorem.  For fixed prime cutoff \(c\), finite
frequency band \(N\), and a finite Galerkin vector \(v\), it constructs an
explicit band-limited test function \(g_v\) and proves the exact identity

\[
 \langle v,Q_\infty v\rangle
   =\sum_{\zeta(1/2+iz)=0}^{*}g_v(z).
\tag{166.1}
\]

It also bounds the omitted archimedean integral when that integral is
numerically cut off at \(T\), so that a finite-\(T\) sign can certify the sign
of the corresponding fixed cutoff-free matrix eigenvalue once it lies outside
the error interval.  These are finite-dimensional, source-faithful results.

They do not establish the needed global statement.  The zero-side identity
(166.1) is available only for the induced finite family \(g_v\); the paper
explicitly makes no claim that arbitrary Guinand--Weil tests are realized by
this family.  More importantly, positivity of one matrix (or of any finite
list of matrices) proves only positivity on its finite-dimensional Galerkin
space.  To obtain Weil positivity one would still need a theorem covering all
frequency bands \(N\) (and the relevant prime-cutoff limit), together with the
required density/closure passage.  The archimedean tail budget controls \(T\)
for fixed \(c,N\); it supplies no uniform lower bound as \(N\to\infty\).

Thus the exact finite dictionary and the tail-order estimate calibrate finite
numerics, but they do not prove positivity of the full Weil quadratic form and
do not close the RH implication.  This is a separate finite-truncation
obstruction from the scalar--cyclic bridge in Rounds 159--164.

**Established:** the candidate closes a finite cutoff-error problem and
provides exact finite zero-sum identities; it does not provide the all-band
positivity theorem required for RH.

**Remaining load-bearing statement:** prove global positivity for the full
admissible Weil test space, or prove an equivalent uniform theorem over every
finite band and every limiting parameter.  No such theorem has been obtained.

**RH status:** no unconditional proof has been produced.
