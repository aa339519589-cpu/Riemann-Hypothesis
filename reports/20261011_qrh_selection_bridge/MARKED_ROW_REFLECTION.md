# 完整标记行的反射界与无素因子数损失的标记合并

本稿使用固定来源 [Q] 的 completed cubic reflection，针对原完整物理行
\(\mathcal B_D(U;m,s)\)，保持全部字符、共同素数和非单位零值。
本文给出一个经逐式复核的完整行点态界及原标记去卷积推论。
整体相关目标仍未证明。

## 1. 对象与定理

采用 [B] 的原定义

\[
\mathcal B_D(U;m,s)=\sum_{c\,\mathrm{sf},n}
\gamma_2(c)\overline{\alpha(cn^3)}\eta(cn^3)\Xi_*(cn^3)^{-1}
\mathcal R(cn^3,s)\chi_{cn^3}(m)\overline{G(cn^3)}
1_{D\mid cn^3}q_c^{-1/2}q_n^{-1}W_G(q_cq_n^3/U).
\tag{1}
\]

这里 \(U>0\)，\(m\ne0\)，\(D\) 是好平方自由理想，\(s\) 是原允许行参数；
\(c,n\) 均避开固定坏素数集 \(S\)，可以共享素因子。\(\alpha(a)=a/|a|\)
是角向因子，\(q_a\) 是范数。\(W_G(y)=(2\sqrt\pi)^{-1}e^{-(\log y)^2/4}\)。
\(G\)、\(\mathcal R\) 和原有限字符保持不变。

写 \(m=u m_S\prod_{p\notin S}p^{v_p(m)}\)，定义

\[
R(m)=\prod_{\substack{p\notin S\\v_p(m)>0}}q_p,
\qquad j_p=v_p(m)\pmod6,
\tag{2}
\]

\[
H(m)=\prod_{j_p\ne0,4}q_p\,
\prod_{j_p=4}3\sqrt{q_p}\,
\prod_{j_p=0}(1-q_p^{-1}+\sqrt{q_p}).
\tag{3}
\]

所有乘积只遍历 \(v_p(m)>0\) 的好素数。定理为

