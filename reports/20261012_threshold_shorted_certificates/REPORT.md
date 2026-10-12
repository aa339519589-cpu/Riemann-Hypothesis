# Exact threshold-preserving finite-rank repair of a full-theta prime/Gamma spectral comparator

Date: 2026-10-12. Baseline: main commit ba52377ff25bf2cae70db7cde6ada4ebefc16d40. Target remains the **unconditional Riemann hypothesis** (all nontrivial ζ zeros on Re(s)=1/2). This note proves an explicit, rank-optimal correction theorem for one prior *invalid-at-threshold comparison design*. It does not prove RH, establish a new zero-free region, or certify an additional positive-depth gap.

## 1. Why the comparison needs repair

The original even operator on L²(R,dx) is
\[
H=ULU^{-1}-\tfrac12I
=M_m b(D)M_m-C_0M_{m^2}
-\sum_{n\ge2}\alpha_n M_m(\tau_{\log n}+\tau_{-\log n})M_m,
\]
with all terms and the closed operator domain as in
`reports/20261012_adaptive_spectral_tail/REPORT.md`.
Here
\[
h(x)=\cosh(x/2),\quad p=2\Phi h,\quad Uq=\sqrt p\,q,\quad
m^2=\frac{\Phi}{2h},\quad
b(t)=\sum_{j\ge0}\frac{(t/2)^2}{(j+\frac14)((j+\frac14)^2+(t/2)^2)},\quad
\alpha_n=\Lambda(n)/\sqrt n.
\]
The theta kernel Φ is the genuine positive even Jacobi theta derivative and \(\widehat\Phi(z)=\Xi(z)=\xi(1/2+iz)\); no zero-location assumption is used.

For integers \(J\ge1,N\ge2\), let
\[
c_J=\sum_{j=0}^{J-1}(j+\tfrac14)^{-1},\quad
R_J(x)=\sum_{j=0}^{J-1}e^{-(2j+1/2)|x|},\quad
p_N(x)=m(x)\sum_{n=2}^N\alpha_n[m(x+\log n)+m(x-\log n)].
\]
Choose any valid \(\delta_N\ge\|S_{>N}\|\), where \(S_{>N}\) is the actual weighted omitted-prime operator. The true finite-Gamma/diagonal-prime comparator is
\[
K_\varepsilon=M_{d_\varepsilon}-M_m(R_J*)M_m,\qquad
d_\varepsilon(x)=\varepsilon-\delta_N+(c_J-C_0)m(x)^2-p_N(x).
\tag{1}
\]
The multiplier \(d_\varepsilon\) is not assumed positive except in the later Birman–Schwinger corollary. Define the **bounded** comparison offset
\[
A_{J,N}:=K_\varepsilon-\varepsilon I,\qquad
\mathfrak D_{J,N}:=H-A_{J,N}=H+\varepsilon I-K_\varepsilon.
\tag{2}
\]
The first is independent of ε. The latter is selfadjoint on the original domain of H; its nonnegative closed form is exactly
\[
\begin{aligned}
\mathfrak d[v]:=\langle v,\mathfrak D v\rangle
={}&\int b_{\ge J}(t)|\widehat{mv}(t)|^2\,\frac{dt}{2\pi}\\
&+\sum_{2\le n\le N}\alpha_n\int_{\mathbb R}
m(x)m(x+\log n)|v(x+\log n)-v(x)|^2\,dx\\
&+\langle v,(\delta_N I-S_{>N})v\rangle\ge0 .
\end{aligned}\tag{3}
\]
This identity is reproduced and proved in
`reports/20261012_diagonal_prime_threshold_no_go/REPORT.md`. In particular
\[
\mathfrak d[v]\ge q_2[v]:=\frac{\log2}{\sqrt2}\int_{\mathbb R}
m(x)m(x+\log2)|v(x+\log2)-v(x)|^2\,dx .
\tag{4}
\]
Because \(m>0\), \(q_2[v]=0\) in L²(R) implies periodicity by log 2, hence v=0. Thus \(q_2\), and therefore \(\mathfrak d\), is strictly positive on every finite-dimensional nonzero subspace (but no global lower constant is claimed).

