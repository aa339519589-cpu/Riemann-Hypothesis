# 原低端的真实非主 dual 核估计

本稿保持用户原 R4 的真实线性 s–m 配对及全部物理 n。最终结论分别覆盖原 completed-index 标记、新 core 标记，以及两种标记各自的第一层 Möbius 去卷积。

- 不使用 Q 的完整非主 quadratic 核：原尺度线性和为 O(Z^(37/96−d/2+ε))，补偿后为 O(Z^(−1/32+ε))。此基础结果独立保留，证明见 Part V。
- 以用户固定输入 Q 为条件的同一完整 quadratic 核：原尺度线性和为 O(Z^(521/2304−d/2+ε))，补偿后为 O(Z^(−439/2304+ε))，比该型所需的 −3/16 低 7/2304。证明见 Parts X–XI。覆盖全部物理 n、原/core 标记及各自第一 Möbius-flat；这里只闭合这一非主 quadratic 类型。
- 完整非主 cubic good-core：包括 H=εw²a⁶、w 非单位 cube-free 的全部混合指数与全部物理 n；线性和为 O(Z^(25/48−d/2+ε))，补偿后为 O(Z^(5/48+ε))，仍高于目标 7/24。不使用 Q 的基础证明见 Part VI。以 Q 为条件，Part XII 的 O(Z^(2/45+ε)) 均值基础保留；Parts XV–XVI 结合真实槽矩、双向光滑矩与完整小指标计数，将同一完整 cubic 类型改善为 O(Z^(−11/2304+ε))，仍高于目标 421/2304。
- 完整 pure fifth-power 型：H=εv⁵a⁶，v 非单位平方自由，涵盖全部物理 n；线性和为 O(Z^(133/480−d/2+ε))，补偿后为 O(Z^(−67/480+ε))，距目标尚差 23/480。不使用 Q 的基础证明见 Part IX。Part XIV 在用户 Q 输入下将同一完整 pure fifth 类型强化为 O(Z^(−63/320+ε))，比该型目标低 3/320；全部物理 n、两标记和各自第一 flat 均保留。
- 完整 mixed 3/5 型：H=εv³w⁵a⁶，v,w 互素、非单位、平方自由，涵盖全部物理 n、两标记及两种 first-flat；不使用 Q，补偿后为 O(Z^(−1/32+ε))，基础证明见 Part XIII。Part XVII 在 Q 条件下将同一完整 mixed(3,5) 类型改善为 O(Z^(−5/32+ε))，仍高于目标 1/32。

上述结果均未覆盖 principal/unit 核及其余混合 sextic good-core，也未证明整个符号配对的目标界或 RH。

Parts I–III 保留 n=1、完整平方层及尺度一致性的已证算术接口；Part IV 给出独立解析双列引理；Parts V–VI 完整证明真实公共系数还原、尾估计及精确去卷积传递。Part VII 给出依赖用户固定输入 Q 的真实 Möbius 列均值；Part VIII 给出真实 selected Euler 乘子矩。这些解析引理本身不直接给完整物理指数；Parts X–XI 将它们与真实双向高矩、全部物理除数和补偿结合，证明上述 Q 条件的 quadratic 强化。各 Part 的公式编号独立。首个 Poisson、Gauss 局部身份与原探针归用户报告及固定源稿；外部解析大筛来源分别在相关 Part 中注明。

# Part I. Rough residual columns

## 原线性补偿探针的粗糙残余列：非主二次核 dual 的双 Poisson 消去

### 状态和范围

数学状态：下面限定范围内的结论已通过独立逐式审核。

本文保留用户原 R4 的线性 \(s\)-\(m\) 配对、所有 Gauss 相位、固定坏素数字符 \(\xi(m)\)、标记和零延拓。不将线性配对换成全正 Gram。

