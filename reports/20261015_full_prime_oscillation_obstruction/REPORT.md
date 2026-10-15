# The full-prime Green transfer does not contract oscillation

Date: 2026-10-15.

This report rules out a strong bounded-ratio comparison for the complete
positive reference form. It does **not** disprove the Hilbert-space
inequality $N\le P$, give a negative Weil-form vector, or settle RH.
All prime powers, the continuous Gamma kernel, and the pole term are kept.

## 1. Forms, the variational solution, and the claim being tested

Use the theta normalization and energy completions of the
[full-prime Green report](../20261013_full_prime_green_reference/REPORT.md).
For $x\ge0$, put $z_n=\pi n^2e^{2x}$ and
\[
\Phi(x)=e^{x/2}\sum_{n\ge1}(4z_n^2-6z_n)e^{-z_n},\qquad
\psi(x)=-\Phi'(x)
=e^{x/2}\sum_{n\ge1}(8z_n^3-30z_n^2+15z_n)e^{-z_n}.
\]
The complete theta identity makes $\Phi$ even and $\psi$ odd;
$\psi(x)>0$ for $x>0$, and
\[
\int_0^\infty s(x)\psi(x)\,dx=\frac18,
\qquad s(x)=\sinh(x/2).
\tag{1}
\]
These facts and the theta bounds are proved in the
[original form foundation](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md)
and the linked full-prime Green report. In particular, for large $x$,
\[
\psi(x)\asymp e^{13x/2}e^{-\pi e^{2x}},\qquad
|\psi'(x)|/\psi(x)\le C e^{2x}.
\tag{2}
\]
Write $d_n=\log n$, $\alpha_n=\Lambda(n)/\sqrt n$, and
$\kappa(t)=e^{-t/2}/(1-e^{-2t})$. On compact smooth ratios with
smooth even extension at zero, define
\[
\begin{aligned}
P_\Gamma[r]&=\iint_{(0,\infty)^2}\psi(x)\psi(y)
 [\kappa(|x-y|)-\kappa(x+y)]|r(x)-r(y)|^2\,dx\,dy,\\
P_F[r]&=2\sum_{n\ge2}\alpha_n\int_0^\infty
 \psi(x)\psi(x+d_n)|r(x)-r(x+d_n)|^2\,dx,\\
P_{\rm pole}[r]&=4\iint_{(0,\infty)^2}s(x)\psi(x)s(y)\psi(y)
 |r(x)-r(y)|^2\,dx\,dy,\\
N[r]&=\sum_{n\ge2}\alpha_n\int_0^{d_n}
 \psi(x)\psi(d_n-x)|r(x)-r(d_n-x)|^2\,dx,
\qquad P=P_\Gamma+P_F+P_{\rm pole}.
\end{aligned}
\tag{3}
\]
Use real bilinear polarizations below. The published bound $N\le CP$,
with a finite constant not asserted to be one, makes the following
variational solution well-defined in the $P$-energy completion modulo
constants: for every compact smooth input $a$, let $h=\mathcal K a$
satisfy
\[
P(h,b)=N(a,b)\quad\hbox{for every compact smooth ratio }b.
\tag{4}
\]
This is a Riesz solution, not a pointwise inverse imposed on an
unweighted source space. The pole part gives a locally square-integrable
ratio representative: after centering, $\int s\psi h^2\le P[h]$.
The completed edge differences agree with that representative by local
$L^2$ convergence. Constants do not change (4).

For a real measurable function, write
$\operatorname{osc}h=\operatorname*{ess\,sup}h- \operatorname*{ess\,inf}h$.

**Theorem.** It is false that, for every compact smooth real ratio $a$,
the solution (4) has a bounded representative with
\[
\operatorname{osc}(\mathcal K a)\le\operatorname{osc}(a).
\tag{5}
\]
Thus a universal contraction on the bounded-ratio quotient by constants
cannot prove the critical Hilbert comparison. The conclusion allows
that some solution is unbounded; it does not assume a bounded extension
of $\mathcal K$ in advance.

## 2. Exact complete rows and their far-wing masses

