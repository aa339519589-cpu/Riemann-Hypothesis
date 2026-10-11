# 完整补偿 Gram 的 Gauss 重缩放正交与有限窗双线性界

## 结论与范围

本稿沿用用户提交 `e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8` 的真实标记行界，和
`4d93d36e5a18d6d9e0ae6c7b346c9fdb496e3bc6` 的有限域 Gram 对象；没有更换字符、零延拓、Gauss 和或窗口。

证明三项新的准确事实：

1. 两个不同重缩放乘子 \(r,r'\) 的点态交叉，只能发生在其对称差素数均以正的六倍赋值同时整除 \(s,m\) 的位置。故在六次幂自由 \(s\) 上，不同 \(r\) 的所有完整标签块精确正交，无须来自同一素数组。
2. 对每一对真实物理行指标 \(A,A'\)，只要 \(r\ne r'\)，包含外部 Gauss 和的完整周期交叉均值精确为零。真实非单位零掩码保证其局部非主字符不能被行字符抵消。
3. 外部 Gauss 部分的绝对交叉平均有明确 Euler 乘积；在用户的实际有限 \(m\) 窗口上可直接使用，所需长度只是 \(X\gg q_{\operatorname{lcm}(r,r')}\)，原尺度以 \(Z^{1/48}\) 的幂余量满足。

第 3 项不保留行字符振荡，只给完整标签交叉的一个有限上界。第 2 项的零主项不代表短窗口交叉为零。同 \(r\) 内不同标记的短窗口 Gram 仍未控制；因此没有证明用户的 \(Z^{7/12+\epsilon}\) 总能量目标、低端封闭或 RH。

## 1. 准确对象

令 \(\mathcal O=\mathbb Z[\omega]\)，\(q_a=N(a)\)，全部理想用原 primary 生成元表示，避开固定坏素数集 \(S\)。\(\chi_p\) 是原六次剩余字符，阶恰为六；所有字符在非单位处延拓为零。定义
\[
g_\psi(t,k)=\sum_{d\bmod t}\psi(d)e(kd/t).
\]
对好平方自由 \(r\mid s\)，令
\[
F_{s,r}(m)=1_{r^2\mid m}\,q_r\,
 g_{\chi_{s/r}}(s/r,-m/r^2).
\tag{1}
\]
不满足整除时先取零，不计算商。模 \(1\) 的 Gauss 和按 \(1\) 取值。

用户的原标签 \(\lambda=(J,\mathbf p)\) 有 \(r=p_J,D=p_{J^c}\)，且
\[
U_\lambda(s,m)=1_{r\mid s}\,
 \frac{\overline{\eta(D)}}{\Xi_*(r)}F_{s,r}(m)
 \mathcal B_D(Zq_D;m/r^2,s/r).
\tag{2}
\]
固定字符前因子的模长为一。标记行准确物理展开为
\[
\mathcal B_D(U;v,t)=\sum_{\substack{c\ \mathrm{sf},\ n\\D\mid cn^3}}
 b(c,n;t)\chi_{cn^3}(v)q_c^{-1/2}q_n^{-1}
 W_G(q_cq_n^3/U),\quad |b|\le1,
\tag{3}
\]
其中 \(b\) 保留原 \(\gamma_2,\overline\alpha,\eta,\Xi_*^{-1},\mathcal R,\overline G\)。
对固定 \(U\)，(3) 对所有 \(v,t\) 由一个可和正项一致支配。已有用户定理给
\[
|\mathcal B_D(U;v,t)|\le C\sqrt U/q_D.
\tag{4}
\]

## 2. 素数幂 Gauss 的精确非零条件

设 \(P=q_p\)、\(a\ge1\)、\(b=v_p(k)\)。在原字符约定下，\(\chi_{p^a}\) 由 \(\chi_p^a\) 诱导，但仍在 \(p\mid d\) 时取零。
对 \(d\bmod p^a\) 先按模 \(p\) 分类，对所有高位求和，得到：
\[
g_{\chi_{p^a}}(p^a,k)=0\quad(b<a-1).
\]
若 \(k=p^{a-1}u\)，则
\[
g_{\chi_{p^a}}(p^a,k)
=P^{a-1}\sum_{x\bmod p}\chi_p(x)^a e(ux/p).
\tag{5}
\]
故
\[
\begin{array}{c|c|c}
 &\text{非零条件}&\text{模长}\\ \hline
6\nmid a&b=a-1&P^{a-1}\sqrt P\\
6\mid a&b=a-1&P^{a-1}\\
6\mid a&b\ge a&P^{a-1}(P-1).
\end{array}
\tag{6}
\]
第二、三行是有限域主字符的 Ramanujan 和，不得把其零延拓删去。
CRT 引入的单位扭曲不影响这些非零条件或模长。\(a=0\) 的模 \(1\) 情形另行处理，没有限制。

在 (1) 的 \(p\) 分量，记 \(a=v_p(s),b=v_p(m)\)。若 \(p\nmid r\)，直接用 (6) 于 \((a,b)\)。若 \(p\mid r\)，首先需要 \(a\ge1,b\ge2\)，再用 (6) 于 \((a-1,b-2)\)。两个状态的交集恰为
\[
\boxed{a=b\in6\mathbb N_{>0}.}
\tag{7}
\]
证明只需分 \(a=1\)、\(a\equiv0,1\pmod6\)、其余余类；\(a=1\) 时未选态要求 \(b=0\)，与选态 \(b\ge2\) 矛盾。若 \(6\mid a\)，选态要求 \(b=a\)，未选态允许此值。其余情况的两个等式或不等式不相交。

## 3. 全标签的点态正交和改善后的共同支撑

令
\[
g=(r,r'),\qquad h=\frac r g\frac{r'}g,
\qquad L=\operatorname{lcm}(r,r')=gh.
\]
\(g,h\) 平方自由且互素。由 (7)，
\[
F_{s,r}(m)\overline{F_{s,r'}(m)}\ne0
\ \Longrightarrow\ 
\begin{cases}
gh^6\mid s,\\
g^2h^6\mid m,\\
v_p(s)=v_p(m)\in6\mathbb N_{>0}&(p\mid h).
\end{cases}
\tag{8}
\]
所有外部固定字符与完整行只可能进一步清零，因此 (8) 适用于真实 \(U_\lambda\overline U_{\lambda'}\)。

令 \(\mathcal H_r(s,m)\) 是所有具有同一重缩放乘子 \(r\) 的真实带符号标签和（完整 \(D\)、窗口和行均保留）。若 \(s\) 六次幂自由，则逐点有
\[
\left|\sum_r\mathcal H_r(s,m)\right|^2
=\sum_r|\mathcal H_r(s,m)|^2.
\tag{9}
\]
更一般，跨 \(r\) 的全部误差只能支撑于 (8)。它强于只检查同 slot 同 prime 的相反状态。

在用户共同环带 \(q_s\asymp Y,q_m\asymp XY\)，共同允许支撑的数目至多
\[
C\left(1+\frac{Y}{q_gq_h^6}\right)
 \left(1+\frac{XY}{q_g^2q_h^6}\right).
\tag{10}
\]
在两个比值均大于常数的部分，(10) 为
\[
\ll \frac{XY^2}{q_g^3q_h^{12}},
\tag{11}
\]
相较旧并集 \(L=gh\) 的 \(XY^2/q_L^3\) 上界增加 \(q_h^{-9}\)。不可在比值小的部分删去 (10) 的 \(1\)。
并且任何非零交叉都必须满足 \(q_gq_h^6\ll Y\)，特别地
\(q_h\ll Y^{1/6}=Z^{23/288}\)。

## 4. 真实物理行的完整周期交叉均值消去

固定 \(s,r,r',A,A'\)，其中 \(r,r'\mid s\)，\(r,r'\) 平方自由，\(A,A'\) 为 (3) 的真实完成指标。考虑
\[
\mathcal K(m)=F_{s,r}(m)\overline{F_{s,r'}(m)}
 \chi_A(m/r^2)\overline{\chi_{A'}(m/r'^2)},
\tag{12}
\]
仍先以 (1) 的整除条件决定为零。它是模理想
\[
\mathfrak M=\operatorname{lcm}\big(sr,sr',r^2\operatorname{rad}(A),
 r'^2\operatorname{rad}(A')\big)
\tag{13}
\]
的周期函数。

**定理 1。** 若 \(r\ne r'\)，则
\[
\boxed{\frac1{q_{\mathfrak M}}\sum_{m\bmod\mathfrak M}\mathcal K(m)=0.}
\tag{14}
\]

**证明。** 取 \(p\mid h\)。若 (7) 不成立，(12) 恒零。否则 \(a=v_p(s)\in6\mathbb N_{>0}\)，并只需考察 \(v_p(m)=a\)。这时两个行商 \(m/r^2,m/r'^2\) 在 \(p\) 处的赋值分别为 \(a-2\) 与 \(a\)，都为正。
故若 \(p\mid A A'\)，真实行的零延拓使 (12) 恒零。

若 \(p\nmid A A'\)，则 \(v_p(\mathfrak M)=a+1\)。在模 \(p^{a+1}\) 的局部分量写 \(m=p^au\)，\(u\in(\mathcal O/p)^\times\)。未选态 Gauss 和为主字符的常数 \(P^{a-1}(P-1)\)。选态的最后一层是 \(\chi_p^{a-1}=\chi_p^{-1}\)，故由 (5) 和有限域 Gauss 换元，其 \(u\) 依赖为常数乘 \(\chi_p(u)\)；若选态在共轭一侧则为 \(\overline{\chi_p(u)}\)。其他 CRT 分量固定时，两个行字符在 \(p\) 局部分量没有依赖，因为 \(p\nmid AA'\)。于是该局部和含
\(\sum_{u\in(\mathcal O/p)^\times}\chi_p(u)^{\pm1}=0\)。CRT 完成证明。

在固定 \(s,Z\) 和有限标签集上，将真实 (3) 代入，以其一致绝对收敛作有限截断再取极限，(14) 也给完整不同 \(r\) 标签块的扩大圆盘均值为零。这里只是均值主项结论，未将有限环带替换成无限圆盘。

## 5. 外部 Gauss 的准确绝对交叉平均

(1) 是模 \(sr\) 的周期函数。令 \(M_0=sL\)。定义
\[
\mathfrak A_s(r,r')=
\frac1{q_{M_0}}\sum_{m\bmod M_0}
 |F_{s,r}(m)F_{s,r'}(m)|.
\tag{15}
\]
Euler \(\varphi\) 指理想上的单位剩余类数，\(\varphi(1)=1\)。

**定理 2。** 若某个 \(p\mid h\) 的 \(v_p(s)\) 不是正的六倍数，则 \(\mathfrak A_s(r,r')=0\)。其余情形准确有
\[
\boxed{
\mathfrak A_s(r,r')=
\sqrt{\varphi(s/r)\varphi(s/r')}
\prod_{p\mid h}(1-q_p^{-1}).}
\tag{16}
\]
特别地，\(r=r'\) 时它等于 \(\varphi(s/r)\)。

**证明。** 在两个状态相同的素数处，有限加法 Parseval 给局部平均 \(\varphi(p^{a-e})\)，其中 \(e=1_{p\mid r}=1_{p\mid r'}\)；选择态的 \(q_p^2\) 振幅平方恰与 \(p^2\mid m\) 的密度抵消。\(a-e=0\) 时仍成立。

在不同状态处，(7) 要求 \(a\in6\mathbb N_{>0}\)。模 \(p^{a+1}\) 有 \(P-1\) 个允许剩余类，均为 \(m=p^au\)。计入选态的外部 \(P\) 后，两个模长分别是
\[
P^{a-1}(P-1),\qquad P^{a-1/2}.
\]
故局部平均为
\[
\frac{P-1}{P^{a+1}}P^{a-1}(P-1)P^{a-1/2}
=P^{a-5/2}(P-1)^2
=\sqrt{\varphi(p^a)\varphi(p^{a-1})}(1-P^{-1}).
\]
CRT 的单位扭曲不影响绝对值，逐素数相乘得到 (16)。

**有限窗推论。** 对任意复平面圆盘或固定厚度环带 \(\Omega_Q\)（范数尺度 \(Q\)），每个模 \(M_0\) 的剩余类在其中有
\[
O(1+Q/q_{M_0})
\]
个 Eisenstein 格点。因此
\[
\sum_{m\in\Omega_Q}|F_{s,r}(m)F_{s,r'}(m)|
\ll (Q+q_s q_L)\,\mathfrak A_s(r,r').
\tag{17}
\]
常数只依赖固定环带形状。不需把实际窗口延长到行字符的完整模数。
用户原窗口 \(Q\asymp q_bq_sX\)，而 \(q_L\ll Z^{1/3}\) 与 \(X=Z^{17/48}\)，故
\[
\frac{Q}{q_s q_L}\gg Z^{1/48}.
\tag{18}
\]
于是实际窗口上 (17) 的右边可取 \(C Q\mathfrak A_s(r,r')\)。

## 6. 保留真实标记行后的一个有限双线性上界

令 \(\lambda,\lambda'\) 的标记为 \(D,D'\)，重缩放为 \(r,r'\)，并写 \(P=rD,P'=r'D'\)。
由用户已经证明的 (4)、(16)–(18)，对固定 \(s\asymp Y\)，
\[
\sum_{q_m\asymp q_bq_sX}|U_\lambda(s,m)U_{\lambda'}(s,m)|
\ll \frac{Zq_sX}{\sqrt{q_Dq_{D'}}}\,
\mathfrak A_s(r,r')
\le \frac{ZXq_s^2}{\sqrt{q_Pq_{P'}}}
 1_{gh^6\mid s}.
\tag{19}
\]
这里仍需 \(r,r'\mid s\)，且 \(s\) 在 \(h\) 处的赋值为六的倍数；最后一步只放宽限制并使用 \(\varphi(t)\le q_t\)。
因此，对用户有限共同域，
\[
\boxed{
\sum_{(s,m)\in D_Z}|U_\lambda(s,m)U_{\lambda'}(s,m)|
\ll\frac{ZXY^2}{\sqrt{q_Pq_{P'}}}
\left(1+\frac{Y}{q_gq_h^6}\right)
1_{q_gq_h^6\ll Y}.}
\tag{20}
\]
在 \(Y/(q_gq_h^6)\gg1\) 时，这为
\[
\ll\frac{ZXY^3}{\sqrt{q_Pq_{P'}}q_gq_h^6}.
\tag{21}
\]
窗口权重 \(W_i\) 可按原标签逐一相乘保留；本式不预先求和并不声称这些标签数无损。

(20) 是所有实际参数都在用户短窗口内的双线性估计，六次幂对称差节省来自真实外部 Gauss 结构，而不是扩大行平均。它仍相当粗，尤其不能独立控制 \(h=1\) 的同 \(r\) 标记相关。不得用 (21) 或大圆盘主项替代待证总能量目标。

## 7. 下一项明确的承重

将全部标签先按 \(r\) 聚合；跨 \(r\) 项只能来自 (8)，有 (14) 的完整周期零主项和 (20) 的有限绝对上界。剩余主要难点是固定 \(r\) 的
\[
\sum_{s,m}\left|
\sum_{\mathbf p:\,p_J=r}
 (\text{原权重和单位因子})
 F_{s,r}(m)\mathcal B_D(Zq_D;m/r^2,s/r)
\right|^2.
\tag{22}
\]
当 \(s/r\) 平方自由时，\(|g_{\chi_{s/r}}(s/r,-v)|^2=q_{s/r}1_{(v,s/r)=1}\)。因此此主层的外部 Gauss 相位在平方中已经消失，只添加真实单位掩码；没有自动消去标记行的 active conductor。要达到用户的目标仍需在 (22) 中证明真实不同 \(D\) 的短窗口相关节省，或另走保留线性探针振荡的路线。

## 固定来源

- 用户的 [准确补偿恒等式](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/COMPENSATION.md)，式 (4)–(10)。
- 用户的 [标记行界](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/reports/20261011_qrh_selection_bridge/MARKED_ROW_BOUND.md)，定理 (4)。
- 用户的 [有限 Gram 接口](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4d93d36e5a18d6d9e0ae6c7b346c9fdb496e3bc6/reports/20261011_qrh_selection_bridge/GRAM_INTERFACE.md)。
- [原论文固定版本](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，原字符与 Gauss 定义、`eq:general-probe`、`eq:compensated-probe-definition`。

上述结论只用这些原对象、有限域 Gauss 正交、CRT 和二维格点计数；不依赖用户后来提供的 QRH 零点区域输入。

独立数学核验见 [REFEREE_GAUSS_RESCALING.md](REFEREE_GAUSS_RESCALING.md)。
