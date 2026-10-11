# 固定 7/8 输入的实际 Lean 验收与数学范围

本文补全 [B] 所引用输入 Q 的形式化验收。固定来源是 `openai/math` 提交
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`；使用其锁定的 Lean 4.34.1、
mathlib 提交 `d13f23b723b8a846827a245b89c10fc7d3f11612` 与原依赖清单。
依赖兼容性处理采用该固定仓库自带的补丁；没有修改 OAI 数学源码或
mathlib 源码，没有用新增假设补足目标证明。

## 1. 实际验收结果

两个真实公开入口分别构建成功：

- `OAI.NumberTheory.DirichletL.Nonvanishing`
- `OAI.NumberTheory.DirichletL.Hecke.Nonvanishing`

附带的 `accept_qrh.lean` 在这个固定项目环境中实际检查成功。
它导入真实入口，并核对公开命题的类型；其八个 `#print axioms` 结果均为

\[
\{\texttt{propext},\ \texttt{Classical.choice},\ \texttt{Quot.sound}\}.
\tag{1}
\]

具体目标如下。

| 目标 | 命名空间中的声明 |
|---|---|
| 终端证书 | `OAI.SevenEighths.CenteredMomentEnergyCertifiedExistence.terminal_certificate` |
| 最终 detector 证书 | `OAI.SevenEighths.ProbeFinalAssemblyUnconditional.detector_certified_bands` |
| 内部 Dirichlet 结论 | `OAI.SevenEighths.ProbeFinalAssemblyUnconditional.dirichlet_nonzero` |
| 内部 ζ 结论 | `OAI.SevenEighths.ProbeFinalAssemblyUnconditional.zeta_nonzero` |
| 公开 Dirichlet 结论 | `OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re` |
| 公开 ζ 结论 | `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` |
| Hecke 族结论 | `OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re` |
| Hecke ray 族结论 | `OAI.SevenEighths.HeckeRayFamily.LFunction_ne_zero_of_seven_eighths_lt_re` |

这些实际目标的证明依赖不含 `sorryAx`，也没有额外项目公理。
这次结论来自真实构建及目标级依赖打印，不来自文本词法扫描。

源码中别的声明或导入文件含 `sorry`，不决定一个指定定理是否使用它。
例如外部 `PrimeNumberTheoremAnd.Wiener` 的两个 `prelim_decay` 声明确实
各自依赖 `sorryAx`，但上表真实目标的输出仍是 (1)。验收范围是这些
指定数学目标；没有将它扩展为整个来源仓库的所有声明均已验收。

## 2. 被验收命题的准确数学范围

公开 Dirichlet 命题针对每个非零自然数模数与每个复 Dirichlet 特征，要求

\[
\Re s>7/8,\qquad \neg(\chi=1\ \wedge\ s=1),
\]

并结论于 Mathlib 的 `DirichletCharacter.LFunction χ s ≠ 0`。
附带例子核对了这些条件和这个原函数，没有改换为另一个目标函数。

ζ 命题针对 Mathlib 的 `riemannZeta`。传统解析意义的 \(s=1\) 是极点，
不作为零点；本稿在其非平凡零点上使用该结论。
Hecke 命题覆盖固定来源定义的 Eisenstein 数域 \(\mathbb Q(\sqrt{-3})\)
有限阶 Hecke 族与 ray 族，并排除相应主特征的 \(s=1\) 极点。
它没有声称任意数域上的同一结论。

这是严格半平面的无零定理；没有排除 \(\Re s=7/8\) 边界。
对 ζ，结合标准函数方程反射，非平凡零点仍只能被限制为

\[
1/8\le\Re\rho\le7/8.
\tag{2}
\]

在 \(\Xi(z)=\xi(1/2+iz)\) 的记号下，\(\rho=\beta+i\gamma\) 对应
\(w=\gamma+i(1/2-\beta)\)，所以 (2) 给

\[
|\Im w|\le3/8.
\tag{3}
\]

这就是 [B] 的输入 Q。实际验收没有排除剩余条带内的离轴零点，没有
证明 (R4)、严格增长下降 (T) 或 Mellin 射线目标 \((T_M)\)，故不构成 RH
证明。第五轮谱输入与选择方程的解析论证仍应按各自定义域审查。

## 3. 固定来源与最小验收源

[Q] [固定 paper.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
主定理及非平凡零点反射范围。

[L] [Dirichlet/ζ 公开入口](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean)，
[Hecke 公开入口](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Nonvanishing.lean)，
以及 [无条件最终组装](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Detector/FinalAssemblyUnconditional.lean)。
依赖与兼容补丁均取同一固定项目，不以比较器模板替代入口。

[B] 本仓库固定提交
[`4495df1` 的桥接报告](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/REPORT.md)，
第 1–4 节。本文补充输入 Q 的实际形式化证据；并不改变该稿对未证
排谱及临界相关估计的限制。

`accept_qrh.lean` 应放在上述固定 `openai/math` 项目的 Lean 环境中检查。
它没有重新提供或替换被验收的数学证明，只导入原证明、核对公开命题类型
并打印其实际公理依赖。目录中其他 Python 指数复算不能替代这份验收。