A direct consequence of (3) is that the uncorrected \(K_\varepsilon\) spuriously penalizes infinitely many known genuine threshold modes of H, uniformly in J,N. This is the previously proved obstruction; the present note builds an **exact one-sided correction**, not a new statement of the obstruction.

## 2. Explicit true threshold vectors and an entirely finite Gram

For \(r\ge1\) define
\[
q_r(x)=\frac{\Phi^{(2r)}(x)}{\Phi(x)}-4^{-r},
\quad w_r=Uq_r,\quad f_r=mw_r=\Phi^{(2r)}-4^{-r}\Phi .
\tag{5}
\]
The full original theta explicit-formula identity yields
\[
Hw_r=0,\qquad w_r\in\operatorname{Dom}H .
\tag{6}
\]
This follows by differentiating \((A_{\rm source}-S_{\rm source})\Phi=-h\)
and using \(h^{(2r)}=4^{-r}h\), as checked in round 5, §4. It is unconditional and does not assume the critical modes exhaust the kernel.

The vectors are linearly independent. Indeed
\[
\widehat f_r(t)=[(-1)^rt^{2r}-4^{-r}]\Xi(t),
\tag{7}
\]
and Ξ is not identically zero, so a finite polynomial linear dependence is impossible. Let \(W_k:\mathbb C^k\to L^2_{\rm even}\) be the column map \(e_r\mapsto w_r\), \(1\le r\le k\).

Define the k by k matrix
\[
\boxed{\ G_k=W_k^*\mathfrak D W_k=-W_k^* A_{J,N}W_k.\ }\tag{8}
\]
The second identity uses (6) and is crucial: **no evaluation of the unbounded full Gamma operator or its resolvent is required to assemble \(G_k\)**. Positivity (4) and independence imply
\[
G_k\succ0,\qquad G_k^{-1}\text{ exists exactly}. \tag{9}
\]
Define the L² column map
\[
\boxed{\ B_k=\mathfrak D W_k=-A_{J,N}W_k.\ }\tag{10}
\]
Every column in (10) is explicitly calculable from the finite Gamma exponential convolution, finitely many known prime shifts, the selected valid tail scalar δ_N, and the *full* theta kernel with its derivatives. There is no unknown off-line-zero label, generalized inverse, or infinite uncomputed operator in either (8) or (10).

For practical exact theta derivative evaluation, on \(x\ge0\) write \(u_n=\pi n^2e^{2x}\) and recursively
\[
P_0(u)=4u^2-6u,\quad
P_{\ell+1}(u)=(\tfrac12-2u)P_\ell(u)+2uP_\ell'(u),\quad
\Phi^{(\ell)}(x)=e^{x/2}\sum_{n\ge1}P_\ell(u_n)e^{-u_n}.
\tag{11}
\]
Equation (11) follows from termwise differentiation of
\(\Phi_n(x)=e^{x/2}(4u_n^2-6u_n)e^{-u_n}\).
For negative x use the true parity \(\Phi^{(2r)}(-x)=\Phi^{(2r)}(x)\), *not* an incorrect evenness assumption on each theta mode. For every fixed ℓ, the n-series and its finite x-derivatives converge absolutely uniformly on compact x≥0 and have explicit Gaussian-in-n tails. Thus the Gram entries in (8) are concrete absolutely convergent integrals, eligible for directed-interval enclosure; no numerical result is asserted here.

## 3. Rank-optimal positive restoration (main theorem)

**Theorem 1 (critical-nullspace shorting).** For any \(J\ge1,N\ge2,k\ge1\), and every valid \(\delta_N\), the explicitly defined bounded finite-rank operator
\[
\boxed{\ F_k=B_kG_k^{-1}B_k^*\ }\tag{12}
\]
has the following properties, uniformly for every ε>0:

