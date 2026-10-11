# 原低端的完整二次与三次 dual 核

本稿保持用户原 R4 的真实线性 s–m 配对及全部物理 n。最终结论分别覆盖原 completed-index 标记、新 core 标记，以及两种标记各自的第一层 Möbius 去卷积。

- 完整非主 quadratic 核：原尺度线性和为 O(Z^(37/96−d/2+ε))，计入原归一与有限补偿后为 O(Z^(−1/32+ε))，距完整负低目标 −3/16 尚差 5/32。证明见 Part V。
- 完整非主 cubic good-core：包括 H=εw²a⁶、w 非单位 cube-free 的全部混合指数与全部物理 n；线性和为 O(Z^(25/48−d/2+ε))，补偿后为 O(Z^(5/48+ε))，仍高于目标 7/24。证明见 Part VI。这是上界，未达目标节省。

两者均未覆盖 principal/unit 核及真正 generic sextic good-core，也未证明整个符号配对的目标界或 RH。

Parts I–III 保留 n=1、完整平方层及尺度一致性的已证算术接口；Part IV 给出独立解析双列引理；Parts V–VI 完整证明真实公共系数还原、尾估计及精确去卷积传递。Part VII 给出依赖用户固定输入 Q 的真实 Möbius 列均值；Part VIII 给出真实 selected Euler 乘子矩。两项解析附录尚未完成全部物理除数与补偿求和，不改变上述完整核指数。各 Part 的公式编号独立。首个 Poisson、Gauss 局部身份与原探针归用户报告及固定源稿；外部解析大筛来源分别在相关 Part 中注明。

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
