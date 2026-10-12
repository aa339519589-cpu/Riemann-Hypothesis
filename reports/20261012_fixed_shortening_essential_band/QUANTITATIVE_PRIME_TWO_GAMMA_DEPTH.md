# Quantitative all-N obstruction: a single retained prime forces superpolynomial Gamma depth

Date: 2026-10-12. This is a new **quantitative no-go** strengthening ESSENTIAL_SPECTRUM_COUNTABLE_SHORTING.md. It concerns only the exact lower comparator already used in the full RH research, not the original H spectrum. It assumes its previously proved full-theta Riesz source-tail and bounded canonical infinite-mode correction.

## 1. Result, including every varying finite prime cutoff

Let \(J\ge1,N\ge2\) be *arbitrary finite integers*, \(c_J=\sum_{j=0}^{J-1}(j+\frac14)^{-1}\), and
\[
g_{J,N}(x)=(c_J-C_0)m(x)^2
-m(x)\sum_{n=2}^N\frac{\Lambda(n)}{\sqrt n}
[m(x+\log n)+m(x-\log n)].
\]
The actual full Jacobi-theta weight is \(m(x)^2=\Phi(x)/(2\cosh(x/2))\). Denote \(g_-=\inf_{\mathbb R}g_{J,N}\), and let \(\delta_N>0\) be the canonical omitted-prime scalar allowance in the countably shorted comparator. The exact essential-spectrum theorem in the preceding file gives
\[
\sigma_{\rm ess}(K_\varepsilon+F_\infty)
=\{\varepsilon\}\cup[\varepsilon-\delta_N+g_-,\,
\varepsilon-\delta_N+g_+].
\tag{1}
\]

**Theorem 1 (explicit n=2 lower bound, uniform in all N).** With the absolute constant
\[
\boxed{C_*=256\pi^2e^{-16\pi}>0,}
\]
we have for **every** \(J\ge1,N\ge2\)
\[
\boxed{-g_-\ge C_*[1+|c_J-C_0|]^{-5/3}
\ge C_*(14+\log J)^{-5/3}.}
\tag{2}
\]
In particular, the exact full-theta lower comparator has *negative essential spectrum* for **every finite N>=2** whenever
\[
\boxed{0<\varepsilon<C_*(14+\log J)^{-5/3}.}
\tag{3}
\]
This obstruction persists even if N is chosen as an arbitrarily large function of epsilon.

**Corollary 2 (superpolynomial necessary J scale).** To avoid this one-prime negative-essential-spectrum obstruction for every sufficiently small epsilon, it is **necessary** that
\[
\boxed{\log J(\varepsilon)\ge
\left(\frac{C_*}{\varepsilon}\right)^{3/5}-14.}
\tag{4}
\]
Consequently every fixed polynomial gamma-depth policy \(J(\varepsilon)=O(\varepsilon^{-M})\), with M fixed, fails the finite-negative-index criterion for this lower comparator at all sufficiently small positive epsilon, **regardless of the growth of N(epsilon)**.

This is a necessary condition, not a sufficient positivity theorem. The very small explicit constant is deliberate: it comes from a globally valid elementary bound and is not fitted from numerical data.

## 2. Fully explicit theta bounds

For \(x\ge0\), set \(r=e^{2x}\). Directly from the complete theta series,
\[
m(x)^2=
\frac{4\pi^2r^2e^{-\pi r}}{1+r^{-1/2}}
\sum_{n\ge1}n^4\left(1-\frac3{2\pi n^2r}\right)
e^{-\pi(n^2-1)r}.
\tag{5}
\]
This is an exact algebraic identity, with **every** positive theta summand included. If \(r\ge4\), then all parentheses are positive. The first term gives
\[
m(x)^2\ge
4\pi^2r^2e^{-\pi r}
\frac{1-3/(2\pi r)}{1+r^{-1/2}}
>\pi^2r^2e^{-\pi r}.
\tag{6}
\]
Indeed \(1-3/(2\pi r)>7/8\) and \(1+r^{-1/2}\le3/2\).

