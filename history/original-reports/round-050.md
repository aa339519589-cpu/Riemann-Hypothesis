## Round 50 — audit of the Zenodo 20518741 self-adjoint determinant claim

I also checked the revised manuscript at
https://zenodo.org/records/20518741. Its proposed closure has a precise
scalar/tensor gap in Lemmas 6.124--6.138.

The manuscript first obtains a scalar matrix-readout identity. In its notation,
for scalar finite-part evaluation \(\mu^{\mathrm{sc}}\) and matrix-coordinate tests
\(\Omega_{ab}\), one has

\[
 \mu^{\mathrm{sc}}(\Omega_{ab})=\langle K_M e_b,e_a\rangle.
\tag{50.1}
\]

This is one value of one linear functional. It then introduces a different
tensor-channel functional by definition:

\[
 \mu^{(\ell)}(\Omega_1\mathbin{\odot}\cdots\mathbin{\odot}\Omega_\ell)
 =\prod_{j=1}^{\ell}\mu^{\mathrm{sc}}(\Omega_j).
\tag{50.2}
\]

The cyclic contraction in (50.2) does give
\(\operatorname{Tr}(K_M^\ell)\); that is a valid finite-dimensional tensor
calculation. The manuscript then asserts that the *ordinary scalar*
Cauchy--Laplace coefficient has the same value:

\[
 \mu^{\mathrm{sc}}(\Psi^{\mathrm{sc}}_{M,\ell})
 =\operatorname{Tr}(K_M^\ell).
\tag{50.3}
\]

No multiplicativity theorem for the scalar functional is supplied. Linearity
and (50.1) only determine evaluations of linear combinations of the
\(\Omega_{ab}\); they do not turn one scalar evaluation into products of
evaluations. The product in (50.2) belongs to a tensor lift, not to the
ordinary scalar test space.

There are only two possible readings, and neither closes the gap. If
\(\Psi^{\mathrm{sc}}_{M,\ell}\) is defined by a \(K_M\)-dependent linear
combination chosen so that (50.3) holds, then it is no longer shown to be the
ordinary \(\ell\)-th coefficient of the scalar Cauchy--Laplace family, and the
claimed scalar expansion in Lemma 6.130 is missing. If it is the ordinary
scalar coefficient, then (50.3) needs an independent scalar-to-tensor
multiplicativity/realization theorem, which is absent.

Therefore the determinant trace bridge in Theorem 6.138 is not established.
The later local logarithmic-derivative identity, \(F_K=\xi\), and the
self-adjoint spectral localization all depend on that bridge. The manuscript's
self-adjoint Hilbert--Schmidt construction alone only gives a determinant whose
own nonzero spectral factors are on the critical line; it does not identify
that determinant with the completed zeta function.

**Established:** the finite-dimensional cyclic identity (50.2) implies the
trace of \(K_M^\ell\) inside the separately defined tensor channel.

**Failure / error:** the unproved identification (50.3) conflates scalar
linearity with tensor multiplicativity.

**RH status:** this candidate is not an unconditional proof.
