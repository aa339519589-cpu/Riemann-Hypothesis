## Round 261 — A/B result: PIHR-XV's boundary Riesz decay is valid at the (o(\sqrt{x})) scale, not at the RH sign scale

Source audited: Borros Arneth, *Crossing Chebyshev--Riesz Reduction,
Selberg--Bregman Energy, Euler-Sieve Memory Decay, and the Sharp Critical
Barrier for RH*, [Zenodo record 22156735](https://zenodo.org/records/22156735),
PDF SHA-256
2ea7f1ada7c041e4876a38e2c975c54f6696974984c4fb74b27c7526edf89178.
The source itself distinguishes the unconditional decay theorem from the
unproved sign barrier. I independently rederived the analytic part.

### VERIFIED PROOF CHAIN addition

Define
\[
J_{1/2}(n)=\sum_{d\mid n}d^{1/2}\mu(n/d),
\qquad
f(n)=\frac{J_{1/2}(n)}{\sqrt n},
\qquad
c=\frac1{\zeta(3/2)},
\]
and
\[
W_f(x)=\sum_{n\le x}f(n)\left(\sqrt{\frac{x}{n}}-1\right),
\qquad
M(x)=W_f(x)-c(x-1).
\]
For \(\Re s>1\), Dirichlet convolution gives
\[
\sum_{n\ge1}\frac{f(n)}{n^s}=\frac{\zeta(s)}{\zeta(s+1/2)}.
\]
Perron inversion with the exact kernel
\[
\frac1{2s(s-1/2)}=-\frac1s+\frac1{s-1/2}
\]
therefore gives, initially on a right-hand line,
\[
W_f(x)=\frac1{2\pi i}\int_{(\sigma)}
\frac{\zeta(s)}{\zeta(s+1/2)}
\frac{x^s}{2s(s-1/2)}\,ds.
\]

At \(s=1/2\), the apparent kernel pole is removable. Writing
\(s=1/2+w\), the pole of \(1/[2s(s-1/2)]\) is cancelled by the zero
of \(1/\zeta(1+w)\), and the finite value is
\[
\lim_{s\to1/2}\frac{\zeta(s)}{\zeta(s+1/2)2s(s-1/2)}
=\zeta(1/2).
\]
Move the contour to \(\Re s=1/2\). The only crossed pole is the
numerator pole at \(s=1\), whose residue contributes \(cx\). A nontrivial
zero \(\rho\) of \(\zeta\) produces a denominator pole at
\(s=\rho-1/2\), which lies strictly to the left of this line because
\(\Re\rho<1\). Trivial denominator zeros also lie to the left.

On \(s=1/2+it\), the standard estimates
\[
\frac1{\zeta(1+it)}\ll\log(2+|t|),
\qquad
\zeta(1/2+it)\ll_\epsilon(2+|t|)^{1/4+\epsilon}
\]
and the \(O(t^{-2})\) kernel bound give an \(L^1(\mathbb R)\) boundary
integrand for \(0<\epsilon<3/4\). Riemann--Lebesgue then yields
\[
W_f(x)=cx+o(\sqrt x),
\qquad
M(x)=c+o(\sqrt x),
\qquad
\frac{M(x)}{\sqrt x}\longrightarrow0.
\]
This is a complete unconditional scale-decay theorem and is added to the
VERIFIED PROOF CHAIN. It does not establish \(M(x)\ge0\), nor the sharper
\(O(1)\) or one-sided \(x^{-1/2}\) barrier required by the RH criterion.

### Remaining RH load-bearing claim

The contribution of a hypothetical zero with \(\Re\rho=\beta>1/2\) is of
order \(x^{\beta-1}\) in \(M(x)\), which tends to zero but is larger than
the critical \(x^{-1/2}\) scale. Thus the decay theorem cannot supply the
missing sign. The source's subsequent claim about large-prime memory must be
checked separately rather than treated as a consequence of RH-scale control.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步产生了一个已完整核验的无条件尺度衰减定理，但没有产生新的无条件 RH 证明进展。
