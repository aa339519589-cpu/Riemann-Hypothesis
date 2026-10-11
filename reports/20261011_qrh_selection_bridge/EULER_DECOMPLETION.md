# Euler 去卷积与 sextic-core 标记的真实补偿探针

本文合并一个新物理探针的完整定义、局部主乘子及有限能量证明。所有原字符、Gauss 因子、坏素数与零延拓均保留；Part III 明确改变标记条件，不能与原探针混同。

- Part I：精确 Möbius 尺度变换与未标记主修正的无零性。
- Part II：逐个物理频率的有限除数表示，及全部移动 numerator 行的修正因子全纯域。
- Part III：原 selected 因子的剩余角向通道；新 core 标记后的完整有限 slot 主修正无零，并分成固定 Mellin 主因子和依赖 Z 的小余量。
- Part IV：新 core 标记及变换保持既有有限窗 sextic 大筛能量界。

各 Part 的公式编号独立。完整高端比较及负指数低端线性相关仍未证明；本稿不证明 RH。原用户 marked-row 结果保留其来源归属，外部大筛仅在 Part IV 的既有输入中使用。

# Part I. Exact Euler decompletion

## Principal Euler factor and an exact Möbius scale transform

### Status and source

This note concerns the actual post-Poisson principal numerator row u=1 of the original probe I_eta, including its auxiliary primitive character xi(m). It does not concern the unweighted periodic mean of g_s B_D. The zero additive Fourier frequency of the actual probe is absent, as the source explicitly states. Its principal numerator row consists instead of nonzero dual indices H=a^6.

