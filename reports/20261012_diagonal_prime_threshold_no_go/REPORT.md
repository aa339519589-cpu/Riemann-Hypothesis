# Exact threshold-mode obstruction to prime-edge diagonal spectral certificates

Date: 2026-10-12. Object: the original, unchanged even theta/Gamma/all-prime jump operator. This is a direct analytic no-go theorem for a specific proposed route to the **sharp half-gap**, not a proof of RH or a new zero-free region.

**Result.** Every comparison of the kind used by the existing certified one-quarter and three-eighths gap arguments that replaces the **n=2 prime shift** by the row-sum/Cauchy diagonal majorant has arbitrarily large negative index as its spectral offset ε goes to zero. This remains true *uniformly when the number J of retained Gamma terms and the prime cutoff N are both allowed to depend on ε and diverge*. Merely increasing J, N and interval precision therefore cannot establish the critical one-half bound by this comparison. The original signed-prime Birman–Schwinger construction is explicitly NOT covered by this no-go theorem.

## 1. Exact original operator and the comparison

Let Φ be the original positive even theta kernel satisfying hat Φ(t)=Ξ(t)=ξ(1/2+it). Set h(x)=cosh(x/2), p=2Φh, m=sqrt(Φ/(2h)), and Uq=sqrt(p)q. On the full even L²(dx) space the actual closed-form selfadjoint operator is

\[
H=ULU^{-1}-\tfrac12I
=M_m b(D)M_m-C_0M_{m^2}-\sum_{n\ge2}\alpha_nM_m(\tau_{d_n}+\tau_{-d_n})M_m,
\tag{1}
\]
\[
a_j=j+\tfrac14,\quad
b(t)=\sum_{j\ge0}\frac{(t/2)^2}{a_j(a_j^2+(t/2)^2)},\quad
\alpha_n=\Lambda(n)/\sqrt n,\quad d_n=\log n.
\]
All primes, the true θ kernel and the full Gamma multiplier are retained in H. The implementation/domain definition is the original one in the fifth round and in the subsequent adaptive-spectral-tail report. In this note the Γ tail is always an *actual positive form*, not a model differential operator.

For arbitrary integers J>=1 and N>=2 put
\[
c_J=\sum_{0\le j<J}\frac1{a_j},\qquad
R_J(x)=\sum_{0\le j<J}e^{-2a_j|x|},
\]
\[
S_N=\sum_{2\le n\le N}\alpha_nM_m(\tau_{d_n}+\tau_{-d_n})M_m,\qquad
p_N(x)=m(x)\sum_{2\le n\le N}\alpha_n
[m(x+d_n)+m(x-d_n)].
\]
Write \(S_{>N}\) for the actual bounded omitted-prime operator and choose *any* valid \(\delta_N\ge\|S_{>N}\|_{2\to2}\). Define the exact lower comparator used by this family of certificates:
\[
K_{J,N,\varepsilon}=M_{D_{J,N,\varepsilon}}-M_m(R_J*)M_m,
\qquad
D_{J,N,\varepsilon}
=\varepsilon-\delta_N+(c_J-C_0)m^2-p_N .
\tag{2}
\]
Here \(R_J*\) means convolution. The comparison is a bounded selfadjoint operator on full even L². In contrast, H has its original closed form domain.

## 2. Exact nonnegative defect, including one fixed prime

The positive digamma expansion gives
\[
b(t)=c_J-\widehat {R_J}(t)+b_{\ge J}(t),\qquad
b_{\ge J}(t)=\sum_{j\ge J}
\frac{(t/2)^2}{a_j(a_j^2+(t/2)^2)}\ge0 .
\]
The symmetric prime shifts give the exact identity
\[
\langle v,(p_N-S_N)v\rangle
=\sum_{2\le n\le N}\alpha_n\int_{\mathbb R}
m(x)m(x+d_n)|v(x+d_n)-v(x)|^2dx .
\]
Consequently on the *full original form domain*
\[
\boxed{\begin{aligned}
\langle v,(H+\varepsilon-K_{J,N,\varepsilon})v\rangle
={}&\int b_{\ge J}(t)|\widehat{mv}(t)|^2\,\frac{dt}{2\pi}\\
&+\sum_{2\le n\le N}\alpha_n\int
m(x)m(x+d_n)|v(x+d_n)-v(x)|^2dx\\
&+\langle v,(\delta_NI-S_{>N})v\rangle .
\end{aligned}}\tag{3}
\]
Every term is nonnegative: omitted Gamma summands are positive; each edge produces an exact squared difference; and \(\delta_N\ge\|S_{>N}\|\).

