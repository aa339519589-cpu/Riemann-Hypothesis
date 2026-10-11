# 真实 theta 算术尾的全频 Lorentzian 下界和严格正首修正

2026-10-11。此稿只处理真实一阶相关核的算术尾，不宣称 RH 或全实轴一阶 Laguerre 非负性已证。

## 0. 结果及边界

采用 [正算术尾定理](../20261011_laguerre_arithmetic_tail/REPORT.md) 的同一完整 theta 核、Bessel 块 Jν 和除数方差 B(r)，以及其已证分解

\[
\mathcal K_1(u)=\sum_{r\ge1}T_r(u),\qquad u\ge0,
\]

\[
T_r(u)=B(r)J_0(r,u)+\frac{d(r)}4H_r(u),\qquad
H_r=\left.\partial_\nu^2J_\nu\right|_{\nu=0},
\]

及每个 \(r\ge2\) 的严格正、递减、凸性和偶延拓正定性。定义

\[
L_r=2\pi r,\quad \lambda_r=2L_r=4\pi r,
\quad a_r=-T_r'(0)>0,\quad t=\frac{k}{\lambda_r}.
\]

傅里叶变换统一为
\(\widehat T_r(k)=\int_\mathbb R T_r(|u|)e^{iku}du\)。

### 定理 A：有显式常数的全频包络

对所有整数 \(r\ge16\) 和所有实数 k，

\[
\boxed{
\widehat T_r(k)=\frac{2a_r}{k^2+\lambda_r^2}(1+\epsilon_r(k)),\qquad
|\epsilon_r(k)|\le
\frac{2000}{L_r(1+t^2)}.
}
\tag{A}
\]

此量词包括 k=0 和任意快于 r 增长的 k；不需要先固定 k 再取 r 极限。

### 定理 B：真实算术首修正及严格下界

存在绝对常数 C 和 R，使对全部整数 \(r\ge R\) 及所有实 k，

\[
\boxed{
\widehat T_r(k)=\frac{2a_r}{k^2+\lambda_r^2}
\left[
1+\frac{7+11t^2}{L_r(1+t^2)^2}+E_r(k)
\right],\qquad
|E_r(k)|\le\frac{C}{L_r^2(1+t^2)}.
}
\tag{B}
\]

C 的存在由下文有限阶积分估计严格给出，不是数值拟合；本稿没有计算最优 C 或数值 R。于是存在绝对整数 \(R_0\)，对每个 \(r\ge R_0\) 及每个有限实 k，

\[
\boxed{\widehat T_r(k)>
\frac{2a_r}{k^2+(4\pi r)^2}>0.}
\tag{C}
\]

该下界的高频主项是准确的 \(2a_r/k^2\)，不是少取固定比例的主项。它还给出全频严格正的第一修正。一般凸函数不会自动满足 (C)；这里使用实际 Bessel 块及完整除数方差。

## 1. 真实算术约束，未平滑除数权重

原始公式为

\[
B(r)=\frac{d(r)}{12}\sum_{p^b\parallel r}b(b+2)(\log p)^2.
\]

因为 \((b+2)\log p\ge3\log2\)，对每个整数 \(r\ge2\)，

\[
\boxed{
\frac{B(r)}{d(r)}\ge\frac{\log2}{4}\log r>0.
}
\tag{1.1}
\]

这一不等式不假定 r 为素数、平方自由数，也不要求相邻整数的 d(r) 平滑。后文始终保留 a_r 的真实值。

## 2. 两个 Bessel 矩及可控的拉普拉斯展开

置

\[
A_q(z)=\int_0^\infty x^{2q}e^{-z\cosh x}dx,
\qquad q=0,1.
\]

故 \(A_0=K_0\)、\(A_1=\partial_\nu^2K_\nu|_0\)。写

\[
F_q(z)=(z^2+9)A_q(z)+6zA_q'(z),\quad
\mathscr D=5+2z\partial_z.
\]

对固定 r，令 \(g_{0,r}=J_0(r,\cdot)\)、\(g_{1,r}=H_r\)。则

\[
g_{q,r}^{(m)}(u)=4\pi^2r^2e^{5u}\mathscr D^mF_q(z),
\qquad z=L_re^{2u}.
\tag{2.1}
\]

以下每次微分都由正积分包络控制，不是形式微分。

