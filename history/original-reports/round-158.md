## Round 158 — the gap is already present at the quadratic coefficient

The scalar/cyclic issue cannot be hidden in the infinite series.  From
\(h_w(u)=(e^{wu}-1)/u\) and the linear finite-jet regularization, the
\(\ell=2\) coefficient of the source's \(w^{\ell-1}\) expansion is, up to
the fixed phase and factorial convention,
\[
 \Psi^{\mathrm{sc}}_{M,2}
 \doteq (I-Q^{\mathrm{cen}}_M)[\chi_M(u)].
\tag{158.1}
\]
Lemma 6.129 claims for this coefficient
\[
 \left\langle\mu^{\mathrm{fp,sc}}_{R,M},
 \Psi^{\mathrm{sc}}_{M,2}\right\rangle
 =\operatorname{Tr}(K_M^2)
 =\sum_{a,b}
 \left|\left\langle K_Me_b,e_a\right\rangle\right|^2.
\tag{158.2}
\]

The definitions preceding the lemma establish only the one-factor identities
\[
 \left\langle\mu^{\mathrm{fp,sc}}_{R,M},
 \Omega_M(e_b,e_a)\right\rangle
 =\left\langle K_Me_b,e_a\right\rangle.
\tag{158.3}
\]
They do not establish either of the two facts needed to derive (158.2):
\[
 (I-Q^{\mathrm{cen}}_M)[\chi_M]
 \stackrel{?}{=}
 \sum_{a,b}\Omega_M(e_b,e_a)\odot_M\Omega_M(e_a,e_b)
\tag{158.4}
\]
in a common scalar space, or the scalar multiplicative evaluation that
would turn the pairing of the right side into the product of the values in
(158.3).  With the source's actual \(\odot_M\), the right side of (158.4)
is a cyclic tensor object rather than an ordinary scalar test, so even the
first equality is ill-typed unless an additional bridge is supplied.

The quadratic case therefore has no coefficientwise or convergence
ambiguity: it asks for one explicit scalar test identity and one explicit
pairing identity.  The finite Gram/Riesz reconstruction provides the
individual readout tests and their one-factor pairings, but it does not
produce (158.4).  The cyclic lift can define the right side of (158.2)
directly; that is exactly why it cannot substitute for the ordinary scalar
pairing.

**Established:** the first nontrivial scalar coefficient already requires
the missing scalar-to-cyclic identification.  The obstruction is present
before the \(N\to\infty\) Schatten limit and is not caused by high-order
normal-convergence estimates.

**Remaining load-bearing statement:** prove (158.4) and its scalar pairing
identity, or replace them with an independent ordinary scalar derivation of
(158.2); then establish the \(M,N\) limits.

**RH status:** no unconditional proof has been produced.
