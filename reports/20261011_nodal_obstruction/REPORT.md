# 真实跳跃算子的半轴节点接口：核反例与绝对值试探

本稿核对第五轮的完整实跳跃形式与固定提交 e93c04f 的振荡结论，研究能否从最低非零偶态的节点结构排除低态。以下否定的是全核的总正性与一般输入的变差缩减路径；最低态专属节点定理仍未证明。

## 结论先行

保留全部素数幂移位后，偶子空间限制到正半轴的连续跳跃核

\[
K_+(x,y)=k(x-y)+k(x+y),\qquad
k(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}},
\]

不满足 TP2。这个失败不是有限截断造成的：可在有限个有界矩形上选择点，使所有素数幂移位原子都避开这些矩形，而连续部分的 2×2 minor 严格为负。进一步，取两个窄而光滑的正半轴 bump，一正一负，得到一变号输入；真实全跳跃生成元的短时 Markov 半群在正半轴上产生至少两次变号。因此此算子没有可直接用于 Sturm 论证的半轴变差缩减性质。

这排除了“真实 jump kernel 自带 TP/变差缩减”的接口，但没有排除一个专门针对最低偶本征态的节点定理。对绝对值试探，能量差可以精确写出；变分原理给出的恰是所需矛盾方向的反面，故还须证明低态特有的严格下界。

## 1. 全跳跃形式和偶半轴核

采用 round05 的记号

\[
p(x)=2\Phi(x)\cosh(x/2),\quad d\nu=p(x)\,dx,\quad
\alpha_n=\frac{\Lambda(n)}{\sqrt n},\quad a_n=\log n,
\]

以及完整正偶 theta 核 \(\Phi\)。真实闭形式是

\[
\mathcal E(q)=\frac12\iint_{\mathbb R^2}
 \Phi(x)\Phi(y)k(x-y)|q(x)-q(y)|^2\,dx\,dy
 +\sum_{n\ge2}\alpha_n\int_{\mathbb R}
 \Phi(x)\Phi(x+a_n)|q(x)-q(x+a_n)|^2\,dx.                 \tag{1}
\]

\(\alpha_n=0\) 时该项自然消失，但以下没有删除任何非零项。第一项的连续 conductance 密度在对角线附近有 \(k(u)\sim(2|u|)^{-1}\) 奇性；第二项是所有素数幂平移对应的原子 conductance。

对实偶 \(q\)，把 (1) 折到 \(x,y>0\)。连续项的半轴 conductance 密度（乘一个与 convention 有关的正常数，不影响下述符号）为

\[
\widetilde J_c(x,y)=2\Phi(x)\Phi(y)K_+(x,y),\qquad
K_+(x,y)=k(|x-y|)+k(x+y).                              \tag{2}
\]

其 jump-rate kernel 还除以一个只依赖出发点 \(x\) 的正密度因子。故任何 2×2 minor 的符号都由 \(K_+\) 决定：\(\Phi(x)\)、\(\Phi(y)\) 和出发点密度只给正的行列乘子。

折叠后的素数原子只会在

\[
|x-y|=\log n\quad\text{或}\quad x+y=\log n,
\qquad (\Lambda(n)\ne0),                              \tag{3}
\]

产生跨矩形的连接。对任一有界区域，相关 \(n\) 有限多个；所以只要矩形中心的这些距离避开 \(\log n\)，缩小矩形即可让全部原子项都避开。

## 2. 半轴 TP2 的严格反例

对含平移原子的完整跳跃测度，此处使用块定义：任取两有序且不交的行区间 I₁<I₂ 和列区间 J₁<J₂，要求质量矩阵 [J(Iᵢ×Jⱼ)] 的 2×2 行列式非负。以下四个交叉块都与对角及所有素数原子曲线分离，故其质量有限；负块行列式直接反驳该性质。连续核的点值 minor 则作为构造这些块的极限。

取

\[
x_1=1,\quad x_2=2+\delta,\quad y_1=2,\quad y_2=4,
\]

其中 \(\delta>0\) 很小。两行、两列均严格递增，且

\[
\begin{aligned}
K_+(x_1,y_1)&=k(1)+k(3),&K_+(x_1,y_2)&=k(3)+k(5),\\
K_+(x_2,y_1)&=k(\delta)+k(4+\delta),&
K_+(x_2,y_2)&=k(2-\delta)+k(6+\delta).
\end{aligned}
\]

当 \(u\downarrow0\)，

\[
k(u)=\frac{1+O(u)}{2u}\longrightarrow+\infty.
\]

所以