### 2.1 一阶估计的显式常数

令 \(c_q=\int_0^\infty x^{2q}e^{-x^2/2}dx\)；q=0,1 时均有 \(c_q=\sqrt{\pi/2}\)。对固定非负整数 j，换元 \(x\mapsto x/\sqrt z\) 给

\[
(-1)^jA_q^{(j)}(z)=c_qe^{-z}z^{-q-1/2}(1+\delta_{q,j}(z)).
\]

利用

\[
\cosh y\le e^{y^2/2},\qquad
0\le\cosh y-1-y^2/2\le y^4\cosh y/24
\]

以及 \(1-e^{-v}\le v\)，当 \(z\ge\max(2,2j)\) 时可逐点将误差控制为

\[
\frac1z\left(\frac j2x^2+\frac1{24}x^4\right)e^{-x^2/4}.
\]

乘 \(x^{2q}\) 后积分，得到

\[
|\delta_{0,j}(z)|\le\frac{\sqrt2(j+1/2)}z,
\qquad
|\delta_{1,j}(z)|\le\frac{\sqrt2(6j+5)}z.
\tag{2.2}
\]

把 \(\sqrt2\) 上界为 3/2 即全为有理常数。

为透明地核验 \(\mathscr D^m\)，定义多项式

\[
p_{0,0}=z^2+9,\quad p_{0,1}=6z,
\]

\[
p_{m+1,j}=(5+2z\partial_z)p_{m,j}+2zp_{m,j-1},
\tag{2.3}
\]

未列下标取零。则 \(\mathscr D^mF_q=\sum_jp_{m,j}A_q^{(j)}\)。对 m=0,1,2,3,4，主项分别是 \((-2)^mz^{m+2}\)。在 \(z\ge100\) 上，以 (2.2) 对剩余有限多项式逐项取绝对值，得到

\[
\mathscr D^mF_q(z)
=(-2)^mc_qe^{-z}z^{m+3/2-q}(1+e_{q,m}(z)),
\tag{2.4}
\]

\[
|e_{q,m}(z)|\le C_m/z,
\qquad (C_0,C_1,C_2,C_3,C_4)=(15,30,47,66,90).
\tag{2.5}
\]

附带脚本仅作有理多项式运算，重算并核验这些向上取整的常数。

### 2.2 二阶余项确实有统一积分界

对每个固定 q=0,1 和 j≤5，有严格的

\[
(-1)^jA_q^{(j)}(z)=c_qe^{-z}z^{-q-1/2}
\left[1+\frac{b_{q,j}}z+O(z^{-2})\right],
\tag{2.6}
\]

\[
b_{q,j}=\frac{j(2q+1)}2-
\frac{(2q+1)(2q+3)}{24}.
\]

这里 O 常数只依赖于有限集合 (q,j)，且对所有充分大实 z 一致。为避免把渐近符号当作证明，给出所需统一包络：令 y=x/√z，使用

\[
0\le y^2/2-\log\cosh y\le y^4/12,
\]

\[
0\le\cosh y-1-y^2/2-y^4/24\le y^6\cosh y/720,
\]

及
\(|e^v-1-v|\le v^2e^{|v|}/2\)、
\(0\le e^{-v}-1+v\le v^2/2\)（v≥0）。于是

\[
\cosh^j(y)e^{-z(\cosh y-1)}
=e^{-x^2/2}
\left[1+\frac{jx^2/2-x^4/24}{z}\right]
+\mathcal E_j(x,z),
\]

其中存在一个固定非负系数多项式 \(Q_j\)，使当 \(z\ge4(j+2)\) 时

\[
|\mathcal E_j(x,z)|\le z^{-2}Q_j(x)e^{-x^2/4}
\qquad(x\ge0).
\tag{2.7}
\]

证明 (2.7) 只需将上面三个余项相乘：指数余项可取
\(x^6 e^{x^2/(2z)}/(720z^2)+x^8e^{x^2/z}/(1152z^2)\)，
cosh 幂余项可取常数乘 \(x^4e^{jx^2/(2z)}/z^2\)，交叉项次数也是固定的。条件 \(z\ge4(j+2)\) 使这些指数因子均被 \(e^{-x^2/4}\) 吸收。积分 \(x^{2q}\mathcal E_j\) 即得 (2.6)，且其常数是一组有限 Gaussian 矩之和。这也为后文的 C 提供了严格可计算的存在论证。

