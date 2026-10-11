## Round 332 — Chua’s Nicolas-criterion descent does not prove its two lemmas

核验 Cheong Siong Chua 的 “Nicolas Criterion and Riemann Hypothesis”，
Zenodo record 20069911，https://zenodo.org/records/20069911。文件
`NICOLAS_CRITERION_AND_RIEMANN_HYPOTHESIS_7_MAY.pdf` 的 MD5 为
9cd8fe3431a212969f4bcc5d1c06d672，SHA-256 为
c4276c63f94ef78ae9df3226c99544b6830fc337163de9c0e72c356f1fafcdb8。

稿件把 Nicolas 判据的等价性作为起点，试图证明：若某个大于 \(10^6\) 的
\(k\) 违反不等式，就可反复推出 \(\lfloor k/2\rfloor\) 也违反，最终与
低于 \(10^6\) 的有限检查矛盾。这个下降步骤不是“数学归纳”本身；它完全
依赖 Lemma 1 和 Lemma 2 的严格、全范围证明。

Lemma 1 只给出
\[
\sum_{i=\lfloor k/2\rfloor+1}^{k}\frac1{P_i}
=\frac{\log2}{\log k}+\frac{(\log2)^2}{2(\log k)^2}
 +O\!\left((\log k)^{-3}\right)
\]
这样的渐近表达式，然后直接推出带有具体系数、对所有 \(k>10^6\) 有效的
严格乘积不等式。稿件没有给出 \(O\)-项的显式常数、符号或阈值，因此该
具体全称不等式没有从所写计算推出。

Lemma 2 的证明同样以带省略号的展开式直接写出
\(\log\log N_k/\log\log N_{\lfloor k/2\rfloor}<1+\log2/\log k\)，没有给出
余项控制或对所有整数 \(k>10^6\) 的严格验证。更直接地，Nicolas 判据的
否定首先只保证存在某个 \(k\) 使不等式不成立，即允许等号；稿件未经证明
就把它写成严格的 “\(<\)”，因此连下降步骤的起点也未覆盖全部否定情形。

有限范围的数值检查不能补上这两个无限范围的解析引理。故该稿没有给出
Nicolas 不等式的无条件全称证明，也没有给出 RH 的无条件证明或否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
