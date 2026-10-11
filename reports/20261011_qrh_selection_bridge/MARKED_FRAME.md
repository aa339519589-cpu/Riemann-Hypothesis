# 完整 E/F 相位重排与有限窗 Gauss 加权标记行算子界

## 1. 固定来源与记号

使用用户 [准确补偿稿](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/COMPENSATION.md) 和 [标记行界](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/reports/20261011_qrh_selection_bridge/MARKED_ROW_BOUND.md) 的原探针、原零延拓与全部原始素数窗口，原始定义均取 `openai/math` 固定提交 `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` 的 [paper.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)。原文第 1038–1045 行的 Gauss CRT 乘法式、第 934–972 行的固定 ray 相位、第 3349–3400 行的完整 corrected row、第 6835–6917 行的原 slot 几何足够支持下列运算。

令
\[
\beta(c,n;s,m)=\gamma_2(c)\overline{\alpha(cn^3)}\eta(cn^3)
\Xi_*(cn^3)^{-1}\mathcal R(cn^3,s)\chi_{cn^3}(m)\overline{G(cn^3)}.
\]
其中 \(c\) 平方自由，\(n\) 任意好理想，允许 \((c,n)>1\)。所有理想使用原 primary 生成元，\(q_a\) 是范数。标记 \(D\) 由不同原 slot 素数组成，每个素数在固定 ray 群 \(T\) 的单位类内。

## 2. 保留相位的全部 E/F 分解

按用户已有的互斥分解，令 \(D=EF\)，其中 \(E\) 恰为 \(D\) 中整除 \(c\) 的素数积。则
\[
c=Ec_0,\quad n=Fn_0,\quad c_0\text{ 平方自由},\quad(c_0,D)=1,
\]
且 \(n_0\) 没有额外互素限制。记 \(A_0=c_0n_0^3\)。准确的相位恒等式为
\[
\boxed{
\overline{\eta(D)}\beta(Ec_0,Fn_0;s,m)
=\frac{\mu(E)}{\Xi_*(E)\gamma_1(E)}
 \frac{\overline{\alpha(F)}^3\eta(F)^2}{\Xi_*(F)^3}
 \chi_E(mc_0^4)\chi_F(m)^3\beta(c_0,n_0;s,m).}
\tag{2.1}
\]
原零延拓保留在两个字符中，即使乘积相消也不能删掉非单位处的零。

证明：CRT 及 cubic reciprocity 给
\[
\gamma_2(Ec_0)=\gamma_2(E)\gamma_2(c_0)
 \chi_E(c_0)^2\chi_{c_0}(E)^2
=\gamma_2(E)\gamma_2(c_0)\chi_E(c_0)^4.
\]
因为 \(E,F\in1_T\)，其积 \(EF^3\) 仍在单位类，且 \(G\) 及 \(\mathcal R\) 确实按原定义通过 \(T\) 因子化，故
\(G(EF^3A_0)=G(A_0)\)、\(\mathcal R(EF^3A_0,s)=\mathcal R(A_0,s)\)。这里没有假定 \(G\) 本身是乘法字符。再用
\(\gamma_1(E)\gamma_2(E)=\mu(E)\alpha(E)G(E)\)、\(G(E)=1\)，及 \(\alpha,\eta,\Xi_*\) 的乘法性，得到 (2.1)。\(\chi_{EF^3A_0}(m)=\chi_E(m)\chi_F(m)^3\chi_{A_0}(m)\) 是带零延拓的准确恒等式，允许 \(E,F\) 与 \(n_0\) 共享素数。证毕。

相应的范数权及 Gaussian 完全准确地变成
\[
q_E^{-1/2}q_F^{-1}\,q_{c_0}^{-1/2}q_{n_0}^{-1},\qquad
W_{\rm G}\!\left(\frac{q_{c_0}q_{n_0}^3q_F^2}{Z}\right).
\tag{2.2}
\]
特别地，主支 \(F=1\) 的 Gaussian 与 \(D=E\) 无关；其标记字符部分为
\[
\frac{\mu(D)}{\sqrt{q_D}\,\Xi_*(D)\gamma_1(D)}\chi_D(mc_0^4).
\tag{2.3}
\]