## 3. 归一曲率密度：全频证明的关键

暂固定 q,r；简写 L=L_r、λ=2L、g=g_{q,r}、a=-g'(0)>0。定义

\[
f_{q,L}(s)=\frac{g''(s/\lambda)}{\lambda a},\qquad s\ge0.
\tag{3.1}
\]

继承的凸性和无穷端衰减给

\[
f_{q,L}\ge0,\qquad\int_0^\infty f_{q,L}(s)ds=1.
\tag{3.2}
\]

### 3.1 显式的一阶加权导数界

由 (2.4)，对 j=0,1,2，

\[
f_{q,L}^{(j)}(s)=(-1)^j
\exp\left[\frac{(j+6-q)s}{L}-L(e^{s/L}-1)\right]
\frac{1+e_{q,j+2}(Le^{s/L})}{1+e_{q,1}(L)}.
\tag{3.3}
\]

当 L≥100 时，分母至少 7/10。对 0≤α≤8，

\[
\left|e^{\alpha s/L-L(e^{s/L}-1)}-e^{-s}\right|
\le\frac{\alpha s+s^2/2}{L}e^{-s/2}.
\tag{3.4}
\]

这是由 \(e^x-1-x\le x^2e^x/2\) 和 \(1-e^{-v}\le v\) 得到的全 s≥0 估计；L≥100 足以吸收额外指数。

置 \(\delta=f_{q,L}-e^{-s}\)，由 (2.5)、(3.3) 得

\[
|\delta(s)|\le L^{-1}(110+6s+s^2/2)e^{-s/2},
\tag{3.5}
\]

\[
|\delta''(s)|\le L^{-1}(172+8s+s^2/2)e^{-s/2},
\qquad |\delta'(0)|\le138/L.
\tag{3.6}
\]

从而

\[
\int|\delta|\le252/L,\quad
\frac12\int s^2|\delta|\le1360/L,
\quad |\delta'(0)|+\int|\delta''|\le522/L.
\tag{3.7}
\]

所有积分域都是 [0,∞)。这些界不涉及 Fourier 频率。

### 3.2 首修正及加权二阶余项

由 (2.6)、(2.3)，令

\[
P_q(s)=(6-q)s-\frac{s^2}{2}-(5-q),
\]

则

\[
\boxed{f_{q,L}(s)=e^{-s}\left[1+\frac{P_q(s)}L\right]+\rho_{q,L}(s).}
\tag{3.8}
\]

存在绝对常数 C_*，对全部充分大 L，

\[
\int(1+s^2)|\rho_{q,L}|+\int|\rho_{q,L}''|
+|\rho_{q,L}'(0)|\le C_*L^{-2}.
\tag{3.9}
\]

这里必须控制二阶导数，只有未加权逐点渐近不足以推出全频结论。

更具体地，在 (2.4) 中以 \(e_{q,m}(z)=\gamma_{q,m}/z+O(z^{-2})\) 表示首系数，(2.3) 准确给出

\[
(\gamma_{0,m})_{m=0}^4=(-49,-81,-121,-169,-225)/8,
\]

\[
(\gamma_{1,m})_{m=0}^4=(-53,-77,-109,-149,-197)/8.
\]

于是 (3.3) 的 j=0,1,2 首修正，除去 \((-1)^je^{-s}\)，分别为
\(P_q\)、\(P_q-P_q'\)、\(P_q-2P_q'+P_q''\)。因此三种受控导数确实来自同一个 \(\rho_{q,L}\)，并非分别选择互不相容的形式余项。

给出 (3.8)–(3.9) 的计算和余项依据。由 (2.6)，

\[
F_0(z)=c_0e^{-z}z^{3/2}[1-49/(8z)+O(z^{-2})],
\]

\[
F_1(z)=c_1e^{-z}z^{1/2}[1-53/(8z)+O(z^{-2})].
\]

因此 g 的主指数是 \(e^{(8-2q)u-Le^{2u}}\)。在 u=s/(2L) 下，记 b=8−2q，c=49/8（q=0）或53/8（q=1），除去常数后

\[
g(s/(2L))=e^{-s}\left[1+\frac{bs/2-s^2/2-c}{L}\right]
+\text{二阶余项}.
\]

