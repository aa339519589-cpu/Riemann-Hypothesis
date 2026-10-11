# 一阶 Laguerre 相关核的正算术尾定理

2026-10-11。本文保留真实 theta 全模态与整数乘法，证明二核相关的完整除数展开与全部 r≥2 算术块的正定性。

**主要结论：完整除数–Bessel 展开；全部 r≥2 的半轴算术块偶延拓为正定函数；任意固定有限前缀的 Fourier 变换在充分高频严格为负。一阶全实轴 Laguerre 非负性与 RH 均未证明。**

与已有 [完整 theta 两点核稿](../20261011_bessel_divisor_growth/REPORT.md) 的生成恒等式关系是 `W_y(2u)=𝓘(2y,u)`。这里的新增结论是第 6 节全部 r≥2 算术块的凸性与偶延拓正定性，并给出正尾的显式 L¹ 控制；相关的有限前缀高频负性同时作为使用边界保留。

## 1. 固定阶目标与使用边界

采用实际尺度

\[
\Phi(x)=\sum_{n\ge1}\Phi_n(x),\qquad
\Phi_n(x)=(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})e^{-\pi n^2e^{2x}},
\quad \Xi(t)=\int_{\mathbb R}\Phi(x)e^{itx}dx.
\]

这里讨论的固定一阶目标是

\[
L_1(t):=\Xi'(t)^2-\Xi(t)\Xi''(t)\ge0\qquad(t\in\mathbb R).
\tag{1.1}
\]