对完整补偿项，设 \(r=p_J\)、\(D=p_{J^c}=EF\)、\(P=rEF\)，总 slot 数为 \(K\)。把 (2.1) 代入用户的准确公共变量重排，\(s_0=s/r\)、\(m_0=m/r^2\) 仍须先检查整除。原 \((-1)^{|J|}\) 乘上 \(\mu(E)\) 变为
\[
(-1)^{|J|}\mu(E)=(-1)^K\mu(F),
\tag{2.4}
\]
而外部系数准确化为
\[
\frac{(-1)^K\mu(F)q_r\,\overline{\alpha(F)}^3\eta(F)^2}
 {\Xi_*(P)\Xi_*(F)^2\gamma_1(E)\sqrt{q_E}\,q_F}.
\tag{2.5}
\]
它还乘原 \(g_{\chi_{s_0}}(s_0,-m_0)\)、(2.2) 的残余和及
\(\chi_E(m_0c_0^4)\chi_F(m_0)^3\)。原 slot 权重全部保留。
因此主支 \(F=1\) 的显式子集符号全为同一 \((-1)^K\)；其真正振荡保留在 inverse Gauss 因子、字符及原 additive Gauss 和中。本恒等式不将这些复相位改为正数。

## 3. 一个真实的有限窗 Gauss 加权 Bessel 界

以下引理只用原 sextic 字符，未以 cubic 字符替代它。

**引理。** 设 \(s\) 是任意好 primary 理想，\(\mathcal D\) 是不同好平方自由理想组成的有限集，且 \(q_D\le P\)，\(P\ge1\)。定义
\[
G_s(m)=q_s^{-1/2}g_{\chi_s}(s,-m).
\]
存在只依固定格子归一的 \(C,c>0\)，使 \(N/(q_sP^2)\ge1\) 时，对任意复系数 \(a_D\)，有
\[
\boxed{
\sum_{m\in\mathcal O}e^{-q_m/N}|G_s(m)|^2
 \left|\sum_{D\in\mathcal D}a_D\chi_D(m)\right|^2
\le CN\left(1+P e^{-cN/(q_sP^2)}\right)
 \sum_{D\in\mathcal D}|a_D|^2.}
\tag{3.1}
\]
固定有界环带上的指示函数或固定光滑权可由该 Gaussian 乘一个固定常数控制。没有假设 \((D,s)=1\)、不同 \(D\) 互素、\(s\) 平方自由或零延拓可忽略。

