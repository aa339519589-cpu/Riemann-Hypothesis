# Mathematical self-audit of the exact threshold-mode shorting theorem

Date: 2026-10-12. Target under audit: [REPORT.md](REPORT.md). This is an internal proof audit, **not** an independent referee review, execution of an interval program, or a formal proof-assistant check.

## 1. Actual unchanged operator and domain

The original full-even selfadjoint H is the closed realization of \(M_m b(D)M_m-V\). For fixed J,N the comparator \(A=K_\varepsilon-\varepsilon I\) is bounded selfadjoint, so the difference \(\mathfrak D=H-A\) is selfadjoint on **the exact original operator domain** \(\operatorname{Dom}H\), with its closed form domain unchanged. No assertion that \(b(D)mv\in L^2\) for every form-domain v is needed: the Gamma term is evaluated only as a positive quadratic form in the proof of \(\mathfrak D\ge0\).

The comparison defect expands *exactly* as the three pieces:
\[
\mathfrak D=M_m b_{\ge J}(D)M_m+(M_{p_N}-S_N)+(\delta_NI-S_{>N})
\]
in form sense. The original full-prime tail is not deleted: it is in the bounded last term, nonnegative by \(\delta_N\ge\|S_{>N}\|\). Each retained prime edge is its full nonnegative squared difference. The original theta function, including all modes, occurs in every multiplier and critical vector.

## 2. Nondegeneracy at one real prime shift

The \(n=2\) term is
\[
q_2[v]=\alpha_2\int m(x)m(x+\log2)|v(x+\log2)-v(x)|^2dx.
\]
The weight is strictly positive almost everywhere. Vanishing implies \(\log2\)-periodicity almost everywhere. No nonzero such function belongs to L²(R), proving \(\ker q_2=\{0\}\).

**Important quantifier:** this gives a positive minimum on each *fixed finite-dimensional sphere*, not a uniform full-Hilbert spectral lower bound. The report never replaces the former by the latter, nor assigns a numerical lower bound to the Gram eigenvalue.

## 3. Domain and arithmetic evaluation of the actual modes

For every r>=1 the cited original identity \((A_{\rm source}-S_{\rm source})\Phi=-h\) and its 2r derivative imply \((A_{\rm source}-S_{\rm source})(\Phi^{(2r)}-4^{-r}\Phi)=0\). Multiplication by the genuine theta weight gives \(H w_r=0\) on the original domain. The source \(\Phi^{(2r)}-4^{-r}\Phi\) has theta double-exponential decay, while \(w_r=(\Phi^{(2r)}-4^{-r}\Phi)/m\in L^2\); this is the already proved source-domain implementation, not an assertion based solely on formal differentiation.

Independence is established by distinct-degree polynomials multiplying the nonzero entire function Ξ in Fourier space. The original true ground \(e_0=U1\) is **not** included in \(W_k\) for the main correction: only the r>=1 H-zero modes are repaired. The ground is used separately for the negative-index transfer.

