# Internal clean derivation and scope audit: explicit zero-free Mellin source

Date: 2026-10-12. Reviewed EXPLICIT_MELLIN_ACTIVATOR.md against the original positive theta/kernel realization, the arithmetic source convention and both nonvanishing claims. This audit is performed within the project, not by an external referee and not by a formal proof assistant. A finite diagnostic is clearly separated below.

## A. Theta source, domain, and no missing normalizations

The original source is the full theta Phi with \(\int\Phi(x)e^{(s-1/2)x}dx=\xi(s)\). It is even and strictly positive, while \(d\nu=2\Phi\cosh(x/2)dx\) is a probability measure. Therefore dividing the explicit \(f_A=e^{-A\cosh2x}\) by Phi is a legal real even source, with no need to invert Xi or divide by an unknown zero.

The true first-mode large-x exponent of Phi is \(-\pi e^{2x}\); the exponent in the constructed f_A is \(-(A/2)e^{2x}\). Their quotient decays, with the exact positive difference \((A/2-\pi)e^{2x}\), iff \(A>2\pi\). This is why the chosen strict parameter range is needed. It also gives all x-derivative tails. For the Hilbert image \(v_A=f_A/m\), \(m\sim2\pi e^{2x-\pi e^{2x}/2}\), so \(v_A\) has even better Gaussian-of-exponential decay. Since \(f_A\in\mathcal S\), \(b(D)f_A\in L^2\) for the complete \(b(t)=O(\log(2+|t|))\) and \(m b(D)f_A\in L^2\). This meets the actual maximal positive-form operator representation, and the bounded full prime potential preserves the domain. No coefficient restriction on the prime sum is omitted.

The arithmetic convention is \(\mathcal B_q(s)=\int \Phi q\,e^{-(s-1/2)x}dx\), not \(\int \Phi q\,e^{+(s-1/2)x}dx\). Its sign is harmless for this even f, but the exact factor is important:
\[
\mathcal B_{q_A}(s)=\tfrac12\int_{\mathbb R}
e^{-A\cosh u-(s-1/2)u/2}du
=K_{(s-1/2)/2}(A).
\]
The factor 1/2 from \(dx=du/2\) cancels the factor 2 between the full-line and positive-half-line K integrals; there is **no extra factor 2** in the final activation. This was also checked by separate numerical integration.

## B. Independent differential-equation verification of the K order-zero location

