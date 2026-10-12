# Independent audit of the fixed-parameter theta-shortened essential spectrum

Date: 2026-10-12. Subject: ESSENTIAL_SPECTRUM_COUNTABLE_SHORTING.md. Audit of a comparison-operator theorem, with no claim of an RH proof or external mathematical peer review.

## Sources and scope

The theta boundary-frame report gives an infinite-dimensional genuine zero-mode subspace W with orthogonal projection P satisfying \(M_mP\in S_1\). The countable-shortening report gives a bounded exact correction \(F_\infty=CE^{-1}C^*\), where \(C=D|_W=-A|_W\), \(E=PC|_W\ge\delta I/4\). Both are necessary assumptions. They are explicitly carried over, not rediscovered.

## Independent operator-ideal check

For fixed J,N, the multiplier g satisfies \(g/m\in L^\infty\). Therefore \(M_gP=M_{g/m}(M_mP)\) is trace class, as is \(TP=M_m(R_J*)M_mP\). T itself is Hilbert-Schmidt, since \(|R_J|\le J\) and \(m\in L^2\). No claim that nonzero multiplication \(M_g\) is compact is used.

On W, \(C=\delta i+L\) with \(L=(-M_g+T)i\) trace class. Thus \(E=\delta I+i^*L\), and the coercivity of E makes \(E^{-1}-\delta^{-1}I=-\delta^{-1}E^{-1}i^*L\) trace class. Expanding \(CE^{-1}C^*\) confirms \(F_\infty-\delta P\in S_1\). The exact equality \(C^*w=Ew\) for w in W proves \((A+F_\infty)P=0\), so the W and Q blocks separate without error.

## Independent compressed-spectrum check

On \(Q=I-P\), the operator is \(-\delta I_Q+QM_gQ+\text{compact}\). Its spectrum is contained in \([g_-,g_+]\) after adding delta back, by the multiplication quadratic-form bound.

For every lambda in the closed range of the continuous real even g, choose bounded symmetric open intervals where g differs from lambda by less than an arbitrarily small eta. On each such interval the space of even supported L2 functions is infinite-dimensional. A compactly supported even cutoff chi gives \(P\chi=(\chi P)^*\) trace class, because \(\chi P=M_{\chi/m}(M_mP)\). Thus one can choose a unit supported vector that is orthogonal to any prescribed finite-dimensional subspace and has arbitrarily small P projection. Choosing a diagonal sequence orthogonal to the first j members of a fixed Hilbert basis gives weak convergence to zero. Its Q-normalization yields a Weyl singular sequence for \(QM_gQ\) at lambda. Therefore the essential spectrum of the Q-compressed multiplier is exactly the closed range \([g_-,g_+]\), including zero.

The zero block on infinite W contributes 0 to the essential spectrum of \(A+F_\infty\). The Q block contributes \([-\delta+g_-,-\delta+g_+]\). Translation by epsilon proves the displayed union.

## Arithmetic strict edge and limits

The full theta first-mode ratio
\[
\frac{m(x-\log2)}{m(x)}
\sim\frac14\exp[(3\pi/8)e^{2x}]\to\infty
\]
and the retained positive n=2 coefficient force \(g(x)<0\) at some finite positive x; hence \(g_-<0\). Since g tends to zero at infinity, \(g_+\ge0\). Therefore all \(0<\varepsilon<\delta-g_-\) give negative essential spectrum for the repaired lower comparator.

The conclusion concerns fixed finite J,N. It does not address adaptive N(epsilon), the sign of the original H, or zeta zeros. A lower comparison having negative directions is not a counterexample to RH.

**Audit conclusion: exact comparator-spectrum theorem accepted with its stated inherited theta-source trace-class input. NO NEW UNCONDITIONAL RH THEOREM PROVED.**
