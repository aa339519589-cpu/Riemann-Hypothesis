# 真实删素—反射接口的复振荡与不可一致支配

日期：2026-10-11。继承公开仓库提交 `74add2e1350dd4414d83dd46a4e10be8aeb7b42f`。

## 状态与本步的准确用途

**NO NEW UNCONDITIONAL RH THEOREM PROVED。** 本文没有排除新的真实离轴零点，也没有证明临界跳跃谱隙。本步给出一个使用真实素数、真实单高斯种子和真实反射尾的辅助障碍：沿有限删素极限，把种子变换当作统一主项、把反射尾当作 Rouché 小扰动的指定策略不成立。

这不是旧三平移反模型的重复：以下对象全部来自真实 ζ。新结论是反射尾在同一固定复点上有确定的两个相反渐近行为；缓慢向左移动分界点也不能消除此现象。它不排除其他复域估计、具有额外相位信息的论证或不同分解。

已读的继承材料：`STATUS.md`、第五轮第 1–10 页中的承重定义和谱论、第六轮恢复摘要、`history/routes/README.md`，以及 `history/source-materials/RH_研究续篇_20261011.md` 的主体与附录 7、14、15。特别继承附录 14 的有限删素恒等式及反射重构 (1.2)、(2.3)、(3.11)，不把其局部一致重构当成无零点证明。

## 1. 固定尺度，避免 Fourier 归一混淆

本文使用续篇附录 14 的旧变量尺度，而非第五轮 x 尺度：

\[
\phi(t)=\sum_{m\ge1}\phi_m(t),\quad
\phi_m(t)=(2\pi^2m^4e^{9t}-3\pi m^2e^{5t})e^{-\pi m^2e^{4t}}.
\]

因此第五轮的 \(\Phi\) 满足 \(\Phi(2t)=2\phi(t)\)，并且

\[
\Psi(z):=\int_{\mathbb R}\phi(t)e^{izt}dt
=\tfrac14\xi(s),\qquad s=\tfrac12+\tfrac{iz}{2}.
\tag{1}
\]

写 \(z=u+iv\)，则 \(\sigma=\Re s=(1-v)/2\)、\(\tau=\Im s=u/2\)。区域 \(|\Im z|<1\) 准确对应 \(0<\Re s<1\)。

令 \(Q_Y=\prod_{p\le Y}p\)，\(\tau_d=\frac12\log d\)，并定义

\[
E_Y(s)=\prod_{p\le Y}(1-p^{-s}),\qquad
F_Y(t)=\sum_{d\mid Q_Y}\mu(d)d^{-1/2}\phi(t+\tau_d).
\]

每个乘积和约数和都是有限的；在 \(\Re s>0\) 单个因子无零点。精确模态恒等式给出

\[
F_Y(t)=\sum_{(m,Q_Y)=1}\phi_m(t),\qquad
\widehat F_Y(z)=E_Y(s)\Psi(z).
\tag{2}
\]

对 \(T\ge0\) 定义

\[
A_T(z)=\int_{-T}^{\infty}\phi_1(t)e^{izt}dt,
\quad B_{Y,T}(z)=\int_{-\infty}^{-T}F_Y(t)e^{izt}dt,
\]
\[
R_{Y,T}(z)=\int_{-T}^{\infty}(F_Y(t)-\phi_1(t))e^{izt}dt.
\]

这些有限 Y、T 下的积分均存在，且

\[
\boxed{A_T+B_{Y,T}+R_{Y,T}=E_Y\Psi.}
\tag{3}
\]

其中真正的反射表达为

\[
B_{Y,T}(z)=\sum_{d\mid Q_Y}\mu(d)d^{-s}
\int_{T-\tau_d}^{\infty}\phi(t)e^{-izt}dt.
\tag{4}
\]

式 (4) 保留 Möbius 符号，不声称逐项非负。

## 2. 真实有限 Euler 因子的振荡定理

### 定理 1

对每个固定 \(s=\sigma+i\tau\)，若 \(0<\sigma<1\)，定义无歧义的解析对数

\[
\ell_Y(s)=\sum_{p\le Y}\operatorname{Log}(1-p^{-s})
=-\sum_{p\le Y}\sum_{k\ge1}\frac{p^{-ks}}k.
\]

这里 \(\operatorname{Log}(1-w)=-\sum_{k\ge1}w^k/k\) 对 \(|w|<1\) 固定分支。因此 \(e^{\ell_Y}=E_Y\)，且