\[
\det\big[K_+(x_i,y_j)\big]_{i,j=1}^2
= [k(1)+k(3)][k(2-\delta)+k(6+\delta)]
-[k(3)+k(5)][k(\delta)+k(4+\delta)]
\longrightarrow -\infty.                              \tag{4}
\]

特别地，存在 \(\delta_0>0\)，使每个 \(0<\delta<\delta_0\) 的 minor 都为负。再取这样的 \(\delta\) 避开有限个禁值：在相关有界距离范围中只有有限个 \(\log n\)；每个原子条件 (3) 对 \(\delta\) 至多排除有限个值。因而可同时保证中心处的全部差、和距离都不等于任何 \(\log n\)。局部有限性允许选取四个足够小的有界区间 \(I_i\ni x_i\)、\(J_j\ni y_j\)，使其四个交叉矩形 \(I_i\times J_j\) 上没有一个素数幂原子连接。

对这些区间积分后的块矩阵满足

\[
\frac{1}{|I_i||J_j|}\iint_{I_i\times J_j}\widetilde J_c(x,y)\,dx\,dy
\longrightarrow \widetilde J_c(x_i,y_j)
\]

当区间直径趋于零。因此其块 minor 与 (4) 同号，取区间足够小后严格为负。因为原子项在这些矩形上恰为零，这也是完整真实跳跃 conductance 的负块 minor，而不只是单独连续项的反例。

结论：真实偶半轴 jump kernel 不是 TP2。普通平移核 \(k(x-y)\) 也可直接看到障碍：在 \(u>0\)，

\[
\frac{d^2}{du^2}\log k(u)=\frac{4e^{2u}}{(e^{2u}-1)^2}>0,
\]

即它在正侧严格对数凸，而平移核 TP2 所需的是对数凹方向。折叠项 \(k(x+y)\) 并没有修复半轴 minor；(4) 是直接针对折叠后的真实核给出的反例。

## 3. 全跳跃 Markov 半群也不是半轴变差缩减

上面的负 minor 已否定 TP2。这里再给出对“最多保留输入变号数”的直接反例，避免把 TP 与某个具体 VD 定义混为一谈。

令 \(y_1=2,y_2=4\)。取 \(w>0\) 很小的非负 \(C_c^\infty\) bump \(u_{1,w},u_{2,w}\)，支撑分别在 \([2-w,2+w]\)、\([4-w,4+w]\)，并归一化

\[
\int_0^\infty \Phi(y)u_{j,w}(y)\,dy=1.
\]

折叠连续出跳积分记为

\[
I_{j,w}(x)=\int_0^\infty \Phi(y)K_+(x,y)u_{j,w}(y)\,dy.
\]

固定 \(x_0=1\) 时，\(I_{1,w}(x_0)/I_{2,w}(x_0)\) 随 \(w\to0\) 收敛到有限正数 \(R_0=K_+(1,2)/K_+(1,4)\)。令 \(x_1=2+2w\)、\(x_2=4-2w\)。在 \(u\in(0,1)\) 上有 \(k(u)\ge c_0/u\)（取某个固定 \(c_0>0\) 即可）。因此 \(y\in[2-w,2+w]\) 时 \(|x_1-y|\in[w,3w]\)，从而 \(I_{1,w}(x_1)\ge c_1/w\)；而 \(I_{2,w}(x_1)=O(1)\)。同理，\(I_{2,w}(x_2)\ge c_2/w\)、\(I_{1,w}(x_2)=O(1)\)。常数与 \(w\) 无关。

选固定 \(c>R_0+1\)。充分小的 \(w\) 给出

\[
I_{1,w}(x_0)-cI_{2,w}(x_0)<0,\quad
I_{1,w}(x_1)-cI_{2,w}(x_1)>0,\quad
I_{1,w}(x_2)-cI_{2,w}(x_2)<0.                         \tag{5}
\]

置 \(q_w=u_{1,w}-c u_{2,w}\) 于正半轴，并作偶延拓。它是偶的、光滑紧支的，且正半轴上恰有一次变号。这里 \(x_0,x_1,x_2\) 均在 \(q_w\) 支撑之外。相应交叉距离在 \(w\to0\) 时只趋于 \(1,2,3,4,5,6,8\) 或 0；正整数不可能等于 \(\log n\)（\(e^r\) 对非零代数数 \(r\) 是超越数），0 又小于 \(\log2\)。局部有限性遂保证 \(w\) 足够小时，所有从三个输出邻域到两个 bump 支撑的素数幂原子都恰为零。

真实跳跃生成元在这些输出邻域没有对角 \(q_w(x)\) 项，也没有素数原子项。由 (1) 的极化，连续项给