证明。对 \(D,D'\)，函数
\[
B_{D,D'}(m)=|G_s(m)|^2\chi_D(m)\overline{\chi_{D'}(m)}
\]
的一个周期理想是 \(\mathfrak l=\operatorname{lcm}(s,D,D')\)，且
\(q_{\mathfrak l}\le q_sP^2\)。首先，\(|G_s(m)|^2\) 在每个素数处只依赖 \(v_p(m)\)：这由原 Gauss 和的 CRT 及素幂公式直接得到。非主字符的局部和在允许赋值处有常模；主字符按原零延拓产生 Ramanujan 和，也只依赖赋值。

若 \(D\ne D'\)，选 \(p\mid D\triangle D'\)。该处字符在单位群上的指数是 \(+1\) 或 \(-1\pmod6\)，为非主字符；其余局部幅度只依赖赋值，且该字符在非单位处为零。因此该局部平均为零，CRT 给
\[
\frac1{q_{\mathfrak l}}\sum_{m\bmod\mathfrak l}B_{D,D'}(m)=0.
\tag{3.2}
\]
对于 \(D=D'\)，该平均非负且不超过 1。事实上有限 Parseval 给
\[
\frac1{q_s}\sum_{m\bmod s}|G_s(m)|^2
=\frac{\varphi(s)}{q_s}\le1,
\tag{3.3}
\]
而对角额外零掩码只减小平均。对于任意 \(D,D'\)，每个规范化有限 Fourier 系数的绝对值也不超过 1，因为其绝对值受 \(|G_s|^2\) 的平均支配。

在固定 Eisenstein 格子上对 Gaussian 作 Poisson，零频项为固定正常数乘 \(N\) 及上述周期均值；非零频项的总绝对值不超过
\[
CN\sum_{0\ne k\in\mathcal O}
 \exp\left(-c\frac{Nq_k}{q_{\mathfrak l}}\right)
\le C'N\exp\left(-c'\frac{N}{q_{\mathfrak l}}\right),
\tag{3.4}
\]
最后一步用 \(N/q_{\mathfrak l}\ge1\) 与固定二维格点计数。故对角 Gram 项至多 \(CN\)，非对角项至多 \(CN e^{-cN/(q_sP^2)}\)。理想计数给 \(\#\mathcal D\le CP\)，用
\((\sum|a_D|)^2\le\#\mathcal D\sum|a_D|^2\) 即得 (3.1)。证毕。

## 4. 原窗口内的固定残余列主支

固定 \(J\)、重缩放素数组 \(r\)、公共 \(s\)，并设 \(s_0=s/r\)。记
\[
d=\sum_{i\in J}\ell_i,\quad
N\asymp Z^{5/6-2d},\quad q_{s_0}\asymp Z^{23/48-d},\quad
P\asymp Z^{1/6-d}.
\]
于是
\[
\boxed{\frac{N}{q_{s_0}P^2}\gg Z^{1/48+d}.}
\tag{4.1}
\]
固定一个残余对 \((c_0,n_0)\)，主支的公共 \(m_0\) 字符为 \(\chi_{A_0}(m_0)\)，其中 \(A_0=c_0n_0^3\)。所有其余不依 \(m_0\) 的相位、原 slot 权、\(\chi_D(c_0)^4\)、\(1_{(D,c_0)=1}\) 和系数 \((\sqrt{q_D}\Xi_*(D)\gamma_1(D))^{-1}\)，均可收入 \(a_D\)。原 \(m_0\) 环带与 Gaussian (2.2) 对该固定残余列是共同的。

此固定残余列的正平方和含共同掩码
\(|\chi_{A_0}(m_0)|^2=1_{(m_0,A_0)=1}\)。先在完整正平方和内删除该掩码，得到 Loewner 上界，然后应用 (3.1) 与 (4.1)，可得
\[
\boxed{
\sum_{q_{m_0}\asymp N}|G_{s_0}(m_0)|^2
 |\chi_{A_0}(m_0)|^2
 \left|\sum_Da_D\chi_D(m_0)\right|^2
\ll N\sum_D|a_D|^2.}
\tag{4.2}
\]
常数对 \(Z,J,r,s_0,c_0,n_0\) 一致（依固定 slot 与 annular 常数）。空 marked-slot 情形只有 \(D=1\)，也包括在内。

这里不能先对每个交叉项删除 \(1_{(m_0,A_0)=1}\) 然后声称其周期不含 \(\operatorname{rad}A_0\)；删除只发生于整个非负平方和的上界中。这一点允许 (4.2) 保持原零延拓而避免人为增大周期。

## 5. 全部 E/F 分支的标记行算子界

**定理。** 对所有 \(Z>0\)、\(N>0\)、\(P\ge1\)，保留 §2 的原 slot 标记与相位，令 \(\mathcal D\) 为其中任意有限集合，\(q_D\le P\)。在 \(N/(q_sP^2)\ge1\) 时，对任意复权 \(w_D\)，有
\[
\boxed{
\sum_{0\ne m\in\mathcal O}e^{-q_m/N}|G_s(m)|^2
\left|\sum_{D\in\mathcal D}w_D\overline{\eta(D)}
 \mathcal B_D(Zq_D;m,s)\right|^2
\le CNZ\left(1+Pe^{-cN/(q_sP^2)}\right)
 \sum_{D\in\mathcal D}\frac{|w_D|^2}{q_D}.}
\tag{5.1}
\]
常数依固定原始算术数据与 Gaussian，不依 \(Z,N,P,s\)、标记的素因子数或系数。对原窗口，指数括号一致有界；固定 annular 频率支撑由 Gaussian 上界覆盖。

证明。按 (2.1)–(2.2) 将完整行写成全部互斥 \(D=EF\) 分支。固定 \(F,c_0,n_0\) 时，共同的 \(m\) 因子为
\(\chi_F(m)^3\chi_{c_0n_0^3}(m)\)。其绝对值平方为单位掩码，先在完整的 \(E\)-和正平方中删除；所有其余不依 \(m\) 的相位和互素筛均收入 \(E\)-系数。该系数的绝对值不超过
\(|w_{EF}|/\sqrt{q_E}\)。用 (3.1)，再对 \(c_0,n_0\) 使用 Hilbert 空间 Minkowski，得固定 \(F\) 部分的范数至多
\[
C\sqrt{N\mathcal E}\,q_F^{-1}
\left(\sum_E\frac{|w_{EF}|^2}{q_E}\right)^{1/2}
\sum_{c_0\ {\rm sf},n_0}q_{c_0}^{-1/2}q_{n_0}^{-1}
W_{\rm G}\!\left(\frac{q_{c_0}q_{n_0}^3}{Z/q_F^2}\right),
\quad \mathcal E=1+Pe^{-cN/(q_sP^2)}.
\tag{5.2}
\]
用户已证的全正尺度正项引理 \(S(V)\ll\sqrt V\) 在 \(V=Z/q_F^2\) 上适用，包括任意小的 \(V\)。故 (5.2) 至多
\[
C\sqrt{NZ\mathcal E}\,q_F^{-2}\sqrt{b_F},\qquad
b_F=\sum_E\frac{|w_{EF}|^2}{q_E},
\tag{5.3}
\]
其中只有 \(EF\in\mathcal D\) 且 \((E,F)=1\) 的项参与。

对 \(F\) 再用 Minkowski 及加权 Cauchy，
\[
\begin{aligned}
\left(\sum_Fq_F^{-2}\sqrt{b_F}\right)^2
&\le\left(\sum_Fq_F^{-3/2}\right)
       \left(\sum_Fq_F^{-5/2}b_F\right)\\
&\le\zeta_{\mathbb Q(\sqrt{-3})}(3/2)
  \sum_{D\in\mathcal D}\frac{|w_D|^2}{q_D}
                    \sum_{F\mid D}q_F^{-3/2}\\
&\le\zeta_{\mathbb Q(\sqrt{-3})}(3/2)^2
 \sum_{D\in\mathcal D}\frac{|w_D|^2}{q_D}.
\end{aligned}
\tag{5.4}
\]
这使用绝对收敛的理想和，不产生 \(2^{\omega(D)}\) 损失。合并即证 (5.1)。所有原始行在 Gaussian 下绝对收敛，上述非负正项控制也直接保证所用 Minkowski 极限合法。证毕。

## 6. 与既有均方界的准确比较及剩余承重

(4.2) 是固定残余列的原有限窗口标记平方和控制；(5.1) 将所有 \(E/F\) 分支合法拼合，去掉对任意标记数组先取绝对值再平方所产生的标签计数损失。其 Gauss 加权和任意 \(w_D\) 量词不同于用户已有的固定结构化 \(B^J\) 均方。

对原标记窗口 \(q_D\asymp P\) 的有界原 slot 权，理想计数给 \(\sum_D|w_D|^2/q_D\ll1\)，因此 (5.1) 仅给 Gauss 加权 \(O(NZ)\)。用户原报告 (R2) 对其结构化、已求和的 \(B^J\) 有无 Gauss 权的更强界 \(O(NZ^\epsilon)\)。本稿未改善那个指数，也不能通过改变权的对象把 (5.1) 宣称为新的临界幂次节省。

不同残余列 \((c_0,n_0)\)、\((c'_0,n'_0)\) 的交叉相关被 §5 的 Minkowski 消耗成 \(Z\) 损失；其中
\(\chi_{c_0n_0^3}(m)\overline{\chi_{c'_0n_0'^3}(m)}\) 不能作为共同单位掩码删除。它的实际残余导子也不再由 \(q_sP^2\) 控制。

所以尚未得到用户 `GRAM_INTERFACE.md` 的完整能量 \(\|\mathcal F_Z\|_2^2\ll Z^{7/12+o(1)}\)，亦没有解决高端延拓余量。下一项真正承重是对这些不同残余列的原短窗交叉相关建立可求和的整体上界，保持 (2.1) 的全部 Gauss、sextic 字符及原零掩码。

进一步应区分“不同拆分”与“不同总 sextic 核”：写原始 \(n=vk^2\)、\(v\) 平方自由后，完全共振由同一对 \((c,v)\) 标记。不同 \((E,F,c_0,n_0)\) 可落入同一个总核，不能一概归为非共振。核路的 LCM covariance–Schur 引理已控制完整零 Poisson 模式，包括所有这种不同拆分；当前剩余的实质困难在真实短窗的非零双频项，尤其不同总 sextic 核的残余相位，而不是未计入的完全共振计数。

本稿的全部相位恒等式与第5节完整算子界均有 [独立数学核验](REFEREE_MARKED_FRAME.md)。用户原点态定理及其全正尺度引理是继承输入，不重新列为本稿成果；本稿不依赖 QRH 的7/8无零区域。