The fixed source is [`openai/math`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex) commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`: the exact high identity and local Euler table at lines 3723-4050, and principal normalization at lines 5501-5535. We use those exact identities, not the external 7/8 zero-exclusion theorem.

The results proved here are: (i) an exact factorization of the principal correction; (ii) an absolutely convergent arithmetic operation on the physical probe which removes one specified Euler factor in its initial high identity; and (iii) holomorphy of the resulting unmarked correction near the principal residue, and nonvanishing of its principal specialization throughout Re x>1/2. The finite selected-prime compensation factors remain separate here; their revised core-marked version is treated in Part III. No global high comparison, critical low estimate, contour move across all other rows, or RH is proved.

### 1. The actual principal correction

The source defines
\[
 \mathcal F_{\eta,u}(x,w,z)=
 \frac{\zeta_F^S(6z)L^S(w,\chi_\bullet(u))}
 {L^S(x,\eta\overline{\chi_\bullet(u)})}
 \mathcal H_{\eta,u}(x,w,z),
\]
with H_eta(x)=mathcal H_{eta,1}(x,1,1/6). Put
\[
 \kappa(a)=\eta(a)^6\overline{\alpha(a)}^6,
 \qquad \alpha(a)=a/|a|.
\]
This is a genuine unitary Hecke character on the original good ideals; the sixth angular power is invariant under the six units. Its Euler series is denoted L^S(v,kappa) where absolutely convergent. No zero-free statement about this angular character is assumed.

At a good prime of norm P, on the principal residue put
\[
 d_p=\eta(p)P^{-x},\qquad r_p=\kappa(p)P^{3-6x}.
\]
The source's j=0 local table gives exactly
\[
 \boxed{H_p(x,1,1/6)
 =\frac{1-P^{-2}}{1-r_p}
       \left(1+\frac{d_p-r_p}{P(1-d_p)}\right).}         \tag{1}
\]
Indeed in that table rho=1, V=W=1/P and R=r_p. Thus
\[
 P_p^*=(1+P^{-1})(r_p-d_p)/(1-r_p),
\]
\[
 P_p=(1+P^{-1})/(1-P^{-1})+P_p^*,
\]
and H_p=P_p(1-P^{-1})^2/(1-d_p), which simplifies to (1).

Define
\[
 E_\eta(x)=\prod_{p\notin S}
       \left(1+\frac{\eta(p)P^{-x}-\kappa(p)P^{3-6x}}
                        {P(1-\eta(p)P^{-x})}\right).
\]
In the region Re x>2/3, where all three Euler products converge absolutely, (1) yields
\[
 \boxed{H_\eta(x)=\zeta_F^S(2)^{-1}
                  L^S(6x-3,\kappa)E_\eta(x).}          \tag{2}
\]
This equality agrees with the source's correction in its original domain. The factor L^S(6x-3,kappa) cannot simply be called nonzero when 1/2<Re x<=2/3.

### 2. The residual correction is holomorphic and nonzero past 1/2

On every closed half-plane Re x>=1/2+delta, delta>0,
\[
 \left|\frac{d_p-r_p}{P(1-d_p)}\right|
 \le C\{P^{-3/2-\delta}+P^{-1-6\delta}\}.               \tag{3}
\]
The prime-ideal sum converges by elementary ideal counting. Thus E_eta converges normally on Re x>1/2 and is holomorphic there, uniformly on compact sets in the unit target phases.

Every local factor is nonzero on this half-plane without changing the original excluded set S. Its numerator, after the common denominator P(1-d_p) is taken, is
\[
 P-(P-1)d_p-r_p.
\]
For Re x>1/2 one has |d_p|<P^{-1/2} and |r_p|<1, so
\[
 |(P-1)d_p+r_p|<(P-1)/\sqrt P+1<P\qquad(P\ge2).
\]
The denominator is also nonzero. The normally convergent product of these nonzero factors is nonzero. In particular no enlargement of S, no replacement of the auxiliary xi, and no change of b_* is needed.
Consequently
\[
 \boxed{\zeta_F^S(2)^{-1}E_\eta(x)
 \text{ is holomorphic and nonvanishing on Re }x>1/2.} \tag{4}
\]
The bounds are local in the distance to 1/2; no uniform bound as delta tends to zero is asserted.

### 3. A physical operation removing precisely this Euler factor

For arbitrary X,Y,Z>0 define, using the same original physical probe,
\[
 \boxed{I_\eta^\flat(X,Y,Z)=
 \sum_{d\,\mathrm{good}}\frac{\mu(d)\kappa(d)}{q_d^2}
                 I_\eta(X,Y,Z/q_d^6).}                \tag{5}
\]
All characters in every summand are unchanged. In particular xi(m), the original zero extensions, and the original Gauss factors remain present. This is a newly defined arithmetic transform of the probe, not a statement that the original probe already has the modified multiplier.

For fixed X,Y, the physical s,m ranges are finite. The user's [all-scale marked-row bound](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/reports/20261011_qrh_selection_bridge/MARKED_ROW_BOUND.md) gives
\[
 |I_\eta(X,Y,T)|\le C_{X,Y}\sqrt T\quad(T>0).
\]
Hence (5) is absolutely convergent, dominated by C_{X,Y}sqrt(Z) times sum_d q_d^{-5}. This holds with any fixed original marking D as well. Its corresponding physical row is explicitly
\[
 B_D^\flat(U;m,s)=\sum_d\frac{\mu(d)\kappa(d)}{q_d^2}
                         B_D(U/q_d^6;m,s),              \tag{6}
\]
with the unconditional bound
\[
 |B_D^\flat(U;m,s)|\le C\sqrt U/q_D.                   \tag{7}
\]
The constant remains independent of U,D,m,s and omega(D).

It is important that (6) does not insert chi_d(m). Thus it must not be identified with simply restricting the old n variable to squarefree ideals. The displayed convolution, including all of its nonunit cases, is its definition.

In the source's initial high lines Re x=3, Re w=3, Re z=2, replacing Z by Z/q_d^6 multiplies its common Mellin weight by
\[
 q_d^{-6(x+z-1)}.
\]
Together with the coefficient q_d^{-2} this is q_d^{4-6x-6z}. Therefore the exact initial high identity for (5) is the source's high integral multiplied by
\[
 \sum_d\mu(d)\kappa(d)q_d^{4-6x-6z}
 =\frac1{L^S(6x+6z-4,\kappa)}.                         \tag{8}
\]
On these lines the real argument is 26, so this extra ideal sum is uniformly absolutely convergent and bounded independently of imaginary parts. The source's absolutely convergent high identity and its rapidly decaying Mellin weights justify all interchanges. No continuation through a zero or interchange of a conditional Euler product is involved.

The same operation commutes with each finite original marked-slot/subset compensation: apply (5) to its common Z variable, while keeping the original finite prime tuple, markings, X/q_r and Y/q_r fixed. Every term receives the same multiplier (8). This statement does not change the moving slot windows as functions of Z.

### 4. Local high continuation near every principal residue point

The natural new local correction is
\[
 H_p^\flat(x,w,z)=(1-R_p)H_p(x,w,z),\qquad
 R_p=\kappa(p)P^{4-6x-6z}.
\]
For the principal numerator u=1 write d=eta(p)P^{-x}, V=P^{-6z}, W=P^{-w}, R=R_p. Directly from the source's exact local table,
\[
 H_p^\flat=N_p/(1-d),
\]
\[
 \begin{split}
 N_p={}&1-d+dVW^2P-dVW^2-dVWP+dV+dW\\
       &+RVW^2-RW^2+RW/P-R/P-VW.                       \tag{9}
 \end{split}
\]
In particular, no denominator 1-R remains.

For any fixed sigma>1/2 there is an open neighborhood of
\[
 (\Re x,\Re w,\Re z)=(\sigma,1,1/6)
\]
in which every monomial of N_p-(1-d) has magnitude at most C P^{-1-epsilon_sigma}, with a positive epsilon_sigma. This can be checked at the center: the respective decay exponents are
\[
 \sigma+2,\ \sigma+3,\ \sigma+1,\ \sigma+1,\ \sigma+1,
 \ 6\sigma,\ 6\sigma-1,\ 6\sigma-1,\ 6\sigma-2,\ 2.
\]
They all exceed one because sigma>1/2. By continuity of these affine exponents they remain so on a sufficiently small neighborhood. Also |1-d| is uniformly bounded below at large primes. Thus product_p H_p^flat converges normally in this neighborhood. More explicitly, the open domain defined by Re x>0 and all ten displayed affine decay exponents being greater than one is convex. It contains the initial point (3,3,2) and every (sigma,1,1/6) with sigma>1/2. Hence this product gives one connected holomorphic continuation of the modified correction, not unrelated local germs.

On the principal residue itself, (1) gives
\[
 \boxed{\mathcal H_{\eta,1}^\flat(x,1,1/6)
       =\zeta_F^S(2)^{-1}E_\eta(x).}                   \tag{10}
\]
This is the unmarked holomorphic nonzero correction of (4), before the finite selected-prime compensation factors are included. The fixed scalar residue factors at w=1 and z=1/6 are unchanged by (8) in the initial region where these identities can be compared. Reaching those residues globally, and controlling every other row and endpoint, requires a separate valid contour argument; the local continuation just proved is not that argument.

### 5. Exact remaining burden

This arithmetic operation removes the specific angular Euler factor from the principal multiplier. Here the nonvanishing assertion concerns the unmarked correction. Although the scale transform commutes with each original finite compensation, this alone does not make the full selected-prime multiplier nonzero on the enlarged half-plane. Its local selected factors and their prime-window sums remain separate objects to be estimated or redesigned. It does not establish a high approximation for all numerator rows when the target zero supremum is merely above 1/2. The unproved global high-side inequalities identified in the user's [HIGH_SIDE_SCOPE.md](HIGH_SIDE_SCOPE.md) remain to be rebuilt for the transformed probe.

It also does not preserve every hypothetical negative low exponent for free. For example, if at fixed X,Y one only knew an absolute bound |I(X,Y,T)|<=C T^a, termwise use in (5) would require
\[
 \sum_d q_d^{-2-6a}<\infty,
 \quad\text{i.e. }a>-1/6.                             \tag{11}
\]
The desired exponent -3/16 is below that threshold. In addition, the source's critical low estimates are on coupled moving X,Y,Z and slot scales, whereas (5) fixes X,Y and the physical slots while varying the third scale. It would be invalid to substitute the coupled-scale estimate unchanged into (5).

The pointwise bound (7) is genuinely stable, but it is much weaker than the missing critical correlation. A complete proof must obtain a new low estimate for (5) with these exact scales and must establish the global high comparison. Neither is proved here, and no RH conclusion is claimed.


# Part II. Physical core and all-row correction

## Two exact interfaces for the Möbius scale transform

These are the physical and all-row interfaces for Part I. They use the original fixed S, b_*, xi, all characters, and every nonunit zero mask without alteration. No global critical low or high comparison is claimed.

### A. The infinite inverse transform becomes a finite physical correction

Fix m!=0. Let rad_S(m) be the squarefree product of the good prime ideals dividing m. Write the original row coefficient as b(c,n;s), exactly as in the [user’s marked-row theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/reports/20261011_qrh_selection_bridge/MARKED_ROW_BOUND.md), so its only m dependence is chi_{cn^3}(m). For all good ideals c,n,k with c squarefree,
\[
 b(c,nk^2;s)=b(c,n;s)\kappa(k),\qquad
 \kappa(k)=\eta(k)^6\overline{\alpha(k)}^6.             \tag{A1}
\]
This identity does not require any coprimality among c,n,k. To verify it from the source, gamma_2(c) stays fixed, alpha and eta are multiplicative, xi(k)^6=1, and chi_{k^6}(b_*)=1 since k is good. The reciprocity bicharacter has values +/-1, hence R(k^6,s)=R(cn^3,k^6)=1. Its quadratic refinement gives G(k^6)=1: indeed G(k^2)=chi_k(4), whose cube is one, and R(k^2,k^2)=1. Thus G(cn^3k^6)=G(cn^3), proving (A1).

The transform B_D^flat remains identically zero if (D,m)!=1, because each original row in its definition is zero. If (D,m)=1, its exact physical expansion is
\[
\boxed{\begin{split}
 B_D^\flat(U;m,s)
 =\sum_{c\,\mathrm{sf},v\,\mathrm{sf}}&
 b(c,v;s)\chi_{cv^3}(m)q_c^{-1/2}q_v^{-1}
 \frac{\kappa(F)}{q_F^2}\\
 &\cdot\sum_{h\mid\operatorname{rad}_S(m)}
 \frac{\mu(h)\kappa(h)}{q_h^2}
 W\left(\frac{q_cq_v^3q_F^6q_h^6}{U}\right),
 \qquad F=\frac D{\gcd(D,cv)}.
\end{split}}                                                   \tag{A2}
\]
The integer ideal F depends on c,v. In particular, a missing marked prime contributes a positive once-occurring square layer, whereas a prime of m contributes a negative once-occurring square layer. The two should not be combined into an unmarked squarefree restriction.

For the proof, initially use the absolutely convergent original Mellin line Re t=4. Every n decomposes uniquely as n=v k^2 with v squarefree; c and v may share primes. Set a=2+6t. By (A1), the k-series is
\[
 \sum_{k:F\mid k,(k,m)=1}\kappa(k)q_k^{-a}
 =\kappa(F)q_F^{-a}L^S(a,\kappa)
       \prod_{p\mid\operatorname{rad}_S(m)}
                       (1-\kappa(p)q_p^{-a}).          \tag{A3}
\]
Here (F,m)=1 follows from (D,m)=1. Shared primes between F and k/F are allowed, so (A3) has no extra factor at F. The exact Möbius scale transform multiplies this Mellin row by L^S(a,kappa)^{-1}, leaving only the finite product. Expanding it and inverting the Gaussian Mellin transform proves (A2).

All of these manipulations take place in absolute convergence. After inversion, the finite h-sum has coefficient total at most sum_h q_h^{-2}<=zeta_O(2). For fixed D, the finitely many possible F permit termwise positive Gaussian majorants for the c,v sums, proving convergence for every U>0. The stronger uniform bound |B_D^flat|<=C sqrt(U)/q_D remains supplied by the original absolute convolution argument.

For D=1, F=1. Then the physical column cv^3 is genuinely sixth-power-free (its prime exponents are 0,1,3,4), and the only residual square-layer correction is the finite sum over divisors of rad_S(m). For a nontrivial D, the mandatory factor F^6 in the norm argument is retained. This is an exact finite representation, not a hypothesis about cancellation in a Möbius partial sum.

### B. A uniform correction domain for every physical numerator row

Let u be any original sixth-power-free nonzero element with (u,S)=1, including its unit. Define the modified local factors
\[
 H_{p,\eta,u}^\flat=(1-R_p)H_{p,\eta,u},\qquad
 R_p=\kappa(p)P^{4-6x-6z}.
\]
For 0<delta<=1/4, consider
\[
 \Omega_\delta:\quad
 \Re x\ge1/2+\delta,\qquad
 \Re w\ge1-\delta/4,\qquad
 \Re z\ge1/6-\delta/12.                               \tag{B1}
\]
The product of the H_p^flat converges normally on a neighborhood of every point in this region, defines a holomorphic function there, and satisfies
\[
 \boxed{\mathcal H_{\eta,u}^\flat(x,w,z)
        \ll_{\delta,\epsilon,\mathcal A}q_u^\epsilon}
 \quad\text{for every epsilon>0},                     \tag{B2}
\]
uniformly in all imaginary parts and all target unit phases. The constants do not depend on the moving row u.

#### Primes not dividing u

Put rho=chi_p(u), d=eta(p)conjugate(rho)P^{-x}, W=rho P^{-w}, and V=P^{-6z}. The polynomial in Part I, equation (9) is unchanged. Its ten monomial decay exponents have their minima in (B1) at the lower corner. In their order in that polynomial these minima are
\[
\begin{gathered}
 5/2,\quad 7/2,\quad 3/2+\delta/4,\quad
 3/2+\delta/2,\quad3/2+3\delta/4,\\
 3+9\delta/2,\quad2+5\delta,\quad2+21\delta/4,\quad
 1+11\delta/2,\quad2-3\delta/4.
\end{gathered}                                               \tag{B3}
\]
All are at least 1+2delta for 0<delta<=1/4. Also |1-d|>=1-2^{-1/2}. Thus
\[
 |H_{p,\eta,u}^\flat-1|\le C P^{-1-2\delta}\quad(p\nmid u).
                                                               \tag{B4}
\]
The first two exponents in (B3) have exact cancellation of their delta contributions; their constant values are intentional.

#### Primes dividing u

Put j=v_p(u) in {1,...,5}, and rho=chi_p(u/p^j). In the source's definitions the zero-extended W and d are now zero. Its exact local table therefore simplifies to
\[
 H_{p,\eta,u}^\flat
 =1-R_p/P-\eta(p)(P-1)P^{-x-w}V^{1_{j\le1}}
                          +(1-V)J_j,                 \tag{B5}
\]
where the original five J_j entries are unchanged. In (B1), |V|<=1, and the possible J_j terms have decay exponents bounded below by
\[
 3/2+3\delta/4,\quad3\delta,\quad
 1/2+11\delta/4,\quad4\delta,\quad
 1/2+15\delta/4,\quad6\delta.
\]
The common term with P-1 has exponent at least 1/2+3delta/4; the R_p/P term has exponent at least 1+11delta/2. Every one is at least 2delta on the declared range. Hence
\[
 |H_{p,\eta,u}^\flat-1|\le C P^{-2\delta}\quad(p\mid u).
                                                               \tag{B6}
\]

The product over p not dividing u converges normally with a uniform bound by (B4). For the remaining finite product, for every epsilon>0 the inequality 1+C P^{-2delta}<=P^epsilon holds at all sufficiently large P. The finitely many remaining prime factors contribute only a fixed constant. This proves (B2), retaining all row primes and every original zero extension.

This domain controls the holomorphic correction only. It neither removes the denominator L(x,eta conjugate chi_u) nor proves a permissible global movement of the high contour with a power-saving error. The original low correlation target must also be rebuilt for the exact finite row (A2).


# Part III. The selected-prime interface and revised core marking

## 真实补偿主乘子的剩余角向通道及 sextic-core 标记修复

### 1. 输入与范围

采用固定 [`openai/math`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex) 提交 `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` 的真实 probe、辅助 primitive 字符、原非负 slot 权及其 local-family-table。使用已审核的 Möbius 去卷积
\[
\kappa(a)=\eta(a)^6\overline{\alpha(a)}^6,\qquad
I^\flat(X,Y,Z)=\sum_a\frac{\mu(a)\kappa(a)}{q_a^2}I(X,Y,Z/q_a^6).
\]
它在原绝对收敛高表示中准确乘 \(L^S(6x+6z-4,\kappa)^{-1}\)。已证未标记 principal correction 为
\[
H_\eta^\flat(x)=\zeta_F^S(2)^{-1}E_\eta(x),
\]
其中 \(E_\eta\) 在 \(\Re x>1/2\) 正常收敛且无零。以下不把未标记结论误用为原完整补偿结论，而是给出准确障碍及一个不同的真实标记探针。

### 2. 原 completed-index 标记仍有 r/d 通道

在真实 principal numerator \(u=1\)、\(w=1,z=1/6\)，对一个好 slot prime 置
\[
P=q_p,\quad d_p=\eta(p)P^{-x},\quad
r_p=\kappa(p)P^{3-6x},\quad
A_p=1-d_p+(d_p-r_p)/P.
\]
原 local table 给
\[
P_p^*=(1+P^{-1})\frac{r_p-d_p}{1-r_p},\quad
P_p=\frac{1+P^{-1}}{1-P^{-1}}+P_p^*.
\]
因此原 selected 比值准确为
\[
\mathcal B_p
=\frac{(r_p/d_p-1)(1-P^{-1})}{A_p}-P^{-1},
\tag{2.1}
\]
而去卷积后的局部 correction 为
\[
H_p^\flat=\frac{1-P^{-2}}{1-d_p}A_p,
\]
\[
\boxed{G_p^\flat=\frac{1-P^{-2}}{1-d_p}
\left[-1+(1-P^{-1})\left(\frac{r_p}{d_p}+\frac{d_p}{P}\right)
                     +\frac{r_p}{P^2}\right].}
\tag{2.2}
\]
这里
\[
r_p/d_p=\eta(p)^5\overline{\alpha(p)}^6P^{3-5x}.
\tag{2.3}
\]
对每个固定 \(1/2<\sigma<3/5\)，(2.2) 严格推出
\[
|G_p^\flat(x,1,1/6)|/P^{3-5\sigma}\longrightarrow1
\quad(P\to\infty,\ \Re x=\sigma),
\tag{2.4}
\]
一致于虚部及原单位相位。这是实际原素数局部式的结论；没有换任意系数。
因此原 full selected-prime multiplier 不能从未标记 \(H_\eta^\flat\) 的无零直接继承。
相应有限 slot 内仍有真实角向和
\[
\sum_{p\in\mathcal P_i(Z)}W_i(q_p/P_i)
 \eta(p)^5\overline{\alpha(p)}^6q_p^{13/6-5x}.
\tag{2.5}
\]
本稿不假定它有平方根节省，也不声称 (2.4) 反驳原 R4。原多素数求和可以有相消；(2.4) 只严格否定该局部因子在整个 \(\Re x>1/2\) 仍一致接近 \(-1\) 的说法。

### 3. 新物理标记：标记 sextic core

每个原 \(n\) 唯一写成
\[
n=v k^2,\qquad v\text{ 平方自由}.
\]
定义新的 row 和 probe：将原标记 \(1_{D\mid cn^3}=1_{D\mid cn}\) 替换为
\[
\boxed{1_{D\mid cv}.}
\tag{3.1}
\]
除此之外，原 \(\gamma_2,\alpha,\eta,\Xi_*,G,\mathcal R,\xi(m)\)、零延拓、全部 Gauss 因子和原 slot 窗口均不变。允许 \((c,v)>1\)、\((cv,k)>1\)。记新 probe 为 \(I_{\eta;D}^{\rm core}\)。它是一个新定义，未称其等于原 \(I_{\eta;D}\)。

原全正尺度正项界仍支配这个子和，故
\[
|B_D^{\rm core}(U;m,s)|\ll\sqrt U/q_D.
\]
所以按同一系数去卷积的 \((B_D^{\rm core})^\flat\) 绝对存在，且有相同量级上界。新完整有限补偿后去卷积定义为
\[
\begin{aligned}
\mathcal I_{\eta,Z}^{\rm core,\flat}
=\sum_a\frac{\mu(a)\kappa(a)}{q_a^2}
\sum_{\mathbf p}\prod_iW_i(q_{p_i}/P_i)
\sum_J(-1)^{|J|}q_r^{-3/2}\overline{\eta(D)}\,
 I_{\eta;D}^{\rm core}
 \left(X/q_r,Y/q_r,Zq_D/q_a^6\right),
\end{aligned}
\tag{3.2}
\]
其中 \(r=p_J,D=p_{J^c}\)，原 prime windows 仍固定在原 \(Z\) 的尺度，不随外部 \(a\) 重缩放。

这项标记只取决于每个 prime 的 \(e_0=v_p(c)\in\{0,1\}\) 与 \(l=v_p(n)\bmod2\)，因此原绝对收敛高表示的局部标记恰为 \(e_0=1\) 或 \(l\) 奇。去卷积仍在原高起始线准确乘同一 \(L^S(6x+6z-4,\kappa)^{-1}\)。

### 4. 原 local table 中被移除的准确家族

在 \(u=1,w=1,z=1/6\) 的 \(j=0\) 行，原标记中不满足 (3.1) 的项准确是
\[
e_0=0,\qquad l=2r+2\quad(r\ge0).
\]
原 local-family-table 对它有两个非零系列：\(s\) 的局部指数为零时贡献
\(R(1-P^{-1})/((1-R)(1-V))\)，局部指数为一时贡献
\(W_{\rm loc}R/(1-R)\)。在 \(V=W_{\rm loc}=P^{-1},R=r_p\) 上相加为
\[
(1+P^{-1})\frac{r_p}{1-r_p}.
\]
没有遗漏 \(c\) 与 \(n\) 共享 prime 的项，因为 \(e_0=1\) 的全部项都保留在新标记内。于是新标记局部和准确是
\[
\boxed{P_{p,\rm core}^*
=-(1+P^{-1})\frac{d_p}{1-r_p}.}
\tag{4.1}
\]
其余三个 parity 家族的 \(j=0\) 值也可直接按原 Gauss 素幂支撑检查：\(e_0=1,l\) 偶留下上述 \(-d_p\) 系列；\(l\) 奇的两家族在 \(j=0\) 为零。

### 5. 完整新补偿 principal multiplier 无零

把 (4.1) 放入同一 marked-minus-rescaled 操作，再乘去卷积因子 \(1-r_p\)。准确得到
\[
\boxed{G_{p,\rm core}^\flat
=\frac{1-P^{-2}}{1-d_p}
 \left[-1+(1-P^{-1})\frac{d_p}{P}+\frac{r_p}{P^2}\right].}
\tag{5.1}
\]
令
\(\mathcal B_{p,\rm core}=G_{p,\rm core}^\flat/H_p^\flat\)。那么
\[
\boxed{\mathcal B_{p,\rm core}+1
=-\frac{(1-P^{-1})[d_p(1-P^{-1})+r_p/P]}{A_p}.}
\tag{5.2}
\]

在整个 \(\Re x>1/2\)，\(|d_p|<P^{-1/2}\)、\(|r_p|<1\)。若 selected primes 均满足 \(P\ge100\)（固定正长 slots 在充分大 \(Z\) 自动满足），则
\[
|A_p|\ge1-P^{-1/2}-(P^{-1/2}+1)/P\ge0.889,
\]
\[
|\mathcal B_{p,\rm core}+1|
\le\frac{P^{-1/2}+P^{-1}}{0.889}<1/4.
\tag{5.3}
\]
这给出真实 selected 局部比值在整个半平面上的统一控制，没有使用角向 prime sum 相消。

对每个非空原 prime slot 定义正正常数
\[
N_i(Z)=\sum_{p\in\mathcal P_i(Z)}W_i(q_p/P_i)q_p^{-5/6}>0,
\]
\[
C_i(x,Z)=-N_i(Z)^{-1}\sum_{p\in\mathcal P_i(Z)}
W_i(q_p/P_i)q_p^{-5/6}\mathcal B_{p,\rm core}(x).
\tag{5.4}
\]
由 (5.3)，\(|C_i-1|<1/4\)。因此它全纯且无零。原 prime windows 的不交性给出完整新 principal correction 的精确分解；用 \((-1)^K\prod_iN_i(Z)\) 正规化后为
\[
\boxed{\mathcal H_{\eta,Z}^{\rm core,\flat}(x)
=\zeta_F^S(2)^{-1}E_\eta(x)\prod_{i=1}^KC_i(x,Z),
\qquad\Re x>1/2.}
\tag{5.5}
\]
未标记积与每个有限 slot 因子均无零，故 (5.5) 全纯且无零。这个式子首先由真实绝对收敛高表示得到，然后由该正常收敛表达式给出局部 principal 延拓；它没有将整体 \(u\)-和跨线移位。

作为可选的数据选择，对任意固定 \(\sigma_0>1/2\)，可在构建全部新 probe 数据之前选定一次充分大的固定排除集 \(S\)，并随之构建 \(b_*,\xi\) 等数据，使
\[
\boxed{\sup_{\Re x>\sigma_0}
|\mathcal H_{\eta,Z}^{\rm core,\flat}(x)-1|\le1/2}
\tag{5.6}
\]
一致于所有 prime slots 非空的原允许 \(Z\)。理由：\(E_\eta\) 的尾积在该半平面一致趋于 1，\(\zeta_F^S(2)^{-1}\to1\)，而 (5.2) 的尾部上界
\(C(P^{-\sigma_0}+P^{2-6\sigma_0})\to0\) 一致于全部虚部和单位相位。固定有限 \(K\) 的乘积因此可控制在所示圆盘。原充分大 \(Z\) 的 slot 非空性可沿用原固定 ray prime normalizer；结论不对空 slot 作除法。这是构建一套新固定数据的许可选择，不是对已经固定的 probe 无损改变 \(S\)。

#### 5.1 固定 Mellin 主乘子与依赖 Z 的余量

式 (5.5) 的完整有限 correction 仍依赖 \(Z\)。为避免把它误当固定 Mellin 信号，设
\[
\ell_{\min}=\min_i\ell_i>0,\qquad
\mathcal R_{\eta,Z}^{\rm core}(x)=\prod_iC_i(x,Z)-1.
\]
由固定 annular 支撑内 \(q_p\asymp P_i=Z^{\ell_i}\)、(5.2) 及正权平均，准确有
\[
\boxed{\sup_{\Re x>1/2}|\mathcal R_{\eta,Z}^{\rm core}(x)|
 \ll_{K,(\ell_i,W_i)} Z^{-\ell_{\min}/2}.}
\tag{5.7}
\]
因而固定的算术主乘子应取
\[
H_{\eta,\mathrm{fixed}}^{\rm core,\flat}(x)
 =\zeta_F^S(2)^{-1}E_\eta(x),
\]
而不是把 \(\mathcal H_{\eta,Z}^{\rm core,\flat}\) 当作固定函数。
定义与原 prime normalizer 相同的非零标量
\[
A_T(Z)=(-1)^K Z^{-\ell/6}\prod_iN_i(Z),\qquad \ell=\sum_i\ell_i=1/6.
\]
则原固定 ray prime normalizer 给 \(|A_T(Z)|\asymp (\log Z)^{-K}\)，且新 principal residue 的完整算术因子准确分解为
\[
\boxed{\mathfrak H_{\eta,1,Z}^{\rm core,\flat}(x,1,1/6)
 =H_{\eta,\mathrm{fixed}}^{\rm core,\flat}(x)
 Z^{\ell/6}A_T(Z)\{1+\mathcal R_{\eta,Z}^{\rm core}(x)\}.}
\tag{5.8}
\]
按 \(A_T\) 而非只按 \(\prod_iN_i\) 正规化，保留原几何信号指数：
\[
X^{1/3}Z^{x-5/6}Z^{\ell/6}=Z^{x-11/16}.
\]
(5.7) 是全虚部一致的局部 residue 因子误差；完整 principal 三重积分的轮廓移动与余项估计尚须单独验证。尤其本稿没有由 (5.7) 直接宣称全 probe 与固定 Mellin 信号已满足高比较。

### 6. 新物理 row 的有限除数形式

对 \(m\ne0\)，记 \(\operatorname{rad}_S(m)\) 为 \(m\) 的好 prime 支撑。令 \(\beta(c,v;s,m)\) 是原 corrected row 系数，包含 \(\chi_{cv^3}(m)\)。则
\[
\boxed{
(B_D^{\rm core})^\flat(U;m,s)
=\sum_{\substack{c,v\ {\rm sf}\\D\mid cv}}
\frac{\beta(c,v;s,m)}{\sqrt{q_c}q_v}
\sum_{h\mid\operatorname{rad}_S(m)}
 \frac{\mu(h)\kappa(h)}{q_h^2}
 W_{\rm G}\left(\frac{q_cq_v^3q_h^6}{U}\right).}
\tag{6.1}
\]
在每个固定 \(m\) 的绝对收敛 Mellin 线上，写 \(n=vk^2\) 后原 \(k\)-和等于 \(L^{S\cup\operatorname{supp}m}(2+6t,\kappa)\)。去卷积把它除以 \(L^S(2+6t,\kappa)\)，准确余下
\(\prod_{p\mid m,p\notin S}(1-\kappa(p)q_p^{-2-6t})\)，反演即 (6.1)。原 ray 相位满足 \(G(k^6)=\mathcal R(k^6,s)=\Xi_*(k)^6=1\)，并且 \(\chi_{k^6}(m)=1_{(k,m)=1}\)。故 (6.1) 没有假定非单位处字符为 1，也不需要任何 Möbius 部分和估计。

### 7. 已解决与未解决的目标

(5.5)–(5.8) 为新、完整、真实补偿探针建立了临界线右侧的 principal 局部 correction 无零性，并将其分成固定全纯无零主乘子与全虚部一致的幂次小余量。它修复了仅作去卷积时 (2.3) 的实际 selected 角向通道；完整 principal 积分及 continuation criterion 的全部条件并未因此完成。

原 R4 针对旧标记，不能未经证明转用于 (3.2)。新 row 虽有相同点态绝对界及有限除数表达，仍须重建负指数低端线性相关；原完整反射估计也不能因子和变小便自动用于带符号平方范数。所有非principal \(u\) 的全局高比较、可统一的余量以及合法整体 contour 仍未证明。故这不是 RH 证明，也未给出原 R4 的严格反例。


# Part IV. Coarse finite-window energy of the revised probe

## Finite-row energy survives core marking and Möbius decompletion

This is a coarse low-side stability result for the new probe, not the critical mixed correlation. It uses the previously proved full-frequency sextic large-sieve row bound and the positive Gauss-divisor transfer. It does not import the stronger original full-compensation reflected-row bound into the modified object.

### 1. Precisely changed marking

Write every original n uniquely as n=v k^2 with v squarefree. Define the core-marked row by replacing only the original condition D|cn^3 with
\[
 D\mid cv.
\]
Keep the original coefficients b(c,n;s), zero-extended chi_{cn^3}(m), and Gaussian unchanged. Denote the result by B_{D,core}(U;m,s). Define
\[
 B_{D,core}^\flat(U;m,s)
 =\sum_{d\,\mathrm{good}}\frac{\mu(d)\kappa(d)}{q_d^2}
                      B_{D,core}(U/q_d^6;m,s).          \tag{1}
\]
The untransformed core marking is a subset of the original completed-index marking in a positive coefficient majorant. Therefore the user's proof, applied to that majorant, gives
\[
 |B_{D,core}(U;m,s)|\le C\sqrt U/q_D                  \tag{2}
\]
for all U>0, independently of the number of marking primes. This is not an inequality between the absolute values of two oscillating rows.

The exact finite representation is
\[
\begin{split}
 B_{D,core}^\flat(U;m,s)
 =\sum_{\substack{c,v\,\mathrm{sf}\\D\mid cv}}
 &b(c,v;s)\chi_{cv^3}(m)q_c^{-1/2}q_v^{-1}\\
 &\cdot\sum_{h\mid\operatorname{rad}_S(m)}
  \mu(h)\kappa(h)q_h^{-2}
  W(q_cq_v^3q_h^6/U),\qquad m\ne0.                    \tag{3}
\end{split}
\]
This follows from the same absolutely convergent Mellin cancellation as Part II, Appendix A, but the marking already lies on c,v and imposes no additional F-square layer. In particular, all original zeros when (D,m)!=1 remain.

### 2. Full-frequency finite-row estimate

Put
\[
 \mathscr T_6(Q,Z)=Q+Q^{1/6}Z+Q^{5/6}Z^{1/3}
                                      +Q^{1/3}Z^{5/6}.
\]
For every epsilon>0, uniformly in Z>=2, Q>=1, all squarefree good D, every allowed s, and every fixed nonzero element a,
\[
 \boxed{\sum_{0<q_m\le Q}
 |B_{D,core}^\flat(Zq_D;am,s)|^2
 \ll_\epsilon\frac{(QZq_D)^\epsilon}{q_D}
                         \mathscr T_6(Q,Z).}           \tag{4}
\]
The constant is independent of a, including its zero masks, and of omega(D).

First the established sextic large-sieve proof of the untransformed row estimate applies to B_{D,core}. Indeed, take E to consist of the marking primes dividing c and F=D/E. Freeze n as in that proof. The new marking merely requires the primes of F to have odd valuation in n, as well as the original condition F|n. This is an m-independent restriction in the outer n sum. The allowed c_0 columns still have (c_0,D)=1 and are squarefree. The same pointwise column-coefficient bounds and positive Minkowski majorants apply. The factor chi_{cn^3}(a) remains a fixed column or outer scalar mask of modulus at most one. Hence
\[
 \sum_{0<q_m\le Q}|B_{D,core}(Zq_D;am,s)|^2
 \ll_\epsilon (QZq_D)^\epsilon q_D^{-1}\mathscr T_6(Q,Z).
                                                               \tag{5}
\]
No termwise comparison with the oscillating completed-index row is used.

To pass to (4), put R=(Z/2)^{1/6}>=1 and split the d sum in (1). For q_d<=R, (5) is available at scale Z/q_d^6>=2. Minkowski and the elementary bound on the square root of a four-term sum show that this part has norm at most
\[
 C_\epsilon\frac{(QZq_D)^{\epsilon/2}}{q_D^{1/2}}
 [Q^{1/2}+Q^{1/12}Z^{1/2}
       +Q^{5/12}Z^{1/6}+Q^{1/6}Z^{5/12}].              \tag{6}
\]
The respective d-series are bounded by sum q_d^{-2}, sum q_d^{-5}, sum q_d^{-3}, and sum q_d^{-9/2}; all converge. The small epsilon prefactor at Z/q_d^6 is at most the one displayed.

For q_d>R, use the all-scale estimate (2) instead of applying a large-scale theorem outside its range. Since the disk has O(Q) elements, the tail norm is at most
\[
 C\sqrt{QZ/q_D}\sum_{q_d>R}q_d^{-5}
 \le C\sqrt{Q/q_D}\,Z^{-1/6}.                         \tag{7}
\]
Ideal counting gives the tail sum O(R^{-4}). This is absorbed by the first term of (6). Squaring proves (4). The same estimates justify the completed infinite sum in the row norm.

### 3. The actual external Gauss square

The positive Gauss-divisor transfer, applied to the uniform frozen-a version of (4), gives
\[
 \boxed{\sum_{\substack{s\,\mathrm{good}\\q_s\le Y}}
 \sum_{0<q_m\le Q}\frac{|g_{\chi_s}(s,-m)|^2}{q_s}
       |B_{D,core}^\flat(Zq_D;m,s)|^2
 \ll_\epsilon\frac{Y}{q_D}(QZYq_D)^\epsilon
                         \mathscr T_6(Q,Z)}            \tag{8}
\]
for Y,Q>=1 and Z>=2. In applying that transfer, first bound the scale-dependent epsilon loss by its value at Q, and then use the four exact powers 1,1/6,5/6,1/3. Thus no exponent greater than one is inserted into its moment statement. The possible p^6 Gauss branch is handled by its proved endpoint divisor moment, not by a maximum-Gauss estimate.

Formulae (4) and (8) are estimates on actual finite windows with every sixth-power frequency retained. They show that the new core marking and decompletion do not worsen these existing coarse finite-row bounds. They do not establish a negative low-probe exponent, do not automatically sum all compensation labels with their required signs, and do not transfer the original stronger reflected completed-row theorem.

### Fixed dependencies

- The user's all-scale positive marked-row proof, original commit e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8.
- The audited full-frequency sextic large-sieve transfer and fixed-row dilation version, [published full-frequency sixth-sieve theorem](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/b8df3dbbeeeb7c93816e8ba2c7ce8e7970ed11b8/reports/20261011_qrh_selection_bridge/SIXTH_SIEVE_DETECTOR.md), based on de Faveri's Theorem 1.1 and the verified fixed-ray family.
- The audited [published positive Gauss-divisor transfer](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/b8df3dbbeeeb7c93816e8ba2c7ce8e7970ed11b8/reports/20261011_qrh_selection_bridge/SIXTH_SIEVE_DETECTOR.md) (included in the same published sixth-sieve report).
- The exact physical Mellin cancellation in Part II, Appendix A.
