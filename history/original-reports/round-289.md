## Round 289 — The newest Aksman vorton/FUP submission still fails at porosity and at the required gap size

审计对象：Mikhail I. Aksman, *The Riemann Hypothesis: Automorphic Scattering,
Fractal Uncertainty, and Coercive Vorton Geometry*, Zenodo record
``10.5281/zenodo.22063440``，2026-08-23。公开记录把资源类型标为
``Poster``；正文 PDF（``RH_Vorton_FUP_Proof.pdf``）SHA-256 为
``29d69b28f45ac43c3c0c0df9edd8a336a8f09d016421cea00ccab2fed560633a``。

正文声称链条

\[
K_a\Longrightarrow \text{uniform porosity}\Longrightarrow \text{FUP}
\Longrightarrow \text{resonance gap}\Longrightarrow \Re(\rho)=\tfrac12,
\]

但关键中间命题在正文中不能成立或没有被推出。

首先，文稿把 (K_a) 定义为由严格正的有限半径径向 mollifier 形成的
“regularized vorton neighborhood”，同时又对所有 (x\in K_a) 和所有趋于零的
尺度 (r) 声称存在固定比例的空球。若 (K_a) 按该定义包含有限半径管状核心，
其内部点在足够小的 (r) 下有 (B(x,r)\subset K_a)，因而不可能存在
\(B(y,\nu r)\subset B(x,r)\setminus K_a\)。若 (K_a) 不包含这个管状核心，
则文稿没有给出“vorton neighborhood”的另一个精确定义，也没有证明它与
零厚度 trapped set 之间的 FUP 常数关系。因此 Lemma 2.2 的全尺度、与 (a)
无关的结论没有建立。

其次，Lemma 2.2 的数值尺度推理本身方向相反。文稿由
\(μ(B(x,r))\asymp r^\delta\)、\(δ<3\) 得出占三维球的体积分数为
\(r^{\delta-3}\)，并声称该量在 (r\to0) 时趋于零；但
\(δ-3<0)，所以 \(r^{\delta-3}\) 趋于无穷而不是零。并且
Patterson--Sullivan 测度的标度关系本身不是三维 Lebesgue 体积占比，不能在
没有额外绝对连续性/管邻域估计的情况下推出空球。正文没有补上这些估计。

再次，即使暂时把 Theorem 2.3 的 FUP 假设当作已知，Proposition 3.1 只写出
\[
\|R_a(s)\|\le C\log|\Im s|\quad
\text{for }\Re(s)>\tfrac12-\varepsilon(\beta),
\]
其中仅声称 \(\varepsilon(\beta)>0\)。Theorem 3.2 却把无共振区直接改成
\(\Re(s)>\tfrac14\)。这需要额外证明
\(\varepsilon(\beta)\ge\tfrac14\)（以及该估计确实适用于所定义的
pseudo-Laplacian 与散射矩阵）；“β>0”并不推出这个定量下界。若
\(0<\varepsilon(\beta)<\tfrac14\)，只能排除
\(\Re(\rho)>1-2\varepsilon(\beta)\)，仍不能排除
\(\tfrac12<\Re(\rho)\le1-2\varepsilon(\beta)\) 的零点。

因此，最新正文仍未证明统一几何正则性、FUP 所需的全尺度孔隙性、从 FUP 到
特定 resolvent 的定量共振隙，或该隙与全部非平凡零点的一一对应。其公开记录
的“proof program”描述不能替代这些定理。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
