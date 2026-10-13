# Independent audit: finite-depth negative spectrum

This review checks the infinite-dimensional spectral step used by the even and odd transfers. It does not replay numerical ledgers or certify the separate high-order regularity estimates.

## Complete-prime form estimate

Use the [original closed realization](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md), with \(H=B-V\), \(B\ge0\), \(H\ge-1/2\), and \(D(H)=D(B)\). Let
\[
 c_N=C_0+2\sum_{2\le n\le N}\alpha_n,\qquad
 V_N=M_m\left(C_0+2\sum_{2\le n\le N}\alpha_n\cos(d_nD)\right)M_m.
\]
The [complete prime norm tail](../20261012_adaptive_spectral_tail/REPORT.md) gives \(\|V-V_N\|\le\delta_N\to0\). Every prime power is either retained or paid in this operator-norm error. For every vector in the actual form domain,
\[
 \mathfrak h[v]\ge\int_{\mathbb R}(b(t)-c_N)|\widehat{mv}(t)|^2\frac{dt}{2\pi}
                  -\delta_N\|v\|^2.
\]
Since \(b\) is nonnegative, increasing in \(|t|\), and tends to infinity, choose finite \(T\) with \(b(T)\ge c_N\). With \(P_T=1_{[-T,T]}(D)\),
\[
 \mathfrak h[v]\ge-c_N\|P_TM_mv\|^2-\delta_N\|v\|^2.\tag{1}
\]
This is the inequality in [the negative-band coverage theorem, Part I §4](../20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md). The nonnegative high-frequency Gamma part was retained before discarding it in this lower bound.

## Compactness is in the weighted low-frequency map

The operator \(A_T=P_TM_m\) is Hilbert--Schmidt, because \(m\in L^2\) and the Fourier convention gives
\[
 \|A_T\|_{HS}^2=\frac{T}{\pi}\|m\|_2^2<\infty.\tag{2}
\]
Neither multiplication by \(m\) nor the physical potential \(V\) is thereby compact. Indeed, on an interval \(I\) of length less than \(\log2\), every shifted compression vanishes and
\[
 1_I V1_I=C_0,1_IM_{m^2}1_I.
\]
This is a nonzero multiplication operator on nonatomic \(L^2(I)\), hence is not compact. Formula (2), rather than compactness of \(V\), is the mechanism used here.

Fix \(0<\kappa\le1/2\), choose \(N\) with \(\delta_N\le\kappa/2\), and put
\[
 Q_\kappa=1_{[-1/2,-\kappa]}(H).
\]
Its range lies in \(D(H)\), since the spectral parameter is bounded on that interval. For \(v\in\operatorname{Ran}Q_\kappa\), the spectral theorem and (1) yield
\[
 c_N\|A_Tv\|^2\ge(\kappa-\delta_N)\|v\|^2
                         \ge\frac\kappa2\|v\|^2.\tag{3}
\]
A compact map cannot be bounded below on an infinite-dimensional closed subspace: the images of an orthonormal sequence would remain uniformly separated. Thus \(Q_\kappa\) has finite rank. Summing (3) over an orthonormal basis and using (2) also gives
\[
 \operatorname{rank}Q_\kappa
 \le\frac{c_N}{\kappa-\delta_N}\|A_T\|_{HS}^2
 \le\frac{2c_N}{\kappa}\frac{T}{\pi}\|m\|_2^2.\tag{4}
\]
This is an infinite-dimensional argument. No finite matrix sign has been substituted for the original form.

The negative spectral projection is the strong limit of these finite-depth projections as \(\kappa\downarrow0\). Its range is the closure of the increasing union of their ranges. Therefore negative spectrum is pure point with finite multiplicity away from zero and can accumulate only at zero. Also \((-H)_+\) is compact: its finite-rank truncation to \(Q_\kappa\) has norm error at most \(\kappa\). This does not make the total negative rank finite or zero.

## Parity, ground removal and actual eigenstates

Reflection reduces \(B\), \(V\), and \(H\); the [odd-domain report](../20261013_odd_operator_domains/REPORT.md) supplies the same closed realization and compact-smooth core on both parities. The estimates (1)--(4) therefore restrict to each parity without a change in constants.

The normalized ground \(e_0\) satisfies \(He_0=-e_0/2\). Its orthogonal complement is reducing. Adding \(\tfrac12|e_0\rangle\langle e_0|\) moves only that line to zero; every other negative spectral point is unchanged. Thus the compactness and finite-band claims also hold on the even ground-orthogonal space. A strictly negative Rayleigh quotient there gives a genuine negative eigenvalue, because a nonzero negative spectral projection must occur in one of the finite-depth bands.

The same conclusion applies to the odd physical \(H_o\). Consequently the [common-core negative-index transfer](../20261013_green_spectral_interfaces/REPORT.md) legitimately passes from a negative form subspace to actual odd eigenstates. It gives a count of negative directions, not a bounded similarity or an individual eigenvalue correspondence between the Green and physical operators.

For the pole-corrected odd operator \(\mathcal A_o=H_o-2|s\rangle\langle s|\), an analogous argument adjoins a scalar row:
\[
 \widetilde A_Tv=(\sqrt{c_N}A_Tv,\sqrt2\langle s,v\rangle),\qquad
 \mathfrak a_o[v]\ge-\|\widetilde A_Tv\|^2-\delta_N\|v\|^2.
\]
This map is compact since \(s\in L^2\). With the finite lower spectral bound of \(\mathcal A_o\), the same proof gives finite rank at each fixed negative depth. The published inertia transfer instead uses its exact rank-one form splitting; it does not silently treat an \(\mathcal A_o\) eigenvector as an \(H_o\) eigenvector.

## Scope

The finite-depth compactness and eigenstate-existence steps pass this review. All complete prime powers and actual form domains are retained. The later Sobolev bootstrap, quantitative spectral-counting refinements, and numerical interval certificates are separate claims, not certified here. None of these compactness statements establishes the critical sign or RH.
