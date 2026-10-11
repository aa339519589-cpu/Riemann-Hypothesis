## Round 254 — A/B result: PIHR Stage VIII yields a verified local kernel theorem, but not the global production-dominance inequality

Source audited: Borros Arneth, *Critical Selberg Production Passivity, Equilibrium Storage, and a Quarter-Block Dressed-Memory Closure Candidate for the Riemann Hypothesis*,
[Zenodo record 22111601](https://zenodo.org/records/22111601), PDF SHA-256
707b09a11245508e3cb67a2c0ee59024f0f2de5d5499cb00eef2f3d937483677.
The source explicitly states that the Riemann Hypothesis is not proved and
identifies the global production-versus-memory inequality as its remaining
problem. I independently checked the local positive-kernel theorem used in
the decomposition.

### VERIFIED PROOF CHAIN addition

Let \(\nu\) be a nonzero finite positive measure on \([0,\tfrac12]\), and set
\[
F(u)=\int_{[0,1/2]}e^{\beta u}\,d\nu(\beta),
\qquad m(u)=\frac{F'(u)}{F(u)}.
\]
Under the probability measure with density proportional to
\(e^{\beta u}\,d\nu(\beta)\), \(m(u)=\mathbb E_u[\beta]\) and
\(m'(u)=\operatorname{Var}_u(\beta)\). Since
\(0\le\beta\le\tfrac12\),
\[
\mathbb E_u[\beta^2]\le\tfrac12\mathbb E_u[\beta]=\tfrac12m(u),
\qquad
0\le m'(u)\le m(u)\bigl(\tfrac12-m(u)\bigr).
\]
If \(m(u)>0\), define
\[
S(u)=u+2\log\!\left(1+\frac{1}{2m(u)}\right).
\]
Differentiation gives
\[
S'(u)=1-\frac{2m'(u)}{m(u)(2m(u)+1)}
\ge 1-\frac{1-2m(u)}{1+2m(u)}>0.
\]
If \(m\equiv0\), the kernel below is strictly positive and there is no
zero to analyze. Otherwise \(S\) is strictly increasing.

For \(s\ge u\), let
\(E=e^{-(s-u)/2}\) and
\[
K_s(u)=F(u)\left(\frac{E}{2}-(1-E)m(u)\right).
\]
Because \(F(u)>0\), a zero of \(K_s\) with \(m(u)>0\) is equivalent to
\[
E=\frac{2m(u)}{1+2m(u)}
\quad\Longleftrightarrow\quad s=S(u).
\]
The strict monotonicity of \(S\) gives at most one zero, hence at most one
sign reversal, for every fixed \(s\). Finally, \(m(u)\le\tfrac12\) gives
\[
K_s(u)\ge F(u)\left(E-\tfrac12\right).
\]
If \(s-u\le\log4\), then \(E\ge\tfrac12\), so
\(K_s(u)\ge0\). Thus every most-recent window
\([s-\log4,s]\) is nonnegative. This is a complete unconditional
load-bearing local theorem and is added to the VERIFIED PROOF CHAIN.

### Remaining RH load-bearing claim

The source's exact quarter-block algebra reduces the unresolved sign to
\(P_\beta(s)\ge\mathcal R_\beta(s)\) for \(0<\beta\le\tfrac12\), or to
the stronger coefficient inequalities
\[
D_{m+1}(s)-sD_m(s)\ge
m\sum_{k\ge1}2^{-k}\int_0^{s-k\log4}u^{m-1}D(u)\,du.
\]
The first coefficient's positive asymptotic reserve does not prove the
higher-order inequalities or the required uniform generating-function
comparison. The paper itself says that neither global inequality has been
proved; finite exploratory positivity is not a substitute.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步产生了一个已完整核验的局部无条件定理，但没有产生新的无条件 RH 证明进展。
