# Euler 去卷积与 sextic-core 标记的真实补偿探针

本文合并一个新物理探针的完整定义、局部主乘子及有限能量证明。所有原字符、Gauss 因子、坏素数与零延拓均保留；Part III 明确改变标记条件，不能与原探针混同。

- Part I：精确 Möbius 尺度变换与未标记主修正的无零性。
- Part II：逐个物理频率的有限除数表示，及全部移动 numerator 行的修正因子全纯域。
- Part III：原 selected 因子的剩余角向通道；新 core 标记的固定主因子与小余量；完整孤立 principal 三重积分的幂次比较。
- Part IV：新 core 标记及变换保持既有有限窗 sextic 大筛能量界。
- Part V：全部 numerator 行的精确 core-selected 局部式、反射域及保留未使用短多项式的乘积控制。
- Part VI：在原 buffered reflected numerator 输入下，z≥1/4 的联合误差槽估计。
- Part VII：以用户新 completed-row 反射为输入，通过精确改标记恒等式获得 core-flat 的全尺度反射界。

各 Part 的公式编号独立。孤立 principal 行的高端比较已完成；全部非principal 行的总高端比较及负指数低端线性相关仍未证明。本稿不证明 RH。原用户 marked-row 结果保留其来源归属，外部大筛仅在 Part IV 的既有输入中使用。

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


# Part III. The selected-prime interface and principal contour comparison

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
(5.7) 是全虚部一致的局部 residue 因子误差，本身不蕴含完整 principal 三重积分的轮廓移动与余项估计。§8 将单独完成这一 principal 积分步骤；全 probe 与固定 Mellin 信号的高比较仍须控制非principal 行。

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

(5.5)–(5.8) 为新、完整、真实补偿探针建立了临界线右侧的 principal 局部 correction 无零性，并将其分成固定全纯无零主乘子与全虚部一致的幂次小余量。它修复了仅作去卷积时 (2.3) 的实际 selected 角向通道。后面的 §8 将独立完成 principal 积分；continuation criterion 的全部条件仍未完成。

原 R4 针对旧标记，不能未经证明转用于 (3.2)。新 row 虽有相同点态绝对界及有限除数表达，仍须重建负指数低端线性相关；原完整反射估计也不能因子和变小便自动用于带符号平方范数。所有非principal \(u\) 的全局高比较、可统一的余量以及合法整体 contour 仍未证明。故这不是 RH 证明，也未给出原 R4 的严格反例。

### 8. 整个 principal 三重积分的两极点提取

本节进一步完成独立 principal 行与固定 Mellin 信号的比较；不移动或估计非principal 行的总和。
采用原全族零点上确界 \(\beta_*\)，只在 \(1/2<\beta_*\le1\) 情形讨论。这个上确界无需被某个零点取到。取
\[
\delta=\min\{(\beta_*-1/2)/2,1/4\}>0,
\qquad 0<e<\delta/100,
\]
并保留原固定有限 slots、几何 \(l_x=17/48,l_y=23/48,\ell=1/6,h=13/16\)。
记 \(\mathscr P_{\eta,Z}^{\rm core,\flat}\) 为 (3.2) 的绝对高表示中单独 \(u=1\) 项。定义
\[
 f_\eta^{\rm core,\flat}(Z)=\frac1{2\pi i}\int_{(2)}
 Z^{x-11/16}e^{(x-5/6)^2}
 \frac{H_{\eta,\mathrm{fixed}}^{\rm core,\flat}(x)}{L_F^S(x,\eta)}\,dx.
\tag{8.1}
\]
原 scalar residue 常数为
\[
 c_S=\widehat W_1(1)M(1/6)
   \left(\operatorname*{Res}_{v=1}\zeta_F^S(v)\right)^2/6>0.
\]
该常数与原数据相同，core marking 及去卷积不改变原外部 Mellin tests。

#### 8.1 全 principal 矩形上的完整 correction

在 \(u=1\) 的一般 \((x,w,z)\) 处，置
\[
 d=\eta(p)P^{-x},\quad W=P^{-w},\quad V=P^{-6z},
 \quad R=\kappa(p)P^{4-6x-6z}.
\]
从原 local table 中移除 §4 的整族，得到
\[
 (1-R)P_{p,\rm core}^*
   =-d-\eta(p)(P-1)P^{-x-w}\frac V{1-V}.
\]
marked-minus-rescaled 的准确局部式是
\[
 G_{p,\rm core}^\flat
 =\overline{\eta(p)}P^x
    \frac{(1-V)(1-W)}{1-d}(1-R)P_{p,\rm core}^*
       -P^{-w}H_p^\flat.
\]
注意最后一项仍是未标记 \(H_p^\flat\)。相消后得到
\[
\boxed{G_{p,\rm core}^\flat
 =-\frac{1-W}{1-d}\{1-V+(P-1)WV\}-WH_p^\flat.}
\tag{8.2}
\]
这个式子没有 \(1-R\)、\(P_p\) 或 \(H_p\) 分母。

