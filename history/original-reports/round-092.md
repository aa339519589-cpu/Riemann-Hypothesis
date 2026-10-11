## Round 92 — finite off-line support can give critical-system density, but not the required coefficient control

Burnol's completeness theorem contains one useful refinement for the finite-off-line branch. For the full multiset of nontrivial zeros, the associated evaluators remain complete in the relevant extended Sonine space after omitting arbitrarily many finitely many zero evaluators once the support parameter is above the completeness threshold. Therefore, if \(\Gamma_{\mathrm{off}}\) were finite, deleting all of it would at least give a density statement for the remaining critical-line system in that Sonine space:
\[
\overline{\operatorname{span}}\{\text{critical-line evaluators}\}
=\mathcal L_a,\qquad a>1.
\tag{92.1}
\]
This is a genuine improvement over having no information in the finite-off-line branch.

It still does not supply Bombieri's limiting null vector. The required relation has a prescribed coefficient domain and a prescribed local restriction:
\[
g_{\mathrm{off},I}
=\sum_{\gamma\in\Gamma_C}
\frac{w_\gamma}{\frac14+\gamma^2}e^{-i\gamma u}
\quad\text{on }I,\qquad
w\in\ell^2(\Gamma_C).
\tag{92.2}
\]
A Hilbert-space closure theorem gives finite-sum approximation in the Sonine norm, not an exact series with the weight \((\frac14+\gamma^2)^{-1}\), nor convergence in the Bombieri boundary-corrected norm. The compact operator \(S_I\) from (85.1) makes the distinction unavoidable: its dense range can contain arbitrarily good approximants while its exact range remains nonclosed.

A transfer theorem strong enough to use (92.1) would have to prove all of the following: equivalence of the Sonine and Bombieri local norms on the relevant subspace; existence of an exact coefficient sequence; the weighted \(\ell^2\) estimate; and compatibility with the finite eigenvalue equation \(\lambda w=Hw\). Burnol's result proves none of these four statements. Thus the finite-off-line Bombieri branch is narrowed to a quantitative coefficient-expansion problem, but it is not eliminated.

**Established:** in the finite-off-line case, a full-zero completeness theorem can yield critical-system density after finite deletion in its own Sonine space.

**Failure / missing step:** density does not imply the weighted exact representation (92.2) or the eigenvector compatibility required by the null-cone limit.

**Route decision:** use (92.1) as an auxiliary reduction for the finite branch. The infinite-off-line branch and the exact coefficient estimate remain separate load-bearing problems; the overall RH proof is not closed.

**RH status:** no unconditional proof has been produced.
