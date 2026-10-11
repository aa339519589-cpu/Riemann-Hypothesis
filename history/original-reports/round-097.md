## Round 97 — the scalar-to-cyclic trace bridge is not proved

I audited the latest Shimizu manuscript, version 2.4, [*Proof of the Riemann Hypothesis*](https://zenodo.org/records/21108581), including its `change_log.txt` and the decisive pages 261--270 of the 308-page PDF. The record itself still labels the manuscript a working draft containing fatal proof errors, while the abstract claims that the finite-window comparison proves
\[
F_K(s)=\xi(s).
\tag{97.1}
\]

The essential missing implication is Lemma 6.129. The scalar central family is defined from the ordinary kernel
\[
h_w(u)=\frac{e^{wu}-1}{u},
\]
so, before the finite-jet subtraction, its coefficient of \(w^{\ell-1}\) is the single scalar test proportional to
\[
\chi_M(u)\,\frac{u^{\ell-2}}{(\ell-1)!}.
\tag{97.2}
\]
By contrast, the proof defines matrix-coordinate tests
\[
\Omega_M(e_b,e_a),
\qquad
\bigl\langle\mu^{\rm fp}_{R,M},\Omega_M(e_b,e_a)\bigr\rangle
=\langle K_Me_b,e_a\rangle,
\tag{97.3}
\]
and then forms the new cyclic tensor
\[
\sum_{a_1,\ldots,a_\ell}
\Omega_{a_1a_2}\odot_M\cdots\odot_M\Omega_{a_\ell a_1}.
\tag{97.4}
\]
Its tensor-lift evaluation is, by the definition of that lift, the matrix trace
\[
\sum_{a_1,\ldots,a_\ell}
\langle K_Me_{a_2},e_{a_1}\rangle\cdots
\langle K_Me_{a_1},e_{a_\ell}\rangle
=\operatorname{Tr}(K_M^\ell).
\tag{97.5}
\]

What is not proved is that the newly introduced finite-readout contraction (97.4) is the original scalar coefficient (97.2), or even converges to it in the stated scalar central topology. The sentence that the finite central readout ledger “exhausts” the scalar coefficient supplies no map or convergence theorem establishing this. The scalar coefficient comes from the fixed \(u\)-kernel and finite-jet counterterm; (97.4) is constructed from the already formed comparison kernel \(K_M\). They are different objects unless an additional multiplication/intertwining theorem is proved. The cyclic tensor lift itself only defines an \(\ell\)-linear extension whose value is the product of the scalar matrix-readout values; it cannot turn that constructed tensor into an identity for the original linear scalar functional.

Therefore the first assertion of Lemma 6.129,
\[
\bigl\langle\mu^{\rm fp,sc}_{R,M},\Psi^{\rm sc}_{M,\ell}\bigr\rangle
=\operatorname{Tr}(K_M^\ell),
\tag{97.6}
\]
is unsupported. If the paper defines \(\Psi^{\rm sc}_{M,\ell}\) to mean the cyclic contraction, (97.6) is circular and it is no longer the coefficient of the Cauchy--Laplace kernel used in the classical Hadamard formula. If it means the actual scalar coefficient of (97.2), the trace identity does not follow from the displayed matrix-coordinate calculation.

This is the exact bridge used in Lemmas 6.137--6.144 to replace the operator-side finite-part pairing by
\[
w\,\operatorname{Tr}\bigl((I+iwK)^{-1}K^2\bigr),
\]
and hence in Theorem 6.156 to identify the logarithmic derivative of \(F_K\) with that of \(\xi\). Without an independent proof of the scalar-to-cyclic identification, the determinant identity and the ensuing self-adjoint spectral conclusion do not follow. The self-adjoint Hilbert--Schmidt construction may be a formal operator construction, but it is not connected to the zeta function by a closed unconditional comparison.

**Established:** the latest claimed proof contains an unproved—and, under the stated definitions, type-changing—scalar-to-cyclic trace bridge at Lemma 6.129.

**Route decision:** discard this manuscript as a completed RH proof. The Bombieri weighted-null-cone program remains active; no unconditional proof has been produced.

**RH status:** no unconditional proof has been produced.
