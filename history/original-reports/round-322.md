## Round 322 — Tope operator v7 direct countercheck

核验对象：Tope, “Proof of the Riemann Hypothesis via the Tope Operator”,
Zenodo 20208426，Version 7。来源：https://zenodo.org/records/20208426；
PDF 8 页，SHA-256 为
`89bd9b470074b784c26dade085830477924d6eb4fd843f288543cfcba8704535`。

第一承重引理即有显式反例。文中 Lemma 2 声称对
\(a\in(0,1/2)\)、\(\sigma\in(0,1)\)、\(\delta\in\mathbb R\)（排除一个
特殊点）有
\[
\frac{a-\sigma}{(a-\sigma)^2+\delta^2}+
\frac{a-(1-\sigma)}{(a-(1-\sigma))^2+\delta^2}<0.
\]
取 \(a=1/4\)、\(\sigma=0.1\)、\(\delta=0\)，左边为
\[
\frac{0.15}{0.15^2}+\frac{-0.65}{(-0.65)^2}
=\frac{20}{3}-\frac{20}{13}>0.
\]
等价地，文中自己的分子
\((2a-1)(uv+\delta^2)\) 在该取值下为正；其“所有构型均为负”的
符号判断错误。因此 Lemma 3 的 \(|\xi(a+ib)|\) 横向单调性、Corollary 4
的唯一性以及后续 Tope 计算均没有成立的前提。

此外还有独立缺口：

1. Tope 积分公式需要连续函数恰有一个零点并满足端点方向；稿件没有从
   RH 反设或函数方程证明 \(f_b(0),f_b(1)\) 必有相反符号，不能简单断言
   “\(f\) 或 \(-f\)”总有合适方向。
2. 对 \(g_b=-\operatorname{Im}\zeta(a+ib)\)，稿件没有给出与 \(f_b\)
   相同的唯一零点定理，却直接把 Tope 定理应用到 \(g_b\)。
3. 其 \(G\) 值的有限 Gauss–Legendre 数值接近零，只是有限数值测试，不能
   修复 Lemma 2 的反例或推出对所有零点的结论。

结论：该稿的证明链在 Lemma 2 处已被直接反例击断；没有给出 RH 的完整、
无条件、非循环证明，也没有给出 RH 的无条件否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
