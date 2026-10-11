## Round 352 — Fixed-window positivity cannot be extrapolated by support decomposition

为检验 Chuk 结果能否仅凭“局部窗口正性”推出全局正性，考虑解析反模型
\[
\mathcal Q_a(f)=\|f\|_2^2-a\left|\int_{\mathbb R}f(u)\,du\right|^2,
\qquad a>0.
\]
若 \(\operatorname{supp}f\subset[-L,L]\)，Cauchy--Schwarz 给出
\[
\left|\int f\right|^2\le 2L\|f\|_2^2,
\]
所以取 \(a<1/(2L)\) 时，\(\mathcal Q_a\) 在整个固定窗口上严格正。可是
取一列在长度为 \(M\) 的区间内近似常数、边界平滑的测试函数，则
\(\|f_M\|_2^2\sim M\)、\(|\int f_M|^2\sim M^2\)，当 \(M>1/a\) 时
\(\mathcal Q_a(f_M)<0\)。

这说明“所有固定小支持窗口均正”在逻辑上不推出“所有紧支撑测试函数均正”；
还必须有一个覆盖尺度、控制跨窗口交叉项的独立全局定理。Chuk 的 Theorem 1
只给出一个固定窗口，论文没有提供该全局延拓定理。因此有限窗口证书不能
完成 Weil criterion。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
