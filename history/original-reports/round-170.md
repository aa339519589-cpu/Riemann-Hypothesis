## Round 170 — the full-source scan finds no earlier scalar-to-readout bridge

I scanned the complete v2.4 source, not only the paragraphs cited by Lemma
6.129.  The earlier occurrences of “restriction” have different types: the
Section 4 occurrences are restrictions of closed forms, operators, or seam
traces, while Lemma 6.17 and Lemma 6.24 concern the open-band space
\(A_\eta\).  None of those constructs a map from the ordinary scalar
Cauchy--Laplace coefficient space into the finite central readout channel.

The scalar/cyclic block has the type sequence

\[
 UCL(r)\xrightarrow{\,\iota_M^{\mathrm{sc}}\,}C^{\mathrm{sc}}_{CL}(r),
 \qquad
 UCL(r)\xrightarrow{\,\iota_M^{\mathrm{cyc}}\,}C^{\mathrm{cyc}}_M(r),
\tag{170.1}
\]

and separately constructs

\[
 \omega^{\mathrm{cen}}_{M,ij}\in C^{(1)}_{\mathrm{rd},M},
 \qquad
 \Omega_M(f,g)=\sum_{i,j}x_i y_j\omega^{\mathrm{cen}}_{M,ij}.
\tag{170.2}
\]

Definitions 6.120--6.128 establish finite-window restriction of the
functionals, the matrix readout \(B_M\), the scalar matrix-coefficient
identity, and the cyclic tensor lift.  They do not define a coefficient map of
the needed form

\[
 R_{M,N}:C^{\mathrm{sc}}_{CL}(r)\longrightarrow
 C^{(1)}_{\mathrm{rd},M}
 \quad\text{or}\quad
 R_{M,N}\Psi^{\mathrm{sc}}_{M,\ell},
\tag{170.3}
\]

with a scalar-topology convergence theorem.  The first relevant occurrence is
inside the proof of Lemma 6.129 (printed pages 261--263):
\(\Psi^{\mathrm{sc}}_{M,\ell;N}\) is said to be obtained by “restricting” the
ordinary scalar coefficient to the readout ledger, and the ledger is then said
to “exhaust” that coefficient.  The following contraction is a valid finite
matrix calculation once this identification is granted; it does not define
the identification.  Theorem 6.130 restates the result, and Theorem 6.144
invokes Lemma 6.129 and Theorem 6.130, so the later uses do not supply an
independent proof.

Thus the scan rules out a hidden earlier lemma as the missing repair.  The
remaining obligation is exactly (170.3), together with

\[
 \Psi^{\mathrm{sc}}_{M,\ell;N}\to
 \Psi^{\mathrm{sc}}_{M,\ell}
 \quad\text{in the scalar comparison topology},
 \qquad
 \left\langle\mu^{\mathrm{fp,sc}}_{R,M},
 \Psi^{\mathrm{sc}}_{M,\ell;N}\right\rangle
 =\operatorname{tr}(K_{M,N}^{\ell}).
\tag{170.4}
\]

The source's finite cyclic identities prove the right-hand trace formula in
their own tensor channel.  They do not prove (170.3)--(170.4) for the
independently defined ordinary scalar coefficient.  Consequently the
scalar--cyclic equality used by the determinant comparison remains an
asserted load-bearing lemma rather than a closed derivation.

**Established:** no earlier source theorem supplies the missing scalar
restriction/lift; the only relevant construction is the unsupported
“restrict/exhaust” step in Lemma 6.129 and its later repetitions.

**Remaining load-bearing statement:** prove (170.3)--(170.4) from the ordinary
scalar coefficient and the readout definitions, without defining the map from
the desired trace identity.

**RH status:** no unconditional proof has been produced.