在已证局部域
\[
 \Omega_\delta:\quad \Re x\ge1/2+\delta,\quad
 \Re w\ge1-\delta/4,\quad
 \Re z\ge1/6-\delta/12
\]
内，\(|1-d|\) 统一离零，\(|W|,|V|<1\)，且
\[
 |PWV|\le P^{-1+3\delta/4}\le1.
\]
已证的未标记局部估计 \(H_p^\flat=1+O_\delta(P^{-1-2\delta})\)
在 \(u=1\) 对全部好 primes 成立。因此 (8.2) 给
\[
 |G_{p,\rm core}^\flat|\ll_\delta1.
\tag{8.3}
\]
不作任何局部商，全 tuple correction 为
\[
 \sum_{\mathbf p}\prod_i
 [W_i(q_{p_i}/P_i)q_{p_i}^{z-1}G_{p_i,\rm core}^\flat]
 \prod_{p\notin S\cup\{p_i\}}H_p^\flat.
\]
未标记积的正 majorant 正常收敛，删除任意有限 selected 集不增加该 majorant。
每个 annular slot 的 prime 数由理想计数为 \(O(P_i)\)，故在任意固定实参数盒内
\[
 \boxed{|\mathfrak H_{\eta,1,Z}^{\rm core,\flat}(x,w,z)|
    \ll_{\delta,\mathrm{data}}Z^{\ell\Re z}}
\tag{8.4}
\]
一致于全部虚部。它在 \(\Omega_\delta\) 邻域全纯；本证明没有把 selected 商在零点处作未经证明的除法。

#### 8.2 轮廓与三个精确余项

对任意 \(\varepsilon>0\)，充分大 \(Z\) 有
\[
\begin{split}
\boxed{\left|\frac{\mathscr P_{\eta,Z}^{\rm core,\flat}}{c_SA_T(Z)}
                -f_\eta^{\rm core,\flat}(Z)\right|
 \ll_{\eta,e,\varepsilon,\mathrm{data}}{}&
 Z^{\beta_*-11/16+(1+h)e-l_y\delta/8+\varepsilon}\\
 &+Z^{\beta_*-11/16+e-h\delta/24+\varepsilon}\\
 &+Z^{\beta_*-11/16+e-\ell_{\min}/2+\varepsilon}.}
\end{split}
\tag{8.5}
\]

证明直接针对本行重做轮廓步骤，而不引用原 principal 提取引理的 \(\sigma_0\ge7/8\) 限制。其绝对起始积分为
\[
 \frac1{(2\pi i)^3}\int_{(3)}\int_{(3)}\int_{(2)}
 X^{1/2-z}Z^{x+z-1}Y^{w-1}e^{(x+z-1)^2}
 M(z)\widehat W_1(w)
 \frac{\zeta_F^S(6z)\zeta_F^S(w)}{L_F^S(x,\eta)}
 \mathfrak H_{\eta,1,Z}^{\rm core,\flat}(x,w,z)\,dz\,dw\,dx.
\tag{8.6}
\]
先移至 \(\Re x=\beta_*+e,\Re w=1+e,\Re z=1/6+e\)。
这条路在 \(\Omega_\delta\) 内，分母倒数在 \(\Re x>\beta_*\) 全纯。
随后将 \(w\) 移至 \(1-\delta/8\)，跨过唯一的 \(w=1\) 极点。
在其留数中再将 \(z\) 移至 \(1/6-\delta/24\)，跨过唯一的 \(z=1/6\) 极点。
未取 \(w\) 留数的积分保持 \(\Re z=1/6+e\)。所有这些实参数仍严格位于所需局部域内；\(M(z)\) 在 \(\Re z>0\) 全纯。

原固定目标 reciprocal 的 logarithmic-control 引理，在零点上确界右侧固定距离 \(e\) 给出固定多项式高度界。主字符情形 \(1/L\) 在一处有零而非极点。两个 zeta 因子在未取留数的最终直线上也有固定多项式高度界。另一方面
\[
 e^{-(\Im(x+z))^2}|M(z)|\,|\widehat W_1(w)|
\]
在每个固定实参数盒上关于三个高度联合任意幂快速衰减；换元
\((\Im x,\Im z,\Im w)\mapsto(\Im(x+z),\Im z,\Im w)\)
的行列式为一。配合 (8.4)，原 integrated/trace-tail 证明逐字给出水平边趋零及绝对积分界。取 \(w\) 留数后同理使用二维核；因此不存在未处理的无限高度轮廓步骤。

外部权与 (8.4) 的真实 \(Z\) 指数为
\[
 l_x/2+\Re x-1+h\Re z+l_y(\Re w-1).
\]
在两个余积分的线上代入，分别得到 (8.5) 的前两项。除以 \(A_T\) 只消耗任意小的 \(Z^\varepsilon\)。
除以 \(c_SA_T(Z)\) 后，双留数恰为
\[
 \frac1{2\pi i}\int_{(\beta_*+e)}Z^{x-11/16}e^{(x-5/6)^2}
 \frac{H_{\eta,\mathrm{fixed}}^{\rm core,\flat}(x)}{L_F^S(x,\eta)}
 \{1+\mathcal R_{\eta,Z}^{\rm core}(x)\}\,dx.
\]
(5.7)、固定距离 reciprocal 界及 Gaussian 直接给 (8.5) 的第三项。
最后只将无余量的主积分右移至 \(\Re x=2\)：沿途无分母零点，固定 \(H\) 全纯且在该闭实条带高度一致有界，Gaussian 杀掉水平边。所得正是 (8.1)，证明 (8.5)。

因为 \(l_y\delta/8,h\delta/24,\ell_{\min}/2\) 都严格为正，先把 \(e\)、再把 \(\varepsilon\) 取得足够小，(8.5) 推出某个 \(\sigma_{\rm pr}>0\) 的真正幂次比较
\[
 \frac{\mathscr P_{\eta,Z}^{\rm core,\flat}}{c_SA_T(Z)}
       -f_\eta^{\rm core,\flat}(Z)
 =O_{\eta,\mathrm{data}}(Z^{\beta_*-11/16-\sigma_{\rm pr}}).
\tag{8.7}
\]
这里 \(e,\varepsilon,\sigma_{\rm pr}\) 可依 \(\beta_*-1/2\) 及固定 slot 长度，均不依高度和 \(Z\)。

