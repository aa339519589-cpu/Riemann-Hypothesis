## Round 148 — the scalar-to-cyclic trace bridge remains an asserted map

I audited the latest public abstract of Shimizu's preprint and the accessible
full text of its earlier version.  The public v8 page
(<https://www.preprints.org/manuscript/202505.2110>) describes a chain using
finite-window scalar coefficients, cyclic tensor contractions, finite-rank
compression, and a Hilbert--Schmidt limit, and then states a central
derivative equality.  The page is marked not peer-reviewed and does not
display the derivation of the scalar-to-cyclic equality.  The full v6 text
(<https://www.preprints.org/frontend/manuscript/137a4b503f7abf9be3cae4a2bc24c6bd/download_pub>)
does expose the relevant type distinction and the exact bridge assertion, so
it provides a concrete audit target.  This does not by itself prove that every
line of v8 is unchanged; it identifies the theorem that a revised version
must supply.

The construction first keeps two different objects separate.  The scalar
coefficient functional has entries

\[
 c_{ab}=\mu_{\mathrm{sc}}(\Omega_{ab})
       =\langle K_M e_b,e_a\rangle ,
\tag{148.1}
\]

whereas the cyclic tensor lift multiplies matrix entries around a cycle.
Consequently its length-\(\ell\) contraction is

\[
 \operatorname{Tr}(K_M^\ell)
 =\sum_{a_1,\ldots,a_\ell}
   c_{a_1a_2}c_{a_2a_3}\cdots c_{a_\ell a_1}.
\tag{148.2}
\]

The full text then asserts, in the proof of its scalar/cyclic comparison
lemma, that the “finite central readout ledger exhausts”
\(\Psi^{\mathrm{sc}}_{M,\ell}\), and uses that assertion to conclude

\[
 \mu_{\mathrm{sc}}\!\left(\Psi^{\mathrm{sc}}_{M,\ell}\right)
   =\operatorname{Tr}(K_M^\ell).
\tag{148.3}
\]

The word “exhausts” is the load-bearing map.  The preceding matrix-entry
identity (148.1) gives only one application of the scalar functional to each
readout \(\Omega_{ab}\); it does not, by linearity alone, turn a scalar
functional into the multilinear cyclic contraction (148.2).  A finite
dimensional check makes the missing content explicit.  If the ordinary
scalar coefficient were represented by a functional-independent linear
combination

\[
 \Psi^{\mathrm{sc}}_{M,2}
   =\sum_{a,b}q_{ab}\Omega_{ab},
\]

then

\[
 \mu_{\mathrm{sc}}(\Psi^{\mathrm{sc}}_{M,2})
   =\sum_{a,b}q_{ab}c_{ab}
\]

would be linear in the matrix entries, while

\[
 \operatorname{Tr}(K_M^2)=\sum_{a,b}c_{ab}c_{ba}
\]

is quadratic.  Equality on a nontrivial family therefore requires an
additional, proved structure: either a special identity constraining the
admissible \(c_{ab}\), or coefficients \(q_{ab}\) that themselves depend on
the same \(K_M\).  The latter would be a \(K_M\)-dependent reconstruction and
would make (148.3) definitional/circular unless its compatibility with the
ordinary scalar Cauchy--Laplace coefficient is independently established.
The text's assertion that the finite readout ledger exhausts the scalar
coefficient does not provide that representation, its coefficients, or the
independence argument.

The one-dimensional version shows the same issue without notation.  Let
\(\mu(\Omega)=c\) and let \(e\) be an independent scalar direction.  Nothing
about the value on \(\Omega\) forces \(\mu(e)=c^2\), although the cyclic trace
of the one-dimensional operator \([c]\) is \(c^2\).  If instead
\(e=q\Omega\) with fixed \(q\), then \(\mu(e)=qc\), still not \(c^2\) for a
variable \(c\).  A theorem identifying the specific scalar coefficient with
the required \(K_M\)-dependent direction is therefore indispensable.

This gap occurs before the claimed equality of the scalar explicit-formula
derivative with the self-adjoint determinant derivative.  The later
Hilbert--Schmidt convergence and identity-theorem steps cannot repair a
missing equality of the finite-window quantities.  Thus the latest public
description is a research claim, not an unconditional RH proof, and the
scalar-to-cyclic spectral bridge remains unclosed.

**Established:** the exact missing statement is a scalar-to-cyclic
compatibility theorem proving (148.3) for the ordinary scalar coefficient,
with explicit maps and domains, independently of defining that coefficient
from \(K_M\).  The accessible full text states this as “exhaustion” but does
not supply the required representation or proof.

**Remaining load-bearing statement:** prove that bridge for the actual
explicit-formula functional, then prove that the resulting self-adjoint
operator determinant is globally the classical \(\xi\)-function.  Without
both steps, the spectral route does not close RH.

**RH status:** no unconditional proof has been produced.
