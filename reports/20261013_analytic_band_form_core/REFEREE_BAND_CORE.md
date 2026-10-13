# Internal proof audit: narrow-band form core and rank obstruction

Date: 2026-10-13. Reviewed ANALYTIC_BAND_FORM_CORE.md against the original maximal even theta/Gamma/full-prime realization, ZETA_ZERO_DUAL_PROBES.md, and HIGH_ZERO_PROBE_TWO_PLANE.md. This is an internal mathematical reconstruction, not a third-party referee or a formal proof certificate.

**Status: the auxiliary statements below are supported by their full analytic derivations; NO NEW UNCONDITIONAL RH THEOREM PROVED.**

## 1. Actual form norm and interval density

The correct form Hilbert space has norm squared
\[
\|v\|_{\mathcal Q}^2=\|v\|_2^2+\int b(t)|\widehat{mv}(t)|^2dt/(2\pi).
\]
The original foundation establishes its even compact-smooth core; the full signed-prime term is bounded and does not change its topology. For \(\psi_\gamma=m\cos(\gamma x)\), the source is \(m^2\cos(\gamma x)\), *not* \(m\cos(\gamma x)\). Translation of the Schwartz transform \(\widehat{m^2}\) and logarithmic growth of b give \(\|\psi_\gamma\|_{\mathcal Q}=O(\sqrt{1+\log(2+|\gamma|)})\). Thus Fourier cosine inversion for \(v=m f,\ f=v/m\in C_c^\infty\), converges as an actual Bochner integral in the form norm, and proves that all real probes have form-dense span.

For any open interval I, let a continuous complex-linear form functional annihilate its probes. Because \(z\mapsto m\cos(zx)\) is entire **in the form norm**, the functional's values are an entire function vanishing on I; the identity theorem forces annihilation of all real probes and hence the whole compact-smooth form core. Hahn–Banach proves the interval core without an illicit inference from L2 density. Continuity gives the rational-frequency version. The projection \(P_0=I-|e_0\rangle\langle e_0|\) is form-continuous since \(e_0\in\operatorname{Dom}H\), giving the complete mean-zero projected core.

This does **not** assert that the discrete real zero set of Xi is a core.

## 2. Explicit finite cosine superoscillation

For fixed \(\Gamma>\ell>0\), \(A=(z_0-\Gamma)/\ell\), the exact binomial identity is
\[
\left(\cos t+iA\sin t\right)^N
=\sum_{k=0}^N\binom Nk
\left(\frac{1+A}2\right)^k
\left(\frac{1-A}2\right)^{N-k}e^{i(2k-N)t}.
\]
Therefore the manuscript's finite sum of **real-frequency** cosine probes is exactly
\[
\frac{v_N(x)}{m(x)}=\tfrac12\big[
e^{i\Gamma x}F_N(x)+e^{-i\Gamma x}F_N(-x)\big],
\]
where \(F_N(x)=[\cos(\ell x/N)+iA\sin(\ell x/N)]^N\). At every fixed real x, \(F_N\to e^{i(z_0-\Gamma)x}\) together with its first derivative. The key domination, uniform in N on the entire real line, is
\[
|F_N(x)|\le e^{|A|\ell|x|},\qquad
|F_N'(x)|\le\ell(1+|A|)e^{|A|\ell|x|}.
\]
At **fixed** \(\Gamma,\ell,z_0\), the true double-exponential m and m² tails absorb these factors. Dominated convergence gives both L2 physical convergence and H1 source convergence. Since \(b(t)\le C(1+t^2)\), the entire untruncated Gamma form converges; boundedness of the full signed prime potential supplies its form convergence.

For \(z_0=i/2\), the limit is \(m\cosh(x/2)=e_0/2\); because \(\|e_0\|=1\) and \(He_0=-e_0/2\), the exact limiting quadratic value is **-1/8**. Real parts of the finite coefficient arrays also converge to the real negative ground vector in the form norm. The result constructs negative **unprojected** high-frequency finite combinations, not negative mean-zero ones. It proves no zero exclusion.