因此，整个 principal 积分步骤已由本节闭合。仍未闭合的是同一新物理 probe 的负指数低端线性相关，以及所有非principal 行的总高比较；两者均不能由 (8.7) 推出。

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

# Part V. All-row core-selected factors and finite-slot savings

## Core-selected local factors on all numerator rows

This appendix extends the exact core marking and Möbius decompletion to every original sixth-power-free numerator row. It retains the original auxiliary character, all nonunit zero extensions, and all physical prime slots. It is an exact local and finite-slot result; the global sum over numerator rows and the critical low correlation remain separate estimates.

### 1. Source table and the exact deletion

Use the fixed QRH source [`openai/math`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex) commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, local-family-table at lines 4075–4140 and the quotient-free selected operation at lines 8657–8730. Write P=q_p, j=v_p(u) in {0,...,5}, rho=chi_p(u/p^j), and
\[
 V=P^{-6z},\quad R=\kappa(p)P^{4-6x-6z},\quad
 W=\chi_p(u)P^{-w},\quad D=\eta(p)\overline{\chi_p(u)}P^{-x}.
\]
Thus W=D=0 at primes dividing u, while rho is always a unit phase. Put
\[
 a_p=\overline{\alpha(p)}^3\eta(p)^3,\quad
 b_p=\overline{\alpha(p)}^2\eta(p)^2\overline{\chi_p(4)},
 \qquad a_p^2=b_p^3=\kappa(p).
\]
The original completed-index marked local sum is P_p^*. The core marker keeps exactly the families with e_0=v_p(c)=1 or odd v_p(n). It therefore deletes the entire family e_0=0, v_p(n)=2r+2, r>=0. Summing the source's entries of that family gives
\[
 \frac{1}{1-R}\left[
 \frac{R(1-P^{-1})}{1-V}
 +1_{j=0}\rho P^{-w}R
 +1_{j=5}(-\kappa(p)P^{3-6x})\right].                 \tag{1}
\]
In particular the j=5 deletion cannot be omitted. All shared c,n prime cases belong to retained families.

Consequently the exact new local marked sum is
\[
 P_{p,\mathrm{core}}^*=
 \frac{1}{1-R}\left[
 -\frac{\eta(p)(P-1)P^{-x-w}V^{1_{j\le1}}}{1-V}
 +J_{j,\mathrm{core}}\right],                         \tag{2}
\]
with the complete table
\[
\begin{array}{c|l}
 j&J_{j,\mathrm{core}}\\\hline
0&-\eta(p)\rho^{-1}P^{-x}\\
1&\eta(p)P^{-x-w}\\
2&a_p\rho^{-3}P^{3/2-3x}\\
3&-\eta(p)b_p\rho^{-2}P^{2-3x-w}
             +b_p^2\rho^{-4}P^{2-4x}\\
4&-\eta(p)a_p\rho^{-3}P^{5/2-4x-w}\\
5&0.
\end{array}                                             \tag{3}
\]
These are identities initially on the original absolute lines. They follow by deleting a specified physical parity family, not by redefining local Euler coefficients arbitrarily.

Let H_p^flat=(1-R)H_p be the unmarked decompleted correction, which was proved holomorphic in Part II. Set
\[
 M_{p,j}=-\eta(p)(P-1)P^{-x-w}V^{1_{j\le1}}
                         +(1-V)J_{j,\mathrm{core}}.
\]
The precise core-selected factor after the same two-term physical compensation is
\[
 \boxed{G_{p,\mathrm{core}}^\flat
 =\overline{\eta(p)}P^x\frac{1-W}{1-D}M_{p,j}
                           -P^{-w}H_p^\flat.}           \tag{4}
\]
The last term is the rescaled unmarked probe and must remain. Formula (4) follows directly by multiplying
\(\overline\eta(p)P^xP_{p,\mathrm{core}}^*-P^{-w}P_p\)
by \((1-R)(1-V)(1-W)/(1-D)\). In particular it has no P_p or H_p denominator, so it is valid through zeros of either correction.

For p not dividing u, put d=D. Then (4) becomes the especially useful identity
\[
 \boxed{G_{p,\mathrm{core}}^\flat
 =-\overline\rho\frac{1-W}{1-d}
       [1-V+(P-1)WV]-P^{-w}H_p^\flat.}                 \tag{5}
\]
If H_p^flat=N_p/(1-d), with N_p the polynomial in Part I, the exact compensation error is
\[
 E_p:=G_{p,\mathrm{core}}^\flat+
                 \overline{\chi_p(u)}H_p^\flat
 =\overline\rho\frac{1-W}{1-d}
                 \{N_p-[1-V+(P-1)WV]\}.               \tag{6}
\]
Here we used P^{-w}=overline(rho)W. At p dividing u, E_p=G_p by the original zero extension.

For explicit use at the ramified row primes, (4) reads
\[
\begin{array}{c|l}
j&G_{p,\mathrm{core}}^\flat\\\hline
1&P^{-w}(1-PV-H_p^\flat)\\
2&-(P-1)P^{-w}+\overline\eta(p)a_p\rho^{-3}(1-V)P^{3/2-2x}-P^{-w}H_p^\flat\\
3&-(P-1)P^{-w}+(1-V)[-b_p\rho^{-2}P^{2-2x-w}
 +\overline\eta(p)b_p^2\rho^{-4}P^{2-3x}]-P^{-w}H_p^\flat\\
4&-(P-1)P^{-w}-a_p\rho^{-3}(1-V)P^{5/2-3x-w}-P^{-w}H_p^\flat\\
5&-(P-1)P^{-w}-P^{-w}H_p^\flat.
\end{array}                                                    \tag{7}
\]

