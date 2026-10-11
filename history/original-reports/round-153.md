## Round 153 — the scalar trace contraction is not implied by matrix readout data

Let \(\mathcal T_M\) be the ordinary scalar finite-window test space and
let

\[
 V_{M,N}:=\operatorname{span}\{\Omega_M(e_b,e_a):1\leq a,b\leq N\}
 \subset \mathcal T_M .
\]

The matrix-coefficient readout proves only

\[
 \mu^{\mathrm{fp,sc}}_{R,M}(\Omega_{ab})
 =c_{ab}
 =\langle K_{M,N}e_b,e_a\rangle .
\tag{153.1}
\]

The cyclic tensor lift may then assign, by its own definition,

\[
 \mu^{\mathrm{fp,cyc}}_{R,M}
 \left(\sum_{a_1,\ldots,a_\ell}
 \Omega_{a_1a_2}\odot_M\cdots\odot_M\Omega_{a_\ell a_1}\right)
 =
 \sum_{a_1,\ldots,a_\ell}
 c_{a_1a_2}\cdots c_{a_\ell a_1}
 =\operatorname{tr}(K_{M,N}^{\ell}).
\tag{153.2}
\]

Equation (153.2) is a tensor-channel evaluation.  It does not follow from
(153.1) for the ordinary scalar functional.  The source itself explicitly
states after this contraction that the step is not a multiplicativity
assertion for the ordinary scalar distribution.  That disclaimer is correct,
but it makes a separate scalar coefficient identity necessary.

If an ordinary scalar coefficient \(p_{M,N,\ell}\) is not proved to lie in
\(V_{M,N}\), then \(V_{M,N}\) is finite-dimensional and closed, so
Hahn--Banach gives a continuous linear functional \(\nu\) with

\[
 \nu|_{V_{M,N}}=0,\qquad \nu(p_{M,N,\ell})\ne0.
\]

For every \(t\in\mathbb C\), the functionals
\(\mu_t=\mu^{\mathrm{fp,sc}}_{R,M}+t\nu\) have the same matrix readout
values (153.1) and the same cyclic trace calculation (153.2), while

\[
 \mu_t(p_{M,N,\ell})
 =\mu^{\mathrm{fp,sc}}_{R,M}(p_{M,N,\ell})
   +t\,\nu(p_{M,N,\ell})
\]

varies with \(t\).  If the coefficient is in \(V_{M,N}\), the proof must
instead display its expansion and prove that its coefficients give the
claimed trace.  If it is only a limit of elements of \(V_{M,N}\), the
missing projection and convergence statement is exactly (151.1).

The failure is also visible in a one-dimensional smooth model.  Let
\(\chi\in C_c^\infty(\mathbb R)\) equal \(1\) near \(0\), put
\[
 \Omega(u)=\chi(u)(1+u),\qquad
 \mu(f)=f(0)+f'(0).
\]
Then
\[
 c=\mu(\Omega)=2,\qquad
 \mu(\Omega^2)=3,\qquad
 c^2=4.
\]
The readout value \(c\) gives the self-adjoint one-dimensional matrix
\(K=[2]\), whose cyclic second trace is \(\operatorname{tr}(K^2)=4\).
The ordinary scalar functional, however, evaluates the product
\(\Omega^2\) as \(3\).  The cyclic lift can return \(4\) because it is
defined by the product of the one-factor readout values; that does not make
it the ordinary scalar pairing.  This model is not a zeta model and is not a
counterexample to RH; it isolates the missing multiplicativity/projection
inference.

**Established:** the finite matrix readout and the cyclic trace identity may
both be valid while the ordinary scalar coefficient pairing remains
undetermined.  The type distinction in Lemma 6.129 does not close this
logical gap.

**Remaining load-bearing statement:** provide an explicit ordinary scalar
coefficient expansion or projection, prove its equality with the cyclic
trace for every \(M,N,\ell\), and prove the scalar \(N\)- and \(M\)-limits in
the stated topology.

**RH status:** no unconditional proof has been produced.
