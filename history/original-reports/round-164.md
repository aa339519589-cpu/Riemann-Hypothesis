## Round 164 — the direct quadratic calculation isolates the missing map

The first nonzero ordinary scalar coefficient can be checked without any
infinite series.  Since

\[
 h_w(u)=w+\frac{w^2}{2}u+\cdots,
 \qquad
 \Psi^{\mathrm{sc}}_{M,2}
 = (I-Q^{\mathrm{cen}}_M)[\chi_M]
\tag{164.1}
\]

up to the fixed convention factor, the scalar side at \(\ell=2\) is exactly

\[
 L_M\!\left((I-Q^{\mathrm{cen}}_M)[\chi_M]\right),
 \qquad
 L_M(\psi):=\left\langle\mu^{\mathrm{fp,sc}}_{R,M},[\psi]\right\rangle.
\tag{164.2}
\]

This is one linear evaluation of one ordinary scalar test.  The valid
finite-readout identity instead is, for an orthonormal finite section,

\[
 L_M(\Omega^{(M)}_{ab})
 =\left\langle K_Me_b,e_a\right\rangle=:c^{(M)}_{ab}.
\tag{164.3}
\]

Finite-dimensional matrix algebra then gives

\[
 \operatorname{tr}(K_{M,N}^2)
 =\sum_{a,b=1}^{N}c^{(M)}_{ab}c^{(M)}_{ba}.
\tag{164.4}
\]

Nothing in (164.1)--(164.3) turns the single scalar test in (164.2) into the
two-factor expression (164.4).  A genuine proof would need one of the
following equivalent kinds of additional input:

\[
 (I-Q^{\mathrm{cen}}_M)[\chi_M]
 =\mathcal M_{M,N}\bigl(\{\Omega^{(M)}_{ab}\}_{a,b}\bigr)
\tag{164.5}
\]

in an explicitly defined ordinary scalar algebra with a proved evaluation rule,
or directly

\[
 L_M\!\left((I-Q^{\mathrm{cen}}_M)[\chi_M]\right)
 =\sum_{a,b=1}^{N}L_M(\Omega^{(M)}_{ab})L_M(\Omega^{(M)}_{ba}),
\tag{164.6}
\]

with the right side converging to \(\operatorname{Tr}(K_M^2)\).  The source
defines neither \(\mathcal M_{M,N}\) nor a scalar multiplicativity theorem that
would imply (164.6).  Its \(\odot_M\) is a separate cyclic tensor operation,
and the tensor-lift functional is explicitly not ordinary scalar
multiplication.

There is also a useful linear-versus-quadratic check.  If the scalar test in
(164.1) had a fixed, K-independent expansion
\(\sum d_{ab}\Omega^{(M)}_{ab}\), then its pairing would be
\(\sum d_{ab}c^{(M)}_{ab}\), a linear expression in the readouts, whereas
(164.4) is quadratic.  If the coefficients \(d_{ab}\) are instead allowed to
depend on \(K\) or on the readout values, the expansion becomes a
K-dependent engineered projection and must itself be proved equal to the fixed
scalar test (164.1).  That is precisely the missing noncircular statement.

**Established:** the quadratic coefficient reduces the alleged bridge to the
explicit scalar identity (164.6).  The definitions prove the one-factor
readouts and the matrix trace formula, but not the scalar identity connecting
them.

**Remaining load-bearing statement:** construct and independently prove the
ordinary scalar map/evaluation in (164.5)--(164.6), beginning at fixed \(M,N\);
only afterwards are the Schatten limits and the determinant comparison valid.

**RH status:** no unconditional proof has been produced.
