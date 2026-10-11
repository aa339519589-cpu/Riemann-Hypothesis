## Round 279 — Abe Version 26 still has a direct tangent-intercept algebra error

审计对象：Yukitaka Abe, *A Rigorous Proof of the Riemann Hypothesis*,
Cambridge Open Engage Version 26 (2026-07-17), PDF SHA-256
\`128a8e156b0f47cca587c9ec57c01406979c0e1c2c45b6fe88430645f824ea55\`。

第 15--16 页的 Proposition 1 使用
\[
\ell_2:\quad
Y=\frac{\frac1{2\alpha}-R}{\sqrt{\frac R\alpha-R^2}}(X-R)+I,
\qquad
I^2=\frac R\alpha-R^2.
\]
令 \(Y=0\) 解这条直线，得到的横截距必为
\[
X_B
=R-\frac{I\sqrt{\frac R\alpha-R^2}}{\frac1{2\alpha}-R}
=R-\frac{\frac R\alpha-R^2}{\frac1{2\alpha}-R}.
\]
论文式 (5.5) 却写成
\[
X_B^{\rm paper}
=R-\frac{\sqrt{\frac R\alpha-R^2}}{\frac1{2\alpha}-R},
\]
少了一个因子 \(I=\sqrt{R/\alpha-R^2}\)。因此式 (5.3) 的
\(PA=OB\) 不能按论文写出的式 (5.5) 转换为式 (5.6)。

这是可独立检查的精确数值反例，不涉及任何渐近或数值猜测。取
\(\alpha=1,\ \beta=2,\ P=(R,I)=(\frac15,\frac25)\)。该点确实同时满足论文
式 (5.1)--(5.2) 对应的两圆方程，并且两圆正交。由直线 \(\ell_2\) 正确求得
\[
X_B=-\frac13,
\]
而式 (5.5) 给出
\[
X_B^{\rm paper}=-\frac{17}{15}.
\]
同时由 \(\ell_1\) 得 \(PA=\frac13\)，恰与正确的
\(|OB|=\frac13\) 相等，却不等于论文式 (5.5) 给出的
\(\frac{17}{15}\)。故论文的 Proposition 1 未被证明；依赖它的 Theorem 1
及最后的 \(B=\frac12\) 推理不能作为无条件 RH 证明。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
