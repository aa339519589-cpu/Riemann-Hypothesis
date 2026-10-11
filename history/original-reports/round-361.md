## Round 361 — 有限谱自伴性只给出平移后的正性，不给出 Weil 形式正性

对照 Consani--Connes--Moscovici, arXiv:2511.22755v1 第 5.2--5.6
节的定义，设 \(T=Q_{\lambda,N}^{W}\) 是有限维截断矩阵，
\(\varepsilon_N=\lambda_{\min}(T)\)，且最小特征值简单、偶特征向量为
\(\xi\)。文中 Lemma 5.4 的实际输入不是 \(T\ge0\)，而是

\[
 T_0:=T-\varepsilon_N I\ge0,
 \qquad \ker T_0=\mathbb C\xi .
\]

在 \(\langle\eta,\xi\rangle=1\) 的归一化下，矩阵恒等式

\[
 [D,T_0]=|\beta\rangle\langle\eta|
             -|\eta\rangle\langle\beta|,
 \qquad T_0D\xi=-\beta
\]

推出 \(D'=D-|D\xi\rangle\langle\eta|\) 湮灭 \(\xi\)，并在商空间
\(E_N/\mathbb C\xi\) 的 \(T_0\)-内积上自伴。因而该有限维定理确实给出
实谱；但它给出的正性是 \(T_0\ge0\)，不是 \(T\ge0\)。恒等关系是

\[
 T\ge0 \quad\Longleftrightarrow\quad \varepsilon_N\ge0.
\]

这是一个纯代数区别。例如一维矩阵 \(T=[-1]\) 的最小特征值为
\(-1\)，而 \(T-\varepsilon_NI=[0]\) 半正定；平移后的商空间谱结论不改变
\(T\) 的负号。故“最小特征值减去自身，所以原截断 Weil 形式半正定”
不是有效推导。

进一步，原文第 3.4 节只证明截断空间的最小特征值随 \(N\) 给出
\(Q^W_\lambda\) 的下界极限；要得到 \(Q^W_\lambda\ge0\)，仍须独立证明
该下界极限非负。对所有 \(\lambda\) 取得这个结论正是需要闭合的 Weil
正性命题，不能由有限谱的实性替代。

这一步得到并核实了有限维的正确自伴性定理，同时精确保留了其未闭合的
正性前提：

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
