# Sharp moving-prime crossover for an exact RH critical theta eigenfamily

Date: 2026-10-12. This is a new quantitative theorem for the **physical** full-prime Dirichlet jump form of round 5, not the diagonal-prime comparison defect. The original operator, theta, all prime powers, Gamma and domains remain unchanged. It builds on the exact real theta-translation family in REPORT.md and the full-prime compression analysis in FULL_PRIME_CRITICAL_SPECTRUM.md. It does not prove RH.

## 1. PNT weighted theta cutoff lemma

Recall \(h(x)=\cosh(x/2)\), \(\Phi>0\) the true even theta kernel, \(\alpha_n=\Lambda(n)/\sqrt n\), and
\[
\lambda_N(x)=\frac1{2h(x)}\sum_{2\le n\le N}\alpha_n
[\Phi(x+\log n)+\Phi(x-\log n)].
\tag{1}
\]
For u>0 set
\[
k_*(u)=u^{-1/2}\Phi(-\log u),\quad
L(c)=\int_0^c k_*(u)\,du,\quad
L(0)=0,\quad L(\infty)=\tfrac12 .
\tag{2}
\]
The normalization is the exact moment
\(\int_{\mathbb R}e^{-x/2}\Phi(x)dx=1/2\).
The complete theta series gives
\[
k_*(u)=O(u^{-5}e^{-\pi/u^2})\ (u\downarrow0),\qquad
k_*(u)=O(u^4e^{-\pi u^2})\ (u\to\infty).
\tag{3}
\]
Thus k is positive, smooth, integrable, and rapidly decaying at both ends.

**Lemma 1.** Let w→∞ and N=N(w)≥2 with N/w→c∈[0,∞]. Then
\[
\boxed{\lambda_{N(w)}(\log w)\longrightarrow L(c).}
\tag{4}
\]
For c in a fixed compact subset of \((0,\infty)\) the convergence is uniform in the ratio N/w (and all sufficiently large w). Only the ordinary unconditional prime number theorem \(\psi(X)=\sum_{n\le X}\Lambda(n)\sim X\) is used.

**Proof.** The exact denominator is \(2h(\log w)=w^{1/2}(1+w^{-1})\); hence
\[
\lambda_N(\log w)
=\frac{1}{1+w^{-1}}\,\frac1w
\sum_{2\le n\le N}\Lambda(n)k_*(n/w)+R_{N,w},
\tag{5}
\]
where \(R_{N,w}\ge0\) arises from \(\Phi(\log(wn))\). The exact theta Gaussian tail for positive argument and \(\Lambda(n)\le\log n\) imply
\[
0\le R_{N,w}
\le Cw^4\sum_{n\ge2}(\log n)n^4e^{-\pi w^2 n^2}
\longrightarrow0
\]
uniformly in N.

For each fixed c>0, PNT implies the weak convergence of rescaled positive arithmetic measures
\((1/w)\sum_{n\ge2}\Lambda(n)\delta_{n/w}\Rightarrow du\)
on compact subintervals of \((0,\infty)\). Testing against k and integrating up to c gives the desired integral. At the lower endpoint, use Chebyshev's \(\psi(X)\le CX\) and eventual increase of k near zero:
\[
\frac1w\sum_{n\le\eta w}\Lambda(n)k_*(n/w)
\le C\eta\sup_{0<u\le\eta}k_*(u)\to0
\quad(\eta\downarrow0).
\]
At the upper endpoint use summation by parts, \(\psi(X)\le CX\), and the eventual rapid decrease of k to bound the weighted sum over n≥Mw by a quantity tending to zero as M→∞. Because the cumulative weighted sums are monotone in c and L is continuous, finite-grid monotone interpolation proves local uniform convergence. For N/w→0 or ∞, use monotone comparison with fixed ratios tending respectively to zero or ∞. \(\square\)

## 2. The true theta escape has an exact Gamma spatial law

Write
\[
a_*=\tfrac12\log2,\quad
v_t(x)=\frac{\Phi(x+t)+\Phi(x-t)-2\cosh(t/2)\Phi(x)}{m(x)},
\quad m(x)=\sqrt{\Phi(x)/(2h(x))}.
\]
The inherited translation theorem proves \(v_t\in\ker H\) for \(0<t<a_*\), and
\(\|v_t\|_2^2\sim(3/128)(a_*-t)^{-5/2}\).
Let \(\delta=a_*-t\), \(u_\delta=v_{a_*-\delta}/\|v_{a_*-\delta}\|_2\), and define \(Y_\delta(x)=\delta e^{2|x|}\). Then
\[
\boxed{(Y_\delta)_*(|u_\delta(x)|^2dx)
\ \Rightarrow\ g(y)dy,\qquad
g(y)=\frac{(2\pi)^{5/2}}{\Gamma(5/2)}
y^{3/2}e^{-2\pi y}\mathbf 1_{y>0}.}
\tag{6}
\]
Here * means pushforward of probability measure.

