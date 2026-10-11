## Round 140 — the full critical-zero family is not a Riesz sequence

The preceding transfer gap is stronger than a missing estimate.  Under the
finite-off-line alternative used by Bombieri, all but finitely many
non-trivial zeros lie on the critical line.  Littlewood's theorem, as quoted
in Bombieri's discussion, says that consecutive ordinates of the non-trivial
zeros have gaps tending to zero; deleting finitely many off-line zeros leaves
the same conclusion for the critical-line ordinates.

For \(I_t=(-t,t)\), put

\[
 u_\gamma=(2t)^{-1/2}e^{-i\gamma u}.
\]

For two adjacent critical ordinates with \(\delta=\gamma'-\gamma\), direct
integration gives

\[
 \|u_{\gamma'}-u_\gamma\|_{L^2(I_t)}^2
 =2\left(1-\frac{\sin(t\delta)}{t\delta}\right)
 \longrightarrow 0
 \qquad(\delta\to0).
\tag{140.1}
\]

If the full family were a Riesz sequence, its lower inequality applied to the
two coefficients \(1,-1\) would give a fixed positive lower bound for the
left side of (140.1), a contradiction.  Therefore a Kadec subsequence may be
useful for a separated model, but it cannot transfer the \(\ell^2\)-mass of an
arbitrary Bombieri eigenvector supported on all critical zeros: the omitted
near-colliding coordinates are not controlled by that subsequence.

There is an even more direct obstruction for Section 10's weighted synthesis.
With \(d_\gamma=\tfrac14+\gamma^2\), the critical columns

\[
 v_\gamma(u)=d_\gamma^{-1}e^{-i\gamma u}
\]

satisfy

\[
 \|v_\gamma\|_{L^2(I_t)}^2=\frac{2t}{|d_\gamma|^2},
 \qquad
 \sum_{\gamma\in\Gamma_C}\|v_\gamma\|_{L^2(I_t)}^2<\infty,
\tag{140.2}
\]

because \(d_\gamma\asymp\gamma^2\) and the Riemann--von Mangoldt bound
\(N(T)=O(T\log T)\) implies
\(\sum_{\gamma\in\Gamma_C}(1+\gamma^2)^{-2}<\infty\).
Hence the synthesis map

\[
 S:\ell^2(\Gamma_C)\to L^2(I_t),\qquad
 S(w)=\sum_{\gamma\in\Gamma_C}w_\gamma v_\gamma,
\]

is Hilbert--Schmidt, in particular compact.  It cannot have a uniform lower
bound on the \(\ell^2\)-norm of \(w\).  This explains structurally why finite
sections can have eigenvalues collapsing to zero; it does not establish an
off-line relation or RH.

Thus the ideal-lattice identity (139.3) cannot be promoted by an ordinary
Kadec argument to the full zeta-zero system.  A zeta-specific injectivity or
minimum-cost range theorem is still required, with the finite-eigenvector
provenance and the off-line packet treated simultaneously.

**Established:** the full critical-zero exponentials fail the Riesz lower
bound, and Bombieri's weighted critical synthesis is compact under the stated
finite-off-line alternative.

**Remaining load-bearing statement:** prove that the particular compact-limit
vectors supplied by Bombieri cannot lie in the range needed to cancel the
off-line packet, or derive an independent positivity/uniqueness theorem that
does so.  No such theorem has been established here.

**RH status:** no unconditional proof has been produced.
