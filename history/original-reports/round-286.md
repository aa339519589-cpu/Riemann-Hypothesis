## Round 286 — Aksman v2 leaves the geometric-to-arithmetic scattering step unproved

审计对象：Mikhail I. Aksman, *Fractal Uncertainty in Vorton Manifolds:
The Spectral Resolution of the Riemann Hypothesis via Automorphic Scattering*,
Zenodo Version v2（2026-08-14），该文件是 5 页 presentation，PDF SHA-256
\`0faa02b987f65442a8570b7e78957f5dfdff3e1d92c287f46ba6878ee928b47f\`。

文稿把以下几个非蕴含步骤直接写成结论，却没有给出相应定理的假设和证明：

1. 有限曲率、有限核半径和 filament separation 不会自动推出 trapped set
   \(K\) 的 Ahlfors--David regularity，也不会自动推出高维位置/动量集合的
   FUP。文稿只声称存在严格 plurisubharmonic weight \(\varphi\)，没有构造
   \(\varphi\)、证明其 Levi form 的全局下界，或验证 FUP 所需的尺度和双集合
   条件。
2. 即使给定 FUP 指数 \(\beta>0\)，文稿也没有从传播、逃逸函数、压力条件和
   pseudo-Laplacian 的域得到式 (9)--(10) 的 resolvent 估计；“defect
   measures 只能集中在 \(K\)”本身不是该估计。有限-core vorton 的几何曲线
   也没有被证明就是模曲面的全部 trapped set。
3. 所谓“精确算术映射”写成
   \[
   \det S(s)=\frac{\xi(2s-1)}{\xi(2s)}G(s),
   \]
   但随后直接声称其散射极点与 \(\xi(s)\) 的非平凡零点双条件对应。式中出现
   的零点参数是 \(2s-1\) 或 \(2s\)，不是 \(s\)；必须另外证明变量变换、零点/极点
   方向、Gamma 因子 \(G\) 的零极点以及拟拉普拉斯 resolvent 的散射极点完全
   对齐。文稿没有给出这些证明。

因此，从几何 porosity 到全局 resolvent，再到 \(\zeta\) 零点的承重链仍断开；
这份 presentation 的声称不能构成 RH 的无条件证明。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
