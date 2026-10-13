# Independent audit of the full-theta zero-selector theorem

Date: 2026-10-12. Audited: ZETA_ZERO_DUAL_PROBES.md. The aim is to find a false implication from the genuinely known theta zero modes to RH; no outside or formal referee status is claimed.

## 1. Exact Hilbert normalization, reflection and Fourier sign

The original probability density is \(d\nu=2\Phi(x)\cosh(x/2)dx\). The original unitary physical constant is \(e_0=2m\cosh(x/2)\), not m. Therefore
\[
\langle m\cos(z\cdot),e_0\rangle=
\int_{\mathbb R} 2m(x)^2\cosh(x/2)\cos(zx)dx
=\int\Phi(x)\cos(zx)dx=\Xi(z).
\]
For the original theta mode \(w_t=f_t/m\) with
\(f_t=\Phi(x+t)+\Phi(x-t)-2\cosh(t/2)\Phi(x)\), both translated cosine integrals give \(\Xi(z)\cos(zt)\). The exact factor is **two**, and no false norm of m or 2h was inserted. The usual mathematically conjugate-linear-first convention would replace z by its conjugate in these displayed overlaps, leaving every zero-selector and orthogonality assertion unchanged. The manuscript explicitly adopts the linear-first convention for consistency.

The converse is not just a one-way construction: if the entire t interval is orthogonal and Xi(z) is nonzero, an identity of entire functions forces the second Taylor coefficient \(-z^2\) to equal +1/4, yielding the *only* exceptions z=±i/2. Both probes equal e0/2. Thus the scalar iff in Theorem 1 is complete.

## 2. Full operator domain and zero multiplicities

For compact sets of complex z and each derivative order j, \(x^j m^2(x)\cos(zx)\) and \(x^j m^2(x)\sin(zx)\) are Schwartz, using the COMPLETE theta series and its modular reflection. The original Gamma b(t) grows logarithmically, so b(D) maps each such source into L2; compact cutoffs converge in the associated graph norm. The original prime potential is an actually bounded operator, with every omitted prime power in its proven complete tail, so no new domain is assumed. The differentiation of the probes is legal in the graph domain. This validates the claims beyond just L2 membership.

If Xi has multiplicity r at z0, differentiating k<r times produces only Xi derivatives of order at most k; each vanishes. Picking zero representatives modulo ± is necessary: cos(zx)=cos(−zx) would otherwise be a repeated column. At nonzero representatives the confluent exponential-polynomial system is linearly independent, and the strictly positive multiplier m cannot destroy that. The theorem does NOT assert that the constructed probes are additional null eigenvectors of H or that they span the entire unknown complement.

Hardy's theorem of infinitely many real critical zeros gives infinitely many such directions unconditionally; one confirmed real zero already disproves density of the entire true-translation kernel in e0-perp. At an off-line hypothetical zero \(|\Im z|<1/2\) is a consequence of the classical critical strip, not an assumption of RH.

## 3. Explicit theta quadrature diagnostic, separated from proof

As an independent floating-point sanity check, use mpmath at 40 decimal digits; on the nonnegative x-axis evaluate the exact formula for Phi with n=1,...,9 and reflect it evenly. Compare the cosine integral \(2\int_0^\infty\Phi(x)\cos(zx)dx\) to the completed xi-function and, at t=1/4, compare
\[
\int_{\mathbb R} f_t(x)\cos(zx)dx
\quad\hbox{to}\quad 2(\cos(zt)-\cosh(t/2))\Xi(z).
\]
The independent run returned, for z=2.4, cosine integral 0.434902657950858119 and completed xi 0.434902657950858119, with numerical difference about \(1.3\cdot10^{-42}\). The two translated-mode pairings both give -0.158728217407656070, with difference below \(10^{-40}\).

Using the first real critical zero near 14.1347251417346937904572519836, the corresponding cosine integral and translated-mode pairing were below \(10^{-42}\) and the completed xi value was below \(10^{-42}\) at working precision. These are sanity checks with a finite theta and spatial quadrature cutoff, NOT interval enclosures and NOT a zero-verification certificate. The proof of Theorems 1--2 instead uses the exact source Fourier identity, and the dimension consequence uses the classical unconditional existence theorem.

## 4. The weak-escape exponent and complete-space density

The inherited squared norm is \(\|w_{a_*-\delta}\|^2\sim (3/128)\delta^{-5/2}\); its **norm**, not its squared norm, is \(\sqrt{3/128}\delta^{-5/4}\). Thus the probe overlap divided by the norm is \(O_z(\delta^{5/4})\), and multiplication by \(\delta^{-5/4}\) yields the manuscript's \(2\sqrt{128/3}\) coefficient. This precisely distinguishes weak escape from norm convergence.

The real-frequency probe family is total because \(m v\in L^1\) for any L2 v, by \(\|mv\|_1\le\|m\|_2\|v\|_2\). The Fourier transform of this even L1 source vanishes at every real frequency only if the source vanishes a.e.; since m is positive, v vanishes. Normalized vectors have norm one, so convergence on a total set implies full weak convergence. No finite-dimensional Gram matrix or unproved density of the zero modes is used.

## 5. Counterexample check against a tempting invalid RH closure

At a real zero gamma, the bounded nonzero function \(g(x)=\cos(\gamma x)\) satisfies \(\Phi*g=0\) identically, by the exact same theta transform. Therefore Fourier division by Xi is **not injective** on arbitrary bounded/exponentially bounded source functions; one cannot conclude a source is zero merely because all of its theta translates pair to zero. This is a rigorous obstruction, not a counterexample to RH.

The known theta modes are in ker H, while the zero-indexed probes lie in the orthogonal complement of their known span. The latter are NOT shown to be negative, zero, or positive spectral vectors. The essential sign condition on the complete original form is still unproved. Consequently the manuscript is accepted as an explicit structural theorem, not as an RH proof.

**Audit result: algebraic identities, domain passage, multiplicity argument, infinite-dimensional complement, escape coefficient and the false-injectivity counterexample check; NO NEW UNCONDITIONAL RH THEOREM PROVED.**
