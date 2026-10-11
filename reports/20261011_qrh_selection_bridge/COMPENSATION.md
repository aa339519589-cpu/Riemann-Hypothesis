# 补偿探针的准确重排：固定素数组的支撑正交与逐频率除数条件

本文研究 [Q] 的完整有限补偿探针，保留其所有字符零延拓和原始素数窗口。
结论是一个准确重排公式及其支撑性质；没有证明临界相关估计或新的零点排除。

## 1. 原对象和标记项的零支撑

采用 [Q] 的 Eisenstein 整数环 \(\mathcal O=\mathbb Z[\omega]\)，
\(q_a=|a|^2\)，理想用乘法相容的 primary 生成元表示。
固定算术数据 \(S,b_*,\xi,\tau,\eta\) 与原论文相同，置
\(\Xi_*(a)=\xi(a)\chi_a(b_*)\)。这里 \(\Xi_*\) 是原论文的有限字符修正，
与 Riemann 的 \(\Xi\) 函数无关。对全部好素数 \(p\notin S\)，这些固定
字符在 \(p\) 处均为单位值。

设 \(\mathcal B_D(U;m,s)\) 表示 [Q] `eq:general-probe` 中完整 corrected row
的 Mellin 积分，加入标记 \(1_{D\mid A}\)，其中完成指标 \(A=cn^3\)：

\[
\mathcal B_D(U;m,s)=\frac1{2\pi i}\int_{(4)}
U^t e^{t^2}T_{m,s,\eta;D}(t)\,dt.
\]

\(T_{m,s,\eta;D}\) 就是原 \(T_{m,s,\eta}\) 的每项乘 \(1_{D\mid cn^3}\)；
原来的 \(\gamma_2\)、\(\alpha\)、\(G\)、\(\mathcal R\) 和零延拓全部不变。
每个这样的项含 \(\chi_A(m)\)。因此

\[
\boxed{(D,m)\ne1\quad\Longrightarrow\quad
\mathcal B_D(U;m,s)=0.}                                    \tag{1}
\]

证明是逐项的：若 \(p\mid D\) 且 \(p\mid m\)，则所有被标记指标都满足
\(p\mid A\)，故 \(\chi_A(m)=0\)。当 \(v_p(A)\) 是六的倍数时，
零延拓仍为零，不能把该局部字符改成在非单位处取值一的函数。
原积分线上的绝对收敛使逐项结论传递到 \(\mathcal B_D\)。

原基探针于是准确写成

\[
\begin{split}
I_{\eta;D}(X,Y,U)=\frac1Y\sum_s
\frac{W_1(q_s/Y)\chi_s(b_*)}{\tau\xi(s)\sqrt{q_{b_*}q_sX}}
\sum_{m\ne0}\xi(m)q_s^{-1/2}g_{\chi_s}(s,-m)
W_0\!\left(\frac{q_m}{q_{b_*}q_sX}\right)
\mathcal B_D(U;m,s).
\end{split}                                               \tag{2}
\]

\(s\) 为避开 \(S\) 的 primary 生成元；\(m\in\mathcal O\)。
\(s,m\) 两个和均因原环带权重而有限。

## 2. 把全部子集换到同一组环带变量

固定一个原允许素数组 \(\mathbf p=(p_1,\ldots,p_K)\)，各 slot 的素数集互不相交。
对 \(J\subseteq\{1,\ldots,K\}\)，置

\[
r=p_J=\prod_{i\in J}p_i,\qquad D=p_{J^c}.
\]

该素数组的带符号补偿和是

\[
\mathcal I_{\mathbf p}=
\sum_J(-1)^{|J|}q_r^{-3/2}\overline{\eta(D)}
I_{\eta;D}(X/q_r,Y/q_r,Zq_D).                              \tag{3}
\]

**命题 1。** 对每个子集项作一一换元
\(s=r s_0\)、\(m=r^2m_0\)。定义与素数组、子集均无关的公共权重

