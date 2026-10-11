## Round 143 — a rigorous toy model of high-frequency local cancellation

The escape mechanism can be realized exactly in a non-zeta model; this
prevents replacing the missing infinite-branch theorem by a generic compactness
claim.  Fix \(0<T<\pi\), let the critical model frequencies be
\(\Gamma_C=\mathbb Z\), and let

\[
 \eta_N=N+i/N,\qquad d_\xi=\tfrac14+\xi^2.
\]

Choose a smooth \(2\pi\)-periodic function

\[
 g_N(u)=1+\chi(u)\bigl(e^{u/N}-1\bigr),
\]

where \(\chi\in C_c^\infty(-\pi,\pi)\) is identically \(1\) on
\([-T,T]\).  Write its Fourier series as
\(g_N(u)=\sum_{k\in\mathbb Z}a_{k,N}e^{-iku}\).  Define coefficient data by

\[
 w_{\eta_N}=1,\qquad
 w_{n,N}=-\frac{d_n}{d_{\eta_N}}\,a_{n-N,N}
 \quad(n\in\mathbb Z).
\tag{143.1}
\]

Then, on \([-T,T]\),

\[
 \begin{aligned}
 \frac{w_{\eta_N}}{d_{\eta_N}}e^{-i\eta_Nu}
 \sum_{n\in\mathbb Z}\frac{w_{n,N}}{d_n}e^{-inu}
 &=\frac{e^{u/N}e^{-iNu}}{d_{\eta_N}}
   -\frac{g_N(u)e^{-iNu}}{d_{\eta_N}}\\
 &=0.
 \end{aligned}
\tag{143.2}
\]

The coefficient vector is in \(\ell^2\): \(g_N\) is smooth, so
\((a_{k,N})\) decays faster than any power, and the polynomial factor
\(d_n/d_{\eta_N}\) preserves square summability.  Moreover,
\(g_N\to1\) in every periodic Sobolev norm as \(N\to\infty\), hence
\(a_{k,N}\to\delta_{k0}\) rapidly in weighted \(\ell^2\).  It follows that

\[
 \sum_{n\in\mathbb Z}|w_{n,N}|^2
 =\sum_{k\in\mathbb Z}
 \left|\frac{d_{N+k}}{d_{\eta_N}}\right|^2|a_{k,N}|^2
 \longrightarrow 1
 =|w_{\eta_N}|^2.
\tag{143.3}
\]

After normalization, the off-line coordinate carries asymptotically one half
of the coefficient mass, while \(|\eta_N|\to\infty\) and
\(\operatorname{Im}\eta_N=1/N\to0\).  The weighted exponential relation is
exact on the fixed interval, yet the off-line mass escapes to unbounded height
and approaches the critical line.

This is not a counterexample for the actual zeta zero set.  It is a hostile
model check: weighted \(\ell^2\) control, a critical lattice, and local
analytic cancellation alone do not supply the non-escape theorem required in
the infinite Bombieri branch.  Any proof of that theorem must use additional
arithmetic information about the simultaneous locations of the zeta zeros,
not merely the decay of \(d_\xi^{-1}\) or local compactness.

**Established:** a fully explicit finite-approximation model realizes exact
fixed-window cancellation with off-line mass tending to one half while the
off-line frequency height tends to infinity and its displacement from the
critical line tends to zero.

**Remaining load-bearing statement:** rule out the analogous escape pattern
for the actual zeta zero set and Bombieri eigenvectors, or replace Bombieri's
route with a global positivity/spectral argument whose domain is independently
constructed.  No such unconditional theorem has been established here.

**RH status:** no unconditional proof has been produced.
