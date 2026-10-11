## Round 74 — the thermodynamic/Arakelov version states its missing closure as an axiom

I audited version 2 of Mikhail I. Aksman's [*The Riemann Hypothesis as a
Stability Theorem*](https://zenodo.org/records/21937318), including the
[presentation PDF](https://zenodo.org/records/21937318/files/Thermodynamic_Positivity_RH_Complete.pdf?download=1).
The document makes the logical gap unusually explicit.

### I. Stability of an invented vacuum is not a proved Weil inequality

The manuscript introduces a Ginzburg--Landau functional
\[
 \mathcal F[u]=\int_M\left(\frac12|\nabla u|^2+V(u)\right)\,d\mu
\tag{74.1}
\]
and then takes thermodynamic stability of an unspecified equilibrium \(u_0\)
as the premise
\[
 \delta^2\mathcal F[u_0](\varphi,\varphi)\ge0.
\tag{74.2}
\]
No precise manifold, potential, equilibrium, admissible perturbation domain,
closed quadratic form, or self-adjoint Hessian is constructed. Therefore
(74.2) is a physical assumption about a proposed model, not an
unconditional mathematical consequence.

The finite Arakelov intersection sign quoted from the
Faltings--Hriljac theorem applies to appropriate degree-zero arithmetic
divisors. The paper does not construct a map from every Weil test function
to such a divisor, prove that its image has the required degree and
regularity, or identify the resulting intersection pairing with the Weil
functional.

### II. “Cycle-cone closure” is asserted, not proved

The paper's Section 9 states the decisive equality
\[
 \mathcal C_{\mathrm{physical}}=\mathcal T_{\mathrm{Weil}},
\tag{74.3}
\]
describing it as the Cycle-Cone Closure Theorem. No theorem or construction
establishes (74.3). A cone of geometric cycles is not automatically a vector
space, and even a dense image would not imply equality of signs for a
quadratic functional unless continuity in the relevant topology and
closedness of the nonnegative cone were proved. The claimed “surjective
covering” is exactly the missing functional-analytic bridge.

The same section asserts that an Arakelov boundary term \(B_\infty(f)\) is
nonnegative because a continuous scattering sector has been neutralized.
Neither the neutralization nor the sign of this boundary term is derived.
Retaining an open cusp while simultaneously declaring its continuous
scattering contribution removed requires a separate operator and determinant
construction, which is not supplied.

### III. The final theorem is conditional on RH-bearing identities

The paper's final theorem assumes a canonical map and the exact identity
\[
 A:\mathcal T_{\mathrm{Weil}}\longrightarrow H_{\mathrm{vac}},
\qquad
 \delta^2\mathcal F[u_0](A(f),A(f))=C\,W(f),\quad C>0.
\tag{74.4}
\]
Together with (74.2), (74.4) immediately gives \(W(f)\ge0\), and Weil's
criterion then gives RH. Hence (74.4) is not a consequence of the preceding
model; it is the whole RH-bearing assertion written as an assumption.

The cited cohomological descent does not replace (74.3)--(74.4). Kolyvagin
Euler systems concern specific Selmer groups and do not, without a new
theorem, exhaust the infinite-dimensional Weil test space or control the
archimedean distribution. No such identification is provided in the paper.

**Established:** if (74.2)--(74.4) were proved in a common rigorously defined
space, the displayed implication to Weil positivity would be immediate.

**Failure / error:** the cycle-cone equality, the physical realization map,
the exact second-variation identity, and the boundary positivity are
asserted rather than proved.

**Remaining load-bearing statement:** construct the map \(A\), prove its
surjectivity onto the full Weil test class, and derive (74.4) with all
finite, archimedean, cusp, and domain terms controlled. The presentation
does not provide these results.

**RH status:** no unconditional proof has been produced.