### 2. A reflected tube for the unmarked and selected corrections

Fix 0<delta<1/4 and e>0. Consider the real tube
\[
 \mathcal T_{\delta,e}:\qquad
 \tfrac12+\delta\le\sigma:=\Re x\le1-\delta,
 \quad\Re w\ge1-\sigma+e,
 \quad\Re z\ge\tfrac16+e.                              \tag{8}
\]
All constants concerning finite slots below are uniform on a fixed compact box of real parts inside this tube, and in all imaginary parts and unit phases. The real box restriction only accounts for fixed annular support ratios raised to Re z.

The same unmarked decompleted product converges normally on a neighborhood of each point of (8). More precisely, if nu=min(e,delta)>0, then
\[
 H_p^\flat=1+O_{\delta,e}(P^{-1-\nu})\ (p\nmid u),
 \qquad H_p^\flat=1+O_{\delta,e}(P^{-\nu})\ (p\mid u).
                                                               \tag{9}
\]
To verify the first assertion directly, the ten monomials of N_p-(1-d), in the order of the main note, have decay exponents at least
\[
 2-\sigma+8e,\quad3-\sigma+8e,\quad1+7e,
 \quad\sigma+1+6e,\quad1+e,
 \quad4\sigma+14e,\quad4\sigma-1+8e,
 \quad5\sigma-1+7e,\quad6\sigma-2+6e,
 \quad2-\sigma+7e.                                      \tag{10}
\]
They all exceed 1 by at least nu. At p dividing u, use the earlier exact formula
\[
 H_p^\flat=1-R/P-\eta(p)(P-1)P^{-x-w}V^{1_{j\le1}}
                                     +(1-V)J_j,
\]
where J_j is the original table, including J_5. The common marked term has decay at least e. The six possible J_j monomials have respective lower decay bounds
\[
 1+e,\quad3\delta,\quad2\delta+e,
            \quad4\delta,\quad3\delta+e,\quad6\delta.
\]
Also R/P decays by at least 1+6delta+6e. This proves (9). The usual positive divisor-product bound therefore yields, also after omitting any chosen finite prime tuple,
\[
 \prod_{p\notin S,\ p\notin\mathcal P}|H_p^\flat|
                 \ll_{\delta,e,\epsilon}q_u^\epsilon.  \tag{11}
\]
No nonvanishing for arbitrary u is needed.

Equations (5)–(7) give the sharper, quotient-free local estimates
\[
\begin{array}{c|cc}
 &|G_{p,\mathrm{core}}^\flat|&|E_p|\\\hline
p\nmid u&O_{\delta,e}(1)&O_{\delta,e}(P^{-\delta})\\
p\mid u&O_{\delta,e}(P^{\sigma})&O_{\delta,e}(P^{\sigma}).
\end{array}                                                    \tag{12}
\]
Indeed, at unramified p the term PVW has decay 6Re z+Re w-1>=1-sigma+7e>=delta; V and d decay more rapidly than P^{-delta}, while N_p-(1-d) has (9). Formula (6) proves its error estimate. In (7), the common growth is P^{1-Re w}<=P^{sigma-e}. The remaining possible growth exponents are
\[
 3/2-2\sigma,\quad2-2\sigma-\Re w,
 \quad2-3\sigma,\quad5/2-3\sigma-\Re w,
\]
all at most sigma when sigma>1/2 and Re w>=1-sigma+e. For j=1, PV has modulus <=P^{-6e}, so that entry is bounded. This proves (12) with the true ramified support retained.

### 3. Finite-slot dynamic expansion with an explicit power saving

Fix the original disjoint annular prime slots, their bounded smooth weights W_i, and positive lengths ell_i. Put P_i=Z^{ell_i}, ell=sum_i ell_i, ell_min=min_i ell_i. Define the exact full correction without any local quotient by
\[
 \mathfrak H_{\eta,u,Z}^{\mathrm{core},\flat}
 =\sum_{(p_i)}\prod_i[W_i(q_{p_i}/P_i)q_{p_i}^{z-1}
                          G_{p_i,\mathrm{core}}^\flat]
       \prod_{p\notin S,\ p\notin\{p_i\}}H_p^\flat.   \tag{13}
\]
Let
\[
 S_i(u;z)=\sum_{p\in\mathcal P_i(Z)}
 W_i(q_p/P_i)q_p^{z-1}\overline{\chi_p(u)}.
\]
On each real box specified above, for every epsilon>0 and Z>=2,
\[
 \boxed{|\mathfrak H_{\eta,u,Z}^{\mathrm{core},\flat}|
       \ll_{\delta,e,\epsilon}q_u^\epsilon Z^{\ell\Re z},}
                                                               \tag{14}
\]
\[
 \boxed{\mathfrak H_{\eta,u,Z}^{\mathrm{core},\flat}
 =(-1)^K\mathcal H_{\eta,u}^\flat\prod_iS_i(u;z)
  +O_{\delta,e,\epsilon}
       (q_u^\epsilon Z^{\ell\Re z-\delta\ell_{\min}}).} \tag{15}
\]
Constants also depend on the fixed slots and their weights. Uniformity in all imaginary parts is unchanged.