对 s 作两次微分，并除以准确的 \(-\partial_sg(0)\)，一次系数中的 c 抵消，恰为 P_q。这也可直接用 (2.3) 在 m=1,2,3,4 核验，不依赖未控制的渐近微分。

为检查非紧 s 区间，令 A=αs/L，B=L(e^{s/L}−1−s/L)，B_0=s²/(2L)。有

\[
|e^A-1-A|\le A^2e^A/2,
\quad |e^{-B}-1+B_0|\le B^2/2+|B-B_0|,
\]

\[
B\le s^2e^{s/L}/(2L),\qquad
0\le B-B_0\le s^3e^{s/L}/(6L^2).
\]

所以展开 (3.3) 的每个一阶项后，其 j=0,1,2 的剩余均被
\(L^{-2}Q(s)e^{-s/2}\) 控制，其中 Q 是固定多项式。这里使用 (2.6) 对 m≤4 的有限多项式组合；分母由 7/10 统一隔离零。积分即得 (3.9)。这证明了 O 常数独立于 L、s 和 k。

最后，\(\int e^{-s}P_q(s)ds=0\)，故由 (3.2)，

\[
\int\rho_{q,L}=0.
\tag{3.10}
\]

## 4. 两端都统一的 Fourier 论证

对 k≠0，两次分部积分及 (3.1) 给

\[
\widehat g(k)=\frac{2a}{k^2}
\left[1-\int_0^\infty f_{q,L}(s)\cos(ts)ds\right],
\qquad t=k/\lambda.
\tag{4.1}
\]

指数密度的余弦变换为 \(1/(1+t^2)\)，正好产生 \(2a/(k^2+\lambda^2)\)。

### 4.1 显式包络，包括 k=0 与 k→∞

令 \(c(t)=\int\delta(s)\cos(ts)ds\)。因为 \(\int\delta=0\)，

\[
|c(t)|\le L^{-1}\min\{1360t^2,252,522/t^2\}.
\tag{4.2}
\]

第一项来自 \(1-\cos ts\le t^2s^2/2\)；第三项来自两次分部积分以及 (3.7)。因此相对误差是
\(- (1+t^2)c(t)/t^2\)。设 x=t²：在 x≤1/5 用第一项；1/5≤x≤2 用第二项；x≥2 用第三项，分别得到

\[
\frac{2000}{L(1+x)}
\]

的统一上界（所需常数分别不超过1958.4、1814.4、1174.5）。

在 k=0 处不作除零：直接由支配收敛或 \(\int s^2f=2\lambda^2\int g/a\)，有

\[
\frac{\widehat g(0)}{2a/\lambda^2}-1
=\frac12\int s^2\delta(s)ds,
\]

其绝对值≤1360/L。高频处则有额外 \((1+t^2)^{-1}\) 衰减，故没有以低频误差冒充全频误差。

### 4.2 精确首修正

直接积分二次多项式给

\[
\int_0^\infty e^{-s}P_q(s)\cos(ts)ds
=-\frac{t^2[(7-2q)+(11-2q)t^2]}{(1+t^2)^3}.
\tag{4.3}
\]

对余项 \(\rho\)，(3.9)–(3.10) 用与 (4.2) 完全相同的低频/高频论证，给相对误差

\[
O\left(\frac1{L^2(1+t^2)}\right)
\]

且对全部实 t 一致。于是

\[
\widehat g_{q,r}(k)=\frac{2a_{q,r}}{k^2+\lambda_r^2}
\left[1+\frac{(7-2q)+(11-2q)t^2}
{L_r(1+t^2)^2}
+O\left(\frac1{L_r^2(1+t^2)}\right)\right].
\tag{4.4}
\]

