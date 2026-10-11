## Round 46 — even weighted-ℓ² range membership does not give generic uniqueness

The remaining exclusion must use arithmetic information about the actual zeta
ordinates. Weighted \(\ell^2\) membership by itself is not enough. Here is a
fully explicit smooth model.

Let \(h\) be an even, nonzero, \(4\pi\)-periodic \(C^\infty\) function such
that

\[
 h(u)=\cosh(u/2)\quad\text{for }|u|\leq\pi.
\tag{46.1}
\]

Such an \(h\) is obtained by multiplying \(\cosh(u/2)\) by an even smooth
cutoff that is one on \([-\pi,\pi]\) and vanishes near the endpoints
\(\pm2\pi\), then extending periodically. Expand it in the period-
\(4\pi\) Fourier series

\[
 h(u)=\sum_{n\in\mathbb Z}z_n e^{-i(n/2)u},
 \qquad
 z_n=\frac1{4\pi}\int_{-2\pi}^{2\pi}h(u)e^{i(n/2)u}\,du.
\tag{46.2}
\]

Smoothness gives \(z_n=O_m((1+|n|)^{-m})\) for every \(m\). With

\[
 \gamma_n=n/2,
 \qquad d_n=\tfrac14+\gamma_n^2=\frac{1+n^2}{4},
 \qquad w_n=d_nz_n,
\tag{46.3}
\]

we have \((w_n)\in\ell^2(\mathbb Z)\), while the series and its first
derivative converge uniformly. On \([-\pi,\pi]\), (46.1)--(46.2) give

\[
 Z(u):=\sum_{n\in\mathbb Z}\frac{w_n}{d_n}e^{-i\gamma_nu}
 =\cosh(u/2)
 =\tfrac12e^{u/2}+\tfrac12e^{-u/2}.
\tag{46.4}
\]

Thus the boundary-corrected function \(F\) is identically zero on the local
interval even though the coefficient vector \(w\) is nonzero and belongs to
weighted \(\ell^2\). The set \(\Gamma=\tfrac12\mathbb Z\) has the required
reflection and conjugation symmetries and satisfies the convergence condition.

This is not a zeta counterexample and does not satisfy Bombieri's eigenvalue
equations. It proves the narrower logical point needed for the audit: the
weighted range criterion in Rounds 24--27 cannot be converted into uniqueness
using only symmetry, convergence, smoothness, or \(\ell^2\) decay. Any successful
closure of (44.6) must exploit a theorem genuinely specific to the zero set of
\(\zeta\), or a new arithmetic identity that supplies that theorem.

**Established:** weighted \(\ell^2\) range membership and local smoothness do
not generically exclude the zero-collapse relation.

**Remaining load-bearing statement:** prove or disprove the corresponding
range exclusion for the actual critical ordinates, with the finite exceptional
packet and boundary terms included.

**RH status:** no unconditional proof has been produced.
