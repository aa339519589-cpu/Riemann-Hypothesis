## Round 163 — the alleged scalar restriction changes the data source

The definitions also expose a dependency-direction problem in the phrase
“restricting the ordinary scalar coefficient to the finite central readout
ledger.”  The ordinary coefficient \(\Psi^{\mathrm{sc}}_{M,\ell}\) is fixed by
the central kernel \(h_w\), the cutoff \(\chi_M\), and the finite-jet operator
\(Q_M^{\mathrm{cen}}\) (Definitions 6.91--6.99).  Those data are fixed before
the pairings and before the determinant construction.  In contrast, the
readout tests \(\omega^{\mathrm{cen}}_{M,ij}\) and \(B_M(x,y)\) are built from
the \(K\)-side comparison range, its Gram matrix, and the Riesz coordinates
(Definitions 6.124--6.125).  They therefore depend on the \(K\)-side data.

Thus an \(N\)-dependent object obtained by expanding or contracting against
that readout ledger is not automatically the already-defined scalar coefficient:

\[
 \Psi^{\mathrm{sc}}_{M,\ell}
 \quad\text{(fixed by the scalar regularization)},
 \qquad
 \Psi^{\mathrm{sc}}_{M,\ell;N}
 \quad\text{(defined using the \(K\)-dependent ledger)}.
\tag{163.1}
\]

To identify them, the proof needs a K-independent scalar equality such as

\[
 \Psi^{\mathrm{sc}}_{M,\ell;N}
   =\Psi^{\mathrm{sc}}_{M,\ell}
 \quad\text{or at least}\quad
 \Psi^{\mathrm{sc}}_{M,\ell;N}\longrightarrow
 \Psi^{\mathrm{sc}}_{M,\ell}
\tag{163.2}
\]

in the ordinary scalar test topology, followed by continuity of the scalar
functional.  The source gives neither (163.2) nor a definition of the relevant
projection.  Instead, it immediately evaluates the new object by the cyclic
matrix contraction and then calls the result the ordinary scalar coefficient.

This is a data-source substitution, not merely a missing estimate.  A
K-dependent projection can always be chosen to force a selected scalar pairing
to equal \(\operatorname{Tr}(K^\ell)\); such a construction proves only the
properties of the projection it defines.  It proves the desired determinant
comparison only if the projection is independently shown to be the fixed
ordinary scalar regularization.  The finite-dimensional model in Round 161
shows that the readout identities alone do not supply that identification.

**Established:** the source's scalar coefficient and its finite readout ledger
are constructed from different data, with the latter depending on the operator
whose determinant is to be identified.  No K-independent equality or convergence
of the ledger restriction to the ordinary scalar coefficient is proved.

**Remaining load-bearing statement:** establish (163.2), or an equivalent
K-independent map from the ordinary scalar Cauchy--Laplace coefficient to the
readout channel, before using the cyclic trace contraction.  Without it,
Theorem 6.144 remains conditional.

**RH status:** no unconditional proof has been produced.