\[
\boxed{\ell_Y(s)=-\frac{Y^{1-s}}{(1-s)\log Y}
+o_s\!\left(\frac{Y^{1-\sigma}}{\log Y}\right).}
\tag{5}
\]

若进一步 \(\tau\ne0\)，则

\[
\boxed{\liminf_{Y\to\infty}|E_Y(s)|=0,\qquad
\limsup_{Y\to\infty}|E_Y(s)|=\infty.}
\tag{6}
\]

### 证明

第一步，只使用无条件素数定理 \(\pi(x)=x/\log x+o(x/\log x)\)。Abel 求和给出

\[
P_Y(s):=\sum_{p\le Y}p^{-s}
=Y^{-s}\pi(Y)+s\int_2^Y\pi(x)x^{-s-1}dx.
\tag{7}
\]

令 \(a=1-\sigma>0\)。一次分部积分及绝对值估计给出

\[
\int_2^Y\frac{x^{-s}}{\log x}dx
=\frac{Y^{1-s}}{(1-s)\log Y}
+O_s\!\left(1+\frac{Y^a}{(\log Y)^2}\right).
\tag{8}
\]

具体地，导数 \(\frac{d}{dx}[x^{1-s}/((1-s)\log x)]\) 与被积函数之差为
\(-x^{-s}/((1-s)(\log x)^2)\)，其积分模至多 \(O_s(1+Y^a/(\log Y)^2)\)。

对 PNT 的余项，给定任意 \(\epsilon>0\)，先选 \(X_\epsilon\) 使其在 \(x\ge X_\epsilon\) 的绝对值不超过 \(\epsilon x/\log x\)。区间 \([2,X_\epsilon]\) 贡献常数，其后贡献不超过
\(\epsilon\int_{X_\epsilon}^Yx^{-\sigma}/\log x\,dx\)。除以 \(Y^a/\log Y\)、令 \(Y\to\infty\) 再令 \(\epsilon\to0\)，得余项为 \(o_s(Y^a/\log Y)\)。代入 (7)：

\[
P_Y(s)=\left(1+\frac{s}{1-s}\right)
\frac{Y^{1-s}}{\log Y}+o_s(Y^a/\log Y)
=\frac{Y^{1-s}}{(1-s)\log Y}+o_s(Y^a/\log Y).
\tag{9}
\]

第二步，所有高次素数幂的贡献严格较小：

\[
|\ell_Y(s)+P_Y(s)|
\le\frac1{1-2^{-\sigma}}\sum_{p\le Y}p^{-2\sigma}
\le C_\sigma\sum_{n\le Y}n^{-2\sigma}.
\]

最右端依 \(\sigma<1/2,=1/2,>1/2\) 分别是
\(O(Y^{1-2\sigma})\)、\(O(\log Y)\)、\(O(1)\)，三者都是
\(o(Y^{1-\sigma}/\log Y)\)。结合 (9) 得 (5)。这里未把临界条带内的无限 Euler 乘积当作 ζ。

第三步，用共轭可设 \(\tau>0\)。置

\[
\theta=\arctan(\tau/(1-\sigma)),\qquad
r_Y=\frac{Y^{1-\sigma}}{|1-s|\log Y}.
\]

取实部得到

\[
\log|E_Y(s)|=-r_Y\cos(\tau\log Y-\theta)+o_s(r_Y).
\tag{10}
\]

两列明确截断尺度为

\[
Y_k^{\downarrow}=\exp((2\pi k+\theta)/\tau),\qquad
Y_k^{\uparrow}=\exp(((2k+1)\pi+\theta)/\tau).
\tag{11}
\]

于是分别有 \(\log|E_{Y_k^{\downarrow}}|=-r_{Y_k^{\downarrow}}(1+o(1))\) 和
\(\log|E_{Y_k^{\uparrow}}|=r_{Y_k^{\uparrow}}(1+o(1))\)。因为 \(r_Y\to\infty\)，得到 (6)。若要求整数截断，对 (11) 向下取整即可；相位变化是 \(O(1/Y)\)，不改变结论。对 \(\tau<0\) 使用 \(|\tau|\) 和共轭。证毕。

## 3. 一个允许移动反射分界的真实余项界

### 引理 2

对任意紧集 \(K\Subset\{z:|\Im z|<1\}\)，存在 \(C_K>0\)，使所有 \(Y\ge2,T\ge0\) 且
\(\pi Y^2e^{-4T}\ge1\) 满足