Crucially, for **every** J>=1, N>=2, ε>0, the defect dominates the very same quadratic form
\[
\boxed{\mathcal Q_2(v)
=\frac{\log2}{\sqrt2}\int_{\mathbb R}
m(x)m(x+\log2)|v(x+\log2)-v(x)|^2dx.}\tag{4}
\]
This comparison is independent of J, N, the size of the omitted-prime envelope and ε.

**Lemma.** \(\mathcal Q_2\) is a bounded positive-definite quadratic form on even L²(dx), with *trivial kernel*. In particular it is strictly positive for every nonzero v, but it need not admit a strictly positive uniform lower bound on the infinite-dimensional unit sphere.

**Proof.** Positivity and boundedness follow from \(m>0\), boundedness of m and Cauchy–Schwarz. If \(\mathcal Q_2(v)=0\), the strictly positive weight forces \(v(x+\log2)=v(x)\) almost everywhere. A nonzero \(\log2\)-periodic function cannot be in L²(R), since its positive L² mass on one fundamental period repeats infinitely often. Thus v=0. □

## 3. Infinitely many *actual* zero modes of H

The original full theta source identity, with the entire prime series, is
\[
(A-S)\Phi=-h,\qquad
(A-S)\Phi^{(2r)}=-4^{-r}h,\quad r=1,2,\ldots .
\tag{5}
\]
Both A and the genuine S commute with differentiation in the permissible source class; the closed realization in (1) is \(H=M_m(A-S)M_m\). These exact identities are inherited from round 5 and the original theta explicit formula. This step does not use RH, any zero-free strip or the unreviewed essential-spectrum assertion.

For \(r\ge1\), put
\[
q_r=\Phi^{(2r)}/\Phi-4^{-r},\qquad
v_r=Uq_r,\qquad v_0=U1=\sqrt p .
\tag{6}
\]
All v_r are even and lie in the original operator/form domain by the explicit rapidly decaying source and the inherited closed-domain check. Their sources and exact eigenvalues satisfy
\[
mv_r=\Phi^{(2r)}-4^{-r}\Phi,\qquad
Hv_r=0,\qquad Hv_0=-\tfrac12 v_0.                    \tag{7}
\]
Integration by parts with \(h^{(2r)}=4^{-r}h\) and \(\int2\Phi h=1\) proves \(\langle v_0,v_r\rangle=0\).

Their source Fourier transforms are
\[
\widehat{mv_r}(t)=[(-1)^rt^{2r}-4^{-r}]\Xi(t),\qquad
\widehat{mv_0}(t)=\Xi(t).                             \tag{8}
\]
The polynomials in (8) have different degrees and Ξ is a nonzero entire function, hence \(v_0,v_1,\ldots,v_k\) are linearly independent for all k. Define
\[
W_k=\mathrm{span}\{v_0,v_1,\ldots,v_k\},\qquad\dim W_k=k+1.
\]
By selfadjointness, orthogonality and (7),
\[
\langle w,Hw\rangle\le0\quad\text{for all }w\in W_k.  \tag{9}
\]
Note that the r>=1 modes lie exactly *at the critical spectral threshold*, not in a putative negative eigenspace.

## 4. Uniform no-go theorem, even with J,N tending to infinity

**Theorem.** For every integer \(k\ge1\), there exists \(\eta_k>0\), depending only on the original theta multiplier and the fixed true-mode space \(W_k\), such that **simultaneously for all** \(J\ge1\), \(N\ge2\), every valid \(\delta_N\), and \(0<\varepsilon<\eta_k\),
\[
\boxed{\operatorname{ind}_-(K_{J,N,\varepsilon})\ge k+1.}\tag{10}
\]
In fact K is strictly negative definite on \(W_k\). Thus a sequence of these row-sum/Cauchy prime-majorant comparisons, however the cutoffs depend on ε, cannot certify “at most one negative direction” for all sufficiently small ε.

