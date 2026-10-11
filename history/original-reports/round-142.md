## Round 142 — explicit noncompactness of the infinite-off-line branch

The finite-dimensional compactness used in Round 141 is genuinely unavailable
when off-line zeros are infinite.  Let
\(\Gamma_{\ge R}=\{\xi\in\Gamma:|\xi|\ge R\}\), and let
\(\|w\|_{\ell^2(\Gamma)}\le1\).  Since every non-trivial zero satisfies
\(|\operatorname{Im}\xi|<\tfrac12\) in the centered coordinate
\(\xi=\gamma\) defined by \(\rho=\tfrac12+i\gamma\), one has, for
\(|u|\le T\),

\[
 \left|
 \sum_{\xi\in\Gamma_{\ge R}}
 \frac{w_\xi}{d_\xi}e^{-i\xi u}
 \right|
 \le
 e^{T/2}
 \left(\sum_{\xi\in\Gamma_{\ge R}}|d_\xi|^{-2}\right)^{1/2},
 \qquad d_\xi=\tfrac14+\xi^2.
\tag{142.1}
\]

The zero-counting bound \(N(x)=O(x\log x)\) and
\(|d_\xi|\asymp|\xi|^2\) at large height give the quantitative tail estimate

\[
 \sum_{\xi\in\Gamma_{\ge R}}|d_\xi|^{-2}
 \ll \frac{\log R}{R^3},
 \qquad
 \sup_{|u|\le T}|Z_{\ge R}(u)|
 \ll e^{T/2}\frac{\sqrt{\log R}}{R^{3/2}}.
\tag{142.2}
\]

Thus unit \(\ell^2\)-mass can move to increasing zero heights while its
weighted exponential synthesis converges uniformly to zero on every fixed
compact \(u\)-interval.  The boundary coefficients \(A,B\), determined from
the endpoint values of \(Z\), vanish in the same fixed-\(T\) limit.  This is
an explicit model of the weak/locally-uniform escape observed in Bombieri's
finite-section discussion; it is not a mere lack of notation.

The factor \(e^{T/2}\) in (142.2) also identifies the exact quantitative
obligation left by the infinite branch.  One needs a theorem linking the
interval length \(T\) selected in the eigenvalue problem to the height \(R\)
where a fixed fraction of the off-line coefficient mass sits.  Bounds for
\(\ell^2\)-normalization alone permit \(R\) to grow faster than any prescribed
function of \(T\), so (142.2) gives no contradiction when \(T=T_N\to\infty\).
The finite-difference argument of Round 141 consequently cannot be passed to
infinite off-line sets by a naive truncation.

**Established:** the weighted synthesis has an explicit high-height tail
bound, and coefficient mass escape makes all fixed-window limit relations
insensitive to that mass.

**Remaining load-bearing statement:** prove a height-versus-window
non-escape estimate for Bombieri's particular negative eigenvectors, or find a
different global argument that controls the infinite off-line spectrum without
such tightness.  No such estimate has been established here.

**RH status:** no unconditional proof has been produced.
