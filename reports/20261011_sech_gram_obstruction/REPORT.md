# 固定 sech 幂 Gram 分解：第 24 个强制系数严格为负

2026-10-11。此稿针对一个具体的全频正性候选作可复算的否决，不讨论其他 Gram 分解，也不把反演的形式渐近级数当作真实核恒等式。

**结论：下述固定函数族上的非负系数 Gram 表示不存在。RH 及真实一阶 Laguerre 非负性均未在这里解决。**

## 1. 候选及准确量词

取真实完整偶核（与 [算术尾定理](../20261011_laguerre_arithmetic_tail/REPORT.md) 同一尺度）

\[
\Phi(x)=\sum_{n\ge1}(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})e^{-\pi n^2e^{2x}},
\]

并定义

\[
\mathcal K_1(u)=\int_{\mathbb R}v^2\Phi(v+u)\Phi(v-u)dv,
\quad
G_j(x)=\frac{\Phi(x)}{\cosh^j x}\quad(j=1,2,\ldots),
\]

\[
C_j(u)=\int_{\mathbb R}G_j(v+u)G_j(v-u)dv.
\tag{1.1}
\]

每个 C_j 是非负的自相关函数，并且按 \(\widehat f(k)=\int f(u)e^{iku}du\) 约定，

\[
\widehat C_j(k)=\frac12\left|\widehat G_j(k/2)\right|^2\ge0.
\]

待检验的具体候选是：是否存在一列实数 \(c_j\ge0\)，使对全部实 u，

\[
\mathcal K_1(u)=\sum_{j\ge1}c_jC_j(u),
\tag{1.2}
\]

且右侧在 u=0 有限？若存在，这确实给一阶相关核的正定分解。这里函数族已经固定，故不是把“存在某个平方根”改写成目标本身。

### 定理

不存在满足 (1.2) 的非负系数列。该身份和非负性将迫使前 24 个系数唯一，并且

\[
\boxed{-\frac{645486}{10^{11}}<c_{24}<-
\frac{645485}{10^{11}}<0.}
\tag{1.3}
\]

证据由下面的收敛论证、完整 theta 渐近隔离、精确有理三角递推和 π 的有理包络组成，不使用数值采样代替不等式证明。

## 2. 先证明无限正级数可合法截尾

设 (1.2) 成立。因 Φ 在零点附近连续严格正，取固定 δ∈(0,1) 与 m>0，使 \(\Phi(v)^2\ge m\) 于 \(|v|\le\delta\)。由 \(\log\cosh v\le v^2/2\)，

\[
C_j(0)\ge\int_{|v|\le\delta/\sqrt j}
m e^{-jv^2}dv
\ge\frac{2\delta m e^{-\delta^2}}{\sqrt j}.
\]

所以 \(\sum c_jC_j(0)=\mathcal K_1(0)<\infty\) 及 \(c_j\ge0\) 迫使

\[
c_j\le C\sqrt j\qquad(j\ge1).
\tag{2.1}
\]

又因

\[
\cosh(v+u)\cosh(v-u)=\cosh^2v+\sinh^2u\ge\cosh^2u,
\]

记 \(q(u)=\operatorname{sech}^2u\)，则对于 j≥N+1，

\[
C_j(u)\le q(u)^{j-N-1}C_{N+1}(u).
\]

结合 (2.1)，对每个固定 N 和全部充分大的 u，

\[
\sum_{j>N}c_jC_j(u)
\le C C_{N+1}(u)\sum_{j>N}\sqrt j\,q(u)^{j-N-1}
=O_N(C_{N+1}(u)).
\tag{2.2}
\]

所以不必预先假定系数级数解析或逐项收敛半径；非负性和 u=0 的有限值已经给出需要的每阶尾控制。

## 3. 真实全 theta 的主尺度与不可丢失的余项

令

\[
a=2\pi,\quad y=e^{2u},\quad z=ay,\quad x=z^{-1},
\quad b(z)=\sqrt{\pi/(2z)}e^{-z},
\]

并用正的公共尺度

\[
P(u)=4\pi^2e^{5u}b(z)z^2.
\tag{3.1}
\]

