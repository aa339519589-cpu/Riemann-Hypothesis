## Round 339 — Connes Theorem 4 does not supply Velez’s Gram factorization

逐页对照 Velez 引用的 Connes 原文，arXiv:math/9811068v1，PDF SHA-256 为
dfd4e9924d8980f82e3da11fdea861d318fda8f5c7ba57ee659baf8631975053。Connes
第 VII 节先在
\[
X_S=A_S/\mathcal O_S^\times,
\qquad L^2(X_S)
\]
上定义截断投影 \(P_\Lambda\)、Fourier 截断 \(\widehat P_\Lambda\) 和
\(R_\Lambda=\widehat P_\Lambda P_\Lambda\)，Theorem 4 的结论是
\[
\operatorname{Trace}(R_\Lambda U(h))
=2h(1)\log'\Lambda+
\sum_{v\in S}\operatorname{PV}\int_{k_v^\times}
\frac{h(u^{-1})}{|1-u|}\,d^\times u+o(1).
\]
这是一个截断算子的迹公式，不是对 Velez 所写
\(\Phi_X(F)=U_X(g_F)\eta_X\) 的构造，也不是
\(\langle\Phi_X(F),\Phi_X(G)\rangle=q_X(F,G)\) 的定理。Connes 在证明中
出现的 \(\eta_\chi\) 是特定正特征情形下用于描述截断投影交集的局部向量，
不能直接替代 Velez 未定义的“cutoff-renormalized completed vacuum vector”。

更直接的是，Connes 第 VIII 节把相应的全局公式写成 “natural to expect”，并
明确说对一般紧支撑 \(h\) 无法直接证明；随后 Theorem 5 在正特征情形把该公式
与 RH 等价，而不是无条件证明它。因而该引用没有闭合 Velez Proposition 6.1
所需的空间识别、向量存在、Gram 内积和 cutoff 极限。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