\[
(-Lq_w)(x)=\frac{1}{2\cosh(x/2)}
\big(I_{1,w}(x)-cI_{2,w}(x)\big)                    \tag{6}
\]

（若采用等价半轴归一，右侧仅多一个固定正因子）。(5) 表明 \(-Lq_w\) 在按顺序排列的三个小开区间上分别严格为负、正、负。圆滑 bump 使 \(q_w\in D(L)\)。具体地，令 \(f=\Phi q_w\in C_c^\infty\)。在报告中的表示 \(Lq=\tfrac12q+[Af-Sf]/(2h)\) 下，Archimedean 乘子满足 \(w(t)=O(\log(2+|t|))\)，故 \(w\widehat f\in L^2\) 且 \(Af\in L^2\)。变换后的加权平方范数含权 \(\Phi(x)/(2h(x))\)，该权有界。对每个平移项，\(f(x\pm a_n)\) 的支撑移到 \(\pm a_n+\operatorname{supp}f\)，而 \(\Phi(x)/(2h(x))\) 在这些支撑上双指数下降；因此 \(\sum_n\alpha_n f(\cdot\pm a_n)/(2h)\) 在 \(L^2(\nu)\) 绝对收敛。关联算子的形式定义于是给出 \(q_w\in D(L)\)。

令 \(P_t=e^{-tL}\)。对 \(q_w\in D(L)\)，

\[
\frac{P_tq_w-q_w}{t}\longrightarrow -Lq_w
\quad\text{于 }L^2(\nu),\qquad t\downarrow0.
\]

在上述三个区间上 \(q_w=0\)，而 \(-Lq_w\) 有严格符号且连续。故对足够小的正 \(t\)，\(P_tq_w\) 在这三个有序区间的正测度子集上仍依次取负、正、负值。它在正半轴上至少有两次变号，而输入 \(q_w\) 仅一次。于是全跳跃 Markov 半群在偶半轴上不具备“不增加变号数”的变差缩减性质。

此反例使用原始完整 \(\sum_n\) 项：在所选的有限输入—输出矩形上，每个素数幂原子都由几何支撑条件排除；它并没有把完整生成元替换成一个删素算子。这里得到的是对全空间核/半群性质的反例，不是对最低本征态的节点数陈述。

## 4. 绝对值试探：精确差额与缺失不等式

设 \(q\) 为实偶、\(\nu q=0\)、\(\|q\|_{L^2(\nu)}=1\)，且 \(Lq=\lambda q\) 是偶零均值空间的最低非零态。写

\[
q_+=\max(q,0),\quad q_- =\max(-q,0),\quad
a=\nu|q|,
\quad r=|q|-a.
\]

由 \(\nu q=0\)，\(\nu q_+=\nu q_-=a/2\)；又 \(\nu r=0\)、\(\|r\|^2=1-a^2\)。Markov 性给 \(\mathcal E(|q|)\le\mathcal E(q)\)。对真实形式，差额有准确公式

\[
\begin{aligned}
\Delta&:=\mathcal E(q)-\mathcal E(|q|)\\
&=4\iint_{\{q(x)>0\}\times\{q(y)<0\}}
 \Phi(x)\Phi(y)k(x-y)q_+(x)q_-(y)\,dx\,dy\\
&\quad+4\sum_{n\ge2}\alpha_n\int_{\mathbb R}\Phi(x)\Phi(x+a_n)
 \big[q_+(x)q_-(x+a_n)+q_-(x)q_+(x+a_n)\big]dx\ \ge0.       \tag{7}
\end{aligned}
\]

这是把每条异号边上的 \((a+b)^2-(a-b)^2=4ab\) 逐项代入；全部素数幂都保留。变分原理对 \(r\) 给

\[
\mathcal E(r)=\lambda-\Delta\ge \lambda\|r\|^2
=\lambda(1-a^2),
\]

即

\[
\boxed{\Delta\le\lambda a^2.}                       \tag{8}
\]

所以仅凭严格 Markov 收缩 \(\Delta>0\) 得不到矛盾。绝对值方案需要额外证明反向严格界 \(\Delta>\lambda a^2\)。

连续差额的归一化形式显示了难点。令 \(d\mu_\pm=q_\pm d\nu\)、\(m=\nu q_+=\nu q_-=a/2\)，则

\[
\frac{\Delta_c}{a^2}=
\frac14\mathbb E_{(\mu_+/m)\otimes(\mu_-/m)}
\left[\frac{k(x-y)}{\cosh(x/2)\cosh(y/2)}\right].       \tag{9}
\]

