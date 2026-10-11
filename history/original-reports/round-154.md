## Round 154 — Lemma 6.129 has an unresolved scalar/cyclic type bridge

The latest v2.4 definitions make the codomain distinction explicit.  The
ordinary coefficient is introduced as
\[
 \Psi^{\mathrm{sc}}_{M,\ell}\in\mathcal C^{\mathrm{sc}}_{\mathrm{CL}},
\]
the ordinary scalar Cauchy--Laplace comparison space.  Separately, the cyclic
coefficient is a tensor object
\[
 \Psi^{(\ell)}_M\in\mathcal C^{(\ell)}_{\mathrm{cyc},M},
\]
and Definition 6.128 places
\[
 \Omega_{a_1a_2}\odot_M\cdots\odot_M\Omega_{a_\ell a_1}
\]
in that cyclic tensor channel.  The source deliberately says that the two
codomains are not identified (v2.4 PDF, printed pp. 258--263:
<https://zenodo.org/records/21108581/files/UEE_00a_Proof_of_the_Riemann_Hypothesis_English_v2.4.pdf?download=1>).

Accordingly, the valid cyclic equation is
\[
 \left\langle\mu^{\mathrm{fp,(\ell)}}_{R,M},
 \Psi^{(\ell)}_{M,N}\right\rangle
 =\operatorname{tr}(K_{M,N}^{\ell}),
\tag{154.1}
\]
where the left side uses the tensor-lift functional.  The scalar equation
needed by the determinant comparison is instead
\[
 \left\langle\mu^{\mathrm{fp,sc}}_{R,M},
 \Psi^{\mathrm{sc}}_{M,\ell;N}\right\rangle
 =\operatorname{tr}(K_{M,N}^{\ell}).
\tag{154.2}
\]
There is no displayed map
\[
 \mathfrak b_{M,N,\ell}:
 \mathcal C^{\mathrm{sc}}_{\mathrm{CL}}
 \longrightarrow \mathcal C^{(\ell)}_{\mathrm{cyc},M}
\]
and no proof that
\(\mathfrak b_{M,N,\ell}(\Psi^{\mathrm{sc}}_{M,\ell;N})\) is the ordered
cyclic tensor used in (154.1).  Without such a map, the two pairings in
(154.1)--(154.2) are evaluations in different spaces and cannot be equated
by the phrase “coefficient contraction.”

If the symbol \(\odot_M\) is replaced by ordinary pointwise multiplication
of scalar tests, a different missing statement appears:
\[
 \Psi^{\mathrm{sc}}_{M,\ell;N}
 \stackrel{?}{=}
 \sum_{a_1,\ldots,a_\ell}
 \Omega_{a_1a_2}\cdots\Omega_{a_\ell a_1}
\quad\text{in }\mathcal C^{\mathrm{sc}}_{\mathrm{CL}},
\tag{154.3}
\]
followed by a proof that the ordinary scalar functional evaluates (154.3)
as the product of its one-factor values.  The latter is precisely a
multiplicativity property and is explicitly disclaimed by the source.  The
one-dimensional model in Round 153 shows that (154.3) plus the matrix
readout still does not imply (154.2).

**Established:** the cyclic trace calculation is well-typed in its tensor
channel, but the scalar equation used to identify it with the
Cauchy--Laplace transform is not connected to that channel by a defined
map or a proved scalar expansion.

**Remaining load-bearing statement:** supply the missing scalar-to-cyclic
bridge map (or a direct scalar expansion), prove its compatibility for every
\(M,N,\ell\), and then prove the scalar limits before using the determinant
trace in the \(\xi\)-comparison.

**RH status:** no unconditional proof has been produced.
