## Round 280 — Abe Version 26 miscounts the poles in the final contradiction

继续审计同一篇 Version 26（PDF SHA-256
\`128a8e156b0f47cca587c9ec57c01406979c0e1c2c45b6fe88430645f824ea55\`）。
第 21--23 页把
\[
F(z)=\frac1{\zeta(z)g(z)},\qquad
g(z)=\prod_j(z-\rho_j)(z-\overline{\rho_j})
\]
用于围绕 \(\sigma=B\) 的矩形移位。若 \(\rho\) 是 \(\zeta\) 的零点，重数为
\(m\ge1\)，而 \(g\) 在 \(\rho\) 有一个简单零点，则局部展开为
\[
\zeta(z)=(z-\rho)^m a(z),\qquad
g(z)=(z-\rho)b(z),\qquad a(\rho)b(\rho)\ne0,
\]
从而
\[
F(z)=\frac{1}{a(\rho)b(\rho)}(z-\rho)^{-(m+1)}
\;+\;\cdots .
\]
特别地，即使 \(\zeta\) 在 \(\rho\) 只是简单零点，
\(1/(\zeta g)\) 也是二阶极点。

论文定义 \(Q(s)\) 时只写入
\[
a_j\frac{x^{\rho_j-s}}{\rho_j-s}
\]
并把 \(a_j\) 称为 \(1/(\zeta g)\) 的“留数”，随后声称 \(Q\) 在
\(Z_B\) 的极点全为简单极点。这遗漏了二阶及更高阶主部。对简单零点情形，
令
\[
F(s+w)=\frac{A}{(w-(\rho-s))^2}
\;+\frac{B}{w-(\rho-s)}+\cdots,\qquad
h(w)=\frac{x^w}{w}.
\]
则 \(w=\rho-s\) 处的留数是
\[
A\,h'(\rho-s)+B\,h(\rho-s),
\]
而不是只有 \(B\,h(\rho-s)\)。其中
\[
h'(\rho-s)
=x^{\rho-s}\left(
\frac{\log x}{\rho-s}-\frac1{(\rho-s)^2}\right)
\]
含有 \((s-\rho)^{-2}\) 项。故正确的 \(Q(s)\) 具有二阶主部（重数
\(m\) 时具有相应的更高阶主部）。

在式 (8.2) 中，\(w=0\) 的留数本身是 \(F(s)=1/(\zeta(s)g(s))\)，也含
\((s-\rho)^{-(m+1)}\)；正确的邻近极点贡献 \(Q(s)\) 的主部可以与它相消，
这是留数定理所要求的局部抵消。论文把 \(Q\) 错写成只有简单极点后，才制造出
式 (8.4) 的“简单极点与二阶极点矛盾”。因此 Proposition 2 的最终矛盾没有
成立，不能推出 \(B=\frac12\)。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
