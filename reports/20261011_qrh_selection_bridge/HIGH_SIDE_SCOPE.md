# 固定 7/8 探针的高端余量：适用范围与临界线接口

本说明把 [B] 第 5 节保留的高端缺口落实到固定来源 [Q] 的参数和误差。
这里只核对原估计的范围与精确代数，不证明新的高端估计。

## 1. 原高端假设

[Q] `eq:part-II-bootstrap` 在 Part II 全程采用反设及范围

\[
\beta_*>7/8,\qquad
\Delta=\beta_*-7/8\in(0,1/24],\qquad
\kappa=2\beta_*-1=3/4+2\Delta\in(3/4,5/6].
\tag{1}
\]

固定尺度 \(h=13/16\)，信号指数 \(C(s)=s-11/16\)。高端所需比较是
相对于 \(C(\beta_*)\) 的误差下降；若误差先以 \(C(7/8)\) 归一化，
必须再减去 \(C(\beta_*)-C(7/8)=\Delta\)。

在 (1) 与原 row/capacity 条件下，[Q] `eq:adaptive-endpoint` 给

\[
E_{\mathrm{actual}}(h)-\Delta
\le-\frac{49}{440640}-\left(1-\frac h4\right)\Delta
+\epsilon_{\mathrm{total}}
=-\frac{49}{440640}-\frac{51}{64}\Delta+\epsilon_{\mathrm{total}}.
\tag{2}
\]

其他端点和高度预算的统一封闭仍使用对每个固定 \(\Delta>0\) 严格正的主余量

\[
m_{\mathrm{hi}}=\frac{51}{64}\Delta>0,
\qquad m_{\mathrm{lo}}=\Delta>0.
\tag{3}
\]

这些主余量随 \(\Delta\downarrow0\) 趋零。

不能将 (2) 的端点常数 \(49/440640\) 自动赋给所有其他端点。
原封闭已经给出的是 (1) 下的统一预算，而非任意零点上确界下的预算。

## 2. 不能直接延伸到任意 \(\sigma_0>1/2\)

若目标改为任意 \(1/2<\sigma_0<7/8\)，反设只给
\(\beta_*>\sigma_0\)。它允许 \(\beta_*\le7/8\)，所以不再推出
\(\Delta>0\)，也不再满足 (1) 的全部范围。

即使只对 (2) 的右端作形式代数代入，在损失趋零时，

\[
-\frac{49}{440640}-\frac{51}{64}\Delta<0
\quad\Longleftrightarrow\quad
\Delta>-\frac{49}{351135}.
\tag{4}
\]

精确分母由 \(440640\cdot51/64=351135\) 得出。若
\(\Delta\le-49/351135\)，显示的代数右端已不提供严格节省。
这不是在证明真实误差必大，也不是将 (2) 宣称为负 \(\Delta\) 下的有效估计。
即使某个小负值使代数右端为负，原 row 估计、网格条件及 (3) 的统一正预算
仍未被扩展到该值。

固定形式化接口同样保留这个范围：
`FinalAssemblyCertifiedBands.lean` 的 `detectorMesh_pos` 显式要求
\(0<\Delta\)，`DetectorCertifiedBands` 则量化于
\(7/8<\mathrm{HeckeZeroSupremum.beta}\) 以及相应 `HighData`。
这些声明的参数范围不能通过替换目标边界自动扩大。

## 3. 下一项仍需证明的估计

若沿原探针推进到临界线，即使未来证明了低端
\(J_\eta(Z)\ll Z^{-3/16+\epsilon}\)，仍须在每个反设
\(\beta_*>\sigma_0>1/2\) 下，重建同一信号的高端近似

\[
J_\eta(Z)-f_\eta(Z)=O_\eta(Z^{C(\beta_*)-\delta}),
\qquad \delta>0,
\tag{5}
\]

并提供延拓判据所需的全纯乘子条件和对目标字符一致的严格余量。
(2)–(3) 在原范围中的成立不能代替这个新量词下的证明。
本稿没有证明 (5)，也没有改善真实零点排除区域。

## 来源与核验范围

[Q] *The Quasi-Riemann Hypothesis*，`openai/math` 固定提交
[`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` 的 paper.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)：
第 6812–6825 行的 Part II 范围；第 16085–16110 行的适应性端点；
第 16174–16187 行的统一高低余量；第 15686–15696 行的高端误差接口；
第 400–429 行的延拓判据和 (5) 所需量词。相同固定版本的
[`FinalAssemblyCertifiedBands.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Detector/FinalAssemblyCertifiedBands.lean)，
`detectorMesh_pos` 与 `DetectorCertifiedBands`。

[B] 本仓库固定提交
[`4495df1` 的桥接报告](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/REPORT.md)，
第 5–7 节。以上核验针对固定文本的参数范围和有理指数代数，
不将来源扫描或依赖构建进度作为实际 Lean 目标的内核认证。