\[
\mathcal C(s,m)=
\frac{W_1(q_s/Y)W_0(q_m/(q_{b_*}q_sX))
\chi_s(b_*)\xi(m)}{Y\tau\xi(s)\sqrt{q_{b_*}q_sX}\sqrt{q_s}},
\]

以及

\[
\begin{split}
U_{J,\mathbf p}(s,m)={}&1_{r\mid s}\,1_{r^2\mid m}
\frac{q_r\overline{\eta(D)}}{\Xi_*(r)}
g_{\chi_{s/r}}(s/r,-m/r^2)\\
&\hspace{14mm}\cdot
\mathcal B_D(Zq_D;m/r^2,s/r).
\end{split}                                               \tag{4}
\]

整除条件不成立时先取零，不计算商。则有准确恒等式

\[
\boxed{\mathcal I_{\mathbf p}
=\sum_{s,m\ne0}\mathcal C(s,m)
\sum_J(-1)^{|J|}U_{J,\mathbf p}(s,m).}                      \tag{5}
\]

**证明。** 范数在换元下满足 \(q_{s_0}=q_s/q_r\)、\(q_{m_0}=q_m/q_r^2\)。
因而两个环带变量分别准确变成

\[
\frac{q_{s_0}}{Y/q_r}=\frac{q_s}{Y},\qquad
\frac{q_{m_0}}{q_{b_*}q_{s_0}(X/q_r)}
=\frac{q_m}{q_{b_*}q_sX}.
\]

范数前因子满足

\[
q_r^{-3/2}\frac1{Y/q_r}
\frac1{\sqrt{q_{b_*}(q_s/q_r)(X/q_r)}}(q_s/q_r)^{-1/2}
=\frac{q_r}{Y\sqrt{q_{b_*}q_sX}\sqrt{q_s}}.                 \tag{6}
\]

固定字符和分母字符的乘法性给

\[
\frac{\chi_{s/r}(b_*)\xi(m/r^2)}{\xi(s/r)}
=\frac{\chi_s(b_*)\xi(m)}{\xi(s)\xi(r)\chi_r(b_*)}.
\]

这里只除以单位值；\(r\) 避开 \(S\)，所以当 \(\xi(m)=0\) 时等式两端
仍同时为零。Gauss 和及完整 row 保留原商变量，不能另换成未缩放对象。
代入 (2) 即得 (4)–(5)。证毕。

## 3. 固定素数组的正交支撑

**命题 2。** 对固定 \(\mathbf p\)，\(U_{J,\mathbf p}(s,m)\) 只能支撑于

\[
\begin{cases}
v_{p_i}(m)\ge2,&i\in J,\\
v_{p_i}(m)=0,&i\notin J.
\end{cases}                                               \tag{7}
\]

所以不同 \(J\) 的支撑互不相交。特别地，任一选定素数在 \(m\) 中恰有一次
赋值时，全部子集分量都为零。

**证明。** 第一行是 \(r^2\mid m\)。若 \(i\notin J\)，则 \(p_i\mid D\)、
\(p_i\nmid r\)；由 (1)，非零的 row 要求 \(p_i\nmid m/r^2\)，即
\(p_i\nmid m\)。对于不同子集，选取其对称差中的一个指标，两行条件
便互相矛盾。证毕。

因此，令 \(V_{J,\mathbf p}(m)=\sum_s\mathcal C(s,m)U_{J,\mathbf p}(s,m)\)，
对任意非负权重 \(w(m)\) 有

\[
\boxed{\sum_m w(m)\left|\sum_J(-1)^{|J|}V_{J,\mathbf p}(m)\right|^2
=\sum_J\sum_m w(m)|V_{J,\mathbf p}(m)|^2.}                 \tag{8}
\]

这是对真实原探针的恒等式。它说明：在 (5) 的公共频率变量中，固定素数组
的子集正负号不会通过平方范数产生负交叉项。它仍允许对 \(m\) 作线性求和
时发生抵消，也允许不同素数组之间发生相关；没有排除这些途径。

## 4. 完整素数组平均的逐频率重排

