# Uniform marked sextic-row mean square

2026-10-11. This note concerns the exact completed row introduced in the user's [marked-row theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/reports/20261011_qrh_selection_bridge/MARKED_ROW_BOUND.md) (commit `e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8`). That pointwise theorem and its definitions are inherited input, not new results of this note. The new statements below use the actual sextic characters and their original zero extensions. They do not prove the short-row estimate required by the critical probe or a new zero-free region.

## 1. Exact objects and claims

Let O=Z[omega], q_a=|a|^2, and let S be the fixed excluded set from the source paper. Ideals have the original multiplicatively compatible primary generators. All ideals below avoid S unless explicitly enlarged in a positive majorant. The fixed s is any row parameter allowed by the original corrected row. For a squarefree good ideal D and U>0, write the exact row as

\[
 B_D(U;m,s)=\sum_{c\,\mathrm{sf},n} b(c,n;s)\chi_{cn^3}(m)
 1_{D\mid cn^3}q_c^{-1/2}q_n^{-1}
 W(q_cq_n^3/U),                                      \tag{1}
\]
\[
 W(y)=(2\sqrt\pi)^{-1}e^{-(\log y)^2/4}.
\]

Here b is exactly the m-independent product gamma_2(c), conjugate alpha(cn^3), eta(cn^3), Xi_*(cn^3)^{-1}, R(cn^3,s), and conjugate G(cn^3). Thus |b|<=1. None of these factors has been replaced in (1). At every good prime p, chi_p has exact order six on (O/p)^times and is zero at zero. All its powers retain that zero value, including powers divisible by six. The series (1) converges absolutely and uniformly in m, by the user's all-scale positive majorant.

For Q>=1 put
\[
 N(Q)=\#\{m\in\mathcal O:0<q_m\le Q\},\qquad
 \mathsf M_Q(F)=N(Q)^{-1}\sum_{0<q_m\le Q}F(m).
\]

**Theorem 1 (unrestricted expanding-row mean).** The limit
\[
 \mathsf M(|B_D|^2)=\lim_{Q\to\infty}\mathsf M_Q(|B_D(U;\cdot,s)|^2)
\]
exists, and
\[
 \boxed{\mathsf M(|B_D|^2)\le C/q_D.}                    \tag{2}
\]
The constant C is independent of U>0, D, s, and the number of prime divisors of D. Here U,D,s are fixed before Q tends to infinity.

**Theorem 2 (one quantitative finite-row range).** For every epsilon>0 there is C_epsilon such that, uniformly for U>=2, every squarefree good D, every allowed s, and
\[
 Q\ge\max\{1,U^{2+\epsilon}/q_D\},
\]
\[
 \boxed{\mathsf M_Q(|B_D(U;\cdot,s)|^2)\le C_\epsilon/q_D.} \tag{3}
\]
No passage between Q and U limits is used to obtain this statement.

Both theorems remain true when the sum (1) is restricted to q_cq_n^3<=H, for any H, with the same constant in (2). The proofs of the means use no cancellation in b, so the asserted constants are uniform in the actual s-dependent phase.

## 2. Exact sextic-core orthogonality

Every ideal n has a unique decomposition n=v k^2 with v squarefree. The ideals c and v may share primes. Then
\[
 cn^3=c v^3 k^6.
\]
The exponent of p in the sextic core c v^3 belongs to {0,1,3,4}. These four residues are distinct modulo six. Consequently two such cores define the same unit character at every prime if and only if their ordered pairs (c,v) agree.