\[
\boxed{\sup_{z\in K}|R_{Y,T}(z)|
\le C_K(1+e^{2T})
\exp\!\left(-\frac\pi4Y^2e^{-4T}\right).}
\tag{12}
\]

### 证明

模态和 (2) 中除 \(m=1\) 之外的剩余整数必有 \(m>Y\)。对于 \(z=u+iv\)，置 \(\sigma=(1-v)/2\in(0,1)\)，并在单模态绝对积分中换元 \(w=\pi m^2e^{4t}\)。得到

\[
\int_{-T}^{\infty}|\phi_m(t)|e^{-vt}dt
\le C_K m^{-\sigma}
\int_{\pi m^2e^{-4T}}^{\infty}
(w^{1+\sigma/2}+w^{\sigma/2})e^{-w}dw.
\]

对 \(w_0\ge1\)，最后的积分至多 \(C_K e^{-w_0/2}\)，这是多项式被 \(e^{w/2}\) 一致支配的直接结果。因此

\[
|R_{Y,T}(z)|\le C_K\sum_{m>Y}m^{-\sigma}
e^{-(\pi/2)m^2e^{-4T}}.
\]

用 \(m^{-\sigma}\le1\)、拆出
\(e^{-(\pi/4)Y^2e^{-4T}}\)，其余 Gaussian 和由
\(C(1+e^{2T})\) 控制，即得 (12)。这不是抽样积分估计。

### 推论 2.1

固定 \(\eta\in(0,1/2)\)。若 \(T=T(Y)\ge0\) 且最终满足

\[
T(Y)\le(1/2-\eta)\log Y,
\tag{13}
\]

则 \(R_{Y,T(Y)}\to0\) 在每个上述 K 上一致成立。因为 (12) 至多是
\(C_K(1+Y)e^{-cY^{4\eta}}\)。

若 \(T(Y)\to\infty\)，还有

\[
A_{T(Y)}(z)\longrightarrow A_\infty(z)
=\frac{iz-1}{8}\pi^{-(1+iz)/4}
\Gamma\!\left(\frac{5+iz}{4}\right),
\tag{14}
\]

在条带紧集上一致。其左尾由 \(e^{(5-v)t}\) 控制。(14) 来自完整单模态积分的直接 Gamma 换元，并且在 \(|\Im z|<1\) **无零点**；线性因子的零点 \(z=-i\) 在边界。

## 4. 反射尾必有支配和近乎完全抵消的两个子序列

### 定理 3：固定 T

固定 \(T\ge0\) 与 \(z\) 满足

\[
|\Im z|<1,\quad\Re z\ne0,\quad\Psi(z)\ne0,\quad A_T(z)\ne0.
\]

按照定理 1 中 \(s=1/2+iz/2\) 的两列尺度（若 \(\Re z<0\)，使用 \(\tau<0\) 的共轭版本），有

\[
\boxed{\frac{B_{Y_k^{\downarrow},T}(z)}{A_T(z)}\longrightarrow-1,\qquad
\left|\frac{B_{Y_k^{\uparrow},T}(z)}{A_T(z)}\right|\longrightarrow\infty.}
\tag{15}
\]

证明只有精确式 (3)：

\[
\frac{B_{Y,T}}{A_T}=\frac{E_Y\Psi}{A_T}-1-\frac{R_{Y,T}}{A_T}.
\]

定理 1 和引理 2 分别控制三个项，得到 (15)。不需要假设任何零点位于临界线。

### 定理 4：向左移动的 T

对每个固定 \(z\) 满足 \(|\Im z|<1,\Re z\ne0,\Psi(z)\ne0\)，如果
\(T(Y)\to\infty\) 且 (13) 成立，则 (15) 对移动的 \(T(Y)\) 仍成立。
原因是 \(A_{T(Y)}\to A_\infty\ne0\)，而 (12) 保证 \(R\to0\)。

### 所排除的准确断言

在定理 3 或 4 的任意一点，不可能存在 \(Y_0\) 使所有 \(Y\ge Y_0\) 满足
\(|B_{Y,T}|<|A_T|\)。更不可能有一个固定 \(\delta>0\)，使
\(|B_{Y,T}|\le(1-\delta)|A_T|\) 最终成立。

这一障碍不依赖未知零点是否存在。因为 \(\Psi(0)>0\)，且对固定 T 有 \(A_T(0)\) 未必总为正但作为整函数不恒零，可直接选 T=0，此时 \(A_0(0)>0\)；连续性给出原点附近的小开集，其中 \(\Psi A_0\ne0\)。任取足够小的非零实部及非零虚部点就适用 (15)。对移动 T，(14) 已自动消除了种子零点问题。

