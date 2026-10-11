## Round 258 — B-result: the thermodynamic positivity manuscript assumes its cycle-cone closure

Source inspected: Mikhail I. Aksman, *Thermodynamic Positivity and the
Riemann Hypothesis: A Vorton-Vacuum Realization of Weil's Explicit Formula
on an Open Arithmetic Boundary*, Zenodo record
[21937318](https://zenodo.org/records/21937318), PDF SHA-256
f1fe318de19657cbb5c59234545ff5f4684b2ffa313c129fa4887b83a3b928ce.

The manuscript does not derive the arithmetic positivity from the displayed
thermodynamic functional. Its starting point is the generic expansion
\[
\mathcal F[u_0+\varphi]
=\mathcal F[u_0]+\frac12\delta^2\mathcal F[u_0](\varphi,\varphi)
+O(\|\varphi\|^3),
\]
which gives a vacuum Hessian
\(H_{\mathrm{vac}}=-\Delta+V''(u_0)\). No definition of the manifold,
domain, boundary conditions, or potential is supplied that identifies this
Hessian with the Weil quadratic form.

The load-bearing identity is asserted in equation (11):
\[
\delta^2\mathcal F[u_0](\mathcal A(f),\mathcal A(f))
=C\,\mathcal W(f)+B_\infty(f).
\]
The cited arithmetic Riemann--Roch and Faltings--Hriljac results do not
establish this identity. Faltings--Hriljac gives a sign statement for the
finite intersection pairing on an appropriate degree-zero divisor space; the
source neither constructs the map \(\mathcal A\) from every Weil test
function to that space nor proves that the finite pairing is the prime and
zero terms of \(\mathcal W\). The claimed \(B_\infty(f)\ge0\) is likewise
only described through a proposed conformal deformation, analytic torsion,
and a Birman--Kre\u{\i}n assertion. No operator domain, trace formula,
renormalization, or inequality proving that sign is given.

The decisive missing premise is then stated explicitly as the “Cycle-Cone
Closure Theorem”:
\[
\mathcal C_{\mathrm{physical}}=\mathcal T_{\mathrm{Weil}}.
\]
The manuscript offers no construction of the physical cycle cone, no
surjectivity or density proof in the Schwartz topology, and no continuity
argument allowing positivity on geometric cycles to pass to all Weil test
functions. The final theorem changes the earlier asserted identity to the
stronger formula
\[
\delta^2\mathcal F[u_0](\mathcal A(f),\mathcal A(f))
=C\,\mathcal W(f),
\]
but does not prove that the \(B_\infty\) term vanishes or has already been
absorbed into this formula. Thus the final implication is conditional on
exactly the missing arithmetic-to-physical identification.

There is also no valid zero-location deduction from the generic stability
statement alone: a positive Hessian for an unspecified physical model does
not imply positivity of the Weil form unless the missing realization and
identity are established. Consequently the manuscript supplies a physical
proposal and a conditional implication, but no complete unconditional Weil
positivity proof and no RH proof.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