1. \(F_k\succeq0\), \(\operatorname{rank}F_k=k\), and, in the sense of the full closed form domain,
\[
\boxed{\quad0\preceq F_k\preceq\mathfrak D .\quad}\tag{13}
\]
2. The repaired comparison
\[
\boxed{\quad K_{\varepsilon,k}=K_\varepsilon+F_k
\preceq H+\varepsilon I\quad}\tag{14}
\]
is a valid one-sided bound for the **unchanged** full-theta, full-prime, full-Gamma operator. It is a bounded selfadjoint operator on full even L².
3. Every selected genuine threshold vector is an **exact reducing eigenmode**:
\[
\boxed{\quad K_{\varepsilon,k}w_r=\varepsilon w_r\quad
(1\le r\le k).\quad}\tag{15}
\]
Equivalently \((\mathfrak D-F_k)W_k=0\) and the positive residual defect has no mixed matrix elements between \(\operatorname{Ran}W_k\) and its orthogonal complement.
4. If \(W_k\subset W_{k+1}\) uses the same \(J,N,\delta_N\), then \(F_{k+1}\succeq F_k\). Thus \(K_{\varepsilon,k}\) increases monotonically, never crossing the true \(H+\varepsilon\) from below.
5. Suppose \(F'\) is **any** bounded correction with \(0\preceq F'\preceq\mathfrak D\), and its repaired comparison is exact on all selected modes in the sense
\((\mathfrak D-F')w=0\) for every \(w\in\operatorname{Ran}W_k\).
Then necessarily \(\operatorname{rank}F'\ge k\). The correction (12) attains this rank lower bound.

**Proof.** Since \(w_r\in\operatorname{Dom}\mathfrak D\), the vectors \(b_r=\mathfrak D w_r\) are actual L² vectors and the map \(B_k\) is bounded from finite-dimensional \(\mathbb C^k\). The exact Gram \(G_k=W_k^*\mathfrak D W_k\) is Hermitian positive definite by (4) and (7).

For any \(v\) in the closed form domain of \(\mathfrak D\), Cauchy–Schwarz for the nonnegative form \(\mathfrak d\) gives
\[
\begin{aligned}
\langle v,F_kv\rangle
&=\|G_k^{-1/2}B_k^*v\|^2\\
&=\sup_{0\ne w\in\operatorname{Ran}W_k}
\frac{|\mathfrak d(w,v)|^2}{\mathfrak d(w,w)}
\le\mathfrak d(v,v).
\end{aligned}\tag{16}
\]
This proves \(0\le F_k\le\mathfrak D\) as forms and (14).

Next \(B_k^*W_k=G_k\), hence
\[
F_kW_k=B_kG_k^{-1}B_k^*W_k=B_k=\mathfrak D W_k. \tag{17}
\]
Subtracting (17) from (2) proves (15). Because \(K_{\varepsilon,k}\) is bounded selfadjoint and \(\operatorname{Ran}W_k\) is an invariant finite-dimensional subspace, it is actually reducing; no unproved decomposition of the whole threshold eigenspace is involved.

If \(B_ka=0\), then \(a^*G_ka=\langle W_ka,B_ka\rangle=0\); (9) gives a=0, so rank \(B_k=k\) and rank \(F_k=k\).

For monotonicity, the RHS of (16) is the supremum of an energy quotient over the chosen subspace. Enlarging the subspace cannot reduce this supremum, proving \(F_{k+1}\ge F_k\).

Finally if \((\mathfrak D-F')W_k=0\) then \(F'W_k=\mathfrak DW_k=B_k\), whose image has dimension k; rank \(F'\ge k\). This proves optimality. □

The exact variational interpretation of the *remaining* defect is
\[
\boxed{\
\langle v,(\mathfrak D-F_k)v\rangle
=\inf_{w\in\operatorname{Ran}W_k}\mathfrak d(v-w,v-w).\ }\tag{18}
\]
It follows by minimizing the strictly convex quadratic in k coefficients; its Gram is \(G_k\). Equation (18) is an exact Schur complement / shorted quadratic form, not a spectral approximation.

### Explicit rank-one instance, requiring only Φ and Φ''

For \(k=1\), put \(w=\sqrt p(\Phi''/\Phi-1/4)\) and \(b=-A_{J,N}w\). The denominator
\[
g=-\langle w,A_{J,N}w\rangle
=\langle w,\mathfrak Dw\rangle\ge q_2[w]>0
\]
is rigorously positive without numerics. The corrected comparator is
\[
\boxed{K_{\varepsilon,1}=K_\varepsilon+\frac{|b\rangle\langle b|}{g},
\qquad K_{\varepsilon,1}w=\varepsilon w.}\tag{19}
\]
This completely eliminates the uncorrected comparison's artificial negative eigen-direction on the *first* true threshold mode, including all cross terms with it. It does not eliminate the other infinitely many threshold modes.

## 4. Exact signed compact Birman–Schwinger test after repair

Suppose, in addition to the theorem's hypotheses, that the explicitly known multiplier satisfies \(d_\varepsilon(x)\ge d_0>0\) for every x. Define on the original full even space
\[
T=M_{m/\sqrt {d_\varepsilon}}\,(R_J*)\,M_{m/\sqrt {d_\varepsilon}}\succeq0,\quad
Z=M_{d_\varepsilon^{-1/2}}B_k,\quad
Y=ZG_k^{-1/2}.
\]
T is positive trace class, since the finite sum of exponential kernels has an integrable nonnegative Fourier multiplier and \(m/\sqrt{d_\varepsilon}\in L^2\). The *exact repaired* comparison is
\[
\boxed{K_{\varepsilon,k}=
M_{\sqrt{d_\varepsilon}}\,(I-\mathcal T_k)\,M_{\sqrt{d_\varepsilon}},
\qquad \mathcal T_k=T-YY^*.}\tag{20}
\]
Unlike T, \(\mathcal T_k\) is signed, but remains compact selfadjoint and Hilbert–Schmidt. Its squared trace is an exact finite-rank update:
\[
\boxed{\operatorname{Tr}(\mathcal T_k^2)
=\operatorname{Tr}(T^2)
-2\operatorname{Tr}(Y^*TY)
+\operatorname{Tr}[(Y^*Y)^2].}\tag{21}
\]
All added terms involve at most k by k Gram matrices or the explicit original finite sum of exponential kernels. The old squared trace \(\operatorname{Tr}(T^2)\) has an exact positive double-integral representation in
`reports/20261012_adaptive_spectral_tail/CERTIFIED_GAP.md`, Part B.

**Corollary 2 (valid finite-depth certification rule).** Fix ε in (0,1/2), and any nonzero test \(\psi\in L^2_{\rm even}\) with
\[
Q=\frac{\langle\psi,\mathcal T_k\psi\rangle}{\|\psi\|^2}>0.
\]
If a *rigorous* interval or analytic bound were to establish
\[
\boxed{\operatorname{Tr}(\mathcal T_k^2)-Q^2<1,}\tag{22}
\]
then \(K_{\varepsilon,k}\) has at most one negative direction, and the **original** mean-zero quadratic form would satisfy
\[
\mathcal E(q)\ge(\tfrac12-\varepsilon)\|q\|_{L^2(\nu)}^2 .
\tag{23}
\]
This condition is currently NOT certified for any new ε.

**Proof.** If \(\mathcal T_k\) had two eigenvalues >1, its largest eigenvalue would be at least Q, so \(\operatorname{Tr}(\mathcal T_k^2)\ge Q^2+1\). This contradicts (22). Congruence (20) then gives negative index at most one. The genuine normalized ground state \(e_0=\sqrt p\) obeys \(He_0=-\tfrac12e_0\), so it already consumes one negative direction of \(H+\varepsilon\). Because \(K_{\varepsilon,k}\le H+\varepsilon\), the latter can have at most one negative direction. Orthogonality to \(e_0\) and selfadjointness imply (23). The argument needs no assumption that \(\mathcal T_k\) is positive. □

One explicit unconditional positive test Rayleigh quotient for (22) is obtained from
\(\psi=\sqrt{d_\varepsilon}\,e_0\):
\[
Q=1-\frac{\langle e_0,K_{\varepsilon,k}e_0\rangle}
                 {\int d_\varepsilon|e_0|^2}
\ge1+\frac{\frac12-\varepsilon}{\int d_\varepsilon|e_0|^2}>1,
\tag{24}
\]
because \(K_{\varepsilon,k}\le H+\varepsilon\). This does *not* imply (22); the trace difference still has to be proved with valid bounds.

## 5. An unavoidable moving-rank requirement

The previously established uniform obstruction says: for every \(s\ge1\), there exists \(\eta_s>0\) such that the *uncorrected* K is strictly negative on the actual \((s+1)\)-dimensional subspace
\[
V_s=\mathrm{span}\{e_0,w_1,\ldots,w_s\}
\]
whenever \(0<\varepsilon<\eta_s\), **uniformly over J,N and all valid δ_N**.

Here is a sharpened general consequence.

**Theorem 3.** Fix any integer \(r\ge0\). For arbitrary choices \(J(\varepsilon),N(\varepsilon),\delta_{N(\varepsilon)}\) and **any bounded selfadjoint perturbation \(P_\varepsilon\) with \(\operatorname{rank}P_\varepsilon\le r\)** (not even required to be positive or a valid lower correction), the operator
\[
K_\varepsilon+P_\varepsilon
\]
still has at least two negative directions for all \(0<\varepsilon<\eta_{r+1}\). Thus no uniformly bounded-rank correction can make this specific diagonal-prime comparison certify the sharp 1/2 gap along all ε↓0.

**Proof.** \(V_{r+1}\) has dimension r+2. Its intersection with \(\ker P_\varepsilon\) has dimension at least (r+2)-r=2. On this two-dimensional intersection the perturbation vanishes, while the original K is strictly negative by the existing theorem. □

The rank-k operator (12) is therefore not advertised as a final RH proof or as something that works with k fixed; it is an *explicit and rank-minimal repair of any chosen k exact threshold modes*, potentially with k increasing. The theorem above rules out a permanent fixed-dimensional patch and explains why threshold-preserving corrections, if used, must adapt to the true infinite critical space.

## 6. Limits and acceptance

- The corrected comparator uses exactly the same original theta and all primes/Gamma through the preserved one-sided error (3). No positive-form error is secretly discarded; (16) is its full-domain bound.
- This construction is genuinely different from the already existing *signed prime multiplier* adaptive resolvent method: it starts with the **diagonal majorant** but then restores its effect on a finite set of exact modes by an optimally shorted correction. Both are legitimate candidate mechanisms for further tests; neither has passed an ε→0 all-depth sign test.
- A finite rank k repairs exactly the specified modes; it neither exhausts the complete kernel nor proves positivity of the remaining complement.
- No claim of originality for abstract Schur-complement shorting is made. The contributions here are the exact original-RH-operator specialization, explicit finite-Gamma/theta formulas (8)–(11), rank optimality with a rigorous comparison, and the signed squared-trace certificate (20)–(22).
- **NO NEW UNCONDITIONAL RH THEOREM PROVED.** The final acceptance criterion, Re(ρ)=1/2 for every nontrivial ζ zero, is not met.

Provenance: source identity and genuine null modes from rounds/05/REPORT-pages-01-05.txt and rounds/05/REPORT-pages-06-10.txt; comparator and certified 1/4,3/8 finite-depth results from reports/20261012_adaptive_spectral_tail/CERTIFIED_GAP.md; uniform no-go from reports/20261012_diagonal_prime_threshold_no_go/REPORT.md. This is an analytic proof with an explicit domain-level audit; it has **not** been independently refereed, numerically certified for new depths, or checked by Lean.

## Countable selected-kernel correction

[COUNTABLE_CORRECTION.md](COUNTABLE_CORRECTION.md) sharpens the canonical full-prime tail allowance to obtain D>=delta_N/4. It constructs a bounded exact shorting over the specified infinite true-theta Riesz span, and gives a coupled finite-mode/prime-cutoff error <=16delta_N. The finite corrections converge strongly at fixed N; their norm error remains at least delta_N/4. Neither the countable correction nor this error bound establishes the remaining all-depth negative-index condition. The independent review is linked there.
