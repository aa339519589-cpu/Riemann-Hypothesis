# 真实 sextic 字符的非对角 Gram 行平方和

2026-10-11。保持原 primary 生成元、全部非单位零值及真实 sextic 字符。本文以 de Faveri 的六次幂自由大筛为外部输入，证明一个非对角 Gram 估计。它可用于已经准确分离的字符多项式族，尚未把用户的完整 R4 线性配对或完整补偿 Gram 归约到此对象。

## 1. 对象与结论

令 \(\mathcal O=\mathbb Z[\omega]\)，\(q_a=|a|^2\)，固定好素数集合沿用 QRH 原稿。\(\chi_p(n)=(n/p)_6\)，非单位处取零。取固定 \(W\in C_c^\infty((0,\infty))\)，不要求非负。理想指数均使用 primary 生成元。

对好平方自由 \(p,p'\)，\(q_p,q_{p'}\asymp P\)，定义

\[
T_{p,p'}(Z)=\sum_{n\equiv1\ (3)}
W(q_n/Z)\chi_p(n)\overline{\chi_{p'}(n)}.
\tag{1.1}
\]

这里 \(n\) 可有任意素数幂，不限平方自由或六次幂自由。可另加 \((n,S)=1\) 的固定排除；下述界不变，仅固定常数改变。

### 定理 1

对 \(P,Z\ge1\)、每个固定上述 \(p\) 及任意 \(\epsilon>0\)，

\[
\boxed{\sum_{\substack{p'\ne p\ {\rm good,sf}\\q_{p'}\asymp P}}
|T_{p,p'}(Z)|^2
\ll_{\mathcal A,W,\epsilon}(PZ)^\epsilon
\left[ZP+P^2Z^{1/6}+P^{3/2}Z^{2/3}\right].}
\tag{1.2}
\]

任意固定 \(p'\) 子集也满足同界。常数只依赖固定算术数据、环带比较常数及有限个 \(W\) 的光滑半范数；不依赖 \(p\) 或其素因子数。

## 2. 有界系数的任意内频率引理

记

\[
\mathscr S_6(B,J)=B+J+B^{5/6}J^{1/3}+B^{1/3}J^{5/6}.
\]

已核对的外部输入 [F, Theorem 1.1] 是：六次幂自由的好行、列上，原 \(\chi_b(a)\) 的平方算子范数至多
\((BJ)^\eta\mathscr S_6(B,J)\)。它同样适用于转置与整体共轭；原 primary 家族的准确匹配已在此前 `SIXTH_SIEVE_DETECTOR.md` 证明。

### 引理 2

设 \(a_h\) 是独立于 \(b\) 的任意复系数，支撑于 \(0<q_h\le J\)，并满足 \(|a_h|\le A_0\)。则

\[
\boxed{\sum_{\substack{b\ {\rm good,sf}\\q_b\le B}}
\left|\sum_{0<q_h\le J}a_h\chi_b(h)\right|^2
\ll_{\eta,\mathcal A} A_0^2(BJ)^\eta J\mathscr S_6(B,J).}
\tag{2.1}
\]

固定行限制、整体共轭及原字符零值均可保留。若 \(a_h\) 仅有固定 divisor 上界，用任意小幂吸收后同证。

**证明。** 把元素 \(h\) 的理想唯一拆为 \(a\ell^6\)，再拆出 \(a\) 在固定 \(S\) 处的六次幂自由部分及单位。因此有限分层后

\[
h=u s_0 a\ell^6,
\]

其中 \(a\) 为好六次幂自由理想，\(s_0\) 在 \(S\) 处赋值为 \(0,\ldots,5\)。\(\ell\) 可含 \(S\) 的素因子。固定 \(u,s_0,\ell\) 后，

\[
\chi_b(h)=\chi_b(us_0)1_{(b,\ell)=1}\chi_b(a).
\]

前一字符是行标量，互素条件是该固定层的行限制。对 \(a\) 的系数独立于 \(b\)，其平方和至多 \(C A_0^2J/q_\ell^6\)。故外部大筛、Minkowski 给每一层的范数上界为常数乘

\[
A_0(BJ)^\eta\left[
B^{1/2}J^{1/2}q_\ell^{-3}
+Jq_\ell^{-6}
+B^{5/12}J^{2/3}q_\ell^{-4}
+B^{1/6}J^{11/12}q_\ell^{-11/2}\right].
\]

全部 \(\ell\) 级数在理想范数下绝对收敛，因为每个指数大于一。有限 \(u,s_0\) 分层改变常数；平方并减小初始损失即得 (2.1)。

这里使用的是 \(|a_h|\le A_0\) 带来的每层平方质量 \(O(J/q_\ell^6)\)，不是任意 \(\ell^2\) 系数的全频率算子界。因此与此前全频率算子界中不可删的 \(J^{1/6}B\) 项并不冲突。证毕。

## 3. 精确 gcd mask 与有限 Gauss 变换

固定 \(p\)，对 \(p'\ne p\) 写

\[
k=(p,p'),\quad p=ka,\quad p'=kb,
\quad K=q_k.
\]

\(a,b,k\) 两两互素、平方自由，\(q_a,q_b\asymp P/K\)。完整原字符乘积准确为

\[
\chi_p(n)\overline{\chi_{p'}(n)}
=1_{(n,k)=1}\chi_a(n)\overline{\chi_b(n)}.
\]

展开 \(1_{(n,k)=1}=\sum_{m\mid(n,k)}\mu(m)\)，置 \(n=mx\)、\(M=q_m\)。因为所有 \(m\mid k\) 均 primary，原 primary 条件等价于 \(x\equiv1\pmod3\)。新 weight 为 \(W(Mq_x/Z)\)，而额外字符值 \(\chi_a(m)\overline{\chi_b(m)}\) 是模一的行标量，不能误写成固定公共常数，但可在每个行平方中保留或取绝对值。

对 \(x\) 的乘积字符

\[
\psi_{a,b}(x)=\chi_a(x)\overline{\chi_b(x)}
\]

作为有限剩余字符在 \(ab\) 上是 primitive：在每个素因子处的指数为 \(+1\) 或 \(-1\)，均非主。它非主，因为唯一可能的主情形 \(a=b=1\) 会给 \(p=p'\)，已排除。

对 primary 格点模 \(3ab\) 作二维 Poisson。零频率因非主性而消失。primitive Gauss 和的模长是 \(\sqrt{q_aq_b}\)，所以变换的幅度与自然双频长度分别为

\[
\mathcal A_0\asymp\frac{Z}{M\sqrt{q_aq_b}}
\asymp\frac{ZK}{MP},
\qquad
J_0\asymp\frac{q_aq_bM}{Z}
\asymp\frac{P^2M}{K^2Z}.
\tag{3.1}
\]

保留而不删改 Gauss/CRT 相位后，频率字符是
\(\overline{\chi_a(h)}\chi_b(h)\)。\(\overline{\chi_a(h)}\) 是独立于变化行 \(b\) 的系数，包括它在非单位处的零。primary 条件只增加固定模数的频率相位和依赖 \(b\) 的标量。

更具体地，使用 trace Fourier 约定并写 \(\lambda=\sqrt{-3}\)，将 primary 剩余类写为 \(x=ab+3t\)。完整有限 Fourier 系数含

\[
e\!\left(\operatorname{Tr}\frac h{3\lambda}\right)
\psi_{a,b}(3\lambda)\overline{\psi_{a,b}(h)}\,
g(\psi_{a,b}).
\tag{3.2}
\]

**这里不把 \(\psi_{a,b}(3\lambda)\) 换成一。** 这在 cubic 情况可以利用 \(3\lambda\) 为 cube 简化，在当前 sextic 情况一般不能。它与完整 Gauss 相位一样，只是该 \(b\) 的模一标量，独立于双频 \(h\)，故不损害下一节的固定系数条件。

## 4. 双频 dyad 与四项求和

在 \(q_h\asymp J\ge1\) 的 dyad 上，变换 weight 的剩余 \(b\) 依赖仅通过 \(q_b\)，因为原 weight 是径向的。对紧区间上的比例 \(q_h/J\)、\(q_b/(P/K)\) 作 Mellin 光滑分离。对每个固定分离参数，\(h\)-系数独立于 \(b\)，且绝对值有共同上界。共同积分主函数快速下降；对每个固定 \(A>0\)，其质量可界为

\[
C_{A,W}(1+J/J_0)^{-A}.
\]

该下降来自固定有限次平面 Fourier 与对数 Mellin 分部积分；若需平方后的指数 \(A\)，先取更大阶数即可。norm 比例的额外幂和 \(b\) 的 Gauss 标量是有界行乘子。由引理 2 及 Minkowski 可估计固定 \(k,m\) 的此 dyad 在 \(b\) 上的平方和。

筛中的 \(J^\eta\) 损失也由同一快速下降吸收：\(M\le K\)、\(Z\ge1\) 给 \(J_0\ll P^2\)，而 \(P/K\ll P\)，故余下小幂可统一写为 \((PZ)^\epsilon\)，在开始时缩小 \(\eta\)。准确的 dyad 界是

\[
C(PZ)^\epsilon
\left(\frac{ZK}{MP}\right)^2
J\left[\frac PK+J+
\left(\frac PK\right)^{5/6}J^{1/3}+
\left(\frac PK\right)^{1/3}J^{5/6}\right]
(1+J/J_0)^{-A}.
\tag{4.1}
\]

原 \(b\) 的互素与环带限制均是固定的正外和限制，允许扩大到 \(q_b\ll P/K\)。没有扩大任何内列和后宣称单调。

对双频 dyads 使用 Minkowski，并保留快速下降；各个正幂对应的 dyadic 范数和由 \(J_0\) 的同次幂控制，因而平方后仍得到下列四项（不是不合法地直接把不同 dyad 平方和相加）：

\[
\frac{ZP}{MK},\qquad
\frac{P^2}{K^2},\qquad
\frac{Z^{2/3}P^{3/2}}{M^{2/3}K^{3/2}},\qquad
\frac{Z^{1/6}P^2}{M^{1/6}K^2}.
\tag{4.2}
\]

若 \(J_0<1\)，全部非零频率都在尾区；同样结论由快速下降成立。由于 \(Z,K,M\ge1\)，(4.2) 的总和至多常数乘

\[
ZP+P^{3/2}Z^{2/3}+P^2Z^{1/6}.
\]

最后 \(k\mid p\)、\(m\mid k\) 只有 divisor 数量。对原 Möbius 和作 Cauchy，重新选择任意小损失后全部吸入 \((PZ)^\epsilon\)。这证明 (1.2)。加 \((n,S)=1\) 时仅多固定素数集的有限 Möbius 拆分，重新缩放 \(Z\) 的固定倍数，不改量级。证毕。

## 5. 使用范围

若写 \(Z=P^z\)，本上界的 exponent 为

\[
\max\{1+z,\ 2+z/6,\ 3/2+2z/3\}.
\]

例如 \(1<z<3/2\) 时为 \(3/2+2z/3\)。这是保留原 sextic 相位的实际非对角上界，不是用零点位置假设得到的一般函数论界。

它不允许任意 row-dependent 系数，不控制未经准确分离的 \((s,m,c,n,D)\) 全耦合核，也不能把先前只对 cubic 的 corrected dispersion 不加核对地改成 sextic。完整 R4 还须给出其真实线性配对到可用核的准确归约，以及相应长度与公共系数；定理 1 单独不提供额外 \(3/8\) 次幂节省。

## 固定来源

[F] Alexandre de Faveri, [*Optimal large sieve for fixed order characters*, arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1), Theorem 1.1。引用其六次幂自由大筛，未独立重证外部定理。

[Q] `openai/math`, [固定 `fd4aeeb2` 的 QRH 原稿](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，primary 与 sextic 零延拓约定。

[C] `openai/math`, [固定 `adc7f124` 的 cubic first-moment 稿 `dual.tex`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dual.tex)，`lem:character-gram` 提供 gcd–Poisson–Gram 组织方式。本文重新写出 sextic 场景的局部相位、全内频率证明与不同幂次；没有引用该稿的 corrected dispersion 作为本定理输入。
