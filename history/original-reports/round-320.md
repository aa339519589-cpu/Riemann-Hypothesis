## Round 320 — Yu Pan energy-integral candidate audit

核验对象：Yu Pan, “Energy Integral of Prime Fluctuations, Scaling Rigidity
and an Unconditional Proof of the Riemann Hypothesis”, rxiVerse 2608.0008,
6 页，2026-08-03。来源：https://rxiverse.org/pdf/2608.0008v1.pdf；PDF
SHA-256 为 `d6423db0c0deb78b6603866230d2034358ec67ff65623613667386168d48a148`。

承重断点如下：

1. Definition 3.1 的 \(H_2\) 是交叉项满足严格指数抑制的条件，Theorem 4.1
   直接以“若 \(H_2\) 成立”推出 \(\sigma^*\le1/2\)。因此该部分是
   条件约化，不是对 \(H_2\) 的无条件证明。
2. Theorem 3.3 声称 \(H_2\) 与弱尺度不变性 \(A_w\) 等价，但“若交叉项
   达到主阶则尺度不变性被破坏”没有给出对无限零点和、符号相消及
   \(Y\mapsto\lambda Y\) 的严格估计；文中只有一句量级叙述。
3. 第 6 节用固定 \(\sigma>1/2\) 的 \(\zeta'/\zeta(\sigma+it)=O(\log|t|)\)
   排除零点簇。该表达式在零点附近有极点，不能作为对所有 \(t\) 的全局
   界；即使零点为单零点也存在该奇性，所以不能由此排除所述机制。
4. Theorem 7.2 把 \(H_2\) 与“uniform zero repulsion conjecture”互推，
   但从间距下界到 Weyl 等分布及无限双重和的平方根抵消没有证明，反向
   “间距趋近则相位锁定并达到全阶”也没有证明。它把待证明的零点排斥
   重新命名为等价条件。
5. Lemma 8.1 的“局部奇性平衡”只考察两个零点的局部对数导数，并从
   \(\delta_j\to0\) 推出 \(\delta\asymp\Delta\gamma\)；没有说明其余
   无限零点项如何控制，也没有从 \(\zeta'/\zeta\) 的真实局部展开得到
   所需上界。故该引理不能排除 \(\delta\gg\Delta\gamma\) 的情形。
6. 显式公式中的零点和、\(F(y)\) 以及 \(|F(y)|^2\) 的双重展开需要对称
   截断、分布意义或统一收敛的严格处理；文中没有给出这些条件，却直接
   交换无限求和与积分并断言能量的主阶。这不足以建立全称的 \(H_2\)。

所以该稿没有提供 RH 的完整、无条件、非循环证明，也没有提供 RH 的
无条件否证。其最终 Theorem 10.1 只是建立在未证明的 \(H_2\)、\(A_w\)、
UC 和 Lemma 8.1 上。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