Define \(K_\nu(r)=\int_0^\infty e^{-r\cosh u}\cosh(\nu u)du\). Differentiation under the integral is legitimate for \(r>0\), complex fixed \(\nu\). Note the exact integration-by-parts identity
\[
r^2\sinh^2u-r\cosh u
=-r e^{r\cosh u}\partial_u(e^{-r\cosh u}\sinh u).
\]
It follows, with both endpoint terms zero, that
\[
r^2K_\nu''+rK_\nu'-r^2K_\nu
=r\nu\int_0^\infty e^{-r\cosh u}\sinh u\sinh(\nu u)du
=\nu^2K_\nu .
\]
Thus the Bessel equation and its **minus sign** in the Liouville transformation are independently checked:
\[
(-\partial_y^2+e^{2y})K_\nu(e^y)=-\nu^2K_\nu(e^y).
\]
If \(K_\nu(A)=0\), both the Dirichlet condition and super-exponential decay hold. The selfadjoint energy identity forces
\(-\nu^2=\frac{\int(|g'|^2+e^{2y}|g|^2)}{\int|g|^2}>A^2>0\).
This excludes orders with nonzero real part, and excludes pure-imaginary orders with \(|\Im\nu|\le A\). No positivity of the *original RH operator* H was used: this positivity is that of an auxiliary one-dimensional confining Schrödinger operator whose spectrum is entirely explicit in terms of K.

The compact-resolvent assertion has a complete form proof: local \(H_0^1\) Rellich compactness and \(\int_Y^\infty|g|^2\le e^{-2Y}\mathfrak q[g]\) give compact embedding of the form domain into L². Eigenvalues are infinite and unbounded since the form domain is infinite-dimensional; Sturm uniqueness makes each eigenvalue simple. The decaying K solution spans the L²-at-infinity solution class.

The derivative-in-s simplicity needs a separate check, which the manuscript includes. For the real decaying eigenfunction \(g(y,\lambda)=K_{i\sqrt\lambda}(e^y)\), the differentiated Wronskian gives
\(-g'(\log A,\lambda_j)\,\partial_\lambda g(\log A,\lambda_j)=\int_{\log A}^\infty g^2dy>0\).
ODE uniqueness gives \(g'\ne0\), so \(\partial_\lambda K_{i\sqrt\lambda}(A)\ne0\). At \(\lambda_j>A^2\), both changes \(\lambda=-\nu^2\) and \(\nu=(s-1/2)/2\) have nonzero derivative, establishing **simple zeros of the actual entire Mellin transform**.

## C. Centering and the exact ordinary-zeta interface

The probability mean is
\[
\int q_A d\nu=\int2\cosh(x/2)e^{-A\cosh2x}dx
=\int_{\mathbb R}\cosh(u/4)e^{-A\cosh u}du
=2K_{1/4}(A).
\]
Thus \(q_A^\circ=q_A-2K_{1/4}(A)\) has exactly zero \(\nu\)-mean, and the original constant ground mode is in the operator domain. Since \(\mathcal B_1(s)=\xi(1-s)=\xi(s)\), the centered transform is
\(K_{(s-1/2)/2}(A)-2K_{1/4}(A)\xi(s)\).
At every ordinary-zeta nontrivial zero, the second term **vanishes identically even for multiple zeros**. At any off-critical such zero, the first term is nowhere zero by the proved order-zero theorem. The claim that the centered source does not necessarily activate *Dirichlet-only* zeros of Dedekind zeta is retained. The uncentered source activates all of them.

This only proves noncancellation at the numerator of the fixed principal. The physical low estimate and signed cross-class term remain open, so no individual actual zeta zero is excluded here.

## D. Independent elementary lower-bound ledger

For A>=1, restrict K0 to \(0\le u\le A^{-1/2}\), and use \(\cosh u\le1+u^2\) there. This gives \(K_0(A)\ge e^{-A-1}/\sqrt A\). Since the cosh Taylor series satisfies \(|\cosh z-1|\le |z|^2e^{|z|}/2\), Young \(Ru\le Au^2/4+R^2/A\) and \(\cosh u\ge1+u^2/2\) give
\[
|K_\nu-K_0|
\le R^2\sqrt\pi\,A^{-3/2}e^{-A+R^2/A}.
\]
For A>=100(1+R²), the relative error is at most
\(e\sqrt\pi e^{1/100}/100< 3\cdot2\cdot(11/10)/100<1/10\).
Therefore the explicit factor 9/10 in the main theorem is strictly valid. For \(0\le\Re s\le1\), \(|\Im s|\le T\), the order satisfies \(|\nu_s|^2\le1/16+T^2/4\), and the displayed choice A>=100(1+T²) suffices. There is no nonuniform limit in T concealed in this finite-window result.

## E. Numerical check, only for formula orientation

With mpmath at 45 decimal digits, A=8, s=0.7+10i, we separately computed the finite real-x integral over [-4,4] and the library Bessel value:
\[
K_{0.1+5i}(8)\approx
0.0000321213991581895997691805085665
+0.00000200690182504690584444625825841\,i.
\]
The difference printed as zero at 45-digit precision. For the mean, the separate source integral over [-4,4] and \(2K_{1/4}(8)\) both give approximately
\(0.000294024247104559861254582502643\), with printed difference \(1.17\times10^{-45}\). The omitted |x|>4 integrals are super-exponentially negligible for this diagnostic because \(A\cosh(8)>10^4\). This is a floating-point **normalization sanity check**, not a certificate for all complex roots or RH; those are covered by the analytic energy proof.

## F. Acceptance limits

- True full theta source and full original operator domain: verified analytically.
- K transform identity, critical-only simple zeros, strict \(|\Im s|>2A\): verified independently by the direct K integral and selfadjoint half-line equation.
- Mean-zero correction for ordinary zeta zeros: verified without an activation oracle.
- Quantitative finite-box lower bound: verified by elementary explicit constants.
- RH: **not proved**. Missing signed full-physical low estimate and arbitrary-vector global Weil positivity remain untouched.

Verdict: ACCEPTED as a genuine explicit source-selection lemma for the precise existing principal, with no claim to solve or bypass the remaining RH-bearing work.
