# 7/8 输入与完整选择方程：指数尾、Mellin 商及临界探针的相关估计

## 1. 对象、输入与结论范围

采用 Fourier 约定 \(\widehat f(z)=\int_{\mathbb R}f(x)e^{izx}\,dx\)，并置

\[
\Xi(z)=\xi(1/2+iz),\qquad h(x)=\cosh(x/2),\qquad
m(x)^2=\frac{\Phi(x)}{2h(x)},\qquad M=\widehat{m^2},
\]

其中 \(\Phi\) 是完整、正、偶的 theta 核，\(\widehat\Phi=\Xi\)。具体归一化为

\[
\Phi(x)=\sum_{n\ge1}
(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})e^{-\pi n^2e^{2x}}.
\]

本文使用两个明确的引用输入。

**选择输入 S。** 对 [S] 的真实实偶亚临界本征态
\(Lq=\lambda q\)、\(0<\lambda<1/2\)，令
\(\varepsilon=1/2-\lambda\)、\(g=2hq\)、\(f=\Phi q=m^2g\)。
记 \(\mathcal Z\) 为 \(\Xi\) 的全部不同零点，\(n_w\) 为重数，
\(a_w=\widehat f(w)\)。继承的完整关系为

\[
\varepsilon g(x)=-\sum_{w\in\mathcal Z}n_wa_we^{-iwx},
\qquad
\varepsilon a_z+\sum_{w\in\mathcal Z}n_wM(z-w)a_w=0
\quad(z\in\mathcal Z),                                      \tag{S1}
\]

\[
a_{-w}=a_w,\qquad a_{\bar w}=\overline{a_w},\qquad
\sum_{w\in\mathcal Z}n_w\langle\Re w\rangle^N|a_w|<\infty
\quad(N=0,1,2,\ldots).                                      \tag{S2}
\]

最后的求和式由 [S] 的任意幂次点态衰减和零点计数推出。
[S] 还给出真实本征态的 Weil 恒等式

\[
Q(f)=-\varepsilon\int_{\mathbb R}m^2|g|^2\,dx<0.              \tag{S3}
\]

这里使用完整无限方程和真实算子定义域；有限零点压缩不替代这些条件。

**条带输入 Q。** 引用 [Q] 的 \(7/8\) 定理，因而对 zeta 的非平凡零点
\(\rho=\beta+i\gamma\)，有 \(1/8\le\beta\le7/8\)。在本稿的谱平面中，

\[
w=\gamma+i(1/2-\beta),\qquad |\Im w|\le3/8.                 \tag{Q}
\]

下文证明由这些输入推出的全阶指数尾、准确增长阶和 Mellin 商界；
另给出 [Q] 固定探针达到临界低端估计所需的一个充分相关估计。
输入 Q 在本文中作为外部定理引用；相关估计 (R4) 与排谱目标 (T) 尚未证明。

## 2. 无对数损失的全阶指数尾

**命题 1。** 若 \(\mathcal Z\subset\{w:|\Im w|\le a\}\)，其中
\(a<1/2\)，且 (S1)–(S2) 成立，则对每个整数 \(j\ge0\)，

\[
|g^{(j)}(x)|\le C_j e^{a|x|},\qquad
|q^{(j)}(x)|\le C'_j e^{-(1/2-a)|x|}.                        \tag{1}
\]

常数可依赖 \(q,j,\varepsilon\)，不声称在 \(\varepsilon\downarrow0\) 时一致。

**证明。** (S2) 和虚部有界给出
\(C_j=\varepsilon^{-1}\sum n_w|a_w||w|^j<\infty\)。
展开及各固定阶导数在紧实区间绝对一致收敛，逐项微分后用
\(|e^{-iwx}|\le e^{a|x|}\)，得到第一式。

对 \(x\ge0\)，置

\[
r(x)=\frac1{2h(x)}=\frac{e^{-x/2}}{1+e^{-x}}.
\]

每个固定阶导数均满足 \(|r^{(k)}(x)|\le D_ke^{-x/2}\)：
令 \(t=e^{-x}\in[0,1]\)，反复使用 \(\partial_x=-t\partial_t\) 即得。
偶性给出负半轴的同一界。对 \(q=rg\) 用 Leibniz 公式即得第二式。证毕。

