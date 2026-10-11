## Round 357 — Aksman 稿件的 Eisenstein 散射系数按其自身约定写反

对该稿件第 4 节的公式作独立代数核验。稿件先写出
\[
 E(z,s)=y^s+\Phi(s)y^{1-s}+O(e^{-2\pi y})
\]
并把 \(\Phi(s)\) 定义为这个展开中的 \(y^{1-s}\) 系数。对
\(PSL_2(\mathbb Z)\) 的标准 Eisenstein 级数，该系数由常数 Fourier
项直接为
\[
 \phi(s)=
 \frac{\sqrt\pi\,\Gamma(s-\tfrac12)\,\zeta(2s-1)}
      {\Gamma(s)\,\zeta(2s)}
 =\frac{\Lambda(2s-1)}{\Lambda(2s)},
 \qquad
 \Lambda(w)=\pi^{-w/2}\Gamma(w/2)\zeta(w).
\]
稿件式 (7) 却写成 \(\xi(2s)/\xi(2s-1)\)，即在其展开约定下的倒数
（且其所称 \(\xi\) 实际采用的是未乘 \(s(s-1)/2\) 的 \(\Lambda\)）。
若改用倒数作为 scattering operator 的约定，就必须同时把第 4 节的
Eisenstein 常数项展开改写；稿件没有这样做。

这处公式错误本身已经使“散射极点逐点对应 zeta 零点”的后续叙述不能按
所写公式推出；即便将其手工改正，第 9 节的
Cycle-Cone Closure Theorem 和第 10 节的全 Weil 空间精确配对仍未证明。
因此该稿件仍没有无条件 RH 证明。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
