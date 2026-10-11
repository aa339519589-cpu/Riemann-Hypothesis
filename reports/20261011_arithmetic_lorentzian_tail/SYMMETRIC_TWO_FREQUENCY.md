# 真实算术尾的对称两频谱 Gram 正性

2026-10-11。**定理：对所有充分大的真实算术块 r，以及全部实频率 a，频点 {a,−a} 的 2×2 谱 Gram 非负。** 本稿不是 RH 证明：有限前缀与完整尾合计的符号仍未闭合，也没有把两点正性升级为任意阶矩阵正性。

继承已证明的真实分解、各 r≥2 的半轴正块及大 r 全频 Lorentzian 下界。以下给出新增非对角估计；不使用 Gamma 同域交换子，不把有限 prime 模型当作完整对象。

准确继承输入：[固定提交 1e3723fc 的主稿](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1e3723fc684becd9df304b677c4796c04928ee46/reports/20261011_arithmetic_lorentzian_tail/REPORT.md)，定理 C 及式(2.4)–(2.5)；独立核验见同目录 [REFEREE.md](REFEREE.md)。第4节只需要其中较早的标量下界，不依赖更强的最优面积尺度定理。

## 1. 精确对象及定理

沿用

\[
C(r,u)=4\pi^2r^2e^{5u},\quad z=L_re^{2u},\quad L_r=2\pi r,
\]

\[
p_z(w)=(z^2+9-6z\cosh(2w))e^{-z\cosh(2w)},
\quad P_z(\xi)=\int_\mathbb R p_z(w)e^{i\xi w}dw,
\quad m_2(z)=\int w^2p_z(w)dw.
\tag{1}
\]

令 c_d=½log r−log d，d遍历 r 的所有正除数，

\[
A_r(i\xi)=\sum_{d\mid r}e^{i\xi c_d},\quad
B(r)=\sum_{d\mid r}c_d^2,\quad d(r)=\sum_{d\mid r}1.
\]

原真实一阶相关块准确为

\[
T_r(u)=C(r,u)[B(r)P_z(0)+d(r)m_2(z)],\quad u\ge0.
\tag{2}
\]

定义非对角块

\[
S_r(\xi,u)=-\frac{C(r,u)}\xi\frac{d}{d\xi}
[A_r(i\xi)P_z(\xi)],
\tag{3}
\]

ξ=0取解析极限，故 S_r(0,u)=T_r(u)。它也等于真实 divisor-pair 的 v²sinc(ξv) 积分。

令 \(\widehat T_r(\xi)=2\int_0^\infty T_r(u)\cos(\xi u)du\)。对称两频矩阵是

\[
\mathbb G_r(a)=
\begin{pmatrix}
4\widehat T_r(2a)&8\int_0^\infty S_r(2a,u)du\\
8\int_0^\infty S_r(2a,u)du&4\widehat T_r(2a)
\end{pmatrix}.
\tag{4}
\]

这里的矩阵是同一真实整函数的谱核

\[
K_\Xi(s,t)=\frac{\Xi(s)\Xi'(t)-\Xi'(s)\Xi(t)}{s-t},
\qquad K_\Xi(t,t)=\Xi'(t)^2-\Xi(t)\Xi''(t)=L_1(t)
\]

在频点 \(\{a,-a\}\) 上的算术分块。具体地，完整除数展开给
\(\sum_r S_r(\xi,u)=\int_{\mathbb R}v^2\operatorname{sinc}(\xi v)\Phi(u+v)\Phi(u-v)\,dv\)，其中 \(\operatorname{sinc}y=\sin y/y\)。完整和关于 u 偶；用 \(x=u+v,y=u-v\)、Jacobian 2 及 Φ 的偶性，得到