For completeness, on slot i ideal counting and (12) give a total unramified error mass O(P_i^{Re z-delta}). There are at most O(log(2q_u)) prime divisors of u, so the ramified error mass is
\[
 O_{\delta,e}(\log(2q_u)P_i^{\Re z-1+\sigma})
 \ll_{\epsilon}q_u^\epsilon P_i^{\Re z-\delta}.
\]
The non-error local factor has total positive mass O(P_i^{Re z}), by (9) and the original zero extension; the all-G mass has the same bound up to q_u^epsilon. The unselected product is bounded by (11). Expand each selected factor as
\(G_p=-\overline{\chi_p(u)}H_p^\flat+E_p\).
The zero-error term is exactly the main term of (15), since every H_p appears once. Every other term contains at least one slot error, giving the displayed saving. Choose the small divisor-product exponents initially as epsilon/(2K+2), so that all finite products of losses are at most q_u^epsilon. This proof never divides by H_p, including at ramified primes or zeros of the full correction.

### 4. Stronger near-residue bounds

In the previously audited region
\[
 \Omega_\delta:\quad\Re x\ge1/2+\delta,
 \quad\Re w\ge1-\delta/4,
 \quad\Re z\ge1/6-\delta/12,\quad0<\delta\le1/4,
\]
again restricted to any fixed real box for slot constants, (5)–(7) give
\[
 |E_p|\ll_\delta P^{-1/2-\delta}\quad(p\nmid u).
\tag{16}
\]
For the ramified rows, the respective growth bounds for j=1,...,5 are
\[
 1,\quad P^{\max(\delta/4,1/2-2\delta)},
 \quad P^{\max(\delta/4,1/2-3\delta)},
 \quad P^{\delta/4},\quad P^{\delta/4}.                 \tag{17}
\]
All are at most P^{1/2}. Consequently (14) holds in this region and the error in (15) improves to
\[
 O_{\delta,\epsilon}(q_u^\epsilon
                      Z^{\ell\Re z-\ell_{\min}/2}).    \tag{18}
\]
The proof is the same sparse-divisor versus full-slot count. For (16), the three extra errors beyond H_p^flat-1 in (6) have decay exponents Re x, 6Re z, and 6Re z+Re w-1, bounded below respectively by 1/2+delta, 1-delta/2, and 1-3delta/4. The latter two exceed the first for delta<=1/4.

The gain in (15) or (18) is an actual finite-slot estimate. It does not by itself control the sum over u with reciprocal L-functions, establish a shifted high integral for all rows, or supply the missing negative low-probe exponent. Those budgets must use the exact main polynomials S_i and the displayed ramified exponents.

### 5. A product majorant retaining every unused short polynomial

There is a stronger form useful for numerator moment estimates. For all sufficiently large Z, depending only on the fixed real box, delta,e and the slots,
\[
 \boxed{|\mathfrak H_{\eta,u,Z}^{\mathrm{core},\flat}|
 \ll_{\delta,e,\epsilon}q_u^\epsilon
       \prod_i\bigl(|S_i(u;z)|+P_i^{\Re z-\delta}\bigr)}  \tag{19}
\]
in the reflected tube. In Omega_delta the exponent delta in every slot on the right can be replaced by 1/2. This estimate keeps the moment savings from every slot in which an error has not been used.

Here is a safe factorization proof, distinct from dividing the whole correction by H. By (9), for all sufficiently large unramified selected primes, |H_p^flat-1|<=1/2. Only at these primes define
\[
 e_i(u;x,w,z)=\sum_{\substack{p\in\mathcal P_i(Z)\\p\nmid u}}
 W_i(q_p/P_i)q_p^{z-1}E_p/H_p^\flat.
\]
Thus |e_i|<=C P_i^{Re z-delta}; in Omega_delta it is <=C P_i^{Re z-1/2-delta}. No division is made at a prime of u, whether its local factor vanishes or not.

Partition the finite tuple sum (13) by the subset R of slots whose chosen prime divides u. For a fixed tuple of such ramified primes let H^{(R tuple)} be the unmarked Euler product with just these primes omitted. Its absolute value is <=C_epsilon q_u^epsilon by (11). All remaining selected primes are unramified, so the sum over them factors exactly as
\[
 \prod_{i\notin R}[-S_i(u;z)+e_i(u;x,w,z)].             \tag{20}
\]
The remaining coefficient is H^{(R tuple)} times the selected G factors at the ramified tuple. Taking its absolute value and summing those finitely many primes gives a factor at most
\[
 C_\epsilon q_u^\epsilon
 \prod_{i\in R}P_i^{\Re z-\delta}.
\]
The near-residue bound replaces delta here by 1/2, as before. Summing over R yields (19), allocating the small epsilon losses before the finite subset expansion. The identities are exact prior to these upper bounds; arbitrary ramified zeros are preserved. This product majorant is still only a local/slot ingredient for a full numerator estimate.

# Part VI. Reflected joint-numerator error estimate

## Core-marked joint numerator estimate on reflected contours

This is a companion to Part V of this report. All factors below are its exact core-selected, Möbius-decompleted factors. We retain every physical sixth-power-free row, original nonunit zero, and strict ramified local term. The only analytic hypothesis is the same buffered reflected numerator estimate used in the fixed QRH source, Proposition `probe-errors` (lines 8853–9055). No RH or new uniform zero-free hypothesis is assumed.

### 1. Precise statement

