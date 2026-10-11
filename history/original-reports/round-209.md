## Round 209 — A/B result: Farrell v1's local projection is undefined on the off-critical quartet defect

**Source inspected:** Jordan G. Farrell, *A Curvature-Homology Proof of the
Riemann Hypothesis*, Version 1, 21-page PDF, Cambridge Open Engage record
<https://www.cambridge.org/engage/coe/article-details/6a2cc0b6d1922e37d5711068>.

The admissible class used in Section 2 is defined by decay on vertical
strips:
\[
\sup_{|\Re z|\le M}(1+|\Im z|)^N|g(z)|<\infty.
\]
The manuscript nevertheless says that Hermite--Gaussian functions belong to
this class.  This is false for its basic Gaussian: for
\(g(z)=e^{-z^2/\varepsilon^2}\),
\[
|g(iy)|=e^{y^2/\varepsilon^2},
\]
so the displayed vertical-strip decay fails.  More importantly, the lifted
zero coordinate is
\[
z_\rho=\frac{\rho-\frac12}{i}
=\gamma-i\left(\Re\rho-\frac12\right).
\]
Its imaginary part stays in a bounded interval while its real part is
unbounded as the ordinate \(\gamma\) grows.  The stated class therefore
provides no decay estimate for \(g(z_\rho)\), contrary to the proof of
absolute convergence of the zero sum.  The same orientation error leaves
the claimed horizontal-contour estimate unjustified.  Thus Theorem 2.1 is
not established from the stated admissibility definition.

Independently, the load-bearing projection step is not defined.  Section 4
defines \(\Pi_\gamma^{(2)}\) only for a real distribution whose local part
has the finite form
\[
c_0\delta_\gamma+c_1\partial_\gamma\delta_\gamma
+c_2\partial_\gamma^2\delta_\gamma+R_\gamma.
\]
For an off-critical quartet, however, the source uses the functional
\[
H_{Q,\delta}[g]
=g(\gamma+i\delta)+g(\gamma-i\delta)-2g(\gamma),
\]
whose Taylor expansion is
\[
H_{Q,\delta}[g]
=-\delta^2g''(\gamma)
+\frac{\delta^4}{12}g^{(4)}(\gamma)
-\frac{\delta^6}{360}g^{(6)}(\gamma)+\cdots.
\]
This is an infinite higher-derivative functional involving evaluations at
complex points, not a finite real local jet in the domain where
\(\Pi_\gamma^{(2)}\) was defined.  The finite Hermite--Gaussian recovery
matrix recovers coefficients after a finite local-jet decomposition has
already been assumed; it does not extend \(\Pi_\gamma^{(2)}\) to this
quartet functional.  Consequently the assertion
\(\Pi_\gamma^{(2)}(H_{Q,\delta})=-\delta^2\) is only the extraction of one
formal Taylor coefficient, not a proved application of a defined linear
projection.

There is also a separate convergence failure in Appendix A: the claimed
comparison reduces absolute convergence to
\[
\sum_{n\ge2}\frac{\log n\,\sqrt n}{(1+\log n)^N},
\]
which diverges because its terms do not tend to zero for any fixed \(N\).
The displayed polynomial Schwartz estimate at \(\log n\) is insufficient to
justify the prime-side interchange.

The direct equation \(-\delta^2=0\) therefore has no valid derivation from
this manuscript.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
