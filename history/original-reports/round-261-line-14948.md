## Round 261 — A/B result: the PIHR-XV boundary Riesz decay theorem is valid, but is below the RH-sensitive scale

Source inspected: Borros Arneth, *Crossing Chebyshev--Riesz Reduction,
Selberg--Bregman Energy, Euler-Sieve Memory Decay, and the Sharp Critical
Barrier for the Riemann Hypothesis*, PIHR--RH XV, Zenodo record
[22156735](https://zenodo.org/records/22156735), PDF SHA-256
2ea7f1ada7c041e4876a38e2c975c54f6696974984c4fb74b27c7526edf89178.

The source defines the Jordan function
\[
J_{1/2}(n)=\sum_{d\mid n}d^{1/2}\mu(n/d),
\qquad
f(n)=\frac{J_{1/2}(n)}{\sqrt n},
\]
and the Riesz sum
\[
W_f(x)=\sum_{n\le x}f(n)\left(\sqrt{\frac{x}{n}}-1\right).
\]
The Dirichlet-series identity is unconditional:
\[
\sum_{n\ge1}\frac{f(n)}{n^s}
=\frac{\zeta(s)}{\zeta(s+1/2)}
\qquad(\Re s>1).
\]
Indeed, the standard Jordan-function convolution gives
\(\sum J_{1/2}(n)n^{-z}=\zeta(z-1/2)/\zeta(z)\); putting
\(z=s+1/2\) yields the displayed formula.

For \(y>1\), Perron's kernel identity
\[
\frac{1}{2\pi i}\int_{(\sigma)}
\frac{y^s}{2s(s-\tfrac12)}\,ds
=\sqrt y-1
\qquad(\sigma>1)
\]
therefore gives
\[
W_f(x)=\frac{1}{2\pi i}\int_{(\sigma)}
\Phi(s)x^s\,ds,
\qquad
\Phi(s)=
\frac{\zeta(s)}{\zeta(s+1/2)}
\frac{1}{2s(s-\tfrac12)}.
\]
At \(s=1/2\), writing \(s=1/2+w\) gives
\[
\frac{1}{\zeta(1+w)}=w+O(w^2),
\qquad
\frac{1}{2s(s-\tfrac12)}=\frac1w-2+O(w),
\]
so the apparent singularity is removable and
\(\Phi(1/2)=\zeta(1/2)\).

Shift the contour to \(\Re s=1/2\). The pole of \(\zeta(s)\) at \(s=1\)
is crossed and has residue
\[
\operatorname*{Res}_{s=1}\Phi(s)x^s
=\frac{x}{\zeta(3/2)},
\]
because the kernel equals \(1\) at \(s=1\). A pole arising from a
nontrivial zero \(\rho\) of the denominator would be at
\(s=\rho-1/2\). The unconditional strip \(0<\Re\rho<1\) places all such
poles strictly to the left of \(\Re s=1/2\); trivial-zero poles are farther
left. The denominator pole at \(s+1/2=1\) is the already-removed
singularity above, and the zero-free line \(\Re(s+1/2)=1\) prevents any
additional boundary pole.

On \(s=1/2+it\), the standard estimates
\[
\frac1{\zeta(1+it)}\ll\log(2+|t|),
\qquad
\zeta(1/2+it)\ll_\varepsilon
(2+|t|)^{1/4+\varepsilon},
\]
and \(1/[2s(s-1/2)]=O(t^{-2})\) imply
\[
\Phi(1/2+it)\ll_\varepsilon
(2+|t|)^{-7/4+\varepsilon}\log(2+|t|).
\]
Choosing \(0<\varepsilon<3/4\) makes this boundary function integrable.
The same bounds, uniformly on the horizontal sides of the finite
contours, make those sides tend to zero, so the contour shift is justified.
Thus
\[
W_f(x)=\frac{x}{\zeta(3/2)}
+\frac{\sqrt x}{2\pi}
\int_{\mathbb R}\Phi(1/2+it)e^{it\log x}\,dt.
\]
The Riemann--Lebesgue lemma now gives the unconditional asymptotic
\[
W_f(x)=\frac{x}{\zeta(3/2)}+o(\sqrt x).
\]
Consequently, if
\[
M(x)=W_f(x)-\frac{x-1}{\zeta(3/2)},
\]
then
\[
M(x)=\frac1{\zeta(3/2)}+o(\sqrt x),
\qquad
\frac{M(x)}{\sqrt x}\longrightarrow0.
\]
This is a valid unconditional scale-decay theorem. It does not establish
the sign \(M(x)\ge0\): a hypothetical zero
\(\rho=\beta+i\gamma\), \(1/2<\beta<1\), contributes on the normalized
scale at order \(x^{\beta-1}\), which still tends to zero while remaining
larger than \(x^{-1/2}\). Therefore the theorem does not prove the
Crossing Chebyshev--Riesz inequality, the PIHR critical transport
positivity, or RH.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步产生了一个已完整核验的无条件 Riesz 尺度衰减定理，但没有产生新的无条件 RH 证明进展。