先用完整 Φ 的偶性将定义中的 Φ(v−u) 写成 Φ(u−v)，然后才展开 theta 双和。单个 theta 模态 Φ_n 并不偶，不能对单模态直接作这次反射。完整 theta 双和按 r=nm 分组后，每一对的指数为 \(e^{-2\pi r y\cosh(2w)}\)。因此 r≥2 的全部项及任何这里固定阶矩，其绝对积分均为

\[
O(y^A e^{-4\pi y})
\]

（A 是固定常数）。除以 (3.1) 后，这个余项小于每个固定的 \(x^N\)。这是从真实全部模态得到的误差估计，不是直接把 Φ 替换为第一模态。

对 C_j 同样成立：分母 \([\cosh(v+u)\cosh(v-u)]^j\ge1\)，不会放大双和的绝对值。故每个固定 j 的代数阶渐近仅由 n=m=1 决定；完整算术模态仍存在，但不能改变任何一个被强制的代数阶系数。

此外 \(C_0(u)=\int\Phi(v+u)\Phi(v-u)dv\) 满足 \(C_0(u)/P(u)=1+O(x)\)，而 \(q(u)=O(x)\)。故 (2.2) 除以 P 后为 \(O_N(x^{N+1})\)，恰能严格提取至第 N 个系数。

## 4. 无浮点的必要系数递推

以下等式中的幂级数只表示每个有限阶都成立的 Poincaré 渐近展开，不断言这些无限形式级数收敛。

标准 Bessel 渐近为

\[
K_\nu(z)\sim b(z)\sum_{\ell\ge0}
\frac{\prod_{h=1}^{\ell}[4\nu^2-(2h-1)^2]}{\ell!8^\ell}x^\ell.
\]

