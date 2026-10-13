# Adversarial mathematical audit: reflected-prime adjoint-domain zero selector

Date: 2026-10-13. Reviewed [ADJOINT_DOMAIN_ZERO_SELECTOR.md](ADJOINT_DOMAIN_ZERO_SELECTOR.md), the existing entire reflected-prime dual and the odd-operator-domain nonclosability report. This is an **internal** adversarial proof review, not an independent external referee, formal verification, or RH proof.

**Acceptance:** the new domain selector, exact multiplicity/dual-Jordan chain, and quantified unbounded cutoff follow from the specified earlier analytic lemmas and the fully reproduced calculations below. A correction was made during review: the exact theta-jet recurrence is \(\mathcal B_\psi r_j=r_{j+1}\), *without* an added \(\frac14r_j\). The final manuscript includes the corrected identity. This is an audit of an uncommitted draft; no previously existing file was altered.

## 1. All-prime and functional-domain test

The reflected energy is
\[
N[r]=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\int_0^{\log n}
\psi(x)\psi(\log n-x)|r(x)-r(\log n-x)|^2dx.
\]
The Hilbert space \(K_N\) is, by definition, the closure of the compact ratio-core gradient images, not an invented \(L^2(dx)\) quotient or a finite set of primes.

**Core injection.** If \(\nabla_Nr=0\) and r has compact support in \([0,R]\), choose \(n=2^j\) with \(j\log2>2R\). For each \(0<x<R\), the partner \(j\log2-x\) lies outside the support. Since this genuine edge has positive weight a.e., r vanishes. Thus the densely defined operator \(Z_0\nabla_Nr=\nabla_N((\psi r)''/\psi)\) is single-valued on its compact core. Smooth even r makes \(\psi r\) odd and its second derivative odd. The simple zero of psi divides it smoothly at zero; the operator preserves this core.

**Dual validity.** The earlier [ENTIRE_REFLECTED_PRIME_ZERO_DUAL.md](../20261013_complex_reflected_prime_zero_dual/ENTIRE_REFLECTED_PRIME_ZERO_DUAL.md) supplies an explicit two-prime-power finite-cost current for every \(q_z=\psi(\sin(zx)-z\Xi(z)x/A)\). Although that current uses only 2- and 3-power channels, the primal Hilbert energy norm is the **original complete N with every prime power**. No deletion or coefficient change is introduced. The current theorem supplies boundedness of \(\mathcal J_z\) and all z-derivatives as norm-entire Banach-dual functionals. The audit does not assume boundedness of the unrenormalized sine moment away from zeros.

## 2. Direct rank-one identity: coefficients and signs

Let \(g=\psi r_e\), \(X(r)=\int xg(x)dx\), \(U_z(r)=\int g(x)\sin(zx)dx\), \(c_z=z\Xi(z)/A\). Then
\[
\mathcal J_z(r)=U_z(r)-c_z X(r),\qquad
\mathcal J_z(\mathcal B_\psi r)=-z^2U_z(r),
\]
because \(x''=0\) and \(\sin(zx)''=-z^2\sin(zx)\). Therefore
\[
\mathcal J_z(\mathcal B_\psi r)+z^2\mathcal J_z(r)
=-z^2c_zX(r)=-z^3\Xi(z)X(r)/A.
\]
There are **two powers of z from differentiating sin twice** and **one from the zero-integral renormalization**, hence z³, not z or z². No \(2\pi\) Fourier normalization is present: all transforms are literal integrals. All integration by parts is on smooth compact full-line odd sources.

