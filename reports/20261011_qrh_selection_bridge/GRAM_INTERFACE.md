# 完整补偿和的有限域 Gram 目标

本文只给出一个有限公共频率域上的充分估计目标。所有字符、零延拓、原始素数窗口及重缩放因子均沿用补偿恒等式中的定义；特别地，以下记号没有把任何原字符替换为忽略非单位值的函数。本文不证明所需的幂次节省，也不处理高端延拓估计。

令
\[
X=Z^{17/48},\qquad Y=Z^{23/48},\qquad q_b=q_{b_*},
\]
其中 \(q_b\) 是固定常数。取由原测试函数支撑确定的公共有限环带域
\[
D_Z=\{(s,m):s\text{ primary 且避开 }S,\ q_s\asymp Y;\quad
m\in\mathcal O\setminus\{0\},\ q_m\asymp q_bq_sX\}.
\]
隐含的环带常数只依赖固定测试函数。公共权重为
\[
\mathcal C(s,m)=
\frac{W_1(q_s/Y)W_0(q_m/(q_bq_sX))\chi_s(b_*)\xi(m)}
{Y\tau\xi(s)\sqrt{q_bq_sX}\sqrt{q_s}}.
\]
对于完整补偿和中的标签 \(\lambda=(J,\mathbf p)\)，令
\[
a_\lambda(s,m)=(-1)^{|J|}
\left(\prod_i W_i(q_{p_i}/P_i)\right)U_{J,\mathbf p}(s,m),
\qquad
\mathcal F_Z(s,m)=\sum_\lambda a_\lambda(s,m).
\]
这里对 \(J\) 和原允许素数数组 \(\mathbf p\) 求和，且 \(U_{J,\mathbf p}\) 是完整补偿重排式中的量，保留其中的 \(q_r\)、商变量、Gauss 和、标记完整行及全部字符。

记补偿探针的未归一化重排和为
\[
\mathfrak P_Z=\sum_{(s,m)\in D_Z}\mathcal C(s,m)\mathcal F_Z(s,m).
\]
公共权重只需在这个有限域上估计。在 \(D_Z\) 上，固定算术因子有界，且
\[
|\mathcal C(s,m)|\ll
\frac1{Y\sqrt{q_sX}\sqrt{q_s}}
\asymp Y^{-2}X^{-1/2}.
\]
由于 \(\mathcal O\) 是二维格子，环带中有 \(O(Y)\) 个 primary \(s\)；给定这样的 \(s\)，满足 \(q_m\asymp q_sX\) 的 \(m\) 有 \(O(XY)\) 个。因此 \(|D_Z|\ll XY^2\)，从而
\[
\sum_{D_Z}|\mathcal C(s,m)|^2
\ll XY^2\cdot Y^{-4}X^{-1}=Y^{-2},
\qquad
\|\mathcal C\|_{\ell^2(D_Z)}\ll Y^{-1}=Z^{-23/48}.
\]
这只是公共有限支撑上的范数界，不是全频率空间的 \(\ell^2\) 断言。

由 Cauchy–Schwarz，以下是得到所需低端探针幂次的一个新的充分目标：对每个 \(\varepsilon>0\)，证明
\[
\boxed{\quad \|\mathcal F_Z\|_{\ell^2(D_Z)}
\ll_\varepsilon Z^{7/24+\varepsilon}.\quad}
\]
它等价（在任意小 \(\varepsilon\) 的记号下）于能量上界
\[
\sum_{D_Z}|\mathcal F_Z(s,m)|^2\ll_\varepsilon
Z^{7/12+\varepsilon}.
\]
若该目标成立，则
\[
|\mathfrak P_Z|
\le \|\mathcal C\|_{\ell^2(D_Z)}\|\mathcal F_Z\|_{\ell^2(D_Z)}
\ll_\varepsilon Z^{-23/48+7/24+\varepsilon}
=Z^{-3/16+\varepsilon}.
\]
这里的指数计算是 \(-23/48+14/48=-9/48=-3/16\)。这只是待证的充分条件；当前材料没有证明该范数节省，也没有证明它是必要条件。

