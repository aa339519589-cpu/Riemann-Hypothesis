## Round 334 — Latest PIHR XII still leaves the half-mode inequality open

核验 Borros Arneth 的最新 PIHR XII， “Renormalized Prime-Flow Dynamics,
Periodic Memory Tails, and Square-Root Bellman Descent for the Critical
Half-Mode”，Zenodo record 22130771，https://zenodo.org/records/22130771，
文件 `PIHR-RH-XII.pdf`。文件 MD5 为
722a0e1febaf77dc692dfdd22944afc4，SHA-256 为
28afb24f3fc098edbe732b4677609202089490e98e338fbf67750b522a09676c。
同时核对其前一版 PIHR XI，Zenodo record 22130625，
https://zenodo.org/records/22130625，PDF SHA-256 为
391dcabeb33187e361af504d05f62c7ec00212d6999cf8b04d5037deda8c0912。

PIHR XII 的 exact identities 包括加权面积等价式、有限素数状态的递推、
周期误差的表示，以及未筛基态的 scaling inequality。它们没有闭合目标
\[
W_f(x)\ge \frac{x-1}{\zeta(3/2)}
\qquad(x\ge1),
\quad
f(n)=\prod_{p\mid n}(1-p^{-1/2}).
\]
该不等式在第 28 节被明确列为 “What Has Not Been Proved”。Theorem 10
只证明未筛状态 \(P=\varnothing\) 的
\(W_1(x/p)\le p^{-1}W_1(x)\)；稿件没有证明这个 scaling inequality 在
自然有序的任意有限 Euler 状态中保持。

真正的 Bellman 步骤只以 “Prime-Flow Bellman Principle — Conjectural”
出现：需要构造储备泛函 \(\mathfrak T_p(x)\)，证明其对所有自然有序状态的
不变正性和收缩递推，再令 \(p\to\infty\)。式 (61)--(69) 没有给出该泛函
或所需不等式的证明。第 28 节还指出互补的上半模条件仍未完成；有限区间
数值检查不改变 \(x\ge1\) 的全称命题。

PIHR XI 的正文和 mathematical status statement 已同样明确写出：完整
scaling-surplus theorem、互补 closure 以及统一零自由区估计仍开放。因此
最新 PIHR 版本只增加了辅助恒等式和精确的未决问题表述，没有给出 RH 的
无条件证明或否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
