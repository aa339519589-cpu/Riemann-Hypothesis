# Correction to the complete absolute-line scale in the averaged high bound

2026-10-12. This corrects the quantitative scale calculation in the user-authored [AVERAGED_NONPRINCIPAL_HIGH.md, equations (16)–(18), at commit 1e8bb596](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1e8bb596a0dcb6a489ad5df47e872ae77ef3343b/reports/20261011_qrh_selection_bridge/AVERAGED_NONPRINCIPAL_HIGH.md). The original files and their authorship are preserved. The averaging mechanism and the separate principal contraction and conditional descent remain valid in their stated scope. The smaller printed sufficient auxiliary-power threshold is not established by the absolute-majorant argument; this note does not claim a counterexample to the stronger inequality itself.

## 1. The missing outside scale

The original full Mellin identity contains

\[
X^{1/2-z}Z^{x+z-1}Y^{w-1}.
\]

This is the exact common weight in the [pinned arithmetic source, line 3825](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L3825), also used at line 5645. On the original absolute line \((\Re x,\Re w,\Re z)=(3,3,2)\), its modulus scale is

\[
X^{-3/2}Z^4Y^2.
\]

With the user's equation (15), which bounds the complete normalized slot factor by \(Z^{2\ell+\epsilon}\), the full absolute majorant therefore has exponent

\[
\boxed{A_{\rm abs}=4-\frac32 l_x+2l_y+2\ell.}
\tag{1}
\]

Using the original definitions

\[
h=1-l_x+\ell,\qquad C(s)=s+\frac{l_x}{2}-1+\frac h6,
\]

the same exponent is

\[
A_{\rm abs}=C(3)+2l_y+\frac{11}{6}h.
\tag{2}
\]

The \(h\) in (2) already includes the slot contribution; no further \(2\ell\) is added. At \(l_x=17/48,l_y=23/48,\ell=1/6\), one obtains

\[
\boxed{A_{\rm abs}=457/96,}
\]

whereas the printed \(C(3)+2\ell\) is \(127/48\). The difference \(203/96\) accounts for the unpaid original \(w,z\) scale factors.

## 2. Corrected full bound and sufficient choice of the auxiliary power

In equations (16)–(17) and both unaveraged tails, replace the outside exponent \(C(3)+2\ell\) by \(A_{\rm abs}\). In the original notation the bound becomes

\[
\boxed{
\frac{|\mathbb E_J\mathscr R^{\star}_{\ne1}(Z)|}{|A_T(Z)|}
\ll_{\epsilon,N}Z^{A_{\rm abs}+\epsilon}
\left(R^{-1/20}+R^{-A_0(1-2\epsilon)}+R^{-A_2N}\right).
}
\tag{3}
\]

For \(R=Z^\lambda\), a sufficient replacement for equation (18) is

\[
\boxed{
\frac\lambda{20}>3-\sigma_0+2l_y+\frac{11}{6}h+m+2\epsilon.
}
\tag{4}
\]

Choose the row and height cutoffs so that the other two powers in (3) meet the same strict margin. Then the stated target

\[
|\mathbb E_J\mathscr R^{\star}_{\ne1}(Z)|/|A_T(Z)|
\ll Z^{C(\sigma_0)-m}
\]

still follows. In the original geometry (4) reads

\[
\lambda>20\left(\frac{523}{96}-\sigma_0+m+2\epsilon\right).
\]

All source profiles, masks, independent Mellin heights and the positive without-replacement auxiliary law remain unchanged. The qualitative ability to obtain a fixed desired high-side power by taking a sufficiently large fixed \(\lambda\) is preserved under the stated finite-order prime input. The existing coarser raw bound \(505/96\) in [RESTORED_AUXILIARY_COMPARISON.md, Part B](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a887d3fa25950f58310a65eab4ae9f53d7d95f24/reports/20261011_qrh_selection_bridge/RESTORED_AUXILIARY_COMPARISON.md) remains a safe alternative and is unaffected.

## 3. Scope

The user's principal-series contraction and safe-line descent retain their hypotheses. In particular the actual low estimate and the safe-line comparison error must both fit the target exponent; \(\sigma_{\rm safe}-m_0\le\sigma_{\rm target}\) is still required when that transfer is used. A matching whole-low estimate remains unproved, and the finite-order prime input has not been independently replaced by an unconditional bound here. No new zeta-zero exclusion follows from this correction.

The [independent source review](REFEREE_ERRATUM_AVERAGED_HIGH_SCALE.md) checks the original prefactor, the correction, and the unaffected conditional arguments. No original user file is changed by this supplement.
