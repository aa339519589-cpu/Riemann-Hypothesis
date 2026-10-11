## Round 273 — Aksman unified architecture: the operator-limit bridge is stated as a conjecture

审计对象：Mikhail I. Aksman, *DSM-861 and the Riemann Hypothesis: The
Complete Unified Proof Architecture From Geometric Necessity to the
\(\Gamma\)-Convergence of Strong Resolvent Limits*, Zenodo record
20634354，PDF SHA-256
\`77e752fbc910f254db1547331960de7676fc4dbbd7df359b8264b398467e1c35\`。

稿件的承重目标是构造自伴算子 \(H_\zeta\)，使其特征值给出所有零点的虚部，并满足
\[
\det(E-H_\zeta)\propto \xi\!\left(\frac12+iE\right).
\]
但在第 II.2 节，这一存在性、收敛性和行列式识别被明确写成
“DSM Hilbert--Pólya Conjecture”；在第 VII.2 节，稿件又把
\[
(\Delta_{Y(N)}-zI)^{-1}\longrightarrow(H_\zeta-zI)^{-1}
\]
列为必须证明的 Task 3，而不是已经证明的定理。

第 VIII--IX 节的 \(\Gamma\)-收敛部分不能填补该缺口。文中没有定义随 \(N\) 变化的精确 Hilbert 空间嵌入、离散 pseudo-Laplacian 的共同形式域、边界条件、离散能量与连续能量的严格对应，也没有证明所写 \(J_N\) 的 lim-inf/lim-sup 估计适用于该算子序列。二维共形映射保持连续 Dirichlet 能量，并不推出 Chebyshev--Gauss--Lobatto 离散化的谱收敛，更不推出强预解收敛或正则化行列式收敛。

此外，稿件把散射扇区中的共振信息与 \(L^2\) 离散本征值混同。即使截断后的算子自伴且具有离散谱，也还必须证明：每个 zeta 零点对应一个稳定的 \(L^2\) 本征值、极限中没有谱污染，并且该谱的正则化行列式确实等于 \(\xi\)。这些识别均未给出。所谓 \(O(1/Y)\) 修正与一个有限数值比值的接近，只是渐近/数值观察，不能代替这些无限维定理。

所以从几何叙述到“所有零点由自伴算子谱给出”的关键桥梁仍是未证明命题；由此不能推出 RH。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
