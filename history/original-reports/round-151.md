## Round 151 — “ledger exhausts” is not a defined projection or density theorem

The latest v2.4 proof makes the remaining finite-window issue even more
precise.  In the proof of its scalar/cyclic Lemma 6.129 (printed pp. 261--262
in the PDF
<https://zenodo.org/records/21108581/files/UEE_00a_Proof_of_the_Riemann_Hypothesis_English_v2.4.pdf?download=1>),
it introduces an \(E_N\)-truncated ordinary scalar coefficient
\(\Psi^{\mathrm{sc}}_{M,\ell;N}\) by saying that the ordinary coefficient is
“restricted” to the finite central readout ledger
\(\{\omega^{\mathrm{cen}}_{M,ij}\}\).  It then states that the ledger
“exhausts” \(\Psi^{\mathrm{sc}}_{M,\ell}\).

That phrase is not yet a mathematical approximation result.  A finite list of
readout tests does not automatically define a projection on the infinite
dimensional ordinary scalar Cauchy--Laplace test space.  To make the step
valid, the proof must specify:

\[
 P^{\mathrm{sc}}_{M,N}:
 \mathcal C_{\mathrm{CL}}(r)\longrightarrow
 \operatorname{span}\{\omega^{\mathrm{cen}}_{M,ij}\},
\]

show that this map is well-defined (including the null space and any
Moore--Penrose convention), and prove

\[
 P^{\mathrm{sc}}_{M,N}\Psi^{\mathrm{sc}}_{M,\ell}
 \longrightarrow \Psi^{\mathrm{sc}}_{M,\ell}
\quad\text{in the stated central comparison topology}.
\tag{151.1}
\]

Only after (151.1), together with continuity of
\(\mu^{\mathrm{fp,sc}}_{R,M}\), can one pass from the finite ledger pairing to
the ordinary scalar pairing.  The Gram/Riesz inverse in the text reconstructs
dual vectors in the finite boundary comparison range; it does not, by itself,
construct \(P^{\mathrm{sc}}_{M,N}\) on the full scalar Cauchy--Laplace space or
prove (151.1).  The proof supplies the finite cyclic contraction and the
Hilbert--Schmidt trace limit, but not this scalar projection/density theorem.

The logical independence can be demonstrated without any zeta model.  Let
\[
 V_N=\operatorname{span}\{\omega_1,\ldots,\omega_{d_N}\}
\]
be the finite ledger and let \(e\) be an independent ordinary scalar direction.
Define a linear functional by
\[
 \mu(\omega_j)=c_j,\qquad \mu(e)=t,
\]
where \(t\) is arbitrary.  All finite readout identities, including any
matrix-trace identity formed from the \(c_j\), remain unchanged as \(t\) varies.
Nevertheless \(\mu(e)\) is not determined by those identities.  If a topology
and projections are supplied for which \(P_Ne\to e\), continuity of \(\mu\)
would determine \(t\); absent that theorem, the assertion that the ledger
exhausts \(e\) is an additional premise.

There is a second fork.  If the author defines \(P^{\mathrm{sc}}_{M,N}\) using
the \(K_M\)-dependent coefficients that force
\[
 \mu(P^{\mathrm{sc}}_{M,N}\Psi^{\mathrm{sc}}_{M,\ell})
 =\operatorname{tr}(K_{M,N}^{\ell}),
\]
then the resulting object is a determinant-side reconstruction.  It still
needs an independent proof that it equals the ordinary coefficient obtained
from \(h_w(u)=(e^{wu}-1)/u\).  Otherwise the trace equality is a valid
identity for a newly defined readout object, not an identification with the
classical scalar explicit-formula transform.

**Established:** the finite readout and cyclic trace calculations can be
correct, and the author has not made the earlier conjugation error suggested by
text extraction.  The unresolved scalar step is specifically the definition
and convergence of the finite-ledger approximation \(P^{\mathrm{sc}}_{M,N}\).

**Remaining load-bearing statement:** prove (151.1) for the ordinary scalar
Cauchy--Laplace coefficient with all \(M,N\) compatibilities, then combine it
with the classical explicit-formula comparison and the global determinant
identification.  The released v2.4 record itself still labels the manuscript a
working draft with fatal proof errors; no unconditional RH proof follows.

**RH status:** no unconditional proof has been produced.