Set
\[
U=\int_0^\infty e^{y/2}\psi(y)\,dy,\qquad
V=\int_0^\infty e^{-y/2}\psi(y)\,dy,
\qquad \theta=\frac1{4U}.
\tag{6}
\]
Equation (1) gives $U-V=1/4$, so $0<\theta<1$ and
$V/U=1-\theta$. Put
\[
L(x)=\sum_{n>e^x}\alpha_n\psi(d_n-x),\quad
A_-(x)=\sum_{2\le n<e^x}\alpha_n\psi(x-d_n),\quad
A_+(x)=\sum_{n\ge2}\alpha_n\psi(x+d_n).
\]
The unconditional prime number theorem, including all Mangoldt labels,
and the complete theta tails give
\[
L(x)=e^{x/2}(U+o(1)),\qquad
A_-(x)=e^{x/2}(V+o(1)),\qquad
A_+(x)=o(e^{x/2}).
\tag{7}
\]
For completeness, on a fixed compact interval of return coordinates,
the measures $e^{-x/2}\sum \Lambda(n)n^{-1/2}\delta_{\log n-x}$
converge to $e^{y/2}dy$, and the analogous past-coordinate measures
converge to $e^{-y/2}dy$. Equivalently, the past row uses the continuous
test $u^{-1/2}\psi(-\log u)$ on $0<u<1$, whose zero endpoint is
theta-flat. The elementary Chebyshev bound
$\sum_{n\le t}\Lambda(n)\le Ct$, followed by unit logarithmic shells
and (2), controls the omitted tails uniformly. This proves (7) for real
$x\to\infty$, hence also uniformly in shrinking neighborhoods of
any two centers tending to infinity.

Relative to the vertex measure $\psi(x)^2dx$, the complete rows on
a smooth test are
\[
\begin{aligned}
L_N a(x)&=\frac2{\psi(x)}\sum_{n>e^x}\alpha_n\psi(d_n-x)
 [a(x)-a(d_n-x)],\\
L_{P,F}h(x)&=\frac2{\psi(x)}\left\{
 \sum_{n\ge2}\alpha_n\psi(x+d_n)[h(x)-h(x+d_n)]
 +\sum_{2\le n<e^x}\alpha_n\psi(x-d_n)[h(x)-h(x-d_n)]\right\},\\
L_{P,\rm pole}h(x)&=\frac{s(x)}{\psi(x)}[h(x)-m],
\qquad m=8\int_0^\infty s(y)\psi(y)h(y)\,dy.
\end{aligned}
\tag{8}
\]
The Gamma row is understood weakly when $h$ is merely bounded.
The coefficient in the last row follows directly from the factor four
in (3), not from discarding the pole. Define
\[
R_X=\frac{2Ue^{X/2}}{\psi(X)}.
\tag{9}
\]
At a large output center $X$, the reflected rate is $R_X(1+o(1))$,
the past rate is $(1-\theta)R_X+o(R_X)$, and the pole rate is
$\theta R_X+o(R_X)$. Both output tests below use the **same** mean $m$.

## 3. Two separated finite return grids

Fix $0<\eta<\theta/2$. Choose a compact interval
$K=[a,b]\subset(0,\infty)$ with
\[
\int_K e^{y/2}\psi(y)\,dy>(1-\eta)U.
\tag{10}
\]
Take output centers $X_1=X$ and $X_2=X+D$, where
$D=\log\sqrt2$, and put $\varepsilon_X=e^{-e^X}$.
The reflected landing points in $K$ are
\[
\mathcal G_i(X)=\{\log n-X_i\in K:\Lambda(n)>0\}.
\]
Each grid is finite. Their mutual spacing is at least $c_K e^{-2X}$
for large $X$. Indeed, the relevant integers $n,m$ are between
fixed positive multiples of $e^X$, and
\[
|2n^2-m^2|\ge1
\quad\Longrightarrow\quad
|\sqrt2 n-m|\ge c_K e^{-X}
\quad\Longrightarrow\quad
|\log n-\log m+D|\ge c_K e^{-2X}.
\tag{11}
\]
Within each grid, the usual integer spacing gives an even larger lower
bound $c_K e^{-X}$. Therefore, for sufficiently large $X$, all the
required landing neighborhoods of radius $2\varepsilon_X$ for the two
grids are disjoint. The output neighborhoods are disjoint from $K$
and from each other.

Choose a real compact smooth $a_X$, zero near zero, with values in
$[-1,1]$, equal to $+1$ on the $2\varepsilon_X$-neighborhood of
$X_1$, and $-1$ on that of $X_2$. Make it equal to $-1$ around
every point of $\mathcal G_1(X)$, and $+1$ around every point of
$\mathcal G_2(X)$, with the same neighborhood radius. A finite smooth
bump construction does this, and $\operatorname{osc}(a_X)=2$.
No bound uniform in $X$ is claimed for its derivatives.

Fix one nonnegative $\mu\in C_c^\infty(-1,1)$ with integral one,
and set $\mu_{i,X}(x)=\varepsilon_X^{-1}\mu((x-X_i)/\varepsilon_X)$.
The mollifiers are thus scaled translates of a single fixed bump.
Equations (7), (10), and
(11), together with $a_X\in[-1,1]$, imply
\[
\begin{aligned}
\frac1{R_{X_1}}\int\mu_{1,X}L_Na_X&\ge2(1-\eta)+o(1),\\
\frac1{R_{X_2}}\int\mu_{2,X}L_Na_X&\le-2(1-\eta)+o(1).
\end{aligned}
\tag{12}
\]
Only the selected compact returns are used. All other reflected terms
have the favorable sign, since each output already takes an extremal
value of $a_X$. Relative variation of $\psi$ on the output supports
is $O(e^{2X}\varepsilon_X)=o(1)$.

