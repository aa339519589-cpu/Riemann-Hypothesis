## Round 83 — a \(1\times1\) countermodel invalidates the scalar trace inference

The scalar/cyclic break can be isolated without any zeta-specific
estimates. In Shimizu's [version 2.4 record](https://zenodo.org/records/21108581),
Lemma 6.129 first obtains the linear scalar readout
\[
c_{ab}=\left\langle\mu^{\mathrm{fp,sc}}_{R,M},
\Omega^{(M)}_{ab}\right\rangle
       =\left\langle K_Me_b,e_a\right\rangle.
\tag{83.1}
\]
It then asserts that the ordinary scalar coefficient has value
\[
\left\langle\mu^{\mathrm{fp,sc}}_{R,M},
\Psi^{\mathrm{sc}}_{M,\ell}\right\rangle
 =
\sum_{a_1,\ldots,a_\ell}
c_{a_1a_2}c_{a_2a_3}\cdots c_{a_\ell a_1}.
\tag{83.2}
\]
The displayed product is valid for the separately defined tensor lift, but
does not follow for the ordinary scalar functional.

The obstruction is already visible for \(N=1\) and \(\ell=2\). Let the scalar
test space be \(V=\mathbb C e\), let the scalar functional be the linear map
\[
\mu_c(e)=c,
\]
let \(\Omega_{11}=e\), and let \(K=[c]\). Then (83.1) holds exactly, while the
ordinary scalar test \(\Psi^{\mathrm{sc}}_{M,2}=e\) has
\[
\mu_c(\Psi^{\mathrm{sc}}_{M,2})=c,
\qquad
\operatorname{Tr}(K^2)=c^2.
\tag{83.3}
\]
For example, \(c=2\) gives \(2\neq4\). This is a type-correct model: the
scalar functional is linear, and the matrix coefficient identity is satisfied.
The tensor-lift functional, by contrast, is defined on
\(\Omega_{11}\odot_M\Omega_{11}\) by
\[
\mu_c^{(2)}(\Omega_{11}\odot_M\Omega_{11})
 =\mu_c(\Omega_{11})^2=c^2,
\tag{83.4}
\]
so it correctly produces the trace power—but only because (83.4) is the
definition of the tensor lift.

More generally, if \(V\) is the ordinary scalar test space and
\(\mu\in V^\ast\), the data \(c_{ab}=\mu(\Omega_{ab})\) determine \(\mu\) on
the linear span of the \(\Omega_{ab}\). They do not determine
\(\mu(\Psi^{\mathrm{sc}}_{M,\ell})\) as a degree-\(\ell\) polynomial in those
data. Such a conclusion requires one additional, explicit statement, for
example:

1. a definition of \(\Psi^{\mathrm{sc}}_{M,\ell}\) as a diagonal pullback of
   the \(\ell\)-fold tensor test together with a theorem that the scalar
   functional respects that pullback; or
2. a genuine multiplicativity theorem for the scalar functional on the
   relevant ordinary products.

The manuscript explicitly says that the scalar functional is not
multiplicative on ordinary scalar products and keeps scalar and cyclic
codomains distinct. Its phrase “the ledger's coefficient contraction gives”
therefore supplies neither of the required statements. The \(1\times1\)
model does not disprove the existence of a new bridge theorem, but it proves
that the bridge is not a consequence of Lemma 6.127, finite matrix
contraction, or Hilbert--Schmidt convergence alone.

**Updated audit conclusion:** the cyclic trace calculation is sound as a
tensor-channel calculation. The ordinary scalar equality in Lemma 6.129 is
not established. Consequently the determinant identity
\[
e^{a+b(s-\frac12)}
\det\nolimits_2\!\left(I+i(s-\tfrac12)K\right)=\xi(s)
\]
still has a load-bearing unproved link, so the self-adjointness of \(K\) does
not yield RH.
