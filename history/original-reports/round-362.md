## Round 362 — 从 theta 和式定义出发，\(\Xi\) 的核是二阶校正后的核

核验 Pavesi, “A Proof of the Riemann Hypothesis via the Log-Concavity of
the Pólya Kernel”, Zenodo record 20828059, v7；下载 PDF 的 SHA-256 为
39fa06ad29ebe2acf895cd6ac0d57279793f0ead57efb440438a1b625a0ba62b。
记

\[
 B(u):=2e^{u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}}.
\]

Jacobi 模变换给出

\[
 B(-u)-B(u)=e^{u/2}-e^{-u/2}=2\sinh(u/2).
\]

因此 \(B\) 本身不是偶函数，而且在 \(u\to-\infty\) 时含有
\(e^{-u/2}\) 增长项；它不能直接作为双边可积的 \(\Xi\) Fourier 核。
与完成 zeta 函数的因子
\(\frac12s(s-1)=-\frac12(t^2+\frac14)\)，
\(s=\frac12+it\)，相匹配的核由

\[
 \Phi(u):=\frac12\left(\frac{d^2}{du^2}-\frac14\right)B(u)
\]

给出。逐项微分得到完全显式的正向定义：

\[
 \Phi(u)=
 \sum_{n\ge1}
 \left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)
 e^{-\pi n^2e^{2u}} .
\]

由于 \((d^2/du^2-1/4)\sinh(u/2)=0\)，上面的模变换立即推出
\(\Phi(-u)=\Phi(u)\)；同时二阶算子消掉 \(B\) 在负无穷处的两个临界
指数项，使 \(\Phi\) 成为正确的快速衰减双边核。对其 Fourier 变换做
Mellin 代换 \(x=\pi n^2e^{2u}\)，并逐项使用 Gamma 积分，得到标准
\(\Xi\) 表达式（按 Fourier 归一化可能差一个整体常数）。

这一步的定义级结论是：Pavesi 稿件中计算的
\[
G(x)=x(S_4S_0-S_2^2)-S_2S_0
\]
只控制 \(B\) 的对数曲率；它没有自动给出二阶校正核 \(\Phi\) 的对数
曲率。两者之间缺少一个已证明的保持不等式，不能把前者直接代入
\(\Xi\) 的 Pólya 判据。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