对公共变量 \(s,m\)，定义

\[
\mathcal R_J(s,m)=\prod_{i\in J}
\{p\in\mathcal P_i(Z):p\mid s,\ p^2\mid m\},\qquad
\mathcal M_{J^c}(m)=\prod_{i\notin J}
\{p\in\mathcal P_i(Z):p\nmid m\}.
\]

把 (5) 乘原权重 \(\prod_iW_i(q_{p_i}/P_i)\)，再对素数组求和。
由 (7)，在每个 \(s,m\) 处，该内和准确等于

\[
\sum_J(-1)^{|J|}
\sum_{\mathbf p_J\in\mathcal R_J(s,m)}
\sum_{\mathbf p_{J^c}\in\mathcal M_{J^c}(m)}
\left(\prod_iW_i(q_{p_i}/P_i)\right)U_{J,\mathbf p}(s,m).    \tag{9}
\]

空乘积及空 slot 系统按通常约定处理。这里没有改变原素数窗口的尺度，
也没有以固定字符替换任何随参数变化的字符。

**逐频率计数。** 设 \(q_m\le C Z^M\)，第 \(i\) 个窗口满足
\(q_p\ge c_i Z^{\ell_i}\)，其中 \(\ell_i>0\) 固定。
若该窗口有 \(N_i(m)\) 个不同素数满足 \(p^2\mid m\)，则

\[
\prod_{\substack{p\in\mathcal P_i(Z)\\p^2\mid m}}q_p^2\le q_m,
\qquad
N_i(m)\le\frac{\log(CZ^M)}{2\log(c_iZ^{\ell_i})}
=\frac{M}{2\ell_i}+O_{\rm fixed}(1/\log Z).                \tag{10}
\]

分母取 \(Z\) 足够大后为正。因此对每个固定 slot 系统，
\(\#\mathcal R_J(s,m)=O_{\rm fixed}(1)\)，一致于这些 \(s,m,Z\)。
在 [Q] 的原尺度上，公共环带给 \(M=5/6\)。

(10) 把重缩放标签的计数移到逐频率除数条件上；它本身不是探针的幂次节省。
换元后的系数含 \(q_r\)，频率范围和剩余标记和也必须一起估计。
特别地，不能把原证明里的 \(Z^d\) 计数直接替换为常数而保留其他估计不变。
不同素数组的支撑可以重叠，所以 (8) 也不能未经证明推广到整个素数组平均。

## 5. 与临界相关目标的关系及复算

[B] 的目标是在固定尺度下把低端指数从 \(3/16\) 推至 \(-3/16\)，并同时
补齐高端估计。本稿提供了保留全部正负号的准确低端重排 (5)、(9)。
固定素数组直接用公共频率平方范数不会获得子集交叉抵消；下一项真正待证的
估计必须控制剩余线性频率和、不同素数组之间的相关，或另一个准确表示。
本稿尚未得到其中任一所需的幂次节省。

`check_compensation.py` 用精确有理数复算 (6) 的所有范数幂，并在完整的
三类赋值 \(0,1,\ge2\) 上检查局部投影恒等式。
三类覆盖全部非负整数赋值；多素数结论由正文的乘积论证给出。
脚本不计算 zeta 零点，也不替代 row 绝对收敛和换元的解析证明。
环境：Python 3.14.8，仅标准库。

```sh
python3 check_compensation.py
```

[Q] *The Quasi-Riemann Hypothesis*，`openai/math` 固定提交
[`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)：
`sec:arithmetic` 的 primary 与零延拓约定；`eq:general-probe`；
`eq:compensated-probe-definition`；`sec:compensated-low` 的 marked row。

[B] 本仓库固定提交
[`1357c71a2bf342e7cc32491644cd8dcc15e4377a` 的选择方程与探针报告](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1357c71a2bf342e7cc32491644cd8dcc15e4377a/reports/20261011_qrh_selection_bridge/REPORT.md)，
第 5–7 节，尤其未证相关目标 (R4) 与高端条件 (9)。
