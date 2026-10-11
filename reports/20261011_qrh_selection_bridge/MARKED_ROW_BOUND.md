# 完整标记行的统一绝对界：所有平方自由标记与所有正尺度

本稿直接估计 [Q] 的 corrected completed row，保留全部零延拓和字符。
证明一个点态绝对界，其常数不依赖标记的素因子数；没有证明 Gram 抵消、
临界低端估计或新的零点排除。

## 1. 准确物理展开

采用 [C] 的 \(\mathcal B_D(U;m,s)\)，其中 \(D\) 为避开固定坏素数集
\(S\) 的平方自由理想乘积，\(U>0\)。理想由原 primary 生成元表示，
\(q_a\) 为范数。令 \(A=cn^3\)，\(c\) 平方自由，\(c,n\) 均避开 \(S\)。
固定来源的准确展开为

\[
\mathcal B_D(U;m,s)=\sum_{c\,\mathrm{sf},n}
\beta(c,n;s,m)1_{D\mid cn^3}q_c^{-1/2}q_n^{-1}
W_{\mathrm G}\!\left(\frac{q_cq_n^3}{U}\right),
\tag{1}
\]

\[
W_{\mathrm G}(y)=\frac1{2\sqrt\pi}e^{-(\log y)^2/4},
\qquad
\beta=\gamma_2(c)\overline{\alpha(A)}\eta(A)\Xi_*(A)^{-1}
\mathcal R(A,s)\chi_A(m)\overline{G(A)}.
\tag{2}
\]

这里 \(\Xi_*\) 是原算术固定字符修正，不是 Riemann \(\Xi\)。
原行的 \(\mathcal R\) 和 \(G\) 保留：\(G(A)\) 是原文的单位值 ray
延拓，不能改为另一个未归一化 Gauss 和。

所有物理系数均满足 \(|\beta|\le1\)。具体地，\(|\alpha|=1\)，
平方自由 \(c\) 的 \(\gamma_2(c)^3=\mu(c)\alpha(c)\) 给
\(|\gamma_2(c)|=1\)；固定字符在单位处模长一，零延拓在非单位处为零；
\(\mathcal R\) 为单位值的互反修正，\(|G(A)|=1\)。
\(\Xi_*(A)^{-1}\) 只在避开 \(S\) 的单位处计算。

(1) 来自原 \(\Re t=4\) 的 Mellin 积分，因为
\(\mathcal M W_{\mathrm G}(t)=e^{t^2}\) 且
\(U^tq_c^{-t}q_n^{-3t}=(q_cq_n^3/U)^{-t}\)。该线的绝对收敛与
Gaussian 竖向衰减保证逐项反演。全部外部 \(m,s,X,Y\) 归一化因子和
加性 Gauss 和在 \(\mathcal B_D\) 外；它们不属于本行估计。

## 2. 对所有正尺度成立的正项估计

**引理。** 对每个 \(V>0\)，

\[
S(V):=\sum_{c\,\mathrm{sf},n}q_c^{-1/2}q_n^{-1}
W_{\mathrm G}(q_cq_n^3/V)\ll\sqrt V.
\tag{3}
\]

常数只依赖固定理想计数与 Gaussian，不需要 \(V\ge1\)。