**Proof.** The actual n=1 theta asymptotic (including its denominator m) gives, uniformly for t close to a* and x→+∞,
\[
v_t(x)=2\pi e^{5x/2-9t/2}
e^{-\pi(e^{-2t}-1/2)e^{2x}}(1+o(1)).
\]
The negative x tail is its even mirror. In the positive tail substitute \(y=\delta e^{2x}\), so \(dx=dy/(2y)\). Since \(\pi(e^{-2t}-1/2)/\delta\to\pi\), the rescaled unnormalized density tends to \(2\pi^2e^{-9a_*}y^{3/2}e^{-2\pi y}\). There are two tails, while fixed compact x intervals contribute \(O(\delta^{5/2})\) after normalization. Uniform theta Gaussian bounds dominate the scaled density by \(Cy^{3/2}e^{-cy}\) for y above the rescaled fixed cutoff. Division by the squared-norm asymptotic \(3/128\) gives precisely g. \(\square\)

## 3. Actual physical energy transition, not a model proxy

For every N, let
\[
J_N=M_{\lambda_N}-S_N,\qquad
S_N=\sum_{2\le n\le N}\alpha_nM_m(\tau_{\log n}+\tau_{-\log n})M_m .
\]
These represent exactly the physical finite-prime Dirichlet energies
\(\langle u,J_Nu\rangle=E_{P,N}(U^{-1}u)\); see round 5 and FULL_PRIME_CRITICAL_SPECTRUM.md.

**Theorem 2 (sharp critical prime scale).** Suppose integers \(N(\delta)\ge2\) obey
\[
N(\delta)\sqrt\delta\longrightarrow c\in[0,\infty].
\tag{7}
\]
Then the exact normalized theta eigenvector satisfies
\[
\boxed{\lim_{\delta\downarrow0}
E_{P,N(\delta)}(U^{-1}u_\delta)
=F(c)
:=\int_0^\infty g(y)L(c/\sqrt y)\,dy .}
\tag{8}
\]
Equivalently for finite c>0,
\[
\boxed{F(c)=\int_{-\infty}^\infty e^{-z/2}\Phi(z)
\frac{\gamma(5/2,2\pi c^2 e^{2z})}{\Gamma(5/2)}\,dz.}
\tag{9}
\]
Here \(\gamma\) denotes the lower incomplete Gamma function. F is continuous and strictly increasing, with
\[
F(0)=0,\quad 0<F(c)<\tfrac12\ (0<c<\infty),\quad F(\infty)=\tfrac12.
\tag{10}
\]
In particular \(N\sqrt\delta\to0\) loses the entire half-unit physical prime energy, while \(N\sqrt\delta\to\infty\) captures the entire half. The characteristic prime scale is **\(N\asymp\delta^{-1/2}\)**.

**Proof.** First the off-diagonal term is uniformly negligible for arbitrary moving N:
\[
\sup_{N\ge2}\|S_Nu_\delta\|_2\longrightarrow0.
\tag{11}
\]
Indeed on the true critical eigenspace each fixed S_N is compact (it factors through the compact \(M_m|_{\ker H}\)), and the S_N converge in operator norm to the compact full S_m. For fixed M split N<M (finitely many compact operators) and N≥M (an arbitrarily small norm distance to S_m). Since \(u_\delta\rightharpoonup0\), this proves (11).

For x>0 put \(w=e^x\), \(y=\delta w^2\). On any compact \(0<y_0\le y\le y_1\), \(w=\sqrt{y/\delta}\to\infty\) and \(N/w\to c/\sqrt y\). Lemma 1 therefore yields, uniformly in this y interval,
\[
\lambda_{N(\delta)}
\left(\tfrac12\log(y/\delta)\right)
\longrightarrow L(c/\sqrt y).
\tag{12}
\]
The same holds at x<0 because \(\lambda_N\) is even. The probability measures of \(Y_\delta\) are tight and converge to g by (6), and \(0\le\lambda_N\le\lambda_P\) with bounded true \(\lambda_P\). Thus diagonal expectations converge by cutoff of y near 0 and ∞, followed by uniform convergence on the remaining compact interval. Combine this with (11) to obtain (8).

Substitute \(u=e^{-z}\) in \(L(c/\sqrt y)\): it becomes
\(\int_{\log(\sqrt y/c)}^\infty e^{-z/2}\Phi(z)dz\).
Tonelli and the Gamma CDF of g yield (9). Positivity of \(\Phi\), monotonicity of L, the exact moment \(\int e^{-z/2}\Phi(z)dz=1/2\), and dominated convergence establish (10). \(\square\)

## 4. Mathematical scope

The cutoffs N and the parameter \(\delta\) have been coupled and then sent to their limits by the **unconditional** PNT and the genuine theta kernel, retaining all prime powers and the original unitary weights. The nontrivial crossover is not a numerical fit and does not require any assumed zero location.

This precise scale explains why fixed-prime truncations, even when accompanied by valid vanishing norm tails in a *different* operator decomposition, can miss a macroscopic prime-jump energy on actual critical eigenvectors. It provides a testable multiscale constraint for a complete RH proof, but does not establish positivity of H off its kernel or exclude any off-critical zeros. **NO NEW UNCONDITIONAL RH THEOREM PROVED.** The round-5 operator/domain construction and translation theorem remain inherited proof dependencies requiring independent review. No existing repo file is modified.