这不是新的判据命名。[Csordas 2014 原文](https://arxiv.org/pdf/1309.0055) 的 Open Problem 4.7 正是这一全实轴问题（该文使用不同尺度），并明确区别于已知的系数 Turán 不等式。本文未找到可独立核验的后续全实轴解决；不能把这个检索范围当作完整文献普查。

固定一阶条件一般不足以排除全部非实根；不能以强对数凹或固定有限 Taylor 系数代替 (1.1)，也不能把一阶目标等同于 RH。

薄共轭根的压力测试是准确的：若 \(F(t)=((t-a)^2+b^2)^mH(t)\)、\(H(a)\ne0\)，则

\[
L_1(a;F)=b^{4m}L_1(a;H)-2m b^{4m-2}H(a)^2.
\tag{1.2}
\]

所以固定非零基底并令 b 足够小时会破坏 (1.1)。这说明全实轴的一阶约束可以检出这类插入非实根的坏变形；并不声称所有坏变形均会被这一阶检出。

## 2. 相关核及精确 Fourier 归一

定义

\[
\mathcal K_1(u)=\int_{\mathbb R}v^2\Phi(u+v)\Phi(u-v)dv,
\qquad
\mathcal I(a,u)=\int_{\mathbb R}e^{av}\Phi(u+v)\Phi(u-v)dv.
\tag{2.1}
\]

对每个实 u，\(\mathcal I\) 关于 a 整，且 \(\mathcal K_1=\partial_a^2\mathcal I(0,u)\)。它关于 u 偶，关于 a 也偶。双指数包络允许相关的微分和积分。

变换 \(x=u+v,y=u-v\)、Jacobian 2 给出

\[
\boxed{L_1(t)=4\int_{\mathbb R}\mathcal K_1(u)e^{2itu}du.}
\tag{2.2}
\]

因为 \(\Xi'^2-\Xi\Xi''=\tfrac12\iint(x-y)^2\Phi(x)\Phi(y)e^{it(x+y)}dxdy\)，此处系数 4 无额外半轴因子。点态 \(\mathcal K_1>0\) 显然，但这不等于其 Fourier 变换非负。

## 3. 全整数乘法的精确生成恒等式

以下 \(K_\nu(z)\) 专指第二类修正 Bessel 函数，与相关核 \(\mathcal K_1\) 不同。使用其标准积分

\[
K_\nu(z)=\frac12\int_{\mathbb R}e^{-z\cosh t+\nu t}dt,
\qquad z>0,
\tag{3.1}
\]

见 [DLMF 10.32.9](https://dlmf.nist.gov/10.32#E9)。

对 r≥1、u∈R 置

\[
z_r=2\pi r e^{2u},\qquad
J_\nu(r,u)=4\pi^2r^2e^{5u}
\big[(z_r^2+9)K_\nu(z_r)+6z_r\partial_zK_\nu(z_r)\big],
\tag{3.2}
\]

并令

\[
A_r(a)=r^{a/2}\sigma_{-a}(r)
=\sum_{d\mid r}\exp\big[a(\tfrac12\log r-\log d)\big].
\tag{3.3}
\]

### 定理 1

对每个实 u 和每个复 a，

\[
\boxed{\mathcal I(a,u)=\sum_{r\ge1}A_r(a)J_{a/2}(r,u).}
\tag{3.4}
\]

此和在 u 的任意紧实区间及 a 的任意紧复集上局部一致绝对收敛，且可任意有限次逐项对 a 或 u 微分。

### 推导

固定有序整数对 (n,m)，写 \(r=nm\)、\(c=\tfrac12\log(m/n)\)、\(v=c+w\)。于是指数部分准确变为

\[
n^2e^{2(u+v)}+m^2e^{2(u-v)}=2r e^{2u}\cosh(2w).
\]

两个真实 theta 多项式因子的乘积为

\[
4\pi^2r^2e^{5u}\big[z_r^2+9-6z_r\cosh(2w)\big].
\tag{3.5}
\]

因此该对的积分为

\[
e^{ac}\,4\pi^2r^2e^{5u}
\int_{\mathbb R}e^{aw}
\big[z_r^2+9-6z_r\cosh(2w)\big]e^{-z_r\cosh(2w)}dw
=e^{ac}J_{a/2}(r,u).
\]

这里 \(\int e^{aw-z\cosh(2w)}dw=K_{a/2}(z)\)，而含 cosh 的积分是 \(-\partial_zK_{a/2}\)，决定了 (3.2) 的正号。对 nm=r 的全部有序对求和正好得到 (3.3)。

交换也需要证明，不能只作形式 theta 乘法。固定 u 紧集，\(z_r\ge c_0r>0\)；固定 a 紧集，\(|e^{ac}|\le r^{C_0}\)。原乘积的绝对值由 (3.5) 中将负号改正号的量控制。任意有限次微分只增加 r、\(\cosh(2w)\)、w、\(\log r\) 的固定次幂。用 \(\cosh(2w)\ge1+2w^2\)，并将部分 \(e^{-z_r\cosh(2w)}\) 吸收这些幂，可把积分控制为 \(C r^B e^{-c_1r}\)。每个 r 至多有 r 个有序除数对，故总和可积且局部一致绝对收敛。Tonelli／支配收敛遂允许展开、重排和微分。

## 4. 一阶相关核中的素数方差

令 \(d(r)=\sum_{d\mid r}1\)，以及

\[
B(r)=\sum_{d\mid r}(\log d-\tfrac12\log r)^2.
\tag{4.1}
\]

因为 \(A_r\) 和 \(J_\nu\) 都关于其参数偶，对 (3.4) 在 a=0 求二阶导得

\[
\boxed{\mathcal K_1(u)=\sum_{r\ge1}
\left[\frac{d(r)}4\,\partial_\nu^2J_\nu(r,u)\big|_{\nu=0}
+B(r)J_0(r,u)\right].}
\tag{4.2}
\]

完整乘法还使 B(r) 有显式素数表达式：

\[
\boxed{B(r)=\frac{d(r)}{12}
\sum_{p^b\parallel r}b(b+2)(\log p)^2.}
\tag{4.3}
\]

证明：在均匀随机除数 \(d\mid r\) 下，各素数指数独立且均匀分布于 \(0,\ldots,b\)。其均值 b/2、方差 b(b+2)/12；log 除数中心化方差相加，最后乘 d(r)。式 (4.3) 包含每个素数及所有指数，不是抽样或删素近似。

作为算术核对，对 \(\Re s>1+|\Re a|/2\) 有绝对收敛的

\[
\sum_{r\ge1}\frac{A_r(a)}{r^s}
=\zeta(s-a/2)\zeta(s+a/2),
\]

以及

\[
\sum_{r\ge1}\frac{B(r)}{r^s}
=\frac12\zeta(s)^2(\log\zeta)''(s)\qquad(\Re s>1).
\tag{4.4}
\]

这由绝对收敛的有序整数对和直接推出，不越过 Euler 乘积的收敛域。

## 5. 正半轴显式绝对尾界

记 (4.2) 的第 r 项为 T_r(u)。对 u≥0，\(z=z_r>2\)，有

\[
\boxed{|T_r(u)|\le E_r(u):=
4\pi^2r^2e^{5u}d(r)(z+3)^2\sqrt{\frac\pi z}e^{-z}
\left[\frac1{2z}+\frac{(\log r)^2}{4}\right].}
\tag{5.1}
\]

因此对每个 R，\(|\mathcal K_1(u)-\sum_{r\le R}T_r(u)|\le\sum_{r>R}E_r(u)\)。

证明：利用原积分 (3.5)，\(|c|\le\tfrac12\log r\)。w 的奇交叉项在偶的绝对值包络内积分为零。\(e^{-z\cosh2w}\le e^{-z}e^{-zw^2}\)，且因 z/2>1、x≥1 时 \(xe^{-(z/2)x}\le e^{-z/2}\)，还有

\[
\cosh(2w)e^{-z\cosh(2w)}\le e^{-z}e^{-zw^2}.
\]

将 \((w+c)^2\) 积分，以 Gaussian 的零阶和二阶矩计算，即得到 (5.1)。

该尾界可服务于有限区间的严格求积或后续解析估计。它是绝对误差界，不能因误差很小便声称整个实频率轴的 Fourier 非负；待比较的 Fourier 量自身可任意小。

## 6. 正向引理：全部 r≥2 的半轴算术块均正定

这里必须使用真实相关核的偶性，把 (4.2) 在 u≥0 上的每块作偶延拓。它不同于把原始 \(T_r(u)\) 在整个实轴直接 Fourier 变换；后者不能默认对 r 绝对交换。

### 定理 2

对每个整数 r≥2，函数 \(u\mapsto J_0(r,u)\) 及

\[
H_r(u)=\partial_\nu^2J_\nu(r,u)\big|_{\nu=0}
\]

在 u≥0 上严格凸、严格正、严格递减且趋零。它们各自的偶延拓是正定函数。因此 (4.2) 的每个 \(T_r(|u|)\)、r≥2 都正定，并且

\[
\boxed{\mathcal R(u):=\mathcal K_1(u)-T_1(|u|)
=\sum_{r\ge2}T_r(|u|)
\quad\text{为正定函数}.}
\tag{6.1}
\]

该和还在 \(L^1(\mathbb R)\) 中绝对收敛，故其 Fourier 变换是非负的连续函数，可逐项求和。

### 证明：Bessel 积分的两个矩比

令

\[
C_2(z)=\partial_\nu^2K_\nu(z)|_{\nu=0}
=\int_0^\infty t^2e^{-z\cosh t}dt>0.
\]

由 \(\cosh t-1\le\tfrac12t\sinh t\) 及积分分部，对 z>0 分别得到

\[
\frac{K_1(z)}{K_0(z)}\le1+\frac1{2z},
\qquad
-\frac{C_2'(z)}{C_2(z)}\le1+\frac3{2z}.
\tag{6.2}
\]

例如 \(\int t\sinh t\,e^{-z\cosh t}dt=K_0(z)/z\)，而 \(\int t^3\sinh t\,e^{-z\cosh t}dt=3C_2(z)/z\)；端点项均为零。这些是不带 RH 输入的实际积分估计。

置 \(F_\nu(z)=(z^2+9)K_\nu(z)+6zK_\nu'(z)\)、\(\mathscr D=5+2z\partial_z\)。Bessel 微分方程给准确恒等式

\[
\begin{aligned}
\mathscr D^2F_\nu={}&
[4z^4+285z^2+225+(4z^2+156)\nu^2]K_\nu\\
&+[60z^2+330+24\nu^2]zK_\nu'.
\end{aligned}
\tag{6.3}
\]

因为 \(\partial_u^2J_\nu=4\pi^2r^2e^{5u}\mathscr D^2F_\nu\)，(6.2) 说明 \(J_0''\) 至少是正前因子乘

\[
P_0(z)K_0(z),\quad
P_0(z)=4z^4-60z^3+255z^2-330z+60.
\]

对 (6.3) 求两次阶导数后，\(H_r''\) 至少是同一正前因子乘

\[
P_2(z)C_2(z)+8[(z-3)^2+27]K_0(z),
\quad
P_2(z)=4z^4-60z^3+195z^2-330z-270.
\tag{6.4}
\]

后一额外项来自显式 \(\nu^2\) 系数的二阶导数，不能漏掉。具体为 \((8z^2+312)K_0-48zK_1\)，再用 (6.2) 作下界。

当 z=12+h、h≥0 时，两个多项式为

\[
P_0=4h^4+132h^3+1551h^2+7518h+12084>0,
\]

\[
P_2=4h^4+132h^3+1491h^2+6078h+3114>0.
\]

对 r≥2、u≥0，\(z=2\pi r e^{2u}\ge4\pi>12\)，故两项确实严格凸。Bessel 积分包络同时给它们及一阶导数在正无穷趋零；严格凸遂推出严格递减和严格正。

### 证明：凸函数偶延拓与全算术尾

对任何这里的函数 g，积分两次可写

\[
g(|u|)=\int_0^\infty(v-|u|)_+g''(v)dv.
\]

每个三角核 \((v-|u|)_+\) 正定。等价地，按 \(\widehat g(k)=\int g(|u|)e^{iku}du\) 约定，对 k≠0 直接有

\[
\widehat g(k)=\frac2{k^2}\int_0^\infty g''(v)[1-\cos(kv)]dv\ge0.
\tag{6.5}
\]

于是正的 d(r)、非负的 B(r) 给出每个 \(T_r(|u|)\) 正定。

还可以将 (5.1) 精确积分。记 \(L=2\pi r\)，换元 \(z=2\pi r e^{2u}\) 后得到

\[
\int_0^\infty E_r(u)du
=\frac{d(r)e^{-L}}{4\sqrt{2r}}
\left[L^2+8L+17+\frac{(\log r)^2}{2}(L+3)^3\right].
\tag{6.6}
\]

右端对 r 可和，故偶延拓的全尾在 \(L^1\) 中绝对收敛。它的正定性也由有限正定和的逐点极限保持。这就证明 (6.1) 及其 Fourier 逐项非负。

该结论有实际但有限的作用：现在所有 r≥2 的真实算术块的 Fourier 符号均已由上述证明确定，未将它们与不受控的 r=1 种子一起含混处理。仍需证明这些正项足以补偿种子可能的负 Fourier 部分；定理 2 本身没有给这个比较。

### 推论：任意固定前缀都在高频失去非负性

令 \(F_N(u)=\sum_{r\le N}T_r(u)\)，u≥0。对每个有限 N≥1，

\[
F_N'(0)>0,
\qquad
\widehat{F_N(|\cdot|)}(k)<0
\quad\text{对全部充分大的 }|k|.
\tag{6.7}
\]

证明：定理 1 的局部逐项微分和完整 \(\mathcal K_1\) 的偶性给 \(\sum_{r\ge1}T_r'(0)=0\)。定理 2 给每个 r≥2 的 \(T_r'(0)<0\)，故

\[
F_N'(0)=-\sum_{r>N}T_r'(0)>0.
\]

有限和及其所有导数在正无穷快速衰减，积分两次分部及 Riemann–Lebesgue 引理给

\[
\widehat{F_N(|\cdot|)}(k)
=-\frac{2F_N'(0)}{k^2}
-\frac2{k^2}\int_0^\infty F_N''(u)\cos(ku)du
=-\frac{2F_N'(0)}{k^2}+o(k^{-2}).
\]

特别地，r=1 种子并不正定。这说明本文所需完整算术尾的作用不能由任意固定前缀替代；小的绝对尾界不是全频率相对正性证书。推论针对的正是实际 theta 分解，不是另造的变形核。

## 7. 仍未闭合的关键点

已经得到固定真实种子、全部除数乘法、显式尾控制和全部 r≥2 偶延拓块的正定性。未知的是该完整和的 Fourier 符号：定理 2 没有涵盖 r=1，也未证明算术尾对它的补偿下界。尤其 (3.5) 的多项式在 w 足够大时有负项，不能把它删除。

同样，任意实 a 下 \(\mathcal I(a,\cdot)\) 是正定的这一事实并不解决问题。直接变换给

\[
\int_{\mathbb R}\mathcal I(a,u)e^{2itu}du
=\frac12\Xi(t-ia/2)\Xi(t+ia/2)
=\frac12|\Xi(t+ia/2)|^2\ge0.
\tag{7.1}
\]

正定函数族的 a² 系数未必正定；要求这个系数非负正是本文尚待证明的 (1.1)，不能用 (7.1) 循环宣布完成。

本稿没有宣称 (4.2) 在文献中首次出现，也没有把精确表示计作 RH 证明。其作用是把下一固定阶问题中的完整算术数据明确到素数指数方差与同一个 Bessel 种子，供独立检验具体正定机制。

## 8. 精确代数复算

运行 `python check_laguerre_tail_algebra.py` 可复核式 (6.3)、两个移位正多项式、阶导数额外项及两个尾积分原函数。已复算环境为 Python 3.12.14、SymPy 1.14.0。程序只验证有限代数；交换、凸性及正定性由正文解析证明承担。