For the explicit derivative recurrence, independently differentiate \(e^{x/2}P(u)e^{-u}\) with \(u=\pi n^2e^{2x}\):
\[
\partial_x=e^{x/2-u}\bigl((\tfrac12-2u)P+2uP'\bigr).
\]
This yields REPORT (11) verbatim. It is used only for x>=0, with the full sum reflected by theta parity for x<0. No false single-mode parity appears.

## 4. The finite-rank algebra is exact

Let W be the actual column map, \(G=W^*\mathfrak DW\), \(B=\mathfrak DW\).

- \(G\succ0\): for nonzero a, \(Wa\ne0\), and \(a^*Ga=\mathfrak d[Wa]\ge q_2[Wa]>0\).
- \(B\) exists as L² columns: \(w_i\in\operatorname{Dom}\mathfrak D\). \(B\) has rank k: \(Ba=0\) would imply \(a^*Ga=0\).
- \(B=-AW\) and \(G=-W^*AW\) because \(HW=0\). Every entry involves known finite comparison expressions only.
- \(F=BG^{-1}B^*\) is bounded, selfadjoint, PSD, rank k.
- For every form-domain v, the *exact* energy Cauchy inequality gives
\[
\langle v,Fv\rangle
=\sup_{0\ne w\in W(\mathbb C^k)}
|\mathfrak d(v,w)|^2/\mathfrak d(w,w)
\le\mathfrak d(v,v).
\]
Thus \(F\le\mathfrak D\) **on the infinite-dimensional original domain**, not merely on a finite trial space.
- \(B^*W=G\) implies \(FW=B=\mathfrak DW\). Hence \((\mathfrak D-F)W=0\), including mixed cross terms, and \((K_\varepsilon+F)W=\varepsilon W\).
- \(K_\varepsilon+F\) is bounded selfadjoint; an invariant finite-dimensional subspace is reducing. There is no assumption of completeness of the selected critical vectors.
- Nested finite-dimensional W give monotonic F by their supremum characterization. A correction exact on W has range containing \(\mathfrak DW\), hence rank at least k.
- Completing the square in k coordinates gives the infimum identity for \(\mathfrak D-F\) with an actual attained minimizer, as G is invertible.

The statements do not claim that the shorted residual vanishes on the entire, infinitely generated kernel of H.

## 5. Signed Birman–Schwinger and squared-trace direction

The extra hypothesis \(d_\varepsilon(x)\ge d_0>0\) is explicitly required **only** for the multiplicative congruence. Under it, \(T=M_{m/\sqrt d}R_J*M_{m/\sqrt d}\ge0\) is trace class, and
\[
K_\varepsilon+F=M_{\sqrt d}[I-(T-YY^*)]M_{\sqrt d},
\quad Y=M_{d^{-1/2}}BG^{-1/2}.
\]
All cross terms in \(\mathrm{Tr}(T-YY^*)^2\) retain the negative sign:
\(\mathrm{Tr}(T^2)-2\mathrm{Tr}(Y^*TY)+\mathrm{Tr}[(Y^*Y)^2]\).
The signed \(\mathcal T=T-YY^*\) is **not** declared positive. Its compact selfadjoint spectrum still satisfies the elementary implication
\[
Q>0,\quad\mathrm{Tr}(\mathcal T^2)-Q^2<1
\Longrightarrow\#\{\lambda_j(\mathcal T)>1\}\le1,
\]
because two eigenvalues >1 would contribute at least \(Q^2+1\) to the squared trace. The full original ground is an actual negative vector of \(H+\varepsilon\) for 0<ε<1/2. Thus one-sided form comparison plus index at most one implies H+ε is nonnegative on the original ground orthogonal complement. **No actual trace inequality for any new ε has been evaluated.**

## 6. Rank obstruction quantifiers

For a perturbation of rank <=r the subspace \(V_{r+1}=\mathrm{span}(e_0,w_1,\ldots,w_{r+1})\) has dimension r+2. Its intersection with the perturbation's kernel has dimension >=2, even when the perturbation varies arbitrarily with ε and J,N. The inherited fixed-subspace \(q_2\) minimum supplies a strictly negative K quadratic form on that 2D intersection uniformly for all sufficiently small ε. This proves only the impossibility of a **fixed-rank patch of this specific diagonal-prime comparison**, not an obstruction to RH or to exact signed-shift schemes.

## 7. Final falsification checks and scope

There is no estimate converting an arbitrary finite k correction into half-gap positivity: the complement can still have negative directions. The report intentionally does not claim that \(k(\varepsilon)\) chosen by an unspecified rule controls those directions. It contains no new evaluated Gram, no interval run for the signed trace, no verified ε→0 sequence, and no deduction of a ζ zero-location theorem. The quantitative sufficient condition is displayed as an *unverified conditional certificate*, with exact arithmetic formulas that can later be tested.

**Audit acceptance:** rank-k restoration, form order, exact-mode invariance, monotonicity, optimal rank, and finite-depth signed inertia criterion follow from the stated true theta source identities and standard Hilbert-space form calculus. The current proof does **not** satisfy the final RH acceptance condition.
