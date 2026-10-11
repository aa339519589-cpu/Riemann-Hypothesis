## Round 285 — Pavesi v7 has a kernel-variable mismatch and does not prove its global interval bound

审计对象：Luca Eliseo Pavesi, *A proof of the Riemann Hypothesis via the
log-concavity of the Pólya kernel*, Zenodo Version v7（2026-06-24），PDF
SHA-256
\`39fa06ad29ebe2acf895cd6ac0d57279793f0ead57efb440438a1b625a0ba62b\`。

论文定义
\[
\Omega(u)=2e^{u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}},\qquad u\in\mathbb R,
\]
但随后对 \(g(v)=\log\Omega(e^v)\) 使用
\[
g(v)=\log2+\frac v2+\log S_0(\pi e^{2v}).
\]
按定义直接代入 \(u=e^v\) 得到的却是
\[
\log\Omega(e^v)=\log2+\frac{e^v}{2}
\;+\log S_0(\pi e^{2e^v}),
\]
所以式 (2.2) 求导的其实是
\(\log(2e^{v/2}S_0(\pi e^{2v}))\)，不是论文所定义的
\(\log\Omega(e^v)\)。此外，对该后者正确求导给出
\[
g''(v)=\frac{4x}{S_0(x)^2}
\bigl[x(S_4S_0-S_2^2)-S_2S_0\bigr],
\qquad x=\pi e^{2v},
\]
而论文式 (2.4) 写成了前因子 \(4x^2/S_0(x)^2\)。

按论文实际定义的 \(\Omega(u)\)，由
\[
S_0(\pi e^{2u})
=\frac{1}{2e^u}-\frac12+O(e^{-\pi e^{-2u}})
\quad(u\to-\infty)
\]
可得
\[
\Omega(u)=e^{-u/2}-e^{u/2}+o(1)\to+\infty
\quad(u\to-\infty),
\]
而 \(\Omega(u)\to0\) 超指数地当 \(u\to+\infty\)。因此它不是偶函数，
不能直接满足论文所引用的“正、偶、且 \(\log\Omega(e^v)\) 凹”的
Pólya 定理假设；论文没有给出另一个核以及两者的等价证明。

即使暂不考虑上述变量问题，Section 3 的 \(O(e^{-\pi^2/x})\) 与
\(O(xe^{-5x})\) 只是渐近记号，不能单独推出在整个 \((0,1]\) 和
\([10,\infty)\) 上的严格符号；Section 4 的网格断言也没有随论文给出可独立
复核的逐格区间证书。故该稿的 log-concavity 主定理未被证明，不能推出 RH。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
