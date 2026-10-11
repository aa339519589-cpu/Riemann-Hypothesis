## Round 360 — 高频 resolvent 衰减本身不能排除有限位置的极点

把 Round 358 中的逻辑缺口写成一个精确反例。任取
\(s_0\) 满足 \(\operatorname{Re}s_0>1/4\)，令
\[
 R(s)=\frac1{s-s_0}.
\]
这是一个在 \(s_0\) 有极点的亚纯函数；但当
\(|\operatorname{Im}s|\ge 2(1+|\operatorname{Im}s_0|)\) 时，
\[
 |R(s)|\le \frac{2}{|\operatorname{Im}s|}
 \le 2|\operatorname{Im}s|^{-1+\beta}
 \qquad(\beta>0).
\]
所以任何只对高频区域给出的
\(O(|\operatorname{Im}s|^{-1+\beta})\) 型估计，都可以与半平面内的
有限位置极点同时成立。要推出无共振，必须另行证明估计在包含每个候选
极点的开区域上一致、解析延拓没有极点，并处理有限频率的紧集；FUP 的
抽象范数式和一个高频幂界并不包含这些结论。

该反例直接否定了 Aksman 第 5 节从式 (3) 跳到
\(\operatorname{Re}s>1/4\) 共振空集的推理。因此该候选仍未产生
无条件 RH 证明。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
