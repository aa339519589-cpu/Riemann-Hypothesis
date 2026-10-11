## Round 45 — nonzero-eigenvalue branch is compact; only the zero-collapse branch survives

Bombieri's Theorem 6 supplies, for each fixed \(t\), the absolute summability

\[
 \sum_{\gamma,\gamma'\in\Gamma}
 |H(\gamma,\gamma';t)|<\infty .
\tag{45.1}
\]

Extend the finite-section eigenvectors by zero to \(\ell^2(\Gamma)\), write
(P_N) for the height truncation, and let

\[
 H_N=P_NHP_N,
 \qquad H_Nw_N=\lambda_Nw_N,
 \qquad \|w_N\|_2=1.
\tag{45.2}
\]

Equation (45.1) implies that \(H\) is a bounded compact operator on
\(\ell^2(\Gamma)\) and that

\[
 \|H-H_N\|_{2\to2}
 \leq
 \sum_{(\gamma,\gamma')\notin\Gamma_N\times\Gamma_N}
 |H(\gamma,\gamma';t)|
 \longrightarrow0.
\tag{45.3}
\]

Suppose a subsequence satisfies \(|\lambda_N|\geq c>0\) and
\(\lambda_N\to\lambda\). For \(Q_K=I-P_K\), (45.2) gives

\[
 \|Q_Kw_N\|_2
 \leq c^{-1}\|Q_KHP_N\|_{2\to2}
 \leq c^{-1}\|Q_KH\|_{2\to2}.
\tag{45.4}
\]

The last quantity tends to zero as \(K\to\infty\), uniformly in \(N\), by
(45.1). Thus the vectors \(w_N\) are uniformly tight in \(\ell^2\). A diagonal
subsequence then converges strongly to a vector \(w\) with

\[
 \|w\|_2=1,
 \qquad
 Hw=\lambda w.
\tag{45.5}
\]

Therefore the nonzero-eigenvalue branch is not the source of the mass-loss
problem: it produces an actual nonzero eigenvector of the infinite compact
operator. The only remaining alternative is

\[
 \lambda_N\longrightarrow0,
\tag{45.6}
\]

along the selected negative branch. In that case (45.4) is unavailable, and
the finite vectors may develop increasingly large critical tails even though
the finite off-critical coordinates retain at least half of their mass. The
coordinate limit remains nonzero by (44.4), but the infinite operator equation
need not be recovered from the eigenvalue equation at the escaped scale.

This establishes a precise dichotomy for the finite-exception strategy:

\[
\boxed{
 \begin{array}{c}
 \limsup_N|\lambda_N|>0
 \Rightarrow \text{strong compactness and an actual negative infinite eigenvalue},\\[1mm]
 \lambda_N\to0
 \Rightarrow \text{the problem reduces to excluding a nonzero weighted-}\ell^2
 \text{ local relation.}
 \end{array}}
\tag{45.7}
\]

The first line is now closed at the operator-compactness level. The second
line is the remaining RH-bearing case; positivity of the small-support Weil
form does not exclude it because the limiting local function can be zero.

**Established:** absolute summability of the source matrix gives norm
convergence of finite sections and strong convergence of every branch bounded
away from zero.

**Remaining load-bearing statement:** prove either a zeta-specific lower bound
preventing (45.6), or an independent theorem excluding the nonzero weighted-
\ell^2 local relation that occurs in the zero-collapse case.

**RH status:** no unconditional proof has been produced.