被平均的核在 \(x=R,y=R+d\)（固定 \(d>0\)）时为 \(O_d(e^{-R})\)。它没有全局正下界。因此 (7) 的逐边严格正性不能给出所需的统一比较；素数原子也只在精确位移处耦合两符号集，且其单边归一化权重含 \(\alpha_n/[h(x)h(x+a_n)]\)，本身不提供无位置依赖的下界。这个观察否定了无条件的“异号边能量自动压过 \(\lambda a^2\)”论证，不否定特定本征态可能满足更强关系。

这个没有全局下界的说法也可在完整离散项下实现。两个窄 bump 各自按 Φdx 质量一归一化后，再以 ν 质量调幅；当宽度趋零时，调幅比趋于 h(R)/h(R+1)，随 R 趋于无穷约为 exp(−1/2)，保持有界。取固定 \(d=1\)，在 \(R\) 与 \(R+d\) 附近放置两个越来越窄的光滑 bump，前者为正、后者为负，作偶延拓并调幅使 \(\nu q=0\)。选 \(R\to\infty\) 避开 \(2R+d=\log n\)；由于每个有界区间只含有限个 \(\log n\)，可再把支撑宽度取得足够小，使异号支撑间的距离区间完全避开全部 \(\log n\)。同侧异号距离接近 \(d=1\)，也避开全部 \(\log n\)。于是 (7) 的素数原子差额恰为 0。连续项的同侧归一化核为 \(O(e^{-R})\)，异侧（正半轴 bump 与其负半轴镜像）为 \(O(e^{-2R})\)，故 \(\Delta/a^2\to0\)。整体缩放可令 \(\|q\|_2=1\)，不改变该比值。此构造只说明在全体中心化测试函数上不存在正的统一下界；它没有声称这些 bump 是本征函数。

## 5. 对低态节点目标的影响

e93c04f 的 [OSCILLATION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e93c04f13b0ced661bfbba87c533d139cad7ede8/reports/20261011_mellin_saddle_transfer/OSCILLATION.md) 在完整选择输入 S 与标准条带下得出

\[
\tau(q_+)=\tau(q_-)=\alpha-\tfrac12\quad(0<\alpha\le\tfrac12).
\]

因此每个假设的非零低态，其正、负部分都在任意远的右半轴上非零；如果 \(q\) 只有有限次右半轴变号，它最终同号，与这两个有限且相等的增长阶冲突。由此，若能独立证明最低偶低态只有有限次半轴变号，就能排除该态并与现有振荡结论形成矛盾。q 的光滑性与两侧在任意远处均有非零符号值还给出无穷个半轴零点；这不提供节点数的有限上界。Mellin 商的正负值也在实射线上无限交替。

本次检查没有得到这种本征态专属节点定理。round05 的形式非负、常数零态单重、零点附近的有限矩阵正性及本质谱信息均不足以建立它；全核/半群变差缩减这条自然路线已由 §§2–3 反例否定。普通局部 Sturm/Courant 论证也不能直接套用，因为任意两个半轴区域之间存在 Archimedean 连续跳跃，且素数原子继续连接非邻接区间。

## 6. 来源与范围

- round05 真实形式、\(k(u)\)、\(\alpha_n\)、生成元表达和偶低态谱范围：[`rounds/05/REPORT-pages-01-05.txt`](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e93c04f13b0ced661bfbba87c533d139cad7ede8/rounds/05/REPORT-pages-01-05.txt)，尤其式 (3)、(7)、(9) 及关于 \((0,1/2)\) 离散态的范围说明；完整正跳跃截断失隙结论见 [`REPORT-pages-06-10.txt`](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e93c04f13b0ced661bfbba87c533d139cad7ede8/rounds/05/REPORT-pages-06-10.txt) 第 6.2 节。
- e93c04f 完整选择输入及准确增长阶：[`reports/20261011_qrh_selection_bridge/REPORT.md`](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e93c04f13b0ced661bfbba87c533d139cad7ede8/reports/20261011_qrh_selection_bridge/REPORT.md) 第 1–3 节；真实 theta Mellin 正负振荡：[`reports/20261011_mellin_saddle_transfer/OSCILLATION.md`](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e93c04f13b0ced661bfbba87c533d139cad7ede8/reports/20261011_mellin_saddle_transfer/OSCILLATION.md)。
- 绝对值试探 (7)–(9) 是从定义的真实闭形式逐项计算；半轴负 minor 和 VD 反例使用 \(k(u)\sim(2|u|)^{-1}\)、局部有限的移位原子集以及正半轴折叠式 (2)。

本文没有证明或排除任何新的真实低态，也不构成 RH 结论。负块 minor 与半群反例由完整真实形式直接推出；与低态无限变号的联系仍继承完整选择输入。