The zero normalization follows from \(\psi=-\Phi'\):
\(\int x\psi=\int\Phi=A\) and \(\int\psi\sin(zx)=z\int\Phi\cos(zx)=z\Xi(z)\). The integration is legitimate even for complex z because Phi decays double-exponentially.

## 3. The moment X is genuinely unbounded in the complete-prime energy

Take even compact \(\chi_R\equiv1\) on \([-R,R]\), supported in \([-R-1,R+1]\). On the true edge differences, \(\nabla_N\chi_R=\nabla_N(\chi_R-1)\). The earlier proved incident-weight inequality gives
\[
N[\chi_R]\le4\int_R^\infty\psi(x)L(x)dx,\qquad
L(x)\ll(1+x)e^{x/2}.
\]
The first theta mode gives \(\psi(x)\ll e^{13x/2}e^{-\pi e^{2x}}\) for large x. The product is \((1+x)e^{7x}e^{-\pi e^{2x}}\). Set x=R+y and use \(e^{2y}\ge1+2y\), obtaining
\[
\int_R^\infty(1+x)e^{7x}e^{-\pi e^{2x}}dx
\le e^{7R-\pi e^{2R}}
[(1+R)/(2\pi e^{2R}-7)+(2\pi e^{2R}-7)^{-2}].
\]
For R large this is \(O((1+R)e^{5R}e^{-\pi e^{2R}})\). All prime labels are paid by L.

Dominated convergence gives \(X(\chi_R)\to A\ne0\). Hence \(X\) has no bounded extension in \(K_N\), and the exact criterion for a linear combination \(L_z+\beta_z X\) with bounded \(L_z\) to be bounded is \(\beta_z=0\). There is no reliance on an unproved closed realization of the unweighted odd source operator.

The lower ratio in the manuscript is derived by taking the square root of the just-proved N upper bound, then using
\(\mathcal J_z(Z_0v(\chi_R))\to-z^3\Xi(z)\).
Its exponent is exactly \(\frac\pi2e^{2R}-\frac52R\) and its polynomial factor is \((1+R)^{-1/2}\).

## 4. Hilbert adjoint conjugation and no false selfadjointness

The scalar functional \(\mathcal J_z\) is linear and is represented as \(\mathcal J_z(u)=\langle h_z,u\rangle\) with the inner product **conjugate-linear in its first slot**. At a zero,
\[
\langle h_z,Z_0u\rangle=-z^2\langle h_z,u\rangle
=\langle-\overline z^{\,2}h_z,u\rangle,
\]
so the true Hilbert adjoint eigenvalue is **\(-\bar z^2\)**, not \(-z^2\). This complex conjugation is essential if an off-line zero is considered.

The prior [odd source domains report](../20261013_odd_operator_domains/REPORT.md) has already shown that \(Z_0\) is densely defined **but nonclosable**, using precisely the same cutoff with
\[
\mathcal B_\psi1=\frac14-r_0,\quad
Z_0\nabla_N\chi_R\to-\nabla_Nr_0\ne0.
\]
Accordingly \(\operatorname{Dom}Z_0^*\) is not dense, and none of its eigenvalues is constrained to be real by a selfadjoint spectral theorem. The new result is a legitimate adjoint-domain theorem with no RH conclusion.

## 5. Multiplicities, Jordan structure and first failure

Differentiate the scalar identity k times. The Leibniz rule supplies exactly
\[
z^2\mathcal J_z^{(k)}
+2kz\mathcal J_z^{(k-1)}
+k(k-1)\mathcal J_z^{(k-2)},
\]
and its unbounded part is exactly
\(-[z^3\Xi(z)]^{(k)}X/A\). Every \(\mathcal J_z^{(j)}\) is itself norm bounded by the earlier entire-current theorem. Therefore \(h_z^{[k]}\in\operatorname{Dom}Z_0^*\) precisely when the scalar derivative vanishes.

For a nonzero zero of order m, the first m derivatives of z³Xi of orders 0 through m-1 vanish and the order-m derivative is \(z_0^3\Xi^{(m)}(z_0)\ne0\). There is **no factorial missing**: for the local expansion \(\Xi(z)=a_m(z-z_0)^m+\cdots\), \(\Xi^{(m)}(z_0)=m!a_m\), exactly as written.

For k<m the subtraction \(c_zx\) and all its derivatives through k vanish at z0. Hence the density of \(\mathcal J_{z_0}^{(k)}\) is \(\psi(x)x^k\sin(z_0x+k\pi/2)\). For z0≠0, the exponents \(\pm iz_0\) are distinct; independence of exponential polynomials proves linear independence of the m functionals on compact ratios. The finite adjoint invariant span has subdiagonal coefficients \(-2k\bar z_0\) (all nonzero for k≥1), giving a single Jordan block, with the displayed \((m-1)!\) coefficient. At order m the cutoff gives an explicit nonzero limit of the adjoint test on norm-vanishing inputs, so the domain failure is genuine.

**Exact executable check.** Run check_selector_algebra.py, using SymPy 1.14.0, for zero multiplicities m=1,...,6. It verifies all Leibniz coefficients, each vanishing defect through m-1, the exact order-m unbounded coefficient, and the special endpoint Xi(i/2)=1/2 yielding \(i/16\). The output is selector_algebra_result.json. This program verifies **finite symbolic algebra only**; the analytic theta tail, two-prime current and adjoint domain are proved in text, not by floating-point numerical tests.

## 6. Independent normalization cross-check and the RH burden

The earlier exact theta source jet moment states \(\mathcal J_z(r_0)=z^3\Xi(z)\). Pair the independently proved graph limit \(Z_0v(\chi_R)\to-v(r_0)\) with the *bounded* dual functional: its limit is \(-z^3\Xi(z)\). This reproduces the integration-by-parts limit without using equation (10). It independently cross-checks the sign, z³ and the complete-source normalization.

The theta jets obey \(\mathcal B_\psi r_j=r_{j+1}\) exactly, because \(f_j''=f_{j+1}\). An earlier draft incorrectly included an extra \(r_j/4\); that error was caught and corrected **before** submission. The projected-core weak-eigenchain claim only uses annihilation of every jet by each zero-dual derivative and the exact core identity; it does not imply the projected relation is symmetric or single-valued. The latest [projected metric obstruction](../20261013_projected_metric_obstruction/REPORT.md) proves it cannot be contained in any symmetric operator.

**Result of internal adversarial audit:** the adjoint-domain/zero multiplicity theorem is mathematically supported by the reproduced arguments and previously checked entire-current input. It is not a proof of RH, a claim of originality in the literature, or an external referee endorsement. No new zero exclusion has been proved.
