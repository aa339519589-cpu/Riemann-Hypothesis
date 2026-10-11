## Round 82 — the new Liouville--Riesz criterion is a one-way sign test, not an unconditional sign proof

I checked Han's new arXiv paper [*On variants of Pólya's conjecture*](https://arxiv.org/abs/2608.27130), submitted on 27 August 2026. It gives a useful exact reduction. Define
\[
f(x):=-\sum_{n\le x}
\frac{\lambda(n)\log n}{\sqrt n}\log\frac{x}{n}.
\tag{82.1}
\]
The paper proves
\[
f(x)\ge0\ \text{for all sufficiently large }x
\quad\Longrightarrow\quad \mathrm{RH},
\tag{82.2}
\]
by using the Mellin transform
\[
\int_1^\infty f(x)x^{-s+1/2}\frac{dx}{x}
=
\frac{F'(s)}{(s-\frac12)^2},
\qquad
F(s)=\frac{\zeta(2s)}{\zeta(s)}.
\tag{82.3}
\]
Eventual nonnegativity forces the Mellin abscissa of convergence to have no
real singularity in \(\Re s>1/2\); a zero of \(\zeta\) there would create a
pole of \(F'\), yielding (82.2).

The converse result in the same paper assumes all three hypotheses
\[
\mathrm{RH},\qquad
\text{all nontrivial zeros simple},\qquad
\sum_{\gamma>0}
\frac{|\zeta(1+2i\gamma)|}
{\gamma^2|\zeta'(\frac12+i\gamma)|}<\infty.
\tag{82.4}
\]
Under (82.4), the paper obtains an explicit formula whose cubic main term is
positive and hence proves eventual positivity. That is a conditional
converse; it cannot be used to prove the premise of (82.2) without already
assuming RH and additional zero information.

**Established:** (82.2) is a sharp, independently checkable sign criterion
and (82.3) identifies the exact analytic obstruction.

**Remaining load-bearing statement:** prove the eventual sign
\(f(x)\ge0\) from unconditional arithmetic information, or supply an
equivalent new zero-exclusion estimate. The paper does not prove that
statement.

**RH status:** no unconditional proof has been produced.