Fix (0<\delta<1/4), (0<e<\delta/100), and a bounded range (1/4\le z_r\le z_{\max}). For
\[
 \tfrac12+\delta\le a\le1-\delta,
 \qquad x_r=a+16e,\quad w_r=1-a-6e,\quad \Re z=z_r,                 \tag{1}
\]
let (u\ne0) be an original sixth-power-free physical row, (q_u\asymp U\ge1), ((u,S)=1). Let (\psi_u^*) be the primitive character inducing the numerator (\chi_\bullet(u)), and assume it is nonprincipal. At the retained points (w), suppose, as supplied by the source's buffered numerator bin estimate, that
\[
 |L(1-w,\overline{\psi_u^*})|\ll_{\epsilon}U^\epsilon
 \quad (|\Im w|\le T_1).                                         \tag{2}
\]
The implied constants in (2) are uniform over the specified retained family. All statements below are uniform in (u), these retained heights, and the other imaginary parts. They include fixed arithmetic and finite weight-seminorm constants.

For sufficiently large (Z), depending on the fixed data, (e,\delta) and the positive slot lengths, every slot prime has (H_p^\flat\ne0). Only at these selected primes define
\[
 B_{p,\mathrm{core}}^\flat=G_{p,\mathrm{core}}^\flat/H_p^\flat,
 \qquad
 Q_i(u;z)=-\sum_{p\in\mathcal P_i(Z)}W_i(q_p/P_i)q_p^{z-1}
                          \overline{\chi_p(u)},
\]
\[
 D_i^{\mathrm{core},\flat}(u)
 =\sum_{p\in\mathcal P_i(Z)}W_i(q_p/P_i)q_p^{z-1}
       \{B_{p,\mathrm{core}}^\flat+\overline{\chi_p(u)}\}.
                                                                    \tag{3}
\]
The original slot annuli are disjoint and (P_i=Z^{\ell_i}), with fixed (\ell_i>0). For every subset (I) of the slots,
\[
 \boxed{\left|L^S(w,\chi_\bullet(u))
             \prod_{i\in I}D_i^{\mathrm{core},\flat}(u)\right|
 \ll U^{a-1/2+6e+\epsilon}(3+T_1)^C
                \prod_{i\in I}P_i^{z_r-1/2}.}                        \tag{4}
\]
Here (C<\infty) is fixed on the indicated bounded real ranges. Arbitrarily small powers used in divisor bounds are included once in the displayed (U^\epsilon). A harmless additional (\prod_iP_i^\epsilon) may instead be retained if desired.

Consequently the **same** exact correction has the pointwise dynamic decomposition
\[
 \mathfrak H_{\eta,u,Z}^{\mathrm{core},\flat}
 =\mathcal H_{\eta,u}^\flat
       \sum_{I\subseteq\{1,\ldots,K\}}
       \prod_{i\in I}D_i^{\mathrm{core},\flat}
       \prod_{i\notin I}Q_i .                                      \tag{5}
\]
No division by the global (\mathcal H_{\eta,u}^\flat) is used, and it need not be nonzero. Equation (5) follows algebraically from the quotient-free tuple identity and the nonvanishing of its finitely many selected local factors only.

The reflected (z) line may therefore be taken at (1/4), rather than the original (17/50), in this local joint-numerator estimate. This is not by itself a global contour shift: the full bin contours, their joins and reciprocal denominator still need their own bounds.

### 2. Local nonvanishing and the unramified cancellation

Write (P=q_p), (V=P^{-6z}), (R=\kappa(p)P^{4-6x-6z}),
(W=\chi_p(u)P^{-w}), (d=\eta(p)\overline{\chi_p(u)}P^{-x}).
For (p\nmid u), the exact unmarked correction is (H_p^\flat=N_p/(1-d)), with
\[
\begin{split}
N_p={}&1-d+dVW^2P-dVW^2-dVWP+dV+dW\\
 &+RVW^2-RW^2+RW/P-R/P-VW .                           \tag{6}
\end{split}
\]
At (1), every monomial of (N_p-(1-d)) decays by (P^{-1-\nu}), where one can take (\nu=\min(10e,\delta)>0). The potentially tight monomial is (dW), whose decay is (x_r+w_r=1+10e). The terms involving (R) have strictly larger margins when (z_r\ge1/4). Hence
\[
 H_p^\flat=1+O(P^{-1-\nu})\quad(p\nmid u).                          \tag{7}
\]
At (p\mid u), the exact formula is
\[
 H_p^\flat=1-R/P-\eta(p)(P-1)P^{-x-w}V^{1_{j\le1}}
                       +(1-V)J_j,\qquad j=v_p(u),                   \tag{8}
\]
with the original (J_j), including (J_5=-\kappa(p)P^{3-6x}). The common term decays at least (P^{-10e}); the (J_j) boundary terms decay at least (P^{-2\delta}), except (J_1), which is smaller still. Thus
\[
 H_p^\flat=1+O(P^{-\nu})\quad(p\mid u).                             \tag{9}
\]
All constants are uniform in phases and heights. Taking the slot primes sufficiently large makes (|H_p^\flat-1|<1/2), and gives the stated local quotients. Equations (7)–(9) also give the usual bound (|\mathcal H_{\eta,u}^\flat|\ll_\epsilon U^\epsilon).

Put (E_p=G_{p,\mathrm{core}}^\flat+\overline{\chi_p(u)}H_p^\flat). For (p\nmid u), the exact identity is
\[
 E_p=\overline\rho\frac{1-W}{1-d}
       \{N_p-[1-V+(P-1)WV]\},\qquad \rho=\chi_p(u).                \tag{10}
\]
In deriving (10), (P^{-w}=\overline\rho W). In particular, there is **no bare (W) error**. The difference in braces consists of the monomials already in (6), together with (V) and (-PVW), and its leading (d) term. Their smallest decay is at least
\[
 \min\{a+16e,\,6z_r-a-6e\}
 \ge\tfrac12+\delta-6e>\frac12+\delta/2.                         \tag{11}
\]
Every other monomial has a larger decay exponent. Also (w_r\ge\delta-6e>0), so the prefactors in (10) are bounded. Dividing by (7),
\[
 |B_{p,\mathrm{core}}^\flat+\overline{\chi_p(u)}|
                  \ll P^{-1/2-\delta/2}\quad(p\nmid u).           \tag{12}
\]
Elementary ideal counting in each annular prime slot now bounds the sum of these unramified error labels by (O(P_i^{z_r-1/2-\delta/2})). No prime cancellation is used for error labels.

