# 完整 Green 异常谱带的对数源代价与定量负谱转移

日期：2026-10-14。证明输入快照：`1cece5ec907004c5e1693148d223cbe75eeec1b3`。

交付前另核对到最新提交 `de454157629b8aa275df0bfee8cf9369a69ee54a`。该提交仅新增旧 **3/2 上界**的复核文 `REFEREE_THREE_HALVES_BOUND.md`，没有修改本稿调用的前提文件。本稿已读完该复核文；它不是对本轮新定理的独立复核。

状态：新增辅助谱估计的完整证明稿，交给 dot 独立复核；未写入仓库。本稿不证明 RH，不声称新增 ζ 零点排除。标量核验已经运行，但不等于算子证明的独立审查。

## 0. 结果与准确范围

沿用仓库原来的完整算子、梯度空间、中心化源以及全部素数幂。令
\[
\mathscr A=T^*T\quad\text{作用于 }K_P,\qquad K=TT^*\quad\text{作用于 }K_N.
\]
给定 \(\varepsilon>0\)，定义
\[
E_\varepsilon=\operatorname{Ran}\mathbf1_{[1+\varepsilon,\infty)}(\mathscr A),
\qquad \delta_0=\frac{\varepsilon}{1+\varepsilon}.
\]
对于 \(a\in E_\varepsilon\)，令 \(r_a\) 是其实际中心化比值源，\(g_a=\psi r_a\)，并令
\[
\mathcal U a=(g_a)_o/m
\]
为其原奇物理空间中的源向量。下标 \(o\) 表示奇延拓。

**定理 A。** 映射 \(\mathcal U:E_\varepsilon\to\mathcal Q(H_o)\) 是良定义、线性、单射的，且对整个谱带的任意向量成立
\[
\boxed{\quad
\|\mathcal U a\|_{L^2(\mathbb R)}^2
\le C_\varepsilon\|a\|_P^2,
\qquad C_\varepsilon=8705+544\log\frac{1+\varepsilon}{\varepsilon}.
\quad} \tag{A}
\]
这里没有谱带维数、所选本征向量个数或分离度因子。保留全部极化混合项，并且
\[
\mathfrak h_o[\mathcal U a]
=\langle a,(I-\mathscr A)a\rangle_P
\le-\varepsilon\|a\|_P^2. \tag{B}
\]
因此
\[
\boxed{\quad
\operatorname{rank}\mathbf1_{[1+\varepsilon,\infty)}(K)
\le
\operatorname{rank}\mathbf1_{(-\infty,-\varepsilon/C_\varepsilon]}(H_o).
\quad} \tag{C}
\]
这是固定谱深度的计数比较，不只是原有的总负惯性相等，也不声称逐个本征向量对应或两个完成空间之间存在有界相似。

**推论 B。** 再使用仓库已有的原奇物理下界 \(H_o\ge-10^{-5}I\)，有
\[
\boxed{\qquad 0\le K\le\frac{21}{20}I.\qquad} \tag{D}
\]
本推论并非定理 A 的对数常数优化，而是其中心区估计与原有固定截断尾证书的直接组合。没有重新做 ζ 零点验证。

尚未解决的是 \(1<\lambda<21/20\)，尤其是趋近 1 的异常谱。本稿也没有解决 `INFINITE_HIGH_TAIL.md` 中实际采样系数的 \(\kappa^{-2}\) 代价或低频与高频之间的有符号耦合。

## 1. 使用的原对象与已建立输入

所有下列文件固定在上述提交。链接中的节号说明本稿具体使用的位置。

