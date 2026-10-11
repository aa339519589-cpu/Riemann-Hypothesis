## Round 128 — the Shimizu v2.4 scalar-to-cyclic trace bridge is not independently established

I audited the current v2.4 manuscript *Proof of the Riemann Hypothesis*,
[Zenodo record 21108581](https://zenodo.org/records/21108581), especially the
argument on the manuscript pages numbered 260--271 (PDF pages 261--272).
The decisive point is Theorem 6.144, which is supposed to identify the
operator-side finite-part functional with

\[
 G_K(w)=w\,\operatorname{Tr}\!\left((I+iwK)^{-1}K^2\right).
\tag{128.1}
\]

The finite-dimensional algebra used after an actual matrix coefficient has
been supplied is correct:

\[
\sum_{a_1,\ldots,a_\ell}
 K_{a_1a_2}K_{a_2a_3}\cdots K_{a_\ell a_1}
=\operatorname{tr}(K^\ell).
\tag{128.2}
\]

But the missing implication is precisely the supply of those products from
the original scalar test family.  Definition 6.128 introduces a new
cyclic-tensor functional by stipulating

\[
 \left\langle\mu_R^{\mathrm{fp},(\ell)},
 \Omega_1\mathbin{\odot}\cdots\mathbin{\odot}\Omega_\ell\right\rangle
 :=
 \prod_{j=1}^{\ell}
 \left\langle\mu_R^{\mathrm{fp},\mathrm{sc}},\Omega_j\right\rangle.
\tag{128.3}
\]

This is a newly defined tensor-channel functional; it is explicitly not
claimed to be multiplication of the original scalar distribution.  The
subsequent Lemma 6.129 then asserts that a scalar coefficient
\(\Psi^{\mathrm{sc}}_{M,\ell}\) and a separately defined cyclic coefficient
\(\Psi^{(\ell)}_M\) both evaluate to
\(\operatorname{Tr}(K_M^\ell)\).  The proof obtains (128.2) for the cyclic
coefficient by construction.  For the scalar coefficient, however, it says
that the “finite central readout ledger” is restricted to the pairwise matrix
readouts and that its coefficient contraction is the cyclic matrix
contraction.  No independent theorem is given that the ordinary scalar
Cauchy--Laplace coefficient \(\Psi^{\mathrm{sc}}_{M,\ell}\) is equal, in the
scalar test space and under the original scalar functional, to that
\(\ell\)-fold tensor contraction.

The type distinction does not repair this.  Theorem 6.130 compares the two
realizations only after pulling them back to a universal coefficient object,
and Theorem 6.132 transports the finite-window scalar equality through that
same notation.  A pullback equality is useful only after both realization
maps and the coefficient images have been independently specified.  Here the
cyclic image is built so that (128.3) produces trace powers, while the
required scalar image-to-cyclic compatibility is the unproved bridge.  An
abstract finite-dimensional countermodel makes the logical issue explicit:
given a self-adjoint matrix \(K\), one may define a scalar family
\(e_\ell\) and a scalar functional with arbitrary values
\(\mu(e_\ell)=a_\ell\), while separately defining a cyclic tensor lift by
(128.3).  Nothing forces \(a_\ell=\operatorname{Tr}(K^\ell)\) unless an
additional map identifying \(e_\ell\) with the cyclic contraction is proved.

Therefore Theorem 6.144 does not follow from the displayed finite trace
identity.  Without it, the manuscript has only a self-adjoint
Hilbert--Schmidt operator \(K\) and a separately defined scalar
explicit-formula residual; it has not proved that the regularized determinant
of \(K\) has the same central logarithmic derivative as \(\xi\).  The later
identity \(F_K\equiv\xi\) and the final RH conclusion depend on exactly this
missing identification.  The Zenodo record itself labels the manuscript a
working draft and states that fatal proof errors remain; that warning is
consistent with this unresolved scalar/cyclic step.

**Established:** the cyclic matrix contraction (128.2) and the
Hilbert--Schmidt determinant calculus are valid once their matrix data are
given.

**Failure / missing lemma:** no source-independent construction proves that
the original scalar finite-part Cauchy--Laplace coefficients equal the
newly-defined cyclic tensor coefficients.  Defining the latter by products
does not prove that equality.

**Remaining load-bearing statement:** provide an independently defined scalar
coefficient map and prove its exact compatibility with the cyclic tensor
contraction, with all limits and pairings controlled, before claiming
\(\mu_R^{\mathrm{fp}}=\mu_L^{\mathrm{det}}\) or \(F_K=\xi\).

**RH status:** no unconditional proof has been produced.

**RH status:** no unconditional proof has been produced.
