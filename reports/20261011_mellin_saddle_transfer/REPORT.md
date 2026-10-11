# 真实 theta 核的 Mellin 鞍点传递与低态的准确幂次阶

本稿继承固定提交 `4495df1319b2ee655cc52cc90b7512371fd0f0c4` 的对象与
选择输入，不修改旧证明。新增内容是一个对真实完整 theta 核的准确 Gamma
平均表示、带指数权导数条件下的鞍点误差，以及真实低态 Mellin 商的准确
实射线幂次阶。没有证明严格增长下降，也没有排除新的真实零点。

## 1. 归一化与定理

保持 [B] 的记号：

\[
\Phi(x)=\sum_{n\ge1}\Phi_n(x),\qquad
\Phi_n(x)=(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})
e^{-\pi n^2e^{2x}},
\]

\[
G(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad
D_{\Phi q}(s)=G(s)^{-1}\int_{\mathbb R}\Phi(x)q(x)e^{(s-1/2)x}\,dx.
\]

对实 \(\sigma>1\)，置

\[
k=\sigma/2,\quad x_\sigma=\tfrac12\log\frac{k}{\pi}
=\tfrac12\log\frac{\sigma}{2\pi},\qquad
A_k=\frac{2(k+1)}{2k-1},\quad B_k=\frac3{2k-1}.
\tag{1}
\]

特别地 \(A_k-B_k=1\)。以下 \(\mathbb E_a\) 表示形状参数为 \(a>0\)、
尺度为 1 的 Gamma 分布的期望。

**定理 1（准确表示）。** 对任意有界可测 \(q:\mathbb R\to\mathbb C\)，

\[
\boxed{D_{\Phi q}(\sigma)=\sum_{n\ge1}n^{-\sigma}
\left[A_k\mathbb E_{k+2}q\!\left(\tfrac12\log\frac T\pi-\log n\right)
-B_k\mathbb E_{k+1}q\!\left(\tfrac12\log\frac T\pi-\log n\right)\right].}
\tag{2}
\]

这里是两个正概率平均的带符号组合。单个 \(\Phi_n\) 在整个实轴上并不
非负，所以不能将单模态归一化的积分直接称作概率测度。

**定理 2（带指数权的鞍点误差）。** 设 \(c>0\)，\(q\in C^2(\mathbb R)\)，
且对 \(j=0,1,2\) 有 \(|q^{(j)}(x)|\le C_j e^{-c|x|}\)。则

\[
\boxed{D_{\Phi q}(\sigma)=q(x_\sigma)
+O_{q,c}(\sigma^{-c/2-1})\quad(\sigma\to+\infty).}
\tag{3}
\]

若同一条件还对 \(j=3\) 成立，则进一步有

\[
\boxed{D_{\Phi q}(\sigma)=q(x_\sigma)
+\frac{3}{2\sigma}q'(x_\sigma)+\frac1{4\sigma}q''(x_\sigma)
+O_{q,c}(\sigma^{-c/2-3/2}).}
\tag{4}
\]

常数依赖所列指数权导数界。没有声称它们在低态谱参数趋近阈值时一致。
这些定理不要求 \(q\) 偶、不要求本征方程，也不要求 7/8 输入。

## 2. 完整模态的绝对交换与准确 Gamma 平均

对单个 \(n\)，换元 \(t=\pi n^2e^{2x}\) 给

\[
\begin{split}
\int_{\mathbb R}\Phi_n(x)q(x)e^{(\sigma-1/2)x}\,dx
={}&\pi^{-k}n^{-\sigma}\int_0^\infty
(2t^{k+1}-3t^k)e^{-t}
q\!\left(\tfrac12\log\frac t\pi-\log n\right)\,dt.
\end{split}
\tag{5}
\]

因 \(G(\sigma)=\pi^{-k}k(2k-1)\Gamma(k)\)，Gamma 递推关系直接给 (2)。
其绝对交换并非使用源方程中的素数平移；这里使用的是原始 theta 模态，
有明确的绝对积分界：

\[
\frac1{G(\sigma)}\sum_{n\ge1}
\int_{\mathbb R}|\Phi_n(x)q(x)|e^{(\sigma-1/2)x}\,dx
\le \|q\|_\infty(A_k+B_k)\zeta(\sigma)<\infty.
\tag{6}
\]

Tonelli/Fubini 因此适用。注意 (2) 中的期望仍依赖 \(\sigma\)：它不是
普通 Dirichlet 级数的固定系数表示，不能援引 [D] 的普通 Dirichlet 类刚性。

对 \(\sigma\ge2\)，积分比较给

\[
\sum_{n\ge2}n^{-\sigma}
\le 2^{-\sigma}+\int_2^\infty t^{-\sigma}\,dt
=2^{-\sigma}\left(1+\frac2{\sigma-1}\right).
\tag{7}
\]

由于 \(A_k+B_k\) 在此范围有界，(2) 中全部 \(n\ge2\) 项均为
\(O_q(2^{-\sigma})\)。这是在 \(q\) 有界的准确表示中使用的估计，
没有将本征源替换成一个单 theta 模态。

## 3. 对数 Gamma 矩与加权 Taylor 余项

固定 \(a\in\{1,2\}\)，在 \(\mathbb E_{k+a}\) 下置

\[
\Delta=\tfrac12\log(T/k),\qquad
\tfrac12\log(T/\pi)=x_\sigma+\Delta.
\]

Gamma 积分对形状参数的微分给

\[
\mathbb E_{k+a}\Delta=\tfrac12[\psi(k+a)-\log k]
=\frac{a-1/2}{2k}+O(k^{-2}),
\tag{8}
\]

\[
\mathbb E_{k+a}\Delta^2
=\tfrac14\{\psi_1(k+a)+[\psi(k+a)-\log k]^2\}
=\frac1{4k}+O(k^{-2}).
\tag{9}
\]

这里 \(\psi=\Gamma'/\Gamma\)、\(\psi_1=\psi'\)；所用展开见 [G]。
不能将 \(\mathbb E|\Delta|=O(k^{-1/2})\) 当成 (8) 的替代，因为
保留有符号的一阶矩才能得到 (3) 的完整一个 \(\sigma\) 次幂误差。

对任意固定实 \(r\)，\(k\) 足够大后，准确恒等式为

\[
\mathbb E_{k+a}\big[(T/k)^r\log^2(T/k)\big]
=k^{-r}\frac{\Gamma(k+a+r)}{\Gamma(k+a)}
\{[\psi(k+a+r)-\log k]^2+\psi_1(k+a+r)\}
=O_{a,r}(k^{-1}).
\tag{10}
\]

利用 \(e^{c|\Delta|}\le(T/k)^{c/2}+(T/k)^{-c/2}\)，得到

\[
\mathbb E_{k+a}[\Delta^2e^{c|\Delta|}]=O_{a,c}(k^{-1}).
\tag{11}
\]

在 \(x_\sigma\ge0\) 时，任意 \(u\in\mathbb R\) 满足
\(e^{-c|u|}\le e^{-cu}\)，所以沿 Taylor 线段有

\[
|q''(x_\sigma+t\Delta)|
\le C_2e^{-cx_\sigma}e^{c|\Delta|}\qquad(0\le t\le1).
\]

因而二阶余项的绝对期望由 (11) 控制：

\[
\mathbb E_{k+a}q(x_\sigma+\Delta)
=q(x_\sigma)+q'(x_\sigma)\mathbb E_{k+a}\Delta
+O_{q,c}(e^{-cx_\sigma}k^{-1})
=q(x_\sigma)+O_{q,c}(e^{-cx_\sigma}k^{-1}).
\tag{12}
\]

使用 \(A_k-B_k=1\)、(7) 和
\(e^{-cx_\sigma}=(k/\pi)^{-c/2}\)，即得 (3)。

若有第三阶导数界，还需控制绝对三阶矩。以
\(Z=\log(T/k)\) 计，加权二阶、四阶对数矩满足

\[
\mathbb E_{k+a}[(T/k)^rZ^2]=O(k^{-1}),\qquad
\mathbb E_{k+a}[(T/k)^rZ^4]=O(k^{-2}).
\tag{13}
\]

第二式可由 Gamma 积分四次微分直接得到：在参数 \(k+a+r\) 的 Gamma
分布下，\(Z\) 的均值为 \(O(k^{-1})\)，二至四阶累积量依次为
\(\psi_1=O(k^{-1})\)、\(\psi_2=O(k^{-2})\)、\(\psi_3=O(k^{-3})\)。
其四阶原点矩为
\(\mu^4+6\mu^2\psi_1+4\mu\psi_2+3\psi_1^2+\psi_3=O(k^{-2})\)，
再乘有界的 \(k^{-r}\Gamma(k+a+r)/\Gamma(k+a)\) 即得。
加权 Cauchy–Schwarz 对 (13) 给

\[
\mathbb E_{k+a}[|\Delta|^3e^{c|\Delta|}]=O_{a,c}(k^{-3/2}).
\tag{14}
\]

三阶 Taylor 余项因此合法。将 (8)、(9) 代入二次 Taylor 式，得到

\[
\mathbb E_{k+a}q(x_\sigma+\Delta)
=q(x_\sigma)+\frac{a-1/2}{2k}q'(x_\sigma)
+\frac1{8k}q''(x_\sigma)
+O_{q,c}(e^{-cx_\sigma}k^{-3/2}).
\tag{15}
\]

因 \(A_k=1+O(k^{-1})\)、\(B_k=O(k^{-1})\)，合并两项时一阶系数为
\(3/(4k)+O(k^{-2})\)，二阶系数为 \(1/(8k)\)。用 \(\sigma=2k\)
换回即得 (4)。误差吸收了系数的 \(O(k^{-2})\) 修正及 (7)。

## 4. 真实低态：由上界升级为准确幂次阶

以下明确继承 [B] 的选择输入 S 与条带输入 Q，而非在本稿重新认证它们。
对每个非零真实实偶亚临界本征态，令

\[
g=2\cosh(x/2)q,\qquad
\alpha(q)=\sup\{|\Im w|:\widehat{\Phi q}(w)\ne0,\ \Xi(w)=0\}.
\]

[B] 已证明

\[
0<\alpha(q)\le3/8,\qquad c=1/2-\alpha(q)>0,\qquad
\tau(q)=-c,\qquad |q^{(j)}(x)|\le C_j e^{-c|x|}.
\tag{16}
\]

其中 \(\tau(q)\) 为右半轴全局指数界的下确界。对于实射线定义

\[
\beta(D)=\inf\{b\in\mathbb R:|D(\sigma)|\le C\sigma^b
\text{ 对全部充分大的实 }\sigma\text{ 成立}\}.
\]

**推论 3（准确幂次阶）。**

\[
\boxed{\beta(D_{\Phi q})=-\frac c2
=-\frac14+\frac{\alpha(q)}2\in(-1/4,-1/16].}
\tag{17}
\]

**证明。** (3) 及 (16) 给 \(\beta(D)\le-c/2\)。若存在
\(b=-c/2-\delta\)、\(\delta>0\)，使 \(D(\sigma)=O(\sigma^b)\)，则 (3) 给

\[
q(x_\sigma)=O(\sigma^{-c/2-\min(\delta,1)}).
\]

因为 \(\sigma=2\pi e^{2x_\sigma}\) 精确覆盖充分大的 \(x_\sigma\)，得到
\(q(x)=O(e^{[-c-2\min(\delta,1)]x})\)。在剩余紧区间增加常数即可成为
全右半轴界，这与 \(\tau(q)=-c\) 矛盾。如果下确界小于 \(-c/2\)，按其
定义必存在一个这样的 \(b\)，所以得到反向不等式。证毕。

这不要求活动虚部上确界被某个零点达到，也不假定 \(q\) 最终同号。
它是绝对值幂次界的准确下确界，不声称存在非零常数的点态等价式
\(D(\sigma)\sim C\sigma^{-c/2}\)；无限频率混合可以振荡。

## 5. 新的准确排谱接口及仍未证明的步骤

由 (17)，一个充分排谱目标是独立地证明，对每个潜在非零真实低态，

\[
\forall\epsilon>0:\qquad
D_{\Phi q}(\sigma)=O_{q,\epsilon}(\sigma^{-1/4+\epsilon}).
\tag{T_M}
\]

若 \(\alpha(q)>0\)，取 \(0<\epsilon<\alpha(q)/2\)，(17) 立即与该界矛盾。
更强的单界 \(O_q(\sigma^{-1/4})\) 当然也足够。目前没有证明其中任何一个。

现有的 \(O_q(\sigma^{-1/16})\) 与 (17) 相容。改善至某个固定
\(O_q(\sigma^{-r})\)，其中 \(1/16<r<1/4\)，至多给
\(\alpha(q)\le1/2-2r\)；它仍允许正的活动离轴距离。
不能将鞍点传递本身解释为增长下降。

在 (16) 的真低态范围内，\((T_M)\) 与以下界族等价：对每个
\(\eta>0\)，\(g(x)=O_{q,\eta}(e^{\eta x})\)，亦即 \(\tau(g)\le0\)。
这里没有声称下确界端点必有 \(g(x)=O(1)\) 的界。
由 (3) 可双向传递任意小正指数余量，并使用
\(g=(e^{x/2}+e^{-x/2})q\)。这个接口把承重问题转为实 Mellin 射线，
没有消除其困难，也没有证明本征源的普通 Dirichlet 保类。

第五轮算子与全零点选择输入的独立复审限制仍保留。所有低态推论都明确
以这些输入为前提；定理 1–2 的 theta/Gamma 传递则有上面的独立证明。

## 6. 来源与复算范围

[B] 固定提交
[`4495df1319b2ee655cc52cc90b7512371fd0f0c4` 的选择方程桥接](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/REPORT.md)，
第 1–4 节，尤其全阶指数界、活动上确界与准确增长阶。输入 S、Q 的原始
固定出处均沿用该稿；本稿不将引用扫描当作 Lean 内核验证。

[D] 固定提交
[`4495df1` 的本征源转移审查](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_theta_dirichlet_rigidity/REFEREE_DIRICHLET_TRANSFER.md)，
第 4–8 节：普通 Dirichlet 保类、双向素数交换与先前实射线界的范围。

[G] NIST DLMF：[Gamma 积分 §5.9](https://dlmf.nist.gov/5.9)、
[Gamma 商与 digamma 展开 §5.11](https://dlmf.nist.gov/5.11)、
[polygamma 展开 §5.15](https://dlmf.nist.gov/5.15)。

`check_saddle_coefficients.py` 仅用标准库有理数/多项式运算，核对单模态
归一化、\(A_k-B_k=1\)、首修正系数及指数传递。它不验证分析余项、不检验
输入 S、Q，也不构成 RH 证明认证。