1. [THREE_HALVES_BOUND.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1cece5ec907004c5e1693148d223cbe75eeec1b3/reports/20261013_full_prime_green_reference/THREE_HALVES_BOUND.md)，§§1–5、Appendix A：实际源接口、常数 193、完整外行与物理尾界、奇物理下界。
2. [supercritical_source_tails/REPORT.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1cece5ec907004c5e1693148d223cbe75eeec1b3/reports/20261013_supercritical_source_tails/REPORT.md)：中心化源、实际辅助算子定义域、合法截断与 Gamma 跨边界块。
3. [green_spectral_interfaces/REPORT.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1cece5ec907004c5e1693148d223cbe75eeec1b3/reports/20261013_green_spectral_interfaces/REPORT.md)，§§4–5：共同核上的完整形式恒等式、极分解及原有总惯性接口。
4. [compact_green_excess/REPORT.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1cece5ec907004c5e1693148d223cbe75eeec1b3/reports/20261013_compact_green_excess/REPORT.md)：\((K-I)_+\) 紧，以及中心化源映射在实际 \(P\)-完成上的连续性。
5. [ORIGINAL_FORM_FOUNDATION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1cece5ec907004c5e1693148d223cbe75eeec1b3/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md)，§§5–6，及 [odd_operator_domains/REPORT.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1cece5ec907004c5e1693148d223cbe75eeec1b3/reports/20261013_odd_operator_domains/REPORT.md)，开头的归一化与定义域：原完整奇物理形式域。
6. [INFINITE_HIGH_TAIL.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1cece5ec907004c5e1693148d223cbe75eeec1b3/reports/20261013_growing_rank_source_estimates/INFINITE_HIGH_TAIL.md)，§§5–6：用于核对未完成问题与范围，不作为新定理的证明前提。

另读了最新提交中的 [REFEREE_THREE_HALVES_BOUND.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/de454157629b8aa275df0bfee8cf9369a69ee54a/reports/20261013_full_prime_green_reference/REFEREE_THREE_HALVES_BOUND.md)。它确认上述原奇形式归一化、193 参考预算、完整行预算以及原物理下界，未增加或修改本稿的假设。

内积对第一变量共轭线性。正半轴上令
\[
\psi=-\Phi'>0,\quad s=\sinh(x/2),\quad w=\psi s,
\quad m^2=\frac{\Phi}{2\cosh(x/2)},
\quad d_n=\log n,\quad\alpha_n=\Lambda(n)n^{-1/2}.
\]
原来的完整能量为
\[
\begin{aligned}
P_\Gamma[r]&=\iint\psi(x)\psi(y)
 [k(|x-y|)-k(x+y)]|r(x)-r(y)|^2\,dx\,dy,\\
P_{\rm pole}[r]&=4\iint w(x)w(y)|r(x)-r(y)|^2\,dx\,dy,\\
P_F[r]&=2\sum_{n\ge2}\alpha_n\int_0^\infty\psi(x)\psi(x+d_n)
 |r(x)-r(x+d_n)|^2\,dx,\\
N[r]&=\sum_{n\ge2}\alpha_n\int_0^{d_n}\psi(x)\psi(d_n-x)
 |r(x)-r(d_n-x)|^2\,dx,
\end{aligned}
\]
其中 \(k(t)=e^{-t/2}/(1-e^{-2t})\)，\(P=P_\Gamma+P_{\rm pole}+P_F\)。所有和式均含全部素数幂。

\(K_P\) 是原紧光滑比值核的 \(P\)-梯度闭包，\(\|a\|_P^2=P[r_a]\)。原源定理给出唯一中心化表示
\[
\int_0^\infty wr_a=0,\qquad \int_0^\infty w=\frac18.
\]
故准确地有
\[
\int_0^\infty w|r_a|^2=P_{\rm pole}[r_a]\le\|a\|_P^2. \tag{1}
\]
这不是把系数二的源极点删掉，而是保留它产生的正方差能量，再采用其中心化代表。