这里 \(a_{q,r}=-g_{q,r}'(0)>0\)。首修正在每个频率严格正。

## 5. 组合真实 theta 块并保留所有整数

定义

\[
\eta_r=\frac{B(r)a_{0,r}}{a_r}\in(0,1),\qquad
1-\eta_r=\frac{d(r)a_{1,r}/4}{a_r}.
\]

\(T_r\) 的归一曲率密度是两种 f 的准确凸组合。因此定理 A 不受 d(r)、B(r) 大小波动影响。

由 (2.4) 在 m=1 的估计，r≥16 时

\[
\frac{a_{1,r}}{a_{0,r}}\le\frac2{L_r}.
\]

配合真实 (1.1)，得到

\[
0<1-\eta_r\le\frac{2}{L_r\log2\log r}.
\tag{5.1}
\]

先不使用 (5.1)，准确凸组合的首修正分子为

\[
(5+2\eta_r)+(9+2\eta_r)t^2.
\]

再用 (5.1)，它与 \(7+11t^2\) 的差在相对展开中是
\(O(L_r^{-2}(1+t^2)^{-1})\)，因为 r≥16 时 \(\log r\) 有固定正下界。这证明定理 B。

由于

\[
\frac{7+11t^2}{(1+t^2)^2}\ge\frac7{1+t^2},
\]

取 L_r 足够大使 C/L_r≤7/2，便得到 (C)，甚至得到

\[
\widehat T_r(k)\ge\frac{2a_r}{k^2+\lambda_r^2}
\left[1+\frac{7}{2L_r(1+t^2)}\right].
\tag{5.2}
\]

## 6. 完整无限尾的可用下界

对 N≥15，定义

\[
\mathcal R_N(u)=\sum_{r>N}T_r(|u|),\quad
S_N(k)=\sum_{r>N}\frac{2a_r}{k^2+\lambda_r^2},
\]

\[
D_N(k)=\sum_{r>N}\frac{4000a_r\lambda_r^2}
{L_r(k^2+\lambda_r^2)^2}.
\]

所有这些是全整数尾，没有用相邻除数权重的平滑替代。已有双指数尾及有限阶导数包络保证上述和绝对收敛；也可由 (2.4) 和 d(r)≤r、B(r)≤d(r)(logr)²/4 直接检验。

定理 A 逐项相加给全频严格包络

\[
\boxed{S_N(k)-D_N(k)\le\widehat{\mathcal R_N}(k)
\le S_N(k)+D_N(k).}
\tag{6.1}
\]

特别地

\[
|\widehat{\mathcal R_N}(k)-S_N(k)|
\le\frac{1000}{\pi(N+1)}S_N(k),
\tag{6.2}
\]

且当 N+1>1000/π 时左界为严格正。对 N足够大，定理 B 的正首修正进一步给

\[
\widehat{\mathcal R_N}(k)>S_N(k)>0
\tag{6.3}
\]

对每个实 k 成立。任意 N与k共同趋无穷也满足 (6.1)–(6.2)；不存在未声明的极限顺序。

当需要整个 r≥2 的尾时，可保留 2≤r≤N 的原始正定块，再接上 (6.1) 或 (6.3)。这不是删去算术模态，也不需要有限频率数值认证。

## 7. 与 T1 补偿的准确接口，尚未闭合之处

令 \(F_N=\sum_{r\le N}T_r\)。真实 theta 模性给 \(\mathcal K_1\) 的偶性及

\[
F_N'(0)=\sum_{r>N}a_r=:A_N.
\]

因此 \(\widehat F_N\) 的 \(-2A_N/k^2\) 与 S_N 的 \(+2A_N/k^2\) 准确抵消。本稿的误差界在高频还降为 O(k^{-4})，而不只是 O(k^{-2})，见 D_N 的定义。这是相较于原始尾绝对积分界更有力的补偿估计。

但是，相对每个大边界项的小误差并不等于相对最终小差值的小误差。\(\widehat{\mathcal K_1}\) 的所有代数边界项都消失，最终所需的符号在这些抵消之后。本稿没有证明

\[
\widehat F_N(k)+\widehat{\mathcal R_N}(k)\ge0
\quad\text{对全部实 }k.
\]

定理 B 给出了可以使用的全频正补偿和严格正首修正；未闭合的是把这些正项与种子及剩余无限阶边界抵消作符号保真的比较。不能将 (6.3) 或任意固定阶相对逼近单独升级为完整补偿，更不能升级为 RH。

## 8. 有理代数复算

运行 `python check_uniform_constants.py` 可精确复核五个向上取整常数、归一曲率密度的三个微分首修正以及余弦变换式 (4.3)。程序仅用有理符号运算，不采样频率。复算环境为 Python 3.12.14、SymPy 1.14.0。无限区间包络和全频量词由正文解析证明承担。