由输入 Q，

\[
\boxed{|q^{(j)}(x)|\le C'_j e^{-|x|/8}\quad(j\ge0).}         \tag{2}
\]

端点 \(a=3/8\) 包含在内，指数无需减去任意小正数。
因此 \(\widehat q\) 在 \(|\Im z|<1/8\) 全纯，并在每个闭子条带上
对 \(\Re z\) 任意幂次衰减；分别由指数可积性和反复分部积分得到。
这没有断言空间函数 \(q(x)\) 自身可复解析延拓。

[S] 已有准 RH 与本征态尾部的关系。本命题利用后来建立的全零点展开，
去掉多项式尾损失并同时控制所有固定阶导数。

## 3. 活动零点的上确界等于准确增长阶

对非零真实低态，定义

\[
\mathcal Z_q=\{w\in\mathcal Z:a_w\ne0\},\qquad
\alpha(q)=\sup_{w\in\mathcal Z_q}\Im w
          =\sup_{w\in\mathcal Z_q}|\Im w|.
\]

第二个等号来自共轭对称。不假定上确界达到。对右半轴函数定义

\[
\tau(u)=\inf\{b\in\mathbb R:\ |u(x)|\le Ce^{bx}\ (x\ge0)
\text{ 对某个有限 }C\text{ 成立}\}.
\]

**命题 2。** 在 S、Q 下，每个非零真实低态满足

\[
0<\alpha(q)\le3/8,\qquad
\boxed{\tau(g)=\alpha(q),\qquad\tau(q)=\alpha(q)-1/2.}       \tag{3}
\]

**证明。** 如果所有离轴系数都为零，实偶 Weil 表达式只剩
\(Q(f)=\sum_{\gamma\in\mathcal Z\cap\mathbb R}n_\gamma a_\gamma^2\ge0\)，
与 (S3) 矛盾。所以有活动离轴点，共轭对称给 \(\alpha(q)>0\)；
上界来自 Q。

由 (S1)–(S2)，对 \(x\ge0\) 有
\(|g(x)|\le\varepsilon^{-1}\sum n_w|a_w|e^{\alpha(q)x}\)，
故 \(\tau(g)\le\alpha(q)\)。另一方面，[S] 的 Laplace 身份为

\[
\mathcal C_g(s)=\int_0^\infty e^{-sx}g(x)\,dx
=-\varepsilon^{-1}\sum_{w\in\mathcal Z}\frac{n_wa_w}{s+iw},
\qquad \Re s>1/2.                                         \tag{4}
\]

右端在避开离散极点的紧集正规收敛：高频项以常数乘
\(|a_w|/|\Re w|\) 控制，低频项只有有限个。于是每个活动点给出
不可去的简单极点 \(s=-iw\)，其留数为 \(-n_wa_w/\varepsilon\ne0\)。
不同点不能相互消去留数，重数已合并为 \(n_w\)。

若 \(|g(x)|\le Ce^{bx}\) 对某个 \(b<\alpha(q)\) 成立，原始积分在
\(\Re s>b\) 全纯。上确界的定义给出活动点 \(w\) 满足
\(\Im w>b\)。由亚纯函数的唯一延拓，积分须与 (4) 一致，却在
该半平面遇到不可去极点，矛盾。因此 \(\tau(g)=\alpha(q)\)。

最后，\(1\le1+e^{-x}\le2\) 给
\(q=e^{-x/2}g/(1+e^{-x})\) 的指数阶恰好平移 \(-1/2\)。证毕。

极点机制继承自 [S]；这里补全准确的上下界及不要求上确界达到的表述。
它也具体指出一个足够的、目前未证的排谱目标：对每个非零真实低态，证明

\[
\exists\eta_q>0:\quad
|2h(x)q(x)|\le C_qe^{(\alpha(q)-\eta_q)x}\quad(x\ge0).       \tag{T}
\]

这将与 (3) 矛盾。\(\eta_q\) 无须对全部低态一致。
另一充分目标是对每个 \(\eta>0\) 得到
\(q(x)=O_{q,\eta}(e^{-(1/2-\eta)x})\)。
单独把 (2) 改善到某个固定衰减率 \(c<1/2\)，仍允许
\(0<\alpha(q)\le1/2-c\)，所以尚不足以排除全部低态。

## 4. 从指数尾到归一化 Mellin 商的幂次界

置

\[
\mathcal Mf(s)=\int_{\mathbb R}f(x)e^{(s-1/2)x}\,dx,\qquad
G(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad
D_f(s)=\frac{\mathcal Mf(s)}{G(s)}.
\]

完整 theta 身份为 \(\mathcal M\Phi(s)=\xi(s)=G(s)\zeta(s)\)。

**命题 3。** 设 \(|q(x)|\le A e^{-c|x|}\)，其中 \(c>0\)，\(f=\Phi q\)。
则对实 \(\sigma>1+c\)，有明确的比较式

\[
\boxed{|D_f(\sigma)|\le A\frac{\xi(\sigma-c)}{G(\sigma)}
=A\pi^{c/2}\frac{(\sigma-c)(\sigma-c-1)}{\sigma(\sigma-1)}
\frac{\Gamma((\sigma-c)/2)}{\Gamma(\sigma/2)}\zeta(\sigma-c).} \tag{5}
\]

特别地，\(D_f(\sigma)=O_{q,c}(\sigma^{-c/2})\)。

**证明。** 对每个实 \(x\)，有 \(e^{-c|x|}\le e^{-cx}\)。由 \(\Phi>0\)，

\[
|\mathcal M(\Phi q)(\sigma)|
\le A\int_{\mathbb R}\Phi(x)e^{(\sigma-c-1/2)x}\,dx
=A\xi(\sigma-c).
\]

除以正数 \(G(\sigma)\) 即得 (5)。固定 \(c\) 时，Stirling 公式给
\(\Gamma((\sigma-c)/2)/\Gamma(\sigma/2)\sim(\sigma/2)^{-c/2}\)，
另有 \(\zeta(\sigma-c)\to1\)，故 (5) 的右侧渐近于
\(A(2\pi)^{c/2}\sigma^{-c/2}\)。证毕。Gamma 渐近来源见 [G]。

把命题 1 应用于活动点集本身，可取 \(c=1/2-\alpha(q)\)。因此

\[
\boxed{D_{\Phi q}(\sigma)=O_q(\sigma^{-1/4+\alpha(q)/2})
       =O_q(\sigma^{-1/16})\quad(\sigma\to+\infty).}          \tag{6}
\]

后一界使用 Q。它加强了 [D] 的实射线衰减，并给出更直接的正核比较证明。
这是实 \(\sigma\) 的结论；没有建立整个右半平面的普通绝对 Dirichlet
级数表示。[D] 已证明，这种表示对非零偶、零极点矩的源本身不可能，
不能把 (6) 升格为未经证明的本征源保类性质。

## 5. 固定准 RH 探针与临界低端目标

以下独立讨论 [Q] 第二阶段的原探针。该节的 \(h\) 是尺度指数，
与前面的函数 \(h(x)\) 无关。其固定参数为

\[
b=\tfrac18,\quad h=\tfrac{13}{16},\quad\ell=\tfrac16,\quad
l_x=\tfrac{17}{48},\quad l_y=\tfrac{23}{48},\quad M=\tfrac56.
\]

[Q] 的 `prop:probe-low` 与 `eq:part-II-mellin-target` 给出

\[
|J_\eta(Z)|\ll_\epsilon Z^{3/16+\epsilon},\qquad
C(s)=l_x/2+s-1+h/6=s-11/16.                                \tag{7}
\]

从原探针到 \(J_\eta\) 的固定次对数归一化吸收到任意小 \(\epsilon>0\) 中。
因为 \(C(7/8)=3/16\)、\(C(1/2)=-3/16\)，在此固定构造下，一个临界
低端目标为

\[
\forall\epsilon>0:\qquad |J_\eta(Z)|\ll_{\eta,\epsilon}
Z^{-3/16+\epsilon}.                                        \tag{8}
\]

与 (7) 相比，需要额外 \(3/8\) 次幂节省。

(8) 单独仍不闭合延拓判据。对每个 \(\sigma_0>1/2\) 及反设
\(\beta_*>\sigma_0\)，还须为同一探针建立

\[
|J_\eta(Z)-f_\eta(Z)|\ll_\eta Z^{C(\beta_*)-\delta},
\qquad\delta>0,                                           \tag{9}
\]

以及 [Q] `lem:continuation-criterion` 的全纯乘子条件
\(\sup_{\Re s>\sigma_0}|H_\eta(s)-1|\le1/2\)。
\(f_\eta\) 是该命题的同一个 Mellin 信号；\(\beta_*\) 是所有原始有限阶
Hecke 目标的零点实部上确界。节省 \(\delta\) 和该判据的低端余量须可
对目标字符一致选择，隐含常数与起始阈值可依目标。

[Q] 原高端封闭在 \(\beta_*>7/8\)、\(\kappa=2\beta_*-1\ge3/4\) 的范围内
证明。推进至任意 \(\sigma_0>1/2\) 时，相应的主项、误差与统一余量必须
重新控制；不能把 (9) 在新范围内视作既有结果。

## 6. 保持原公式时，仅调尺度的代数限制

这是带明确前提的代数命题，不假定 [Q] 的分析估计已推广至所有可变参数。
保留

\[
b,\ell\ge0,\quad l_y=l_x+b,\quad2l_x+b+\ell=1,\quad
h=1+\ell-l_x,\quad L=l_x/2+b/12,
\quad C(s)=l_x/2+s-1+h/6.
\]

低界与信号相遇的边界 \(B\) 满足 \(C(B)=L\)。直接消元给

\[
l_x=(1-b-\ell)/2,\qquad h=(1+b+3\ell)/2,\qquad
B=1-h/6+b/12=11/12-\ell/4.                                \tag{10}
\]

若所有补偿后尺度 \(X'=Z^{l_x-d}\)、\(0\le d\le\ell\) 仍增长，则
\(l_x-\ell>0\)，从而

\[
\ell<(1-b)/3,\qquad B>5/6+b/12\ge5/6.                      \tag{11}
\]

若仅要求未补偿的 \(X\) 增长，即 \(l_x>0\)，则只有

\[
\ell<1-b,\qquad B>2/3+b/4\ge2/3.                           \tag{12}
\]

所以在上述公式保持原样的前提下，单独调尺度不能达到 \(1/2\)。
(11) 不声称 \(5/6\) 已可达到，也不排除改变探针、抵消估计或最短尺度处理。
(11) 与 (12) 使用不同条件，不可混用。

## 7. 一个精确的算术相关估计目标

沿用 [Q] `eq:low-separated` 与 `sec:compensated-low` 的全部算术定义：
\(q_m\) 是其范数，\(\xi(m)\) 是其固定算术系数，\(\sigma\in T\) 为 ray class，
\(W_0,W_1,\Omega\) 是原测试函数。这里的 \(\xi(m)\) 不指完成 zeta 函数。
原始字符的零延拓、prime masks 和模数均保留。

对补偿子集 \(J\)，固定重缩放素数组 \(\mathbf p_J\)，置

\[
d=\sum_{i\in J}\ell_i\in[0,1/6],\qquad
X'=X/q_{p_J},\quad Y'=Y/q_{p_J},\quad Q=q_{b_*}X'Y'
\asymp Z^{5/6-2d}.
\]

其中加性因子准确为

\[
A_{m,\sigma,v}(Y')=\frac1{Y'}\sum_{s\in\sigma}
\frac{W_1(q_s/Y')\chi_s(b_*)}{\tau\xi(s)}
(q_s/Y')^{-1/2+iv}q_s^{-1/2}g_{\chi_s}(s,-m).
\]

\(B^J_{m,\sigma}(Z)\) 是 [Q] `sec:compensated-low` 中已经对未重缩放
slots \(i\notin J\) 求和的 marked completed row；保留其原 Gaussian
Mellin 权重和整条 \(\Re t=4\) 积分。固定的 \(\mathbf p_J\) 只通过
\(X',Y'\) 进入分离式。定义

\[
S_J(v,\sigma,\mathbf p_J;Z)=\sum_{m\ne0}
\Omega(q_m/Q)\xi(m)(q_m/Q)^{-iv}
A_{m,\sigma,v}(Y')B^J_{m,\sigma}(Z).                         \tag{R1}
\]

原分离式是 \(Q^{-1/2}/(2\pi)\) 乘
\(\sum_{\sigma\in T}\int\widehat W_0(iv)S_J(v,\sigma,\mathbf p_J;Z)\,dv\)。
[Q] 的 `old-eq:5.6`、`old-eq:5.4` 在相关支撑上给出

\[
\sum|A_m|^2\ll (1+|v|)^D Z^{3/8-d+\epsilon},\qquad
\sum|B^J_m|^2\ll Z^{5/6-2d+\epsilon}.                       \tag{R2}
\]

固定有界权重吸收到常数中，Cauchy–Schwarz 因而给

\[
|S_J|\ll(1+|v|)^{D/2}Z^{29/48-3d/2+\epsilon}.              \tag{R3}
\]

**尚未证明的充分目标：** 对每个 \(\epsilon>0\)，存在固定有限阶 \(D'\)，
使对全部这些 \(J,\sigma\)、原始支持上的 \(\mathbf p_J\) 及实 \(v\)，一致有

\[
\boxed{|S_J|\ll(1+|v|)^{D'}Z^{11/48-d/2+\epsilon}.}         \tag{R4}
\]

\(D'\)、常数和起始阈值可依固定算术数据、slot 系统、测试函数及
\(\epsilon\)，但不随 \(Z,v,\mathbf p_J\) 增大。

**(R4) 对 (8) 的充分性证明。** \(Q^{-1/2}\) 贡献指数 \(-5/12+d\)。
\(\widehat W_0(iv)\) 任意幂次衰减，吸收 \((1+|v|)^{D'}\) 的积分。
剩余重缩放素数组至多有 \(Z^{d+\epsilon}\) 个，原补偿系数为
\(O(Z^{-3d/2})\)。因此总指数为

\[
(-5/12+d)+(11/48-d/2)+d-3d/2=-3/16.                        \tag{13}
\]

分配有限次出现的小 \(\epsilon\)，对固定有限个子集与 ray classes 求和，
再吸收固定对数归一化，即得 (8)。证毕。

所需相关节省准确为

\[
(29/48-3d/2)-(11/48-d/2)=3/8-d\in[5/24,3/8].               \tag{14}
\]

这是两个因子之间需要取得的额外抵消，现有均方界相乘尚不给出它。
(R4) 是逐项充分条件；完整有符号的 \(J,\mathbf p_J\) 求和也可能提供所需
总节省，所以 (R4) 不被宣称为 RH 的必要条件。它亦没有解决高端条件 (9)。

## 8. 来源与精确复算

[S] 本仓库固定提交
[`60374863affee2cb4f4f4ca636b5dfeb2cb639d6` 的研究续篇](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/60374863affee2cb4f4f4ca636b5dfeb2cb639d6/history/source-materials/RH_%E7%A0%94%E7%A9%B6%E7%BB%AD%E7%AF%87_20261011.md)：
`EIGENMODE_SELECTION`，第 2242–2414 行的展开、完整系数方程和 Laplace 极点；
第 2567–2762 行的序列空间与域核验。

[Q] *The Quasi-Riemann Hypothesis*，`openai/math` 固定提交
[`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` 的 paper.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)：
主定理；`lem:continuation-criterion`；`eq:low-separated`；
`eq:part-II-mellin-target`；`old-eq:5.1`；`sec:compensated-low`；
`prop:probe-low`。引用参数和公式均指此固定版本。

[D] 本仓库固定提交
[`4d2cc4cf6a147078c7a4bcc4922f7d5639223d5e` 的本征源转移审查](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4d2cc4cf6a147078c7a4bcc4922f7d5639223d5e/reports/20261011_theta_dirichlet_rigidity/REFEREE_DIRICHLET_TRANSFER.md)，
第 4–8 节：普通 Dirichlet 类的限制及实射线速率。

[G] NIST DLMF，[§5.11，Stirling 展开与 Gamma 商](https://dlmf.nist.gov/5.11#iii)。

随附 `check_exponents.py` 仅用标准库 `fractions.Fraction`，精确复算
(6)–(14) 的有理指数和关于 \(b,\ell,d\) 的仿射恒等式；它不替代分析证明，
也不检查引用输入 S、Q。运行环境为 Python 3.14.8，无第三方包：

```sh
python3 check_exponents.py
```

本文尚未证明 (T)、(R4) 或适用于任意 \(\sigma_0>1/2\) 的 (9)，
因此没有完成 RH 证明。
