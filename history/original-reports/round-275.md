## Round 275 — Anthropic 2026 zero-proportion result does not close the remaining fraction

审计对象：Claude/Anthropic, *More Than Two Thirds of the Zeros of the
Riemann Zeta Function Are Simple and on the Critical Line*, 2026-08-11，
PDF SHA-256
\`19f827bee5834d61aa6dd756cdaea582492703ddbfd6bdc2058de10b93f7e814\`。
官方说明页同时明确表示该工作没有证明或否证 RH。

稿件的 Theorem A 是一个比例下界：按其声明，分块区间 \((T,2T)\) 中至少
\((2/3-o(1))N(T,2T)\) 个零点（按重数）是临界线上的简单零点；采用
Montgomery--Taylor 窗口时，声明的常数为 \(0.6725\)。这类结果即使全部成立，也只约束一个正比例，不能推出剩余零点全部在临界线上。

其自身第 7.2 节给出了该有限证书的代数上限：只使用矩阵的迹、Hilbert--Schmidt 范数、临界线正半定部分与非临界成对块的惯性信息时，存在达到相同数据的抽象极端配置，其中 \(2/3\) 的量由临界线简单零点承担，其余量由非临界成对块承担。因而该 rank--trace 证书的严格不等式不能从 \(2/3\) 自动提升到 \(1\)；“存在正比例”与“所有零点”之间缺少新的全局输入。

所以这项工作可以是重要的无条件部分比例进展，但它没有提供排除最后非临界零点的定理，也没有改变本任务的全称承重条件。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
