# Review of actual original-form tail absorption

This is an independent automated mathematical read-through of
[ACTUAL_FORM_TAIL_ABSORPTION.md](ACTUAL_FORM_TAIL_ABSORPTION.md), followed
by an author check of its formulas and scope. It is not proof-assistant
certification or external human peer review. The cited scalar-state
sampling, original closed-form synthesis, and centered-coupling theorems
are the analytic inputs.

The stated theorem follows from those inputs under its lowest-eigenvalue
hypothesis. The cutoff dependence pays a uniform all-depth conclusion.
The finite signed comparison (13) remains open; critical positivity and
RH are not proved.

## Weighted sampling and thresholds

For (3), weighting each dyadic block of (G8) leaves a geometric sum of
the form

\[
 \sum_{j\ge0}4^{-j}(L+h_T+j)(h_T+j)^r
       \le C_r(L+h_T)h_T^r,
 \qquad h_T=\ell(T)\ge\log4>1.
\]

This proves the required cases \(r=0,1,2\), retaining genuine node
multiplicities and without a spacing assumption. At
\(T=A\kappa^{-1}L^{5/2}\), both thresholds are uniform: the (D16)
threshold follows from \(A L_{\min}^{5/2}\ge C_1\), and the (G8)
threshold follows by choosing \(A\) above the finite supremum displayed
after (4). Neither choice depends on the state or its depth.

## Original form, diagonal, and complete cross terms

The identities \(J^2=4\kappa^{-2}E_1\) and
\(Q^2=4\kappa^{-2}E_2\) in (5) retain the reconstruction cost. Direct
substitution yields the respective bounds

\[
 C A^{-2}(1+\log A)^2\kappa/L,
 \qquad C A^{-2}(1+\log A)^3\kappa.
\]

The cited synthesis bounds control the physical norm and complete Gamma
form on the original closed form domain. The remaining physical
perturbation, including all prime powers in both directions, is bounded.
This pays \(|\mathfrak h[v]|\), and

\[
 |R_>(T)|\le|\mathfrak h[v]|+\ell(T)\|m\|_\infty^2\|v\|^2
\]

costs the same cubic logarithmic factor. The upper bound for
\(Q_\kappa[v]\) follows likewise; its nonnegative sign specifically
uses that \(-\kappa\) is the bottom of the ground-perpendicular even
spectrum.

Equation (6) uses a damped shell sum, not an undamped low-frequency
budget. Substitution gives (7), retaining the second factor
\(\kappa^{-1}\) in the centered coupling. The original form
eigen-equation gives exactly \(K_T=-Q_\kappa[v]-D_T\), so all mixed
terms are paid as stated. No mixed sign or omitted cross block is used.
Each term in the sum (2) is bounded by a fixed multiple of
\(r(A)\kappa\). Since \(r(A)\to0\), the same choice
\(A(\varepsilon)\) works on the entire interval \(0<\kappa\le1/2\),
not only as \(\kappa\to0\).

## Finite packet and retained positive squares

The eigen-equation gives \(Q_\kappa[l]=Q_\kappa[v]\). With
\(\|v\|\le1/4\) and \(Q_\kappa[v]\le\kappa/4\), one has
\(\|l\|\ge3/4\), and the Rayleigh arithmetic in (10) is

\[
 -\kappa+\frac{\kappa/4}{9/16}=-\frac59\kappa< -\frac12\kappa.
\]

At the same cut the high imaginary-square cost is at most
\(2E_0(T)\le C\kappa L^2(L+h_T)T^{-2}\), hence at most
\(\kappa/4\) after increasing one fixed \(A\). The global vertical
derivative estimate (R3)--(R6) makes the near-line contribution at most
another \(\kappa/4\), for one sufficiently small fixed \(c\).
Subtracting only these negative-square contributions from the exact
identity (11) proves (12), with every positive square retained. All
statements use a single actual depth; no estimate for mixtures across
different eigenvalues is inferred.

The upper comparison (13) is not supplied by any of these Hermitian
tail or boundary estimates. It remains the signed step that would be
needed to exclude the hypothesized lowest negative state.
