## Round 168 — v2.4's own change log confirms the scalar bridge was clarified, not proved

The v2.3-to-v2.4 change log for Shimizu's manuscript describes the
scalar/cyclic addition as a \(K_R\)-side comparison of two realizations of a
universal Cauchy--Laplace coefficient object.  It explicitly lists the
ingredients as matrix-coefficient identities, finite cyclic contractions, and
the \(S_2\to S_1\) limit, while saying that no ordinary scalar
multiplicativity is asserted:

<https://zenodo.org/records/21108581/files/change_log.txt?download=1>

That clarification is consistent with the PDF, but it does not add the
missing map.  At fixed \(M,N,\ell\), the proof still needs a scalar-valued
restriction/lift \(R_{M,N}\) and a convergence statement of the form

\[
 R_{M,N}\Psi^{\mathrm{sc}}_{M,\ell}
   \longrightarrow \Psi^{\mathrm{sc}}_{M,\ell}
\quad\text{in the scalar test topology,}
\qquad
 \left\langle\mu^{\mathrm{fp,sc}}_{R,M},
 R_{M,N}\Psi^{\mathrm{sc}}_{M,\ell}\right\rangle
 =\operatorname{tr}(K_{M,N}^{\ell}).
\tag{168.1}
\]

Definitions 6.123--6.125 provide two realization maps from the universal
coefficient object into distinct scalar and cyclic/readout codomains; they do
not define \(R_{M,N}\) in (168.1).  Lemma 6.129 instead introduces
\(\Psi^{\mathrm{sc}}_{M,\ell;N}\) by saying that the ordinary scalar
coefficient is “obtained by restricting” it to the readout ledger, then
invokes that the ledger “exhausts” the coefficient.  No scalar topology
estimate or density/projection identity proves either assertion.  The
\(S_2\)-convergence of \(K_{M,N}\) controls only the cyclic matrix side; it
cannot by itself imply convergence of an independently defined ordinary
scalar test.

Therefore the revision makes the dependency language more explicit but leaves
the same fixed-level implication unproved.  The determinant comparison remains
conditional on (168.1), and the subsequent identity-theorem step cannot be
used to manufacture it.

**Established:** the latest revision records a type distinction and valid
finite cyclic algebra, but does not establish the ordinary scalar
restriction/lift required to connect that algebra to the classical
finite-part pairing.

**Remaining load-bearing statement:** prove (168.1) from the concrete scalar
and readout definitions, independently of the determinant target and of any
claimed \(F_K=\xi\) identity.

**RH status:** no unconditional proof has been produced.
