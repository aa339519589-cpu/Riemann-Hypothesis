## Round 171 — compact weighted synthesis identifies the infinite escape condition

The Bombieri infinite-off-line branch can be separated from the finite-off-line
argument by an exact tightness requirement.  For a fixed interval
\(I_T=[-T,T]\), let

\[
 S_{C,T}a(u):=\sum_{\gamma\in\Gamma_C}
       \frac{a_\gamma}{d_\gamma}e^{-i\gamma u},
 \qquad d_\gamma=\tfrac14+\gamma^2,
\tag{171.1}
\]

where \(\Gamma_C\) is the critical-line zero set.  Since
\(N(x)=O(x\log x)\),

\[
 \sum_{\substack{\gamma\in\Gamma_C\\|\gamma|>R}}|d_\gamma|^{-2}
 \ll \frac{\log R}{R^3}.
\tag{171.2}
\]

Consequently, by Cauchy--Schwarz,

\[
 \left\|S_{C,T}\big|_{|\gamma|>R}\right\|_{\ell^2\to C(I_T)}
 \ll \frac{\sqrt{\log R}}{R^{3/2}},
\tag{171.3}
\]

and the same estimate holds in \(L^2(I_T)\), up to a fixed factor depending
on \(T\).  Thus \(S_{C,T}\) is Hilbert--Schmidt and compact.  A normalized
sequence of coefficient vectors can converge weakly to zero while its
weighted exponential synthesis converges uniformly to zero on \(I_T\).

For the finite-section eigenvectors \(w^{(N)}\) in Bombieri's construction,
the mass inequality
\(\sum_{\Gamma_O}|w^{(N)}_\eta|^2\ge\tfrac12\) is not a tightness estimate.
The additional statement needed to pass that mass to a nonzero limiting
coefficient vector is

\[
 \lim_{R\to\infty}\ \sup_N
 \sum_{\substack{\eta\in\Gamma_O\\|\eta|>R}}
 |w^{(N)}_\eta|^2=0.
\tag{171.4}
\]

Without (171.4), the off-line mass may move to increasing heights while the
fixed-window synthesis becomes invisible.  This is exactly the distinction
between the finite-off-line compactness argument in Round 141 and the
infinite-off-line alternative.  The weighted tail estimate controls the image
of the coefficient vector; it does not control its unweighted \(\ell^2\)-mass.

The finite-section eigenvalue equation does not supply (171.4) merely from
the available row estimates.  After splitting the matrix into off-line and
critical blocks, the response is

\[
 y_N=-(C_N+\varepsilon_N I)^{-1}S_Nx_N,
\tag{171.5}
\]

when \(\lambda_N=-\varepsilon_N\).  A small tail for \(S_Nx_N\) can still
produce order-one \(y_N\) if the critical block has singular values comparable
to or smaller than \(\varepsilon_N\); Round 147 gave the corresponding
Schur-complement equation and an explicit two-by-two model.  No uniform
critical-block lower bound or alternative provenance estimate has been proved
for the actual zeta zero set.

Even if (171.4) were established, it would only produce a nonzero limiting
relation; an independent uniqueness or global Weil-positivity theorem would
still be needed to contradict it.  If (171.4) fails, the local compactness
route cannot even preserve the off-line mass.  Therefore the infinite
off-line branch remains a genuine unresolved alternative, not a consequence
that can be removed by the polynomial \(d_\gamma^{-1}\) weight.

**Established:** the exact missing estimate for the infinite branch is
uniform \(\ell^2\)-tightness such as (171.4), and compact weighted synthesis
does not imply it.

**Remaining load-bearing statement:** derive (171.4) from Bombieri's exact
finite-section equations, or replace it with a global argument that excludes
infinite off-line zeros without passing through a locally compact weighted
synthesis.

**RH status:** no unconditional proof has been produced.
