## Round 290 — Independent algebra check confirms the newest Aksman gap is not a closed RH implication

对 Round 289 所审计的 Aksman 最新稿再作一次只依赖正文公式的独立核验。正文的
Lemma 2.2 把 \(δ<3\) 代入三维占比 \(r^{δ-3}\)，并称其在
\(r\to0\) 时趋于零；取例如 \(δ=1\)、\(r=10^{-6}\)，该表达式为
\(10^{12}\)，一般地 \(δ-3<0\) 时极限是 (+\infty)。这不是一个尚待
估计常数的细节，而是该段推出“存在固定比例空球”的方向错误。即使把
Patterson--Sullivan 测度替换为适当的邻域体积，也仍须另行证明邻域体积的
全尺度上界；正文没有给出。

对正文 Proposition 3.1 和 Theorem 3.2 的参数作精确量词转换：若已知的无共振区
只有
\[
\Re(s)>\frac12-ε,
\]
并且散射极点对应 \(ρ=2s\)，则直接得到的零点排除区为
\[
\Re(ρ)>1-2ε.
\]
要排除 RH 所需的全部右半临界带 \(\Re(ρ)>\tfrac12\)，必须有
\(1-2ε\le\tfrac12\)，即 \(ε\ge\tfrac14\)。稿件只从
\(β>0\) 声称存在某个 \(ε(β)>0\)，没有证明这个数值下界，也没有给出
从所定义的 FUP 算子到该 resolvent 的完整定理。因此“正的 FUP 指数”不能被
改写成“\(\Re(s)>\tfrac14\) 无共振”。

这些是正文内部公式之间的直接反推，不依赖有限数值实验，也不把作者的结论
当作前提。最新记录仍只是一个声称完整架构的 poster/proof program；它没有
提供可独立检查的 uniform porosity、定量 \(\varepsilon\ge\tfrac14\)、或
几何散射到 zeta 零点的完整闭合定理。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
