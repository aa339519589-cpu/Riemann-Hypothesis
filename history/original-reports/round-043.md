## Round 43 — an explicit weighted-ℓ∞ local-null countermodel

The gap in Round 42 cannot be repaired by saying that the bound (42.5) is
``morally'' an \(\ell^2\) bound. There is an exact elementary model with the
same denominator \(d_\gamma=\tfrac14+\gamma^2\) in which the extracted class
contains a nonzero local null relation.

Take

\[
 \Gamma=\mathbb Z,\qquad I=(-\pi,\pi),\qquad d_n=n^2+\tfrac14,
\]

and define

\[
 z_n=\frac{(-1)^n\sinh(\pi/2)}{\pi d_n},
 \qquad
 w_n=d_nz_n=\frac{(-1)^n\sinh(\pi/2)}\pi.
\tag{43.1}
\]

The coefficients \(z_n\) are absolutely summable. A twofold integration by
parts, or direct integration, gives

\[
 \frac1{2\pi}\int_{-\pi}^{\pi}\cosh(u/2)e^{inu}\,du
 =\frac{(-1)^n\sinh(\pi/2)}{\pi(n^2+1/4)}=z_n.
\tag{43.2}
\]

Therefore the uniformly convergent Fourier series satisfies

\[
 Z(u):=\sum_{n\in\mathbb Z}z_ne^{-inu}
 =\cosh(u/2)
 =\tfrac12e^{u/2}+\tfrac12e^{-u/2}
 \quad(-\pi\leq u\leq\pi).
\tag{43.3}
\]

Consequently the boundary-corrected function

\[
 F(u)=Z(u)-\tfrac12e^{u/2}-\tfrac12e^{-u/2}
\]

vanishes identically on the interval, although the coefficient vector is
nonzero. At the same time,

\[
 (w_n)\in\ell^\infty(\mathbb Z)\setminus\ell^2(\mathbb Z).
\tag{43.4}
\]

This toy set has the required symmetries \(\Gamma=-\Gamma=\overline\Gamma\)
and satisfies Bombieri's stated convergence condition. It is not the zeta-zero
set and it does not solve the finite eigenvalue equations; its purpose is
narrow and exact: the convergence assumptions, the denominator
\(\tfrac14+\gamma^2\), and a local \(H^1\) function limit do not by themselves
exclude a local null relation. The extra \(\ell^2\) weighted hypothesis used
by Rounds 24--27 would exclude (43.1), but that hypothesis is not obtained in
Section 10.

**Established:** the source-faithful weighted-\(\ell^\infty\) limit class is
strictly larger than the weighted-\(\ell^2\) range, and local vanishing of
\(F\) does not force all limiting coefficients to vanish under the former
class.

**Remaining load-bearing statement:** for the actual zeta ordinates, derive
weighted tightness from the finite eigenvalue equations, or prove directly
that the selected branch cannot converge to a relation of the type (43.3).
Neither conclusion follows from coordinatewise extraction or the local energy
estimate.

**RH status:** no unconditional proof has been produced.
