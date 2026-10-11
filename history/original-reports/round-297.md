## Round 297 — Chen v3's own $K$-derivation admits that the unconditional constant is not proved

核验 Chen 概念记录的真正最新版本：Zenodo record 22143035，2026-08-28，
版本 v3；正文 PDF SHA-256 为
``5a6feb94ae15bbd532a02b62a9011ed479f2d650bbeb84cd2617ecb55b397196``。
该版本修正了旧版 Hadamard 核的符号，但其随附的
``grh_K_derivation.md``（SHA-256
``9dd0cccc39da4f39cdfcfea69d61a8652d37c683441a4f73b21e92e0b98c5685``）
对决定性常数作出了相反于“已闭合”的明确说明。

该附录在离线零点部分写出：当 \(|r-γ|<1\) 时，每个离线零点的负贡献最多为
\(-1/\delta^2\)，而普通 Ingham 型零密度估计在
\(σ\to\tfrac12^+\) 时不能把局部零点数压到 (O(\log(qr)))；要得到所需
的 \(O(\log(qr))\) 负项控制，还需要额外的近临界线估计或计算验证。附录
随后明确写出
\[
K_{Λ,\mathrm{offline}}\ “\text{无法被严格控制为小常数}”,
\]
并把 (0.1\sim0.3) 称为依赖“显式量化”的极度保守估计。

更直接地，附录的合成部分给出
\[
K=K_{ζ,\mathrm{main}}+K_{Λ,\mathrm{main}}
 +K_{Λ,\mathrm{offline}},
\]
并说明无计算验证时取 (K=1.0) 只是“safe choice”，但“需要将零密度估计的
显式常数完全量化才能严格成立”。然而 v3 正文却把同一个 (K=1.0) 当作
\(r>3\times10^{12}\) 的无条件下界，并据此声称 \(g_K'(r)>0\)。这是一条
稿件自身明确承认尚未完成的承重推理，不能由其数值表格或有限区间网格代替。

因此，Chen v3 虽已消除旧版的符号矛盾，仍没有证明全尺度角单调性，更没有
提供无条件 RH/GRH 证明。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
