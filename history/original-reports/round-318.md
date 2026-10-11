## Round 318 — Aksman Heegner spectral compactification audit

核验对象：Aksman, “The Heegner Spectral Compactification Program: The
Confining CM Potential, the Analytical Bessel Resolution, and the Exact
Determinant Falsification Test”, Zenodo 21359411，PDF 10 页。来源：
https://zenodo.org/records/21359411；PDF SHA-256 为
`8ab7d6f2983aa136fd8e9edc11cfede1507284806fd4de9d3b41d3d2fda58c02`。

逐页核对得到：

1. Proposition 4.1 只证明一个条件等价：若预先有
   \(\det(H_\alpha-\mu(1-\mu)I)=C\,\xi(\mu)L(\mu,\chi_{-163})\)，则自伴性
   会把相应零点限制到临界线；它没有证明这个行列式恒等式。全文没有给出
   该恒等式的解析推导。
2. Theorem 3.1 仅由尖点处的渐近正增长声称紧预解式。定义的
   \(V_\alpha(z)=\alpha\log|j(z)-j(\tau_{163})|^2\) 在 Heegner 点有
   对数负奇性；文中没有给出带奇性势的自伴算子定义域、下有界性、或
   投影后算子 \(P_EH_\alpha P_E\) 的严格构造。且乘法势一般不与
   Eisenstein/cuspidal 正交投影交换，不能仅凭 \(P_E=I-P_{cusp}\) 就把
   扰动算子限制到 Eisenstein 子空间。
3. Theorem 5.1 的 Macdonald 函数只解高尖点区的零 Fourier 模方程，且
   使用渐近线性势；这不是完整商空间上的二维算子谱，也没有由此得到
   其正则化谱行列式的零点集合。
4. 第 6 节把“与前三个已知 ordinates 的匹配”定义为一维参数 \(\alpha\)
   的数值成本函数 \(J(\alpha)\)。即使有限精度下三个点匹配，也不能推出
   全部零点的行列式恒等式或 RH；论文自己把它称为 falsification test，
   而不是已完成的全局解析匹配。附录 B 的“confirmed”分支也只是预设
   扫描结果的二分判据，不是无条件定理。
5. 文中对 \(j(\tau_{163})\) 的书写同时出现“\(-6403203\)”和
   “\(-262537412640768000\)”两个不同数值（后者是前者的立方），反映出
   具体势的定义还需要先统一。无论修正哪一个，仍不能补足第 1–4 项的
   谱匹配缺口。

结论：该稿没有从定义建立 RH 的无条件证明，也没有给出 RH 的无条件否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