定义完整反射行与辅助变量
\[
L(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x),\qquad
\mu^2=\frac\psi L,\qquad Va=\frac{g_a}{\mu}.
\]
已有参考逆定理及其认证常数给出全完成上的界
\[
\|V\|_{K_P\to L^2(0,\infty)}^2\le193. \tag{2}
\]
并有
\[
\frac{\mu(x)^2}{m(x)^2}\le2048e^{3x}\quad(x\ge0). \tag{3}
\]
原源闭形式恒等式把 \((g_a)_o\) 连续地放入完整 Gamma 对数形式域。一旦证明 \((g_a)_o/m\in L^2\)，原物理最大形式域的描述便给出 \(\mathcal U a\in\mathcal Q(H_o)\)，以及 (B) 的等式。无需假设 \(\mathcal U a\in D(H_o)\)。

## 2. 新的 theta 权比引理

**引理 1。** 对所有 \(x>0\)，
\[
\boxed{\quad \frac{\psi(x)}{m(x)^2\sinh(x/2)}\le136e^{2x}.\quad} \tag{4}
\]

**证明。** 置 \(u_n=\pi n^2e^{2x}\)，并把完整 theta 和写成
\[
\Phi=\sum_{n\ge1}f_n,\qquad
f_n=e^{x/2}(4u_n^2-6u_n)e^{-u_n}>0.
\]
令 \(p_n=f_n/\Phi\)，\(q=-\Phi'/\Phi=\psi/\Phi\)，以及
\[
q_n=-\frac{f_n'}{f_n}
=2u_n-\frac92-\frac6{2u_n-3}.
\]
完整和及其导数在每个紧区间正常收敛，故
\[
q=\sum_np_nq_n,\qquad
q'=\sum_np_nq_n'-\left(\sum_np_nq_n^2-q^2\right)
\le\sum_np_nq_n'. \tag{5}
\]
这里减去的是正权方差，未假设任何 ζ 零点性质。又因为 \(u_n\ge\pi>3\)，
\[
q_n'=4u_n+\frac{24u_n}{(2u_n-3)^2}\le4u_n+8. \tag{6}
\]
完整 theta 尾满足
\[
\sum_{n\ge1}n^6e^{-u_1(n^2-1)}\le\frac{65}{64}.
\]
一个直接证明如下：对 \(n\ge2\)，将 \(u_1\) 换成下界 3，邻项比不超过 \((3/2)^6e^{-15}<1/4\)；因此尾不超过 \((4/3)64e^{-9}<1/64\)。后一个不等式可由 \(e^3>20\) 得到。

分母保留 \(n=1\) 项的下界 \(2e^{x/2}u_1^2e^{-u_1}\)，分子将每项的 \(4u_n^2-6u_n\) 上界为 \(4u_n^2\)，得
\[
\sum_np_nu_n\le2u_1\sum_{n\ge1}n^6e^{-u_1(n^2-1)}
\le\frac{65}{32}\pi e^{2x}.
\]
代入 (5)–(6)，用 \(\pi<22/7\) 和 \(e^{2x}\ge1\)，得到
\[
q'\le\left(\frac{65\pi}{8}+8\right)e^{2x}
<34e^{2x},
\]
因为 \(65(22/7)/8+8=939/28<34\)。theta 的真实偶性给出 \(q(0)=0\)，故
\[
q(x)\le17(e^{2x}-1).
\]
于是
\[
\frac{\psi}{m^2s}=2\coth(x/2)q
\le34\coth(x/2)(e^{2x}-1)
=34e^{2x}(1+e^{-x})^2\le136e^{2x}.
\]
引理得证。特别是对任何已有中心化比值源和任何 \(R>0\)，(1) 给出
\[
2\int_0^R\frac{|g_a|^2}{m^2}\,dx
\le272e^{2R}\|a\|_P^2. \tag{7}
\]
式 (7) 是正中心能量的估计，不涉及空间外尾的谱分母。

## 3. 从单个本征源到整段谱：没有维数损失

由紧正超额定理和 \(T\) 的极分解，\(E_\varepsilon\) 有限维。定义其上的正算子
\[
\Delta=I-\mathscr A^{-1}|_{E_\varepsilon},\qquad
\delta_0I\le\Delta<I,\qquad\|I-\Delta\|\le1. \tag{8}
\]

下面仅使用这个有限维性作定义域论证，最终常数不依赖维数。令 \(\mathcal B=B_N\ge0\) 为原辅助半轴正 Gamma 算子，其形式是 \(q_b[(\mu v)_o]\)。沿用原报告中的完整有界算子
\[
\mathcal F=\sum_{n\ge2}\alpha_n(A_n^++A_n^-),\qquad
\mathcal R=\sum_{n\ge2}\alpha_nB_n,\qquad e=s\mu,
\]
其中
\[
A_n^+=M_\mu\tau_{d_n}M_\mu,\quad A_n^-=(A_n^+)^*,\quad
B_n=M_\mu\mathcal R_{d_n}M_\mu.
\]
\(\mathcal R_{d_n}\) 是 \((0,d_n)\) 上的反射，\(\tau_dv(x)=v(x+d)\)。全部和式在算子范数下收敛。

对 \(\mathscr A a=\lambda a\)，原源报告已在实际辅助算子域证明
\[
\mathcal BVa-2C_0\mu^2Va-2\mathcal FVa
+2(1-\delta)\mathcal RVa-8e\langle e,Va\rangle
=-2\delta Va,
\qquad\delta=1-\lambda^{-1}.
\]
在 \(E_\varepsilon\) 的本征基上合并这些恒等式，得到准确的算子柱方程
\[
\mathcal BV+2V\Delta
=2C_0M_{\mu^2}V+2\mathcal FV
+8|e\rangle\langle e|V-2\mathcal RV(I-\Delta). \tag{9}
\]
没有把不同 \(\delta\) 替成同一个数，也未假设 \(V\) 与 \(\Delta\) 可交换。极点项虽因中心化而为零，仍完整保留在 (9) 及下述行预算中。

取 \(Q_R=\mathbf1_{(R,\infty)}\)，\(R\ge7/5\)。原报告已经证明：这个投影保持实际 Gamma 形式域；外侧限制形式给出正自伴算子 \(\mathcal B_R\)，且跨边界形式是有界块
\[
\mathcal C_R=Q_R\mathcal B(I-Q_R),\qquad
\|\mathcal C_R\|\le E_N(R).
\]
这里的块记号按形式理解，而不是先假设截断保持全算子域。将 (9) 与外侧形式域向量配对，令 \(X_R=Q_RV\)，得到
\[
\mathcal B_RX_R+2X_R\Delta=Y_R, \tag{10}
\]
其中
\[
\begin{aligned}
Y_R={}&2C_0Q_RM_{\mu^2}V+2Q_R\mathcal FV
+8Q_R|e\rangle\langle e|V\\
&-2Q_R\mathcal RV(I-\Delta)
-\mathcal C_R(I-Q_R)V.
\end{aligned}
\]
完整行预算为
\[
\begin{aligned}
\|Y_R\|\le\bigl[&2C_0\mu_R^2+8\|Q_Re\|\|e\|+E_N(R)\\
&+2\sum_{n\ge2}\alpha_n\{
\|Q_RA_n^+\|+\|Q_RA_n^-\|+\|Q_RB_n\|\}\bigr]\|V\|.
\end{aligned}
\]
原 `THREE_HALVES_BOUND.md` §4 的推导把 \(1-\delta\) 上界为 1；因而原样适用于这里的 \(\|I-\Delta\|\le1\)。所有外侧素数幂都由其完整 Stieltjes 尾支付，得到
\[
\|Y_R\|\le256e^RM(R)\|V\|,
\qquad M(R)=128e^{7R/2-\pi e^{2R}/2}. \tag{11}
\]

**定义域与 Sylvester 积分。** (10) 的右侧有界。逐列取 \(\Delta\) 的本征向量，弱形式等式说明 \(X_Ra\in D(\mathcal B_R)\)，并给出
\((\mathcal B_R+2\delta)X_Ra=Y_Ra\)。因此其唯一解是
\[
X_R=\int_0^\infty e^{-t\mathcal B_R}Y_Re^{-2t\Delta}\,dt. \tag{12}
\]
这个积分在算子范数中收敛，因为 \(\mathcal B_R\ge0\)、\(\Delta\ge\delta_0I\)。不等式
\[
\|X_R\|\le\frac{\|Y_R\|}{2\delta_0}
\]
直接按算子范数成立，而不是先逐列相加。使用 (2) 与 (11)，得到
\[
\boxed{\quad
\|Q_RV|_{E_\varepsilon}\|^2
\le193\,2^{28}\delta_0^{-2}e^{9R-\pi e^{2R}}.
\quad} \tag{13}
\]
这一步控制了任意线性组合中的全部源范数混合项。一般不能仅从每个本征向量的同样标量界推出 (13)，因为直接相加会引入维数代价。

## 4. 完整物理空间外尾与形式域

固定 \(a\in E_\varepsilon\)，令
\[
F_a(R)=\int_R^\infty|Va|^2\,dx.
\]
式 (13) 对所有 \(R\ge7/5\) 给出统一界。由 (3)，Stieltjes 分部积分得到
\[
\begin{aligned}
\int_R^\infty\frac{\mu^2}{m^2}|Va|^2\,dx
&\le2^{11}\left[e^{3R}F_a(R)
+3\int_R^\infty e^{3x}F_a(x)\,dx\right]\\
&\le193\,2^{40}\delta_0^{-2}
 e^{12R-\pi e^{2R}}\|a\|_P^2. \tag{14}
\end{aligned}
\]
无穷边界项由 (13) 消失。末步使用
\[
\int_R^\infty e^{12x-\pi e^{2x}}dx
\le\frac{e^{12R-\pi e^{2R}}}{2\pi e^{2R}-12},
\qquad2\pi e^{2R}-12>84,
\]
以及 \(1+3/84<2\)。这与原物理尾证明使用相同的完整权比和尾积分，但现已对整个谱带成立。

由 (7)、(14)，\(\mathcal Ua\in L^2(\mathbb R)\)，并且
\[
\boxed{\quad
\|\mathcal Ua\|^2
\le\left[272e^{2R}
+193\,2^{41}\delta_0^{-2}e^{12R-\pi e^{2R}}\right]\|a\|_P^2,
\quad R\ge7/5.
\quad} \tag{15}
\]
式 (15) 已包含奇延拓的全线因子二。结合原源映射的完整对数形式域连续性及原物理最大形式域，得到 \(\mathcal Ua\in\mathcal Q(H_o)\)。完整源形式恒等式随之成立：
\[
\mathfrak h_o[\mathcal Ua]
=P[r_a]-N[r_a]
=\langle a,(I-\mathscr A)a\rangle_P.
\]
中心化令原系数二的极点配对为零；它的正方差能量已在 (1)、(7) 中使用。这里没有把极点从算子定义中移除，也没有将 \(\mathcal Ua\) 误当作 \(H_o\) 的本征向量。

## 5. 对数代价及谱深度比较

设 \(L_0=\log(1/\delta_0)\ge0\)，在 (15) 中取
\[
t=e^{2R}=32+2L_0.
\]
于是 \(R\ge7/5\)。因为
\[
t^6\le32^6e^{3L_0/8},\quad\pi>3,\quad193<2^8,\quad e>2,
\]
(15) 的尾项系数满足
\[
\begin{aligned}
193\,2^{41}e^{2L_0}t^6e^{-\pi t}
&<2^{79}e^{-96}e^{-29L_0/8}\\
&<2^{-17}<1.
\end{aligned}
\]
从而
\[
\|\mathcal Ua\|^2
\le[272(32+2L_0)+1]\|a\|_P^2
=(8705+544L_0)\|a\|_P^2.
\]
这证明 (A)。若 \(a\ne0\)，(B) 严格为负，所以 \(\mathcal Ua\ne0\)，证明单射性。

对 \(\mathcal UE_\varepsilon\) 中任意非零向量，
\[
\frac{\mathfrak h_o[\mathcal Ua]}{\|\mathcal Ua\|^2}
\le-\frac{\varepsilon}{C_\varepsilon}.
\]
原奇物理负谱在每个固定负深度处有限维。极小极大原理因此给出
\[
\dim E_\varepsilon\le
\operatorname{rank}\mathbf1_{(-\infty,-\varepsilon/C_\varepsilon]}(H_o).
\]
\(T\) 的极分解保持 \(TT^*\) 与 \(T^*T\) 的非零谱带秩，得到 (C)，定理 A 得证。

## 6. 完整算子上界 21/20

这一推论只需 (15) 的固定截断版本，单个异常本征源便已足够。

反设 \(K\) 有本征值 \(\lambda\ge21/20\)。取其对应的 \(\mathscr A\) 本征梯度 \(a\)，使 \(\|a\|_P^2=1\)。于是
\[
\delta=1-\lambda^{-1}\ge\frac1{21},\qquad
\mathfrak h_o[\mathcal Ua]=-(\lambda-1).
\]
在 (15) 取 \(R=7/5\)，使用原证书中的
\[
2^{40}e^{84/5-\pi e^{14/5}}<\frac1{1000}
\]
以及 \(e^{14/5}<17\)，得
\[
\begin{aligned}
\|\mathcal Ua\|^2
&<272\cdot17+\frac{2\cdot193\cdot21^2}{1000}\\
&=\frac{2397113}{500}<5000.
\end{aligned} \tag{16}
\]
但已有的 \(H_o\ge-10^{-5}I\) 给出
\[
\lambda-1
\le10^{-5}\|\mathcal Ua\|^2
<\frac{2397113}{50000000}<\frac1{20},
\]
矛盾。最后用 \((K-I)_+\) 紧，将全部 \(\lambda\ge21/20\) 本征值的排除提升到整个 Green 空间的算子上界 (D)。不是有限电流或有限素数矩阵的断言。

## 7. 假设、核验和未解决的一步

**额外假设。** 定理 A 没有添加 RH、零点分离、单零点、核穷尽、有限素数、有限总零点秩等假设。它调用 §1 明列的原完整算子与定义域定理及认证常数。推论 B 额外调用的是仓库已使用的 \(H_o\ge-10^{-5}I\)，后者依赖既有高度 \(3\cdot10^{12}\) 的零点验证；本轮没有做新的零点验证。

**本轮实际核验。** `verify_green_band.py` 使用 Python 标准库的有理数运算、指数 Taylor 余项与反正切交错级数包络，核验了 theta 引理的有理系数、\(e^{14/5}<17\)、原物理尾标量 \(<1/1000\)、对数吸收常数及最终严格矛盾余量
\[
\frac1{20}-\frac{2397113}{50000000}
=\frac{102887}{50000000}>0.
\]
脚本已执行，输出见 `verification.json`。此外本轮用符号代数核对了 \(q_n\) 与 \(q_n'\) 的两个有理式恒等式。没有将数值试验当作无限维证明，也没有宣称 proof-assistant 认证或独立同行审查。

**精确边界。** 未证明 \(K\le I\)。对数界仍容许足够小的正 \(\varepsilon\) 满足 \(\varepsilon\le10^{-5}C_\varepsilon\)。谱带内部的源范数混合项控制，不等于 `INFINITE_HIGH_TAIL.md` 的低频与高频有符号形式耦合；其实际 \(\kappa^{-2}\) 采样系数问题在本稿中原样保留。没有把这些不同缺口混为一谈。

**复核重点。** 新证明的关键是 §2 的正权方差恒等式与 §3 的实际形式域 Sylvester 方程。二者分别负责中心物理权比和整段谱带的维数无关外尾。所有原有限高度、原完整行及定义域输入均已明确列出，便于 dot 分别审核。