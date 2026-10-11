## Round 150 — latest v2.4 audit: conjugation is correct, while the scalar expansion is still omitted

I checked the author's latest Zenodo release rather than relying only on the
older Preprints.org extraction.  The v2.4 record is
<https://zenodo.org/records/21108581>; its change log identifies the release
as the public-response consolidation v8 and says that the headline theorem was
retained.  The same record still carries the author's disclaimer that the
manuscript is a working draft containing fatal errors within the proofs.  The
change log is at
<https://zenodo.org/records/21108581/files/change_log.txt?download=1>.

The visual PDF check also corrects a possible false lead.  In the original
v2.4 PDF, Definition 2.1 uses the standard complex inner product with
\(\overline{g(x)}\), and the matrix readout later uses
\(x_i\overline{y_j}\).  Thus the apparent missing conjugation in text
extraction is an extraction artifact, not an additional mathematical defect.

The latest v2.4 pages containing the scalar/cyclic lemma preserve the exact
distinction recorded in Rounds 148--149.  The valid part is:

\[
 c_{ab}
 =\left\langle\mu^{\mathrm{fp,sc}}_{R,M},\Omega_{ab}\right\rangle
 =\langle K_Me_b,e_a\rangle .
\tag{150.1}
\]

For the explicitly defined ordered cyclic tensor

\[
 \mathcal C^{(\ell)}_{M,N}
 =\sum_{a_1,\ldots,a_\ell=1}^{N}
 \Omega_{a_1a_2}\odot_M\Omega_{a_2a_3}
 \odot_M\cdots\odot_M\Omega_{a_\ell a_1},
\]

the tensor-lift definition then gives the valid finite identity

\[
 \left\langle\mu^{\mathrm{fp,(\ell)}}_{R,M},
 \mathcal C^{(\ell)}_{M,N}\right\rangle
 =\sum_{a_1,\ldots,a_\ell}
 c_{a_1a_2}\cdots c_{a_\ell a_1}
 =\operatorname{tr}_{E_N}(K_{M,N}^{\ell}).
\tag{150.2}
\]

The unresolved line is the scalar one.  The proof introduces
\(\Psi^{\mathrm{sc}}_{M,\ell;N}\) as the \(E_N\)-truncated *ordinary scalar*
Cauchy--Laplace coefficient “obtained by restricting” it to the finite
central readout ledger.  It immediately states that its coefficient
contraction is the right side of (150.2), and then passes to
\(\operatorname{Tr}(K_M^\ell)\).  It does not display the scalar test-object
equality that would justify this contraction.

The precise obligation is therefore to construct, for every \(M,N,\ell\), the
map or coefficient identity

\[
 \Psi^{\mathrm{sc}}_{M,\ell;N}
 =\mathcal Q_{M,N,\ell}\bigl(\{\Omega_{ab}\}\bigr)
\]

inside the ordinary scalar Cauchy--Laplace test space, with
\[
 \left\langle\mu^{\mathrm{fp,sc}}_{R,M},
 \mathcal Q_{M,N,\ell}\bigl(\{\Omega_{ab}\}\bigr)\right\rangle
 =\sum_{a_1,\ldots,a_\ell}
 c_{a_1a_2}\cdots c_{a_\ell a_1},
\]
and to prove that this construction is the same ordinary scalar coefficient
coming from \(h_w(u)=(e^{wu}-1)/u\), not a \(K\)-dependent scalar test defined
after the determinant trace is known.  The latest text contains the readout
identity (150.1) and the tensor-lift calculation (150.2), but the displayed
“ledger exhausts” sentence is not this missing map or proof.

This is now a sharply delimited gap, not a claim that the finite cyclic
calculation is wrong.  If the author supplies the omitted scalar
coefficient-level construction and its \(N,M\) compatibility, this particular
objection is discharged.  Until then, the K-side determinant trace cannot be
identified with the ordinary scalar explicit-formula transform, so the
subsequent equality \(F_K\equiv\xi\) is not established.

**Established:** the latest v2.4 PDF has the correct complex conjugation
convention, and its finite tensor-lift trace identity is mathematically
coherent as a conditional K-side calculation.

**Remaining load-bearing statement:** provide and verify the ordinary scalar
coefficient expansion just described, then close the determinant-to-\(\xi\)
identity and the global spectral conclusion.  The author-side v2.4 disclaimer
also independently confirms that the released manuscript is not a completed
proof.

**RH status:** no unconditional proof has been produced.