\[
\sum_{r\ge1}4\widehat T_r(2a)=L_1(a),\qquad
\sum_{r\ge1}8\int_0^\infty S_r(2a,u)du
=-\frac{\Xi(a)\Xi'(a)}a=K_\Xi(a,-a).
\]

零频取解析极限。这里按半轴原除数分解后折叠每个块；不要求单个未折叠的 r 块本身关于 u 偶。全部等式的积分和求和由完整 theta 双指数尾支配。

**定理。** 存在绝对整数 R，使每个整数 r≥R、每个实 a 均有 \(\mathbb G_r(a)\succeq0\)；a≠0时可取严格正定。因而完整尾 \(\sum_{r>N}\mathbb G_r(a)\) 在 N≥R 时亦非负，按原完整 theta 指数尾绝对收敛。

R在本稿只证明存在；没有计算数值阈值。未得到有限前缀+尾的完整矩阵正性。

## 2. 处理有符号 theta 多项式的统一 Fourier 引理

**引理 A。** 存在绝对 z₀，使全部 z≥z₀ 和实 ξ 均有 P_z(0)>0、m₂(z)>0，且

\[
\boxed{
\frac{|P_z(\xi)|}{P_z(0)}\le\frac1{1+\xi^2/(32z)},
\qquad
\frac{|P_z'(\xi)/\xi|}{m_2(z)}\le\frac1{1+\xi^2/(32z)}.}
\tag{5}
\]

ξ=0时两个归一比值均为1。ξ≠0时，上界可以取严格。

这里 p_z 在远尾可能为负；证明不会把它当作概率密度。

### 2.1 缩放后的定量 Gaussian 逼近

设 x=√z w，并去掉正的整体因子 z²e^{-z}：

\[
h_z(x)=[1+9/z^2-(6/z)\cosh(2x/\sqrt z)]e^{-E_z(x)},
\quad E_z(x)=z[\cosh(2x/\sqrt z)-1].
\]

令 g(x)=√(2/π)e^{-2x²}。基本 Taylor 余项和 E_z≥2x² 给

\[
0\le E_z-2x^2\le C z^{-1}x^4\cosh(2x/\sqrt z),
\]

\[
|E_z'-4x|\le C z^{-1}|x|^3\cosh(2x/\sqrt z),\quad
|E_z''-4|\le C z^{-1}x^2\cosh(2x/\sqrt z).
\]

对 z≥1，cosh(2x/√z)≤e^{2|x|}，故以上误差及 h_z 的两阶微分误差均由 C/z 乘可积的“固定多项式×e^{C|x|−2x²}”控制。逐项积分并归一化给

\[
\rho_{0,z}(x)=\frac{p_z(x/\sqrt z)}{\sqrt z P_z(0)},\quad
\int\rho_{0,z}=1,
\]

\[
\int(1+|x|^4)|\rho_{0,z}-g|dx+
\|\rho_{0,z}''-g''\|_1+
\|x(\rho_{0,z}'-g')\|_1\le C/z.
\tag{6}
\]

分母 \(\int h_z\to\sqrt{\pi/2}>0\)，所以 z充分大时归一化合法。式(6)保留 signed p_z，未删除其负尾。

### 2.2 第二响应的准确 Stein 尾密度

置

\[
q_z(w)=\int_{|w|}^\infty v p_z(v)dv,
\quad \int q_z=m_2(z),\quad
\widehat q_z(\xi)=-P_z'(\xi)/\xi.
\tag{7}
\]

由 q_z′(w)=−w p_z(w)、q_z″=−p_z−wp_z′，以及(6)，归一化缩放

\[
\rho_{1,z}(x)=\frac{q_z(x/\sqrt z)}{\sqrt z m_2(z)}
=\frac{\int_{|x|}^\infty t\rho_{0,z}(t)dt}
{\int t^2\rho_{0,z}(t)dt}
\]

满足 ∫ρ₁,z=1、m₂(z)>0，且

\[
\int x^2|\rho_{1,z}-g|dx+
\|\rho_{1,z}''-g''\|_1\le C/z.
\tag{8}
\]

例如尾积分的 x²加权 L¹差由(1/3)∫|t|⁴|ρ₀,z−g|dt控制；分母趋向1/4。Gaussian 本身满足 \(\int_{|x|}^\infty t g(t)dt=g(x)/4\)，所以两个响应有相同 Gaussian 极限。

### 2.3 全频而非固定频率的上界

两个归一化密度都实偶且积分1。设 t=ξ/√z。用 cos(tx)−1 的二阶界得到低频误差，用两次分部积分得到高频误差；(6)、(8)遂给 j=0,1：

\[
|\widehat\rho_{j,z}(t)-e^{-t^2/8}|
\le\frac C z\min(t^2,t^{-2}).
\tag{9}
\]

对全部 t≠0，有初等严格余量

\[
\frac1{1+t^2/32}-e^{-t^2/8}
\ge\frac1{1+t^2/32}-\frac1{1+t^2/8}
\ge\frac1{16}\min(t^2,t^{-2}).
\tag{10}
\]

最后一步分别在 t²≤1 和 t²≥1 用分母估计；精确常数8/99还大于1/16。选 z≥32C 后，(9)被(10)严格吸收，给出(5)。因此该估计覆盖所有 ξ，包含 ξ远大于z；没有把固定 ξ 的 Laplace 展开误用成全频结论。

## 3. 真实除数相位的非对角控制

对每个 ξ，完整真实除数集合给

\[
|A_r(i\xi)|\le d(r),\qquad
\left|-\frac1\xi\frac d{d\xi}A_r(i\xi)\right|
=\left|\sum_{d\mid r}\frac{c_d\sin(\xi c_d)}\xi\right|
\le B(r).
\tag{11}
\]

把(5)代入(3)，对 L_r≥z₀ 及 u≥0 得

\[
\boxed{|S_r(\xi,u)|\le
\frac{T_r(u)}{1+\xi^2/[32z(u)]}.}
\tag{12}
\]

这一步保留完整算术相位，没有把 A_r(iξ)换成正数；控制的是其绝对值与准确二阶除数矩。

## 4. 一个足够而不最优的面积校准 Lorentzian

令 I_r=∫₀∞T_r(u)du，a_r=−T_r′(0)。继承已证大 r 标量结论

\[
\widehat T_r(\xi)\ge\frac{2a_r}{\xi^2+4L_r^2}.
\tag{13}
\]

真实 Bessel 的边界 Laplace 尺度同时给

\[
\frac{a_r}{I_r}=4L_r^2(1+O(L_r^{-1})),\quad
\frac{\int u^2T_r(u)du}{I_r}=\frac1{2L_r^2}(1+O(L_r^{-1})),
\]

\[
\bar z_r:=\frac{\int z(u)T_r(u)du}{I_r}=L_r(1+O(L_r^{-1})).
\tag{14}
\]

这些 O 对全部整数 r一致：对两个正分量 C(r,u)P_z(0)、C(r,u)m₂(z)，分别用

\[
P_z(0)\sim\sqrt{\pi/2}\,z^{3/2}e^{-z},\quad
m_2(z)\sim\tfrac14\sqrt{\pi/2}\,z^{1/2}e^{-z}
\]

及其一阶 z 导数展开，换变量 v=2L_ru。两分量归一轮廓均趋 e^{-v}，由 \(L_r(e^{2u}-1)\ge2L_ru\) 得统一可积包络。相应比值对正系数 B(r)、d(r) 的混合只是加权平均，所以无需假设除数权随 r 平滑。

以上三项也可从主稿的显式 m=0,1 误差直接取常数，避免只依靠渐近记号。其分量 g_q（q=0,1）满足 m=0 相对误差≤15/z、m=1相对误差≤30/z。令 L=L_r≥128，并置

\[
P_3(L)=1+3/L+6/L^2+6/L^3\le1+4/L.
\]

换元 z=Le^{2u} 后分量面积是一个正共同因子乘以 ∫_L^∞e^{-z}z^{3-q}(1+e_{q,0})dz。因而

\[
\frac{a_q}{I_q}\ge4L^2\frac{1-30/L}{(1+15/L)P_3(L)}\ge\frac52L^2.
\]

利用 u≤(z−L)/(2L)，

\[
\frac{\int u^2g_q}{I_q}\le
\frac{1+15/L}{1-15/L}
\frac{2+18/L+72/L^2+120/L^3}{4L^2}\le L^{-2}.
\]

最后不完全 Gamma 多项式比值给

\[
\bar z_q\le\frac{1+15/L}{1-15/L}(L+4)\le2L.
\]

L=128时这些有理不等式均有严格余量，右侧修正因子随L增大而改善。对两个正分量加权平均，遂对真实 T_r 得到 a_r/I_r≥(5/2)L_r²、∫u²T_r/I_r≤L_r^{-2}、bar z_r≤2L_r。

写 x=ξ²/L_r²。若0≤x≤1，用 cos v≥1−v²/2 得

\[
\frac{\widehat T_r(\xi)}{2I_r}\ge1-x/2\ge(1+x)^{-1}.
\]

若x≥1，(13)给

\[
\frac{\widehat T_r(\xi)}{2I_r}\ge\frac{5/2}{x+4}\ge(1+x)^{-1}.
\]

因此全部实ξ上

\[
\boxed{\widehat T_r(\xi)\ge\frac{2I_rL_r^2}{L_r^2+\xi^2}.}
\tag{15}
\]

此保守尺度 L_r 比最优面积校准尺度更宽，但(15)在ξ=0准确等号，足够承接下一步。它不需要主稿中更强的最优面积尺度结果。

## 5. 两频矩阵的闭合

用正概率密度 T_r/I_r、函数 z↦z/(z+ξ²/32) 的凹性，以及(12)：

\[
\left|8\int S_r(\xi,u)du\right|
\le8I_r\,\frac{\bar z_r}{\bar z_r+\xi^2/32}.
\tag{16}
\]

当 L_r充分大且≥64时，bar z_r≤2L_r≤L_r²/32，故

\[
\frac{\bar z_r}{\bar z_r+\xi^2/32}
\le\frac{L_r^2}{L_r^2+\xi^2}.
\]

结合(15)，

\[
\boxed{
\left|8\int S_r(\xi,u)du\right|
\le\frac{8I_rL_r^2}{L_r^2+\xi^2}
\le4\widehat T_r(\xi).}
\tag{17}
\]

取 ξ=2a，这恰是矩阵(4)的非负性。事实上使用 bar z_r≤2L_r，还得到可以逐项求和的定量补偿：

\[
\boxed{\mathbb G_r(a)\succeq
8I_r\frac{\xi^2L_r(L_r-64)}
{(L_r^2+\xi^2)(64L_r+\xi^2)}\,I_2,
\qquad\xi=2a.}
\tag{18}
\]

对 L_r≥128、a≠0，右侧严格正。a=0时矩阵的两行相同，正确地只为半正定。完整尾可把(18)的正标量对所有r>N相加；这给了真实非对角尾的显式、全频、可计算补偿函数，而非只给一个未量化的“正”标签。其使用范围仍须满足新引理和继承定理的共同绝对阈值R。

## 6. 意义及精确未完成项

新增正向控制是：真实全部 divisor 相位下，充分大 r 的对称两频非对角可被同一块的已证正对角全频压住；全算术尾因此保持这个2×2矩阵正性。这里确实需要 v与u两种不同尺度，而非逐点核正值或一般凸性。

对完整 Ξ，矩阵(4)的总和要求

\[
L_1(a)\ge|\Xi(a)\Xi'(a)/a|.
\]

本稿没有证明有限前缀与尾的总和满足它，更没有证明任意有限频点集的 Gram 正性。因此不能声称已经排除真实离轴零点、证明 RH，或把这条2×2尾定理替代全域谱桥。