**Proof.** By the lemma, \(\mathcal Q_2\) is continuous and strictly positive on the unit sphere of the finite-dimensional \(W_k\). The sphere is compact, so
\[
\eta_k=\min_{\substack{w\in W_k\\\|w\|_2=1}}\mathcal Q_2(w)>0.  \tag{11}
\]
Importantly, this number has no J or N dependence. From (3), (4) and (9), for all w in \(W_k\),
\[
\begin{aligned}
\langle w,K_{J,N,\varepsilon}w\rangle
&=\langle w,Hw\rangle+\varepsilon\|w\|_2^2
-\langle w,(H+\varepsilon-K_{J,N,\varepsilon})w\rangle\\
&\le(\varepsilon-\eta_k)\|w\|_2^2 .
\end{aligned}
\]
For \(0<\varepsilon<\eta_k\), the right side is strictly negative whenever w is nonzero. Hence \(W_k\) is a \((k+1)\)-dimensional negative subspace. □

The \(k=1\) case alone proves that all such comparisons have at least **two** negative directions at sufficiently small ε, *uniformly* over J,N. Taking larger k proves arbitrarily high negative index as ε goes to zero. No numerical estimate for \(\eta_k\) is required for the universal ε→0 obstruction.

**Birman–Schwinger corollary.** If some comparator additionally satisfies \(D_{J,N,\varepsilon}\ge dI>0\), the congruence
\[
K=M_{\sqrt D}(I-T)M_{\sqrt D},\quad
T=M_{m/\sqrt D}(R_J*)M_{m/\sqrt D}
\]
is valid with a positive compact T. For \(0<\varepsilon<\eta_k\), T must have at least k+1 eigenvalues **strictly above one** (multiplicity counted). In particular the rank-one trace-minus-Rayleigh or squared-trace sufficient condition cannot hold there. If D loses its positive lower bound first, this congruence certificate ceases to apply earlier; that also cannot complete the critical proof.

This does **not** contradict the already checked ε=1/4 and ε=1/8 certificates: nothing here asserts that those fixed ε values are below the unknown \(\eta_1\).

## 5. A second, weaker independent obstruction: fixed Gamma truncation

Even if all prime shifts were kept *exactly*, a permanently fixed finite J discards
\[
\int b_{\ge J}(t)|\widehat{mv}(t)|^2\,dt/(2\pi).
\]
On \(W_k\), (8) makes this a positive-definite Gram form
\[
\int b_{\ge J}(t)\left|
\Xi(t)\left(c_0+\sum_{r=1}^kc_r[(-1)^rt^{2r}-4^{-r}]\right)\right|^2\frac{dt}{2\pi}. \tag{12}
\]
It is positive for every nonzero coefficient vector: \(b_{\ge J}(t)>0\) for \(t\ne0\), Ξ is nonzero almost everywhere and a nonzero polynomial vanishes only at finitely many t. Thus a *fixed* J truncation also introduces arbitrarily many spurious negative directions near ε=0. This Gram minimum can shrink with J, so unlike (10), this weaker statement does **not** exclude adaptive J(ε) if the true signed-prime structure is retained.

## 6. What this establishes and what it does not

The final target remains the **unconditional RH theorem**, equivalently the original mean-zero sharp positivity H>=0. The theorem here does not imply that H has any negative spectrum; every negative direction proved is solely in the *lower comparator*, produced by dropping a positive form from a true infinite-dimensional zero space.

The original epsilon-dependent signed Birman–Schwinger construction in the current adaptive-spectral-tail reports retains the shift cross terms in \(C_N(D)\). It does **not** use the diagonal majorant \(p_N-S_N\) and is therefore **not contradicted** by (10). On any future path toward an exact half-gap, one must preserve threshold cancellations: either retain the actual shifts (already one viable design), or prove an alternative defect which vanishes on the entire true threshold nullspace rather than charging every critical mode a strictly positive error. That is a necessary structural design condition, not a sufficient RH proof.

**Acceptance:** exact auxiliary no-go theorem against a specified family of full-operator lower comparisons; **NO NEW UNCONDITIONAL RH THEOREM PROVED**.

## Evidence/provenance

- Exact theta source and threshold modes: rounds/05/REPORT-pages-01-05.txt and rounds/05/REPORT-pages-06-10.txt, section 4.
- The actual six-Gamma-term and n<=6 diagonal-majorant certificates under review: reports/20261012_adaptive_spectral_tail/CERTIFIED_GAP.md, Parts A and B.
- The distinct sign-preserving comparator not excluded: reports/20261012_adaptive_spectral_tail/POLYNOMIAL_ACCURACY_TAIL.md.
- All deductions above are analytic identities and finite-dimensional compactness arguments; no numerical, interval, formal proof-assistant or external-referee verification is claimed.
