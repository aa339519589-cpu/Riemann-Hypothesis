## Round 327 — Alarcón correlation claim does not exclude a sparse off-line set

核验 David Alarcón 的 “Berry-Keating convergence of Riemann zero spectral
statistics implies the Riemann Hypothesis”，Zenodo record 19268989，
https://zenodo.org/records/19268989，以及其所依赖的原始
Rudnick–Sarnak 材料：https://www.math.tau.ac.il/~rudnick/papers/RudnickSarnakCRAS1994.pdf。
Zenodo 摘要把“若该收敛模式精确成立则 RH 成立”与一个声称使用
Rudnick–Sarnak 和线性规划的 companion paper 并列；这两者不能合并成
无条件证明。

直接核对 Rudnick–Sarnak 原始陈述可见：其对临界零点的 n-level GUE
结论在放宽测试函数条件时明确写成 “If we assume RH”；无 RH 假设时，
结论带有受限 Fourier support 等条件。任何把该结果用于 RH 的证明都必须
说明 off-line zeros 如何被纳入计数，并证明线性规划误差对它们给出逐点
排除；摘要没有提供这一承重推导。

更基本的逻辑反检验是：归一化的 pair/n-level 相关极限只控制相对密度。
在任意具有给定 GUE 极限的序列中加入 \(o(N(T))\) 个离线点，归一化
相关统计的主极限可以保持不变，但“所有点均在临界线”已经失败。因此，
即使统计收敛被无条件证明，也不能单凭该收敛排除一个零密度的离线零点
集合；还需要一个未给出的、把每个可能离线零点转化为不可忽略统计量的
严格定理。有限高度数据和有限网格上的线性规划误差更不能承担这个
全称结论。

故该候选最多给出统计量的条件性约化/数值研究，未给出从 zeta 的解析
延拓和零点集合到“无离线零点”的完整无条件证明，也没有给出 RH 的
无条件否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