## 3. Uniform fixed-dimensional complex cluster theorem

For any collection of offsets \(|u_j|\le L\) and total derivative multiplicity \(d=\sum r_j\le r\), the exact exponential decomposition is
\[
v(x)=\tfrac12m(x)\{e^{i\Gamma x}g(x)+e^{-i\Gamma x}g(-x)\},
\quad g(x)=\sum_{j,k}a_{jk}(ix)^ke^{iu_jx}.
\]
The second envelope is \(g(-x)\), **not** its complex conjugate. The polynomial-exponential g solves the constant-coefficient differential equation
\(\prod_j(D_x-iu_j)^{r_j}g=0\).
Its companion matrix has uniformly bounded coefficients for fixed r,L. Every companion matrix's finite observation Gram on [-1,1] is positive definite: a solution vanishing on an interval has every initial derivative zero. Compactness of the family, including all node collisions, gives a uniform lower Gram eigenvalue. This yields
\[
|g^{(k)}(x)|\le C_{r,L,k}e^{C_{r,L}|x|}\|mg\|_2.
\]
Since m decreases doubly exponentially, a fixed R captures at least half the weighted \(m^2\)-mass of every such g. On [-R,R], m has a positive minimum; hence
\(\int m^4|g|^2\ge\kappa_{r,L}\int m^2|g|^2\)
with \(\kappa_{r,L}>0\), even at exact collisions.

Uniform Schwartz control makes the \(\pm2\Gamma\) cross integrals \(O_{r,L,N}(\Gamma^{-N})\|mg\|^2\), retaining all complex coefficients. Plancherel and the complete high-carrier asymptotic of b show
\[
\langle mv,b(D)mv\rangle
=\log\Gamma\,\|mv\|^2+O_{r,L}(\|mg\|^2).
\]
The complete signed-prime potential is bounded, contributing another \(O(\|mg\|^2)\). Thus for sufficiently high \(\Gamma\), the **entire** fixed-dimension cluster has positive H-form with lower bound \(c_{r,L}\log\Gamma\|v\|^2\), uniformly over all offset collisions. No number-of-cluster-points growth with \(\Gamma\) is covered.

## 4. Ground projection sign and precise rank quantifiers

For real s,t, the unprojected source pairing is
\(\langle m^2\cos(sx),(b(D)-C_0-S)m^2\cos(tx)\rangle\).
The exact ground identity gives a **positive** projection correction:
\[
H[P_0v]=H[v]+\tfrac12|\langle v,e_0\rangle|^2,\qquad
\langle\psi_s,e_0\rangle=\Xi(s).
\]
Thus the displayed \(\mathsf K(s,t)\) in the main paper is exactly the projected original H-form Gram. Every prime-power shift remains in its absolutely convergent weighted source pairing; S is **not** asserted bounded on arbitrary L2.

The archived round-05 Weil equivalence identifies RH with H nonnegative on the full mean-zero form domain. Theorem A proves this is equivalent to PSD of **all finite rational-frequency Gram matrices in any one open band**. This is a countably specified equivalent criterion, not a finite certificate.

For any band centered at Γ, Theorem B gives a negative unprojected finite combination. Theorem C implies that for every fixed r, all combinations using at most r nodes have positive H-form for sufficiently large Γ. Hence the minimal cardinality of a negative full-space band combination is finite at each Γ but diverges as Γ increases, **unconditionally**. If RH is false, form density similarly supplies negative **projected** finite combinations in every band, whose minimum cardinality must also diverge. If RH holds, no projected negative combination exists. These alternatives leave the RH sign burden unchanged.

**Accepted scope:** full-form band core, explicit form-convergent superoscillation, unconditional original-H high-band negative full-space witnesses, collision-uniform fixed-rank positivity, projected countable kernel criterion and rank-divergence obstruction. **NO NEW UNCONDITIONAL RH THEOREM PROVED.**