### 3. Ramified boundary terms and the strict family

At (p\mid u), the main character is exactly zero. From the exact core-selected table, after multiplying by (P^{z-1}), separating (P^z), and dividing by the bounded (H_p^\flat), all non-strict boundary terms have the following exponents (bounded factors (1-V) are suppressed):
\[
\begin{array}{c|ccccc}
j&1&2&3&4&5\\\hline
 &-1-w_r,\ 1-w_r-6z_r-1
 &\tfrac12-2x_r
 &1-2x_r-w_r,\ 1-3x_r
 &\tfrac32-3x_r-w_r
 &\text{none}.
\end{array}                                                       \tag{13}
\]
The entry (1-w_r-6z_r-1=-w_r-6z_r) in the (j=1) column is the (PV) term after normalization. Each entry in (13) is at most (-1/2-c\delta), for a fixed positive (c). The common rescaling term (-P^{-w}H_p^\flat) has normalized exponent (-1-w_r<-1).

The only term not bounded this way is
\[
 -(P-1)P^{-w},\qquad j\ge2,                                      \tag{14}
\]
coming from the actual local family ((e_0,l,k,m)=(1,0,1,0)). Its normalized exponent is (-w_r). Core marking retains this family. The removed square-layer family and removed (J_5) do not create replacements for it.

For the primitive numerator conductor (\mathfrak f_u), the exact Kummer/reciprocity argument in the source gives
\[
 q_{\mathfrak f_u}\ll_S q_{\operatorname{rad}(u)}
 \le C_S U\prod_{p\in J_0}P^{-(j_p-1)}                            \tag{15}
\]
for any set (J_0) of distinct selected ramified labels. Every good (p\mid u) has conductor exponent one, since the local character (\chi_p^{j_p}) has nontrivial order (6/\gcd(6,j_p)). This input is unchanged by the new core marking.

Let (A_*=1/2-w_r=a-1/2+6e>0). The primitive functional equation, (2), and Stirling yield
\[
 |L(w,\psi_u^*)|\ll q_{\mathfrak f_u}^{A_*}
                       U^\epsilon(3+T_1)^C.                       \tag{16}
\]
Restoring the original zero-extended numerator costs (U^\epsilon): the fixed deleted factors and the factors at row primes have bounded positive product because (w_r>0); the character is already zero at every good ramified conductor prime. Fixed normalizing factors are included in the constant.

For a tuple of strict labels (J_0), apply (15) **once to the entire set**, before summing any labels. Each has (j_p\ge2), so
\[
 -w_r-(j_p-1)A_*\le-w_r-A_*=-\tfrac12.                            \tag{17}
\]
Combining (14)–(17) gives the simultaneous factor
\[
 U^{A_*+\epsilon}(3+T_1)^C\prod_{p\in J_0}P^{z_r-1/2}.            \tag{18}
\]
Distinctness is guaranteed by the original disjoint slot annuli. Thus the same conductor factor is not spent twice.

Expand the product of error slots into unramified labels, non-strict ramified terms, and strict terms. Equations (12)–(13) give the required slot factor for the first two types. Equation (18) supplies it for all strict labels together. Each ramified slot has only divisor-many possible labels, whose total cost is (U^\epsilon) after fixing the preliminary losses. This proves (4), including (I=\varnothing). The tuple-independent unmarked product is then bounded by (7)–(9), and (5) follows as stated.

### 4. Exact scope

This establishes the reflected local error interface for the newly defined full core probe. It permits the original detector main-slot polynomial and preserves its row-independent coefficients and all masks. It does not yet prove a row-count estimate outside its stated source hypotheses, the global nonprincipal high comparison, or the low R4 correlation. In particular, moving the real (z) contour in the full integral still requires a separate contour-accounting proof.

Fixed source: [QRH paper at fd4aeeb2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), Proposition `probe-errors`, lines 8853–9055, for the unchanged primitive-conductor and reflected-functional-equation inputs. The exact new local factors are proved in the companion Part V of this report from that source's local-family table.

# Part VII. Exact transfer of the user’s completed reflection to core-flat rows

## An exact bridge from core-flat rows to the user's completed reflection

### Input and attribution

The reflected completed-row estimate in this note is the user's [completed-row reflection theorem at commit 56c6cf64ac7e683e02e2a6fbf0f57f8004e24102](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/56c6cf64ac7e683e02e2a6fbf0f57f8004e24102/reports/20261011_qrh_selection_bridge/MARKED_ROW_REFLECTION.md). It is not claimed as our new theorem. We use its original completed marker D|cn^3 and its all-scale estimate
\[
 |B_D(U;m,s)|\le C\min\left\{\frac{\sqrt U}{q_D},
                  \frac{H(m)\sqrt{q_D}}{\sqrt U}\right\},          \tag{1}
\]
where H(m)<=C R(m) and R(m) is the norm of the good-prime radical of m. All original coefficients, ray data and nonunit zero extensions are retained. The new step below is an exact finite-marker identity that makes (1) applicable to the different core-flat row; there is no direct comparison between two oscillating marked rows.

