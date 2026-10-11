## Round 157 — direct Taylor expansion shows what the ordinary scalar coefficients are

The ordinary scalar coefficients are not mysterious once Definitions
6.91--6.98 are expanded.  The source gives
\[
 h_w(u)=\frac{e^{wu}-1}{u}
 =\sum_{a\geq0}\frac{w^{a+1}}{(a+1)!}\,u^a,
\]
and the finite-window regularization is
\[
 \Psi^{\mathrm{fw}}_{w,M}
 =(I-Q^{\mathrm{cen}}_M)\,[\chi_M h_w].
\]
Both \(\chi_M\) and \(Q^{\mathrm{cen}}_M\) are independent of \(w\), and
\(Q^{\mathrm{cen}}_M\) is linear.  Therefore the coefficient of
\(w^{a+1}\) in the ordinary scalar realization is explicitly
\[
 q^{\mathrm{sc}}_{M,a+1}(u)
 =\frac1{(a+1)!}
 (I-Q^{\mathrm{cen}}_M)\bigl[\chi_M(u)u^a\bigr].
\tag{157.1}
\]
If the source's universal basis starts at \(\ell=2\) and absorbs the phase
\((-i)^{\ell-2}\), then the coefficient of \(w^{\ell-1}\) is
\(q^{\mathrm{sc}}_{M,\ell-1}\), so
\[
 \Psi^{\mathrm{sc}}_{M,\ell}
 =(-i)^{2-\ell}q^{\mathrm{sc}}_{M,\ell-1}
\]
for the corresponding coefficient convention.  Equivalently, before the
phase normalization,
\[
 q^{\mathrm{sc}}_{M,\ell-1}(u)
 =\frac1{(\ell-1)!}
 (I-Q^{\mathrm{cen}}_M)\bigl[\chi_M(u)u^{\ell-2}\bigr],
 \qquad \ell\geq2.
\]
This index shift does not alter the type or linearity of the coefficient.

Thus the ordinary scalar pairing is a single linear moment:
\[
 \left\langle\mu^{\mathrm{fp,sc}}_{R,M},
 \Psi^{\mathrm{sc}}_{M,\ell}\right\rangle
 =
 \left\langle\mu^{\mathrm{fp,sc}}_{R,M},
 q^{\mathrm{sc}}_{M,\ell-1}\right\rangle
 \times(\text{the fixed convention factor}).
\tag{157.2}
\]
The \(K\)-side trace claimed in Lemma 6.129 is instead
\[
 \operatorname{Tr}(K_{M,N}^{\ell})
 =
 \sum_{a_1,\ldots,a_\ell}
 c_{a_1a_2}\cdots c_{a_\ell a_1},
 \qquad
 c_{ab}=
 \left\langle\mu^{\mathrm{fp,sc}}_{R,M},\Omega_{ab}\right\rangle.
\tag{157.3}
\]
Equation (157.3) is a degree-\(\ell\) polynomial in separate one-factor
readout values, whereas (157.2) is the value of the same linear functional
on the one scalar test (157.1).  A theorem relating them would have to give
an actual scalar expansion of (157.1) in the readout system together with a
nontrivial evaluation identity.  The source supplies neither that expansion
nor such an identity; it instead introduces the cyclic tensor lift, where
(157.3) is built into the definition.

This makes the logical fork concrete.  Either the scalar coefficient
\(q^{\mathrm{sc}}_{M,\ell-1}\) lies in the finite readout span and its exact
coordinates are displayed and proved to yield (157.3), or it does not and a
projection/density theorem is required.  The Taylor expansion itself supplies
neither alternative.  In particular, the finite-jet counterterm only removes
the fixed local principal-part coordinates; it does not turn the remaining
scalar moment into a cyclic tensor moment.

**Established:** the ordinary \(h_w\)-based scalar coefficient has an explicit
linear Taylor form, while the trace power is a cyclic multilinear
contraction.  The two forms are not equal by formal Taylor expansion or by
the finite-jet regularization.

**Remaining load-bearing statement:** prove the missing scalar readout
expansion/evaluation for the concrete coefficients (157.1), with all
\(M,N\) limits, before identifying the determinant trace with the classical
explicit-formula transform.

**RH status:** no unconditional proof has been produced.
