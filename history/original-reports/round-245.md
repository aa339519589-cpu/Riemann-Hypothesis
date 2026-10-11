## Round 245 — A/B result: Shimizu's determinant closure assumes the missing equality of the two comparison functionals

**Source inspected:** Yoshinori Shimizu, *Proof of the Riemann Hypothesis*,
Zenodo record
<https://zenodo.org/records/20399267>, version 2.0, PDF pp. 147--200
(especially Theorem 6.100 and its proof).
Downloaded source SHA-256:
1816a686267a8f74a21feed618ed13714a9fe9870fe5fae3258fbed5c064c367.

The record page itself warns that the working draft contains fatal errors.
The independent logical break is visible in the manuscript's own definitions.
On p. 152, \(\mu_L\) is defined as a residual-free singular-boundary
functional obtained from the \(K_R\)-component, while \(\mu_\xi\) is defined
as the calibrated finite-window explicit-formula functional for \(\xi\). They
are distinct functionals; no equality is established at that point.

Theorem 5.18 and Proposition 5.19 establish only an orthogonal direct-sum
decomposition, exact evaluation of the arithmetic trace, and vanishing of
cross terms. Definition 5.20 then replaces a representative \(x\) by
\((\Pi_R+\Pi_{\rm arith}^X)x\), thereby discarding the residual component by
definition. None of these statements gives equality between the scalar
functional extracted from the \(K_R\)-projection and the scalar functional
from the completed-zeta explicit formula. In general, projecting a vector
and quotienting out a component does not preserve an unrelated scalar
functional.

Nevertheless, Lemma 6.100 asserts
\[
\langle\mu_L,\Psi^{\rm fw}_{w,M}\rangle
=
\langle\mu_\xi,\Psi^{\rm fw}_{w,M}\rangle
\]
for every finite window. Its proof says that applying the residual-free
interface “gives” this equality, but the interface cited there supplies only
the projection and arithmetic-trace facts just listed. It does not prove that
the \(K_R\)-side pairing equals the zeta-side explicit-formula pairing. The
subsequent Theorem 6.101, local logarithmic-derivative equality, and global
identity \(F_K\equiv\xi\) all depend on Lemma 6.100. Thus the self-adjoint
Hilbert--Schmidt operator construction does not yield an independently
verified determinant representation of \(\xi\), and no zero-location theorem
follows.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
