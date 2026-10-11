## Round 294 — Han's latest Riesz criterion is an implication, with its converse explicitly conditional on RH

审计对象：Songlin Han, *On variants of Pólya’s conjecture*, arXiv:2608.27130v1，
日期 2026-08-28，PDF SHA-256
``ea51312d9e5770f45e350e647be4287062fcc2de829610e2625ef586bb8f9418``。

该稿的 Theorem 1.1 形式是：如果存在 (x_0) 使
\[
f(x)=-\sum_{n\le x}\frac{\lambda(n)\log n}{\sqrt n}\log\frac{x}{n}
\ge0\qquad(x\ge x_0),
\]
则 RH 成立。正文通过 Mellin 变换把这一假设转成
\(F'(s)/(s-\tfrac12)^2\) 的解析性，再排除
\(F(s)=\zeta(2s)/\zeta(s)\) 在右半平面的极点；这是一个“正性若成立则
推出 RH”的判据，不是对该正性本身的证明。

其 Theorem 1.2 反向分析明确以 H1（RH）、H2（所有非平凡零点简单）和 H3
\[
\sum_{\gamma>0}
\frac{|\zeta(1+2i\gamma)|}
{\gamma^2|\zeta'(\tfrac12+i\gamma)|}<\infty
\]
为前提。因而随后得到 (f(x)\sim(\log x)^3/(12|\zeta(\tfrac12)|))
和 eventually positive 不能用于证明 RH：它已经把 RH 和额外的简单零点/
收敛条件放进假设。最新 arXiv 摘要也只声称这两种条件下的 converse，
没有给出无条件的 (f(x)\ge0) 全尾证明。

所以这篇最新判据没有关闭最后的全称正性命题；它没有提供无条件 RH 证明或
否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