For any c,v,c',v',k,k', let A=c v^3 k^6 and A'=c'v'^3 k'^6. The product chi_A(m) conjugate chi_A'(m) is periodic modulo the squarefree ideal rad(AA'). Complete residue averaging and the Chinese remainder theorem give
\[
 \mathsf M(\chi_A\overline{\chi_{A'}})=
 \begin{cases}
  \displaystyle\prod_{p\mid cvkk'}(1-q_p^{-1}),&(c,v)=(c',v'),\\
  0,&(c,v)\ne(c',v').
 \end{cases}                                           \tag{4}
\]
The same complete average is the limit over the expanding lattice disks: for a fixed ideal, every residue class has its area-density. This follows, for example, by tiling with a fundamental parallelogram and bounding the boundary tiles by O(sqrt(Q))+O(1).

The zero in the second line remains valid in the presence of every original zero mask: at a prime where the core exponents differ, the local average is the sum of a nonprincipal character over the unit group, divided by q_p. In the first line the masks are essential. In particular, if D divides both A and A', then
\[
 0\le\mathsf M(\chi_A\overline{\chi_{A'}})
 \le \phi(D)/q_D=\prod_{p\mid D}(1-q_p^{-1}).             \tag{5}
\]

The assertion would change if a sixth character power were assigned the value one on nonunits. No such alteration has been made.

## 3. An all-scale Gaussian square-sum majorant

Let all sums in this section range over nonzero integral ideals, with indicated squarefreeness retained or dropped in upper bounds. Define
\[
 F(t)=\sum_k q_k^{-2}W(q_k^6/t),
\]
\[
 \mathcal S(V)=\sum_{c\,\mathrm{sf},v\,\mathrm{sf}}
 q_c^{-1}q_v^{-2}F(V/(q_cq_v^3))^2.
\]
Then
\[
 \sup_{V>0}\mathcal S(V)<\infty.                       \tag{6}
\]

Indeed, ideal counting #\{a:q_a<=x\}<=C x gives
\[
 \sup_{T>0}\sum_{c\,\mathrm{sf}}q_c^{-1}W(q_c/T)^2<C_0.
                                                               \tag{7}
\]
On each dyadic interval [2^j,2^{j+1}) the unweighted reciprocal-norm sum is bounded, while the supremum of the Gaussian is bounded by C exp[-c(j-log_2 T)^2]. The sum over integer j is uniformly bounded under all real translations; extending j>=0 to all integers only enlarges it.

Apply Minkowski in the Hilbert space indexed by (c,v):
\[
 \begin{split}
 \mathcal S(V)^{1/2}
 &\le\sum_k q_k^{-2}
 \left[\sum_vq_v^{-2}\sum_cq_c^{-1}
 W\left(\frac{q_cq_v^3q_k^6}{V}\right)^2\right]^{1/2}\\
 &\le C_0^{1/2}\zeta_{\mathcal O}(2)^{3/2}.
 \end{split}
\]
All sums are positive, so finite truncation followed by monotone convergence justifies Minkowski. This proves (6), for small V as well as large V.

## 4. Marked partition and the zero-mask Euler compensation

By (4), only terms with the same c,v interact in the mean square. By (5) and |b|<=1,
\[
 \mathsf M(|B_D|^2)\le\frac{\phi(D)}{q_D}
 \sum_{c\,\mathrm{sf},v\,\mathrm{sf}}q_c^{-1}q_v^{-2}
 \left[\sum_{k:\,D\mid cvk}q_k^{-2}
 W(q_cq_v^3q_k^6/U)\right]^2.                           \tag{8}
\]
The condition D|cvk is equivalent to D|cv^3k^6 because D is squarefree.

For every fixed pair (c,v), partition D uniquely as D=EFH, where
- E consists of primes of D dividing c;
- F consists of the remaining primes of D dividing v;
- H consists of primes dividing neither c nor v.

These three squarefree factors are pairwise coprime. Write c=E c_0, v=F v_0 and k=H k_0. The original restrictions on c_0,v_0 may be dropped in a positive majorant. They remain squarefree; c_0 and v_0 may share primes. The contribution from this partition to the sum in (8) is at most
\[
 q_E^{-1}q_F^{-2}q_H^{-4}\,
 \mathcal S\left(\frac{U}{q_Eq_F^3q_H^6}\right).
\]
Using (6) and summing all three-way partitions,
\[
 \begin{split}
 \mathsf M(|B_D|^2)
 &\le C\frac{\phi(D)}{q_D}
 \prod_{p\mid D}(q_p^{-1}+q_p^{-2}+q_p^{-4})\\
 &=\frac C{q_D}\prod_{p\mid D}
 (1-q_p^{-1})(1+q_p^{-1}+q_p^{-3})\\
 &\le C/q_D.                                          \tag{9}
 \end{split}
\]
The final inequality holds factor by factor: for x=1/q_p in (0,1),
\[
 (1-x)(1+x+x^3)=1-x^2+x^3-x^4<1.
\]
Thus the original nonunit zero masks remove, rather than cause, the otherwise accumulating Euler loss. There is no factor depending on omega(D).

For an infinite row, first restrict q_A<=H. Formula (4) applies to the finite polynomial. Uniform absolute convergence of (1) implies uniform convergence of its square, so its disk means converge to the limit of these finite means. This proves existence and (2). Removing a cutoff only enlarges the positive majorants above, proving the same uniform bound for truncated rows.

## 5. Uniform Gaussian tail and a finite-disk estimate

Two elementary ingredients make the finite-row quantifier precise.

### 5.1 Tail

For H>=U>=1 let R_H be the part of (1) with q_A>H. The pointwise marked positive-majorant proof in the user's theorem works without change for the broader Gaussian exp[-(log y)^2/8]. Since
\[
 W(y)1_{y>H/U}\le C\exp[-\log^2(H/U)/8]
 \exp[-(\log y)^2/8],
\]
we have, uniformly in m,s,D,
\[
 \|R_H\|_\infty\le C\frac{\sqrt U}{q_D}
 \exp[-\log^2(H/U)/8].                                 \tag{10}
\]
For completeness, the inherited positive-majorant argument uses E={p|D:p|c}, F=D/E, c=E c_0, n=F n_0. For either Gaussian the unmarked sum is O(sqrt(V)) at all V>0 by a translated dyadic Gaussian sum. Each part then contributes O(sqrt(U)q_D^{-1}q_F^{-3/2}), whose sum is bounded by zeta_O(3/2). Thus (10) does not assume coprimality between c and n.

### 5.2 Periodic Gaussian averaging

Write a_0=sqrt(3)/2 for the covolume of O as a Euclidean lattice and set
\[
 \mathsf G_Q(P)=\frac{a_0}{Q}\sum_{m\in\mathcal O}
 e^{-\pi q_m/Q}P(m).
\]
If P is periodic modulo an ideal M and |P|<=1, then
\[
 |\mathsf G_Q(P)-\mathsf M(P)|\le C e^{-cQ/q_M}
 \quad\text{whenever }Q\ge q_M.                       \tag{11}
\]
Here M(P) is its complete residue average. To see this with uniform constants, expand P in the finite Fourier group M^*/O^*, using the standard Euclidean Fourier pairing. Each normalized Fourier coefficient has modulus at most one. Poisson summation gives
\[
 \mathsf G_Q(P)=\sum_{\nu\in M^*}
 \widehat P(\nu\bmod O^*)e^{-\pi Q|\nu|^2}.
\]
The zero dual vector is M(P). Every ideal lattice of O is a rotated and scaled copy of O, so the remaining dual Gaussian sum is at most C exp(-cQ/q_M) for Q/q_M>=1. This also accounts for nonzero dual vectors representing the principal finite character.

Apply (11) to each product chi_A conjugate chi_A' in the truncated row B_H. Its period is M=rad(AA'). Since D divides both rad(A) and rad(A'),
\[
 q_M\le q_Aq_{A'}/q_D\le H^2/q_D.                    \tag{12}
\]
The sum of the absolute row coefficients is at most C sqrt(U)/q_D, by the inherited theorem. Thus, if Qq_D>=H^2,
\[
 \mathsf G_Q(|B_H|^2)
 \le C/q_D+C\frac U{q_D^2}e^{-cQq_D/H^2}.              \tag{13}
\]
In (13), the mean-square term is bounded by the truncated version of Theorem 1. If the truncation is empty, (13) is immediate.

For Q>=1, G_Q(1) is uniformly bounded. Hence (10), (13), and |x+y|^2<=2|x|^2+2|y|^2 imply
\[
 \boxed{\mathsf M_Q(|B_D|^2)\le \frac C{q_D}
 +C\frac U{q_D^2}\left[
 e^{-cQq_D/H^2}+e^{-\log^2(H/U)/4}\right]}
                                                               \tag{14}
\]
whenever H>=U>=1, Q>=1, and Qq_D>=H^2. To pass from the Gaussian mean to the disk mean, use e^{-pi q_m/Q}>=e^{-pi} inside the disk and N(Q)>=c_0 Q. Excluding m=0 only decreases this nonnegative sum. No assertion about the value of B_D at m=0 is needed.

To prove Theorem 2, if q_D>=U the inherited pointwise bound already gives |B_D|^2<=C/q_D for every m. Otherwise choose H=U^{1+epsilon/4}. The assumed Q gives
\[
 Qq_D/H^2\ge U^{\epsilon/2}.
\]
After factoring q_D^{-1}, the two errors in (14) are bounded respectively by
\[
 Ue^{-cU^{\epsilon/2}},\qquad
 Ue^{-\epsilon^2(\log U)^2/64}.
\]
Both have finite suprema on U>=2, depending only on epsilon. This proves the uniform statement (3).

## 6. Exact scope of the new estimate

At the user's compensation scale U=Zq_D, Theorem 1 improves the expanded-row RMS scale from the pointwise bound sqrt(Z/q_D) to O(q_D^{-1/2}). This is genuine sextic orthogonality with the original zero masks, but it is an expanding-row assertion.

The finite-row range proved here requires
\[
 Q\ge Z^{2+\epsilon}q_D^{1+\epsilon}.
\]
The user's critical probe instead uses a much shorter row ball, Q approximately Z^{5/6-2d}. Formula (14) does not apply at that scale. The remaining precise issue for this route is to estimate the nonzero Poisson frequencies of the actual completed-row products when Qq_D is much smaller than U^2, retaining the coupled Gauss factor and the original slot sums. The complete-residue identity (4) cannot be substituted for that short-row estimate.

This note does not prove the full finite-domain F_Z energy bound, the mixed low-probe target R4, the independent high-side continuation, or RH.

## Fixed sources

1. User's [all-scale marked-row bound](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/reports/20261011_qrh_selection_bridge/MARKED_ROW_BOUND.md), fixed commit `e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8`.
2. User's [exact compensation formula](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/COMPENSATION.md), fixed commit `4495df1319b2ee655cc52cc90b7512371fd0f0c4`, equations (1)-(4).
3. [`openai/math`, fixed paper.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`: original sextic symbol and zero-extension definitions; prime character order and Gauss identities around lines 760-800; corrected row around lines 3349-3412; marked physical row around lines 8083-8137.

The independent mathematical verification is [REFEREE_SEXTIC_MEAN_SQUARE.md](REFEREE_SEXTIC_MEAN_SQUARE.md). This proof uses the original arithmetic definitions and the user’s positive majorant; it does not use the external 7/8 zero-free theorem or a new Lean build.

## Appendix: the exact external Gauss square preserves sextic-core orthogonality

This is a short corollary of Theorem 1 above, with the original unnormalized Gauss sum
\[
 g_s(m)=g_{\chi_s}(s,-m)=\sum_{x\bmod s}\chi_s(x)e(-mx/s).
\]
The normalization in the original probe is q_s^{-1/2}g_s(m). The ideal s is good, as in that probe. Put
\[
 s_2=\prod_{p:\,v_p(s)\ge2}p.
\]
All means below first fix U,D,s and then expand the m disk.

**Corollary.** Uniformly over U>0, squarefree good D, and all such s,
\[
 \boxed{\mathsf M\left(\frac{|g_s(m)|^2}{q_s}
             |B_D(U;m,s)|^2\right)\le C/q_D.}            \tag{G1}
\]
If (D,s_2) is not the unit ideal, the function inside this mean vanishes identically.

The exact pair identity behind (G1), for A=cv^3k^6 and A'=c'v'^3k'^6, is
\[
 \mathsf M\left(\frac{|g_s|^2}{q_s}
                  \chi_A\overline{\chi_{A'}}\right)
 =\begin{cases}
 \displaystyle\prod_{p\mid sAA'}(1-q_p^{-1}),
 &(c,v)=(c',v'),\ (AA',s_2)=1,\\
 0,&\text{otherwise}.
 \end{cases}                                           \tag{G2}
\]
Thus the original external Gauss factor does not break the completed-core orthogonality. This identity includes all higher-power Gauss degeneracies; it does not replace s by a squarefree index.

### Local proof

By CRT the absolute square of the Gauss sum factors into local absolute squares; the CRT unit multipliers of the additive parameter do not change the formulas below. Write e=v_p(s), j=v_p(m), and P=q_p.

If e>=1 and 6 does not divide e, decomposition of the residue variable modulo p^e into its class modulo p and its remaining p^{e-1} lifts gives zero unless j=e-1. In the latter case the Gauss absolute square is P^{2e-1}. Thus the normalized weight is
\[
 |g_{p^e}(m)|^2/P^e=P^{e-1}1_{j=e-1}.                 \tag{G3}
\]
Its average is P^{e-1}(P^{-(e-1)}-P^{-e})=1-P^{-1}. For e=1, (G3) is exactly the unit mask 1_{p\nmid m}. For e>=2 its support consists of multiples of p.

If 6 divides e, the original character is the unit mask, not the constant function. Its Gauss sum is the prime-power Ramanujan sum: zero for j<e-1, equal to -P^{e-1} for j=e-1, and equal to P^{e-1}(P-1) for j>=e. Its normalized squared-weight mean is
\[
 P^{e-2}(P^{-(e-1)}-P^{-e})
 +P^{e-2}(P-1)^2P^{-e}
 =P^{-1}(1-P^{-1})+(1-P^{-1})^2=1-P^{-1}.              \tag{G4}
\]
Since here e>=6, this weight also has support on multiples of p.

Consequently every p|s_2 forces both A and A' to avoid p, or their zero-extended character product is identically zero on this Gauss support. Once they avoid p, the local character product is one, and (G3)-(G4) give the factor 1-P^{-1}. At a prime with e=1, the weight is the unit mask and ordinary sextic orthogonality still gives zero unless the two core exponents coincide. At primes outside s, equation (4) of the main note applies. Distinct pairs (c,v) must therefore give zero somewhere, while matching pairs give exactly (G2).

In every nonzero term marked by D on both sides, the product in (G2) is at most phi(D)/q_D. The unchanged E/F/H partition and all-scale Gaussian bound from the main note then prove (G1), with the same uniform constant. If p divides both D and s_2, every row index contains p while every nonzero Gauss term has p|m, proving the stated pointwise vanishing.

For the infinite row, fix s first. The Gauss weight is then a bounded periodic function, so uniform absolute convergence of the original row justifies passing its finite truncations through the mean. No uniform-in-s interchange of moving limits is used.

### Scope

This corollary is about the actual factor in the probe, but still an expanding-row mean. The main note's finite-Q threshold is not automatically inherited: the period of a product now also includes s. In the original short window, the nonzero Poisson modes and the sum over moving s remain to be estimated.

Source for the exact normalization: fixed `openai/math` commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb, `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`, definition of g_psi and `eq:general-probe` at lines 3355-3412. Original zero-extension convention: lines 625-646 of the same file.