出处为 [DLMF 10.40.2](https://dlmf.nist.gov/10.40#E2) 及 [10.17.1](https://dlmf.nist.gov/10.17#E1)。在 ν 的固定小复邻域可以通过积分形式的 Laplace 展开一致控制余项，因而允许在 ν=0 作有限阶导数。具体地，换元 s=cosh t−1 得

\[
K_\nu(z)=e^{-z}\int_0^\infty e^{-zs}
\frac{\cosh(\nu\operatorname{arcosh}(1+s))}{\sqrt{s(s+2)}}ds.
\]

去掉 s^(−1/2) 后的振幅在 s=0 解析；局部 Taylor 余项与远端指数包络都对 ν 紧集一致。由 Cauchy 估计可作所需有限阶 ν 微分，z 微分则在同一 Laplace 积分下处理。

定义全部为有理数的

\[
b_0=1,\qquad b_\ell=-\frac{(2\ell-1)^2}{8\ell}b_{\ell-1},
\]

\[
U_0=0,\qquad
U_\ell=-8b_\ell\sum_{h=1}^{\ell}(2h-1)^{-2}\quad(\ell\ge1).
\tag{4.1}
\]

记 \(U(x)=\sum U_\ell x^\ell\)，则 \(\partial_\nu^2K_\nu(z)|_0\sim b(z)U(x)\)。真实相关核满足

\[
\frac{\mathcal K_1(u)}{P(u)}\sim T(x),
\qquad
[x^n]T=\frac14[U_n-6U_{n-1}+(18-6n)U_{n-2}],
\tag{4.2}
\]

负下标按零处理。这是对
\(\tfrac14[(z^2+9)\partial_\nu^2K_\nu+6z\partial_z\partial_\nu^2K_\nu]|_0\)
直接展开所得。

为写 C_j 的系数，定义形式级数 \(M_m(x)=\sum_\ell M_{m,\ell}x^\ell\)，满足

\[
M_{0,\ell}=b_\ell,\qquad
M_{m+1,\ell}=M_{m,\ell}+(\ell-\tfrac12)M_{m,\ell-1}.
\tag{4.3}
\]

其含义是 \((-\partial_z)^mK_0(z)\sim b(z)M_m(x)\)。对 n≥0，置

\[
W_{j,n}(c)=\sum_{k=\lceil n/2\rceil}^{n}
(-1)^k\binom{j+k-1}{k}\binom{k}{n-k}2^{2k-n}c^{2k-n}.
\]

这是

\[
(1+2acx+a^2x^2)^{-j}
=\sum_{n\ge0}a^nW_{j,n}(c)x^n
\]

的形式系数。把 \(c^m\) 替换为 \(M_m(x)\) 的线性映射记为 \(\mathfrak M\)。定义

\[
B_j(x;a)=(1+9x^2)\sum_{n\ge0}a^nx^n\mathfrak M[W_{j,n}(c)]
-6x\sum_{n\ge0}a^nx^n\mathfrak M[cW_{j,n}(c)].
\tag{4.4}
\]

准确有 \(B_j(0;a)=1\)，且

\[
\frac{C_j(u)}{P(u)}\sim(4ax)^jB_j(x;a).
\tag{4.5}
\]

其中分母的真实身份是

\[
\cosh(v+u)\cosh(v-u)=\frac y4
[1+2\cosh(2v)/y+y^{-2}].
\]

即使 v 无界，(4.5) 的有限阶展开仍合法：对 t≥0，\((1+t)^{-j}\) 的固定阶 Taylor 余项由常数乘 \(t^{N+1}\) 控制；积分产生的每个固定 \(\cosh(2v)\) 次幂是 \((-\partial_z)^mK_0(z)\)，有相同的指数衰减尺度。

由 (1.2)、(2.2) 和 (4.2)–(4.5)，系数被唯一三角确定。写 \(t_j=[x^j]T\)，令

\[
D_1(a)=t_1,\qquad
D_j(a)=t_j-\sum_{i=1}^{j-1}D_i(a)[x^{j-i}]B_i(x;a),
\]

\[
\boxed{c_j=\frac{D_j(2\pi)}{(8\pi)^j}.}
\tag{4.6}
\]

每个 D_j 是次数至多 j−1 的有理系数多项式。前两项是

\[
c_1=\frac1{32\pi},\qquad
c_2=\frac{2-1/(4\pi)}{128\pi}>0.
\]

前几项正并不能使正 Gram 分解成立。

## 5. 第 24 项的精确符号证书

附带 `certify_sech_coefficients.py` 只使用整数与 Python `Fraction` 实现 (4.1)–(4.6)，N=24。π 的包络使用

\[
\pi=16\arctan(1/5)-4\arctan(1/239)
\]

及两个交错有理级数的上下余项，再向外取整为分母 \(10^{100}\) 的有理区间。脚本对 D_24 作有理区间 Horner 求值，并除以正的 \((8\pi)^{24}\) 区间。

把标准输出保存为 `sech_coefficient_certificate.json` 即得到 D_24 的全部 24 个有理系数和以下严格外包络：

\[
\frac{-645485003704880932405926869015016150730682592}{10^{50}}
<c_{24}<
\frac{-645485003704880932405926869015016150730682591}{10^{50}}.
\tag{5.1}
\]

这比 (1.3) 更窄。前 23 项在同一有理包络下严格正，第 24 项严格负。脚本证明的是有限代数运算与区间包含；无限核展开和必要性的证明是前述第 2–4 节，不能互相替代。

故 (1.2) 的非负系数假设矛盾，候选被否决。无需再把更高阶系数的收敛半径当作未决条件。

## 6. 作用范围

本结论只排除固定 \(G_j=\Phi\operatorname{sech}^j\) 的对角非负 Gram 混合。不排除换用其他明确函数族、非对角的正半定系数矩阵，或其他完全不同的正定机制。

完整 theta 的超越代数阶算术项未被等同于零：它们不足以修正已被迫为负的 c_24，所以此处确能否决候选；反过来，即使所有形式 c_j 都正，也不能据此声称整个核身份成立。

## 7. 两种精确实现的复算

- `python certify_sech_coefficients.py`：有理多项式递推，以 a=2π 为变量，再作有理区间 Horner 求值。
- `python check_gram_negative_coefficient.py`：以 β=1/(2π) 为参数，在 q=e^(−2u) 中直接三角反演；每次运算作 100 位定点有理向外舍入。

两份脚本均仅使用 Python 标准库，复算环境为 Python 3.12.14；均证明前 23 个必要系数严格正、第 24 个严格负。第二实现独立得到

\[
-\frac{6454850037049}{10^{18}}\le c_{24}\le-\frac{6454850037048}{10^{18}}<0,
\]

与第一实现的更窄区间相容。两份代码只承担有限算术证书，第 2–4 节承担真实无限核与这些系数的联系。
