## Round 149 — correction: the finite matrix trace calculation is valid, but its scalar input is not identified

The preceding audit must be narrowed.  The accessible full text does provide a
valid finite-dimensional calculation (Lemma 6.124, pp. 240--241 of
<https://www.preprints.org/frontend/manuscript/137a4b503f7abf9be3cae4a2bc24c6bd/download_pub>):
for finite readout tests \(\Omega_{ab}\), it states

\[
 c_{ab}
 =\left\langle\mu^{\mathrm{fp,sc}}_{L,M},\Omega_{ab}\right\rangle
 =\langle K_Me_b,e_a\rangle .
\tag{149.1}
\]

If one forms the ordered cyclic tensor test
\[
 \sum_{a_1,\ldots,a_\ell}
 \Omega_{a_1a_2}\odot_M\Omega_{a_2a_3}
 \odot_M\cdots\odot_M\Omega_{a_\ell a_1},
\]
and defines the tensor-lift functional to multiply the scalar readout values,
then its evaluation is exactly

\[
 \sum_{a_1,\ldots,a_\ell}
 c_{a_1a_2}\cdots c_{a_\ell a_1}
 =\operatorname{tr}\!\left((P_NK_MP_N)^\ell\right).
\tag{149.2}
\]

The Hilbert--Schmidt limit of (149.2) to
\(\operatorname{Tr}(K_M^\ell)\) is also a standard valid estimate for
\(\ell\ge2\).  Therefore Round 148's finite-dimensional linear-versus-
quadratic check does not, by itself, refute the paper: a test object is allowed
to depend on the operator if that dependence is explicitly proved.

The unresolved step is more specific.  The scalar and cyclic codomains are
kept distinct in Definitions 6.116--6.123.  The scalar realization is defined
coefficientwise by the ordinary scalar Cauchy--Laplace coefficients
\(\Psi^{\mathrm{sc}}_{M,\ell}\), while the cyclic realization is defined from
ordered readout tensors.  In the proof of Lemma 6.124 the paper introduces a
finite restriction \(\Psi^{\mathrm{sc}}_{M,\ell;N}\) and then says that the
“finite central readout ledger exhausts”
\(\Psi^{\mathrm{sc}}_{M,\ell}\); this is the step used to write its scalar
pairing as the right side of (149.2).

The preceding identities establish (149.1) and the tensor-lift evaluation
(149.2).  They do not establish that the independently specified ordinary
scalar coefficient has the required readout expansion.  To close that step,
one must give, for every \(M,N,\ell\), an explicit equality of scalar test
objects (or their coefficient vectors) between the ordinary regularized
Cauchy--Laplace coefficient and the readout expression whose coefficients are
the products \(c_{a_1a_2}\cdots c_{a_\ell a_1}\), and then prove compatibility
as \(N\to\infty\) and \(M\to\infty\).  The sentence “the ledger exhausts” is
not such an equality: it specifies neither the expansion coefficients nor a
derivation from the ordinary \(h_w\)-based scalar coefficient.

This distinction can be expressed in a one-dimensional test.  Knowing only
\(\mu(\Omega)=c\) gives the matrix coefficient \(c\), and a separately
defined tensor lift can be made to evaluate to \(c^2\).  It does not determine
the value of an independently defined ordinary scalar coefficient \(e\).
If \(e=q\Omega\) with fixed \(q\), its value is \(qc\); if \(e\) is assigned a
\(c\)-dependent representation, the paper must prove that this representation
is the ordinary scalar coefficient rather than a determinant-side definition.
Thus the finite trace computation is sound, but it cannot substitute for the
scalar-coefficient identification.

This correction leaves the load-bearing gap intact.  The latest public v8
page (<https://www.preprints.org/manuscript/202505.2110>) states the same
overall architecture in its abstract but does not display this missing
coefficient-level derivation.  Consequently it is not justified to infer the
central derivative equality, and hence \(F_K\equiv\xi\), merely from the
validity of the cyclic finite-matrix calculation.

**Established:** (149.1), the finite tensor-lift computation (149.2), and
the Hilbert--Schmidt trace-power limit are legitimate conditional components
of the K-side construction.

**Remaining load-bearing statement:** independently identify the ordinary
scalar explicit-formula coefficient with the readout expansion used in
(149.2), including all finite-window and limiting maps; then verify the global
determinant-to-\(\xi\) identity and the self-adjoint spectral conclusion.

**RH status:** no unconditional proof has been produced.