\[
\boxed{|\mathcal B_D(U;m,s)|\le C\frac{H(m)\sqrt{q_D}}{\sqrt U}
\le C'\frac{R(m)\sqrt{q_D}}{\sqrt U}.}
\tag{4}
\]

常数只依固定算术数据、格子和 Gaussian，独立于 \(U,m,s,D\) 及
\(\omega(D),\omega(m)\)。与已证的 [B] 合起来，将给出

\[
|\mathcal B_D(U;m,s)|\le C\min\left\{
\frac{\sqrt U}{q_D},\frac{R(m)\sqrt{q_D}}{\sqrt U}\right\}.
\tag{5}
\]

当 \((D,m)\ne1\) 时，原行逐项为零；以下只需处理 \((D,m)=1\)。

## 2. 固定来源的反射输入与实际行匹配

\(\overline{G(A)}\) 按原有限 ray 群 \(T\) 展开为
\(\sum_{\theta\in\widehat T}a_\theta\theta(A)\)，其系数绝对值和至多
\(\sqrt{|T|}\)。其余固定行相位与 \(\chi_A(m)\) 用 [Q] 的
`lem:reflection-row-sectors` 分解。单位、坏素数赋值模六和固定 ray 类
只有有限种，故得到一个固定的 \(\Psi_0\) 有限家族及一个公共坏模数 \(L\)。
所有移动好素数均留在局部集合中，指数是 \(j_p\)，包括保留非单位零值的
\(j_p=0\)。没有将 \(G\) 本身擅自当作乘法字符。

对每个固定 ray Fourier 分量，completed reflection 的项由
\(h_0\bmod L\) 和激活素数子集确定。若激活乘积为 \(r\)，它们有

\[
c=c_Fr,\qquad |\zeta|\le1/81,
\qquad
\zeta\sum_{\mu\ne0}\frac{d(\mu)\alpha(\mu)\vartheta(\lambda^4\mu)}{\sqrt{q_\mu}}
\prod_{p\,\mathrm{active}}B_p(\lambda^4\mu)
V^\sharp(q_\mu U/q_c^2).
\tag{6}
\]

\(c_F\) 属固定有限集，\(d\) 属三个固定 cusp 系数函数，\(\vartheta\)
的模数固定。局部列为

\[
B_p(x)=\begin{cases}
\chi_p(x)^{-j_p-2},&j_p\ne0,4,\\
q_p^{-1/2}(-1+q_p1_{p\mid x}),&j_p=4,\\
q_p^{-1/2}\chi_p(x)^{-2},&j_p=0\text{ 且激活}.
\end{cases}
\tag{7}
\]

所有 \(j_p\ne0\) 强制激活，\(j_p=0\) 有激活或未激活两个分支。
未激活分支的唯一额外因子是 \(1-q_p^{-1}\)。[Q] 明确保证：向局部集合
加入一个未激活的零指数素数时，\(c_F,c,d,\vartheta,\kappa_F\)、其他激活
素数数据和整个核均与该素数缺席时相同；这对所有 \(h_0\) 成立。
下节必须用这条同时兼容性，不能只用分支数上界。

固定来源证明中，\(T(s,\Psi)=D(s,\Psi)L_0(s,\Psi)\) 的 Mellin 表达式来自
\(\partial_{\bar z}\) 作用于三维双曲空间 theta 函数的水平坐标。
每个 cusp 的常数项与水平坐标无关，故导数将其消去。实际行的
\(\overline{\alpha(cn^3)}\) 正是此导数产生的角向权重；它不同于不含角向
权的 cubic Gauss 平均。移线对象是完整乘积 \(T\)，而非分别宣称
\(D,L_0\) 整；[Q] 对该乘积证明了整延拓和多项式条带增长，因此 (6)
没有遗漏零频 main term 或留数。整延拓的中间增长常数可以依赖移动
局部集合；本稿最终估计仅使用 (6)–(7) 的统一显式数据、cusp 系数界
和核界，不使用这些中间常数作为统一常数。

## 3. 标记的未激活分支先合并

由 \((D,m)=1\)，\(D\) 与原移动素数集合不交。准确展开

\[
1_{D\mid A}=\sum_{D'\mid D}(-1)^{\omega(D')}1_{(A,D')=1}.
\tag{8}
\]

对每个 \(D'\)，将其素数作为零指数局部素数加入反射。先固定原 \(m\)
素数的一个分支及 \(h_0\)，再固定标记中激活的子积 \(E\mid D\)。
所有能产生这个激活集合的 \(D'\) 唯一写为 \(E F\)，\(F\mid D/E\)，
其中 \(F\) 的素数未激活。由上述兼容性，这些项除了标量外完全相同。
故在取绝对值之前可以精确求和其标量：

\[
\sum_{F\mid D/E}(-1)^{\omega(EF)}\prod_{p\mid F}(1-q_p^{-1})
=\frac{(-1)^{\omega(E)}}{q_{D/E}}.
\tag{9}
\]

这里每个素数的因子是 \(1-(1-q_p^{-1})=q_p^{-1}\)。
每个分支中，原 \(m\) 素数的激活乘积记为 \(r_m\)；它包含强制激活素数
及该分支已激活的原零指数素数，并非在所有分支中取整个根基。
新的激活乘积为 \(r_mE\)，双边尺度为

\[
L_E=\frac{q_{c_F}^2q_{r_m}^2q_E^2}{U}.
\tag{10}
\]

标记激活列还给 \(q_E^{-1/2}\prod_{p\mid E}\chi_p(\lambda^4\mu)^{-2}\)。
其模长至多 \(q_E^{-1/2}\)，零值保持原样。不能在 (8) 的层面先取绝对值，
否则会失去 (9)。

## 4. 全部 cusp 系数的整除密度

固定来源给出唯一的支持表示
\(\mu=u\lambda^k n b^3\)，\(k\ge-4\)，\(n\) 平方自由，\(n,b\) primary，
可以共享素数，并满足

\[
\frac{|d(\mu)|}{\sqrt{q_\mu}}\le
27\,3^{-k/3}q_n^{-1/2}q_b^{-1}.
\tag{11}
\]

对于任意好平方自由 \(F\)，由格点计数证明

\[
\sum_{\substack{M\le q_\mu<2M\\F\mid\mu}}
\frac{|d(\mu)|}{\sqrt{q_\mu}}
\le C\,\frac{2^{\omega(F)}}{q_F}\sqrt M.
\tag{12}
\]

证明如下。把每个 \(p\mid F\) 分配给被它整除的 \(n\) 或 \(b\)，得到
\(F=F_1F_2\)，\(F_1\mid n,F_2\mid b\)；共享素数可分给任一变量，
重复计数只增大上界。一共有 \(2^{\omega(F)}\) 个这样的分配。
固定 \(k\) 与 \(q_b\asymp B=2^j\)，令 \(N=M/(3^kB^3)\)。
实际 \(q_n\) 位于与 \(N\) 双向可比的区间。主理想格点计数在可解
dyad 上给出

\[
\sum_{q_n\asymp N,F_1\mid n}q_n^{-1/2}\le C N^{1/2}/q_{F_1},
\quad
\sum_{q_b\asymp B,F_2\mid b}q_b^{-1}\le C/q_{F_2}.
\tag{13}
\]

其理由是 \(a=F_i a'\) 将理想范数缩放 \(q_{F_i}\)，而理想计数为
\(O(T)\)；当 dyad 小于必要的最小范数时没有项。所有这些常数独立于
\(F_i\) 的素因子数。于是每个 \((k,B,F_1,F_2)\) 的贡献至多

\[
C\sqrt M\,3^{-5k/6}B^{-3/2}/q_F.
\tag{14}
\]

对 \(k\ge-4\)、\(j\ge0\) 求和收敛，再求和分配，得 (12)。\(F=1\)
特别给出不含任何 \(M^\epsilon\) 的 \(C\sqrt M\) 界。

令 \(J_4\) 是原 \(m\) 素数中 \(j_p=4\) 的乘积。取 (7) 的 Ramanujan
列绝对值并展开，(12) 给出

\[
\sum_{M\le q_\mu<2M}\frac{|d(\mu)|}{\sqrt{q_\mu}}
\prod_{p\mid J_4}|B_p(\lambda^4\mu)|
\le C\sqrt M\frac1{\sqrt{q_{J_4}}}
\sum_{F\mid J_4}2^{\omega(F)}
= C\sqrt M\frac{3^{\omega(J_4)}}{\sqrt{q_{J_4}}}.
\tag{15}
\]

因为所有这些素数避开 \(\lambda\)，\(p\mid\lambda^4\mu\) 与
\(p\mid\mu\) 等价。其余原非零指数列模长至多一；原激活零指数列的
\(q_p^{-1/2}\) 单独保留。

## 5. 任意正双边尺度与局部因子总和

Gaussian 的反射核对任意固定 \(A>1/2\) 有

\[
|V^\sharp(x)|\le C_A\min(x^{1/4},x^{-A}).
\tag{16}
\]

将 cusp dyad 延伸为所有整数尺度只扩大正上界。对任意 \(L>0\)，

\[
\sum_{j\in\mathbb Z}2^{j/2}
\min\{(2^j/L)^{1/4},(2^j/L)^{-A}\}\le C_A\sqrt L.
\tag{17}
\]

写 \(L=2^{h+\theta}\)，\(0\le\theta<1\)，在 \(j\le h\) 和 \(j>h\)
分别是比例 \(2^{3/4}\) 与 \(2^{1/2-A}\) 的收敛几何级数，常数与
\(L\) 无关。这覆盖小于一的 \(L\)，无需加入 \(1+L\)。实际 cusp 支持
还满足 \(q_\mu\ge3^{-4}\)，不存在逼近零的无穷项。

固定原 \(m\) 分支，结合 (9)、(10)、(15)、(17)，标记子积 \(E\) 的
贡献至多一个固定常数乘

\[
\frac1{q_{D/E}}\frac1{\sqrt{q_E}}
\frac{3^{\omega(J_4)}}{\sqrt{q_{J_4}}}
\prod_{\substack{p\mid m\\j_p=0\text{ active}}}q_p^{-1/2}
\prod_{\substack{p\mid m\\j_p=0\text{ inactive}}}(1-q_p^{-1})
\frac{q_{r_m}q_E}{\sqrt U}.
\tag{18}
\]

\(q_{c_F}\) 由固定常数吸收。求和 \(E\mid D\) 时准确有

\[
\sum_{E\mid D}\frac{\sqrt{q_E}}{q_{D/E}}
=\sqrt{q_D}\sum_{F\mid D}q_F^{-3/2}
\le C\sqrt{q_D}.
\tag{19}
\]

右侧常数来自所有理想的范数 \(-3/2\) 次幂和收敛，独立于
\(\omega(D)\)。对于原 \(m\) 的强制激活素数，\(q_{r_m}\) 给 \(q_p\)；
若 \(j_p=4\)，与 (15) 合并给 \(3\sqrt{q_p}\)。若 \(j_p=0\)，其两个
分支相加恰给 \(1-q_p^{-1}+\sqrt{q_p}\)。其他 moving 标量的模长一，
不产生分支数损失。有限 \(h_0\) 与固定 ray Fourier 分量最后求和，
即得 (4) 的第一式。

为第二式，\(3\sqrt{q_p}\le q_p\) 当 \(q_p\ge9\)；范数小于九的素理想
只有有限多个，其所有超额乘积可由一个固定常数控制。零指数的
\(1-q_p^{-1}+\sqrt{q_p}\le q_p\) 对 \(q_p\ge3\) 成立。好素数避开二、三
上方的素理想，特别满足这个范围。因此 \(H(m)\le C R(m)\)。

## 6. 原尺度与整体相关目标

在 \(U=Zq_D\) 上，(4) 给

\[
|\mathcal B_D(Zq_D;m,s)|\le C R(m)/\sqrt Z\le C q_m/\sqrt Z.
\tag{20}
\]

在原 \(q_m\asymp Z^{5/6-2d}\)、\(q_D\asymp Z^{1/6-d}\) 尺度，其一般
点态指数不超过 \(1/3-2d\)，相对于 [B] 的 \(5/12+d/2\) 行界省
\(1/12+5d/2\)。这包括 \(d=0\)，不是只在正 \(d\) 上的改进。

但 \(\mathcal B_D\) 是一个固定标记的原始完整行，\(B_m^J\) 还包含
原 slot 素数组之和，\(S_J\) 还包含 \(m\)、加性 Gauss 权与归一化因子。
原 R2 已有不同对象 \(\sum_m|B_m^J|^2\ll Z^{5/6-2d+\epsilon}\)。
仅作绝对标记求和时，\(#D\ll Z^{1/6-d}\)，(20) 给出的
\(\sum_m|B_m^J|^2\) 指数为 \(11/6-8d\)，比既有 R2 大
\(1-6d\ge0\)。不能把 (20) 的逐行改进当作 R2 的改进，更不能
省略标记和再宣称 R4
的 \(Z^{11/48-d/2+\epsilon}\) 成立。整体线性相关和高端仍需新的证明。

## 7. 原标记的 Euler 去卷积推论

定义 \(\kappa(a)=\eta(a)^6\overline{\alpha(a)}^6\)，并仅对同一个原标记
\(D\mid cn^3\) 定义 [E] 的物理尺度变换

\[
\mathcal B_D^\flat(U;m,s)=
\sum_{a\,\mathrm{good}}\frac{\mu(a)\kappa(a)}{q_a^2}
\mathcal B_D(U/q_a^6;m,s).
\tag{21}
\]

这里 \(\mu(a)\) 是 Möbius 系数，不能与反射变量 \(\mu\) 混淆。
\(\kappa\) 是单位值的固定 Hecke 角向字符。由 [B]，该级数绝对收敛：
每项绝对值至多 \(C\sqrt U/(q_Dq_a^5)\)。没有插入 \(\chi_a(m)\)，
也没有把原标记改为 sextic core 标记。

(5) 给出下面的全尺度推论：

\[
\boxed{|\mathcal B_D^\flat(U;m,s)|\le C
\min\left\{\frac{\sqrt U}{q_D},R(m)^{2/3}U^{-1/6}\right\}.}
\tag{22}
\]

**证明。** 置 \(A=\sqrt U/q_D\)、\(B=R(m)\sqrt{q_D}/\sqrt U\)。
将 (5) 代入 (21)，变换后每项至多
\(C\min(Aq_a^{-5},Bq_a)\)。对任意 \(T\ge1\)，理想计数给

\[
\sum_{q_a\le T}q_a\le CT^2,\qquad
\sum_{q_a>T}q_a^{-5}\le CT^{-4}.
\tag{23}
\]

故分割后总和至多 \(C(BT^2+AT^{-4})\)。当 \(A/B\ge1\)，取
\(T=(A/B)^{1/6}\)，两项均等于
\(A^{1/3}B^{2/3}=R(m)^{2/3}U^{-1/6}\)；全部 \(q_D\) 幂消去。
此时也可用原正项界 \(CA\)。当 \(A/B<1\) 时，第二个候选量大于
\(A\)，直接用 \(CA\)。两种情况给出 (22)。证毕。

在 \(U=Zq_D\) 上，第二项是
\(R(m)^{2/3}Z^{-1/6}q_D^{-1/6}\)。在原 \(q_m\)、\(q_D\) 窗口，用
\(R(m)\le q_m\) 得到点态指数 \(13/36-7d/6\)。这个推论与 [E] 的
原标记尺度变换相容；它不涵盖 [E] 另行定义的 core 标记，也没有估计
变换后探针的完整低端线性相关或全部非主高端行。

## 8. 来源

[Q] `openai/math` 固定提交
[`fd4aeeb2` 的 paper.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)：
`prop:completed-reflection` 第 1676–2471 行，特别是 (7) 的局部列、
同时分支兼容性、cusp 支持与系数、核界和完整 Mellin 移线证明；
`lem:reflection-row-sectors` 第 2472–2545 行；`eq:general-probe` 的原行与
有限 ray Fourier 展开。这里的反射输入不调用 7/8 零点排除定理。

[B] [已证的原始标记行绝对界](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/reports/20261011_qrh_selection_bridge/MARKED_ROW_BOUND.md)。

[C] [准确补偿与零支撑](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/COMPENSATION.md)。

[E] [Euler 去卷积的物理定义](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/dfc211e29c3ac231ada82a640601753c9a119695/reports/20261011_qrh_selection_bridge/EULER_DECOMPLETION.md)，
Part I 第 3 节的 \(\mathcal B_D^\flat\) 与原标记区别。推论 (22) 的
平衡分割证明是本稿的新推导。

本稿新增步骤是 (9) 的分支先合并、(12) 的无小幂整除密度、(17) 的
全正尺度核求和、(18)–(19) 的标记/原行素数分别求和及 (22) 的优化分割。
独立数学核验见 `REFEREE_MARKED_ROW_REFLECTION.md`。
`check_gram_geometry.py` 只复算有限未激活标量恒等式、范数幂、
去卷积平衡幂及点态/整体指数的区别；不认证反射输入或无限相关抵消。
本文没有证明 RH。
