# Mathematical audit: actual Mellin moments of full prime energy

Date: 2026-10-12. Reviewed: PRIME_ENERGY_MELLIN_MOMENTS.md. This is an internal proof audit, NOT a third-party referee or formal proof-assistant certificate. The scope is an auxiliary identity for the actual full theta and complete von Mangoldt energy, not a proof of RH.

## 1. Input and logical independence

The spectral statement H v_t=0 is inherited from the original theta/source identity and exact derivative-mode domain proof. The new **arithmetic moment theorem** does not require this spectral claim: it starts from literal nonnegative prime edge energies E_n(q_t), the explicit theta family f_t, and the unconditional PNT. Thus the spectral essential-spectrum independent-review marker does not logically affect the arithmetic moment estimates.

The proof uses no critical-strip zero information, no zero simplicity and no assumptions about zeros. The completed factor \(\xi(1+s)\) appears only at real s and equals the explicitly positive theta Mellin integral. At s=-5 one must use \(\xi(-4)=\xi(5)>0\), not \(\zeta(-4)=0\); the completed gamma factor cancels that trivial zeta zero.

## 2. Full prime algebra, no hidden factor two

For real even q, f=Phi q and v=f/m, the literal expansion of each n-edge gives
\[
\sum n^s E_n(q)=
\int |v(x)|^2\frac{1}{2h(x)}
\sum_{n\ge2}\Lambda(n)n^{s-1/2}
\{\Phi(x-\log n)+\Phi(x+\log n)\}dx-\langle f,S_sf\rangle.
\]
Each prime power is counted once in E_n, and S_s contains both shifts. The coefficient \(1/(2h)\), not \(1/h\), is essential.

Put X=e^x, u=n/X. The backwards rate after dividing by X^s becomes
\[
\frac{X^{1/2}}{2h(x)}
\left(\frac1X\sum_n\Lambda(n)u^{s-1/2}\Phi(-\log u)\right).
\]
Unconditional PNT gives the rescaled measure \(X^{-1}\sum\Lambda(n)\delta_{n/X}\to du\) against compactly supported tests. The true test \(\phi_s(u)=u^{s-1/2}\Phi(-\log u)\) is dominated as u->0 by a power times \(e^{-\pi/u^2}\) and as u->infinity by a power times \(e^{-\pi u^2}\). Chebyshev \(\psi(Y)\ll Y\) with partial summation controls both noncompact tails. Its integral is
\[
\int_0^\infty u^{s-1/2}\Phi(-\log u)du
=\int_{\mathbb R}e^{-(s+1/2)y}\Phi(y)dy
=\xi(-s)=\xi(1+s).
\]
No Euler product is continued into its nonconvergent region.

For the cross term, fix \(a>\max(0,s+1/2)\); the real t source family \(e^{a|x|}f_t\) has uniformly bounded L2 norm up to t=a*. Translation correlations are \(O(n^{-a})\), so the entire weighted von Mangoldt sum \(\sum \Lambda(n)n^{s-a-1/2}\) converges absolutely. After multiplying by \(\delta^{s/2}/\|v_t\|^2\), the bounded cross term is \(O_s(\delta^{(s+5)/2})\), vanishing for s>-5.

## 3. Squared-norm normalization and critical borderline

On each true theta tail,
\[
v_t(x)\sim2\pi e^{5|x|/2-9t/2}e^{-c_t e^{2|x|}},
\quad c_t=\pi(e^{-2t}-1/2)\sim\pi\delta.
\]
Double the positive half-axis and use r=e^(2x). For s>-5,
\[
I_s(t)\sim4\pi^2e^{-9a_*}\Gamma((s+5)/2)(2c_t)^{-(s+5)/2}.
\]
Thus the actual moment ratio is \((2\pi)^{-s/2}\Gamma((s+5)/2)/\Gamma(5/2)\), without a missing Fourier normalization.

At s=-5 the r-power becomes r^(-1), giving \(\log(1/\delta)\). One cannot interchange the limits s->-5 and delta->0. Exact SymPy algebra, independently executed during this audit, confirmed
\[
4\pi^2\,2^{-9/2}\Gamma(5/2)(2\pi)^{-5/2}=3/128,
\]
\[
(128/3)\,4\pi^2\,2^{-9/2}\xi(5)=40\sqrt2\,\zeta(5),
\]
and the right side of the s>-5 moment formula has pole residue \(80\sqrt2\zeta(5)\) at s=-5. The residue is twice the logarithmic coefficient, consistent with \(\Gamma((s+5)/2)\sim2/(s+5)\).

For s<-5, the bound \(|v_t|^2\lambda_s(x)\le C_s e^{(s+5)|x|}\) is integrable and uniform through t=a*. Dominated convergence and the uniformly absolutely summable weighted cross shift give the finite endpoint energy. It is strictly positive because the endpoint q is not log2-periodic.

## 4. Separate FLOATING-POINT sanity, not an interval certificate

An independently calculated six-mode theta and actual von Mangoldt prime-power sampling through n<=8exp(x) gave these approximate ratios \(\lambda_s(x)e^{-sx}/\xi(1+s)\), columns s=-3,0,1:

| x | -3 | 0 | 1 |
|---|---|---|---|
| 3 | .951741 | .952439 | .951467 |
| 4 | .984570 | .982007 | .982399 |
| 5 | .993552 | .993307 | .993688 |

These tests check only direction and normalization; they are not proofs of PNT, the omitted theta tail, or RH. The provided file check_mellin_moment_constants.py contains reproducible algebra and numerical checks. Their rigorous portion is confined to exact SymPy constant identities.

## 5. Final scope

The theorem is a true full-prime uniform-integrability result for known equality-mode energy distributions. It does **not** prove the needed lower bound on the orthogonal complement, exclude a true subcritical eigenstate, or prove RH. Nothing in the full-real-axis Mellin positivity of \(\xi(s)\) can be used as a critical-strip zero theorem without a further valid argument.

**NO NEW UNCONDITIONAL RH THEOREM PROVED.**
