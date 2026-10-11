## Round 85 — Beurling--Malliavin completeness cannot replace exact weighted range exclusion

The Beurling--Malliavin route addresses completeness or the existence of
some measure with a Fourier gap. Poltoratski's [spectral-gap theorem](https://arxiv.org/abs/0908.2079)
defines the gap size by taking a supremum over all nonzero measures supported
on a set and describes that existential quantity through density and energy
conditions. The paper also notes the dual relation with completeness in
\(L^2\). Neither statement controls a prescribed coefficient vector in an
exact synthesis equation.

For the Bombieri setup, let \(\Gamma_C\) be the critical-line ordinates and
consider the weighted synthesis operator on a bounded interval \(I\),
\[
S_I:\ell^2(\Gamma_C)\longrightarrow L^2(I),\qquad
(S_Iw)(u)=\sum_{\gamma\in\Gamma_C}
\frac{w_\gamma}{\frac14+\gamma^2}e^{-i\gamma u}.
\tag{85.1}
\]
Using the Riemann--von Mangoldt bound
\(N(T)=O(T\log T)\), partial summation gives
\[
\sum_{\gamma\in\Gamma_C}
\left(\frac{1}{\frac14+\gamma^2}\right)^2<\infty.
\tag{85.2}
\]
Consequently
\[
\|S_I\|_{\mathrm{HS}}^2
=|I|\sum_{\gamma\in\Gamma_C}
\left(\frac{1}{\frac14+\gamma^2}\right)^2<\infty,
\tag{85.3}
\]
so \(S_I\) is compact. If its range is infinite-dimensional, that range is
not closed: a compact operator cannot map onto an infinite-dimensional
Hilbert space, and a compact operator with closed infinite-dimensional range
would have a bounded inverse on the orthogonal complement of its kernel.

Thus even if a density theorem proves
\[
\overline{\operatorname{Ran}S_I}=L^2(I),
\tag{85.4}
\]
the exact equation
\[
S_Iw_C=-g_{\mathrm{off},I}
\tag{85.5}
\]
is a strictly stronger assertion. Here \(g_{\mathrm{off},I}\) is the
restriction to \(I\) of the boundary-corrected contribution from a prescribed
finite or infinite packet of off-line zeros. Equation (85.5) is precisely the
coefficient-level cancellation that the Bombieri null-cone argument must
exclude. Approximation of \(g_{\mathrm{off},I}\) by critical exponentials
does not supply an exact \(w_C\in\ell^2\), and no uniform lower bound for the
inverse of \(S_I\) is available.

This is also why a spectral-gap theorem for the support
\(\Gamma_C\) cannot finish the RH argument: it either supplies an existential
measure/gap statement or a closure statement such as (85.4), while the
Bombieri alternative asks for the non-membership of a particular arithmetic
vector in the nonclosed weighted range. The missing result is an
unconditional, source-faithful theorem of the form
\[
g_{\mathrm{off},I}\notin\operatorname{Ran}S_I
\quad\text{for every admissible off-line packet and every relevant }I.
\tag{85.6}
\]

**Route decision:** retain exact weighted range exclusion as the immediate
analytic target, because it attacks the surviving Bombieri alternative
directly. The competitive alternative is a new unconditional arithmetic
positivity theorem for the full Weil form; that would close the same
alternative through a different dual formulation, but no such source theorem
is currently available. Completeness/density alone is ruled out by the
compact-range obstruction above.

**Established:** compactness of the Bombieri weighted critical synthesis
operator and the logical separation between dense range and exact range
membership.

**Remaining load-bearing statement:** prove (85.6), or prove a genuinely
stronger arithmetic positivity statement that implies it. The BM density
machinery does not provide (85.6).

**RH status:** no unconditional proof has been produced.
