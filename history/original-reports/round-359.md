## Round 359 — Liflandsky 的 Möbius--Laplace 判据未证明其核心衰减界

核验 Sergey Liflandsky, “Explicit Formula for the Discrete Laplace Transform
of the Möbius Function, Related Special Functions, and a Criterion for the
Riemann Hypothesis”，arXiv:2607.09797v3，37 页，PDF SHA-256 为
3c42a00fb5ee58186e68c5849938e4245a850ca47cfd297440d7563af1841e57。

其 Theorem 1.3(a) 的逻辑是正确的条件性判据：若
\[
 \Phi(e^{-x})=\sum_{n\ge1}\mu(n)e^{-nx}=O(x^{-1/2})
 \quad(x\to0^+),
\]
则 Mellin 变换
\[
 G(s)=\int_0^\infty \Phi(e^{-x})x^{s-1}\,dx
\]
在 \(\operatorname{Re}s>1/2\) 全纯；在 \(\operatorname{Re}s>1\) 有
\(G(s)=\Gamma(s)/\zeta(s)\)，再由恒等定理可排除右半临界带零点，
最后用函数方程排除左侧零点。这个推导本身没有把假设伪装成结论。

但该稿件没有证明上述 \(O(x^{-1/2})\) 衰减。它能从
\(|\mu(n)|\le1\) 得到的直接界只是
\[
 |\Phi(e^{-x})|\le\sum_{n\ge1}e^{-nx}
 =\frac1{e^x-1}=O(x^{-1}),
\]
而将指数级 Möbius 和改善到 \(O(x^{-1/2})\) 正是 RH 强度的消去性
信息。其 Theorem 1.3(b) 反向方向还明确另加 RH、零点简单性和
Hypothesis (H)。因此这篇稿件提供了一个正确的条件性判据和显式公式，
没有提供无条件 RH 证明。
