## Round 161 — finite-dimensional hostile model for the missing restriction

The fixed-window gap can be stated as an explicit algebraic countermodel to the
inference used in Lemma 6.129.  Fix a finite-dimensional space \(E\), a
self-adjoint matrix \(K\) on \(E\), and let \(W\) be the finite-dimensional
span of all first-order readout tests \(\omega^{\mathrm{cen}}_{M,ij}\) used by
the Gram construction.  Adjoin one independent vector \(q\) and set

\[
 V=W\oplus\mathbb Cq.
\tag{161.1}
\]

Define a linear functional \(\mu:V\to\mathbb C\) on \(W\) so that

\[
 \mu\bigl(B_M(x,y)\bigr)=\langle x,y\rangle
 \tag{161.2}
\]

for every readout vector \(x,y\), exactly as in Lemma 6.126.  This fixes all
one-factor matrix readouts and therefore fixes the finite cyclic contraction

\[
 \sum_{a_1,\ldots,a_\ell}
 c_{a_1a_2}\cdots c_{a_\ell a_1}
 =\operatorname{tr}(K_{M,N}^{\ell}).
\tag{161.3}
\]

But define \(\mu(q)=t\), where \(t\in\mathbb C\) is arbitrary.  Every
readout identity (161.2), every finite matrix trace identity (161.3), and the
linear functional axioms remain true for every value of \(t\).  Choosing
\(q=\Psi^{\mathrm{sc}}_{M,2}\) models precisely the ordinary scalar
coefficient; Lemma 6.129 would require the extra condition

\[
 t=\mu\!\left(\Psi^{\mathrm{sc}}_{M,2}\right)
 =\operatorname{Tr}(K_M^2).
\tag{161.4}
\]

Nothing in Definitions 6.120--6.125 or Lemmas 6.126--6.127 forces the
ordinary scalar coefficient to lie in \(W\), or forces its value to be the
cyclic polynomial.  If the actual function-space construction is intended to
exclude the independent direction \(q\), it must prove that exclusion by an
explicit scalar expansion or a density/projection theorem.  Merely naming the
finite collection a “readout ledger” does not do so.

This model is not a counterexample to the zeta function and makes no claim
about the actual value of the scalar coefficient.  It is a hostile logical
check: the premises cited before the scalar-to-cyclic step admit models with
identical matrix data and different scalar values.  Therefore the missing
identity is an additional mathematical premise, not a consequence of finite
dimensionality, Riesz reconstruction, or \(S_2\)-convergence.

**Established:** the one-factor readout and cyclic trace identities leave the
ordinary scalar coefficient undetermined unless an explicit restriction map or
span/evaluation theorem is added.

**Remaining load-bearing statement:** prove that the concrete
\(\Psi^{\mathrm{sc}}_{M,\ell}\) belongs to the finite readout image with the
claimed cyclic evaluation, beginning with \(\ell=2\); then prove its stability
under the \(N\)- and \(M\)-limits.

**RH status:** no unconditional proof has been produced.