证明目标是一个明确的非零 dual 子分支消去：在原物理行的 \(n=1\)、\(c=Dc_0\) 主支中，如果 \(c_0\) 没有范数不超过 \(C Y'\) 的素因子，则第一次 \(m\)-Poisson 后，全部
\[
H=\varepsilon v^3 a^6,\qquad v\ne1\text{ 平方自由},\quad a\text{ 任意好理想},
\tag{0.1}
\]
的贡献，比任意负幂都小。\(\varepsilon\) 是任一单位；允许 \((v,a)>1\)。这是非主二次 sextic-core 层，非 \(H=0\)，也非 \(H=\varepsilon a^6\) 主层。

该结论不覆盖一般 cubic/sextic core、含较小残余素因子的 \(c_0\)、或 \(n>1\) 的其余物理行。它尚未给 R4 所需的总节省。

### 1. 原尺度与线性对象

固定原重缩放子集 \(J\)，令
\[
d=\sum_{i\in J}\ell_i\in[0,1/6],\quad
X'\asymp Z^{17/48-d},\quad Y'\asymp Z^{23/48-d},
\quad q_D\asymp Z^{1/6-d},\quad Q=q_bX'Y'.
\tag{1.1}
\]
这里 \(b=b_*\)，\(q_b\) 固定。\(D\) 仍按原剩余 slot 素数组求和，原权重记为 \(w_D\)；这些权重有界、有限、与物理 \(m,s\) 无关。

固定 \(\sigma\in T\) 和实 Mellin 参数 \(\nu\)。R4 的频率权写为
\[
\Omega_\nu(z)=\Omega(|z|^2)|z|^{-2i\nu},
\quad \Omega\in C_c^\infty(0,\infty),
\]
故每个固定阶 Schwartz 半范数至多是 \((1+|\nu|)\) 的固定幂。外部 \(s\) 权为
\[
W_1(q_s/Y')(q_s/Y')^{-1/2+i\nu}/Y'.
\]

在原 \(B^J\) 物理展开中只保留 \(n=1\)、\(c=Dc_0\)、\((D,c_0)=1\)，并且
\[
p\mid c_0\Longrightarrow q_p>C Y',
\tag{1.2}
\]
其中 \(C\) 大于 \(W_1\) 支撑的上端常数。\(c_0=1\) 可按空条件包括。原系数保持
\[
\gamma_2(c)\overline{\alpha(c)}\eta(c)\Xi_*(c)^{-1}
\mathcal R(c,s)\overline{G(c)}q_c^{-1/2}
W_G(q_c/(Zq_D)).
\tag{1.3}
\]
标记前因子 \(\overline{\eta(D)}\) 和 \(w_D\) 也保持。

对这一个实际子级数在 \(m\) 上作 Poisson，定义 \(\mathfrak S_{J,\sigma,\nu}^{\mathrm{rough,quad}}\) 为其中满足 (0.1) 的全部 Fourier 项。下面的定理针对这个准确子级数，不声称其正交投影范数控制整个探针。

### 2. 第一次 Poisson：原相位的简明核验

使用原自对偶约定
\[
e(z)=\exp(4\pi i\operatorname{Im}z/\sqrt3),\quad
 d\mu(z)=\frac2{\sqrt3}d\Re z\,d\Im z,\quad
 \widehat W(y)=\int_{\mathbb C}W(z)e(-zy)d\mu(z).
\]
对好平方自由 \(c\)、任意好 \(s\)，定义含全部固定校正的线性被积系数
\[
\begin{split}
f_{s,c}(m)={}&\frac{\chi_s(b)}{\tau\xi(s)}q_s^{-1/2}
 g_{\chi_s}(s,-m)\xi(m)\\
&\cdot\gamma_2(c)\overline{\alpha(c)}\eta(c)\Xi_*(c)^{-1}
\mathcal R(c,s)\overline{G(c)}q_c^{-1/2}\chi_c(m).
\end{split}
\tag{2.1}
\]
令 \(g=(c,s)\)。若 \((c,s/g)\ne1\)，则 (2.1) 恒零：在相应素数处 \(p^2\mid s\)、\(p\mid c\)，Gauss 支撑强制 \(p\mid m\)，而 \(\chi_c(m)=0\)。

其余情形写 \(s=gs_1,c=gc_1\)，三个因子 \(g,s_1,c_1\) 两两互素。令
\[
\mathfrak c_g(k)=\sum_{x\bmod g,(x,g)=1}e(kx/g)
\tag{2.2}
\]
为原零延拓对应的 Ramanujan 和。对任意 Schwartz \(W\)，准确有
\[
\boxed{
\sum_mW(m/\sqrt Q)f_{s,c}(m)
=\frac{Q\mu(c)\eta(c)}{\sqrt{q_b}\sqrt{q_s}q_c}
\sum_{k\in\mathcal O}\mathfrak c_g(k)
 \chi_{s_1}(gk)\overline{\chi_{c_1}(gk)}\overline{\xi(gk)}
 \widehat W\!\left(\frac{\sqrt Q k}{bgs_1c_1}\right).}
\tag{2.3}
\]

这是原论文完整 \(m\)-Poisson/local-scalar 表在 \(n=1\) 层的简式，不作为新的第一 Poisson 定理。
其直接核验为：最小充分周期是 \(bgs_1c_1\)；互素的 \(s_1,c_1,b\) 部分分别给有限 Fourier 正交、\(\gamma_1(c_1)\)、\(\tau\)，共同 \(g\) 部分给 (2.2)。原 reciprocity 校正和 \(\Xi_*\) 消除 CRT 的交叉单位因子；
\(\gamma_1(c)\gamma_2(c)=\mu(c)\alpha(c)G(c)\) 消除其余 Gauss 相位。共享 \(g\) 留下的单位因子为
\(\chi_{s_1}(g)\overline{\chi_{c_1}(g)}\overline{\xi(g)}\)，已收入 \(gk\)。

写 \(H=gk\) 后，Fourier 参数统一为 \(\sqrt Q H/(bsc)\)。特别地 \(\overline{\xi(H)}\) 排除 \(H=0\) 及所有遇到 \(S\) 的 \(H\)；没有用一个不含 \(\xi\) 的裸均值代替实际 R4。

对于固定 \(c,H\)，非零项强制
\[
g=(c,\operatorname{rad}H),\qquad s=gt,\qquad(t,c)=1.
\tag{2.4}
\]
其余 \(t\)-依赖的字符准确为 \(\chi_t(H)\)。外面的
\(\mathfrak c_g(H/g)\overline{\chi_{c/g}(H)}\overline{\xi(H)}\)
保持不变。

### 3. 两个统一尾截断

任取足够小的固定 \(0<\delta<1/64\)。由于 \(W_G\) 对 \(\log\) 变量为 Gaussian，可仅为估计将
\[
q_c>Z^{1+\ell'+\delta},\qquad\ell'=1/6-d,
\tag{3.1}
\]
的整个尾控制为 \(O_A((1+|\nu|)^{C_A}Z^{-A})\)，任意 \(A>0\)。原理是 Gaussian 尾超过任意固定幂，其他原权、格点和标记计数至多有固定多项式增长。并未硬截断后声称等式不变。

在剩余 \(c\) 范围，\(q_s\asymp Y'\)，(2.3) 的 Fourier 参数平方与
\[
\frac{X' q_H}{q_c}
\]
双向可比。因此 \(\widehat\Omega_\nu\) 的任意阶 Schwartz 衰减将
\[
q_H>Z^{13/16+2\delta}
\tag{3.2}
\]
的整个尾也控制为同样的任意负幂；其半范数仅增加 \((1+|\nu|)\) 的固定幂。
这里精确用到
\((1+\ell')-(17/48-d)=13/16\)。

这些尾估计也可先对 \(c,H\) 作有限截断，再由可和正项取极限。Ramanujan 因子的粗界 \(|\mathfrak c_g(k)|\le q_g\le q_c\) 已足够，不需要其相消。

### 4. 二次核分支的所有掩码

令 \(H=\varepsilon v^3a^6\) 满足 (0.1) 和 (3.2)。则
\[
q_vq_a^2=q_H^{1/3}\le Z^{13/48+2\delta/3}.
\tag{4.1}
\]
由 \(d\le1/6\) 有 \(Y'\gg Z^{5/16}\)。因此 \(q_v,q_a<C Y'\)（\(Z\) 足够大），粗糙条件 (1.2) 推出
\[
(c_0,va)=1,\qquad g=(c,\operatorname{rad}H)\mid D.
\tag{4.2}
\]

在 (2.4) 中，\((t,c_0)=1\) 自动成立，因为 \(q_t\ll Y'/q_g\le CY'\)，但 \(c_0\) 的每个素因子更大。\(\chi_t(H)\) 本身已排除 \((t,g)>1\)。因此剩余 \((t,c)=1\) 只需保留 \((t,D/g)=1\)。精确展开
\[
1_{(t,D/g)=1}=\sum_{e\mid D/g,\ e\mid t}\mu(e).
\tag{4.3}
\]
这里 \((e,H)=1\)，因为 \(g\) 已取 \(D\) 与 \(\operatorname{rad}H\) 的全部公因子。

另有准确字符分解
\[
\chi_t(H)=\chi_t(\varepsilon v^3)1_{(t,a)=1}.
\tag{4.4}
\]
在设 \(t=e t_1\) 后，对 (4.4) 的剩余 mask 再用
\[
1_{(t_1,a)=1}=\sum_{f\mid\operatorname{rad}a,\ f\mid t_1}\mu(f).
\tag{4.5}
\]
若 \((f,v)>1\)，相应系数 \(\chi_f(\varepsilon v^3)\) 为零；不能将其改为一。

写 \(t=efz\)。所有仍存的字符 \(z\)-依赖是
\(\chi_z(\varepsilon v^3)\)，其在好素数上的部分为原 primitive quadratic 字符 \(\chi_v(z)^3\)。原 primary 条件、ray class \(gefz\in\sigma\)、固定坏素数排除，以及 reciprocity 和单位 \(\varepsilon\) 产生的相位，全部可写成模一个固定坏素数理想 \(\mathfrak b_0\) 的有界函数乘 \(\chi_v(z)^3\)。\(\mathfrak b_0\) 与 \(v\) 互素，且可对全部允许 \(g,e,f,v,\varepsilon\) 一致固定。

因为 \(v\ne1\) 平方自由，至少一个好素数上的 quadratic 因子非主；故这个周期函数模 \(\mathfrak b_0v\) 的平均严格为零，即使保留全部固定 coset 条件。

### 5. 第二次 Poisson 的真实尺度优势

上节每个 \(e,f\) 分量的 \(z\) 范数尺度为
\[
V=\frac{Y'}{q_gq_eq_f}.
\tag{5.1}
\]
利用 \(ge\mid D\)、\(q_f\le q_a\) 和 (4.1)，得到
\[
\begin{aligned}
\frac{V}{q_v}
&\ge \frac{Y' q_a^2}{q_Dq_f Z^{13/48+2\delta/3}}\\
&\gg Z^{\,23/48-d-(1/6-d)-13/48-2\delta/3}\,q_a\\
&=Z^{1/24-2\delta/3}q_a
\gg Z^{1/32}.
\end{aligned}
\tag{5.2}
\]
最后可放宽到 \(1/32\)，因为 \(\delta<1/64\)。关键是原 \(d\) 完全相消，而非将一个固定正余量错误地外推。

第二次 Poisson 现在应用于真正的非主 periodic character-weighted \(z\) 和。零 dual 向量消失。其余 dual 向量在原自对偶格子中的长度至少固定常数乘 \(q_v^{-1/2}\)。紧支撑 \(s\) 权及 (2.3) 的 Fourier 因子的任意固定阶导数，均由
\[
C_N(1+|\nu|)^{C_N}(1+X'q_H/q_c)^{-N}
\]
乘一个固定 \(Y'\) 的幂支配。
这里的导数均先取在归一变量 \(r=q_s/Y'\) 上：\(r\) 位于一个固定的正环带。
对 \(\widehat\Omega_\nu\) 的径向表达 \(\widetilde\Omega_\nu(A/r)\)，链式法则产生的
\(A^j\) 由提高 Schwartz 阶数吸收，而不产生新的 \(Z\) 次幂。
因此下面覆盖原前因子的固定指数 \(C_0\) 与分部积分次数无关。

对 \(z\) 做任意多次分部积分后，对每个 \(B>0\) 有
\[
\left|\sum_z(\text{完整周期系数})
       F_{c,H,g,e,f,\nu}(z/\sqrt V)\right|
\ll_B (1+|\nu|)^{C_B}Z^{C_0}
 V\left(\frac{q_v}{V}\right)^B.
\tag{5.3}
\]
这里 \(C_0\) 是覆盖原前因子及所需归一的固定数，与选择的目标负幂无关；也可以直接将那些原前因子留在外面。(5.3) 只用周期平均零和 Schwartz 衰减，不假设 GRH、SW 或 moving-twist 的原 R2 一致性。

在 (3.1)–(3.2) 内，\(c,D,H,e,f\) 的计数及原系数只有固定多项式增长；例如理想计数和粗除数上界即足够。由 (5.2) 选择 \(B\) 足够大，可吸收所有这些代价。再加回 §3 的两个尾，得到：

**定理。** 对每个 \(A>0\)，存在固定有限阶 \(C_A\)，一致于原全部 \(J\)、\(\sigma\)、重缩放素数组和实 \(\nu\)，有
\[
\boxed{
|\mathfrak S_{J,\sigma,\nu}^{\mathrm{rough,quad}}|
\ll_A (1+|\nu|)^{C_A}Z^{-A}.}
\tag{5.4}
\]
常数和起始阈值可依原固定算术数据、slot 系统和测试函数。原 mark 和全部 \(g,e,f\) 掩码已计入，\(v,a\) 共享素数没有被排除。

### 6. 该消去尚不覆盖的承重

(5.4) 消掉的是原线性探针里一个真实非零 dual 分支。对一般六次幂自由 \(u\)，active conductor 可达 \(q_u\asymp Z^{13/16}\)，而这里可保证的第二次 Poisson 长度最低仅 \(Y'/q_D\asymp Z^{5/16}\)。因此不能把二次核层的 \(1/24\) 余量外推给 generic cubic/sextic 层。

同样，当 \(c_0\) 带有 \(\le CY'\) 的素因子时，(4.3) 需要额外 moving divisor；它不再满足 \(ge\mid D\) 的关键比较，不能直接照搬 (5.2)。完整 \(n>1\) 的 Gauss/Euler 局部表也尚未并入本定理。R4 所需的剩余整体相关估计仍未证明。

### 固定来源

- 用户 `4495df1319b2ee655cc52cc90b7512371fd0f0c4`，`reports/20261011_qrh_selection_bridge/REPORT.md`，§7 的 R1–R4。
- 同一提交的 `COMPENSATION.md`，原 mark、重缩放与所有前因子。
- [`openai/math`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex) 固定提交 `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` 的 `paper.tex`，原 primary/self-dual 约定（§2）、`eq:general-probe`、`eq:local-F`、`eq:local-scalar-values`、`eq:signal`。

第一 Poisson 和 Gauss 局部表是这些来源的原身份。本稿额外使用原标记尺度以及第二次平滑 Poisson，取得上面限定粗糙残余/二次核层的统一快速消去。

# Part II. The full n=1 quadratic sector

## 原线性探针 n=1 层的完整非主二次核 dual 上界

### 结论

沿用 Part I of this report §1–2 的原 R4 对象、自对偶 Fourier 约定和准确第一次 Poisson 身份，保留外部 primitive \(\xi\)、全部原 Gauss 校正、标记、ray class 和零延拓。本稿不加粗糙条件。

固定原 \(J\)，记
\[
d\in[0,1/6],\quad X'\asymp Z^{17/48-d},\quad
Y'\asymp Z^{23/48-d},\quad P\asymp Z^{1/6-d},\quad Q=q_bX'Y'.
\tag{1}
\]
\(D\) 按剩余原 slot 求和，\(q_D\asymp P\)，所有原 slot 权重有界。
令 \(\mathfrak S^{(1,\mathrm{quad})}_{J,\sigma,\nu}\) 为原 R4 的 \(n=1\) 物理层作 \(m\)-Poisson 后，所有
\[
H=\varepsilon v^3a^6,\qquad v\ne1\text{ 平方自由好理想},\quad a\text{ 任意好理想}
\tag{2}
\]
的准确总贡献。单位 \(\varepsilon\) 有限，允许 \((v,a)>1\)。这里的 \(H\) 是原完整模 \(bsc\) 的频率，最小模的变量是 \(H/g\)，没有混用两者。

**定理。** 对每个 \(\epsilon>0\)，存在固定有限阶 \(C_\epsilon\)，一致于原全部 \(J,\sigma\)、重缩放素数组和实 \(\nu\)，有
\[
\boxed{
|\mathfrak S^{(1,\mathrm{quad})}_{J,\sigma,\nu}|
\ll_\epsilon (1+|\nu|)^{C_\epsilon}
 Z^{25/48-d/2+\epsilon}.}
\tag{3}
\]
乘原 Mellin 分离前因子 \(Q^{-1/2}\) 并积分后，对应原子探针贡献为
\[
\ll_\epsilon Z^{5/48+d/2+\epsilon}.
\tag{4}
\]
原补偿系数 \(q_r^{-3/2}\) 和重缩放素数组数仍须计入；按用户原计数，全部此层的补偿探针贡献因此为 \(O_\epsilon(Z^{5/48+\epsilon})\)。

本稿仅估计 \(n=1\) 的非主二次 sextic-core 层；不覆盖整个 \(B^J\) 或整个原探针。式 (3) 比所需 R4 的 \(Z^{11/48-d/2+\epsilon}\) 仍差 \(7/24\) 次幂，不声称 R4 或 RH 闭合。

### 1. 两次 Poisson 使用的准确因子

原第一 Poisson 简式给：令 \(c\) 平方自由，\(g=(c,s)\)。当 \((c,s/g)\ne1\) 时局部项为零；其余写 \(c=gc_1,s=gt\)，则完整原校正系数的 \(m\)-和变为
\[
\frac{Q\mu(c)\eta(c)}{\sqrt{q_b}\sqrt{q_s}q_c}
\sum_{H:g\mid H}\mathfrak c_g(H/g)
\chi_t(H)\overline{\chi_{c_1}(H)}\overline{\xi(H)}
\widehat\Omega_\nu\!\left(\frac{\sqrt Q H}{bsc}\right).
\tag{5}
\]
\(\mathfrak c_g\) 是原单位零掩码的 Ramanujan 和。所有 \(\gamma_2\)、\(\gamma_1\)、\(\alpha\)、\(G\)、\(\mathcal R\)、\(\Xi_*\)、\(\tau\) 的原相位在这一步准确相消为 \(\mu(c)\eta(c)\)。

对于固定 \(c,H\)，非零条件进一步给
\[
g=(c,\operatorname{rad}H),\qquad s=gt,\qquad(t,c)=1.
\tag{6}
\]
故 \(g\mid\operatorname{rad}H\)，而 \((c_1,H)=1\)。\(\chi_t(H)\) 已使 \((t,g)>1\) 的项为零，只需对剩余 \((t,c_1)=1\) 展开
\[
1_{(t,c_1)=1}=\sum_{e\mid c_1,e\mid t}\mu(e).
\tag{7}
\]
保留所有标记条件 \(D\mid gc_1\)。

在 (2) 中，
\[
\chi_t(H)=\chi_t(\varepsilon v^3)1_{(t,a)=1}.
\]
因 \((e,H)=1\)，设 \(t=e t_1\) 后，第二个 mask 准确展开为
\[
1_{(t_1,a)=1}=\sum_{f\mid\operatorname{rad}a,f\mid t_1}\mu(f).
\tag{8}
\]
相应原字符值 \(\chi_f(\varepsilon v^3)\) 若为零就取零。写 \(t=efz\)，剩余 \(z\)-字符在好素数上恰为 primitive quadratic \(\chi_v(z)^3\)。全部固定 primary/ray/坏素数条件只乘一个模固定坏素数理想的有界周期函数。

原 \(s\)-支撑使
\[
q_gq_eq_f\ll Y',
\qquad V:=\frac{Y'}{q_gq_eq_f}
\tag{9}
\]
是这个 \(z\)-和的范数尺度。若支撑为空则直接取零，不把空短和延长成一个人为的长和。

### 2. 全尺度的平滑 quadratic 字符界

设 \(v\ne1\) 平方自由、避开固定坏素数。对任意 \(V>0\) 和固定紧环带上的光滑 \(F\)，包括固定 primary/ray 掩码，有
\[
\left|\sum_z(\text{固定坏素数周期系数})\,
 \chi_v(z)^3 F(z/\sqrt V)\right|
\ll \sqrt{q_v}\,\mathfrak p(F),
\tag{10}
\]
其中 \(\mathfrak p\) 是固定有限阶的 Schwartz/导数半范数；常数与 \(v,V\) 无关。

证明：周期模为固定坏理想乘 \(v\)，其平均为零。规范化有限 Fourier 系数由 primitive quadratic Gauss 和界为 \(Cq_v^{-1/2}\)。第二次 Poisson 的前因子为 \(V\)，剩余 dual 向量的 Schwartz 和为
\[
\ll\begin{cases}
q_v/V,&V\le q_v,\\
(V/q_v)^{-B},&V\ge q_v,
\end{cases}
\]
对固定足够大的 \(B\) 成立，零向量已由非主性删除。第一行与前因子抵消给 \(\sqrt{q_v}\)，第二行也不超过这个上界。固定坏模仅改变常数，(10) 得证。

应用于 (5) 时，对归一变量 \(r=q_s/Y'\) 作导数。\(r\) 在固定正环带；\(\widehat\Omega_\nu\) 的链式幂由 Schwartz 衰减吸收。因此在 \(q_c\asymp C\) 的环带上，相应半范数不超过
\[
C_N(1+|\nu|)^{C_N}
\left(1+\frac{X'q_H}{C}\right)^{-N}
\tag{11}
\]
乘原共同因子 \(Y'^{-1/2}\)。不存在随分部积分次数增长的额外 \(Z\) 次幂。

### 3. reciprocal 列质量与完整 slot 的共享素数补偿

先固定一个 \(c\) 环带 \(q_c\asymp C\)，以及 \(g,e,H\)。写 \(c=gc_1\)。标记与 (7) 要求
\[
D/(D,g)\mid c_1,
\qquad e\mid c_1.
\]
令
\[
L=\operatorname{lcm}(e,D/(D,g)).
\]
以理想计数并删掉其余限制，在任意正 \(C/q_g\) 尺度上准确有
\[
\sum_{\substack{q_{c_1}\asymp C/q_g\\L\mid c_1}}q_{c_1}^{-1}
\ll q_L^{-1}.
\tag{12}
\]
若非空，则 \(q_L\ll C/q_g\)，由此也吸收格点计数的常数项。等价地，可直接将 \(c_1=Lc_2\) 后用每个 annulus 的 reciprocal 理想质量一致有界。原 Gaussian 在此环带取统一上界即可；其中心 \(Zq_D/q_g\) 随 \(D\) 变化不影响 (12)。

又 \(|\mathfrak c_g(H/g)|\le q_g\)。它与 (5) 中 \(q_c^{-1}=(q_gq_{c_1})^{-1}\) 的 \(q_g^{-1}\) 抵消，不额外损失 \(q_g\)。

下面的 slot 和是关键：在 (9) 的 \(q_gq_e\ll Y'\) 下，
\[
\boxed{\sum_{D\text{ 原 slots}}
 \frac{|w_D|}{q_{\operatorname{lcm}(e,D/(D,g))}}
\ll_{\rm slots}\frac1{q_e}.}
\tag{13}
\]
证明：对每个 slot，其某个素数 \(p\) 的额外局部因子是 \(1\)（若 \(p\mid eg\)）或 \(q_p^{-1}\)（否则）；共同外因子为 \(q_e^{-1}\)。因不同 slot 的素数集互不相交，求和按 slots 分解。
固定环带的理想计数给 \(\sum_{p\in\mathcal P_i}q_p^{-1}\ll1\)。若窗口下端 \(q_p\ge c_iZ^{\ell_i}\)，则
\[
\#\{p\in\mathcal P_i:p\mid eg\}
\le\frac{\log(CY')}{\log(c_i Z^{\ell_i})}=O_{\rm slots}(1).
\]
每个 \(\ell_i>0\) 固定，故各局部和一致有界。空 slot 乘积也包括。这里未把共同素数当作独立，也未删掉任何原 character；仅在已经取绝对值的上界中计数。

最后
\[
\sum_{q_e\ll Y'}q_e^{-1}\ll\log(2+Y').
\tag{14}
\]
因此 \(c,D,e\) 的全部绝对质量只有对数损失，而不是一个额外标记计数因子。

### 4. 完整二次核频率的加权计数

对于固定 \(H\)，\(g\mid\operatorname{rad}H\) 和 \(f\mid\operatorname{rad}a\) 的数目至多是 \(q_H^\epsilon\) 乘一个依 \(\epsilon\) 的常数。该除数界不要求 \((v,a)=1\)。
对任意 \(K>0\)，\(N\) 足够大时，理想计数给
\[
\begin{aligned}
\sum_{v\ne1\ {\rm sf},a}\sqrt{q_v}\,q_H^\epsilon
 \left(1+\frac{q_v^3q_a^6}{K}\right)^{-N}
&\ll_\epsilon K^{1/2+O(\epsilon)}\quad(K\ge1),\\
\sum_{v\ne1\ {\rm sf},a}\sqrt{q_v}\,q_H^\epsilon
 \left(1+\frac{q_v^3q_a^6}{K}\right)^{-N}
&\ll_\epsilon K^{1/2}\quad(0<K\le1).
\end{aligned}
\tag{15}
\]
第一行的小幂可按需重新命名。其基本原因是
\[
\sum_{q_v\le T}\sqrt{q_v}\ll T^{3/2},\qquad
T=K^{1/3}/q_a^2,
\]
故得到 \(K^{1/2}\sum_aq_a^{-3}\)，后者收敛；外部 dyadic Fourier 尾用 (11) 求和。小 \(K\) 时可用任意高的 Fourier 衰减直接控制。本式不是无权删掉 \(H\) 尾。

### 5. Gaussian 环带求和和原指数

令 \(C_j=e^j ZP\)，用固定重叠 annuli 分解 \(c\)。因为全部原 \(q_D/P\) 位于固定紧区间，
\[
W_G(q_c/(Zq_D))\ll C_0e^{-c_0 j^2}
\quad(q_c\asymp C_j)
\tag{16}
\]
可对所有标记一致取值。这里完整保留 Gaussian 尾，没有把不满足硬截断的项当作零。

原 R4 中 (5) 的共同前因子，加上 \(Y'^{-1}\) 的外部平均以及 \(q_s^{-1/2}\asymp Y'^{-1/2}\)，为
\[
O\left(\frac{Q}{Y'^{3/2}}\right)
\]
（固定 \(q_b\) 吸入常数）。合并 (10)–(16)，在每个 \(j\) 上得到
\[
\ll_\epsilon (1+|\nu|)^{C_\epsilon}
 \frac{Q}{Y'^{3/2}}e^{-c_0j^2}
 \left(\frac{C_j}{X'}\right)^{1/2}
 Z^{\epsilon}e^{O(\epsilon|j|)}.
\tag{17}
\]
无标记或列支撑为空的 annulus 直接为零；极小 \(K=C_j/X'\) 用 (15) 第二行。对 \(j\) 求和，Gaussian 吸收所有固定指数和小幂，得到
\[
|\mathfrak S^{(1,\mathrm{quad})}|
\ll_\epsilon (1+|\nu|)^{C_\epsilon}
 \frac{Q}{Y'^{3/2}}\left(\frac{ZP}{X'}\right)^{1/2}Z^\epsilon.
\tag{18}
\]
将 (1) 代入，指数准确为
\[
(5/6-2d)-\tfrac32(23/48-d)+\tfrac12(13/16)
=25/48-d/2.
\]
而 \(Q^{-1/2}\) 给
\[
25/48-d/2-(5/12-d)=5/48+d/2.
\]
原 \(\widehat W_0(i\nu)\) 的任意阶衰减吸收 \((1+|\nu|)^{C_\epsilon}\)。这证明 (3)–(4)。

### 限定

本定理没有使用 GRH、moving-numerator 的未证 R2 一致性、或不适用的 cubic dispersion 黑箱。它控制原始线性配对中一个完整非零 dual 核型，且使用真实 slot 的共享素数结构。

尚未控制的部分包括 \(n>1\) 的局部两支相消、generic cubic/sextic \(H\)-核以及 \(H=\varepsilon a^6\) 主行。即使将这一个层的界计入全部原补偿，它仍没有达到 \(Z^{-3/16+\epsilon}\) 的完整低端目标。

来源与原 Fourier 身份同配套 Part I of this report；其中第一 Poisson/CRT 归一已独立审核。本稿新增的是不加粗糙限制的二次核总量上界及 (13) 的真实 slot LCM 密度拼合。

# Part III. The complete quadratic dual sector for all physical n

## The complete nonprincipal quadratic dual sector, with all physical square layers

### Result and scope

Fix the original rescaling J, ray class sigma and Mellin parameter nu. Write
\[
 X'\asymp Z^{17/48-d},\quad Y'\asymp Z^{23/48-d},\quad
 q_D\asymp P=Z^{1/6-d},\quad Q=q_bX'Y',\quad0\le d\le1/6.
\]
The remaining original prime slots and their bounded weights are fixed at this Z. For a second positive parameter 0<T<=Z, change only the marked row's Gaussian argument from q_c q_n^3/(Zq_D) to q_c q_n^3/(Tq_D). Keep X',Y', every original auxiliary character, every Gauss factor, every zero extension and every slot unchanged.

After exact m-Poisson using the original full modulus bscn^3, select the entire set of frequencies
\[
 H=\varepsilon v^3a^6,\qquad v\ne1\text{ good squarefree},\quad
 a\text{ good},                                       \tag{1}
\]
with arbitrary unit epsilon and with no coprimality required between v and a. Let S_quad(T) denote this contribution to the true linear R4 pairing, summed over **all** original physical n. The same definition can instead use the changed core marker D|c n_0, where n=n_0r^2 with n_0 squarefree.

**Theorem.** For either of these two precisely stated markings,
\[
 \boxed{|S_{\rm quad}(T)|\ll_\epsilon
 (1+|\nu|)^{C_\epsilon}Z^\epsilon
 \frac{Q}{Y'^{3/2}}\left(\frac{TP}{X'}\right)^{1/2},
 \qquad0<T\le Z.}                                    \tag{2}
\]
In particular, the original T=Z contribution is
\[
 O_\epsilon((1+|\nu|)^{C_\epsilon}Z^{25/48-d/2+\epsilon}). \tag{3}
\]
The exact Möbius-decompleted core-marked probe has the same bound for its complete nonprincipal quadratic dual sector. Its normalized finite compensation, and that of the original probe for this sector, are O_epsilon(Z^{5/48+epsilon}). These are bounds for one complete nonzero numerator-core type. They do not estimate the principal/unit-core, generic cubic/sextic types, or the whole R4 pairing; they remain 7/24 short of the critical low target.

### 1. Remove the infinite physical square layer without discarding its masks

Write the old physical index uniquely as n=n_0r^2, n_0 squarefree. The exact coefficient identity, already proved from the original alpha, eta, Xi, R and G conventions, is
\[
 b(c,n_0r^2;s)=b(c,n_0;s)\kappa(r),\qquad
 \chi_{cn_0^3r^6}(m)=\chi_{cn_0^3}(m)1_{(r,m)=1}.
\]
Here \(\kappa(r)=\eta(r)^6\overline{\alpha(r)}^6\). No coprimality among c,n_0,r is assumed. Consequently this layer has coefficient kappa(r)/q_r^2 and Gaussian W_G(q_c q_{n_0}^3 q_r^6/(Tq_D)). Expand its remaining unit mask exactly:
\[
 1_{(r,m)=1}=\sum_{h\mid\operatorname{rad}r,\ h\mid m}\mu(h).
                                                               \tag{4}
\]
A term with (h,cn_0)!=1 is zero by the character already present, and is kept as zero.

For a surviving term put j=(h,rad s), k=h/j. The prime-power Gauss formula shows that any p|j with v_p(s)=1 contributes zero. If v_p(s)>=2, the Gauss sum is already supported on p|m, including the v_p(s)=0 mod 6 Ramanujan case. The surviving s therefore satisfy
\[
 j^2\mid s,\quad(s,k)=1,\quad(h,cn_0)=1,              \tag{5}
\]
and (4)'s m restriction reduces to k|m. Write m=k m'. Its precise arithmetic multiplier is
\[
 \xi(k)\chi_{cn_0^3}(k)\overline{\chi_s(k)}.           \tag{6}
\]
It has modulus one because (k,bscn_0)=1.

Use the full base modulus M=bscn_0^3 for m'. If L is its frequency, the original full modulus Mr^6 for m has frequency
\[
 H=(r^6/k)L.                                          \tag{7}
\]
This includes all redundant-period divisibility conditions. At p|r, b_p=v_p(r), the exponent of H is at least 6b_p-1. An exponent of a quadratic core as in (1) is 0 or 3 modulo 6, so it is at least 6b_p. Thus r|a. Write
\[
 H'=H/r^6=\varepsilon v^3(a')^6,\quad a'=a/r,
 \qquad L=kH'.                                       \tag{8}
\]
Substitution of L=kH' cancels (6) exactly in the finite Fourier coefficient. This also follows directly from the unit covariance f(km')=(6)f(m') of the entire original periodic arithmetic function: its normalized Fourier coefficient at kH' is multiplied by the inverse of (6). The Fourier argument after m=k m' is sqrt Q L/(kM), hence becomes sqrt Q H'/M. The only remaining change in the completion prefactor is q_k^{-1}.

This argument retains the unit of H and its sixth-power-free core. It does not relabel an unrelated Fourier sum. All squarefree-n_0 computations below are therefore in the true core (1), with a' in place of a, a row scale T/q_r^6, and the exact additional support (5).

### 2. The two physical squarefree-n branches on a quadratic core

We record the needed consequence of the source's coefficientwise Gauss/CRT identity, including its ray cancellation. If p|n_0, the local table for a quadratic frequency has exactly two nonzero choices:

- p does not divide c, v_p(s)=1 and v_p(H')=3;
- p divides c, v_p(s)=0 and v_p(H')=3.

There is no case v_p(H')=3+6b with b>0. Thus
\[
 n_0\mid v,\qquad(n_0,a')=1.                         \tag{9}
\]
Put E=(c,n_0), F=n_0/E. Both are squarefree, and (E,F)=1. The E branch is shared with c; the F branch forces s once. Their normalized completed local magnitudes are respectively
\[
 P^{-2}=P^{-1}_{\ c}\,P^{-1}_{\ n_0},\qquad
 P^{-3/2}=P^{-1/2}_{\ s}\,P^{-1}_{\ n_0}.             \tag{10}
\]
For an independent check directly from the original local scalar C: the F branch has t=3,k_s=1,j'=3 and C=G_1P^2G_2 of magnitude P^3; the E branch has t=4,k_s=0,j'=3 and C=P^3G_4 of magnitude P^{7/2}. Division by the source's exact q_c^{1/2}q_{n_0}q_A normalization gives (10), retaining the separate s^{-1/2} factor.

At all other primes the audited n=1 completion applies. Define
\[
 g=(c,\operatorname{rad}H')/E,\qquad
 c=Egc_1,\qquad s=Fg j^2t.
\]
Every surviving term has (g,n_0h)=1, (c_1,n_0hH')=1, and the required coprimality of the remaining free s variable is retained. The Gauss support forces s once at g. Its Ramanujan factor has magnitude at most q_g, **not** q_{Fg}. The latter distinction is essential.

The original coefficientwise cancellation of all CRT and fixed-ray factors leaves the free-t character chi_t(H'), multiplied by a uniformly bounded function of one fixed bad modulus and by phases independent of t. In particular its moving good-prime part is precisely the primitive quadratic chi_v(t)^3. It does not turn into a cubic character at the forced F primes: those primes have already been extracted from s, and their rho^{-2}/rho^{-4} factors are fixed coefficients of the row H'. Zeros when t meets H', or when j meets H', are retained. This assertion is the coefficient identity behind the source's scalar Euler product, not an assumption that its finite-ray refinement G is multiplicative.

The completed coefficient has absolute prefactor
\[
 \frac{Q}{\sqrt{q_b}\sqrt{q_s}\,q_cq_{n_0}}
   |\mathfrak c_g|,
\]
besides q_r^{-2}q_k^{-1}, the original weights and unit phases. After q_c=q_Eq_gq_{c_1}, the Ramanujan bound cancels only q_g, leaving the useful factor
\[
 \frac1{q_{n_0}q_E}\,\frac1{q_{c_1}}.                \tag{11}
\]

### 3. Second Poisson and the true marked-column density

Expand the c_1 coprimality mask with the free t over e|c_1. The remaining k and sixth-power-a' masks can be expanded over f|rad(k a'). Their coefficients are zero if they meet v. Since e is coprime to hH', no hidden shared e mask occurs. After t=efz the s norm scale is
\[
 V=Y'/(q_Fq_gq_j^2q_eq_f).
\]
The primitive quadratic smooth character bound O(sqrt(q_v)) holds for every positive V, including short scales. Nonempty s support gives q_Fq_gq_eq_j^2q_f<<Y'. All derivatives are in the normalized variable q_s/Y' on a fixed positive annulus. The original Fourier weight retains
\[
 (1+X'q_{H'}/(Cq_{n_0}^3))^{-N}
\]
when q_c is in an annulus C; all chain-rule powers are absorbed by Schwartz decay.

For the original completed-index marking D|cn, the condition is D|cn_0r. Hence the reciprocal c_1 column mass is at most a constant times
\[
 q_{\operatorname{lcm}(e,D/(D,gn_0r))}^{-1}.          \tag{12}
\]
For core marking replace gn_0r by gn_0. This reciprocal ideal-count bound is uniform in every positive column scale, including empty or subunit annuli.

For all Fourier frequencies, without a hard H' cutoff, the actual slot sum satisfies
\[
 \sum_D\frac{|w_D|}{q_{\operatorname{lcm}(e,D/(D,gn_0r))}}
 \ll_{\epsilon,\rm slots}\frac{(q_rq_{H'})^\epsilon}{q_e}.
                                                               \tag{13}
\]
Indeed the extra local factor of a slot prime is one if it divides egn_0r and 1/q_p otherwise. The reciprocal sum over the whole prime window is O(1). The number of its prime divisors in egn_0r is
\[
 O_{\rm slots}\!\left(1+
    \frac{\log(2q_rq_{H'})}{\log Z}\right),
\]
since q_ge<<Y' and q_{n_0}<=q_v<=q_{H'}^{1/3}. The product over finitely many fixed slots is bounded by the displayed arbitrarily small power. This proves (13) for the genuine Gaussian/Fourier tails too. Summing e costs O(log Z).

The remaining g and f choices cost only (q_rq_{H'})^epsilon. Finally the **weighted** sum of both squarefree-n_0 branches is
\[
 \sum_{n_0\mid v}\sum_{E\mid n_0}\frac1{q_{n_0}q_E}
 =\prod_{p\mid v}(1+q_p^{-1}+q_p^{-2})
 \ll_\epsilon q_v^\epsilon.                          \tag{14}
\]
Constraints such as (n_0,a')=1 merely delete positive terms in this majorant. This is where both original j=3 branches are retained, rather than charging a forced divisor to the s length and discarding its companion branch.

### 4. Simultaneous physical and Fourier tails

For fixed n_0,r take Gaussian annuli
\[
 C_l=e^l TP/(q_{n_0}^3q_r^6).
\]
Their common Gaussian bound is O(exp(-c l^2)), uniformly over the original D. Crucially
\[
 K_l=C_lq_{n_0}^3/X'=e^l TP/(q_r^6X')
\]
is independent of n_0. Thus the weighted n_0 sum (14) can be performed before the quadratic frequency count. With all its small divisor powers included, that count is O(K_l^{1/2+epsilon}) for K_l>=1 and O(K_l^{1/2}) for K_l<=1. It follows from sum_{q_v<=B}sqrt(q_v)=O(B^{3/2}) and the convergent ideal sum sum_{a'}q_{a'}^{-3}; Schwartz tails are retained, not discarded.

Since 0<T<=Z and the original X',P are fixed powers of Z, all positive small powers of K_l are absorbed by Z^epsilon exp(O(epsilon|l|)). Gaussian summation in l is uniform, including q_r^6>TP. We obtain for fixed r,h,j, k=h/j,
\[
 \ll_\epsilon(1+|\nu|)^{C_\epsilon}Z^\epsilon
 \frac{q_r^{-5+\epsilon}}{q_k}
 \frac{Q}{Y'^{3/2}}\left(\frac{TP}{X'}\right)^{1/2}.   \tag{15}
\]
The power q_r^{-5} consists of the exact q_r^{-2} coefficient and q_r^{-3} from the Gaussian scale. The number of pairs h|rad r, j|h is at most 3^{omega(r)}<<q_r^epsilon. Therefore their complete sum and then the r sum converge absolutely, proving (2).

### 5. Core marking, exact decompletion and the original normalization

The proof of (2) applied directly to core marking, with its stated condition D|c n_0. No inequality between two oscillatory marked rows was used. The decompleted probe is the exact sum over external d of the same core-marked probe with T=Z/q_d^6 and coefficient mu(d)kappa(d)/q_d^2. On the original absolute lines this is its defining arithmetic operation. Lifting each original modulus by d^6 multiplies the dual index by d^6, preserving the unit and the sixth-power-free core; hence the sector (1) commutes with this operation. Equation (2) is uniform for these T, so its sector sum is bounded by
\[
 \sum_dq_d^{-2}q_d^{-3}<\infty
\]
times (3). This also gives absolute justification after completion. This use of the positive column-scale exponent 1/2 does not presume transfer of the unproved negative critical low exponent.

Finally
\[
 \frac{Q}{Y'^{3/2}}\left(\frac{ZP}{X'}\right)^{1/2}
 \asymp Z^{25/48-d/2}.
\]
The original Q^{-1/2} factor gives 5/48+d/2; the original q_rho^{-3/2} finite compensation coefficient and its Z^d tuple count remove this d/2, leaving 5/48. Here rho denotes the original rescaling product, distinct from the physical square variable r used above. The original Mellin weight absorbs the polynomial dependence on nu.

### Exact dependencies

- The [fixed source QRH paper](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb: exact Poisson series and coefficientwise unit cancellation, local scalar and family tables (source lines 3735–4145). In particular both j=3 physical odd branches are used.
- The audited Part II of this report: full-modulus n=1 normalization, all-scale quadratic Poisson bound, reciprocal column count and weighted Fourier/Gaussian tails.
- The audited arithmetic coefficient identity and exact Möbius operation in [EULER_DECOMPLETION.md, Parts II and IV](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/dfc211e29c3ac231ada82a640601753c9a119695/reports/20261011_qrh_selection_bridge/EULER_DECOMPLETION.md).
- The explicit unit-covariant square-layer completion in §§1–2 above. All row primes, fixed auxiliary xi, and every zero extension remain present.

No QRH/GRH zero-free input, conjectural Möbius cancellation, moving-numerator R2 uniformity, or unproved cubic dispersion estimate is used. This establishes a complete partial-core estimate, not the missing whole-probe correlation.

# Part IV. A common-coefficient quadratic two-column estimate

## A common-coefficient quadratic two-column estimate

This is an analytic interface for the actual quadratic branch of the Poisson calculation. It does not by itself establish that every remaining physical phase has the required coefficient separation. The latter is a separate arithmetic identity.

Let \(K=\mathbb Q(\sqrt{-3})\), \(q_{\mathfrak a}=N\mathfrak a\), with the original primary generators and fixed excluded set \(S\). Write
\(\psi_v(n)=\chi_v(n)^3=(n/v)_2\), including its zero extension. The row \(v\) is squarefree, good, and \(q_v\asymp V\ge1\). We allow a fixed finite decomposition by ray classes and fixed ray twists. The estimates apply to an arbitrary subset of the rows.

For the long smooth column below, require that its **actual character after all fixed twists** is nonprincipal and has conductor comparable to \(q_v\), with fixed comparison constants. This is automatic for nonunit good squarefree \(v\), since a fixed \(S\)-twist cannot remove its good ramified primes. Unit rows or fixed-conductor exceptional pieces must be kept separately unless their actual nonprincipal character is retained before taking absolute values.

### 1. Two separate column norms

Let \(L\ge1\), and let \(\lambda_c\) be coefficients independent of \(v\), supported on good squarefree \(c\), \(q_c\asymp L\), with
\[
 \sum_c|\lambda_c|^2\ll_\epsilon L^{-1+\epsilon}.
 \tag{1}
\]
Thus divisor-bounded weights divided by \(q_c\) are allowed. Fixed conditions such as \((c,a e)=1\), or finitely many prescribed column divisors, may be included if (1) is checked for the resulting common coefficients. Goldmakher–Louvel gives
\[
 \left(\sum_{v\asymp V}\left|\sum_c\lambda_c\psi_v(c)\right|^2\right)^{1/2}
 \ll_\epsilon(VL)^\epsilon\sqrt{1+V/L}.
 \tag{2}
\]
The exact squarefree quadratic input is Theorem 1.1 of [GL]; primary symbols are matched after fixed ray separation as in the source lemma quadratic, fixed QRH October 5 manuscript, lines 1886–1920. The character family and its transpose have the same bound. No arbitrary row-dependent inner coefficients are permitted.

Let \(S_0\ge1\), and let
\[
 B_v(S_0)=\sum_{s\ {\rm good}}\rho(s)\psi_v(s)W(q_s/S_0),
 \tag{3}
\]
where \(\rho\) is a fixed ray character (or fixed finite combination), \(W\) is a common smooth annular test, and all nonprincipal conditions above hold for each retained component when Poisson is used. Unlike the \(c\)-column, this sum allows arbitrary powers in \(s\).

For every \(A>1\), uniformly over common tests with the requisite fixed seminorm bounds,
\[
 \left(\sum_{v\asymp V}|B_v(S_0)|^2\right)^{1/2}
 \ll_{\epsilon,A}(VS_0)^\epsilon
 \mathcal B_A(V,S_0),
 \tag{4}
\]
where
\[
 \mathcal B_A(V,S_0)=
 \begin{cases}
  \sqrt{VS_0},&1\le S_0\le V,\\
  S_0(S_0/V)^{-A},&S_0\ge V .
 \end{cases}
 \tag{5}
\]

For the first line, uniquely write \(s=t\ell^2\), \(t\) squarefree. At each fixed \(\ell\),
\(\psi_v(s)=\psi_v(t)1_{(v,\ell)=1}\); this is a restriction of the positive outer row sum. The common \(t\)-coefficient mass is \(O(S_0/q_\ell^2)\), up to small powers. Applying [GL] and Minkowski gives
\[
 \sqrt{VS_0}\sum_{q_\ell\ll\sqrt{S_0}}q_\ell^{-1}
 +S_0\sum_\ell q_\ell^{-2}
 \ll \sqrt{VS_0}\log(2+S_0)+S_0.
 \tag{6}
\]
For \(S_0\le V\), this is (4). This square-layer step cannot be omitted by pretending the original \(s\)-column is squarefree.

For the second line of (5), use two-dimensional smooth Poisson for the actual nonprincipal character of conductor norm \(\asymp V\). Its zero Fourier frequency vanishes; its nonzero finite Fourier coefficients have modulus at most a fixed multiple of \(\sqrt V\). Fourier decay and lattice counting therefore give, for each row,
\[
 |B_v(S_0)|\ll_A
 (S_0/\sqrt V)(S_0/V)^{-A}\qquad(S_0\ge V),
 \tag{7}
\]
after taking sufficiently many derivatives. There are \(O(V)\) rows. This proves (4). Fixed excluded primes only cause a fixed finite decomposition. Formula (7) is not asserted for arbitrary divisor-bounded coefficients in the \(s\)-sum.

### 2. The finite divisor-scale sum

Let \(C,Y,G,f,V\ge1\). At each good ideal \(e\), put
\[
 L_e=\frac C{Gq_e},\qquad S_e=\frac Y{Gf q_e}.
 \tag{8}
\]
Only the actual finite range
\[
 1\le q_e\le E,\qquad
 E\ll\min\{C/G,Y/(Gf)\}
 \tag{9}
\]
is used. Fixed annular comparison constants may enlarge this cutoff; scales between a fixed positive constant and one are handled by a fixed rescaling. In particular, (9) is essential: an unrestricted infinite \(e\)-sum would contain a divergent harmonic term.

Suppose the true \(e\)-piece, after a common smooth separation, is
\[
 \frac{\omega_e}{q_e}
 \sum_{v\asymp V} a_{v,e}
 \left(\sum_{c\ {\rm sf}}\lambda_{e,c}\psi_v(c)\right)
 B_{v,e}(S_e),
 \tag{10}
\]
or its conjugate orientation, where
\(|\omega_e|,|a_{v,e}|\ll\mathfrak X^\epsilon\), the common column \(\lambda_{e,c}\) satisfies (1) at \(L_e\), and \(B_{v,e}\) is of the precise smooth type (3). The ambient \(\mathfrak X\ge2\) bounds all parameters by fixed powers. Row restrictions depending on \(e\), such as \((v,e)=1\), are harmless. Cauchy, (2) and (4) bound (10) by small powers times
\[
 q_e^{-1}\sqrt{1+VGq_e/C}\,
            \mathcal B_A(V,Y/(Gf q_e)).
 \tag{11}
\]

#### Proposition

For \(A>1\),
\[
\boxed{
 \sum_{1\le q_e\le E}\frac1{q_e}
 \sqrt{1+\frac{VGq_e}{C}}\,
 \mathcal B_A\!\left(V,\frac Y{Gf q_e}\right)
 \ll_A
 V\left(1+\sqrt{\frac Y{Cf}}\right)\log(2+E).}
 \tag{12}
\]
Consequently the sum of the actual pieces (10) is bounded by
\(\mathfrak X^\epsilon V(1+\sqrt{Y/(Cf)})\), after choosing the initial small powers appropriately.

**Proof.** Put \(E_0=Y/(GfV)\).
For \(q_e\ge E_0\), the summand is at most a fixed multiple of
\[
 \sqrt{\frac{VY}{Gf}}
 \left(q_e^{-3/2}+\sqrt{\frac{VG}{C}}q_e^{-1}\right).
 \tag{13}
\]
Ideal counting gives
\(\sum_{R\le q_e\le E}q_e^{-3/2}\ll R^{-1/2}\) for \(R\ge1\), and
\(\sum_{q_e\le E}q_e^{-1}\ll\log(2+E)\).
If \(E_0\ge1\), the first coefficient times \(E_0^{-1/2}\) is exactly \(V\); if \(E_0<1\), its value is at most \(V\). The second coefficient is \(V\sqrt{Y/(Cf)}\). This bounds the short-column range.

For \(q_e\le E_0\), necessarily \(E_0\ge1\), the summand is at most
\[
 V E_0^{1-A}
 \left(q_e^{A-2}+\sqrt{VG/C}\,q_e^{A-3/2}\right).
 \tag{14}
\]
Since \(A>1\), ideal counting gives respective sums
\(O_A(E_0^{A-1})\) and \(O_A(E_0^{A-1/2})\). Thus this range costs
\[
 O_A\{V(1+\sqrt{VG E_0/C})\}
 =O_A\{V(1+\sqrt{Y/(Cf)})\}.
 \tag{15}
\]
This proves (12), including empty ranges. QED.

### 3. How a moving gcd is allowed, and what must be checked

One may absorb an entire finite sum over \(g\mid\operatorname{rad}(v a)\), \(q_g\asymp G\), into \(a_{v,e}\), provided:

1. all surviving \(g\)-dependence outside the smooth weights is independent of both inner columns \(c,s\);
2. its total absolute coefficient mass is divisor-bounded;
3. the weights admit a common Mellin/Fourier separation with uniformly integrable seminorm majorants;
4. all remaining zero masks in \(c\) are either the true \(\psi_v(c)\) zero extension or fixed common column conditions, and the \(s\)-column retains precisely the common smooth fixed-character form required for (7).

Fixed dyadic ratios \(q_g/G\) can then be separated into bounded row multipliers. A common separated integral is handled by Minkowski before applying (2)–(4). There is no factor \(G^{1/2}\) merely because \(g\) varies with the row: its divisor-many choices have already been summed in the row coefficient. Conversely, if a residual phase or mask couples \(g\) to either inner column and cannot be separated with these properties, (12) alone does not control that physical expression.

This proposition validates the analytic budget and common-coefficient large-sieve step. It does not certify an unproved CRT cancellation or automatically establish the claimed full quadratic R4 exponent.

### Primary sources

[GL] Goldmakher–Louvel, [A quadratic large sieve inequality over number fields, arXiv:1112.1642v2](https://arxiv.org/pdf/1112.1642), Definition 1, Theorem 1.1 and Corollary 1.2. Both large-sieve indices there are squarefree.

The matching to primary \(\chi_v^3\) is also explicitly given in the [fixed October 5 QRH manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), lemma quadratic, lines 1886–1920. That manuscript's global \(11/12\) conclusion is not a new input to this argument; only its explicit fixed-ray normalization is used.

# Part V. Bilinear saving for the complete physical quadratic sector

## A genuine bilinear saving for the complete quadratic dual sector

### Claim and scope

Keep the objects, scales, original prime slots and all normalizations of Part III of this report. Its nonprincipal quadratic sector is the entire set H=epsilon v^3 a^6, v nonunit squarefree, with all physical indices n and their original zero extensions. The two admissible markings are the original D|cn and the explicitly changed core marker D|c n_0, n=n_0r^2.

**Theorem (independently reviewed).** For both markings at the original scale,
\[
 |S_{\rm quad}(Z)|\ll_\epsilon(1+|\nu|)^{C_\epsilon}
 Z^{37/96-d/2+\epsilon}.                              \tag{1}
\]
The exact Möbius-decompleted core-marked probe and the original-marked Möbius-decompleted probe both satisfy the same bound. After the original Q^{-1/2} normalization and finite signed compensation, this complete dual type contributes
\[
 \boxed{O_\epsilon(Z^{-1/32+\epsilon}).}               \tag{2}
\]
This gains 13/96 over the earlier complete quadratic-sector estimate. The principal/unit-core and generic cubic/sextic dual types are outside (1), and the whole-probe negative target is still 5/32 stronger.

The proof keeps the actual linear s--m pairing. Its new input is the quadratic large sieve applied after an exact common-coefficient reorganization; no stronger full positive Gram is substituted for the R4 target.

### 1. The analytic common-coefficient lemma

Let chi_v^3 be the exact primitive quadratic Hecke family on squarefree primary good ideals v in a norm interval V<=q_v<=2V, V>=1, with a fixed finite ray partition if needed. Goldmakher--Louvel gives
\[
 \sum_v\left|\sum_{c\ {\rm sf}} a_c\chi_v(c)^3\right|^2
 \ll_\epsilon(VL)^\epsilon(V+L)\sum_c|a_c|^2           \tag{3}
\]
when the columns have norm O(L). All allowed column coefficients below are independent of v.

For squarefree columns of norm about L and coefficients a_c/c with divisor-bounded a_c, the resulting norm is
\[
 \ll_\epsilon(VL)^\epsilon(1+V/L)^{1/2}.              \tag{4}
\]
Fixed column masks are allowed, as are bounded row weights. For a smooth sum over all primary s of norm about S, with only a fixed ray factor and fixed smooth weight, squarefree decomposition s=t ell^2 and Minkowski give
\[
 \Big\|\sum_s F(q_s/S)\chi_v(s)^3\Big\|_{\ell^2(v)}
 \ll_\epsilon(VS)^\epsilon(\sqrt{VS}+S).              \tag{5}
\]
The ell-induced row restriction (v,ell)=1 is deleted only inside its positive norm. Indeed the two sums in Minkowski are bounded by sqrt(VS) sum_{q_ell<=sqrt S}q_ell^{-1} and S sum_ell q_ell^{-2}.

For S>=V, the actual primitive smooth Poisson estimate is sharper than (5): each row is O(S/sqrt V (S/V)^{-A}), and the row norm is
\[
 O_A(S(S/V)^{-A}).                                   \tag{6}
\]
Thus one may use B(V,S)=sqrt(VS) for S<=V and B(V,S)=S(S/V)^{-A} for S>=V, with harmless small powers. This use of (6) requires the s coefficients to remain common smooth/ray coefficients, not arbitrary divisor coefficients.

Here is the summation form used below. Put L=C_*/(Gq_e), S=Y_*/(Gq_eq_f), where f is fixed. On nonempty physical annuli L,S are bounded below by a fixed positive constant. Then
\[
 \sum_e q_e^{-1}(1+VGq_e/C_*)^{1/2}
 B\left(V,\frac{Y_*}{Gq_eq_f}\right)
 \ll V\left(1+\sqrt{\frac{Y_*}{C_*q_f}}\right)
       (1+\log(2+Y_*)).                              \tag{7}
\]
Explicitly, the sum is finite: q_e is at most a fixed constant times min(C_*/G,Y_*/(Gq_f)). The sum only uses these actual nonempty ranges. To prove (7), split at E_0=Y_*/(Gq_fV). Above E_0 the two elementary reciprocal ideal sums are bounded by
sqrt(VY_*/(Gq_f)) sum q_e^{-3/2} and
V sqrt(Y_*/(C_*q_f)) sum q_e^{-1}.
Below E_0 use (6) with A>1. If E_0<1 start at q_e=1; the first contribution is smaller than V. This proves the same bound in every case. Powers and logarithms of the original bounded physical ranges will be absorbed into Z^epsilon below.

### 2. First verify the common coefficients at n=1

Set H'=epsilon v^3(a')^6 and g=(c,rad H'). In the audited first completion, c=g c_1, s=g t, and the Ramanujan factor is exactly phi(g): at every prime of g the exponent of H'/g is at least two. The completed arithmetic coefficient, apart from original smooth weights and fixed constants, is
\[
 \frac{\mu(c)\eta(c)}{q_c}
 \phi(g)\chi_t(H')\overline{\chi_{c_1}(H')}.
\]
Expand the remaining (t,c_1)=1 mask with e|c_1, and the sixth-power mask with f|rad a'. Write c_1=e c_2 and t=e f s_2. All nonzero terms have (e,H')=1. The exact algebra is
\[
 \mu(c)\mu(e)=\mu(g)\mu(c_2),\qquad
 \chi_e(H')\overline{\chi_e(H')}=1.
\]
Consequently the remaining coefficient is
\[
 \underbrace{\mu(g)\eta(g)\phi(g)/q_g}_{\rm row}
 \underbrace{\eta(e)/q_e}_{\rm fixed\ e}
 \underbrace{\mu(c_2)\eta(c_2)/q_{c_2}}_{\rm column}
 \chi_f(\epsilon v^3)\,
 \chi_v(s_2)^3\chi_v(c_2)^3,                          \tag{8}
\]
up to explicitly retained fixed bad-ray factors. The conjugate quadratic symbol equals the same quadratic symbol. In particular eta(e) is not dropped.

The c_2 conditions are: c_2 squarefree, (c_2,e)=1 and (c_2,a')=1. Any coprimality with the part of g dividing v is already enforced by chi_v(c_2)=0; the other part of g divides a' and is covered by the fixed a' mask. The row condition (e,v)=1 is a bounded row mask. The free s_2 sum has only its common smooth weight and fixed ray data: its a' mask was expanded exactly over f. It has no unexpanded divisor-dependent column coefficient.

It follows that g must not be bounded one value at a time. On a dyadic interval q_g about G, its entire sum over g|rad(v a') can be placed in a v-row coefficient of size O_epsilon(q_{va'}^epsilon), once the smooth norm-ratio weights have been Mellin separated. This preserves the large sieve's common column coefficients.

### 3. Actual prime slots also have common coefficients

For n=1, each selected slot prime dividing c=g e c_2 belongs to exactly one of g,e,c_2. Split the finitely many original slots into these three classes. Primes assigned to g are summed as divisors inside the row coefficient, primes assigned to e give a fixed-e scalar, and primes assigned to c_2 form the column coefficient. The latter is divisor-bounded and independent of v. Its reciprocal-column square mass in a norm interval L is O_epsilon(L^{-1+epsilon}), not an absolute count of the whole marking family.

The Gaussian dependence on D is separated on the zero real Mellin line: W_G(q_c/(Tq_D)) uses q_D^{it}, so no unaccounted real power of q_D enters. All original slot weights, including bar eta(D), factor over the fixed slots. Conditions attached to the finite ray groups are handled by a finite partition, not suppressed.

For general physical n=n_0r^2, use the audited square-layer and odd-branch decomposition. Thus h|rad r, j=(h,rad s), k=h/j; nonzero terms have (h,cn_0)=1, j^2|s and (s,k)=1. The exact full-frequency identity H=(r^6/k)L, and then H=r^6H', L=kH', cancels every k phase, leaving q_r^{-2}q_k^{-1}. The two odd branches give n_0|v, (n_0,a')=1 and n_0=EF with E=(c,n_0). Write
\[
 c=E g e c_2,\qquad s=F g j^2 e f s_2.                \tag{9}
\]
The additional positive prefactor is 1/(q_{n_0}q_E). The Ramanujan contribution is still phi(g), and only that g is canceled against the c denominator. The original coefficientwise CRT identity leaves exactly the same primitive chi_v^3 kernel in c_2 and s_2. The two n_0 phases rho^{-2}/rho^{-4} are row coefficients, never characters evaluated at a forced nonunit.

The square-layer divisor j is disjoint from cn_0. At its primes the base completion is therefore the free-s character branch: its original zero extension makes every term with (j,H')!=1 zero. On the surviving terms the fixed j^2 character factor has modulus one and belongs to the row coefficient. This j support is distinct from the forced F primes of n_0, whose nonzero values are supplied by the two special odd branches and are not evaluated as chi_F(H').

All new good-prime masks can be assigned exactly as follows:

- h and e restrictions on c_2, and the a' restriction, are fixed column masks;
- n_0 and the v part of g are handled by chi_v(c_2)'s original zero extension;
- the remaining part of g divides a' and is already excluded by the fixed a' mask;
- the k and a' masks on s are expanded over f|rad(k a'); coefficients meeting v remain zero row coefficients;
- the remaining ray restrictions are handled by a fixed finite partition.

In particular the s_2 sum still has the smooth/ray form required by (6).

For original marking D|cn_0r, assign each chosen prime to the first applicable factor in the ordered list r,n_0,g,e,c_2. For core marking omit r from this list. The r and e divisor selections are fixed scalars, the n_0,g selections belong to the v-row coefficient, and the c_2 selections belong to the common column coefficient. The exclusions imposed by this priority assignment either involve fixed r,e,a' or are already enforced by the quadratic column zero. This keeps the exact marking, including all shared primes. Its scalar and row bounds cost only (q_rq_eq_{H'})^epsilon.

### 4. Uniform Mellin separation and the cancellation of n_0 E

For fixed r,h,j,a', use Gaussian annuli
\[
 q_c q_{n_0}^3\asymp U_l=e^l TP/q_r^6,
\]
and dyadic intervals q_{n_0} about N, q_E about B, q_g about G, q_v about V. Here B is a norm scale, not a character row. The normalized c and s variables lie in fixed compact positive intervals. Separate the joint smooth factors in their logarithmic variables by Fourier/Mellin inversion on real part zero. The original Gaussian, first Fourier transform, slot weights and finite ray splits produce absolutely integrable separation coefficients. Uniform derivative bounds give an envelope
\[
 C_{A,M}(1+|\nu|)^{C_{A,M}}e^{-c l^2}
 \left(1+\frac{X'V^3q_{a'}^6}{U_l}\right)^{-M},       \tag{10}
\]
after absorbing any fixed polynomial in l. All separated powers of n_0,E,g,D have modulus one; bounded ratios of their dyadic norm scales are harmless. The normalized s derivative argument is exactly the already audited one: chain-rule powers of the first Fourier argument are absorbed by its Schwartz decay.

For each separated term the v-row coefficient is divisor-bounded, uniformly in all Mellin frequencies up to polynomial seminorm costs absorbed in (10). It includes the whole sum over n_0,E,g in their current dyadic blocks. Thus (3) is applied to common c_2 coefficients, not separately to a family depending on v.

The two physical column scales are
\[
 L=\frac{U_l}{N^3 B G q_e}=\frac{C_*}{Gq_e},\qquad
 S=\frac{Y'B}{N G q_j^2q_eq_f}=\frac{Y_*}{Gq_eq_f},
\quad C_*=\frac{U_l}{N^3B},\quad Y_*=\frac{Y'B}{Nq_j^2}.
\]
Their outside factor is 1/(NB). Applying (7) gives
\[
 \frac{V}{NB}\left(1+\sqrt{\frac{Y_*}{C_*q_f}}\right)
 =V\left(\frac1{NB}+\frac1{q_j}\sqrt{\frac{Y'}{U_lq_f}}\right).
                                                               \tag{11}
\]
This exact cancellation is why the physical odd branches can be included without degrading the new estimate. The number of N,B,G blocks and the f choices costs arbitrarily small divisor powers; summing the first term's 1/(NB) over dyadic N,B is bounded. All actual masks and signs were retained before applying positive norm inequalities.

### 5. Fourier tails, square layers and a useful uniform scale bound

Weighted dyadic V summation in (10), then summation over a', gives the factor
\[
 \mathcal P_M(K)=\begin{cases}K^{1/3},&K\ge1,\\K^M,&0<K\le1,\end{cases}
 \qquad K=U_l/X',                                    \tag{12}
\]
with any fixed sufficiently large M, up to arbitrarily small powers. For K>=1 the a' sum is bounded by K^{1/3} sum_{a'}q_{a'}^{-2}; for K<=1 retain the arbitrarily high original Fourier decay. This is a bound on the full frequency tail, not a sharp cutoff.

Combining (10)--(12), the contribution for fixed r,h,j before Gaussian summation is bounded by the common Q/Y'^{3/2}, the exact q_r^{-2}q_k^{-1}, and
\[
 e^{-c l^2}\mathcal P_M(U_l/X')
       (1+\sqrt{Y'/U_l}),                            \tag{13}
\]
with small divisor powers. The h,j count is at most 3^{omega(r)}. If U_l/X'>=1, the first term in (13) gives q_r^{-4}, which is summable. Its second term gives q_r^{-1}, but only until q_r^6<=e^l TP/X'; this is a logarithmic ideal sum. Beyond that point use the second line of (12); for M>1 the remaining r sums converge, including the apparent square-root factor U_l^{-1/2}. Small divisor powers and all logarithms are absorbed into Z^epsilon, since T<=Z. Gaussian summation also covers every negative or positive l tail.

Consequently, if K_0=TP/X', the following uniform bound holds for any fixed M>1, after possibly increasing derivative orders:
\[
 |S_{\rm quad}(T)|\ll_{\epsilon,M}
 (1+|\nu|)^{C_{\epsilon,M}}Z^\epsilon\frac{Q}{Y'^{3/2}}
 \begin{cases}
 K_0^{1/3}(1+\sqrt{Y'/(TP)}),&K_0\ge1,\\
 K_0^M(1+\sqrt{Y'/(TP)}),&0<K_0\le1.
 \end{cases}                                         \tag{14}
\]
When K_0 is small, the Gaussian annuli for which e^lK_0>=1 are absorbed by their Gaussian tail; this yields any prescribed fixed power K_0^M. Thus (14) does not assume a coupled-scale theorem at a different T.

At T=Z, one has ZP>>Y', K_0=Z^{13/16} up to fixed constants, and
\[
 \frac{Q}{Y'^{3/2}}K_0^{1/3}
 \asymp Z^{11/96-d/2+13/48}=Z^{37/96-d/2}.
\]
This proves (1).

### 6. Exact decompletion and normalization

The core-marked Möbius operation sums T=Z/q_d^6 with coefficient mu(d)kappa(d)/q_d^2 and keeps all physical slots, X',Y' fixed. It preserves the numerator core because its redundant-modulus lift multiplies the frequency by d^6. Apply the uniform bound (14).

For q_d<=K_0^{1/6}, its first term has d^{-4} and is absolutely summable. The second term has d^{-1}; its truncated sum is logarithmic and its outside size relative to the main term is sqrt(Y'/(ZP))<<1. For q_d>K_0^{1/6}, the small-K line gives convergent powers d^{-2-6M} and d^{1-6M}. Their tail is bounded by the same main term, for M>1. This proves (1) for the exact core-flat sector, without assuming convergence of an unproved negative low exponent.

The identical argument also applies to the original-marked flat operation: (14) holds for that original completed marker with the same fixed X',Y' and slots. This is precisely the original-marked transform in the user's commit 56c6cf64, `MARKED_ROW_REFLECTION.md` §7, not a substitution of the core marker for it. Its pointwise reflection estimate is the user's separate result; no part of that new estimate is needed in this bilinear proof.

Finally Q^{-1/2} gives -1/32+d/2. The original rescaling coefficient and tuple count remove d/2, giving (2). The original Mellin weight absorbs every polynomial in nu.

### Dependencies and remaining burden

The exact arithmetic is inherited from the audited complete-quadratic-sector proof and the source coefficientwise local table, not from a new formal spectral equivalence. The only new analytic input is the fixed-ray Goldmakher--Louvel quadratic sieve, already stated and verified for the genuine characters in the original source, plus ordinary primitive smooth Poisson. The separate analytic lemma and this complete arithmetic interface have both passed independent review.

The proof must be read with its exact common-coefficient interface: moving masks are not deleted from mixed products, and the s sum is not replaced by arbitrary coefficients before (6). The result treats a complete nonprincipal quadratic kernel type. It leaves all other types and the stronger complete-probe correlation unresolved.

# Part VI. The complete cubic good-core sector with all physical indices

## The complete cubic dual sector with all physical indices

### Result and exact scope

Use the user's original R4 linear pairing, fixed finite prime slots, ray class sigma, rescaling J and Mellin parameter nu. Write
\[
 X'\asymp Z^{17/48-d},\quad Y'\asymp Z^{23/48-d},\quad
 q_D\asymp P=Z^{1/6-d},\quad Q=q_bX'Y',\quad0\le d\le1/6.
\]
All good ideals and their primary generators use the original conventions. For 0<T<=Z, replace only the Gaussian scale Z by T, retaining X',Y', the actual Gauss factors, auxiliary characters, slots and their weights.

In the exact first m-Poisson formula with the original full modulus bscn^3, select all frequencies
\[
 H=\epsilon w^2a^6,\qquad w\ne1\ \text{cube-free},\qquad
 a\ \text{arbitrary good},                            \tag{1}
\]
where epsilon ranges over the original units. The representation is unique: w=v_1v_2^2 with v_1,v_2 squarefree and coprime. No coprimality between w and a is imposed. Thus (1) is the entire nonprincipal cubic good-core sector, including both exponents 2 and 4 and all physical indices n. It excludes the principal/unit-core and genuine sextic types.

Two markers are covered: the original D|cn, and the changed core marker D|c n_0 where n=n_0r^2, n_0 squarefree. Let S_cub(T) be the corresponding selected contribution to the actual linear pairing.

**Theorem.** For either marker, with K=TP/X',
\[
 \begin{split}
 |S_{\rm cub}(T)|\ll_\varepsilon &(1+|\nu|)^{C_\varepsilon}
 Z^\varepsilon\frac{Q}{Y'^{3/2}}\left[
 K^{1/2}+\left(\frac{Y'}{TP}\right)^{1/2}K^{11/20}
 +\left(\frac{Y'}{TP}\right)^{1/6}K^{3/5}\right],
 \qquad0<T\le Z.                                    \tag{2}
 \end{split}
\]
The exact original-marked and core-marked Möbius-decompleted probes satisfy the same bound at T=Z. In particular,
\[
 |S_{\rm cub}(Z)|\ll_\varepsilon(1+|\nu|)^{C_\varepsilon}
 Z^{25/48-d/2+\varepsilon}.                          \tag{3}
\]
After Q^{-1/2} and the original finite signed compensation, this complete sector contributes O_epsilon(Z^{5/48+epsilon}). This remains 7/24 above the desired complete-probe low exponent -3/16. In particular this covers the n=1,H=v^2 subcase within the complete core type; it does not establish R4.

### 1. The analytic lemma uses the norm of a cube-free index

Define psi_w(t)=chi_t(w^2), with all original zero values. After a fixed finite ray partition, this is precisely the cubic reciprocity family, possibly conjugated and multiplied by fixed ray characters. Its good primitive conductor is rad(w), not w. The row parameter below is nevertheless
\[
 M\le q_w\le2M,\qquad M\ge1.                         \tag{4}
\]
We never substitute q_rad(w) for q_w in a large-sieve parameter.

The cube-free version of [de Faveri, Theorem 1.1, n=3](https://arxiv.org/html/2610.04045v1) gives
\[
 \sum_{w\ \mathrm{cube\!\!\!-free},\ q_w\ll M}
 \left|\sum_{c\ \mathrm{cube\!\!\!-free},\ q_c\ll L}
 b_c\psi_w(c)\right|^2
 \ll_\varepsilon(ML)^\varepsilon
 [M+L+(ML)^{2/3}]\sum_c|b_c|^2.                     \tag{5}
\]
Here the field contains the third roots of unity. The original reciprocal c columns are squarefree, hence allowed in (5). If b_c is divisor-bounded times q_c^{-1}, with fixed column masks and common coefficients, its row norm is
\[
 \ll(ML)^\varepsilon
 [1+(M/L)^{1/2}+M^{1/3}L^{-1/6}].                  \tag{6}
\]

The second column has actual common smooth/ray coefficients over *all* ideals t. Decompose t=t_0 ell^3, t_0 cube-free, use (5), then Minkowski. The three ell sums have powers -3/2,-3,-5/2, all convergent. The induced (w,ell)=1 restriction is deleted only inside the positive row norm. Therefore
\[
 B_3(M,S):=\left\|\sum_t\psi_w(t)F(t/\sqrt S)\right\|_{\ell^2(w)}
 \ll_\varepsilon(MS)^\varepsilon
 [\sqrt{MS}+S+M^{1/3}S^{5/6}].                      \tag{7}
\]
For the original primary/ray decomposition, F is a common compactly supported smooth function on a fixed normalized annulus; its fixed-order seminorms enter the constant.

There is also a genuine smooth Poisson bound. If c_w is the primitive conductor norm, c_w<=C M and c_w is supported on rad(w) and fixed bad primes. Nonprincipality gives no zero Fourier term. Each row is O(sqrt(c_w)) at all scales and, for S>=C M,
\[
 O_A\left(\frac S{\sqrt{c_w}}(S/c_w)^{-A}\right)
 \ll_A\frac S{\sqrt M}(S/M)^{-A},\qquad A>1/2.
\]
The last inequality uses c_w<=C M with fixed constants. There are O(M) rows. Enlarging constants on S comparable to M gives
\[
 B_3(M,S)\ll_\varepsilon(MS)^\varepsilon
 \begin{cases}
 \min\{M,\sqrt{MS}+M^{1/3}S^{5/6}\},&S\le M,\\
 S(S/M)^{-A},&S\ge M.
 \end{cases}                                       \tag{8}
\]
This argument is valid for mixed w=v_1v_2^2 despite its smaller primitive conductor. It would not be valid to treat an arbitrary s-dependent coefficient as F.

For positive physical scales C_*,Y_*,G, put Y_f=Y_*/q_f and
L=C_*/(Gq_e), S=Y_f/(Gq_e). The e sum is finite, restricted by the actual nonempty c and s annuli. Equations (6)--(8) imply
\[
 \begin{split}
 &\sum_e\frac1{q_e}
 [1+(MGq_e/C_*)^{1/2}+M^{1/3}(Gq_e/C_*)^{1/6}]
 B_3(M,Y_f/(Gq_e))\\
 &\qquad\ll Z^\varepsilon\left[
 M+M^{11/10}(Y_f/C_*)^{1/2}
   +M^{6/5}(Y_f/C_*)^{1/6}\right].                  \tag{9}
 \end{split}
\]
The small power here stands for logarithms and small powers of the bounded physical ranges and row size; later all unbounded Fourier ranges retain their decay.

For completeness split at E_0=Y_f/(GM), E_1=Y_f/(GM^{4/5}). For q_e<=E_0 use the arbitrary long-column decay; for E_0<q_e<=E_1 use B_3<=M; thereafter use sqrt(MS)+M^{1/3}S^{5/6}. Reciprocal ideal summation gives exactly the three displayed powers, with only logarithms at exponent -1. If E_0 or E_1 is below one, the corresponding physical interval is empty or starts at one; the same majorant holds. Importantly (9) does not assume C_*>=Y_f. This unabsorbed middle term is needed for all n.

### 2. The physical square layer, with its true frequency lift

Write n=n_0r^2, n_0 squarefree. The original arithmetic coefficients satisfy
\[
 b(c,n_0r^2;s)=b(c,n_0;s)\kappa(r),\qquad
 \chi_{cn_0^3r^6}(m)=\chi_{cn_0^3}(m)1_{(r,m)=1},
 \quad\kappa(r)=\eta(r)^6\overline{\alpha(r)}^6.
                                                               \tag{10}
\]
No coprimality of c,n_0,r is assumed. Expand the last mask over h|rad(r), h|m. Terms with (h,cn_0)!=1 remain zero. Put j=(h,rad s), k=h/j. The original prime-power Gauss formula forces
\[
 j^2\mid s,\qquad(s,k)=1,\qquad(h,cn_0)=1.           \tag{11}
\]
At a prime dividing j, exponent one in s vanishes; at exponents at least two its Gauss sum already forces p|m. Thus only k|m remains to be imposed explicitly.

Set m=km'. Its unit multiplier is exactly
xi(k) chi_{cn_0^3}(k) overline{chi_s(k)}. For the base modulus bscn_0^3, write L for the frequency. Relative to the original full modulus the frequency is H=(r^6/k)L. At p^b||r this gives v_p(H)>=6b-1. Since a frequency in (1) has exponent 0,2 or4 modulo six, it follows that v_p(H)>=6b. Therefore r divides a, and
\[
 H=r^6H',\quad H'=\epsilon w^2(a')^6,\quad L=kH'.    \tag{12}
\]
The finite Fourier coefficient's unit covariance cancels the entire displayed k multiplier when L=kH' is substituted. The Fourier argument becomes sqrt(Q)H'/(bscn_0^3). The additional positive factor is exactly
\[
 q_r^{-2}q_k^{-1},                                  \tag{13}
\]
and the Gaussian scale becomes T/q_r^6. This coefficientwise derivation retains the original unit and cubic core, not just an isomorphic family.

### 3. Both odd n_0 branches from the original local C table

Write w=v_1v_2^2 as above. At p|n_0, l=v_p(n)=1 after (10). The source scalar table C_p(t,k_s,j'), t=e_0+3l, has precisely these nonzero cubic choices:

- j'=2, (e_0,k_s)=(0,0): C=P^2 G_3 has magnitude P^{5/2};
- j'=4, (e_0,k_s)=(1,1): C=omega_p^{-1}G_1 P^3G_3 has magnitude P^4.

No j'=2+6m or4+6m with m>0 survives. Consequently
\[
 n_0=F_2E_4,\quad F_2\mid v_1,\quad E_4\mid v_2,
 \quad(n_0,a')=1.                                   \tag{14}
\]
The two completed local magnitudes, including the original n_0 weight, are P^{-3/2} and P^{-2}, respectively. For the first divide C by P^3 then multiply n_0^{-1}; for the second divide by P^4 and include s^{-1/2}c^{-1/2}n_0^{-1}. Relative to the common Q/(sqrt(q_b) sqrt(q_s) q_c) normalization the residual factors are
F_2^{-3/2}E_4^{-1/2}. Both c and s contain E_4 once; neither contains F_2.

All CRT and ray cancellation is coefficientwise in the original local-P formula. The remaining n_0 phase is rho^{-3} times fixed prime phases, where rho=chi_p(epsilon(w/p^{v_p(w)})^2). Thus rho^{-3}=chi_p(epsilon)^{-3}; its moving good core cancels as a sixth power. These phases are retained in the row coefficient. In particular no character is evaluated at a forced nonunit to stand in for an odd-branch Gauss value.

At other primes the audited n=1 completion applies. Put
\[
 c=E_4 g c_1,\qquad s=E_4 g j^2t,\qquad
 g\mid\operatorname{rad}(w a'),\quad(g,n_0h)=1.       \tag{15}
\]
The shared g has exactly the Ramanujan factor phi(g): every exponent of H'/g is positive. E_4 has no Ramanujan factor. The free variables c_1 and t have the cubic characters overline{psi_w(c_1)} and psi_w(t), with fixed ray/unit factors retained. At primes of j the base completion is the free-s branch and forces (j,H')=1; j is disjoint from n_0. This is distinct from the forced E_4 branch.

Pulling E_4^{-1} from q_c gives the decisive residual prefactor
\[
 q_{F_2}^{-3/2}q_{E_4}^{-3/2}=q_{n_0}^{-3/2}.        \tag{16}
\]
The original phases from the two local branches are unit-modulus row coefficients, not assumptions of positivity.

### 4. Common columns, shared divisors and real marking

Expand (c_1,t)=1 over e|c_1,t, and the remaining k,a' mask on t over f|rad(k a'). Write
\[
 c_1=e c_2,\qquad t=e f s_2.                         \tag{17}
\]
On every nonzero term, (e,H')=1. The actual algebra is
\[
 \mu(c_1)\mu(e)=\mu(c_2),\qquad
 \psi_w(e)\overline{\psi_w(e)}=1.
\]
After expressing q_s^{-1} as Y'^{-1} times a common smooth annular factor, the outside normalization is Q/Y'^{3/2}. Apart from fixed phases and (16), the coefficient is
\[
 \underbrace{\mu(g)\eta(g)\phi(g)/q_g}_{\text{row}}
 \underbrace{\eta(e)/q_e}_{\text{fixed }e}
 \underbrace{\mu(c_2)\eta(c_2)/q_{c_2}}_{\text{common column}}
 \psi_w(f)\,\psi_w(s_2)\overline{\psi_w(c_2)}.        \tag{18}
\]
The local n_0 unit phases from §3 are additionally retained in the row. The following allocation keeps every mask:

- c_2 is squarefree, with fixed restrictions from e,h,a';
- its restrictions at n_0 and the w part of g follow from psi_w(c_2)'s zero extension;
- the remaining part of g divides a', already a fixed column mask;
- f expands the k,a' mask on s; if it meets w, its row is zero;
- (e,w)=1, all n_0 restrictions (14), and j support belong to the row;
- residual original bad-ray restrictions are split into finitely many common ray characters.

Thus s_2 still has only common smooth/ray coefficients. In particular it has not inherited an arbitrary w-dependent divisor coefficient before use of (8).

For original marking assign each chosen prime in D|c n_0 r to its first applicable factor in the ordered list r,n_0,g,e,c_2. For core marking omit r. The r,e assignments are fixed scalars; n_0,g assignments are divisor sums inside the w-row; c_2 assignments are part of the common column. Priority exclusions are either fixed masks or enforced by the cubic zero extension. All original slot weights, including overline{eta(D)}, remain. On fixed physical annuli the reciprocal c_2 column square mass is O_epsilon(Z^epsilon L^{-1}).

The Gaussian's D dependence is separated on real Mellin part zero. Hence q_D^{it} has modulus one, and no hidden positive marking power is introduced. The sums over n_0,E_4,g in their dyadic blocks are pooled *inside* the row coefficient. Their number is divisor-bounded in w,a', while their unit phases are allowed there. Applying the large sieve separately for each moving divisor and then treating that count as constant would not establish this interface.

### 5. All n_0 scales in the e-sum

For fixed r,h,j,a', use Gaussian annuli
\[
 q_c q_{n_0}^3\asymp U_l=e^l TP/q_r^6.
\]
In dyadic blocks q_{n_0} about N, q_{E_4} about B, q_g about G, and q_w about M, the actual two column scales are
\[
 L=\frac{U_l}{N^3BGq_e}=\frac{C_*}{Gq_e},\qquad
 S=\frac{Y'}{BGq_j^2q_eq_f}=\frac{Y_*}{Gq_eq_f},
 \quad C_*=\frac{U_l}{N^3B},\quad Y_*=\frac{Y'}{Bq_j^2}.
                                                               \tag{19}
\]
The original weights separate into an absolutely integrable common Mellin kernel in the normalized log variables. Fixed derivative orders give the envelope
\[
 C_{A,N}(1+|\nu|)^{C_{A,N}} e^{-c l^2}
 (1+X'M^2q_{a'}^6/U_l)^{-A}.                        \tag{20}
\]
This follows from the Gaussian and original Fourier Schwartz bounds; chain-rule factors in the first Fourier argument are absorbed by increasing A. All separated n_0,E_4,g,D powers have real part zero. Nonempty physical ranges suffice; no spurious terms are introduced at scales below one.

Multiply (9) by N^{-3/2} from (16). Since
Y_*/(C_*q_f)=Y'N^3/(U_l q_j^2q_f), its three terms become
\[
 \frac M{N^{3/2}}
 +M^{11/10}\left(\frac{Y'}{U_lq_j^2q_f}\right)^{1/2}
 +\frac{M^{6/5}}{N}\left(\frac{Y'}{U_lq_j^2q_f}\right)^{1/6}.
                                                               \tag{21}
\]
The middle cancellation is exact, and requires keeping that term in (9). Sum the dyadic N,B,G ranges after the common-coefficient estimate. The first and third N weights are summable; the middle has only a logarithmic number of ranges. B<=N and every n_0,E_4,g choice is already divisor-bounded inside its row. The remaining f choices and j factors cost only divisor-small powers; the positive j,f denominators can be bounded by one. Thus (21), with (20), is bounded by the same expression with N=j=q_f=1, times harmless small powers.

### 6. Complete frequency and square-layer sums

For any alpha>0 and sufficiently large A, weighted dyadic M summation and then all a' give
\[
 \sum_{a'}\sum_{M\ \mathrm{dyadic}} M^\alpha
 (1+M^2q_{a'}^6/K_l)^{-A}
 \ll_\alpha K_l^{\alpha/2},\qquad K_l=U_l/X',        \tag{22}
\]
for alpha=1,11/10,6/5. For K_l>=1 the a' powers are respectively -3,-33/10,-18/5, all summable. For K_l<=1, take A sufficiently large; the original Fourier tail gives any prescribed power before bounding it by the displayed positive power. Arbitrarily small divisor powers are absorbed by increasing A and an overall Z^epsilon. There is no sharp Fourier cutoff.

Using (13), the per-r,h,j,l bound is therefore Q/Y'^{3/2} times
\[
 \frac{e^{-cl^2}}{q_r^2q_k}\left[
 (U_l/X')^{1/2}
 +(Y'/U_l)^{1/2}(U_l/X')^{11/20}
 +(Y'/U_l)^{1/6}(U_l/X')^{3/5}\right],               \tag{23}
\]
with the stated seminorm and small-power costs. Under U_l=e^l TP/q_r^6, the three r powers in (23) are
\[
 q_r^{-5},\qquad q_r^{-23/10},\qquad q_r^{-23/5}.     \tag{24}
\]
All are absolutely summable over ideals, even after the h,j count at most 3^{omega(r)} and small powers. The Gaussian sums over all l also converge. This proves (2) for both exact markings, including every physical n.

At T=Z the central K is Z^{13/16}, and Y'/(ZP)=Z^{-11/16}. Relative to the first term in (2), the second and third terms are respectively
\[
 Z^{-97/320},\qquad Z^{-1/30}.                       \tag{25}
\]
Since Q/Y'^{3/2}=Z^{11/96-d/2} up to fixed constants, (3) follows.

### 7. Exact decompletion and original finite compensation

The first Möbius-decompleted operation is the actual sum over d_0 of the completed row at T=Z/q_{d_0}^6, with coefficient mu(d_0)kappa(d_0)/q_{d_0}^2. Its full-modulus lift multiplies H by d_0^6 and preserves (1), including its unit. Hence the selected sector commutes with this operation coefficientwise in the original absolute regime.

Apply (2) at every positive T=Z/q_{d_0}^6. Its three d_0 weights are again exactly -5,-23/10,-23/5. Their sums converge absolutely, which justifies the completed sector sum as well. This works for the original marker and the core marker separately; it does not infer a bound on one oscillatory probe from another. It also avoids assuming transfer of an unproved negative low exponent.

Finally Q^{-1/2} changes the exponent in (3) to 5/48+d/2. The original q_rho^{-3/2} finite compensation coefficient and its Z^d tuple count remove this d/2, giving 5/48. Here rho is the original rescaling product, distinct from the physical square variable r. The original Mellin weight absorbs all polynomial dependence on nu.

### Dependencies and precise remaining problem

The arithmetic identities come from the [fixed QRH source fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), particularly its full m-Poisson formula, local C table, coefficientwise pair-phase cancellation and local-P formula. The square-layer unit covariance and common-slot organization are also explicitly established in Parts III and V of this report, but the cubic odd branches and row family have been checked separately here. The external analytic input is the cube-free cubic sieve (5) and ordinary primitive smooth Poisson.

This is a bound for a complete nonprincipal cubic core type in the actual low probe. It requires no all-u root-number theorem, no RH input, and no unproved moving-numerator R2 estimate. Its exponent is positive after normalization and remains insufficient for R4. The principal/unit-core, generic sextic types and the additional cancellation required inside the complete signed pairing remain open.

# Part VII. Conditional density bounds for genuine Möbius columns

## True Möbius columns in a quadratic Hecke family

This note concerns the actual Möbius column left by the audited quadratic
Poisson calculation. It gives an average estimate, rather than replacing
that column by arbitrary large-sieve coefficients. The application uses
the user's input Q (the fixed zero-free half-plane to the right of 7/8).
No estimate here covers the other cubic, sextic or principal dual types.
The complete physical divisor/slot summation is not asserted below.

### 1. Family, inputs, and precise claim

Let \(K=\mathbb Q(\sqrt{-3})\), and write \(q_a=Na\).
Fix a finite excluded set and a finite-order Hecke character \(\eta\).
For squarefree good ideals \(v\), let \(\psi_v=\chi_v^3\) be the
quadratic Hecke family in the original primary convention. After a fixed
finite ray partition the primitive character inducing
\(\eta\psi_v\) has conductor norm comparable to \(q_v\). Finite exceptional
principal twists are separated. Constants may depend on this fixed data.
All moving \(v\) below satisfy \(V\le q_v\le2V\), \(V\ge2\).

We use the following already established inputs:

* Goldmakher--Louvel, Theorem 1.1, for the squarefree quadratic family,
  with both indices squarefree. The fixed \(\eta\) factor is a common
  column coefficient.
* The usual functional equation and approximate functional equation for
  primitive Hecke \(L\)-functions over this fixed field.
* Q: every finite-order Hecke \(L\)-function over this field is zero-free
  for \(\Re s>7/8\). This is the precise user-supplied input recorded in
  [the user's FORMAL_INPUT_Q](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/52ee48d3e2e4c5b0beeb3e4880eca86fb2208ce1/reports/20261011_qrh_selection_bridge/FORMAL_INPUT_Q.md). The formal build reported there is the user's contribution; the present proof uses Q as an explicit input and does not claim an independent rerun of that build.

For a fixed smooth annular function \(W\), an ideal \(M\), and a real
Mellin parameter \(t_0\), define the genuine column
\[
 A_v(L;M,t_0)=
 \sum_{(c,M)=1}\frac{\mu(c)\eta(c)\psi_v(c)}{q_c^{1+it_0}}
 W(q_c/L).                                                     \tag{1}
\]
Here \(c\) always ranges over the original good ideals, avoiding the
fixed excluded set \(S\). Replace \(M\) by its \(S\)-free part without
loss. Every Euler product caused by the coprimality mask below runs
only over \(p\mid M,\ p\notin S\); the fixed \(S\)-Euler factors of the
primitive \(L\)-function are kept separately.
Its coefficients are not arbitrary divisor-bounded coefficients.
Let an ambient parameter \(\mathfrak X\ge2\) bound \(V,L,q_M\) by fixed
powers. Dependence on \(t_0\) and on a fixed number of smooth seminorms
will always be polynomial.

**Proposition.** Subject to Q, for every \(\epsilon>0\),
\[
 \sum_{v\asymp V}|A_v(L;M,t_0)|
 \ll_\epsilon \mathfrak X^\epsilon(1+|t_0|)^{C_\epsilon}
 V^{1/3}L^{-1/8},
 \qquad L\ge V^{64/27}.                                        \tag{2}
\]
The corresponding second-moment consequence is
\[
 \left(\sum_{v\asymp V}|A_v(L;M,t_0)|^2\right)^{1/2}
 \ll_\epsilon \mathfrak X^\epsilon(1+|t_0|)^{C_\epsilon}
 V^{1/6}L^{-1/8},
 \qquad L\ge V^{32/27}.                                        \tag{3}
\]
These estimates allow arbitrary restrictions of the positive row sums
and row weights of size \(\mathfrak X^\epsilon\). They do not allow
arbitrary extra coefficients inside (1).

The endpoint powers in (2)--(3) include the displayed arbitrarily small
loss. No contour is shifted onto a possible zero with real part 7/8.

### 2. The quadratic fourth moment needed for detection

For a fixed finite-order twist, uniformly for \(T\ge2\),
\[
 \sum_{v\asymp V}\sup_{|t|\le T}
 |L(1/2+it,\eta\psi_v)|^4
 \ll_\epsilon V^{1+\epsilon}(1+T)^{C_\epsilon}.                  \tag{4}
\]
For the height supremum it is enough to bound \(L(s)^2\) and
\(\partial_s(L(s)^2)\) in the row \(L^2\) norm; those are the
derivatives used below, rather than an additional assertion about
the fourth moment of \(L'(s)\).

Here is a direct verification of the conductor exponent in (4).
Apply an approximate functional equation to \(L(s,\eta\psi_v)^2\).
Its analytic conductor is \(O(V^2(1+T)^C)\), so the two Dirichlet
polynomials have norm length
\(B\ll V(1+T)^C\). Their coefficients are
\(\eta(n)\tau(n)q_n^{-1/2-it}\), with common smooth weights after
Mellin separation of the conductors. The root number is a bounded row
factor. Write \(n=b\ell^2\), \(b\) squarefree. The factor
\(\psi_v(\ell^2)=1_{(v,\ell)=1}\) is a restriction of the positive row
sum, and the coefficient has the additional factor \(q_\ell^{-1}\).
Goldmakher--Louvel and Minkowski therefore bound the row norm of each
polynomial by
\[
 (VB)^\epsilon
 \sum_{q_\ell\ll\sqrt B}q_\ell^{-1}
       \sqrt{V+B/q_\ell^2}
 \ll (VB)^\epsilon(\sqrt V+\sqrt B).                             \tag{5}
\]
Squarefree-column squared masses are logarithmic up to divisor powers.
The tails of the approximate functional equation are treated by its
rapid decay. This proves the fixed-height version of (4).
Differentiating the approximate functional equation for \(L(s)^2\)
inserts only logarithms and derivatives of common weights, and gives
the same row \(L^2\) bound for \(\partial_s(L(s)^2)\).
The elementary one-dimensional Sobolev inequality on \([-T-1,T+1]\),
followed by integration of these fixed-height moment bounds, proves (4).
This also justifies taking different heights for different rows.

For the truncated inverse polynomial
\[
 M_X(s,v)=\sum_{q_b\le X}\mu(b)\eta(b)\psi_v(b)q_b^{-s},
\]
the same sieve, with its already squarefree support, gives
\[
 \sum_{v\asymp V}\sup_{|t|\le T}|M_X(1/2+it,v)|^2
 \ll_\epsilon (VX)^\epsilon(V+X)(1+T)^{C_\epsilon}.              \tag{6}
\]

### 3. A zero-density bound, with its exact proof ingredients

Let \(\mathcal E(\sigma,T)\) be the rows for which the actual primitive
\(L(s,\eta\psi_v)\) has a zero with
\(\Re\rho\ge\sigma,\ |\Im\rho|\le T\).
For fixed \(1/2<\sigma<1\), we claim
\[
 |\mathcal E(\sigma,T)|
 \ll_\epsilon (VT)^\epsilon (1+T)^{C_\epsilon}
 V^{d(\sigma)},\qquad
 d(\sigma)=\frac{3(1-\sigma)}{2-\sigma}.                         \tag{7}
\]
Uniformity holds when \(\sigma\) ranges over a fixed compact subset of
\((1/2,1)\). Counting rows, rather than all their zeros, suffices.

For completeness, use the detector in the proof of BGL Corollary 1.6,
Section 5, retaining the restricted row set in its first term.
Choose one qualifying zero for each row, put \(R=|\mathcal E|\), and
take \(1<X<Y\). Mellin inversion with \(\Gamma(w)Y^w\) applied to
\(L(\rho+w,\eta\psi_v)M_X(\rho+w,v)\) gives a constant term of size
one, a polynomial tail over \(q_b>X\), and an integral on
\(\Re(\rho+w)=1/2\). The residue at \(w=0\) vanishes because
\(L(\rho,\eta\psi_v)=0\).
Dyadic decomposition and partial summation handle the varying real
parts of the zeros; Sobolev handles their varying imaginary parts.
The first integral has its full Gamma weight: heights outside a fixed
neighborhood of the selected zero are not discarded. Equations
(4)--(6), used on successive height intervals with their polynomial
height growth, are summable against the exponential Gamma decay.
Thus the displayed polynomial \(T\)-factor also bounds that full
integral; it is not an unproved hard truncation of it at \(T+1\).
Thus, with logarithms absorbed in small powers,
\[
\begin{split}
 R\ll (VXYT)^\epsilon(1+T)^C\bigg[
 &Y^{1/2-\sigma}
   R^{1/4}V^{1/4}(V+X)^{1/2}\\
 &+\sup_{X\le U\le Y^{1+\epsilon}}
 U^{-2\sigma}
 \sum_{v\asymp V}\sup_{|t|\le T+1}
 \left|\sum_{U\le q_b\le2U}a_b\eta(b)\psi_v(b)q_b^{-it}\right|^2
 \bigg].                                                       \tag{8}
\end{split}
\]
Here \(a_b=\sum_{d\mid b,\ q_d\le X}\mu(d)\), or its bounded smooth
dyadic version, so \(a_b\ll_\epsilon q_b^\epsilon\), independently
of \(v\). The first line is precisely Hölder with exponents
\(4,2,4\), using (4), (6), and \(R\) rows. This is the improvement
over discarding the restricted row set at the start.

In the second line write \(b=b_0\ell^2\), \(b_0\) squarefree, while
keeping \(a_{b_0\ell^2}\) as a common column coefficient. For each
\(\ell\), the row restriction \((v,\ell)=1\) can be enlarged in a
positive norm. The norm is bounded by
\[
 (VU)^\epsilon
 \sum_{q_\ell\ll\sqrt U}
 \sqrt{(V+U/q_\ell^2)U/q_\ell^2}
 \ll (VU)^\epsilon(\sqrt{VU}+U).
                                                                    \tag{9}
\]
The same bound with polynomial \(T\)-loss holds for the supremum.
Thus the second line of (8) costs
\[
 VX^{1-2\sigma}+Y^{2-2\sigma},
                                                                    \tag{10}
\]
up to small powers. The harmless \(Y^\epsilon\) enlargement is
absorbed by choosing the initial losses smaller.

Take \(X=V\) and \(Y=V^{3/(4-2\sigma)}\), slightly enlarged if necessary.
If the first term in (8) dominates \(R\), divide by \(R^{1/4}\);
it gives
\[
 R\ll (VT)^\epsilon(1+T)^C
 VY^{(2-4\sigma)/3}= (VT)^\epsilon(1+T)^C V^{d(\sigma)}.
                                                                    \tag{11}
\]
The \(Y^{2-2\sigma}\) term has the same exponent, while
\(V^{2-2\sigma}\le V^{d(\sigma)}\) for \(\sigma\ge1/2\).
This proves (7). All finite-order twists remain fixed common
coefficients, so no statement about a different family is imported.

### 4. Finite-height zero-free boxes really do control the inverse

Fix a small \(h>0\), and let \(b\in[1/2+h,7/8]\).
Suppose a particular nonprincipal row has no zero in
\[
 \Re s>b,\qquad |\Im s|\le4T,
                                                                    \tag{12}
\]
where \(T\) is a sufficiently large small power of \(\mathfrak X\),
times a sufficiently large fixed power of \(3+|t_0|\); in particular
choose \(T\ge4(1+|t_0|)\).
Then for \(b+h\le\Re s\le2,\ |\Im s|\le T\),
\[
 L(s,\eta\psi_v)^{-1}
 \ll_{h,\epsilon}\mathfrak X^\epsilon(1+|t_0|)^{C_{h,\epsilon}}.
                                                                    \tag{13}
\]
The parameters in this assertion are chosen in the order: desired
loss, fixed \(h\), then the sufficiently small power defining \(T\).

Here are the boundary details. In the zero-free rectangle use the
analytic logarithm agreeing with the Euler logarithm on the right.
Polynomial conductor-height bounds for \(L\), together with
Borel--Carathéodory on discs centered at \(2+it\), give
\[
 |\log L(s)|\ll_h\log(V(4T+3))
 \quad(\Re s\ge b+h/4,\ |\Im s|\le2T).
                                                                    \tag{14}
\]
These discs stay a positive distance from the left and horizontal
boundaries of (12). On \(\Re s=1+h/4\), the Euler series gives
\(|\log L(s)|\ll_h1\).
Apply the two-constants theorem to the subharmonic function
\(\log|\log L(s)|\) in this rectangle, using its limiting value at
zeros of the analytic logarithm. For \(|\Im s|\le T\), the harmonic
measure of the horizontal sides is \(O_h(e^{-c_hT})\).
At \(\Re s\ge b+h\) the weight of the left side is bounded by
\(1-c_h\). Therefore
\[
 |\log L(s)|\ll_h
 \{\log(V(4T+3))\}^{1-c'_h}.                                    \tag{15}
\]
For the chosen polynomially growing \(T\), this implies (13).
Bounded values of \(\mathfrak X\) are absorbed in the constant.
This argument needs the height buffer in (12); zero freedom only
on the integration segment would not suffice.

The Euler factors deleted by \((c,M)=1\) contribute
\[
 \prod_{p\mid M}(1-\eta(p)\psi_v(p)q_p^{-s})^{-1}
 \ll_{h,\epsilon}q_M^\epsilon
 \quad(\Re s\ge1/2+h).                                         \tag{16}
\]
To see this, bound logarithms by \(O_h(q_p^{-1/2-h})\), and split
at a sufficiently large fixed prime norm so that each remaining
term is at most \(\epsilon\log q_p\).

Mellin inversion of (1), truncated at imaginary heights \(\pm T/2\),
now shifts that contour from
\(\Re s>0\) to \(\Re s=b+h-1\). Formula (13) applies to
\(1+s+it_0\) throughout the shifted contour, since its imaginary
part has modulus at most \(T/2+|t_0|<T\). Horizontal pieces
and the tails on the original Euler line are negligible by taking
enough smooth derivatives. Consequently
\[
 |A_v(L;M,t_0)|
 \ll_{h,\epsilon}\mathfrak X^\epsilon
 (1+|t_0|)^{C_{h,\epsilon}} L^{b+h-1}
 +O_A(\mathfrak X^{-A}).                                       \tag{17}
\]
The fixed possible principal rows are treated separately by removing
the pole of \(L\); its reciprocal has a zero there. Their contribution
satisfies the Q bound \(L^{-1/8+h}\), with the same harmless losses.

### 5. Stratification by the rightmost low-height zero

Use bins of fixed width \(h\) between \(1/2+h\) and \(7/8\).
In each bin classify a row by the supremum of the real parts of
its zeros of height at most \(4T\). If there are no zeros to the
right of \(1/2+h\), use that baseline. Formula (7) bounds the
number in a bin with left endpoint \(b\) by
\(\mathfrak X^\epsilon V^{d(b)}(1+|t_0|)^C\); formula (17), applied
above its upper endpoint, bounds its column by \(L^{b-1+O(h)}\).
Input Q ensures that the last possible endpoint is \(7/8\).
There may be zeros on that boundary, but the evaluation line remains
strictly to its right.

For the first moment the controlling expression is
\[
 \max_{1/2\le b\le7/8} V^{d(b)}L^{b-1}.                         \tag{18}
\]
Since \(d'(b)=-3/(2-b)^2\), it is nondecreasing in \(b\) if
\(\log L/\log V\ge64/27\). At the endpoint it is
\(V^{1/3}L^{-1/8}\). The baseline count \(O(V)\) is the same
expression at \(b=1/2\). Choose \(h\), then the height exponent
in \(T\), small enough to absorb every displayed loss into the
prescribed \(\mathfrak X^\epsilon\). This proves (2).

For the squared moment replace \(L^{b-1}\) by \(L^{2b-2}\).
The same argument only requires \(L\ge V^{32/27}\), and its square
root is \(V^{1/6}L^{-1/8}\), proving (3).

### 6. Prescribed prime slots and the exact present scope

If a selected squarefree product \(D\) is forced into the column,
then, on its genuine unit support,
\[
 A_{v,D}(L;M)
 =\frac{\mu(D)\eta(D)\psi_v(D)}{q_D}
 \sum_{(c,DM)=1}\frac{\mu(c)\eta(c)\psi_v(c)}{q_c}
 W(q_Dq_c/L).
                                                                    \tag{19}
\]
If \((D,M)>1\), or a character vanishes, the corresponding term
is simply zero. Thus for this fixed \(D\), the right sides of
(2)--(3) are multiplied by \(q_D^{-1}\) and use length \(L/q_D\).

For a fixed number of original prime slots with product norm
\(P_c\), summing their bounded smooth weights in absolute value
at the stage of (17) gives at most
\[
 L^{b-1+O(h)}
 \sum_{D\ {\rm in\ the\ slots}}q_D^{-b+O(h)}
 \ll_\epsilon \mathfrak X^\epsilon (L/P_c)^{b-1+O(h)}.
                                                                    \tag{20}
\]
Accordingly the safe first-moment bound is
\[
 \sum_v|A_v^{\rm selected}(L)|
 \ll_\epsilon \mathfrak X^\epsilon
 V^{1/3}(L/P_c)^{-1/8},
 \qquad L/P_c\ge V^{64/27},                                    \tag{21}
\]
and similarly for (3). A rowwise divisor bound alone would not
justify this step: it is the exact Möbius/Euler structure (19)
that does. Fixed coprimality masks cost only (16).

In the audited clean saturation block of the genuine quadratic
sector, all slots are assigned to the row gcd, so \(P_c=1\).
The scales are
\[
 V=Z^{13/48},\quad L=Z^{23/24},\quad S\asymp V.
                                                                    \tag{22}
\]
For its true smooth nonprincipal character sum, primitive Poisson
gives the pointwise estimate \(|B_v(S)|\ll\sqrt V\).
Using (2), this block is bounded by
\[
 \mathfrak X^\epsilon V^{5/6}L^{-1/8},                           \tag{23}
\]
instead of the earlier norm bound \(V\).
The exponent saving relative to that bound is \(95/576\).
It exceeds \(5/32\) by \(5/576\) for this one block.

This last comparison is not a bound for the full physical sector.
As the divisor scales move, \(S\) can be smaller than \(V\), and
some slots can move into the Möbius column. Then (21), the actual
pointwise or moment bound for \(B_v(S)\), and every outside divisor
weight must be combined before claiming a complete exponent.
In particular, neither the special block (23) nor finite numerical
tests prove the full low comparison or RH.

### 7. A robust finite-divisor summation consequence

This consequence deliberately uses the second moment (3), rather than
optimizing restricted-row moments in (23). It can be inserted into the
already audited full physical decomposition without selecting a new
exceptional scale.

Write \(L_e=C/(Gq_e)\), \(S_e=Y/(Gf q_e)\), \(R=Cf/Y\), and let
\(P_c\ge1\) be the norm product of the slots assigned to the Möbius
column. Only actual nonempty annuli \(L_e,S_e\gg1\) are included.
Suppose the two columns have exactly the common coefficients of the
audited bilinear lemma, with the Möbius column additionally having the
Euler structure of (19). Up to arbitrarily small ambient powers, its
row norm can be bounded by
\[
 \sqrt{1+V/L_e},
\]
or, when \(L_e/P_c\ge V^{32/27}\), by
\[
 V^{1/6}(L_e/P_c)^{-1/8}.
                                                                    \tag{24}
\]
The genuine smooth second column has norm
\(\sqrt{VS_e}\) for \(S_e\le V\), and
\(S_e(S_e/V)^{-A}\) for \(S_e\ge V\).
Consequently the full finite \(e\)-sum satisfies
\[
\boxed{\quad
 \sum_e q_e^{-1}\|A_e\|_2\|B_e\|_2
 \ll_\epsilon\mathfrak X^\epsilon
 \left[
 \min\{V,\ V^{25/24}(P_c/R)^{1/8}\}
 +V/\sqrt R
 \right].\quad}                                                 \tag{25}
\]

To verify the estimate, put \(x=P_c/R\).
The old common-coefficient lemma gives \(V+V/\sqrt R\).
If \(x\ge V^{-1/3}\), this is the minimum branch in (25).
Suppose therefore \(x<V^{-1/3}\), and set
\(S_*=xV^{32/27}<V\).
For \(S_*\le S\le V\), (24) times the second-column norm is
\[
 V^{2/3}x^{1/8}S^{3/8},
                                                                    \tag{26}
\]
whose largest value is \(V^{25/24}x^{1/8}\).
For \(S\ge V\), the corresponding product is
\[
 V^{1/6}x^{1/8}S^{7/8}(S/V)^{-A},
                                                                    \tag{27}
\]
with the same largest value if \(A>1\).
Ideal counting in dyadic \(q_e\)-intervals makes their \(q_e^{-1}\)
mass bounded, so the nonzero powers in (26)--(27) sum geometrically.
No infinite harmonic sum has been inserted.

In the residual short range \(S<S_*\), use the sieve bound. The
product is at most a constant times
\[
 \sqrt{VS}+V/\sqrt R.
                                                                    \tag{28}
\]
The first term is at most \(V^{59/54}x^{1/2}\) when \(S_*\ge1\).
Its ratio to \(V^{25/24}x^{1/8}\) is
\[
 V^{11/216}x^{3/8}\le V^{11/216-1/8}<1.
                                                                    \tag{29}
\]
If \(S_*<1\), this short range is empty up to fixed annular constants.
The second term in (28) is summed only over the original finite
nonempty \(e\)-range; its logarithm is absorbed in
\(\mathfrak X^\epsilon\).
This proves the improved bound, and taking the minimum with the old
bound proves (25). Fixed annular constants do not change any exponent.

For reference, in the exact full quadratic notation,
\[
 C=\frac U{N^3B},\qquad Y=\frac{Y'B}{Nq_j^2},
 \qquad R=\frac{Uq_j^2f}{Y'N^2B^2},
                                                                    \tag{30}
\]
and the outer factor is \(1/(NB)\).
The improved term of (25), after this outer factor, is exactly
\[
 V^{25/24}P_c^{1/8}(Y'/U)^{1/8}
 (NB)^{-3/4}q_j^{-1/4}f^{-1/8}.                                \tag{31}
\]
Thus this analytic consequence preserves a negative power of both
odd-branch scales. A full physical theorem must still retain the
audited Fourier/Gaussian tails, square layers, and compensation.

### Primary sources

* Goldmakher--Louvel, A quadratic large sieve inequality over number
  fields, Definition 1, Theorem 1.1 and Section 3:
  https://arxiv.org/pdf/1112.1642
* Blomer--Goldmakher--Louvel, L-functions with n-th order twists,
  proof of Corollary 1.6, Section 5, especially (5.3).
  The detector is used as an argument and re-estimated above;
  its published higher-order density conclusion is not substituted
  for a theorem about this quadratic fixed-twist family:
  https://arxiv.org/pdf/1112.1650
* Input Q, fixed source theorem and finite-order Hecke scope:
  https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex

# Part VIII. Moments of the actual selected Euler multiplier

## Selected-prime multipliers in the true quadratic Möbius column

### Result and exact scope

This note supplies a positive-moment estimate for the *actual Euler multiplier* caused by selected primes in the completed quadratic Möbius column. It does not supply a new zero-density theorem or close the complete low comparison. The quadratic character is the same zero-extended primary family used in the audited double-Poisson calculation.

Let K=Q(sqrt(-3)), write q_a=Na, and let psi_v=chi_v^3 for good squarefree v with V<=q_v<=2V, V>=2. All fixed ray factors can be resolved into finitely many common coefficients. Fix k>=1 and J>=0. For i=1,...,J let P_i be a disjoint set of good prime ideals in a fixed-ratio norm annulus [P_i,C P_i], P_i>=2. A selected product D consists of one prime from each of these sets; put P=product_i P_i. Products over no slots mean 1. Let |z_D|<=1. Every constant can depend on fixed J,k,C and the underlying ray data.

Define
\[
 A_v=\sum_D\frac{z_D\psi_v(D)}{q_D}.
 \tag{1}
\]
For every epsilon>0,
\[
 \sum_{v\asymp V}|A_v|^{2k}
 \ll_{\epsilon,k,J}(VP)^\epsilon\left(1+\frac V{P^k}\right).
 \tag{2}
\]
The estimate holds after arbitrary restriction of the positive v-sum, and permits fixed additional coprimality conditions on D. It does not assert orthogonality of different marked products pointwise.

Fix a finite-order eta and s=sigma+it with 1/2+delta<=sigma<=1, delta>0. The exact selected-column Euler multiplier is
\[
 E_v(s)=P^{s-1}\sum_D z_D
       \prod_{p\mid D}\frac{\eta(p)\psi_v(p)q_p^{-s}}
                             {1-\eta(p)\psi_v(p)q_p^{-s}}.
 \tag{3}
\]
(The factors mu(D), slot weights and common Mellin powers may be absorbed in z_D.) Then, uniformly in t,
\[
 \sum_{v\asymp V}|E_v(s)|^{2k}
 \ll_{\epsilon,k,J,\delta}(VP)^\epsilon
            \left(1+\frac V{P^k}\right).
 \tag{4}
\]
Common smooth slot weights bounded with their needed seminorms are allowed. Formula (4) includes the original zero mask psi_v(p)=0 at p|v; it does not replace that value by a unit.

### 1. Moment proof with every repeated-prime mask retained

Expand A_v^k. In each slot, partition its k selected occurrences according to equality of primes. There are finitely many equality patterns, depending only on k,J. For a fixed pattern let r_i be the number of distinct primes in slot i, and o_i the number of these primes having odd multiplicity. The product character is psi_v(C) times a unit mask for the primes of positive even multiplicity; C is the squarefree product of the odd-multiplicity primes. Its norm is comparable to
\[
 R=\prod_i P_i^{o_i}.
\]
Freeze all even-multiplicity primes first. Their row mask is retained in the positive row norm and may then be removed by enlarging that norm. Their exclusion from the odd-prime choices is a common column restriction, so the genuine quadratic large sieve still applies. There are at most O(product_i P_i^{r_i-o_i}) choices of these even primes. The coefficients of the odd column are common, supported on squarefree C, of size O(product_i P_i^{-k}), with multiplicity bounded in terms of k,J. Thus Goldmakher--Louvel gives for this pattern
\[
 \|A_v^k\|_{\ell^2(v)}
 \ll (VP)^\epsilon\sqrt{V+R}\,
       \prod_i P_i^{r_i-o_i/2-k}.
 \tag{5}
\]
The case R=1 is interpreted as the direct norm of the constant column and satisfies the same bound.

The multiplicities imply k>=2r_i-o_i and r_i<=k. Consequently the sqrt(V) part of (5) is at most sqrt(V)/P^{k/2}, and the sqrt(R) part is at most 1. Summing the finitely many patterns and squaring proves (2). This argument keeps all sharing between repeated selected products, rather than invoking an unsupported independent-prime model.

### 2. Exact Euler denominator reduction

For x=psi_v(p) in {0,1,-1}, the exact identity is
\[
 \frac{\eta(p)xq_p^{-s}}{1-\eta(p)xq_p^{-s}}
 =\frac{\eta(p)xq_p^{-s}+\eta(p)^2x^2q_p^{-2s}}
              {1-\eta(p)^2q_p^{-2s}}.
 \tag{6}
\]
Both sides vanish for x=0. For sigma>=1/2+delta the denominator is uniformly bounded away from zero, and is independent of v.

Expand the numerator in (6) over the fixed J slots. Write I for slots contributing x, and I^c for slots contributing x^2. Freeze the latter primes. Their product is a positive row unit mask. For the I slots, the normalized coefficients are O(1/q_D) times bounded common phases because q_D is comparable to product_{i in I}P_i. Apply (2) to this shorter slot family, with the frozen-prime exclusions retained. Summing the frozen primes in absolute value contributes at most
\[
 P_{I^c}^{-\sigma},\qquad
 P_{I^c}=\prod_{i\notin I}P_i,
\]
after the normalization P^{sigma-1} in (3). Therefore
\[
 \|E_v(s)\|_{2k}
 \ll (VP)^\epsilon\sum_{I\subseteq\{1,\ldots,J\}}
 P_{I^c}^{-\sigma}
 \left(1+\frac{V^{1/(2k)}}{P_I^{1/2}}\right)
 \ll (VP)^\epsilon\left(1+\frac{V^{1/(2k)}}{P^{1/2}}\right).
 \tag{7}
\]
The final step uses sigma>=1/2 and the fixed number of subsets. Raising (7) to 2k proves (4). Norm estimates for a restricted row set follow by positivity, without deleting a mask inside a signed product.

### 3. Exact link to a selected Möbius column

Every c below is good. Replace a common mask M by its part outside the fixed excluded set S, so that M is good. For this fixed common mask M and selected D prime to M, the Dirichlet series on Re s>1 is
\[
 \sum_{D\mid c,\,(c,M)=1}\frac{\mu(c)\eta(c)\psi_v(c)}{q_c^s}
 =\frac{1}{L_K^S(s,\eta\psi_v)}
   \prod_{p\mid M}(1-\eta(p)\psi_v(p)q_p^{-s})^{-1}
   \prod_{p\mid D}\frac{-\eta(p)\psi_v(p)q_p^{-s}}
                            {1-\eta(p)\psi_v(p)q_p^{-s}}.
 \tag{8}
\]
If p|D and p|v, both sides are zero. Common fixed ray restrictions are handled before (8) by the same finite partition as in the audited true-column proof. After summing the selected products, its genuine Mellin integrand contains P^{1-s} E_v(s), with the appropriate signs included in z_D. Thus on a zero-free contour at real part sigma the scalar length factor is (L/P)^{sigma-1}; the remaining multiplier is precisely (3), not an arbitrary extra column coefficient.

If an independently established zero-density decomposition provides a set of R bad rows at that contour, and B_v(S) is the exact smooth free-s character sum, (4) can be combined directly with Holder, for example
\[
 \sum_{v\in\mathcal E}|E_v(s)B_v(S)|
 \le R^{1/2}\|E_v(s)\|_4\|B_v(S)\|_4.
 \tag{9}
\]
The required smooth-s moment, density, inverse-L bounds, and the full physical divisor summation are separate inputs. No bound for the final complete probe is claimed in this note.

### Source

Goldmakher--Louvel, *A quadratic large sieve inequality over number fields*, Theorem 1.1 and the same primary quadratic family as the original QRH source: https://arxiv.org/pdf/1112.1642 . The arithmetic interface is the already audited quadratic bilinear full-probe calculation; no change of the target character family is made here.

# Part IX. Complete pure fifth-power sextic-core sector

## The complete pure fifth-power sextic-core sector

### Theorem and exact scope

This note concerns the original physical linear s--m pairing and the already-defined core marker and first Möbius decompletion. It does not use the second physical operator. The frequency sector is precisely
\[
 H=\varepsilon v^5a^6,\qquad
 v\ne1\text{ squarefree and good},\quad a\text{ any good ideal},
                                                               \tag{1}
\]
with the original finite unit choices. All physical n are retained. This is a complete pure conjugate-sextic core type; it excludes mixed cores and the unit core.

Use the original finite subset J, its length d in [0,1/6], and
\[
 X'=Z^{17/48-d},\quad Y'=Z^{23/48-d},\quad
 P\asymp Z^{1/6-d},\quad Q=q_{b_*}X'Y'.                \tag{2}
\]
Each remaining mark D is in the original slots, q_D about P. The independently reviewed bound is
\[
 |S_{\rm fifth}(Z)|\ll_\epsilon
 (1+|\nu|)^{C_\epsilon}Z^{133/480-d/2+\epsilon}.         \tag{3}
\]
After the actual Q^{-1/2} normalization and finite signed compensation, this yields
\[
 O_\epsilon(Z^{-67/480+\epsilon})                       \tag{4}
\]
for this entire frequency type. The same statement holds for original marking, core marking, and their first-decompleted versions. The complete-probe target is still 23/480 stronger, and every other sextic-core type remains outside this statement.

The source identities are the fixed QRH local scalar and phase-cancellation table, and the audited first Poisson/common-coefficient reorganization in Part V of this report. The analytic sieve below is the audited fixed-ray sixth-power large sieve of de Faveri, with the genuine residue characters; it is not a large sieve for arbitrary characters of comparable conductor.

### 1. A sixth-order common-coefficient estimate

Let v range over squarefree primary good ideals with q_v about V>=1. The sixth-power large sieve gives
\[
 \Theta_6(V,L)\ll_\epsilon(VL)^\epsilon
 [V+L+V^{5/6}L^{1/3}+V^{1/3}L^{5/6}].                 \tag{5}
\]
Thus a squarefree column of norm L, coefficient a_c/q_c with divisor-bounded a_c independent of v, has row norm at most a small power times
\[
 A(V,L)=1+(V/L)^{1/2}
                   +V^{5/12}L^{-1/3}+V^{1/6}L^{-1/12}. \tag{6}
\]
Fixed column masks, bounded row masks and conjugating the characters are allowed.

For a common smooth/ray s sum of norm S, its row norm is at most a small power times
\[
 \sqrt{VS}+S+V^{5/12}S^{2/3}+V^{1/6}S^{11/12}.        \tag{7}
\]
To include all s, write s=t ell^6 with t sixth-power-free. For each ell apply (5) to the t column and use Minkowski. The four resulting ell-series have powers -3,-6,-4,-11/2, all summable; the restriction (v,ell)=1 is deleted only inside each positive norm.

Primitive smooth Poisson, with its zero Fourier mode absent, also gives row norm O(V) for all S<=V, and
\[
 O_A(S(S/V)^{-A})\quad(S>=V).                         \tag{8}
\]
The fixed bad/ray conductor changes only the constant. For S<=V, the S term in (7) is absorbed by sqrt(VS), and its last term by the preceding one. Consequently use
\[
 B(V,S)\ll
 \begin{cases}
 \sqrt{VS},&S\le V^{1/2},\\
 V^{5/12}S^{2/3},&V^{1/2}\le S\le V^{7/8},\\
 V,&V^{7/8}\le S\le V,\\
 S(S/V)^{-A},&S\ge V.
 \end{cases}                                         \tag{9}
\]
All small-power losses are understood. The two middle breakpoints arise from the actual sixth-order sieve, not the quadratic bound.

Put L=C_*/(Gq_e), S=Y_*/(Gq_eq_f) on nonempty physical annuli. The analytic summation estimate needed below is
\[
\boxed{\begin{split}
 \sum_e q_e^{-1} A\left(V,\frac{C_*}{Gq_e}\right)
                   B\left(V,\frac{Y_*}{Gq_eq_f}\right)
 \ll Z^\epsilon\bigg[
 V+V^{17/16}\left(\frac{Y_*}{C_*q_f}\right)^{1/2}
 +V^{9/8}\left(\frac{Y_*}{C_*q_f}\right)^{1/3}
 +V^{35/32}\left(\frac{Y_*}{C_*q_f}\right)^{1/12}
 \bigg].
\end{split}}                                                    \tag{10}
\]
Here the e sum is only over its actual finite nonempty ranges, and the smooth seminorms are suppressed. To prove (10), note L=R S with R=C_*q_f/Y_*. Each dyadic e interval has bounded reciprocal ideal mass. On the three small-S intervals in (9), multiply B successively by 1, V^{1/2}R^{-1/2}S^{-1/2}, V^{5/12}R^{-1/3}S^{-1/3}, and V^{1/6}R^{-1/12}S^{-1/12}. Their maximum V-powers are respectively
\[
 1,\quad17/16,\quad9/8,\quad35/32.
\]
For example the last three maxima occur at S=V^{7/8}. The first small-S interval of the second term is constant in S and contributes only a logarithm. On S>=V use (8) with A sufficiently large; the corresponding exponents are no larger. The number of actual dyadic intervals and every logarithm are included in the small power. This argument never inserts an empty subunit column annulus.

### 2. Common coefficients at n=1

The audited first completion is valid for (1), with g=(c,rad H), c=g c_1 and s=g t. Its Ramanujan factor is phi(g), since every positive valuation of H is at least five. Expand (t,c_1)=1 using e|c_1 and expand the sixth-power mask using f|rad a. Then c_1=e c_2 and t=e f s_2.

Exactly as in the original coefficientwise CRT identity,
\[
 \mu(c)\mu(e)=\mu(g)\mu(c_2),\qquad
 \chi_e(H)\overline{\chi_e(H)}=1.
\]
The remaining c_2 coefficient is mu(c_2)eta(c_2)/q_c2, with the original divisor-slot weights and fixed masks. The free characters are, after a fixed ray partition,
\[
 \chi_v(c_2),\qquad\overline{\chi_v(s_2)}.              \tag{11}
\]
The f character and all unit factors are bounded row weights. All choices of g in one dyadic block are collected inside the v-row coefficient, not estimated separately with row-dependent column coefficients. The c_2 masks involving the v part of g are already enforced by chi_v(c_2)=0; its remaining part divides a and is a fixed column mask. The free s_2 coefficient is common smooth/ray data after the exact f expansion, so (8) applies.

The original prime slots are assigned to g,e,c_2, in that priority order. The g selections are row divisors, e selections are fixed scalars and c_2 selections are common divisor-bounded column coefficients. The Gaussian dependence on D is Mellin-separated on real part zero. Thus no real power of the number of marks is lost.

### 3. Every physical n is a square, and its exceptional boundary

The fixed local table has odd-l entries only in numerator residue classes j=2,3,4. In (1) every numerator prime residue is 0 or 5. Therefore any nonzero physical term has
\[
 n=r^2.                                                \tag{12}
\]
For a prime p^b exactly dividing r, write e_0=v_p(c) in {0,1}, k=v_p(s), and j'=v_p(H). The exact local scalar table gives no nonzero term with j'<6b-1.

If j'>=6b, comparison with the n=1 scalar at frequency valuation j'-6b gives the common factor P^{6b}, except for the explicitly retained multiplier
\[
 M_p(c,s)=1_{p^2\nmid s}
          [1-P^{-1}1_{p\nmid c,\ p\nmid s}].          \tag{13}
\]
Indeed:
- e_0=k=0 gives the principal Ramanujan value P^{6b}(1-P^{-1});
- e_0=0,k=1 is nonzero only at j'=6b and gives P^{6b};
- e_0=1,k=0 or 1 is exactly P^{6b} times the n=1 scalar;
- k>=2 is zero.
The original phase table gives precisely kappa(p)^b: gamma_3(p)^2=omega_p cancels its extra omega_p^b factor. Including the original q_n^{-1} and q_A^{-1}, the outside multiplier is kappa(p)^b P^{-2b}.

There is one lower boundary: j'=6b-1, necessarily e_0=k=0. Its scalar is -P^{6b-1}. In the fifth-power type this means p divides v and v_p(a)=b-1. Let h_0 be the squarefree product of all these boundary primes. Then
\[
 h_0\mid\operatorname{rad}r,\quad h_0\mid v,\quad
 a=(r/h_0)a',\quad(h_0,a'cs)=1,                       \tag{14}
\]
and the extra multiplier is exactly mu(h_0)/q_h0. Shared primes between r/h_0 and h_0 are allowed.

For this reduced n=1 comparison the effective frequency is H_eff=Hh_0/r^6=(v/h_0)^5(a')^6. In its common-coefficient reorganization, use g=(c,rad H_eff)=(c,rad(v a')); the last equality uses (c,h_0)=1. This g need not equal (c,rad H), because ordinary sixth-power factors of r have been removed. All additional effects at those fixed r primes are retained by (13). The apparent h_0 twist is not dropped: the free s character acquires bar chi_s(h_0), and the c character acquires chi_c(h_0), which restore exactly (11) for the full v. The auxiliary bad character is likewise the original bar xi(v^5). Thus the full r,h_0 contribution has coefficient
\[
 \frac{\kappa(r)}{q_r^2}\frac{\mu(h_0)}{q_{h_0}},       \tag{15}
\]
with the same common c/s character pair, all original masks, and (13) at the ordinary primes of r.

For precision about the finite masks, expand each factor (13) before applying a norm inequality. It produces only C^{omega(r)} choices of fixed-prime c/s restrictions. A c-unit condition factors among g,e,c_2; its g part is a row mask and its c_2 part a fixed column mask. After splitting the finitely many possible valuations of the fixed r primes in g,e,f, an s-divisibility condition extracts a fixed divisor tau from s_2. Its character value is a bounded row coefficient, zero when required by the original extension, and the free s scale is reduced from Y' to Y'/q_tau. No arbitrary coefficient is inserted in that free smooth sum. Every term of (10) is nondecreasing in Y_*, so using Y_*<=Y' is a valid upper bound after applying (10). The finite count is absorbed into q_r^epsilon.

For original marking assign a chosen prime to the first applicable factor among r,g,e,c_2; for core marking omit r. This is the same exact finite-slot assignment as in the audited full quadratic argument. It preserves common column coefficients, fixed scalars and divisor-bounded row coefficients, including every shared prime.

### 4. The full r,h_0 and frequency sums

Keep independent T in (0,Z], with all original X',Y',slots fixed, and put
\[
 C=TP,\qquad K=C/X'.
\]
Use Gaussian annuli q_c q_r^6 about C_l=e^l C. Thus c has norm about C_l/q_r^6, and every nonempty annulus has q_r<=O(C_l^{1/6}). The free s annulus remains at most Y'. For fixed r,h_0,a', the Fourier envelope is
\[
 C_{A,M}(1+|\nu|)^{C_{A,M}}e^{-c l^2}
 \left(1+\frac{X'V^5(q_r/q_{h_0})^6q_{a'}^6}{C_l}\right)^{-M}.
                                                               \tag{16}
\]
All joint smooth weights are separated on real part zero as in the audited quadratic proof. This keeps the Gaussian tail and all column and row coefficients exact prior to Cauchy and the sieve.

Apply (10) with C_*=C_l/q_r^6, Y_*<=Y'. The four V-powers p are 1,17/16,9/8,35/32. Dyadic V summation against (16) gives, for every C_l/X'>0,
\[
 (C_l/X')^{p/5}(q_{h_0}/q_r)^{6p/5}q_{a'}^{-6p/5}.
                                                               \tag{17}
\]
This uses the full Schwartz tail and does not presume a hard frequency cutoff. Since every p>=1, the a' sum is absolutely convergent. All divisor factors can be absorbed by choosing preliminary small powers sufficiently small.

Multiply (17) by the actual r,h_0 weight q_r^{-2}q_h0^{-1}. For the last three terms also include respectively q_r^3, q_r^2, q_r^{1/2} coming from the powers of C_*^{-1}. Since h_0 divides rad r, the resulting bounds, after summing the choices of h_0 with a divisor loss, are respectively
\[
 q_r^{-3+\epsilon},\qquad q_r^{\epsilon},\qquad
 q_r^{-1+\epsilon},\qquad q_r^{-5/2+\epsilon}.         \tag{18}
\]
The first and fourth ideal sums converge. The third is logarithmic up to a small power. The second, summed over its actual nonempty range q_r<=O(C_l^{1/6}), is O(C_l^{1/6+epsilon}). This is why the exceptional 6b-1 boundary does not invalidate the bound but cannot be treated by the quadratic assertion r|a.

Gaussian summation over l, including empty small annuli and both tails, proves the uniform estimate
\[
\boxed{\begin{split}
 |S_{\rm fifth}(T)|\ll_\epsilon
 &(1+|\nu|)^{C_\epsilon}Z^\epsilon\frac{Q}{Y'^{3/2}}\,
 \mathcal F(TP;X',Y'),\\
 \mathcal F(C;X,Y)={}&
 (C/X)^{1/5}
 +(C/X)^{17/80}Y^{1/2}C^{-1/3}\\
 &+(C/X)^{9/40}(Y/C)^{1/3}
 +(C/X)^{7/32}(Y/C)^{1/12}.
\end{split}}                                                    \tag{19}
\]
It is valid also when C/X<1: (17) remains a valid positive moment upper bound there, and the empty physical annuli are not replaced by fictitious terms. The estimate need not reflect the stronger rapid decay that is available at very small T.

### 5. Original exponents and first decompletion

At T=Z and (2), the four powers inside F are respectively
\[
 13/80,\qquad269/11520-d/6,\qquad-89/1920,
                         \qquad185/1536.              \tag{20}
\]
The first is strictly the largest for every d in [0,1/6]. The common factor Q/Y'^{3/2} has exponent 11/96-d/2. Hence (19) gives (3).

For the first Möbius scale transform, keep X',Y' and every physical slot fixed and substitute T=Z/q_b^6 in (19), with its actual coefficient mu(b)kappa(b)/q_b^2. The four b-series have powers
\[
 -16/5,\qquad-51/40,\qquad-27/20,\qquad-45/16,         \tag{21}
\]
all strictly less than -1. Therefore the same bound passes by an absolutely convergent estimate to original-marked flat and core-flat probes. Multiplication of the redundant frequency by b^6 preserves exactly the pure fifth-power core. This does not invoke a missing coupled-scale low theorem at a different T.

Finally Q^{-1/2} gives -67/480+d/2. The original rescaling coefficient q_r^{-3/2} and its tuple count remove d/2, producing (4). The original Mellin weight absorbs the polynomial nu-loss. The common-coefficient, square-boundary, all-n summation and flat-transfer interfaces have passed independent review. The result controls only the frequency sector (1).

Primary sieve source: [de Faveri, Theorem 1.1, sixth-order family](https://arxiv.org/html/2610.04045v1). The exact original-family transfer is also recorded in [SIXTH_SIEVE_DETECTOR.md](SIXTH_SIEVE_DETECTOR.md).

# Part X. Two-sided high moments of the genuine smooth quadratic column

## Duality improves the high moments of the actual smooth column

This lemma uses only the audited quadratic Hecke large sieve and the
actual primitive smooth Poisson formula. It needs neither input Q nor
an external subconvexity estimate. It applies to the smooth free column
left by the exact physical decomposition, not to arbitrary column
coefficients.

Let \(v\) be nonunit good squarefree, \(q_v\asymp V\ge2\), and let
\(\nu_v=\rho\psi_v\), \(\psi_v=\chi_v^3\), with fixed finite ray data.
The actual characters are nonprincipal and their primitive conductor
norms are comparable to \(V\). Let
\[
 B_v(S)=\sum_{\mathfrak s\ {\rm good}}\nu_v(\mathfrak s)
 W(q_{\mathfrak s}/S),\qquad 1\le S\le V,
                                                               \tag{1}
\]
where \(W\) is a common smooth annular function. Finite common smooth
ray components, and common smoothly separated angular components, are
allowed with their fixed seminorm costs. Any fixed integer \(k\ge1\)
is permitted.

### Proposition

Uniformly for \(1\le S\le V\),
\[
 \boxed{
 \|B(S)\|_{\ell^{2k}(v)}
 \ll_{\epsilon,k}(VS)^\epsilon
 \left[V^{1/(2k)}S^{1/2}+\min\{S,V^{1/2}\}\right].}
                                                               \tag{2}
\]
The constants are controlled by finitely many smooth seminorms.
Consequently, for an arbitrary set \(\mathcal E\) of \(R\) rows,
\[
 \sum_{v\in\mathcal E}|B_v(S)|
 \ll_{\epsilon,k}(VS)^\epsilon
 R^{1-1/(2k)}
 \left[V^{1/(2k)}S^{1/2}+\min\{S,V^{1/2}\}\right].              \tag{3}
\]
One can also use the pointwise bound
\[
 \sum_{v\in\mathcal E}|B_v(S)|
 \ll_\epsilon (VS)^\epsilon R\min\{S,V^{1/2}\}.                 \tag{4}
\]
There is no assumption that \(\mathcal E\) is independent of \(S\).

### 1. Direct moments

The \(k\)-th power of (1) is a common Dirichlet polynomial of norm
length \(O_k(S^k)\):
\[
 B_v(S)^k=\sum_{\mathfrak n}a_{\mathfrak n}\psi_v(\mathfrak n),
 \qquad a_{\mathfrak n}\ll_{\epsilon,k}q_{\mathfrak n}^{\epsilon}.
                                                               \tag{5}
\]
The fixed \(\rho\)-factor and all smooth product weights are inside
the common coefficients. Decompose
\(\mathfrak n=\mathfrak b\mathfrak l^2\), with \(\mathfrak b\)
squarefree, and keep the actual coefficients
\(a_{\mathfrak b\mathfrak l^2}\).
The factor \(\psi_v(\mathfrak l^2)\) is the row restriction
\((v,\mathfrak l)=1\), removable only in the positive row norm.
Goldmakher--Louvel and Minkowski give, for any common polynomial
of length \(N\) with these bounded coefficients,
\[
 \left\|\sum_{q_n\ll N}a_n\psi_v(n)\right\|_2
 \ll_\epsilon(VN)^\epsilon
 \sum_{q_l\ll\sqrt N}
       \sqrt{(V+N/q_l^2)N/q_l^2}
 \ll_\epsilon(VN)^\epsilon(\sqrt{VN}+N).                        \tag{6}
\]
Take \(N\asymp S^k\) and then the \(k\)-th root. This proves
\[
 \|B(S)\|_{2k}
 \ll_{\epsilon,k}(VS)^\epsilon
       (V^{1/(2k)}S^{1/2}+S).                                 \tag{7}
\]
The argument does not pretend that the product indices in (5)
are squarefree.

### 2. Apply the same moment to the true Poisson dual

Primitive smooth Poisson expresses (1) as a fixed finite combination
of terms of the form
\[
 \epsilon_v\,\frac S{\sqrt{q_{f_v}}}
 \sum_{\mathfrak n\ne0}\overline{\nu_v}(\mathfrak n)
       \widetilde W(q_{\mathfrak n}S/q_{f_v}),                  \tag{8}
\]
where \(q_{f_v}\asymp V\), \(|\epsilon_v|=1\), and
\(\widetilde W\) is the actual Schwartz transform.
The zero frequency is absent because the actual character is
nonprincipal. Fixed deleted primes and finite ray conventions are
handled before this step by their fixed finite decomposition.
Concretely, partition by the finitely many bad conductor factors
\(f_v=c_vv\). Extra deleted bad Euler factors give only a fixed
finite collection of dilations and bounded row factors. Moving
coprimality masks are not included in this assertion.

The ratio \(q_{f_v}/V\) lies in a fixed compact positive interval.
Mellin/Fourier separation of this ratio gives common dual column
weights, with absolutely integrable separation coefficients.
Their seminorms and the Schwartz-tail bounds are uniform.
For an explicit separation, put \(x=q_{f_v}/V\), \(N=V/S\), and
insert a fixed compact cutoff in \(x\). Fourier inversion in
\(\log x\) of \(\zeta(x)\widetilde W(y/x)\), \(y=q_n/N\), gives
common functions \(h_t(y)\) times the row factor \(x^{it}\).
Their seminorms decay faster than any chosen power of \(|t|\).
On \(0\le y\le2\) they are uniformly bounded; on \(y\asymp2^j\)
they additionally have arbitrarily rapid \(2^{-j}\) decay.
The root number and all separated imaginary powers are bounded
row factors; they do not affect positive high moments.

The dual scale is \(N=V/S\ge1\). On its main range, apply (7) to
the conjugate quadratic family. Dyadic tails beyond \(N\) are
summed by arbitrarily rapid Schwartz decay; on norm below \(N\)
one uses (6) for a polynomial of length \(O(N)\).
In particular, the dual weight is not assumed to vanish near zero.
Its bounded near-zero part is handled on \(q_n\le2N\); the zero
frequency itself was removed in (8).
Minkowski in \(\ell^{2k}\) also handles the absolutely integrable
separation. It follows that
\[
\begin{split}
 \|B(S)\|_{2k}
 &\ll_{\epsilon,k}(VS)^\epsilon
   \frac S{\sqrt V}
   \left[V^{1/(2k)}(V/S)^{1/2}+V/S\right]\\
 &=(VS)^\epsilon
   \left[V^{1/(2k)}S^{1/2}+\sqrt V\right].
                                                               \tag{9}
\end{split}
\]
Taking the smaller of (7) and (9) proves (2).
Hölder proves (3). Formula (4) is the direct length estimate
together with the already audited smooth primitive Poisson bound.

For nonradial common weights, the same argument is carried out
on the two-dimensional Poisson transform, or after angular Fourier
separation. The dual weights may depend on that fixed separated
angular order, with polynomial seminorm bounds; rapid decay of the
original angular Fourier coefficients makes the sum converge.
The conductor generator's complex direction, when present, is
separated at the same time: its angular mode contributes
\(e^{im\arg f_{v,\rm prim}}\), a unit-modulus row factor.
Finite unit compensation only changes the fixed bad-ray factor
according to \(m\) modulo six. The good conductor remains \(v\).
No arbitrary moving coefficient is placed in the dual column.

### 3. Why the sixth moment changes the relevant scale

For illustration only, suppose a zero-detected row set satisfies
\(R\le V^{1/3}\). Write \(S=V^s\), \(0\le s\le1\).
The fourth moment in (2) is
\[
 \|B(S)\|_4\ll V^{1/4}\sqrt S,
                                                               \tag{10}
\]
up to small powers throughout this entire interval.
This is stronger, for \(S>\sqrt V\), than retaining only the
direct fourth-moment term \(S\).

The sixth-moment bound is
\[
 \|B(S)\|_6\ll
 V^{1/6}\sqrt S+\min(S,\sqrt V).                               \tag{11}
\]
Combining (3) for \(k=2,3\) with (4), and multiplying by
\(S^{-1/8}\), the largest power is
\[
 V^{53/72},                                                    \tag{12}
\]
attained at the intersection of the increasing sixth-moment branch
and the pointwise branch, \(S=V^{7/9}\).
One may verify this by the exponents
\[
 \min\!\left\{
 \frac13+\min(s,\tfrac12),\
 \frac14+\frac14+\frac s2,\
 \frac5{18}+
   \max(\tfrac16+\tfrac s2,\min(s,\tfrac12))
 \right\}-\frac s8.                                           \tag{13}
\]
The middle expression is the fourth-moment bound with its full
Poisson improvement. A direct finite piecewise-linear check gives
the maximum \(53/72\); the earlier intersection at \(s=5/9\)
only gives \(17/24\).

This example is not yet a full marked physical theorem.
Prime-slot multipliers require their own common moments, and the
actual odd/square layers, finite divisor ranges, Gaussian tails,
and compensation must all be retained. Formula (2), with its
complete quantifiers, is the reusable statement.

### Sources

Goldmakher--Louvel, *A quadratic large sieve inequality over number
fields*, Theorem 1.1 and Section 3:
https://arxiv.org/pdf/1112.1642

The exact common-column and nonprincipal Poisson matching are those
already audited for the complete physical quadratic-sector
decomposition. The new step is to apply the same common-coefficient
moment estimate on both sides of that genuine Poisson identity.

# Part XI. Q-conditional closure of the complete nonprincipal quadratic type

## The complete nonprincipal quadratic type below the low-comparison threshold

### Result and dependencies

This note applies the true quadratic Möbius-column density theorem, the selected-prime Euler-multiplier moments, and the two-sided smooth character-sum moments to the already audited complete double-Poisson identity. It keeps all physical n, all original fixed slots, all shared primes, and both exact first Möbius flattenings. The arithmetic identities are unchanged.

The new input Q is exactly the user's fixed finite-order Hecke zero-free half-plane Re s>7/8, with the provenance stated in Part VII of this report. The earlier bilinear bound did not use Q. Nothing here treats the principal/unit core or another nonquadratic kernel type.

Use the original subset parameters
\[
 X'=Z^{17/48-d},\quad Y'=Z^{23/48-d},\quad
 P=Z^{1/6-d},\quad Q\asymp X'Y',\quad 0\le d\le1/6.
 \tag{1}
\]
The fixed number of remaining selected-prime slots have product norm comparable to P. Let the quadratic sector consist of the original nonzero completed frequencies H=epsilon v^3 a^6, where v is good squarefree and nonunit. All units epsilon, all allowed common factors, and every original physical n are retained.

**Theorem.** Subject to the stated Q input and the independently proved analytic lemmas listed below, for every epsilon>0 the complete quadratic sector satisfies
\[
 |S_{\rm quad}|\ll_\epsilon (1+|\nu|)^{C_\epsilon}
 Z^{521/2304-d/2+\epsilon}.                              \tag{2}
\]
After the original Q^{-1/2} normalization and the full finite compensation,
\[
 |I_{\rm quad}^{\rm compensated}|
 \ll_\epsilon Z^{-439/2304+\epsilon}.
 \tag{3}
\]
This holds for the original completed marker D|cn^3, the core marker D|cn_0 with n=n_0r^2, and their respective exact first Möbius-flat operators. The exponent in (3) is below -3/16 by 7/2304. It closes the required estimate for this complete nonprincipal quadratic type only.

The proof uses no Burgess subconvexity input. The earlier pointwise Burgess budget is superseded by a genuine smooth dual-moment estimate.

### 1. Precise analytic inputs

Write psi_v=chi_v^3 in the original zero-extended primary convention. After a fixed finite ray partition, the true Möbius column has a reciprocal of L(s,eta psi_v), with eta fixed finite-order. Its common masks delete only Euler factors; they do not change the exceptional family of zeros.

For a fixed small bin width h>0, the density theorem partitions the v~V rows according to their rightmost zero at the required finite buffered height. If b is the lower endpoint of a bin, put
\[
 a=1-b,\qquad \mathfrak d(a)=\frac{3a}{1+a},\qquad
 1/8\le a\le1/2.
 \tag{4}
\]
Endpoint displacements O(h) are absorbed in the prescribed Z^epsilon loss. The bin has at most Z^epsilon V^{\mathfrak d(a)} rows. On a contour just to the right of its upper endpoint the reciprocal L-function is Z^epsilon times a polynomial in the separated Mellin parameters. The deleted common Euler factors cost only the same small-power loss. Thus, before taking a row sum, the unselected Möbius column has scalar factor L^{-a}; with selected c-slots of total norm P_c it has (L/P_c)^{-a} times the *exact* normalized Euler multiplier E_v(s).

For every fixed integer k>=1, that multiplier satisfies
\[
 \sum_{v\asymp V}|E_v(s)|^{2k}
 \ll_\epsilon (VP_c)^\epsilon(1+V/P_c^k).
 \tag{5}
\]
The coefficients selecting those primes are independent of v. Every repeated-prime unit mask and every selected-prime Euler denominator is included in (5).

Let B_v(S) be the actual free-s smooth character sum after the already audited common-weight separation. For every fixed integer l>=1, the two-sided smooth moment is
\[
 \|B_v(S)\|_{2l}
 \ll_\epsilon (VS)^\epsilon
 \max\{V^{1/(2l)}\sqrt S,\min(S,\sqrt V)\},\quad 1\ll S\ll V.
 \tag{6}
\]
The trivial and primitive-Poisson pointwise bound is min(S,sqrt V), and for S>=V the actual smooth sum has arbitrary power decay in S/V. Formula (6) follows by applying the genuine quadratic sieve to B^l both before and after primitive two-dimensional Poisson, whose dual length is V/S. The root number is a bounded row factor. The dual smooth weights have common Mellin separation and rapidly decaying tails. In particular no arbitrary rough column is submitted to that Poisson step.

All fixed-ray factors, norm-Mellin parameters, and smooth seminorm costs in these three inputs match the previously audited common-column interface.

The user's commit [bbb8bba6, QUADRATIC_MOBIUS_GAIN.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/bbb8bba6f6a678848a270a4c950568a672cc975f/reports/20261011_qrh_selection_bridge/QUADRATIC_MOBIUS_GAIN.md) Sections 3--5, makes three inherited structural points explicit, and they are retained here. First, joint log-Fourier separation is used in the form
\[
 F(x,y)=\frac{\rho_x(x)\rho_y(y)}{(2\pi)^2}\int \widehat F(t,u)x^{it}y^{iu}\,dt\,du,
\]
with fixed product cutoffs equal to one on the original profile support; thus every separated mode remains compactly supported in both columns. Second, the actual reciprocal-L modulus contains every deleted prime, especially h. The original character zeros absorb the v, n_0, and v-supported g factors; the other common masks include e,h,a'. Their full imprimitive modulus is retained and costs at most the ambient small-power factor, rather than being hidden in a fixed-conductor constant. Third, the user's exact LCM calculation gives mu(e)mu(lcm(e,D_0))=mu(D_0/(D_0,e)) on compatible squarefree support. In our priority decomposition this is the same one-time cancellation producing the true c_2 Möbius column; it creates no extra free Möbius sign in e. The e sum in Section 4 is still bounded in absolute value. These clarifications are attributed to that user-authored source and do not alter the exponent below.

### 2. The entire free-s scale, using the eighth moment

Set R=V^{\mathfrak d(a)}. For a bin containing at most R rows, Holder with l=4 in (6), and the pointwise bound, gives
\[
 \sum_{v\in\mathcal E}|B_v(S)|
 \ll Z^\epsilon\min\left\{
 R\min(S,\sqrt V),\
 R^{7/8}\max(V^{1/8}\sqrt S,\min(S,\sqrt V))\right\}.
 \tag{7}
\]
For all positive effective scales S, including the rapid long-S tail,
\[
 S^{-a}\sum_{v\in\mathcal E}|B_v(S)|
 \ll Z^\epsilon V^{F(a)},\qquad
 F(a)=\frac78\mathfrak d(a)+\frac12-\frac a2.
 \tag{8}
\]
Here is a complete scale check. For S<=sqrt V the right side of (7), multiplied by S^{-a}, increases on each of its power pieces; its maximum is at S=sqrt V and has exponent
\[
 F_{\rm left}=7\mathfrak d/8+1/2-a/2.
\]
For sqrt V<=S<=V^{3/4} the eighth-moment norm is sqrt V, so the same expression decreases. Above V^{3/4}, the moment piece meets the pointwise piece at S=V^{(3+\mathfrak d)/4}; its largest value has exponent
\[
 F_{\rm right}=\mathfrak d+1/2-a(3+\mathfrak d)/4.
\]
Their exact difference is
\[
 F_{\rm right}-F_{\rm left}
 =\frac{a(1-8a)}{8(1+a)}\le0.
 \tag{9}
\]
The long-S Poisson tail only reduces the bound. At a=1/8 both possible peaks are present, at S=V^{1/2} and S=V^{5/6}, and F(1/8)=35/48. No isolated transition point is mistaken for the maximum over the whole scale range.

### 3. Selected slots do not recreate the old power loss

Combining (5) with either bound in (7) gives an extra common factor
\[
 R^{-1/(2k)}(1+V/P_c^k)^{1/(2k)}
\]
for the normalized Euler multiplier. Holder is legitimate since 1/(2k)+1/8<=1. The total selected-column cost relative to L^{-a} is therefore at most
\[
 P_c^a\min_{k\ge1}
 R^{-1/(2k)}(1+V/P_c^k)^{1/(2k)}
 \ll_\epsilon V^\epsilon\{1+P_c^a V^{-\mathfrak d(a)/4}\}.
 \tag{10}
\]
Only finitely many k, depending on epsilon, are needed.

For clarity, if P_c<=sqrt V set t=log V/log P_c>=2. A sufficiently tiny P_c is handled by P_c^a<=V^epsilon and the direct bound |E_v(s)|<<1: in each of the fixed number of slots, the prime count times q_p^{-Re s}, together with its normalization P_i^{Re s-1}, is bounded; the Euler denominators are uniformly bounded on these contours. Otherwise put m=floor t>=2 and choose k=m or m+1. The former gives no positive power loss when t<=m(1+a); the latter does so when t>=2(m+1)(1+a)/3. Since m>=2, these two intervals cover [m,m+1]. This proves a V^epsilon bound in that range. If P_c>=sqrt V, take k=2 in (5), obtaining the second term in (10). The case P_c=1 is immediate. This argument uses the actual Euler-multiplier moments, not a putative independence between the slots and the exceptional rows.

### 4. Exact physical n and finite e summation

We now use the previously audited identities without changing their masks. Write n=n_0r^2, n_0 squarefree; h|rad r, j=(h,rad s), k=h/j. The exact frequency transfer preserves the quadratic core and leaves r^{-2}k^{-1}. Nonzero odd branches force n_0|v and (n_0,a')=1. Write n_0=EF, q_{n_0}~N, q_E~B. With g the genuine c-only common-prime divisor,
\[
 c=E g e c_2,\qquad s=F g j^2 e f s_2.
 \tag{11}
\]
Only g contributes the Ramanujan factor. The exact outside coefficient is 1/(NB), while the two free columns have lengths
\[
 L=\frac{U}{N^3 B G q_e},\qquad
 S=\frac{Y'B}{N Gq_j^2q_eq_f},\qquad
 \frac LS=\frac{Uq_j^2q_f}{Y'N^2B^2}.
 \tag{12}
\]
Here U=e^ell ZP/q_r^6 before an outer flattening. All original r/e/a' masks are fixed column masks; the v and n_0 masks are enforced by the original zero extension. The complete divisor sum over n_0,E,g in each dyadic block remains a bounded row coefficient. The fixed number of original selected slots are assigned to r,n_0,g,e,c_2 in the previously stated priority order (omit r for the core marker). In particular the c_2 slots in (10) really have common coefficients.

The actual e cutoff is finite: q_e is at most a constant times min(C_*/G,Y_*/(Gq_f)). In each dyadic e interval the ideal count cancels its outside reciprocal q_e^{-1}. Since the ratio L/S is independent of e, (8)--(10) give the full finite e sum, up to logarithms, as
\[
 Z^\epsilon V^{F(a)}
 \left(\frac{Y'}U\right)^a
 (NB)^{-1+2a}q_j^{-2a}q_f^{-a}
 \{1+P_c^aV^{-\mathfrak d(a)/4}\}.
 \tag{13}
\]
Every N,B dyadic sum is harmless because -1+2a<=0; the endpoint costs only logarithms. The j,f factors are at most one. Thus all physical odd branches are controlled. This estimate does not discard an e term on a claim that its support is artificial; every term of the exact inclusion-exclusion is bounded.

### 5. Full Fourier tails, all square layers, and both exact flattenings

The common smooth separation retains the audited envelope
\[
 e^{-c\ell^2}\left(1+\frac{X'V^3q_{a'}^6}{U}\right)^{-M}.
 \tag{14}
\]
This is a bound for the whole Fourier/Gaussian tail, not a sharp frequency truncation. Put
\[
 \kappa_0=F(a),\qquad \kappa_1=F(a)-\mathfrak d(a)/4.
\]
On 1/8<=a<=1/2, both kappas are strictly greater than 1/2. Therefore the V sum and then the a' sum give, for either kappa,
\[
 (U/X')^{\kappa/3}\quad(U/X'\ge1),
\]
with the convergent factor sum_{a'}q_{a'}^{-2kappa}; if U/X'<=1 they give any chosen positive power (U/X')^M instead. Gaussian summation absorbs the ell factors with arbitrarily large positive or negative ell.

For an exact first flat operator include its coefficient mu(delta)kappa(delta)/q_delta^2 and its scale Z/q_delta^6. Combine rho=r delta. The number and weights of its factorisations, and the h/j choices, cost only q_rho^epsilon. The unflattened operator corresponds to delta=1. Thus the square and flat layers are jointly bounded by a reciprocal-square rho sum with
\[
 U\asymp U_0/q_\rho^6,\qquad U_0=ZP,\qquad K_0=U_0/X'.
\]
For a term with exponent kappa, the range q_rho<=K_0^{1/6} contributes
\[
 Y'^a U_0^{\kappa/3-a}X'^{-\kappa/3}
 \sum_{q_\rho\le K_0^{1/6}}
 q_\rho^{-2-2\kappa+6a+\epsilon}.
 \tag{15}
\]
The first branch has an absolutely convergent rho sum: throughout the stated a interval, 2+2F(a)-6a>=5/4. For the second branch, if it is not absolutely convergent, the *actual finite cutoff* in (15) gives the additional boundary term
\[
 P^aY'^a U_0^{-1/6}X'^{1/6-a}.
 \tag{16}
\]
The complementary range uses the small-U/X' line following (14), and has the same or smaller boundary bound. No divergent infinite harmonic or subharmonic sum is suppressed. Gaussian tails preserve these bounds. This proves the same estimate for all four marker/operator choices in the theorem, using the exact original core-preserving frequency lift for each flattening.

Consequently, apart from Z^epsilon and the common Q/Y'^{3/2}, the entire sector is bounded by the sum, over the finitely many density bins, of
\[
 Y'^a\left[
 U_0^{F/3-a}X'^{-F/3}
 +P^a U_0^{(F-\mathfrak d/4)/3-a}
        X'^{-(F-\mathfrak d/4)/3}
 +P^aU_0^{-1/6}X'^{1/6-a}\right].
 \tag{17}
\]
All dependencies on nu and separated smooth parameters remain polynomial and are absorbed by the original rapidly decreasing Mellin weight.

The ambient parameter in the density and reciprocal-L estimates is, before any infinite sum, chosen to contain Z,V,q_rho,q_{a'},e^{|ell|} and the relevant separated heights. The e and other common-mask norms are controlled by these labels and their nonempty physical supports. Thus the intermediate losses are small powers of these actual labels, not literally Z^epsilon alone. They are absorbed only at the final summation: 2kappa_1>1 leaves strict room in the a' ideal sum, the first rho branch has exponent at most -5/4, the second rho branch retains its true finite cutoff and boundary estimate, and the full Schwartz/Gaussian bounds handle the remaining Fourier and ell tails. All initial small powers and the bin width h are selected in terms of the prescribed final epsilon. This yields the Z^epsilon notation in (17) without assuming that the infinite labels were uniformly bounded in advance.

### 6. Exact exponents and the scope of the closure

After Q^{-1/2}, the original subset contributes Z^{d/2} times the following exponents. The finite compensation removes that d/2 exactly as in the previous complete-quadratic proof. Since P<=Z^{1/6}, the two main exponents are bounded by
\[
 G_0(a)=-\frac{29}{96}+\frac{13}{48}F(a)-\frac{11}{16}a,
\]
\[
 G_1(a)=G_0(a)+\frac a6-\frac{13}{192}\mathfrak d(a).
 \tag{18}
\]
Both decrease on [1/8,1/2]. Indeed F'(a)=21/[8(1+a)^2]-1/2<=85/54, which already proves G_0'<0 and G_1'<0 even after dropping the negative derivative of its last term. At a=1/8,
\[
 G_0=-\frac{439}{2304},\qquad
 G_1=G_0-\frac1{576}.
 \tag{19}
\]
The boundary term (16), after the same normalization, has exponent at most
\[
 -\frac7{16}+\frac7{24}a\le-\frac7{24},
 \tag{20}
\]
which is smaller than (19). Taking h and every analytic small-power loss sufficiently small proves (2)--(3).

The arithmetic and the new mean estimates concern the complete nonprincipal quadratic type. They do not prove that a principal/unit term dominates every remaining generic cubic or sextic type. The input Q, its fixed public provenance, and the independent status of every new analytic lemma must remain explicit when this result is integrated into the larger report.

### Internal proof dependencies

- Part V of this report: audited exact original/core/all-n/flat common-column arithmetic and normalization.
- Part VII of this report: genuine eta psi_v density, finite-height reciprocal control, and precise Q input.
- Part VIII of this report: exact selected-prime Euler-multiplier moments, including all zero masks.
- Part X of this report: genuine smooth direct/dual quadratic moments and their common-weight justification.

The user-supplied input Q and its formal-build attribution are pinned in [FORMAL_INPUT_Q](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/52ee48d3e2e4c5b0beeb3e4880eca86fb2208ce1/reports/20261011_qrh_selection_bridge/FORMAL_INPUT_Q.md). The present conditional consequence does not claim an independent rerun of that build.

# Part XII. Q-conditional true Möbius mean for the complete cubic type

## A true Möbius-column mean bound for the complete cubic sector

### Statement and inputs

Retain every definition and arithmetic normalization in the independently audited Part VI of this report. In particular the entire cubic sector is H=epsilon w^2a^6 with nonunit cube-free w, all physical n, all units and sixth-power layers, and either the original or core marker. This note improves its normalized exponent using the actual Möbius column, not a bound for arbitrary large-sieve coefficients.

The additional input is **Q**: the user's fixed theorem that every finite-order Hecke L-function over Q(sqrt(-3)) is zero-free in Re(s)>7/8. Its recorded source and scope are retained; this note does not independently rerun the supplied formal verification. The other input is the cube-free cubic zero-density argument of de Faveri, Corollary 1.5 and its proof, with a fixed finite-order twist inserted in the common coefficients.

**Theorem (independently reviewed).** For the original marker, core marker, and each one's exact first Möbius-decompleted probe, the complete cubic contribution to the original normalized finite compensation satisfies
\[
 \boxed{I_{\rm cub}(Z)\ll_\varepsilon Z^{2/45+\varepsilon}.}      \tag{1}
\]
The Mellin seminorm dependence is polynomial and absorbed by the original outer weight. This improves 5/48 by 43/720. The result is still positive, and remains 167/720 above the full low target -3/16. No principal/unit-core or genuine sextic contribution is asserted here.

The whole finite e sum is included. Its worst permitted intermediate scale is not the convenient transition S=M: at the decisive zero bin it is S=M^{3/5}. A bound for one clean block would not prove (1).

### 1. Fixed-twist cubic density with the actual index norm

Let psi_w(c)=chi_c(w^2), retaining zero extensions, with cube-free w in M<=q_w<=2M. Fixed primary/ray partitions are understood. Its primitive conductor divides rad(w) times a fixed ideal and is O(M). Fix the original target eta. The family relevant to the Möbius column is the primitive family inducing eta overline{psi_w}; finite principal exceptions are harmless.

For one selected zero of each row, with real part at least b and height at most T, write R(b,T) for the number of such rows. The proof of de Faveri's Corollary 1.5 applies with eta inserted in every common Dirichlet coefficient and gives
\[
 R(b,T)\ll_\varepsilon M^{D_*(b)+\varepsilon}(1+T)^{C_\varepsilon},
 \quad\frac12<b<1,                                  \tag{2}
\]
where for the range used here
\[
 D_*(b)=\begin{cases}
 \dfrac{8(1-b)}{7-6b},&\frac12\le b\le\frac56,\\[2mm]
 \dfrac{2x(3-10x)}{1-12x^2},\quad x=1-b,
     &\frac56\le b\le\frac78.
 \end{cases}                                        \tag{3}
\]
We give the twist check rather than declaring a theorem for an unrelated family. The detector uses the finite inverse polynomial with coefficients mu(c)eta(c), and a polynomial tail with divisor-bounded coefficients multiplied by eta(c). Both remain common coefficients. The functional equation for eta overline{psi_w} has analytic conductor O_eta(M(1+T)^C); its root number is a bounded row factor. Its second moment on the half-line follows from the approximate functional equation of length at most sqrt(M) times a fixed height power and the cube-free cubic sieve. On removing c=t ell^3, the corresponding cube-layer sums converge. Thus the detector's moment and polynomial estimates retain exactly the M exponents of the cited argument, with only fixed eta and polynomial-height changes. Deleting finitely many fixed Euler factors also preserves them. No variable second cubic kernel is treated as a fixed twist.

Here is a simpler upper envelope sufficient for every subsequent exponent:
\[
 D(b)=\begin{cases}
 1,&\frac12\le b\le\frac23,\\
 \frac73-2b,&\frac23\le b\le\frac56,\\
 \frac{19}6-3b,&\frac56\le b\le\frac78.
 \end{cases}                                        \tag{4}
\]
It is continuous and 13/24<=D(b)<=1. Indeed, with x=1-b, the differences between the two linear pieces and the corresponding formulas (3) are
\[
 \frac{(1-6x)^2}{3(1+6x)},\qquad
 \frac{(1-6x)^3}{6(1-12x^2)},                         \tag{5}
\]
respectively. The second is used only for x<=1/6. For the first piece use the trivial O(M) row count. Hence (2) holds with D in place of D_*.

### 2. True inverse bounds and the price of column slots

Every column ideal c below is an original good ideal, coprime to the fixed excluded set S. The mask ideal m_0 means only its S-exterior part; Euler factors already deleted at S are not inserted again. For a fixed smooth annular W, such a column-mask ideal m_0 and real Mellin height t_0, define
\[
 A_w(L;m_0,t_0)=\sum_{(c,m_0)=1}
 \frac{\mu(c)\eta(c)\overline{\psi_w(c)}}{q_c^{1+it_0}}W(q_c/L).
                                                               \tag{6}
\]
The finite-height logarithmic-control argument used in Part VII of this report applies unchanged: in a zero-free rectangle Re(s)>b, |Im(s)|<=4T, Borel--Carathéodory followed by the two-constants theorem for log|log L| yields a subpower inverse bound a fixed positive distance from its boundary. The Euler logarithm fixes the analytic branch. The height buffer makes horizontal harmonic measure exponentially small. Consequently Mellin inversion of (6), truncated within |t|<=T/2, gives
\[
 |A_w(L;m_0,t_0)|\ll \mathfrak X^\varepsilon
 (1+|t_0|)^C L^{b-1+O(h)}                            \tag{7}
\]
for a row whose rightmost low-height zero is below b+O(h). Here h>0 is the fixed bin width, T is a sufficiently small positive power of an ambient arithmetic size mathfrak X times a fixed height power, and all data lie in a fixed power of mathfrak X. Derivatives of W control the discarded horizontal and high-height tails. Factors deleted by m_0 cost at most q_{m_0}^epsilon on the shifted lines. At the baseline b=1/2, use the bin beginning at 1/2+h and the trivial row count. Input Q caps the final bin at 7/8; the contour stays strictly right of a possible boundary zero.

A forced squarefree column product D_c must be extracted exactly:
\[
 A_{w,D_c}(L;m_0)=\frac{\mu(D_c)\eta(D_c)\overline{\psi_w(D_c)}}{q_{D_c}}
 A_w(L/q_{D_c};D_cm_0),                              \tag{8}
\]
with every nonunit case kept as zero. The original finite slot weights factor after zero-real-part Mellin separation. If their product scale is P_c, summing (7)--(8) over these actual slots costs
\[
 L^{b-1}\sum_{D_c}q_{D_c}^{-b}
 \ll_\varepsilon\mathfrak X^\varepsilon(L/P_c)^{b-1}.             \tag{9}
\]
This is the genuine price of column slots. It does not follow merely from a divisor bound on a marked row. Fixed masks, including e,h,a' from the completed arithmetic, are allowed in (6).

Choose bins of width h and a detector height exponent small enough, in that order, that all errors in (2), (7), and (9) fit a prescribed small power. Each bin then has at most mathfrak X^epsilon M^{D(b)} rows, on each of which the marked Möbius column has size at most mathfrak X^epsilon (L/P_c)^{b-1}. Arbitrary restrictions of these row sets and divisor-bounded row weights are allowed.

### 3. The restricted smooth column and the complete finite e integral

Use the audited common smooth/ray s_2 column B_w(S), not arbitrary coefficients. On a row set of cardinality at most M^{D}, where 1/2<=D<=1, one has
\[
 \sum_{w\text{ in the set}}|B_w(S)|
 \ll \min\{M^D\min(S,\sqrt M),\ M^{D/2} B_3(M,S)\},\quad S\le M,
                                                               \tag{10}
\]
up to small powers and smooth seminorms. The first term uses genuine pointwise counting and primitive Poisson; the second is Cauchy followed by the positive restriction of the cubic mean norm. For S>=M the pointwise long-Poisson estimate gives an arbitrarily decaying tail.

Recall from the complete-cubic proof that
\[
 B_3(M,S)\ll
 \begin{cases}
 \sqrt{MS},&S\le M^{1/2},\\
 M^{1/3}S^{5/6},&M^{1/2}\le S\le M^{4/5},\\
 M,&M^{4/5}\le S\le M.
 \end{cases}                                        \tag{11}
\]
All three estimates have harmless small powers. The cubic-layer decomposition and conductor<=M long-Poisson comparison were verified there.

For fixed physical n_0,E_4,g,f,j blocks, let
\[
 L=C_*/(Gq_e),\qquad S=Y_*/(Gq_eq_f),\qquad
 \mathcal R=\frac{C_*q_f}{Y_*P_c}.
\]
Thus L/P_c=mathcal R S. The sum over e has reciprocal weight q_e^{-1} and is finite on its actual nonempty supports. Dyadic ideal counting bounds it by a logarithmic multiple of the positive integral in dS/S. Combining (9)--(11) gives
\[
 \sum_e\frac1{q_e}\sum_{w\text{ in bin}}
   |A_w^{\rm marked}(L)B_w(S)|
 \ll \mathfrak X^\varepsilon\mathcal R^{b-1}M^{J(b,D)},
                                                               \tag{12}
\]
where
\[
 J(b,D)=\frac{D(2+3b)}5+\frac{3+2b}{10}.             \tag{13}
\]

Here is the full scale check. Below S=sqrt(M), each of the two bounds in (10), multiplied by S^{b-1}, is nondecreasing in S; the endpoint dominates, with a logarithm if b=1/2. Between sqrt(M) and M^{4/5}, the increasing large-sieve bound and decreasing pointwise-Poisson bound cross at
\[
 S_0=M^{(3D+1)/5}.                                  \tag{14}
\]
Since D>=1/2, this lies in that interval. At the crossing the value is
M^{D+1/2}S_0^{b-1}=M^{J(b,D)}. Above M^{4/5}, the pointwise bound dominates the capped mean bound and decreases after multiplying by S^{b-1}; beyond M use the true long-Poisson tail. These facts prove (12), including truncated or subunit e-transition ranges. No signed e contribution was identified with this positive majorant.

### 4. Complete n_0, marks, physical squares and decompletion

The audited exact arithmetic is unchanged. Write N about q_{n_0}, B about q_{E_4}, U_l=e^l TP/q_r^6. Then
\[
 C_*=\frac{U_l}{N^3B},\qquad Y_*=\frac{Y'}{Bq_j^2},
 \qquad\mathcal R=\frac{U_lq_j^2q_f}{N^3Y'P_c}.
                                                               \tag{15}
\]
The common outside n_0 weight is N^{-3/2}. Thus its factor in (12) is
\[
 N^{-3/2}\mathcal R^{b-1}
 =N^{3/2-3b}
 \left(\frac{U_l}{Y'P_c}\right)^{b-1}
 (q_j^2q_f)^{b-1}.                                  \tag{16}
\]
For b>=1/2, the N exponent is nonpositive and the number of dyadic ranges is logarithmic. Every choice of n_0,E_4,g is already pooled as a divisor-bounded row coefficient, as in the audited all-n proof. Positive j,f denominators may be bounded by one.

The first-applicable-factor slot assignment remains r,n_0,g,e,c_2 for the original marker and n_0,g,e,c_2 for the core marker. Row assignments are divisor-bounded; fixed e,r assignments retain their original scalar weights; column assignments are handled by (8)--(9). Since P_c<=C P and b-1<0, the safe uniform majorant in (16) replaces P_c by P. This includes the worst case where every remaining slot enters the Möbius column, rather than silently assuming P_c=1.

The Fourier envelope is still (1+X'M^2q_{a'}^6/U_l)^{-A}, with Gaussian e^{-cl^2}. In (12) use D=D(b) from (4), and write J(b)=J(b,D(b)). Weighted M summation then all a' give
\[
 (U_l/X')^{J(b)/2}\sum_{a'}q_{a'}^{-3J(b)}.
\]
Here J(b)>0.97 throughout the compact range, so the latter ideal sum converges with ample margin. The original arbitrary Fourier decay handles every small effective scale, without a hard cutoff.

Combining with q_r^{-2}q_k^{-1}, the r power is
\[
 q_r^{\,4-6b-3J(b)}.                                \tag{17}
\]
It is at most q_r^{-23/10} throughout 1/2<=b<=7/8; all h,j and divisor-small factors are summable. Gaussian l tails are also summable. Thus, up to a finite number of bins and arbitrarily small losses, the whole cubic sector at every 0<T<=Z is bounded by
\[
 \frac{Q}{Y'^{3/2}}
 \max_{1/2\le b\le7/8}
 \left(\frac{TP}{X'}\right)^{J(b)/2}
 \left(\frac{T}{Y'}\right)^{b-1}.                  \tag{18}
\]
The exact first Möbius operation has T=Z/q_{d_0}^6 and coefficient q_{d_0}^{-2} times a unit/sign. Its three-scale calculation is now replaced by (17) with d_0 in place of r; the same strict summability applies. The operation preserves the cubic core through the full-modulus d_0^6 frequency lift. Hence (18) covers both actual flat probes as well.

For rigor with the finite-height detector on unbounded physical tails, use an ambient arithmetic size containing Z, M, q_r, q_{a'}, and e^{|l|}. The resulting arbitrarily small powers are absorbed into the strict r,a' summability and the original Fourier/Gaussian decay, by choosing the initial losses smaller. No conductor-dependent constant is suppressed as a fixed row constant.

### 5. The actual worst exponent

At T=Z, K=Z^{13/16} and Z/Y'=Z^{25/48+d}. After Q^{-1/2}, the exponent before the original rescaling coefficient and tuple count is
\[
 E_d(b)=-\frac{29}{96}+\frac d2
          +\frac{13}{32}J(b)
          +\left(\frac{25}{48}+d\right)(b-1).
                                                               \tag{19}
\]
The original finite compensation contributes -d/2. Since d>=0 and b<1, the remaining d(b-1) is nonpositive. It suffices to maximize
\[
 E(b)=-\frac{29}{96}+\frac{13}{32}J(b)
                         +\frac{25}{48}(b-1).        \tag{20}
\]
For the three pieces (4),
\[
 J(b)=\begin{cases}
 \frac7{10}+\frac45 b,&\frac12\le b\le\frac23,\\
 \frac{37}{30}+\frac45b-\frac65b^2,&\frac23\le b\le\frac56,\\
 \frac{47}{30}+\frac9{10}b-\frac95b^2,&\frac56\le b\le\frac78.
 \end{cases}                                        \tag{21}
\]
E is increasing on the first two pieces: at the right end of the second its derivative is still 1/30. It is decreasing throughout the last piece. Therefore its maximum is at b=5/6, where
\[
 D=2/3,\qquad J=16/15,\qquad E=2/45.                \tag{22}
\]
This proves (1) for the complete arithmetic interface above. At this zero bin the finite-e peak (14) is S=M^{3/5}. The attractive S=M clean block is not the worst block of the actual completed majorant.

### Sources and boundary

- de Faveri, *Optimal large sieve for fixed order characters*, Theorem 1.1, Corollary 1.5 and its proof: https://arxiv.org/html/2610.04045v1 . The fixed target twist is checked through the argument in §1, rather than adding a moving twist to the stated theorem.
- User Q, fixed finite-order Hecke statement: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex . Its attribution and the recorded source-level/formal verification scope remain unchanged.
- The independently reviewed complete-cubic arithmetic proof and the quadratic Möbius note's finite-height inverse lemma. This part derives the cubic density and the complete physical e/slot budget separately.

A positive upper bound cannot establish a positive main term or a counterexample to the desired low bound. The remaining extra saving must use arithmetic beyond the absolute bin and e majorant proved here, or cancellation between its genuine signed pieces. Nothing here replaces the total R4 problem by a stronger arbitrary-coefficient inequality.

The user-supplied Q and its formal-build attribution are recorded in [FORMAL_INPUT_Q](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/52ee48d3e2e4c5b0beeb3e4880eca86fb2208ce1/reports/20261011_qrh_selection_bridge/FORMAL_INPUT_Q.md). This conditional extension does not independently rerun that build.

# Part XIII. Complete mixed quadratic and conjugate-sextic type

## A complete mixed quadratic / conjugate-sextic frequency type

### Claim and scope

Retain the original physical probe, its actual prime slots and signed finite compensation. This note concerns precisely
\[
 H=\varepsilon v^3w^5a^6,\qquad vw\text{ squarefree},\quad
 (v,w)=1,\quad v,w\ne1,                              \tag{1}
\]
with all original good-prime and unit conventions and every physical index n. The original marker and the core marker are both retained, as are their exact first Möbius-decompleted versions. There is no second physical operator.

Write d for the original rescaled subset length and use
\[
 X'=Z^{17/48-d},\quad Y'=Z^{23/48-d},\quad
 P\asymp Z^{1/6-d},\quad Q=q_{b_*}X'Y',\quad0\le d\le1/6.
                                                               \tag{2}
\]
The independently reviewed bound is
\[
 |S_{3,5}(Z)|\ll_\epsilon (1+|\nu|)^{C_\epsilon}
 Z^{37/96-d/2+\epsilon},                            \tag{3}
\]
and hence the complete normalized finite compensation from (1) is
\[
 O_\epsilon(Z^{-1/32+\epsilon}).                    \tag{4}
\]
This is a whole mixed type, not a bounded-w truncation. It remains 5/32 short of the full low target. It uses neither input Q nor a new zero-density theorem.

### 1. A quadratic family with the true fixed sextic twist

Fix squarefree w of norm about W, and let squarefree v have norm about V, with (v,w)=1. The two actual free characters after first completion are
\[
 \chi_v(c)^3\chi_w(c),\qquad
 \chi_v(s)^3\overline{\chi_w(s)}.                   \tag{5}
\]
A finite primary/ray partition supplies only fixed data. Their primitive conductor norms are comparable to VW, since the two good supports are disjoint; the original fixed bad factors do not change this comparison. This is the conductor used below, not V.

The audited quadratic large sieve still applies to the v rows: chi_w(c) is part of the common column coefficient. For squarefree c columns of norm L with divisor-bounded coefficients divided by q_c, their row norm is
\[
 A(V,L)\ll_\epsilon(VL)^\epsilon(1+\sqrt{V/L}).     \tag{6}
\]
For the actual common smooth free s column, direct square decomposition s=t ell^2 and Minkowski give
\[
 B(V,W;S)\ll_\epsilon(VWS)^\epsilon(\sqrt{VS}+S).
                                                               \tag{7}
\]
The additional fixed factor bar chi_w(ell^2) is bounded; its zero is retained. Only the v-induced row mask is removed inside a positive norm. Thus the direct estimate has no conductor-W loss.

Pointwise primitive smooth Poisson for the genuine product character, followed by the positive v norm, gives
\[
 B(V,W;S)\ll
 \begin{cases}
 V\sqrt W,&S\le VW,\\
 S W^{-1/2}(S/(VW))^{-A},&S\ge VW.
 \end{cases}                                        \tag{8}
\]
The zero dual frequency is absent. Its root number is a bounded row factor. Common norm-ratio/angular separation has uniform seminorms, with the same precise meaning as in the audited quadratic proof. In particular (8) is not invoked for arbitrary s coefficients.

Combining (7)--(8), usable ranges are
\[
 B(V,W;S)\ll
 \begin{cases}
 \sqrt{VS},&S\le V,\\
 S,&V\le S\le V\sqrt W,\\
 V\sqrt W,&V\sqrt W\le S\le VW,\\
 S W^{-1/2}(S/(VW))^{-A},&S\ge VW.
 \end{cases}                                        \tag{9}
\]
For L=C_*/(Gq_e), S=Y_*/(Gq_eq_f), the complete finite e sum consequently satisfies
\[
 \boxed{\sum_e q_e^{-1}A(V,L)B(V,W;S)
 \ll Z^\epsilon\left[V\sqrt W+
 V W^{1/4}\sqrt{\frac{Y_*}{C_*q_f}}\right].}         \tag{10}
\]
Only actual nonempty annuli are included. Each dyadic e interval has bounded reciprocal ideal mass. Put L=RS, R=C_*q_f/Y_*. The first column term in (6) times (9) has maximum V sqrt W; the second has maximum V W^{1/4}/sqrt R, at S=V sqrt W. The entire plateau costs at most logarithms. The S>=VW tail is no larger. This proves (10) uniformly even when a transition falls outside the actual e range.

### 2. Exact complete physical n and the new boundary

The source local C_p table has odd physical valuation l only at numerator residues 2,3,4 modulo six. Hence in (1), writing n=n_0r^2 with n_0 squarefree,
\[
 n_0\mid v.                                          \tag{11}
\]
At p|n_0 only residue 3 occurs. Its two nonzero branches are exactly the audited quadratic ones: E=(c,n_0), F=n_0/E; E is forced into c and F into s. The extra positive amplitude is 1/(q_{n_0}q_E), with every original unit/rho phase retained. Also (n_0,a')=1 in the effective frequency below. The common-character derivation does not evaluate these special branch phases as a character at a forced nonunit. In this mixed type the original rho^{-2} and rho^{-4} branch phases also contain the w residue-symbol factors. For fixed w they are genuine unit row factors attached to n_0|v; they are not declared to depend only on the fixed bad-ray class.

At a prime p^b||r with p|n_0, comparison with the l=1 coefficient at frequency exponent lowered by 6b has scalar ratio P^{6b}; all the relevant Gauss characters are nonprincipal. There is no extra boundary.

At p^b||r with p not dividing n_0, the exact comparison is the audited pure-fifth comparison of Part IX. On the ordinary range j'>=6b it has multiplier
\[
 M_p(c,s)=1_{p^2\nmid s}\bigl[1-P^{-1}1_{p\nmid c,p\nmid s}\bigr],
                                                               \tag{12}
\]
in addition to P^{6b}. The only lower boundary is j'=6b-1, necessarily residue 5 with p not dividing cs. Collect these primes into h_0. Then
\[
 h_0\mid\operatorname{rad}r,\quad h_0\mid w,\quad
 a=(r/h_0)a',\quad(h_0,a'cs)=1.                     \tag{13}
\]
The outside square-layer factor is exactly
\[
 \kappa(r)q_r^{-2}\mu(h_0)q_{h_0}^{-1}.              \tag{14}
\]
To check its phase also when p|n_0, compare l=l_0+2b with l_0 in {0,1} in the source local-P formula. The rho exponent changes by -6b. The omega exponent changes by 6bk-2be_0-b(2l_0+2b-1), congruent to b modulo two; gamma_3^{-2b}=omega^{-b} cancels it. The remaining phase is a_p^{2b}=kappa(p)^b.

The effective frequency is H_eff=Hh_0/r^6=v^3(w/h_0)^5(a')^6. Restore the omitted h_0 character factors from the source unit formula: free c gains chi_c(h_0), and free s gains bar chi_s(h_0), while shared g factors cancel. These restore precisely (5), including the original bad-character factor of H. Set
\[
 g=(c/E,\operatorname{rad}H_{\rm eff})=(c/E,\operatorname{rad}(vw a'))
                                                               \tag{15}
\]
after the forced E factor has been removed. The equality uses (c,h_0)=1. It need not equal the corresponding gcd with the unreduced H.

The remaining common decomposition is
\[
 c=E g e c_2,\qquad s=F g e f s_2,                  \tag{16}
\]
with any further fixed-divisor extraction from (12) kept in the second equation. Its free c_2 coefficient is the actual mu(c_2)eta(c_2)/q_c2 times chi_w(c_2), fixed masks and original column-slot weights. The free s_2 coefficient is common smooth/ray data times bar chi_w(s_2). The quadratic v-character pair is as in (5).

All g choices in a dyadic block are pooled inside the v-row coefficient. The part of g supported on v is already excluded from c_2 by chi_v(c_2)^3=0; its w,a' part gives fixed column masks. The ordinary multipliers (12) expand into fixed c-unit conditions and s-divisor extractions. Splitting the fixed-r prime valuations in E,F,g,e,f makes each extraction a fixed scalar divisor tau; the character of tau is a bounded row factor and the free smooth scale decreases. There are at most C^{omega(r)} choices. Every zero from the original character extensions remains.

Original slot assignment uses the first applicable factor in r,n_0,g,e,c_2; core assignment omits r. The row assignments are divisor-bounded, the fixed factors remain scalars, and the c_2 assignments are common divisor-bounded column coefficients. Norm dependence of D is separated at real Mellin part zero. Thus (6)--(10) apply with no slot-count power loss.

### 3. Simultaneously sum the exceptional square boundary and the w twist

Keep the physical third scale T in (0,Z], with X',Y' and slots fixed, and use Gaussian annuli
\[
 q_c q_{n_0}^3q_r^6\asymp C_l=e^lTP.
\]
Let N be the n_0 norm scale and B the E norm scale. Ignoring only nonnegative fixed-divisor reductions of Y_*, the common column scales in (10) are
\[
 C_*={C_l\over q_r^6N^3B},\qquad
 Y_*=Y'B/N.                                        \tag{17}
\]
The outside factor 1/(NB) transforms (10) into
\[
 {V\sqrt W\over NB}
       +V W^{1/4}q_r^3\sqrt{Y'/C_l}.                \tag{18}
\]
The N,B,g choices are already divisor-bounded row coefficients after separation, just as in the audited full quadratic proof. Summing their dyadic blocks costs only small powers. The first term's 1/(NB) is harmless.

Before any norm estimate, perform the joint logarithmic Fourier separation with fixed product cutoffs retained in every mode. If x,y are the normalized free-column norm variables on fixed positive annuli, choose rho_x,rho_y equal to one on the original joint support and use exactly
\[
 F_\lambda(x,y)=\rho_x(x)\rho_y(y)(2\pi)^{-2}
 \int\widehat F_\lambda(t,u)x^{it}y^{iu}\,dt\,du.
\]
The weighted L1 norm of the Fourier coefficients is bounded by a polynomial in the original nu seminorm times e^{-cl^2}(1+lambda)^{-A}, where lambda is the frequency ratio displayed in (19). Every separated c_2 and s_2 mode thus remains compactly supported; it is not an untruncated pure norm power. The same construction handles any additional compact norm-ratio variables. This exact cutoff discipline is also recorded in the user's [commit bbb8bba6, QUADRATIC_MOBIUS_GAIN.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/bbb8bba6f6a678848a270a4c950568a672cc975f/reports/20261011_qrh_selection_bridge/QUADRATIC_MOBIUS_GAIN.md), Section 4; its attribution is retained here. All arithmetic masks are fixed or pooled before this separation. The genuine e coefficient eta(e)/q_e remains, and no further Möbius cancellation in e is asserted.

The actual Fourier envelope, with all fixed smooth seminorms, is
\[
 (1+|\nu|)^C e^{-cl^2}
 \left(1+{X' V^3W^5(q_r/q_{h_0})^6q_{a'}^6\over C_l}\right)^{-A}.
                                                               \tag{19}
\]
Weighted dyadic V summation contributes
\[
 K_l^{1/3}W^{-5/3}(q_{h_0}/q_r)^2q_{a'}^{-2},
 \qquad K_l=C_l/X'.                                \tag{20}
\]
For K_l<1, the same expression may be multiplied by any fixed additional positive power of K_l, by taking A larger: the underlying frequency numerator in (19) is at least one. This retains the complete Schwartz tail rather than a hard cutoff.

Here the actual constraint h_0|w is essential. For fixed h_0, the number of w in a norm interval W is O(W/q_{h_0}), and that interval is empty unless W is at least a constant times q_{h_0}. Multiplying this count, (14), (18), and (20), the two summands are bounded respectively by
\[
 K_l^{1/3}q_{a'}^{-2}q_r^{-4}W^{-1/6},\qquad
 K_l^{1/3}\sqrt{Y'/C_l}\,q_{a'}^{-2}q_r^{-1}W^{-5/12}.
                                                               \tag{21}
\]
For precise uniformity, begin with ambient small powers of 2+Z+q_v+q_w+q_r+q_{a'}+q_e+e^{|l|}, not a presumed bounded moving modulus. Choose their exponents before summing. The strict W powers -1/6 and -5/12, the convergent a' power -2, the actual r cutoff, and arbitrarily many derivatives in the original Fourier/Gaussian envelope then absorb them into the prescribed Z^epsilon loss. All small divisor losses may be chosen below these strict W exponents. The dyadic W sums are therefore bounded, indeed they gain q_h0^{-1/6} and q_h0^{-5/12}. Summing h_0|rad r costs at most q_r^epsilon. The a' ideal sum converges. The r^{-4} ideal sum converges; the r^{-1} sum has only a logarithmic loss because the actual Gaussian annulus has
\[
 q_r\ll C_l^{1/6}
\]
whenever it is nonempty. Empty subunit physical annuli are not added. All logarithms and arbitrarily small divisor losses are absorbed using T<=Z and the Gaussian l tails.

Consequently, for any fixed M>1, the complete type (1) obeys
\[
 |S_{3,5}(T)|\ll_{\epsilon,M}(1+|\nu|)^{C_{\epsilon,M}}
 Z^\epsilon {Q\over Y'^{3/2}}
 \begin{cases}
 K^{1/3}(1+\sqrt{Y'/(TP)}),&K=TP/X'\ge1,\\
 K^M(1+\sqrt{Y'/(TP)}),&0<K\le1.
 \end{cases}                                        \tag{22}
\]
For small K, the Gaussian annuli with e^lK>=1 are absorbed by their Gaussian tail. No different coupled X',Y' scale is assumed.

### 4. Original scales and flat tails

At T=Z, K=Z^{13/16} and ZP is larger than Y'. Formula (22) gives (3). The original Q^{-1/2} factor and the actual finite subset compensation give (4), exactly as in the complete quadratic proof.

For the first Möbius operation substitute T=Z/q_b^6 into (22) with its original coefficient mu(b)kappa(b)/q_b^2, keeping all other windows and prime slots fixed. For q_b<=K_0^{1/6}, K_0=ZP/X', the two b weights are b^{-4} and b^{-1}; the second is summed only over that actual finite range. For the tail q_b>K_0^{1/6}, the small-K line gives summable b^{-2-6M} and b^{1-6M}. This proves the same bound for both exact flat probes. The redundant modulus multiplies the frequency by b^6 and hence preserves (1).

### Dependencies and boundary

The proof imports the exact source C_p and unit-factor table, the audited all-n quadratic odd branches and common-slot arrangement, the audited pure-fifth exceptional square boundary, and the genuine quadratic Hecke large sieve. The new estimates are (10) with the true VW conductor and (21), where h_0|w is counted rather than dropped.

No variable w twist was inserted into a theorem with a fixed-conductor constant: the direct large sieve sees it only in common coefficients, while smooth Poisson uses its full conductor VW. No quadratic zero-density assertion for this moving sextic twist is used. The result does not cover all remaining mixed residues or imply the full low target.

The exact local scalar and unit-factor sources are those fixed in Parts I–III; the common-column quadratic input is Part IV, the complete quadratic arithmetic is Part V, and the exceptional fifth-power boundary is Part IX.

# Part XIV. Q-conditional closure of the complete pure fifth-power type

Subsections A and B retain separate equation numbering.

## A. Density estimate and exact budget

### The fifth-power boundary support pays the full density budget

#### Result and inherited arithmetic

This note gives the analytic replacement in the already audited complete
pure fifth-power sector H=epsilon w^5a^6, with nonunit good squarefree w.
It uses input Q, with its existing user attribution: every finite-order
Hecke L-function over the original field has no zero to the right of
7/8. It does not cover a mixed or principal frequency type.

Retain the exact physical decomposition, ordinary-prime masks, original
and core slot assignments, and all original scales in
Part IX of this report. In particular physical n=r^2; the lower
6b-1 boundary is a squarefree h dividing rad(r) and w; its coefficient
is mu(h)/q_h, and its character restores the full original w family.
Write R=q_r, H=q_h, W about q_w, C=TP, K=C/X'. After the same joint
smooth separation, the column scales are C_*=C_l/R^6, Y_*<=Y', with
C_l=e^l C, and the outside r,h coefficient has modulus R^-2 H^-1.
The full Fourier/Gaussian bound is
\[
 e^{-c l^2}\left(1+\frac{W^5(R/H)^6q_{a'}^6}{C_l/X'}\right)^{-A}.
                                                               \tag{1}
\]
Crucially h|w and h|r give H<=O(W) and H<=R. No density improvement by
a factor H is asserted or used.

**Theorem (independently reviewed).** With all these exact arithmetic inputs,
the Q-conditioned complete fifth sector satisfies
\[
 I_{\rm fifth}(Z)\ll_\epsilon Z^{-63/320+\epsilon}.             \tag{2}
\]
This is below -3/16 by 3/320. The analytic derivation and its complete physical interface have both
passed independent review.

#### 1. The true sixth-family density and column

Let a=1-b, 1/8<=a<=1/2. For the actual fixed-target twist of the
squarefree sixth family w~W, one selected zero per row has the bound
\[
 R_b\ll\mathfrak X^\epsilon(1+T_0)^C W^{D(a)},                  \tag{3}
\]
where
\[
 D(a)=\begin{cases}
 \dfrac{216a^2-90a+1}{144a^2-24a-14},&1/8\le a\le1/3,\\[2mm]
 \dfrac{14a-3}{12a-2},&1/3\le a\le1/2.
 \end{cases}                                                 \tag{4}
\]
These are 1-delta_6(b) from de Faveri's Corollary 1.5. Its positive
sixth-power-free row sum permits the present squarefree restriction.
For the original fixed finite-order eta, its common values are inserted
in the detector and AFE coefficients; the half-line second moment has
AFE length O(sqrt(W)) and sixth-sieve size O(W). Thus the proof has the
same W powers and polynomial height losses. This is not an assertion
for a varying twist with an unrecorded conductor constant.

Use the already audited finite-height inverse-L lemma on each zero bin,
with its horizontal buffer, small fixed contour gap and final Q cap.
The actual Möbius column, with every common deleted Euler factor, has
bound L^-a times ambient small powers. A forced column product D_c
is extracted exactly, so the absolute sum over actual finite slots
changes this to (L/P_c)^-a, with P_c<=O(P). No slot moment saving is
needed for the present result.

The genuine smooth free column is nonprincipal and primitive conductor
is comparable to W. Thus its pointwise bound is min(S,sqrt(W)) for
S<=W, and it has arbitrary long-Poisson decay for S>=W. After taking
absolute values on the permitted zero-bin rows, the complete finite
reciprocal e sum is bounded by
\[
 \mathfrak X^\epsilon
 \left(\frac{Y_*P_c}{C_*q_f}\right)^a W^{F(a)},\qquad
 F(a)=D(a)+\frac{1-a}{2}.                                  \tag{5}
\]
Indeed L/S=C_*q_f/Y_*, each dyadic e interval has O(1) reciprocal
ideal mass, and the maximum of S^-a min(S,sqrt(W)) occurs at
S=sqrt(W). Its value is W^{(1-a)/2}. The genuine long-S tail gives no
larger term. Truncated and subunit transition ranges only decrease this
positive majorant. Consequently Y_*<=Y', P_c<=O(P), q_f>=1 give
\[
 W^{F(a)}(Y'P/C_l)^a R^{6a}.                                \tag{6}
\]
Every finite ordinary-r restriction is expanded exactly before this
argument, as in the audited physical proof. It only changes common
column masks or decreases Y_*, with a divisor-small number of choices.

#### 2. The stronger actual r support

On every nonempty original row h|w,
\[
 W^5(R/H)^6\gg R^5,                                        \tag{7}
\]
because R/H>=1. Split the exponent A in (1) into two large pieces.
One keeps the W-frequency decay; the other gives an independent
Schwartz bound (1+R^5/K_l)^-B, K_l=C_l/X'. Dyadic W summation then gives
\[
 K_l^{F/5}(H/R)^{6F/5}q_{a'}^{-6F/5}
 (1+R^5/K_l)^{-B}.                                         \tag{8}
\]
This estimate is valid for every positive K_l, including below one.
It follows from the full rapidly decaying weight, not a hard cutoff.
The bound uses h<=O(W) only to retain (7), never to divide a zero count
by H.

Throughout the interval in (4), F>5/6. For an explicit check on the
first interval, F-5/6 is the negative of
(216a^3-540a^2+225a-17)/[6(72a^2-12a-7)]. The denominator is negative,
and under a=1/8+5t/24 the numerator has positive cubic Bernstein
coefficients 199/64,161/16,83/8,6. On the second interval use
F-5/6=-(18a^2-33a+7)/[6(6a-1)]>0 directly. Thus the a' ideal sum converges.
Multiplying (8) by R^-2 H^-1 R^{6a}, and summing the squarefree divisors
h of rad(r), costs at most a divisor-small multiple of
\[
 K_l^{F/5}\sum_r R^{-3+6a+\epsilon}(1+R^5/K_l)^{-B}.          \tag{9}
\]
The ideal count is O(U) up to norm U. Put q(a)=max(6a-2,0). The sum in
(9) is at most a small power times K_l^{q(a)/5} when K_l>=1; the
borderline a=1/3 adds a logarithm. For K_l<1 its Schwartz decay gives
the same bound, on choosing B large enough. The constants can be made
uniform over a in the compact interval, after a small-power allowance.
Consequently, retaining all Gaussian annuli,
\[
 |S_{\rm fifth}(T)|\ll\mathfrak X^\epsilon(1+|\nu|)^C
 \frac{Q}{Y'^{3/2}}\max_{1/8\le a\le1/2}
 (TP/X')^{[F(a)+q(a)]/5}(Y'/T)^a.                           \tag{10}
\]
All other original small divisor losses fit the strict a' summability
and the arbitrarily strong Fourier/Gaussian decay. In particular the
small-K region is not discarded.

#### 3. Exact exponent and first-decompletion check

Let alpha in [0,1/6] denote the original finite-compensation subset
length, to avoid confusion with the zero-bin parameter a. At T=Z,
\[
 K=Z^{13/16},\quad Y'/Z=Z^{-25/48-\alpha}.
\]
After the actual Q^-1/2 normalization and the original finite
compensation, (10) has exponent at most
\[
 G(a)=-\frac{29}{96}+\frac{13}{80}[F(a)+q(a)]
                           -\frac{25}{48}a,                 \tag{11}
\]
since the remaining alpha term is -alpha a<=0.

Here are fully rational checks of the maximum. On [1/8,1/3],
\[
 G'(a)=-\frac{p(a)}{480(72a^2-12a-7)^2},
\]
\[
 p(a)=1498176a^4-499392a^3-401328a^2+172104a-10877.
\]
Under a=1/8+5t/24, its Bernstein coefficients of degree four are
240361/64, 220293/32, 54167/8, 15921/4, 1899. They are all positive,
so G strictly decreases there. At a=1/8,
\[
 G(1/8)=-16641/75520<-63/320.
\]
On [1/3,1/2] the simpler factorization is
\[
 G(a)+63/320=
 \frac{(2a-1)(1074a-101)}{960(6a-1)}\le0.                    \tag{12}
\]
Equality holds at a=1/2, interpreted through its buffered initial bin.
This proves the exponent -63/320 after arbitrarily small losses, using
the independently reviewed exact physical interface in the opening.

For the first Möbius scale operation keep every original X',Y' and
slot window fixed, and put T=Z/q_delta^6 with its actual coefficient
of modulus q_delta^-2. Write
\[
 \beta(a)=\frac{F(a)+q(a)}5-a.
\]
One has beta(a)>=-1/10. For a<=1/3 this follows from
\[
 \beta(a)+1/10=
 -\frac{(3a-1)(264a^2-76a-13)}{10(72a^2-12a-7)}\ge0;
\]
the quadratic numerator factor and denominator are both negative on
this interval. For a>=1/3,
\[
 \beta(a)=\frac{a(6a-5)}{10(6a-1)},\qquad
 \beta'(a)=\frac{36a^2-12a+5}{10(6a-1)^2}>0,
\]
and beta(1/3)=-1/10. Hence the delta series is dominated by
\[
 \sum_\delta q_\delta^{-2-6\beta(a)+\epsilon}
 \le\sum_\delta q_\delta^{-7/5+\epsilon}<\infty.              \tag{13}
\]
The original frequency lift by delta^6 preserves the pure fifth core.
This proves the same analytic transfer for each exact first flat, with
uniform all-scale control rather than an assumed large-T range.

#### Sources and verification scope

The density is the n=6 specialization of de Faveri, *Optimal large sieve
for fixed order characters*, Corollary 1.5 and its proof:
https://arxiv.org/html/2610.04045v1 . The exact all-n/slot/first-flat
arithmetic is inherited from the already independently reviewed
Part IX of this report; the finite-height inverse proof is the
already reviewed genuine Möbius-column lemma. Input Q retains its
original user-source attribution and source-audit versus independent
rerun distinction. The physical transfer and exponent have passed independent review.
The theorem controls this complete pure-fifth type, not the full R4
expression or the Riemann Hypothesis.

Input Q is attributed to the user's [FORMAL_INPUT_Q](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/52ee48d3e2e4c5b0beeb3e4880eca86fb2208ce1/reports/20261011_qrh_selection_bridge/FORMAL_INPUT_Q.md). This conditional consequence does not claim an independent rerun of that formal build.

## B. Complete physical interface

### The exact physical interface for the pure-fifth Möbius improvement

This is the arithmetic companion to the complete pure-fifth density calculation. It uses the already audited pure-fifth sector H=epsilon w^5a^6, w good squarefree nonunit, and its exact ordinary/exceptional square decomposition. It verifies that the analytic estimate is for the original whole type, rather than an unmarked n=1 model.

Fix the original subset parameters X',Y',P,Q and a Gaussian scale 0<T<=Z. Put C_l=e^l TP and K_l=C_l/X'. Every nonzero physical n is r^2. For h_0|rad r at its unique 6b-1 boundary, the exact formula has
\[
 h_0\mid w,\quad a=(r/h_0)a',\quad(h_0,a'cs)=1,
 \qquad {\kappa(r)\mu(h_0)\over q_r^2q_{h_0}}.
                                                               \tag{1}
\]
The ordinary fixed-prime multiplier is exactly
\[
 \prod_{p\mid r,\ p\nmid h_0}
 1_{p^2\nmid s}[1-q_p^{-1}1_{p\nmid c,p\nmid s}],
\]
The boundary and ordinary prime choices are disjoint. A boundary prime may still divide r/h_0 when its exponent in r exceeds one; it is nevertheless excluded from this ordinary product. The effective frequency is Hh_0/r^6, and the restored h_0 unit phases give the original full w character in both free columns. No factor is evaluated at a forced nonunit.

After fixing the exact ordinary-mask branch, and using its fixed s-divisor extractions, the common free lengths satisfy
\[
 L={C_l\over q_r^6Gq_e},\qquad
 S={Y_*\over Gq_eq_f},\qquad0<Y_*\le Y'.             \tag{2}
\]
Every joint logarithmic Fourier mode retains fixed compact product cutoffs in these free variables, with the original Gaussian/Schwartz envelope. The e coefficient eta(e)/q_e is retained. The original slots are assigned to the first applicable factor r,g,e,c_2, or to g,e,c_2 for the core marker. The r/e assignments are fixed scalars, the g assignments are bounded divisor row weights, and the remaining c_2 assignments are true selected-prime conditions in the Möbius column.

For a rightmost-zero bin b=1-alpha, 1/8<=alpha<=1/2, let D_6(b) be the audited sixth-family density exponent. There are at most ambient^epsilon W^{D_6(b)} rows with w~W in that bin. The original fixed Q input caps the bins at b=7/8. The primitive inverse-L rectangle bound applies to the genuine mu(c_2)eta(c_2)chi_w(c_2)/q_c2 column.

If a selected product D_c of norm about P_c is forced into c_2, extract it exactly before any bound. Its outside factor is mu(D_c)eta(D_c)chi_w(D_c)/q_Dc and its new column scale is L/q_Dc; its coprimality Euler factors are included in the actual imprimitive modulus. On the bin's contour this gives L^{-alpha}q_Dc^{alpha-1}. Summing over the actual fixed slots gives at most ambient^epsilon (L/P_c)^{-alpha}. The count is the elementary reciprocal-prime-slot mass, not an independence assertion. We use P_c<=O(P). All moving common mask primes remain in the imprimitive modulus; they are never made part of a fixed S.

The free s column has the actual nonprincipal primitive character of conductor about W, so its genuine pointwise smooth estimate is min(S,sqrt W), with rapid decay for S>=W. Consequently the full finite e sum, including every true inclusion-exclusion term, is bounded by
\[
 \mathrm{ambient}^{\epsilon}
 \left({Y'P_c q_r^6\over C_l}\right)^{\alpha}W^{F(\alpha)},
 \qquad F(\alpha)=D_6(1-\alpha)+(1-\alpha)/2.        \tag{3}
\]
Indeed L/S=C_l q_f/(q_r^6Y_*), and the maximum of S^{-alpha}min(S,sqrt W) is W^{(1-alpha)/2}. Each actual dyadic e block has bounded reciprocal ideal mass. An empty free-column annulus is never inserted. The smaller scale Y_* can be increased to Y' in this positive estimate. Every original mask and phase was retained until this step.

Multiplying (3) by (1), the exact positive r,h_0 weight before the full Fourier tail is
\[
 (Y'P_c/C_l)^{\alpha}\,
 q_r^{6\alpha-2}q_{h_0}^{-1}W^{F(\alpha)}.          \tag{4}
\]
The frequency envelope is
\[
 e^{-cl^2}\left(1+{W^5(q_r/q_{h_0})^6q_{a'}^6\over K_l}\right)^{-A}.
                                                               \tag{5}
\]
Crucially W>=q_h0 up to the dyadic constants, and hence the frequency numerator is at least a fixed constant times q_r^5 q_a'^6. Thus the genuine Schwartz tail cuts the r norm at K_l^{1/5}, not merely at the longer physical nonempty-column limit C_l^{1/6}.

Dyadic W summation in (4)--(5), preserving W>=q_h0, yields
\[
 K_l^{F/5}q_{a'}^{-6F/5}
 q_r^{6\alpha-2-6F/5}q_{h_0}^{6F/5-1}
 \min\{1,(K_l/(q_r^5q_{a'}^6))^A\},               \tag{6}
\]
after increasing the original derivative order. The finite h_0 choices can be bounded using h_0<=r and F>5/6. This gives precisely the r power 6alpha-3, and the a' power -6F/5 is strictly below -1 throughout the compact bin interval. All original ordinary-mask counts are divisor-small and are absorbed using the strict summability or actual Schwartz cutoff. There is no replacement of h_0|w by a false density-row factor 1/h_0.

It follows that the entire physical type, including both original/core markers, is bounded by the common Q/Y'^{3/2} times
\[
 Z^\epsilon\max_{1/8\le\alpha\le1/2}
 \left({Y'\over T}\right)^\alpha
 \left({TP\over X'}\right)^{[F(\alpha)+(6\alpha-2)_+]/5}.
                                                               \tag{7}
\]
The analytic companion verifies the exact sixth-density exponent, the finite-bin small losses, the maximum -63/320 after normalization, and the uniform scale exponent beta>=-1/10. All moving norms are included first in the ambient parameter and only then absorbed by the complete Fourier/Gaussian tails and the strict a' and r margins.

Finally the first flat operator substitutes T=Z/q_delta^6 and retains its actual coefficient mu(delta)kappa(delta)/q_delta^2 while X',Y' and slots stay fixed. In (7) this gives an absolute delta power at most -7/5. The redundant frequency lift multiplies H by delta^6 and preserves the pure-fifth core and unit. Thus both exact first-flat probes obey the same improved bound, with no use of an unproved coupled-scale theorem.

# Part XV. Exact cubic rational-slot moments

## Rational selected-prime multipliers in the genuine cubic column

### Scope and result

This note supplies a high-moment bound for the actual selected-prime
Euler multiplier, including its prime-square branches and every zero
mask. It does not assert a complete physical low estimate. The input is
the cube-free cubic large sieve; input Q is not needed for this lemma.

Let K=Q(sqrt(-3)), q_a=Na, and let w range over good cube-free ideals
with M<=q_w<=2M, M>=2. Write psi_w(c)=chi_c(w^2), in the original
primary convention. Its complex conjugate is equally permitted. The
fixed finite ray partitions identify this with the cubic Hecke family
in the large sieve below, up to common coefficient twists and bounded
row factors. No moving prime is added to the fixed excluded set S.

Fix a finite-order character eta and J disjoint prime-slot sets. Slot i
is supported in P_i<=q_p<=C P_i, P_i>=2, with fixed C. A selected D
has one good prime from each slot; put P=product_i P_i. Let |z_D|<=1
be arbitrary common coefficients. Fixed common coprimality restrictions
on the selected products are allowed. All constants may depend on J,
the fixed ray data, and the indicated fixed moment order.

For s=sigma+it with 1/2<=sigma<=1 define
\[
 E_w(s)=P^{s-1}\sum_D z_D
 \prod_{p\mid D}\frac{\eta(p)\psi_w(p)q_p^{-s}}
                         {1-\eta(p)\psi_w(p)q_p^{-s}}.       \tag{1}
\]
Signs, fixed phases, bounded common smooth slot weights and their
Mellin phases can be included in z_D. Products over zero slots equal 1.
Every factor is zero if the corresponding selected prime divides w.

**Proposition.** For every fixed integer k>=1 and epsilon>0,
\[
 \boxed{\sum_{w\asymp M}|E_w(s)|^{2k}
 \ll_{\epsilon,k,J}(MP)^\epsilon
 \left(1+\frac M{P^k}+\frac{M^{2/3}}{P^{k/3}}\right).}        \tag{2}
\]
The estimate is uniform in t and the stated closed sigma range. It
remains valid after any restriction of the positive row sum. In
addition, uniformly in the same parameters,
\[
 \sup_w|E_w(s)|\ll_J1.                                      \tag{3}
\]
The factors (MP)^epsilon can accommodate any fixed number of original
smooth seminorms. Neither (2) nor (3) permits arbitrary coefficients
inside a different signed free-s column.

### 1. Exact three-cycle identity

For x in {0,1,omega,omega^2},
\[
 \frac{\eta xq^{-s}}{1-\eta xq^{-s}}
 =\frac{\eta xq^{-s}+\eta^2x^2q^{-2s}
               +\eta^3x^3q^{-3s}}{1-\eta^3q^{-3s}}.          \tag{4}
\]
When x=0 both sides vanish; when x is a unit cubic root, multiply the
numerator by 1-eta x q^{-s}. Thus (4) preserves the zero mask exactly.
The denominator is independent of w and its modulus is at least
1-2^(-3/2)>0. The third numerator term contains x^3, which is the unit
mask, not the constant 1 on every row.

For one occurrence of a prime in slot i, branch j in {1,2,3} of (4),
after the normalization in (1), has coefficient of size
\[
 O(P_i^{-1-(j-1)\sigma}).                                  \tag{5}
\]
Its character factor is psi_w(p)^j. This coefficient bound is uniform
in the Mellin height. Taking absolute values in (1), counting at most
O(P_i) primes per slot, proves (3). No prime number theorem is needed.

### 2. Repeated primes and sparse cube-free columns

Expand E_w(s)^k, including the choices of the three branches in every
one of its kJ occurrences. For each slot partition its k occurrences
according to equality of primes. There are finitely many patterns,
depending only on k,J. Work with one such pattern and branch choice.

For a distinct prime block in slot i let m>=1 be its number of
occurrences and n the sum of their branch exponents. Thus m<=n<=3m.
Write r=n mod 3, with r in {0,1,2}. Let r_{i,0}, r_{i,1}, r_{i,2}
count the distinct blocks of the respective residues, and put
\[
 t_i=r_{i,1}+r_{i,2},\qquad
 u_i=r_{i,1}+2r_{i,2},\qquad J_i=\sum_{\text{blocks}}n.
\]
For this slot sum m=k and k<=J_i<=3k. The common coefficient has
modulus at most a constant times
\[
 P_i^{-k-\sigma(J_i-k)}.                                   \tag{6}
\]
All actual complex phases and original z_D correlations are retained
inside this common coefficient.

Freeze first all primes with residue r=0. Their character product is
exactly a row coprimality mask. Keep this mask in the positive row norm,
then enlarge the row set when applying the sieve. Their exclusion from
the other primes is a common column restriction. There are at most
O(product_i P_i^{r_{i,0}}) choices of the frozen primes.

The remaining column ideal C is the cube-free product of residue-one
primes and the squares of residue-two primes. Its norm is comparable to
\[
 B=\prod_i P_i^{u_i},                                      \tag{7}
\]
and its number of possible values is only
O(product_i P_i^{t_i}). In particular a prime-square branch has norm
scale P_i^2 but only O(P_i) possible values. The finite pattern fixes
multiplicities, so each column has bounded representation multiplicity.

The cube-free cubic large sieve gives
\[
 \Theta_3(M,B)\ll_\epsilon(MB)^\epsilon
               [M+B+(MB)^{2/3}].                           \tag{8}
\]
Using the actual sparse coefficient mass in (8), and Minkowski for
the frozen primes, bounds the row norm of this pattern by
\[
 (MP)^\epsilon\,[\sqrt M+\sqrt B+M^{1/3}B^{1/3}]
 \prod_i P_i^{r_{i,0}+t_i/2-k-\sigma(J_i-k)}.                \tag{9}
\]
The column B=1 is interpreted directly and satisfies the same bound.
All norms here are of the k-th power, in ell^2(w).

### 3. Every local exponent is paid

It suffices to bound each of the three terms in (9). Because n>=m,
its exponent is largest at sigma=1/2. For a prime block define
h_0=1 and h_1=h_2=1/2. Its contribution from the product in (9) is
at most h_r-(m+n)/2.

For the sqrt(M) term one has
\[
 h_r-(m+n)/2\le-m/2.                                      \tag{10}
\]
Indeed h_0=1 and residue zero forces n>=3; for nonzero residue n>=1.
For the sqrt(B) term,
\[
 h_r+r/2-(m+n)/2\le0.                                    \tag{11}
\]
The smallest pairs (m,n) for residues 0,1,2 are respectively bounded
below by (1,3), (1,1), (1,2), which verify (11).
Finally, for the mixed term,
\[
 h_r+r/3-(m+n)/2\le-m/6.                                  \tag{12}
\]
Equivalently h_r+r/3<=n/2+m/3. The three left sides are 1,5/6,7/6;
the corresponding minimum right sides are 11/6,5/6,4/3.

Summing over the k occurrences in each slot, (10)--(12) turn (9) into
\[
 \|\text{one pattern}\|_2\ll(MP)^\epsilon
 \left[M^{1/2}P^{-k/2}+1+M^{1/3}P^{-k/6}\right].             \tag{13}
\]
There are only finitely many patterns. Sum them by Minkowski and
square. The identity ||E^k||_2^2=sum_w|E_w|^(2k) proves (2), after
shrinking the input epsilon. Thus no prime-square branch was falsely
treated as a same-length squarefree column.

### 4. Restricted rows and the decisive cubic bin

Let a>=0, let a row set have cardinality at most R_0=M^D, and let
B_w be an actual second factor for which a 2l-th moment is available.
For fixed k,l with 1/(2k)+1/(2l)<=1, Holder gives
\[
 \sum_{w\in\mathcal E}|E_wB_w|
 \le R_0^{1-1/(2k)-1/(2l)}\|E\|_{2k}\|B\|_{2l}.             \tag{14}
\]
The analogous pointwise-B bound has R_0^{1-1/(2k)} instead. Hence the
extra factor relative to these respective unmarked restricted-row
bounds, after restoring the actual column-slot length factor P^a, is
at most
\[
 (MP)^\epsilon P^a M^{-D/(2k)}
 \left[1+\frac M{P^k}+\frac{M^{2/3}}{P^{k/3}}\right]^{1/(2k)}.
                                                                    \tag{15}
\]
This uses the upper row count R_0 consistently; it does not require
that the actual set have exactly R_0 rows or be independent of B.

At the decisive cubic zero bin a=1/6, D=2/3, let p=log(P)/log(M).
The exponent of M in (15), apart from epsilon, is the maximum of
\[
 \frac p6-\frac1{3k},\qquad
 \frac1{6k}-\frac p3,\qquad 0.                             \tag{16}
\]
It is zero whenever
\[
 \frac1{2k}\le p\le\frac2k.                               \tag{17}
\]
In particular P=M^(1/6) is covered by k=3. For every fixed epsilon,
(3) handles P<=M^epsilon. For epsilon<p<=2 select a k from a finite
set depending only on epsilon, using the covering (17). For p>=2
use k=1. Consequently the optimized factor (15), with the small-P
alternative (3), is bounded by
\[
 (MP)^\epsilon\left[1+P^{1/6}M^{-1/3}\right].                \tag{18}
\]
The moment order is never allowed to grow with M. Finitely many moment
bounds suffice after the desired epsilon is fixed. This endpoint
corollary is only an input to a separate complete-bin/physical budget.

### Source and family matching

Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
Theorem 1.1, arXiv:2610.04045v1 (2 October 2026):
https://arxiv.org/html/2610.04045v1 .
Its definition (1.2) and theorem explicitly allow both indices to be
cube-free. For n=3 its four-term bound reduces to (8). The underlying
Eisenstein primary/ray identification is the same one used in the
already audited complete cubic dual calculation; conjugating the whole
character kernel preserves the same positive operator bound. Fixed
ray factors are partitioned before applying (8), rather than changing
the character family as the selected primes move.

# Part XVI. Q-conditional negative bound for the complete cubic type

## A negative bound for the complete cubic sector from true slot moments and dual smooth moments

### Result and scope

Use the original scales, units, fixed ray classes and physical definitions of Part VI of this report, and the actual cubic Möbius column identified in Part XII of this report. All frequencies H=epsilon w^2a^6 with w nonunit cube-free, every physical n, every original selected-prime slot and zero extension are retained. Both the original and core markers, and each one's exact first Möbius-decompleted probe, are included.

The input **Q** is the user's fixed zero-free half-plane Re(s)>7/8 for finite-order Hecke L-functions over Q(sqrt(-3)); attribution and verification scope are unchanged. The cube-free cubic sieve, the already reviewed fixed-twist zero-density/finite-height inverse argument, and the independently reviewed rational-slot moment lemma are used below.

**Theorem (independently reviewed).** The complete cubic sector of the actual normalized finite compensation satisfies
\[
 \boxed{I_{\rm cub}(Z)\ll_\varepsilon Z^{-11/2304+\varepsilon}.}  \tag{1}
\]
The polynomial dependence on the original Mellin height is absorbed by its original outer weight. This is a negative bound for one complete core type. It remains 421/2304 weaker than the full low target -3/16 and leaves the other core types and the whole-probe high comparison unresolved.

Unlike the preceding 2/45 estimate, this argument preserves the selected-prime phases inside the genuine inverse column and uses Poisson duality before taking a high smooth-column moment. The small cube-free-index range is estimated separately with its complete physical-square and sixth-power multiplicities.

### 1. Retained arithmetic and a compact common-coefficient separation

Write
\[
 X'\asymp Z^{17/48-d},\quad Y'\asymp Z^{23/48-d},\quad
 P\asymp Z^{1/6-d},\quad Q=q_bX'Y',\quad0\le d\le1/6.
                                                               \tag{2}
\]
The audited full cubic completion uses n=n_0r^2, n_0=F_2E_4 with F_2|v_1, E_4|v_2 when w=v_1v_2^2. It retains c=E_4g e c_2, s=E_4g j^2 e f s_2, the exact n_0 factor q_{n_0}^{-3/2}, the physical-square factor q_r^{-2}q_k^{-1}, and the full-frequency lift H=r^6 epsilon w^2(a')^6. The only Ramanujan factor is phi(g).

Put N about q_{n_0}, B about q_{E_4}, G about q_g. In the Gaussian annulus indexed by l,
\[
 U_l=e^l TP/q_r^6,\qquad
 L=\frac{U_l}{N^3BGq_e},\qquad
 S=\frac{Y'}{BGq_j^2q_eq_f}.                         \tag{3}
\]
Here 0<T<=Z changes only the Gaussian row scale. The complete shared-divisor, fixed-ray and original prime-slot organization is as in the audited proof. In particular the c_2 column retains the exclusions from h,e,a'; no prime of the physical square-layer mask is omitted from the deleted Euler factors. The w part of a moving divisor is enforced by the original character zeros.

A useful precision about separation is retained throughout. On each normalized c,s annulus choose fixed compact cutoffs rho_c,rho_s equal to one on the support of the actual joint smooth kernel. Fourier inversion in the two log variables is then multiplied by rho_c rho_s. Every separated mode is still the product of two genuinely compact smooth factors, not a pair of uncut powers. The coefficient norm is integrable with the original Gaussian and Fourier envelope
\[
 (1+|\nu|)^C e^{-c l^2}
 (1+X'M^2q_{a'}^6/U_l)^{-A},\qquad q_w\asymp M.      \tag{4}
\]
All Gaussian slot separation remains on zero real Mellin part. This preserves both the genuine Möbius contour shift and the compact smooth Poisson estimate used below.

### 2. A common smooth column and its genuine eighth moment

Let B_w(S) be the remaining common smooth/ray s_2 column, with w cube-free of norm about M. Its good primitive conductor is rad(w), not w. Split its full primitive conductor norm into dyadic C blocks; C<=C_0 M, with only fixed bad-prime data in C_0.

For every fixed integer k>=1, the direct moment follows by raising the sum to the k-th power and applying the cube-free cubic sieve to its common convolution column, of norm length about S^k. Removing cube factors has the same convergent three sums as in the audited all-power cubic lemma. Thus
\[
 \|B(S)\|_{2k}\ll_\varepsilon(MS)^\varepsilon
 [M^{1/(2k)}\sqrt S+S+M^{1/(3k)}S^{5/6}].            \tag{5}
\]
The coefficients of the product column are divisor-bounded, not assumed squarefree. All restrictions induced by its cube factor are enlarged only in positive row norms.

Actual primitive Poisson summation gives a dual smooth column of norm length C/S and amplitude S/sqrt(C), with a unit root-number factor depending only on the row. After a common Mellin separation of the normalized conductor ratio, that row phase has no effect on moments and all remaining coefficients are common. For a nonradial weight, also expand its angular variable in Fourier modes: rotation by the complex conductor generator contributes only exp(i m arg(f_w)), a pure row phase. The original smooth angular decay absorbs the polynomial mode seminorms. Rapid dual tails are included by dyadic summation. Consequently
\[
 \|B(S)\|_{2k}\ll_\varepsilon(MS)^\varepsilon
 [M^{1/(2k)}\sqrt S+\sqrt C
                 +M^{1/(3k)}C^{1/3}S^{1/6}].        \tag{6}
\]
For C/S<1, do not apply a large sieve with a subunit column length. The actual nonzero Poisson tail, with tail order at least one, bounds each row by O(sqrt(C)). Its 2k-th row norm is at most M^{1/(2k)}sqrt(C)<=M^{1/(2k)}sqrt(S), already covered by the first term of (6). The common dual-moment calculation above is used only when C/S>=1.

Fixed bad-ray classes and smooth seminorms change only constants and polynomial height factors. Replacing C by C_0M in this upper bound is legitimate; it does not pretend that the primitive conductor equals the cube-free index. The positive row restriction to a conductor block is retained before enlargement in the sieve.

For k=4, taking the minimum of (5) and (6), one obtains the following convenient eighth-moment envelope, with harmless small powers:
\[
 \|B(S)\|_8\ll
 \begin{cases}
 M^{1/8}S^{1/2},&1\le S\le M^{1/8},\\
 M^{1/12}S^{5/6},&M^{1/8}\le S\le M^{1/2},\\
 M^{5/12}S^{1/6},&M^{1/2}\le S\le M^{7/8},\\
 M^{1/8}S^{1/2},&M^{7/8}\le S\le M.
 \end{cases}                                        \tag{7}
\]
The original all-scale pointwise estimate |B_w(S)|<=C min(S,sqrt(M)) is also available on nonempty physical annuli. For S>=M the true long-Poisson estimate supplies arbitrary decay in S/M. Small physical S is either empty or comparable to a fixed positive constant.

### 3. The exact selected-prime rational multiplier

For a fixed zero bin b in [1/2,7/8], the already reviewed density bound gives at most mathfrak X^epsilon M^{D(b)} rows, with
\[
 D(b)=\begin{cases}
 1,&1/2\le b\le2/3,\\
 7/3-2b,&2/3\le b\le5/6,\\
 19/6-3b,&5/6\le b\le7/8.
 \end{cases}                                        \tag{8}
\]
All fixed twists remain fixed common coefficients. On a common contour a fixed bin-width to the right of those rows' buffered low-height zeros, the actual reciprocal L-function and the fixed deleted Euler factors are subpower-bounded. The bin-width, detector-height and seminorm losses are chosen smaller than the final epsilon. Input Q caps the bins; no evaluation occurs on a possible boundary zero.

Let P_c be the product scale of those actual slots assigned to c_2. Their original overline{eta(D_c)} factors cancel the eta numerators introduced by forcing D_c into the Möbius column. The exact remaining multiplier is a sum of products
\[
 \frac{-\overline{\psi_w(p)}q_p^{-s}}
       {1-\eta(p)\overline{\psi_w(p)}q_p^{-s}},       \tag{9}
\]
with the original common slot weights and exclusions p not dividing the fixed column mask. All columns and masks refer only to original good ideals; already deleted bad Euler factors are not reintroduced. Formula (9) is obtained by extracting each forced prime in the Dirichlet series of the true Möbius column. It is holomorphic on the shifted positive real lines.

Normalize this multiplier by P_c^{s-1} and call the result E_w(s). The independently reviewed rational-slot lemma gives, for every fixed k>=1,
\[
 \sum_{w\asymp M}|E_w(s)|^{2k}
 \ll_\varepsilon(MP_c)^\varepsilon
 [1+M/P_c^k+M^{2/3}/P_c^{k/3}],\qquad\sup_w|E_w(s)|\ll1.
                                                               \tag{10}
\]
It includes the prime-square branches and the cubic unit masks of the exact identity
x/(1-eta xq^{-s})=(x+eta x^2q^{-s}+eta^2x^3q^{-2s})/(1-eta^3q^{-3s}); x^3 is a unit mask, not identically one. Its repeated-prime proof uses the actual sparse cube-free column mass. No same-length squarefree shortcut is used for prime-square branches.

For a row set of size at most M^D, Holder with (10) and either (7) or a pointwise B bound introduces, relative to the corresponding unmarked restricted-row estimate, at most
\[
 F_k=P_c^{1-b}M^{-D/(2k)}
 [1+M/P_c^k+M^{2/3}/P_c^{k/3}]^{1/(2k)}.            \tag{11}
\]
This counts the actual prime multipliers rather than taking their phases in absolute value. Arbitrary positive restrictions and divisor-bounded row weights are permitted.

### 4. All zero bins have no slot-power loss when P_c<=sqrt(M)

Write p=log(P_c)/log(M), and a=1-b. Apart from small powers, the exponent in F_k is the maximum of
\[
 ap-\frac D{2k},\qquad
 \frac{1-D}{2k}+(a-1/2)p,\qquad
 \frac{2/3-D}{2k}+(a-1/6)p.                         \tag{12}
\]
Suppose 0<=p<=1/2.

- If 1/2<=b<=2/3, D=1 and k=1 makes all three quantities nonpositive.
- If 2/3<=b<=5/6, choose q=kp in [1/2,1]. Substitution of D=7/3-2b makes all three quantities nonpositive.
- If 5/6<=b<=7/8, choose q=kp in [3/2,2]. Substitution of D=19/6-3b again makes all three nonpositive.

Both required q intervals are covered by integers k when 0<p<=1/2: use ceil(1/(2p)) or ceil(3/(2p)), respectively. To keep moment orders genuinely fixed, first handle p<=epsilon_0 with the pointwise part of (10), costing at most M^{epsilon_0/2}; for p>=epsilon_0 only finitely many k are used. Empty column slots have multiplier one and require no moment. Fix epsilon_0 sufficiently small before all applications.

Hence, uniformly in every bin, the actual marked restricted-row sum admits both bounds
\[
 \sum_{w\text{ in bin}}|E_w^{\rm raw}(s)B_w(S)|
 \ll\mathfrak X^\varepsilon
 \min\{M^D\min(S,\sqrt M),\ M^{7D/8}\|B(S)\|_8\},             \tag{13}
\]
provided P_c<=C sqrt(M), with fixed constants absorbed into the small loss. The raw factor includes the restoring P_c^{1-b} already paid by (11). This assertion is a bound after inverse-contour control; the original inverse L-factor remains present until that control is justified.

### 5. The entire finite e sum with the eighth-moment envelope

From (3), L/S=U_lq_j^2q_f/(N^3Y'). There is now no column-slot length loss. Multiply (13) by the true inverse-column factor L^{b-1}. The finite reciprocal e sum is bounded by its positive dyadic integral in dS/S, retaining compact support at every mode. Equation (7) and the pointwise bound yield
\[
 \sum_e\frac1{q_e}\sum_{w\text{ in bin}}
 |A_w^{\rm marked}(L)B_w(S)|
 \ll\mathfrak X^\varepsilon
 \left(\frac{U_lq_j^2q_f}{N^3Y'}\right)^{b-1}
 M^{J_8(b)},                                        \tag{14}
\]
where
\[
 J_8(b)=\max\left\{
 \frac{7D(b)}8+\frac b2,
 \frac{D(b)(3+b)}4+\frac{3b-1}4\right\}.             \tag{15}
\]

For a full verification, below S=sqrt(M) every envelope in (13), after multiplication by S^{b-1}, is nondecreasing. At S=sqrt(M) the exponent is the first term in (15). Between sqrt(M) and M^{7/8}, the moment exponent is 7D/8+5/12+(b-5/6)log(S)/log(M); the pointwise envelope is decreasing. Their possible intersection lies at or beyond M^{7/8} since D>=13/24>1/2. In the last interval, the increasing moment bound and decreasing pointwise bound meet at
\[
 S=M^{(3+D)/4};                                     \tag{16}
\]
its exponent is the second term in (15). Beyond M there is the true rapid Poisson tail. These checks prove (14), also when its apparent transition lengths lie outside the finite physical e range. All endpoint logarithms enter mathfrak X^epsilon.

At the decisive b=5/6 one has D=2/3, J_8=73/72 and S=M^{11/12}. Neither just retaining the dual cubic term nor evaluating the convenient S=M block would give this correct worst exponent.

### 6. High cube-free indices and all physical tails

First restrict to M>=Z^{1/3}, up to fixed annulus constants. Since P_c<=C P<=C Z^{1/6}, the hypothesis of §4 holds. The n_0 factor N^{-3/2} in the actual completion turns the N contribution in (14) into N^{3/2-3b}, which is nonpositive. The complete n_0,E_4,g divisor sums and all slot assignments are handled inside the common row coefficient, exactly as in the audited all-n proof. Fixed j,f denominators can be bounded by one.

Summing weighted M annuli against (4), then all a', gives (U_l/X')^{J_8/2}; the a' sum has exponent -3J_8<-1 uniformly. The physical r power is
\[
 q_r^{4-6b-3J_8(b)},                                \tag{17}
\]
and is uniformly strictly below -1, so every h,j choice and divisor-small loss is summable. Gaussian l tails remain complete. The exact first Möbius scale operation has the same power (17) in its external divisor and preserves the cubic core. Thus this high-index argument covers original/core and both flat probes.

At T=Z, Q^{-1/2} and the finite original compensation cancel the d/2 terms. Since ZP/X'=Z^{13/16} and ZP/Y'=Z^{11/16}, the normalized exponent is
\[
 E_8(b)=-\frac{29}{96}+\frac{13}{32}J_8(b)
                              +\frac{11}{16}(b-1).  \tag{18}
\]
For b<=2/3 the first term in (15) dominates and E_8 is increasing. On 2/3<=b<=5/6 the two candidates in (15) have derivatives -5/4 and -1/6-b. Each gives a strictly increasing expression (18). On 5/6<=b<=7/8 the second candidate dominates and its derivative is (D-6-3b)/4; (18) is strictly decreasing, already with derivative -83/768 at 5/6. Therefore
\[
 \max_{1/2\le b\le7/8}E_8(b)=E_8(5/6)=-11/2304.     \tag{19}
\]
The positive enlargement of the final M sum to all M is made only after (14) has been proved for high M; it does not apply a slot moment outside its permitted range.

### 7. Small cube-free indices: retain r and a multiplicities

For M<=Z^{1/3}, use the already proved 2/45 method, including its safe absolute column-slot price. Denote its exponent by
\[
 J_0(b)=\frac{D(b)(2+3b)}5+\frac{3+2b}{10},\qquad
 C(b)=\max\{1,5-6b\}.                               \tag{20}
\]
Before summing the physical square variable and sixth-power variable, write q_r about R and q_{a'} about A. Their complete dyadic counts give the weight
\[
 A R^{5-6b}
 \left(1+\frac{M^2A^6R^6}{e^l Z^{13/16}}\right)^{-N}.          \tag{21}
\]
Here R^{5-6b} includes the actual q_r^{-2}, the inverse-scale power q_r^{6(1-b)}, and the number of ideals r in its dyad. A is the actual number of sixth-power factors in its dyad. Dropping these two multiplicities would give an invalid low-M estimate.

For fixed M, dyadic A,R summation in (21) is bounded, with logarithms, by
\[
 \left(\frac{e^l Z^{13/16}}{M^2}\right)^{C(b)/6}.     \tag{22}
\]
For an effective ratio below one, increase N and retain the original rapid tail. Equation (22) follows by allocating the available product AR to whichever of the exponents 1 and 5-6b is larger. The exact external Möbius divisor has the same exponent as R and merely adds another dyadic logarithm; its full frequency lift is included in the same product constraint.

Since J_0(b)-C(b)/3>0 uniformly, summing M<=Z^{1/3}, and then the Gaussian annuli, gives normalized exponent at most
\[
 E_{\rm small}(b)=
 -\frac{29}{96}+\frac{J_0(b)}3+\frac{25}{48}(b-1)
                              +\frac{7C(b)}{288}.   \tag{23}
\]
The original rescaling contributes an additional d(b-1)<=0 and may be discarded in this upper bound. The piecewise formulas show (23) is increasing up to 5/6 and decreasing thereafter. Its maximum is
\[
 E_{\rm small}(5/6)=-13/1440<-11/2304.               \tag{24}
\]
This proves that the range where P_c may exceed sqrt(M) is harmless for (1), without claiming globally lossless slot control.

### 8. Justification and remaining burden

All arithmetic zero masks, shared-prime conditions, fixed deleted Euler factors and finite slot priority assignments are retained from the audited complete-cubic identity. The moment order varies only within a finite set after epsilon is fixed; it never increases with Z. The finite-height inverse argument uses an ambient arithmetic size including unbounded physical and Gaussian/Fourier tails. Its small powers are absorbed into the strict a',r and external Möbius summability and the original rapid decay.

The two ranges §§6--7 establish the theorem. The eighth-moment argument, final complete physical budget and rational-slot lemma have all passed independent review. This is a bound for one complete nonprincipal cubic type, not the full signed R4 expression, and it supplies no lower bound or resonance counterexample.

#### Mathematical dependencies

- The independently reviewed complete cubic arithmetic identity and the true Möbius 2/45 argument, including the fixed-twist cubic density and buffered inverse lemma.
- The independently reviewed Part XV of this report, whose sparse repeated-prime argument proves (10) for the exact rational multiplier.
- de Faveri, *Optimal large sieve for fixed order characters*, Theorem 1.1 and Corollary 1.5: https://arxiv.org/html/2610.04045v1 . The direct and dual eighth moments are derived in §2 from this input, not asserted for arbitrary row-dependent columns.
- User Q, fixed finite-order Hecke zero-free statement and recorded verification scope: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex .

The user attribution for Q is pinned in [FORMAL_INPUT_Q](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/52ee48d3e2e4c5b0beeb3e4880eca86fb2208ce1/reports/20261011_qrh_selection_bridge/FORMAL_INPUT_Q.md); no independent formal rebuild is claimed here. The joint compact-cutoff convention retains the user's [joint-Möbius interface, §4](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/bbb8bba6f6a678848a270a4c950568a672cc975f/reports/20261011_qrh_selection_bridge/QUADRATIC_MOBIUS_GAIN.md), as in Part XI.

# Part XVII. Q-conditional complete mixed(3,5) density bound

Subsections A–D retain independent equation numbering.

## A. Forward quadratic moving-conductor input

### Quadratic detection with a moving conjugate-sextic twist

#### Scope

This note makes the conductor dependence explicit when the completed quadratic method is applied to the mixed frequency H=epsilon v^3w^5a^6. The variables v,w are good, nonunit, squarefree, coprime, with q_v~V and q_w~W. In this note w is frozen before averaging over v. No dependence on W is hidden in a fixed-character constant. The exact mixed local identities and physical n/r/h_0 boundary are supplied separately by Part XIII of this report.

Let psi_v=chi_v^3. The true Möbius column is twisted by the finite-order character eta chi_w psi_v, and the smooth free-s column by rho bar chi_w psi_v, with the original fixed ray data. Their primitive conductor norms are comparable to VW. All character zeros at primes dividing vw remain in the formulae.

#### 1. Uniform detection, including the W dependence

The approximate functional equation for L(s,eta chi_w psi_v)^2 has length O(VW times a polynomial in the height). After common-weight separation, its coefficients contain the actual chi_w values. They are independent of v. The quadratic large sieve and the full square-layer decomposition therefore give
\[
 \sum_{v\asymp V,(v,w)=1}\sup_{|t|\le T}
 |L(1/2+it,\eta\chi_w\psi_v)|^4
 \ll_\epsilon (VWT)^\epsilon VW(1+T)^C.              \tag{1}
\]
The factor W in (1) is not removed by treating chi_w as a common coefficient: the polynomial length is VW. The actual zero masks of chi_w are retained in that coefficient. The truncated inverse polynomial still has second moment bounded by (V+X) times small powers, since its coefficients also have chi_w as a common factor.

Run the same zero detector as in the audited true quadratic-density lemma. Set a=1-b, 0<a<=1/2, and let R count rows with a qualifying zero of real part at least b at the specified buffered finite height. Its first term is
\[
 Y^{a-1/2}R^{1/4}(VW)^{1/4}(V+X)^{1/2},
\]
and its squared-polynomial tail is bounded by
\[
 VX^{2a-1}+Y^{2a}.
\]
Taking X=V and Y=(V^3W)^{1/(2+2a)} gives
\[
 \boxed{R\ll (VWT)^\epsilon(1+T)^C
 \min\{V,(V^3W)^{a/(1+a)}\}.}                     \tag{2}
\]
For X<=V the balanced first term already has this power; X>V only enlarges it. Thus changing X alone does not improve the W exponent in this detector.

Input Q and the finite-height inverse-L argument apply to the genuine finite-order character eta chi_w psi_v. Their ambient parameter contains VW, all deleted Euler factors and all actual infinite-tail labels. They give small powers of that ambient parameter, which are only later absorbed. In particular Q does not turn (1) into a bound uniform in W with no displayed power.

#### 2. True smooth direct and dual moments

Let B_v(S) be the common smooth free-s column with its fixed w twist. For every fixed integer l>=1 and 1<=S<=VW,
\[
 \boxed{\|B(S)\|_{2l}
 \ll_\epsilon(VWS)^\epsilon
 \left[V^{1/(2l)}\sqrt S+\min(S,\sqrt{VW})\right].}  \tag{3}
\]
Indeed direct quadratic moments give V^{1/(2l)}sqrt S+S. Primitive Poisson has prefactor S/sqrt(VW) and dual length VW/S. Applying the same common-coefficient moment to that true dual gives V^{1/(2l)}sqrt S+sqrt(VW). The root number is a bounded row factor; the conductor norm and its direction are separated in the actual smooth weights. Fixed excluded primes are treated by finite decompositions. Moving w primes are kept in chi_w's common coefficient, rather than added to a purported fixed excluded set.

Pointwise one has min(S,sqrt(VW)); beyond S=VW the actual smooth sum has arbitrary power decay. These statements do not apply to a free-s sum after arbitrary row-dependent rough coefficients have been inserted.

#### 3. Complete free-s scale with the eighth moment

Put
\[
 R_0=\min\{V,V^{3a/(1+a)}W^{a/(1+a)}\},\quad1/8\le a\le1/2.
\]
For any exceptional subset of size at most R_0, (3), Holder and the pointwise bound imply
\[
 \boxed{\sup_{S>0}S^{-a}
   \sum_{v\in\mathcal E}|B_v(S)|
 \ll(VW)^\epsilon R_0^{7/8}(VW)^{(1-a)/2}.}          \tag{4}
\]
The left possible peak is at S=sqrt(VW), giving the displayed bound. The right possible peak is at S=R_0^{1/4}V^{3/4}W, and its ratio to the left peak is
\[
 R_0^{1/8-a/4}V^{-a/4}W^{-a/2}\le1.                 \tag{5}
\]
To check the inequality use R_0<=(V^3W)^{a/(1+a)}. Its V exponent is a(1-8a)/[8(1+a)]<=0, and its W exponent is -a(3+6a)/[8(1+a)]<0. The remaining short/long pieces are monotone or rapidly decaying, as in the complete quadratic scale proof.

The actual selected c-slot Euler multiplier still has the quadratic moments (5) of Part XI of this report: replace its fixed local eta(p) by eta(p)chi_w(p), keeping p|w as a zero. On the surviving primes it has modulus one. The slot coefficients remain independent of v. Since R_0>=V^{3a/(1+a)}, the same floor/ceil choice proves the safe marked version of (4), with its column scalar factor L^{-a}, multiplied by
\[
 (VW)^\epsilon\{1+P_c^a R_0^{-1/4}\}.               \tag{6}
\]
When P_c is larger than V, the second moment can sometimes improve R_0^{-1/4} to R_0^{-1/2}; no uniform all-slot saving beyond the displayed bounds is claimed here.

#### Proof inputs and attribution

The argument uses the already audited quadratic large sieve, the actual approximate functional equations, primitive two-dimensional Poisson, and the Q-based finite-height reciprocal theorem. The exact mixed phases, odd n branches and exceptional h_0 square boundary remain the responsibility of the complete mixed arithmetic identity. This note supplies the explicit moving-conductor analytic interface and does not replace that identity.

## B. Reverse sextic moving-conductor input

### A uniform reverse-sextic interface with the moving conductor retained

This note supplies analytic inputs for the actual mixed type H=epsilon v^3w^5a^6. It does not assert a complete physical low estimate. It proves the selected-prime multiplier moments as an analytic input, but does not apply them to a complete physical n-layer and slot budget. The companion arithmetic manuscript keeps those exact objects.

Let v,w be good squarefree and coprime, with w nonunit; v is allowed to be the unit ideal. Put q_v about V and q_w about W, V>=1 and W>=2. The fixed excluded set contains the conductors of the fixed eta and ray data. Consequently every w prime supplies a nontrivial sextic local component, so all actual product characters used below are nonprincipal. Fix v and vary w. After the original finite primary/ray partition, write
\[
 \lambda_{v,w}=\eta\chi_v^3\chi_w^{\pm1},
\]
with the original fixed finite-order eta. The actual primitive conductor norm is comparable to VW. No prime dividing v is added to a supposedly fixed excluded set. Its character values, including zero, remain common column coefficients. The implied constants below depend on the original fixed data but not on v.

#### 1. The finite-height moving-twist zero density

Assume 1<=V<=W. For one selected zero per row in Re(s)>=b and |Im(s)|<=T, let R_v(b,T) be the number of qualifying w~W rows, including arbitrary positive restrictions such as (v,w)=1. Then the independently reviewed uniform estimate is
\[
 \boxed{R_v(b,T)\ll_\epsilon
 (VW)^{\epsilon}(1+T)^{C_\epsilon}
 \min\{W,(WV^{1/6})^{D_6(b)}\},}
 \qquad\tfrac12<b\le\tfrac78,                     \tag{1}
\]
where
\[
 D_6(b)=
 \begin{cases}
 \dfrac{11-14b}{10-12b},&\tfrac12<b\le\tfrac23,\\[2mm]
 \dfrac{216b^2-342b+127}{144b^2-264b+106},
       &\tfrac23\le b\le\tfrac78.
 \end{cases}                                       \tag{2}
\]
In particular D_6(2/3)=5/6 and D_6(7/8)=55/118. All contours used with (1) stay strictly to the right of the actual zero bin; possible endpoint zeros are not discarded.

##### Proof of the uniform conductor payment

Apply the primitive approximate functional equation on the half-line. Its polynomial length is bounded by (VW)^{1/2} times a fixed height power. Its coefficients are the genuine fixed twist times n^{-1/2}, with common smooth weights after conductor-ratio separation. Root numbers are bounded row factors.

For an individual polynomial of norm length B, write n=t ell^6. The row norm for each ell is at most ell^{-3} times the square root of the true sixth-order large sieve at (W,B/ell^6), with small divisor losses. All four ell sums converge. Hence the row second moment is bounded, up to small powers and polynomial height factors, by
\[
 \Theta_6(W,B)\ll W+B+W^{5/6}B^{1/3}+W^{1/3}B^{5/6}.
\]
At B=(VW)^{1/2} this becomes
\[
 W+(VW)^{1/2}+WV^{1/6}+W^{3/4}V^{5/12}
 \ll WV^{1/6},\qquad V\le W.                        \tag{3}
\]
Differentiating common AFE weights and using one-dimensional Sobolev gives the same conductor powers for finite-height suprema, with polynomial height loss.

Set M=WV^{1/6}. The truncated inverse polynomial has the original coefficients mu(c)eta(c)chi_v(c)^3 and hence its positive row norm is bounded by Theta_6(W,X), which is no larger than Theta_6(M,X). The detector's long tail also has common divisor-bounded coefficients with the same fixed twist. Removing all sixth powers is exactly the original argument, with its genuine zero masks.

Thus every step in the proof of de Faveri Corollary 1.5 is valid with its family-size parameter replaced by M: its half-line second moment is O(M), by (3), and its two large-sieve polynomial estimates are bounded by the corresponding Theta_6(M,.) expressions. More explicitly the original detector upper bound becomes
\[
 (MTXY)^\epsilon(1+T)^C\bigg[
 Y^{1/2-b}M^{1/2}
 (X+M+X^{1/3}M^{5/6}+X^{5/6}M^{1/3})^{1/2}
 +Y^{2-2b}+MX^{1-2b}
 +\sup_{X\le U\le Y}U^{1-2b}
       (M^{1/3}U^{5/6}+M^{5/6}U^{1/3})\bigg].       \tag{4}
\]
Its original optimization therefore gives M^{D_6(b)}. Formula (2) is the n=6 specialization of the published exponent, in the range capped by 7/8. The other bound R<=O(W) is the actual row count. This proves (1), without treating the moving twist as fixed-conductor data.

#### 2. Two-sided smooth high moments for the sixth family

Let B_w(S) be the actual common smooth/ray free column with character chi_v^3 chi_w^{+1} or its conjugate, and let C=VW denote its conductor scale. For every fixed integer k>=1 and 1<=S<=C,
\[
 \|B(S)\|_{2k}\ll_\epsilon(VWS)^\epsilon
 \min\{\mathcal A_k(W,S),\mathcal D_k(W,C,S)\},      \tag{5}
\]
where
\[
 \mathcal A_k(W,S)=W^{1/(2k)}\sqrt S+S
                  +W^{5/(12k)}S^{2/3}
                  +W^{1/(6k)}S^{11/12},
\]
\[
 \mathcal D_k(W,C,S)=W^{1/(2k)}\sqrt S+\sqrt C
                  +W^{5/(12k)}C^{1/6}S^{1/3}
                  +W^{1/(6k)}C^{5/12}S^{1/12}.      \tag{6}
\]
The minimum is taken between the complete two sums, not termwise. The original pointwise estimate min(S,sqrt C) and the long-S primitive-Poisson rapid decay remain available.

To prove the direct bound, expand B_w(S)^k as a common Dirichlet polynomial of length O_k(S^k), with divisor-bounded coefficients. In the product index n=t ell^6, the true row zero mask (w,ell)=1 may be removed only inside its positive row norm. The sixth-order large sieve and Minkowski give
\[
 \|\sum_{q_n\ll N}a_n\chi_w(n)\|_2
 \ll(WN)^\epsilon
 [\sqrt{WN}+N+W^{5/12}N^{2/3}+W^{1/6}N^{11/12}].
\]
Its four ell powers are -3,-6,-4,-11/2 and are summable. Taking the k-th root yields the first line of (6).

Primitive smooth Poisson has the exact amplitude S/sqrt C and dual norm scale C/S. The conductor ratio q_{f_w}/C lies in a fixed compact interval; its common Mellin separation is absolutely integrable. The normalized root number and imaginary norm powers are bounded row factors. Apply the just-proved direct high moment to the genuine conjugate sixth family at scale C/S, keeping the fixed chi_v twist. Multiplication by S/sqrt C gives the second line of (6). Schwartz tails and common angular components are handled with their actual smooth seminorms, as in the audited quadratic two-sided moment proof.

#### 3. What transfers to the actual Möbius column

If the user-supplied Q input is invoked, the rightmost-zero bins stop at 7/8. The previously audited finite-height inverse-L argument then applies to the true column
\[
 \sum_{(c,m_0)=1}{\mu(c)\eta(c)\chi_v(c)^3\chi_w(c)^{\pm1}
                   \over q_c^{1+it}}\,W_0(q_c/L).
\]
For a b bin it gives L^{b-1+O(h)} times ambient small powers and polynomial Mellin-height losses. Here c ranges only over the original good ideals, and m_0 is replaced by its part outside the fixed excluded set S. The common mask m_0 retains its exact deleted Euler factors; its full imprimitive modulus, including every such deleted prime, is included in the ambient small-power loss, not only the primitive conductor. The exceptional-row count is (1), not the quadratic density exponent. This statement does not drop any selected-prime Euler multiplier; such a multiplier must be estimated separately with the true sixth large sieve.

#### 4. The actual selected-prime Euler multiplier in the sixth family

Let a fixed number J of disjoint original prime slots have norm scales P_i, let P=product P_i, and let D select one prime from each slot. The coefficients z_D are bounded common weights, including all original signs, fixed twists and zero-real-part Mellin factors. For sigma=Re(s)>=1/2 in a fixed compact interval, define the actual normalized multiplier
\[
 E_w(s)=P^{s-1}\sum_D z_D\prod_{p\mid D}
 {y_p\chi_w(p)\over1-y_p\chi_w(p)},\qquad
 y_p=\eta(p)\chi_v(p)^3q_p^{-s}.
                                                               \tag{7}
\]
For each fixed integer k>=1,
\[
 \boxed{\sum_{w\asymp W}|E_w(s)|^{2k}
 \ll_{\epsilon,k,J}(WP)^\epsilon
 \left[1+{W\over P^k}
       +{W^{5/6}\over P^{2k/3}}
       +{W^{1/3}\over P^{k/6}}\right].}             \tag{8}
\]
The bound is uniform in v; its character and zero masks are common coefficients. Restricting the positive row sum is allowed. The same bound holds for A_w=sum_D z_D chi_w(D)/q_D.

Here are details accounting for every repetition and denominator. First expand A_w^k and fix an equality pattern of the k occurrences in each slot. At a given slot let z denote the number of distinct primes whose multiplicity is divisible by six, r the number with nonzero residue, and o the sum of their residues in {1,...,5}. Freeze the z zero-residue primes. Their row unit masks can be enlarged only inside the positive norm; their exclusion from the remaining primes is a common column restriction. The residual column index is sixth-power-free, of norm about P_i^o. The pattern has at most O(P_i^z) frozen choices and O(P_i^r) residual columns, and coefficient size O(P_i^{-k}). The sixth-order sieve gives the row norm
\[
 \sqrt{\Theta_6(W,R)}\prod_i P_i^{z_i+r_i/2-k},
 \qquad R=\prod_iP_i^{o_i},                         \tag{9}
\]
with small-power losses. Finite equality-pattern multiplicities do not affect the powers. The constant residual column R=1 is handled by its direct row norm.

The four terms of sqrt(Theta_6(W,R)) give, respectively, contributions bounded by
\[
 W^{1/2}P^{-k/2},\qquad1,\qquad
 W^{5/12}P^{-k/3},\qquad W^{1/6}P^{-k/12}.           \tag{10}
\]
For example, for a nonzero residue prime of multiplicity m and residue t=m mod 6, the relevant additive pattern costs are 1/2, (1+t)/2, 1/2+t/6, and 1/2+5t/12. They are bounded by m/2, m, 2m/3 and 11m/12, respectively. A zero-residue prime has cost 1 in every case and m>=6, so the same inequalities hold. These are exactly the exponents in (10). Minkowski over the fixed number of patterns and then squaring proves the A_w version of (8).

For the Euler multiplier use the exact identity
\[
 {yx\over1-yx}={\sum_{j=1}^{6}y^jx^j\over1-y^6},
 \qquad x\in\{0\}\cup\mu_6.                       \tag{11}
\]
Both sides are zero at x=0. The denominator is common to the rows and uniformly bounded away from zero because |y|<=q_p^{-1/2}. Expand (11) over the fixed slots and first apply the triangle inequality in the row L^{2k} norm to these finitely many branches. In each branch fix the exponent j_i in each slot; only then take its k-th power. Thus the repeated occurrences in that branch genuinely have the same j_i, rather than discarding mixed exponent terms in E_w(s)^k. The normalized coefficient per occurrence is O(P_i^{-kappa_i}),
\[
 \kappa_i=1+(j_i-1)\sigma\ge(j_i+1)/2.
\]
Repeat the equality-pattern argument, now taking the residual exponent t=j_i m mod 6 and total coefficient exponent k kappa_i. For j_i=1 the preceding bounds apply. For j_i>=2, a nonzero residue has t<=j_i m and m>=1, so the four additive costs obey
\[
 \tfrac12\le(\kappa_i-\tfrac12)m,\qquad
 \tfrac{1+t}{2}\le\kappa_i m,
\]
\[
 \tfrac12+\tfrac t6\le(\kappa_i-\tfrac13)m,
 \qquad\tfrac12+\tfrac{5t}{12}
                  \le(\kappa_i-\tfrac1{12})m.
\]
At a zero-residue prime the cost is 1, and the same four upper bounds hold because kappa_i>=3/2. Thus (10) still bounds every expanded Euler branch. This proves (8) while keeping all repeated-prime unit masks, every finite denominator and every moving-family zero.

Unlike the quadratic multiplier theorem, (8) contains two real cross terms. They must remain in any subsequent density/high-moment Holder calculation. The selected Möbius column contributes the exact scalar (L/P)^{sigma-1} times this E_w(s); it cannot be replaced by an arbitrary row-independent bound without paying that scale factor.

#### Source and scope

The sole new external density input is de Faveri, *Optimal large sieve for fixed order characters*, Theorem 1.1 and the proof of Corollary 1.5, https://arxiv.org/html/2610.04045v1 . The moving-twist modification is proved by (3)--(4), rather than asserted from the fixed-data wording of the theorem. The conductor and zero extensions are those of the original QRH source family.

The quadratic mixed-type baseline is independent of Q. Any use of this analytic interface with the Q-capped Möbius contour must retain the user's attribution and the previously recorded formal/source-audit distinction. Neither (1) nor (5) alone closes a physical mixed-type low estimate.

## C. Finite two-direction budget

### A finite two-sided certificate for the clean mixed dyadic budget

This is an analytic budget lemma at the original third scale. It is not yet a theorem for every physical n, exceptional h_0 boundary or first flat. Those require the separate exact transfer. The purpose is to give a finite, checkable substitute for numerical optimization of the two audited moving-twist interfaces.

Use logarithms to base Z. Put v=log_Z V, w=log_Z W, p=log_Z P_c, s=log_Z S. Assume
\[
 3v+5w\le13/16,\qquad 0\le p\le1/6,
 \qquad \log_Z(L/S)=11/16.
 \tag{1}
\]
The original normalized prefactor is Z^{-29/96}. The forward method fixes w and counts it absolutely; the reverse method fixes v and counts it absolutely. The true selected-slot multiplier is estimated by its respective audited moments. All row coefficients have only small-power size. The claim of this lemma is that the sum of these positive dyadic majorants can be bounded by Z^{-5/32+epsilon}, on choosing the better direction. No attainment or lower-bound statement is intended.

#### 1. Forward direction up to w=5/48

The positive majorants are nondecreasing in V and W, so it suffices to use v=(13/16-5w)/3. Write a=1-b, d=3a/(1+a), delta=a/(1+a). The uncapped density majorant has row exponent r=dv+delta w; using it even if it exceeds V is an upper bound. The eighth-moment scale lemma gives the unselected exponent
\[
 -29/96-11a/16+
 [7d/8+(1-a)/2]v+[7delta/8+(1-a)/2]w+w.
 \tag{2}
\]
The final w is the number of frozen twists. For each permitted Holder moment, the derivative of its whole exponent in a is at most
\[
 \frac{13}{48}\frac{85}{54}-\frac{11}{16}+\frac16<0.
 \tag{3}
\]
Indeed the maximum of F_v'(a)v+F_w'(a)w along (1) occurs at w=0, and the selected scalar contributes at most p<=1/6. The derivative of the removed row-count factor only helps. Thus the endpoint a=1/8 controls every bin and every selected-slot choice.

At that endpoint the unselected exponent is
\[
 -439/2304+(23/72)w.
 \tag{4}
\]
The quadratic selected-slot moments with k=1,2 and the already proved floor/ceil choices bound the additional exponent by
\[
 \max\left\{0,\frac{13/16-10w}{144},
                    -\frac7{288}+\frac29w\right\}.
 \tag{5}
\]
For completeness, p<=v/2 costs no power, up to an arbitrary small loss. For v/2<=p<=v use the smaller of
\[
 (a-1/2)p+(v-r)/2,\qquad ap-r/4.
\]
Their intersection has value av-(a/2+1/4)r. For p>=v use the second moment, whose cost is ap-r/2. Maximizing these safe bounds over p<=1/6 gives (5).

On 0<=w<=5/48, (4) plus (5) increases piecewise and has its maximum at w=5/48. Both nonzero candidates in (5) are then negative. The result is
\[
 -\frac{1087}{6912}<-\frac5{32}.
 \tag{6}
\]

#### 2. Reverse direction: reduce to one rational endpoint

For w>=5/48, the frequency boundary has v<=7/72<w, so the audited reverse-sextic density applies. At a=1/8 its row exponent is
\[
 r=\frac{55}{118}(w+v/6).
\]
The general zero-bin exponent D_6(a) is the one in the reverse interface. The elementary derivative bound
\[
 0\le D_6'(a)\le9816/3481\quad(1/8\le a\le1/2)
 \tag{7}
\]
follows on the first branch from
\[
 D_6''(a)=
 -\frac{648(2a-1)(216a^2-156a+29)}{(72a^2-12a-7)^3}<0.
\]
The quadratic numerator factor has discriminant -720 and is positive; on the second branch D_6'(a)=8/(12a-2)^2<=2. Thus (7) shows that each full Holder candidate decreases with a: its derivative is at most
\[
 (13/80)(9816/3481)-11/16+1/6<0.
\]
Thus this direction also needs only a=1/8.

Along the frequency boundary v=(13/16-5w)/3, each selected-multiplier/smooth-moment Holder exponent decreases with w. The frozen-v count has derivative -5/3. The row exponent has derivative (13/18)(55/118)<1. Direct or dual smooth 2l-moment terms have w derivative at most 1/(2l), and selected 2k-moment terms at most 1/(2k). The row-count Holder exponent is 1-1/(2k)-1/(2l)>=0. Consequently the total derivative is at most -2/3. Pointwise choices have the same or a stronger inequality. The permitted interval 0<=s<=v+w also shrinks as w increases. It therefore suffices to prove the reverse estimate at
\[
 w=5/48,\quad v=7/72,\quad c=v+w=29/144,\quad
 r=715/12744.
 \tag{8}
\]

#### 3. No selected-slot loss at (8)

At (8), r/w=286/531>10/21. The true sextic Euler multiplier has normalized 2k-norm exponent
\[
 A_k=\frac1{2k}\max\{0,w-kp,5w/6-2kp/3,w/3-kp/6\}.
 \tag{9}
\]
The total multiplier penalty is p/8+A_k-r/(2k). If p<=w, set t=w/p and choose floor(t) or ceil(t), with the arbitrarily tiny-p case handled by a fixed sufficiently high moment. The floor choice works when
\[
 t/m\le \frac{5/12}{5/6-r/w};
\]
the ceiling choice works when
\[
 t/(m+1)\ge\frac{1/12}{r/w-1/3}.
\]
Their intervals cover each [m,m+1], m>=1, because r/w>=10/21. These inequalities include the real two cross terms of the sixth-family multiplier; they are not the quadratic moment formula.

If w<=p<=1/6, choose k=1. Here p<=2w, and the largest remaining term gives the cost
\[
 p/24+(w/3-r)/2\le1/144+(5/144-715/12744)/2<0.
\]
Thus every selected-slot size has no positive power loss, apart from the prescribed epsilon. The same chosen multiplier moment can be combined with every smooth moment below by Holder.

#### 4. Four rational s intervals

At (8), the fixed exponent outside the row sum is
\[
 B_0=-29/96+v-11/128=-335/1152.
\]
For a dual smooth 2l moment, the remaining exponent is
\[
 B_0+r(1-1/(2l))-s/8+
 \max\left\{
 \frac{w}{2l}+\frac s2,\frac c2,
 \frac{5w}{12l}+\frac c6+\frac s3,
 \frac{w}{6l}+\frac{5c}{12}+\frac s{12}
 \right\}.                                             \tag{10}
\]
Use the following complete cover. Each maximum is verified by the two endpoints of its interval because it is a maximum of affine functions:

- 0<=s<=1/8: dual second moment (l=1), maximum -3619/22656;
- 1/8<=s<=1/6: dual fourth moment (l=2), maximum -16183/101952;
- 1/6<=s<=11/60: dual sixth moment (l=3), maximum -96539/611712;
- 11/60<=s<=29/144: pointwise square-root bound, maximum -159979/1019520.

All four numbers are at most
\[
 -321/2048=-5/32-1/2048.
 \tag{11}
\]
The genuine long-S Poisson tail is no larger. This proves the reverse bound, uniformly over the selected slots. Together with (6), it proves the stated clean dyadic budget.

#### Scope of this intermediate lemma

The present clean budget alone does not include physical square boundaries, odd branches or flat operators. Subsection D proves the complete transfer by restoring the genuine character, removing only its redundant boundary-unit mask on the actual support, and then extending positive row norms. No exceptional density count is divided by the boundary divisor.

## D. Complete physical transfer

### The complete mixed (3,5) type: physical transfer of the two-sided budget

#### Theorem and inputs

Use the exact original mixed type
\[
 H=\varepsilon v^3w^5a^6,\qquad vw\text{ good squarefree},\quad
 (v,w)=1,\quad v,w\ne1,
                                                               \tag{1}
\]
with all physical n, the original marker or core marker, and each one's exact first Möbius-flat operator. Retain input Q with its original user attribution and source-audit status. The independently reviewed complete bound is
\[
 \boxed{I_{3,5}^{\rm compensated}(Z)
              \ll_\epsilon Z^{-5/32+\epsilon}.}               \tag{2}
\]
This remains 1/32 above the full low target. No other mixed type or principal core is asserted here.

The dependencies are the independently audited exact arithmetic in Part XIII of this report; the two moving-twist density/moment interfaces in subsections A–B; and the independently audited finite clean budget in subsection C. The latter is used only as a positive analytic inequality at fixed physical windows, not as an already proved all-n theorem. The complete transfer below instead uses the restored-character positive-extension argument; no change of the reverse family by w=h_0w_0 is assumed. The two-sided bound and its transfer are separated below.

Put
\[
 C_0=ZP,\quad K_0=C_0/X'=Z^{13/16},\quad
 C_0/Y'=Z^{11/16},\quad P\ll Z^{1/6}.
                                                               \tag{3}
\]
After Q^{-1/2} and the actual finite subset compensation, the common prefactor is Z^{-29/96}. These identities hold for every original subset length; enlarging P to Z^{1/6} in a positive bound does not change any actual slot.

Write alpha=1-b, 1/8<=alpha<=1/2, for a rightmost-zero bin, reserving a' for the actual sixth-power frequency index. All bin widths and finite-height losses are chosen first, within the final epsilon.

#### 1. The exact full physical weight

The inherited local table gives n=n_0r^2 with n_0|v. Its two odd branches are E=(c,n_0), F=n_0/E. With N about q_n0 and B about q_E, the outside factor is 1/(NB), and after the ordinary fixed-prime restrictions the free column ratio is
\[
 {L\over S}={C_l q_f\over R^6Y_*N^2B^2},
 \qquad C_l=e^lTP,\quad R=q_r,\quad0<Y_*\le Y'.     \tag{4}
\]
Fixed s-divisor extractions may further reduce Y_*. The positive bin estimate consequently contributes (NB)^{-1+2alpha}<=1, since alpha<=1/2. The full sums over n_0,E,g in their dyadic ranges are the already verified divisor-bounded row factors. Their original w-dependent odd-branch phases remain there.

At the exceptional fifth boundary, h_0|rad(r), h_0|w, and
\[
 H_0=q_{h_0}\le R,\qquad
 a=(r/h_0)a',\qquad (h_0,a'cs)=1.
\]
The exact outside coefficient has modulus R^{-2}H_0^{-1}. Restoring the h_0 unit factors gives the full actual v,w character pair, not a character evaluated at a forced nonunit. Ordinary primes are p|r with p not dividing h_0, even when a boundary prime has exponent greater than one in r.

After (4), the precise outside bin weight, apart from the common Q/Y'^{3/2}, is
\[
 (Y'/C_l)^{\alpha} R^{6\alpha-2}H_0^{-1},            \tag{5}
\]
and the full Fourier/Gaussian envelope is
\[
 (1+|\nu|)^Ce^{-cl^2}
 \left(1+{V^3W^5(R/H_0)^6q_{a'}^6\over C_l/X'}\right)^{-A}.
                                                               \tag{6}
\]
Before any reverse positive extension, work on the actual support h_0|w. The restored full character already vanishes whenever (cs,h_0)>1. Thus the extra h_0-unit mask in the c and s columns is redundant on this support. Define the common smooth column for every w by the restored character without that redundant rough mask, and only then enlarge the positive row norm from h_0|w to all w. This preserves a genuine common smooth column for Poisson; it does not claim uniform Poisson for an arbitrary retained h_0-unit mask. Ordinary r masks are first expanded exactly into the fixed divisor extractions already used in (4). In the reverse common-column organization, the w part of g is enforced by the zero extension of chi_w, its v part by the fixed chi_v zero extension, and its a' part by the original fixed column mask. Since v is frozen there, the actual n_0,E divisors of v are fixed divisor choices; their w-symbols enter only bounded row factors. Their c/s-dependent phases have already been canceled by the exact local identity. Thus the reverse family retains common c coefficients and a genuinely common smooth s column at every physical layer.

All original prime slots remain assigned to r,n_0,g,e,c_2, or with r omitted for the core marker. The actual c_2 slot multiplier is the one in the corresponding audited moment theorem. In particular it is not omitted from the clean budget below.

Joint logarithmic Fourier separation retains fixed product cutoffs in every mode, as in the user's [QUADRATIC_MOBIUS_GAIN.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/bbb8bba6f6a678848a270a4c950568a672cc975f/reports/20261011_qrh_selection_bridge/QUADRATIC_MOBIUS_GAIN.md) Section 4 and the audited mixed baseline. All arithmetic masks are fixed or pooled first. The e coefficient is eta(e)/q_e; no second Möbius cancellation in e is assumed.

#### 2. Small bins: a homogeneous contraction of the true clean majorants

Assume 1/8<=alpha<=1/4. For fixed column slots P_c, let A_alpha(U) denote the positive clean analytic majorant summed over dyadic V,W with V^3W^5<=U, including the full S scale (the reciprocal e sum) and using the better of the two proved directions. Factor out (Y'/C_0)^alpha. Each permitted Holder expression has:

- one frozen-twist count V or W;
- a nonnegative power of the actual density bound R_bin;
- a selected-multiplier positive norm;
- a smooth direct/dual positive norm, or its pointwise alternative;
- S^{-alpha}, and the exact selected scalar P_c^alpha.

For 0<t<=1 apply
\[
 (V,W,S)\longmapsto(tV,tW,t^2S),\qquad P_c\text{ fixed}.
                                                               \tag{7}
\]
The frozen count contributes t. Every monomial in either family's direct or dual smooth-moment bound is at most t times its original value. For example the quadratic dual terms are V^{1/(2k)}sqrt(S) and sqrt(VW); the sixth dual terms are
\[
 W^{1/(2k)}\sqrt S,\quad\sqrt{VW},\quad
 W^{5/(12k)}(VW)^{1/6}S^{1/3},\quad
 W^{1/(6k)}(VW)^{5/12}S^{1/12}.
\]
Their respective t exponents are at least one. The direct terms have the same property. The pointwise min(S,sqrt(VW)) and the genuine long-S Poisson bound also contract by at least t; the ratio S/(VW) is unchanged in that tail. The density majorants and the selected positive moments are nondecreasing in their family-size variables, so their nonnegative Holder powers do not increase under (7). Finally S^{-alpha} contributes t^{-2alpha}. Thus every permitted clean majorant contracts by at least
\[
 t^{2-2\alpha}.                                      \tag{8}
\]
This assertion uses the actual common coefficients and full primitive conductor VW. It neither drops a root number from a signed identity nor rescales the physical probe.

As V^3W^5 contracts by t^8, put
\[
 \gamma(\alpha)=(1-\alpha)/4\ge3/16.
\]
Inflating an actual pair with V^3W^5<=U<=K_0 by t^{-1}, t=(U/K_0)^{1/8}, keeps its V/W ratio and puts it in the clean frequency range. In particular the reverse condition V<=W, whenever used by the inflated clean choice, remains valid for the original pair. Every original slot is fixed. Taking the same Holder choice and summing the dyadic ranges gives
\[
 A_\alpha(U)\ll Z^\epsilon (U/K_0)^{\gamma(\alpha)} B_\alpha,
 \quad0<U\le K_0,                                  \tag{9}
\]
where B_alpha is the clean certificate upper bound at K_0. The harmless logarithmic dyadic counts and fixed-ratio annular endpoints are included in epsilon. Empty subunit ranges remain empty.

For clarity about the complete frequency tail, (9) is a counting-function estimate, not a hard frequency cutoff. For U>=K_0 reapply the clean algebra with the enlarged reference parameter Z_U=Z(U/K_0)^{16/13}. The actual slots still obey P_c<=Z_U^{1/6}; only the explicit factors (Y'/C_0)^alpha and the normalized prefactor need to be restored, giving a fixed polynomial power of U/K_0. Explicitly one may take the common clean upper envelope B_alpha=Z^{7/48+11alpha/16}, which follows from its normalized exponent -5/32 after removing Z^{-29/96}(Y'/C_0)^alpha; substituting Z_U therefore gives a finite power (U/K_0)^{(16/13)(7/48+11alpha/16)} uniformly on this compact alpha interval. This is an application of the clean inequality to larger analytic ranges, not an invocation of a coupled-scale physical theorem. Hence A_alpha(U)<=Z^epsilon B_alpha(U/K_0)^B for a uniform finite B. Here is the precise tail application, including effective cutoffs below one. Put x=(T/Z)(H_0/R)^6 q_a'^{-6}<=1 and E=e^l x K_0. The two counting-function bounds imply, by a dyadic decomposition in U/E (or Stieltjes integration),
\[
 \int_0^\infty (1+U/E)^{-A}\,dA_\alpha(U)
 \ll Z^\epsilon B_\alpha e^{C|l|}x^{\gamma(\alpha)}.
                                                               \tag{9a}
\]
Choose A larger than B and gamma, with a fixed positive margin. For U<=K_0 insert (9); for U>=K_0 insert the polynomial bound, and sum the convergent geometric tails. If E>K_0, its excess power is bounded by e^{C|l|}, since x<=1. If E<1 the counting function vanishes below the first actual ideal range and the same Schwartz inequality still applies. Thus no arithmetic range is replaced by a hard cutoff, and no contraction with t>1 is used. The factor e^{C|l|} is absorbed by the original Gaussian exp(-cl^2).

The clean certificate states that the normalized prefactor times (Y'/C_0)^alpha B_alpha is O(Z^{-5/32+epsilon}). Combining its contraction factor with (5)--(6), the remaining exact square and sixth-power weights are
\[
 R^{6\alpha-2-6\gamma}H_0^{6\gamma-1}
 q_{a'}^{-6\gamma}.
                                                               \tag{10}
\]
Since 6gamma>=9/8 and H_0<=R, their r bound is R^{6alpha-3}<=R^{-3/2}; the a' bound is at most q_a'^{-9/8}. The h_0 divisor count and all ordinary-mask counts are small powers. These are genuine absolutely convergent ideal sums, uniformly on this bin interval.

For the exact first flat, insert T=Z/q_delta^6 with coefficient mu(delta)kappa(delta)/q_delta^2 while X',Y' and all slots remain fixed. The same argument adds the delta power
\[
 -2+6\alpha-6\gamma=-7/2+15\alpha/2\le-13/8.         \tag{11}
\]
This also converges absolutely. The redundant frequency lift preserves (1). Therefore the whole small-bin part, including all physical layers and both first flats, satisfies (2).

#### 3. Large bins: a simpler marked pointwise calculation

Assume 1/4<=alpha<=1/2. Use only the forward quadratic moving-twist density
\[
 R_{\rm bin}\ll V^{D}W^{D/3},\qquad D=3\alpha/(1+\alpha),
                                                               \tag{12}
\]
and the actual pointwise smooth bound min(S,sqrt(VW)). The uncapped density is a valid upper bound even when it exceeds V. Extract every selected column product exactly and sum its actual slot mass in absolute value. This costs P_c^alpha<=O(P^alpha), with every deleted Euler factor still present in the true imprimitive modulus. No selected-slot moment is needed here.

The full finite e sum peaks at S=sqrt(VW). Define
\[
 \kappa=D+(1-\alpha)/2,\qquad
 \lambda=D/3+(1-\alpha)/2.
\]
For a fixed w its positive bound is V^kappa W^lambda times (Y'P/C_l)^alpha R^{6alpha-2}H_0^{-1}. Now use the actual support h_0|w: the number of w~W is O(W/H_0). This is ordinary ideal counting of frozen twists, not division of a zero-density row count by H_0.

Weighted V summation in (6) gives
\[
 (C_l/X')^{\kappa/3}(H_0/R)^{2\kappa}
 W^{-5\kappa/3}q_{a'}^{-2\kappa}.
\]
Consequently the remaining W power is
\[
 m(\alpha)=1+\lambda-5\kappa/3
   ={\alpha^2-9\alpha+2\over3(1+\alpha)}\le-1/20.
                                                               \tag{13}
\]
Indeed m(1/4)=-1/20 and m'(alpha)=(alpha^2+2alpha-11)/(3(1+alpha)^2)<0 on this interval. Sum the actual dyadic W ranges with W>=H_0. They give at most a fixed constant times H_0^{m(alpha)}. The residual H_0 exponent is
\[
 2\kappa-2+m(\alpha)={2D-1-2\alpha\over3}\le0.       \tag{14}
\]
The r and flat exponents are both
\[
 6\alpha-2-2\kappa=7\alpha-3-2D\le-3/2.             \tag{15}
\]
For the signs in (14)--(15), their exact factorizations are -(alpha-1)(2alpha-1)/(3(1+alpha)) and (6alpha-2-2kappa)+3/2=(2alpha-1)(7alpha+3)/(2(1+alpha)). Also 2kappa>=39/20>1, so the a' ideal sum converges. Thus all ordinary masks, h_0 divisors, physical square layers and exact flat tails are strictly summable.

The resulting all-scale bound, apart from the common Q/Y'^{3/2} and small powers, is
\[
 (Y'/T)^\alpha(TP/X')^{\kappa/3}.                    \tag{16}
\]
It is valid also at small T: the weighted V moment was applied to the full Fourier tail, and no nonempty range was extended by a fictitious hard cutoff. Gaussian l summation preserves (16).

At T=Z, the normalized finite-compensation exponent is at most
\[
 G(\alpha)=-29/96+13\kappa/48-25\alpha/48.
\]
This decreases on [1/4,1/2], since kappa'=3/(1+alpha)^2-1/2 and 13 kappa'<25 throughout the interval. Hence
\[
 G(\alpha)\le G(1/4)=-323/1920<-5/32.               \tag{17}
\]
The remaining original subset-length term is negative and may be discarded. This proves more than (2) for every large bin.

#### 4. Uniformity, provenance and exact conclusion

In all steps choose the initial ambient small powers using the actual moving norms v,w,r,a',e,h_0,delta and exp(|l|). Only afterward absorb them in the strict r, a', W and delta exponents, and in arbitrarily many Fourier/Gaussian derivatives. Every joint separated mode retains its compact product cutoffs. Original unit/ray phases and zero extensions are unchanged before the positive inequalities. Smooth seminorm and Mellin-height losses remain polynomial and are absorbed by the original outer Mellin weight.

Combining Sections 2 and 3 proves the complete mixed-type estimate (2) in the exact original/core/all-n/two-first-flat scope. The result uses the user's Q theorem through the actual inverse-L/zero-density bins. It improves the earlier Q-free -1/32 for this same mixed type by 1/8, but it does not prove the full low comparison or RH. The complete transfer has passed independent review in the companion REFEREE, Part XVII D; its acceptance is separate from the earlier clean certificate.

Input Q is pinned to the user's [FORMAL_INPUT_Q](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/52ee48d3e2e4c5b0beeb3e4880eca86fb2208ce1/reports/20261011_qrh_selection_bridge/FORMAL_INPUT_Q.md); its build is attributed to the user, and this conditional consequence does not claim an independent formal rerun.
