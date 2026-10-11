## Round 270 — Shimizu v2.4 does not prove the operator-convergence bridge needed for its determinant identity

Source audited: Yoshinori Shimizu, *Proof of the Riemann Hypothesis*,
[Zenodo record 21108581](https://zenodo.org/records/21108581), version 2.4,
PDF SHA-256
66d18d697e4aa3baeb7c46121327f0101ad15c4c6607350038fbb47e09faba4b.
The record itself labels the manuscript a working draft containing fatal errors
in its proofs.

The claimed determinant closure requires the finite-window boundary operators
to converge to the infinite operator. In Lemma 6.141 the required statement is
\[
(C_{R,M}-C_R)A\longrightarrow0
\quad\text{in }S_4,
\qquad A=(I+A_R)^{-a_{\mathrm{tr}}},
\]
which is then used to infer \(K_M\to K\) in \(S_2\). The proof reduces the
tail by the \(S_4\) bound, but its finite-dimensional part is justified only by
an appeal to the convergence of the particular central Cauchy--Laplace
cutoff family in Lemma 6.109.

Lemma 6.109 proves convergence of the vectors
\(\Psi^{\mathrm{fw}}_{w,M}\) for the specified central kernel family in the
defined test-data seminorms. It does not prove, for a dense set of arbitrary
Hilbert-space inputs \(h\), that
\[
C_{R,M}Ah\longrightarrow C_RAh,
\]
nor does it give the uniform operator estimates needed to pass from
finite-dimensional convergence to \(S_4\)-convergence. Convergence of one
specified test family, even with a uniform bound for that family, is not an
operator-convergence theorem. The proof supplies no lemma establishing the
missing finite-dimensional convergence for the spectral basis vectors used in
the \(P_N\) argument.

Without this bridge, the asserted \(K_M\to K\) in Lemma 6.141 is unproved.
Consequently Lemma 6.144 has not established that the finite-part realized
boundary functional equals the determinant trace; the later central pairing
equality and \(F_K\equiv\xi\) cannot be concluded from the displayed chain.
The self-adjointness of the formally constructed \(K\), by itself, does not
identify its determinant with the completed zeta function.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