特别地，有限删素全都保留真实零点，却不能从“每个因子无零点”或“反射表达精确”推断种子始终支配尾项。这里没有排除只在经过证明选定的轮廓/子序列上成立的新估计。

## 5. 归一重构的必然病态量级

固定 T 和定理 3 中的点。由于 (12) 是 \(e^{-cY^2}\) 级别，而定理 1 给
\(\log|E_Y|=O_s(Y^{1-\sigma}/\log Y)\)，有 \(R_{Y,T}/E_Y\to0\)。因此

\[
A_T+B_{Y,T}=E_Y\Psi(1+o(1)).
\tag{16}
\]

考察只对这两个加数的相对扰动条件数

\[
\kappa_Y(z)=\frac{|A_T(z)|+|B_{Y,T}(z)|}
{|A_T(z)+B_{Y,T}(z)|}.
\]

在缩小子序列上由 (15)、(16) 得

\[
\kappa_{Y_k^{\downarrow}}
\sim\frac{2|A_T|}{|\Psi|\,|E_{Y_k^{\downarrow}}|},\qquad
\boxed{\frac{\log\kappa_{Y_k^{\downarrow}}}{r_{Y_k^{\downarrow}}}\to1.}
\tag{17}
\]

这是该二项重构的数学条件数，不是所有算法的复杂度下界，也不证明任何计算的实际误差。在这种直接相加实现中，若两项的相对输入误差同阶，抵消导致的潜在有效位损失约为 \(r_Y/\log2\)。不能把绝对余项极小自动理解成分子稳定、具有相对符号裕量。

对移动 T，同样的相对误差推理在充分条件
\(T(Y)\le c\log Y\)、\(c<(1+\sigma)/4\) 下成立，因为 Gaussian 指数的幂
\(2-4c\) 严格大于 \(1-\sigma\)。这里是充分条件，**未声称锐利阈值**。

## 6. 在真正零点处发生什么；精确剩余缺口

若 \(\Psi(z_0)=0\)，则 (3) 给出

\[
A_T(z_0)+B_{Y,T}(z_0)=-R_{Y,T}(z_0)
\tag{18}
\]

对每个 Y 精确成立。固定 T 且 \(A_T(z_0)\ne0\) 时，\(B/A_T\to-1\) 沿**全部** Y 成立；移动 T 满足定理 4 的假设时亦然。

但定理 3 已证明：在一个明确非零点上也有 \(B/A_T\to-1\) 的无限子序列。因此，“出现非常准确的种子—反射尾抵消”不是零点识别或排除机制。若去要求一种能够区分 (18) 与非零点情形的统一相对下界，该下界本身仍须从真实算术结构独立证明，不能由解析重构等式推出。

本步尝试过的闭合是：无零点单 Gamma 种子 + 真实反射尾 + 删除越来越多素数，寻求最终严格种子支配。定理 3、4 表明这个**具体闭合尝试失败**。本步保留下来的原始 RH 目标仍是：对全部实偶紧支光滑 q，证明真实无限跳跃能量
\(\mathcal E(q)\ge\frac12\operatorname{Var}_\nu(q)\)，或者通过一项独立的新估计排除全部亚临界本征态。本文没有得到该估计。

## 7. 外部输入、复算与非循环检查

- 唯一新增算术输入是无条件 PNT；可用更强但非必需的 Song–Yao 正式化版本：[Prime Number Theorem with Remainder Term](https://isa-afp.org/entries/PNT_with_Remainder.html)。本文只用其蕴含的 \(\pi(x)\sim x/\log x\)，不使用条件于 RH 的误差项。
- [DLMF §27.4](https://dlmf.nist.gov/27.4) 所述无限 Euler 乘积的绝对收敛恒等式仅在 \(\Re s>1\)。本文没有把它越界使用；E_Y 始终有限。
- 新证明 (5)–(17) 从无条件 PNT、有限因子对数、已有真实核恒等式和绝对积分估计推导；不使用无实部偏移零点、Ξ 谱实性、Weil 正性或目标临界谱隙。
- 同目录脚本 `check_prime_reflection.py` 只交叉核对归一化、有限删素反射身份和截断乘积的振荡尺度。输出标记 `NUMERICAL_ONLY`，不承担无限量词或 RH 结论。
- 本文的“新”只指在所检查的项目材料中新增，不主张文献首次。尚需独立人工复审，未做 Lean/Isabelle 对本文新推导的内核验证。