For an upper bound, use \(n^4\le16^{n-1}\) and \(n^2-1\ge3(n-1)\) for \(n\ge1\). Then
\[
\sum_{n\ge1}n^4e^{-\pi(n^2-1)r}
\le\frac1{1-16e^{-3\pi r}}<2\quad(r\ge4).
\]
Equation (5) therefore gives \(m(x)^2<8\pi^2r^2e^{-\pi r}<16\pi^2r^2e^{-\pi r}\). Thus the two-sided *actual complete-theta* bound
\[
\boxed{\pi r e^{-\pi r/2}<m(\tfrac12\log r)
<4\pi r e^{-\pi r/2}\qquad(r\ge4)}
\tag{7}
\]
is valid without dropping an uncontrolled theta mode.

If \(r\ge16\), both r and r/4 satisfy this bound. Since replacing x by \(x-\log2\) replaces r by r/4,
\[
\boxed{
\frac{m(x-\log2)}{m(x)}
>\frac1{16}\exp[(3\pi/8)r]\quad(r\ge16).}
\tag{8}
\]

## 3. Select one genuine n=2 edge; no use of other prime signs

Set \(b=1+|c_J-C_0|\ge1\), \(K=e^{6\pi}\), and choose
\[
r=\frac8{3\pi}\log(Kb)\ge16,\qquad x=\frac12\log r.
\tag{9}
\]
The genuine n=2 coefficient is
\(\alpha_2=\Lambda(2)/\sqrt2=\log2/\sqrt2>1/3\).
Since \(e^{6\pi}>96\), (8) gives
\[
\alpha_2\frac{m(x-\log2)}{m(x)}
>\frac{\alpha_2Kb}{16}>2b.
\tag{10}
\]
All remaining retained prime-power terms are nonnegative. Therefore, for **every N>=2**,
\[
\begin{aligned}
g_{J,N}(x)
&\le |c_J-C_0|m(x)^2-\alpha_2m(x)m(x-\log2)\\
&< (b-1-2b)m(x)^2\le-bm(x)^2.
\end{aligned}
\tag{11}
\]
Use (6), (9), and \(e^{-\pi r}=(Kb)^{-8/3}\):
\[
\begin{aligned}
-g_-
&\ge -g_{J,N}(x)>b\pi^2r^2e^{-\pi r}\\
&=\frac{64}{9}e^{-16\pi}
[\log(Kb)]^2b^{-5/3}\\
&\ge 256\pi^2e^{-16\pi}b^{-5/3}.
\end{aligned}
\tag{12}
\]
This is the first inequality in (2).

For the second, the original \(0<C_0<8\) and
\[
c_J=4+\sum_{j=1}^{J-1}\frac1{j+1/4}
\le4+\sum_{j=1}^{J-1}\frac1j
\le5+\log J
\]
give \(b=1+|c_J-C_0|<14+\log J\). Because \(b\mapsto b^{-5/3}\) is decreasing, this proves all of (2).

## 4. Necessary depth and asymptotic no-go

If \(0<\varepsilon<C_*(14+\log J)^{-5/3}\), then (2) gives \(\varepsilon<-g_-\). Since \(\delta_N>0\) for every N, this implies
\[
\varepsilon-\delta_N+g_-<0.
\]
By (1), the exact infinite-mode **lower comparator** has negative essential spectrum and hence infinitely many negative directions. This proves (3), uniformly over all varying finite N. The contrapositive gives the necessary condition (4).

For any fixed M and fixed A, \(J(\varepsilon)\le A\varepsilon^{-M}\) implies
\((14+\log J)^{5/3}=O(\log^{5/3}(1/\varepsilon))\).
But \(\varepsilon\log^{5/3}(1/\varepsilon)\to0\). Hence inequality (3) eventually holds: every polynomial-in-1/epsilon choice for J fails, even after the exact countable shorting and regardless of the finite-prime cutoff N.

**Interpretation:** the first *actual* prime p=2 already enforces a logarithmically distant spatial region where the truncated-Gamma diagonal is smaller than the retained prime multiplication. This cannot be patched by repairing only the selected true zero-mode space. To obtain an all-epsilon RH proof via this particular comparison, one must change the comparison itself or allow much faster growth of the Gamma truncation and subsequently solve the remaining full-space signed-spectrum burden. No negative eigenvalues of the original H have been inferred.

**Accepted new quantitative obstruction, NO NEW UNCONDITIONAL RH THEOREM PROVED.**
