## Round 325 — Zhang Ising candidate: the zeta partition function is assumed

核验 arXiv:2411.16777 v4，Zhidong Zhang，2026-08-16 修订，46 页，
https://arxiv.org/abs/2411.16777。下载 PDF
/tmp/zhang-ising-v4.pdf，SHA-256
3c3f952509ca2acfff73019edb29adf477de03385f6472f408f522aff39d3b1d。
稿件声称用带随机竞争相互作用的二维 Ising 模型证明 RH/GRH。

承重断点在其 Theorem 1 的式 (21)。稿件把每个 replica 的 Ising
partition function 直接写成
\[
\bar Z_\alpha=\sum_{n\ge1}\exp(-E_n/(k_BT))
=\sum_{n\ge1}n^{-s}=\zeta(s),\qquad E_n=\mathcal E\log n.
\]
这不是从式 (18) 的有限二维 Ising Hamiltonian 或其 transfer matrix 推导
出的谱结论，而是预先把能级设为 \(\mathcal E\log n\)。有限 \(m\times n\)
Ising 系统的 Hilbert 空间有有限个自旋构型；稿件没有证明其能级等于
对所有 \(n\ge1\) 的 \(\mathcal E\log n\)，也没有证明式 (34) 得到的
\(\gamma_{2j}\) 与这些能级逐项对应。随机矩阵的普适统计或“随机分布”
不能推出 Dirichlet 系数和逐项谱相等。

此外，式 (21) 的 Dirichlet 级数只在 \(\operatorname{Re}s>1\) 收敛。
稿件没有构造该物理 partition function 在临界带的解析延拓，也没有证明
延拓后仍等于 \(\zeta(s)\)。所以由式 (21) 得出的
\(\bar Z_\alpha=0\Longleftrightarrow\zeta(s)=0\) 不能覆盖非平凡零点。

Theorem 4 也没有补上这个缺口：式 (40) 已经对 disorder 做平均，并把
随机相互作用替换成其均值；引用铁磁/反铁磁 Ising 模型的 Fisher 零点
结论，不能自动证明这个随机竞争模型及其平均模型的全部零点都在同一
单位圆上。即使单位圆结论成立，仍需先证明该 partition function 的零点
与 \(\zeta\) 的零点完全相同。

最后，Theorem 5 的收尾明确先承认临界线的实部仍需确定，再用 Hardy 的
无穷多个临界线零点和有限数值计算来“固定”实部。这不能排除其余无限
多个零点位于临界线外；有限计算不产生全称解析结论。

因此，该稿没有给出从定义到 RH 结论的完整无条件非循环证明，也没有给出
RH 的无条件否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