### 1. Exact physical identity

Let D be good and squarefree, U>0, m!=0, and let s be an original allowed row parameter. Write n=v k^2 with v squarefree. The core marker is D|cv. Its first Möbius scale transform is denoted B_{D,core}^flat. Then
\[
\boxed{\begin{split}
 B_{D,\mathrm{core}}^\flat(U;m,s)
 =1_{(D,m)=1}\sum_{F\mid D}\frac{\mu(F)\kappa(F)}{q_F^2}
 \sum_{\substack{a\ \mathrm{good}\\(a,D)=1}}
 \frac{\mu(a)\kappa(a)}{q_a^2}
 B_{D/F}\left(\frac{U}{q_F^6q_a^6};m,s\right).
\end{split}}                                                    \tag{2}
\]
The B on the right is the user's original completed marked row. The second sum excludes every prime of the full D, not just the primes of F. No chi_a(m) or chi_F(m) is inserted. The external indicator is necessary: without it, (2) need not hold when a marked prime divides m.

Here is a proof retaining the global phases. The already verified coefficient identity
\[
 b(c,vk^2;s)=b(c,v;s)\kappa(k)
\]
holds without any coprimality assumption among c,v,k. Work first on the original absolute Mellin line Re t=4 and set
\[
 r_p=\kappa(p)P^{-2-6t},\qquad
 M_D(c,v)=D/\gcd(D,cv).
\]
For (D,m)=1, the k-series of the completed D-row is exactly
\[
 L^{S\cup\operatorname{supp}(m)}(2+6t,\kappa)
                                  \prod_{p\mid M_D(c,v)}r_p.
\]
For the core row it is that same L-series times 1_{D|cv}. The sum over a in (2) gives the inverse Euler product over good primes outside D. Its ratio with the displayed k-series leaves
\[
 \prod_{p\mid\operatorname{rad}_S(m)}(1-r_p)
                                  \prod_{p\mid D}(1-r_p)^{-1}.
\]
For each fixed c,v, the remaining finite sum over F factors primewise:
\[
 \sum_{F\mid D}\mu(F)\prod_{p\mid F}r_p
                 \prod_{p\mid M_{D/F}(c,v)}r_p
 =\begin{cases}
 \prod_{p\mid D}(1-r_p),&D\mid cv,\\
 0,&D\nmid cv.
 \end{cases}                                                     \tag{3}
\]
At a prime of cv, the local sum is 1-r_p. At a prime not dividing cv, it is r_p-r_p=0. This cancels the unwanted finite inverse product exactly, leaving the previously proved core-flat Mellin row. Inverting the Gaussian proves (2). When (D,m)!=1 the original core row is zero termwise, so the stated external indicator gives the full identity.

All exchanges can also be checked directly after inversion. The absolute majorant from the first term of (1) is
\[
 \frac{C\sqrt U}{q_D}
               \sum_{F\mid D}q_F^{-4}\sum_aq_a^{-5}<\infty.       \tag{4}
\]
This is independent of omega(D); c and v may share primes throughout. Thus (2) is an absolutely convergent physical identity at every positive scale, not just a formal Euler calculation.

### 2. The reflected bound actually transferred

Define the explicit marker factor
\[
 K(D)=\sum_{F\mid D}q_F^{-1}
                       =\prod_{p\mid D}(1+q_p^{-1}).
\]
Then (1)–(2) imply
\[
 \boxed{|B_{D,\mathrm{core}}^\flat(U;m,s)|
 \le C\min\left\{\frac{\sqrt U}{q_D},
                H(m)^{2/3}U^{-1/6}K(D)\right\}.}                  \tag{5}
\]
In particular H(m) may be replaced by C R(m).

To see this without assuming scale covariance, fix F and put D'=D/F, U'=U/q_F^6. The partial inverse transform
\[
 \sum_{(a,D)=1}\mu(a)\kappa(a)q_a^{-2}B_{D'}(U'/q_a^6;m,s)
\]
is estimated by taking absolute values and using (1). The restriction (a,D)=1 can be dropped in this positive upper bound. Exactly the user's optimized split then gives
\[
 C\min\{\sqrt{U'}/q_{D'},\ H(m)^{2/3}(U')^{-1/6}\}.
\]
For clarity, its summands are at most min(A q_a^{-5},B q_a), with A=sqrt(U')/q_D' and B=H(m)sqrt(q_D')/sqrt(U'). Splitting at q_a=(A/B)^{1/6} when that number is >=1, and otherwise using the first bound, proves the displayed estimate for every U'>0.

After multiplication by q_F^{-2}, the two alternatives are
\[
 C\frac{\sqrt U}{q_D}q_F^{-4},\qquad
 C H(m)^{2/3}U^{-1/6}q_F^{-1}.
\]
Summing either alternative over F gives (5). We do not silently replace K(D) by an omega(D)-uniform constant.

For the actual fixed finite slot family, D contains at most K fixed slot primes. Then K(D)<= (3/2)^K, and hence
\[
 |B_{D,\mathrm{core}}^\flat(U;m,s)|
 \ll_{\mathrm{slots}}\min\{\sqrt U/q_D,\ R(m)^{2/3}U^{-1/6}\}.
                                                               \tag{6}
\]
At U=Zq_D this supplies the same reflected scale as the user's original-marked flat estimate, now rigorously for the different core marker. Its original-window pointwise exponent is 13/36-7d/6 when R(m)<=q_m is used. This is a fixed-row estimate: it does not by itself preserve the original full reflected B^J theorem, sum the signed compensation, or prove the missing low linear correlation.