为明确这个目标中的交叉相关，令
\[
G_{\lambda,\lambda'}=
\sum_{(s,m)\in D_Z}a_\lambda(s,m)\overline{a_{\lambda'}(s,m)}.
\]
则完整 Gram 展开为
\[
\begin{aligned}
\|\mathcal F_Z\|_{\ell^2(D_Z)}^2
&=\sum_{\lambda,\lambda'}G_{\lambda,\lambda'}\\
&=\sum_{J,\mathbf p}\sum_{J',\mathbf p'}
(-1)^{|J|+|J'|}
\sum_{D_Z}
\left(\prod_iW_i(q_{p_i}/P_i)\right)
\overline{\left(\prod_iW_i(q_{p'_i}/P_i)\right)}
U_{J,\mathbf p}(s,m)\overline{U_{J',\mathbf p'}(s,m)}.
\end{aligned}
\]
若两个标签在同一 slot \(i\) 使用同一素数 \(p_i=p'_i\)，但 \(i\in J\) 與 \(i\notin J'\)（或反之），则其局部支撑要求同时有 \(p_i^2\mid m\) 和 \(p_i\nmid m\)，故该 Gram 项为零。这给出一类精确的支撑正交。若没有这种矛盾，整除条件相容只表示允许支撑可能相交；它不能推出对应的真实完整行非零，也不能给出 Gram 项的大小。因而不能仅凭此局部检查断言整个标签族正交。

还可对一对标签给出一个粗的允许支撑计数。设 \(R\) 是这两个标签中被各自子集 \(J,J'\) 选中的素数的并集，重复素数只计一次，并记其范数为 \(q_R\)。在两标签的局部整除条件相容时，任何共同允许频率均满足
\[
R\mid s,\qquad R^2\mid m.
\]
按 Eisenstein 整数环中的主理想格点计数，
\[
\#\{s:q_s\asymp Y,\ R\mid s\}\ll 1+Y/q_R,
\]
且对每个这样的 \(s\)，
\[
\#\{m:q_m\asymp q_bq_sX,\ R^2\mid m\}
\ll 1+XY/q_R^2.
\]
因此这对标签的共同允许支撑大小至多
\[
\ll (1+Y/q_R)(1+XY/q_R^2).
\]
令 \(e\) 为 \(R\) 中素数窗口尺度指数之和。每个标签的选中尺度总和至多 \(\ell=1/6\)，所以并集满足 \(e\le 2\ell=1/3\)，而固定环带素数窗口给出双向比较 \(q_R\asymp Z^e\)。于是
\[
\frac{Y}{q_R}\gg Z^{23/48-e}\ge Z^{7/48},\qquad
\frac{XY}{q_R^2}\gg Z^{5/6-2e}\ge Z^{1/6}.
\]
两个因子均趋于无穷，故上式进一步成为
\[
\#\{\text{共同允许 }(s,m)\}
\ll \frac{XY^2}{q_R^3}
\ll Z^{21/16-3e},
\]
其中 \(XY^2\) 的指数是 \(17/48+2(23/48)=21/16\)。这是每对标签的整除允许支撑计数；它本身不是 Gram 相关估计，也不控制完整行的振荡或大小。

因此，有限域 Gram 目标把需要的新输入明确化为对完整标签和的能量节省。它尚未提供该节省，亦未解决原报告中的高端条件。


## 固定出处与核验范围

[C] 本仓库固定提交 [`4495df1` 的补偿重排](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/COMPENSATION.md)，式 (4)–(10)。

[B] 同一提交的 [桥接报告](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/REPORT.md)，第 5–7 节。

[Q] `openai/math` 固定提交 [`fd4aeeb2` 的 paper.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，`eq:compensated-probe-definition`。上文的未归一化对象准确为该有限修改探针；转为 `J_eta` 的固定对数归一化可吸收到任意小的正指数余量。这里没有改变原补偿因子或素数窗口。

新结果的核验范围为有限恒等式、二维格点计数与准确有理指数。Gram 目标仍未证明，且它是充分条件，不是 RH 的必要条件；线性探针求和还可能采用其他抵消路径。

`check_gram_geometry.py` 以精确有理数复算公共范数幂、并集计数幂、低端目标及高端形式阈值，并检查同素数反状态的局部正交。脚本不计算真实 row，也不证明所需 Gram 节省。