## 4. The Gamma row is negligible in the required weak tests

Assume (5), and shift the representative $h_X=\mathcal K a_X$ by a
constant so that $-1\le h_X\le1$ almost everywhere. Write $m_X$
for its mean in (8). Thus $m_X\in[-1,1]$. Use in (4) the actual compact
smooth ratio tests
\[
 b_{i,X}(x)=\mu_{i,X}(x)/\psi(x)^2.
\tag{13}
\]
The source corresponding to (13) is $\mu_{i,X}/\psi$, still smooth
and compactly supported away from zero. No point evaluation of the
Green solution is involved.

Here is a uniform bound for $P_\Gamma(h_X,b_{i,X})$. In the next
estimate, $\mu$ denotes the scaled mollifier $\mu_{i,X}$. Set
$\beta_X=e^{-3X}$. For $|x-y|<\beta_X$, symmetrize the weak
pairing before estimating. Its test-factor difference is exactly
\[
 \mu(x)\frac{\psi(y)}{\psi(x)}
 -\mu(y)\frac{\psi(x)}{\psi(y)}.
\]
If this difference is nonzero and $|x-y|<\beta_X$, both points
lie within $2\beta_X$ of the output center. On this band the logarithmic derivative
bound in (2) gives relative weight variation $O(e^{2X}|x-y|)$.
The translation estimate for the probability mollifier is
$\|\mu(\cdot+t)-\mu\|_1\le C\min(1,|t|/\varepsilon_X)$.
Since $\kappa(t)\le C/t$ for $0<t<1$, the resulting contribution
is at most
\[
C\int_0^{\beta_X}
 \left\{\frac{\min(1,t/\varepsilon_X)}t+e^{2X}\right\}\,dt
\le C(1+\log(\beta_X/\varepsilon_X)+e^{2X}\beta_X)
=O(e^X).
\tag{14}
\]
This estimates the whole difference of the test factors; it does not
assign derivatives to $h_X$.

On $\beta_X\le|x-y|<1$, use $|h_X(x)-h_X(y)|\le2$, and
estimate the row with the mollifier at one endpoint. Monotonicity of
$\psi$ sufficiently far out and (2) give the deliberately coarse bound
$C e^{3X}\psi(X_i-1)/\psi(X_i)+C e^X$.
On $|x-y|\ge1$, use the complete exponential kernel bound and
$\int e^{y/2}\psi(y)dy=U$, obtaining
$C e^{-X_i/2}/\psi(X_i)$. The subtracted reflected Gamma kernel
is no larger than the same-wing kernel and is included in these estimates.
Consequently
\[
\frac{|P_\Gamma(h_X,b_{i,X})|}{R_{X_i}}
\le C\left\{e^X\psi(X_i)e^{-X_i/2}
 +e^{3X-X_i/2}\psi(X_i-1)+e^{-X_i}\right\}=o(1).
\tag{15}
\]
All constants can be fixed for $i=1,2$. The full future-prime pairing
is likewise $o(R_{X_i})$, by $A_+(x)=o(e^{x/2})$ and boundedness of
$h_X$. Neither assertion gives a pointwise Gamma value for $h_X$.

## 5. The shared pole mean yields a contradiction

The remaining past and pole rows in (8) are absolutely integrable
against the fixed mollifiers. Since $-1\le h_X\le1$, the first
output obeys
\[
\frac{P(h_X,b_{1,X})}{R_{X_1}}
\le 2-\theta(1+m_X)+o(1),
\tag{16}
\]
while the second obeys
\[
\frac{P(h_X,b_{2,X})}{R_{X_2}}
\ge-2+\theta(1-m_X)+o(1).
\tag{17}
\]
For example, the upper bound is the sum of
$(1-\theta)(h_X+1)$ from the past row and
$\theta(h_X-m_X)$ from the pole row, averaged over the mollifier,
then bounded using $h_X\le1$. The lower bound is identical with
$h_X\ge-1$. The error estimates are uniform over every bounded
representative with this normalization.

Using (4) and (12) in (16)--(17) gives
\[
\theta(1+m_X)\le2\eta+o(1),\qquad
\theta(1-m_X)\le2\eta+o(1).
\]
Adding yields $2\theta\le4\eta+o(1)$, contrary to
$\eta<\theta/2$ for large $X$. This proves the theorem.

## 6. Scope

The inputs are legitimate compact smooth ratios, but their rapidly
separated return patterns have no uniform Hölder bound. Accordingly,
this result does not exclude a contraction restricted to a hypothetical
actual eigenratio with additional quantitative constraints.
It also does not imply that the positive self-adjoint edge Green
operator $TT^*$ has norm greater than one: oscillation modulo constants
and the $P/N$ Hilbert norms are different comparisons. The critical
Hilbert inequality and the genuine-prime upper bound remain open.