**证明。** 理想计数 \(\#\{a:q_a\le H\}=O(H)\) 给：在
\(q_n\asymp N=2^j\)、\(q_c\asymp C=2^k\)、\(j,k\ge0\) 的框上，
不含 Gaussian 的加权质量至多 \(O(C^{1/2})\)。平方自由或避开 \(S\)
的条件只会减小正项和。

框内 \(q_cq_n^3/(CN^3)\) 位于固定紧区间，因此 Gaussian 的上界为
\(C_1\exp[-c_1\log^2(CN^3/V)]\)，其中常数固定。置
\(t=k+3j-\log_2V\)，准确有

\[
C^{1/2}=\sqrt V\,N^{-3/2}2^{t/2}.
\]

对任意实移位 \(b\)，平移格点和

\[
\sum_{k\in\mathbb Z}2^{(k-b)/2}e^{-c_2(k-b)^2}
\]

一致有界：配方后是平移 Gaussian 和，将移位约到 \([0,1]\) 并以
可和尾支配即可。把 \(k\ge0\) 的正项延到全部整数，获得一个不依赖
\(V,N\) 的上界。余下 \(\sum_{j\ge0}2^{-3j/2}\) 收敛，得到 (3)。
这同时覆盖任意小的 \(V\)。证毕。

## 3. 标记分解与无素因子数损失的统一界

**定理。** 对所有平方自由好标记 \(D\)、全部 \(U>0\) 和原允许行参数，

\[
\boxed{|\mathcal B_D(U;m,s)|\ll\frac{\sqrt U}{q_D}.}
\tag{4}
\]

常数与 \(D,U,m,s\) 及 \(\omega(D)\) 无关；没有固定槽数或
\(q_D\le Z^{1/6}\) 的前提。

**证明。** 对每个被标记项准确定义

\[
E=\prod_{\substack{p\mid D\\p\mid c}}p,\qquad F=D/E.
\]

这是所有项的互斥划分。每个 \(p\mid F\) 均不整除 \(c\)，而
\(D\mid cn^3\) 强制 \(F\mid n\)。于是写 \(c=Ec_0\)、\(n=Fn_0\)。
\(c_0\) 仍平方自由，且不含 \(D\) 的素因子；\(n_0\) 可以和 \(E\) 或
\(c_0\) 共享素数。此处没有假设 \((c,n)=1\)。

取绝对值，再删去剩余限制，只增大正项和。外部权重与剩余尺度准确为

\[
q_E^{-1/2}q_F^{-1},\qquad
V=\frac{U}{q_Eq_F^3}.
\]

由 (3)，该份至多为

\[
q_E^{-1/2}q_F^{-1}S\!\left(\frac{U}{q_Eq_F^3}\right)
\ll\frac{\sqrt U}{q_Eq_F^{5/2}}
=\frac{\sqrt U}{q_D}\,q_F^{-3/2}.
\tag{5}
\]

最后保留这个衰减权，不将每份都替换为同一个常数：

\[
\sum_{F\mid D}q_F^{-3/2}
\le\sum_{a\text{ 非零理想}}q_a^{-3/2}<\infty.
\tag{6}
\]

收敛同样由理想计数 \(O(H)\) 的 dyadic 分组得到。因此总常数不依赖
\(\omega(D)\)，没有 \(2^{\omega(D)}\) 损失。将 (5) 对全部份求和即得 (4)。
证毕。

## 4. 原补偿尺度的推论与边界

在原标记尺度 \(U=Zq_D\) 上，(4) 直接给

\[
\boxed{|\mathcal B_D(Zq_D;m,s)|\ll Z^{1/2}q_D^{-1/2}.}
\tag{7}
\]

它对任意标记大小成立；不需要把 \(D\) 限制在固定总长度的窗口。
本稿是绝对值估计，不使用行间相关。它没有证明 [B] 的 (R4) 或
`GRAM_INTERFACE.md` 的整体能量目标；不能把 (7) 当成那些均方或相关和
已达标的结论。真实补偿系数 \(q_r\)、Gauss 和及公共权重仍必须在探针
整体估计中保留。

## 5. 固定来源与核验

[Q] `openai/math` 固定提交
[`fd4aeeb2` 的 paper.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)：
第 3349–3412 行的 \(\Psi\)、完整 corrected row 和一般探针；
第 1288–1314 行的 Gaussian Mellin 归一化；第 8083–8137 行的标记行
与物理反演；第 934–972 行的互反修正与 \(\gamma_2\) 身份。
本稿使用的是这些对象的定义和绝对收敛，不使用外部 7/8 零点定理。

[C] 固定提交
[`4495df1` 的补偿重排](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/COMPENSATION.md)，
第 1–2 节，尤其 \(\mathcal B_D\) 的定义、\(U=Zq_D\) 与准确重缩放系数。

[B] 同一提交的 [桥接报告](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/REPORT.md)，
第 5–7 节的未证相关目标。

正文的 Gaussian 平移和、理想计数及标记划分是独立解析证明。
随附 `check_gram_geometry.py` 只复算 (5) 的范数幂及先前接口的精确代数，
不验证任何未证的相关抵消或形式化目标。
