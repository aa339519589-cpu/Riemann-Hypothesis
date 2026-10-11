# 真实低态的 ε 常数、空间局域化与活动零点定位

2026-10-11。续接 [近指数 Fourier 估计](../20261011_lowstate_subexponential_decay/REPORT.md) 与 [阈值源紧性及逆采样约束](REPORT.md)。本稿只量化此前依赖 \(\varepsilon\) 的常数，并给出能与真实逆采样 Gram 矩阵直接比较的移动窗口。**不假设零点简单、间隔下界或 \(\zeta'(\rho)\) 下界；不证明 RH。**

所有未数值化的正常数均只依赖原固定真实算子与归一约定。下文给出它们关于 \(\varepsilon\) 的依赖，不声称已经算出可直接数值验收的窗口高度。

固定非零实偶、零均值的真实低态 \(Lq=(1/2-\varepsilon)q\)，\(0<\varepsilon<1/2\)，并规范为 \(v=\sqrt{2\Phi h}\,q\)、\(\|v\|_2=1\)。以下 \(f=mv=\Phi q\)、\(F=\widehat f\)，\(H=L|_{\mathcal H}-1/2\)，其闭谱实现、评价向量与逆采样输入均使用同目录主稿的准确定义。


记

\[
L_\varepsilon=\log(e/\varepsilon),\qquad
\mathfrak M(\varepsilon)=\varepsilon^{-1}\sqrt{L_\varepsilon}.
\]

## 1. 完整 theta 给出的两侧尾与完整素数包络

沿用 \(m=\sqrt{\Phi/(2h)}\)、\(h=\cosh(x/2)\)。令

\[
r=e^{2|x|}\ge1,\qquad a=\pi/2.
\]

完整 theta 第一正模态下界、全部正模态上界及偶性给固定 \(c_m,C_m>0\)，使

\[
\boxed{c_m r e^{-ar}\le m(x)\le C_m r e^{-ar}
\quad(x\in\mathbb R).}
\tag{1.1}
\]

例如在 \(x\ge0\)，

\[
\Phi_1(x)=4\pi^2e^{9x/2}
\left(1-\frac3{2\pi e^{2x}}\right)e^{-\pi e^{2x}}
\]

且括号统一正；\(e^{x/2}\le2h(x)\le2e^{x/2}\)。上界只需
\(\sum_{n\ge1}n^4e^{-\pi(n^2-1)}<\infty\)。于是 (1.1) 并非只是一项渐近等价。

记 \(\alpha_n=\Lambda(n)/\sqrt n\)。由 (1.1) 可取固定 \(C\) 使 \(m(y)\le Ce^{-2|y|}\)。完整素数移位满足

\[
\boxed{G(x):=\sum_{n\ge2}\alpha_n[m(x-\log n)+m(x+\log n)]
\le Ce^{|x|/2}.}
\tag{1.2}
\]

此处需要的 \(\psi(X)\le C X\) 有初等自足证明。对整数 \(n\ge1\)，素因子赋值公式给
\(\psi(2n)-\psi(n)\le\log\binom{2n}{n}\le2n\log2\)：每个 \(n<p^k\le2n\) 在二项式赋值差中贡献一份 \(\log p\)，其他贡献非负。沿二进尺度累加并用单调性，得到全部 \(X\ge1\) 上的 \(\psi(X)\le4(\log2)X\)。

又 \(m(y)\le Ce^{-2|y|}\)。对 \(x\ge0\)、\(X=e^x\)，向内和的两段由

\[
Ce^{-2x}\sum_{n\le X}\Lambda(n)n^{3/2}\le C e^{-2x}X^{5/2},
\]

\[
Ce^{2x}\sum_{n>X}\Lambda(n)n^{-5/2}\le C e^{2x}X^{-3/2}
\]

控制。第一式直接用 Chebyshev，第二式由 Stieltjes 分部积分与同一界得到。二者均为 \(O(e^{x/2})\)。向外和至多 \(Ce^{-2x}\sum_n\Lambda(n)n^{-5/2}\)，负端用偶性。这证明 (1.2)，没有用 PNT 误差、零点位置或任何条件性算术估计。

## 2. Gårding 常数的真实算术尺度

真实算子 \(P_\varepsilon=B+\varepsilon-\mathcal V\) 的移位配对满足

\[
|\langle u,\mathcal Vu\rangle|\le\int W(x)|u(x)|^2dx,
\]

\[
W(x)=|C_0|m(x)^2+
m(x)\sum_{n\ge2}\alpha_n[m(x-\log n)+m(x+\log n)].
\tag{2.1}
\]

这是对完整对称移位使用 \(2|ab|\le|a|^2+|b|^2\) 并换元的准确结果。

由 (1.1)–(1.2)，保留真实 theta 前因子，得到

\[
W(x)\le C_A A(r),\qquad
W(x)/m(x)^2\le C_B B(r),
\tag{2.2}
\]

\[
A(r)=r^{5/4}e^{-ar},\qquad
B(r)=r^{-3/4}e^{ar}.
\]

\(|C_0|m^2\) 可以吸收到同一包络，因为
\(r^2e^{-2ar}/A(r)\) 在 \(r\ge1\) 上有界；\(W/m^2\) 的常数项亦同样可吸收。

\(A\) 在 \(r\ge1\) 严格递减趋零，因为

\[
(\log A)'=\frac{5}{4r}-a<0.
\]

\(B\) 在 \(r\ge1\) 严格递增，因为
\((\log B)'=a-3/(4r)>0\)。增大固定 \(C_A\)，保证 \(C_AA(1)>1/4\)。于是每个 \(0<\varepsilon<1/2\) 有唯一 \(r_\varepsilon>1\) 满足

\[
C_AA(r_\varepsilon)=\varepsilon/2.
\tag{2.3}
\]

在 \(r\ge r_\varepsilon\) 有 \(W\le\varepsilon/2\)，在内部

\[
W/m^2\le C_B B(r_\varepsilon)
=\frac{2C_AC_B}{\varepsilon}
r_\varepsilon^{1/2}.
\tag{2.4}
\]

由 \(A(r)\le C e^{-ar/2}\) 和 (2.3)，有
\(r_\varepsilon\le C\log(e/\varepsilon)=CL_\varepsilon\)。因此

\[
\boxed{W\le\varepsilon/2+M_\varepsilon m^2,
\qquad M_\varepsilon\le C\mathfrak M(\varepsilon).}
\tag{2.5}
\]

这一步只用完整 theta 与初等 Chebyshev 素数界，不使用任何零点信息、PNT 误差或导数下界。

由于真实 Γ 符号满足 \(b(t)\ge c_b\log(e+|t|)-C_b\)，可取

\[
K_0(\varepsilon)\le\exp(C\mathfrak M(\varepsilon))
\]

使 \(b(t)\ge M_\varepsilon\) 当 \(|t|\ge K_0\)。于是

\[
\langle u,P_\varepsilon u\rangle
\ge\frac\varepsilon2\|u\|_2^2
-M_\varepsilon\|\mathbf1_{[-K_0,K_0]}(D)(mu)\|_2^2.
\tag{2.6}
\]

对每个 \(K\ge1\)，Schwartz 系数 \(m\) 给

\[
\|\mathbf1_{[-K,K]}(D)M_m u\|_2
\le C(1+K)\|u\|_{H^{-1}}.
\tag{2.7}
\]

自足核验：在 Fourier 卷积中令 \(k=\xi-\eta\)，对 \(|\xi|\le K\) 有
\(\langle\eta\rangle\le C(1+K)\langle k\rangle\)。将输入写成
\(\langle\eta\rangle\langle\eta\rangle^{-1}\widehat u(\eta)\)，再用 Young 与
\(\int\langle k\rangle|\widehat m(k)|dk<\infty\) 即得。

所以原 Gårding 估计中的常数可以选择为

\[
\boxed{C_\varepsilon\le\exp(C\mathfrak M(\varepsilon)).}
\tag{2.8}
\]

这是关于 \(\varepsilon\) 的统一量级，不仅是逐态存在常数。

## 3. 近指数权范数的双指数前因子

使用已证的固定对数权

\[
\omega(t)=\int_0^{|t|}\frac{ds}{\log(e+s)},\qquad
\tau=c_*\varepsilon,
\]

及真实全部系数的统一交换子估计
\(\|W_NP_\varepsilon W_N^{-1}-P_\varepsilon\|\le\varepsilon/4\)，其中
\(W_N=e^{\tau\min(\omega(D),N)}\)。

对归一真实低态 \(P_\varepsilon v=0\)、\(\|v\|_2=1\)，此前完整域证明给

\[
\frac\varepsilon4\|W_Nv\|_2^2
\le C_\varepsilon\|W_Nv\|_{H^{-1}}^2.
\]

选择 \(K_1\) 使 \(C_\varepsilon\langle K_1\rangle^{-2}\le\varepsilon/8\)。由 (2.8)，可取

\[
K_1(\varepsilon)\le\exp(C\mathfrak M(\varepsilon)).
\]

低频权至多 \(e^{\tau\omega(K_1)}\)，因而

\[
\|e^{\tau\omega(D)}v\|_2^2
\le\frac{8C_\varepsilon}\varepsilon
e^{2\tau\omega(K_1)}.
\]

用 \(\omega(t)\le|t|\) 并增大一个固定常数，得到

\[
\boxed{\|e^{c_*\varepsilon\omega(D)}v\|_2
\le\exp\{\exp(C\mathfrak M(\varepsilon))\}.}
\tag{3.1}
\]

源 \(F=\widehat{mv}\) 的条带卷积证明中，乘法系数的指数 Fourier 常数可对 \(\tau\le a_0/2\) 统一。因此在真实零点所在条带 \(|\operatorname{Im}z|\le1/2\)，

\[
\boxed{|F(t+ib)|\le A_\varepsilon e^{-c_*\varepsilon\omega(t)},
\qquad A_\varepsilon\le\exp\{\exp(C\mathfrak M(\varepsilon))\}.}
\tag{3.2}
\]

这里可同时与不含 \(\varepsilon\) 的普通 \(L^2\) 评价界 \(|F(t+ib)|\le C\) 取最小值；(3.2) 只在其高频区有效改善该普通界。

## 4. 一个受控移动零点窗口

零点按重数计数满足 \(N(T)=O(T\log(e+T))\)。因
\(\omega(t)\ge c\sqrt{|t|}\) 对 \(|t|\ge1\) 成立，对 \(0<\tau<1\) 可用 Stieltjes 分部积分和较粗 \(N(T)\le C(1+T^2)\) 得

\[
\sum_{w\in Z}m_we^{-\tau\omega(\operatorname{Re}w)}
\le C\tau^{-4}.
\tag{4.1}
\]

全部有限低高度零点已吸收入固定常数；此处没有使用零点间隔或导数下界。

每个离轴四元组只取一个 \(w_i=\gamma_i+i\delta_i\)、\(\gamma_i,\delta_i>0\)。由 (3.2)，将 \(e^{-2\tau\omega(\gamma_i)}\) 的一个因子抽出尾阈值，再用 (4.1)，得到

\[
\sum_{\gamma_i>T}\frac{4m_i[\operatorname{Im}F(w_i)]^2}{\varepsilon}
\le C\varepsilon^{-5}A_\varepsilon^2
e^{-c_*\varepsilon\omega(T)}.
\tag{4.2}
\]

### 定理 2

存在只依赖原固定真实算子的 \(C_2>0\)，使对全部归一真实低态，取

\[
\boxed{T_\varepsilon=\exp(C_2\mathfrak M(\varepsilon))}
\tag{4.3}
\]

就有

\[
\boxed{\sum_{\gamma_i>T_\varepsilon}
\frac{4m_i[\operatorname{Im}F(w_i)]^2}{\varepsilon}\le\tfrac14.}
\tag{4.4}
\]

证明：\(\omega(T)\ge T/\log(e+T)\)。由 (3.2)，(4.2) 前因子的对数至多

\[
2e^{C\mathfrak M(\varepsilon)}+5\log(1/\varepsilon)+O(1).
\]

而对 (4.3)，

\[
c_*\varepsilon\omega(T_\varepsilon)
\ge\frac{c_*\varepsilon e^{C_2\mathfrak M(\varepsilon)}}
{\log(e+e^{C_2\mathfrak M(\varepsilon)})}.
\]

选择足够大的固定 \(C_2>C\)，后者在全部 \(0<\varepsilon<1/2\) 上支配上述前因子对数再加 \(\log4\)；先对小 \(\varepsilon\) 比较指数，剩余紧 \(\varepsilon\) 区间通过增大同一个 \(C_2\) 处理。因此 (4.4) 成立。证毕。

这不声称此窗口小或可目前直接算出数值；它给出一个与 \(\varepsilon\) 配对的严格移动尺度，而不是随意交换两个极限。

### 推论 2A：谱距与活动零点高度的定位

完整真实负平方总量除以 \(\varepsilon\) 至少为 1，而 (4.4) 的高频部分至多为 \(1/4\)。所以每个归一低态必在

\[
0<\gamma_i\le\exp(C_2\mathfrak M(\varepsilon))
\]

的某个真实离轴零点上活动，且该窗口承载至少 \(3/4\) 的归一负平方质量。

如果高度 \(\gamma\le T\) 的全部真实零点已严格确证在临界线上，令 \(Y=\log T>1\)，并增大 \(C_2\) 使 \(C_2\ge1\)。定义

\[
\mathcal A(Y)=\sqrt{\log(eY)}.
\]

则所有真实低态必须满足

\[
\boxed{\varepsilon\le\frac{C_2\mathcal A(\log T)}{\log T}.}
\tag{4.5}
\]

证明：若反有 \(\varepsilon>C_2\mathcal A(Y)/Y\)，则 \(\varepsilon>1/Y\)，故
\(L_\varepsilon=\log(e/\varepsilon)<\log(eY)\)。于是

\[
C_2\mathfrak M(\varepsilon)
\le C_2\mathcal A(Y)/\varepsilon<Y,
\]

得到 \(T_\varepsilon<T\)，与活动离轴零点存在矛盾。

渐近量级为 \(\varepsilon\ll\sqrt{\log\log T}/\log T\)。此结论把有限高度排零转成谱距的剩余区间，并不把有限验证升级为 RH。常数 \(C_2\) 尚未数值化，因此也不声称现在可以代入某已验高度得出实用的数值界。

## 5. 与真实逆采样 Gram 的最短联合约束

令 \(I(T)\) 是高度 \(\gamma_i\le T\) 的全部真实离轴标签，

\[
v_i=2\sqrt{m_i}\,\frac{-\sin(\gamma_i x)\sinh(\delta_i x)}{2h(x)},
\quad u_i=H^\dagger v_i,\quad
\mathsf S_{I(T)}=\mathsf U_{I(T)}^*\mathsf U_{I(T)}.
\]

已证的真实完整负平方及逆采样给，对任何有限 \(I\)，

\[
\sum_{i\notin I}\frac{4m_i[\operatorname{Im}F(w_i)]^2}{\varepsilon}
\ge1-\varepsilon\|\mathsf S_I\|.
\tag{5.1}
\]

对受控窗口 (4.3) 同时使用 (4.4) 与 (5.1)，得到每个真实低态必须满足

\[
\boxed{\|\mathsf S_{I(T_\varepsilon)}\|\ge\frac3{4\varepsilon}.}
\tag{5.2}
\]

因此低态所需的负平方质量有至少 \(3/4\) 必须由这个有限高度窗口承担。若窗口内根本没有离轴标签，已与低态存在矛盾；一般情况下，(5.2) 只是必要的真实插值 Gram 增长要求。

下一步的承重点可以精确放在：能否对完整 \(\Xi\) 的实际零点除法插值，证明与 (5.2) 冲突的独立上界。当前没有该上界。尤其不能默认简单零点、零点分离、\(|\zeta'(\rho)|\) 的多项式下界，或把固定有限标签的范数界当作 \(T\to\infty\) 一致界。

本结论没有把必要关系称作矛盾，没有新增无条件排零，也没有将粗窗口误称有限数值 RH 证书。其价值是把当前空间/频率常数与移动零点窗口明确配对，使下一项算术估计有准确量词。

## 6. 证明范围

本稿依赖上述明确引用的真实算子、近指数交换子、全部零点计数及逆采样；新增推导是 \(\varepsilon\) 常数链、移动窗口、活动高度和 Gram 必要下界。未作形式化内核验证，所有固定常数均未数值化。

## 7. 全零点加权采样与活动零点的联合定位

### 7.1 固定记号

采用已证的真实 theta 源：
\[
h(x)=\cosh(x/2),\quad d\nu=2\Phi h\,dx,\quad Q(x)=\frac{\Phi(x)}{2h(x)},
\quad f=\Phi q=\sqrt Q\,v,\quad F(z)=\int_{\mathbb R}f(x)e^{izx}\,dx.
\]
这里 \(q\) 是任意实偶 \(L^2(\nu)\) 函数，\(v=\sqrt{2\Phi h}\,q\)，故 \(\|v\|_2=\|q\|_\nu\)。真实 \(\Phi\) 的双指数尾使 \(F\) 整，且
\[
M_\theta:=\sup_{x\in\mathbb R}x^2Q(x)e^{3|x|/2}<\infty.
\tag{7.1}
\]
每个真实离轴四元组只取 \(w_i=\gamma_i+i\delta_i\)，\(\gamma_i>0\)、\(0<\delta_i<1/2\)，重数为 \(m_i\)。真实 Riemann–von Mangoldt 局部计数给固定 \(A_0<\infty\)，使所有实数 \(u\) 满足
\[
\sum_{i:\,|\gamma_i-u|\le1/4}m_i\le A_0\log(3+|u|).
\tag{7.2}
\]
有限低高度通过增大同一 \(A_0\) 吸收；不要求零点简单或分离。设 \(K=128A_0M_\theta\)。

### 7.2 全标签采样不等式

对以上所有 \(q\)，均有
\[
\boxed{4\sum_i\frac{m_i[\operatorname{Im}F(w_i)]^2}
 {\delta_i^2\log(4+\gamma_i)}\le K\|q\|_\nu^2.}
\tag{7.3}
\]
证明。令 \(B_i=\sup_{0\le s\le1/2}|F'(\gamma_i+is)|^2\)。对解析函数 \(F'\) 使用半径 \(1/4\) 的圆盘均值不等式，并把每个圆盘包含在同一矩形内，得
\[
 B_i\le\frac{16}{\pi}\int_{\gamma_i-1/4}^{\gamma_i+1/4}
 \int_{-1/4}^{3/4}|F'(u+iy)|^2\,dy\,du.
\tag{7.4}
\]
当 \(|u-\gamma_i|\le1/4\) 时，\(3+|u|\le4+\gamma_i\)。故由 (7.2)，
\[
\sum_{i:\,|\gamma_i-u|\le1/4}\frac{m_i}{\log(4+\gamma_i)}\le A_0.
\]
Tonelli 与 Plancherel 因而给
\[
\begin{aligned}
\sum_i\frac{m_i B_i}{\log(4+\gamma_i)}
&\le\frac{16A_0}{\pi}\int_{-1/4}^{3/4}\int_{\mathbb R}|F'(u+iy)|^2\,du\,dy\\
&=32A_0\int_{-1/4}^{3/4}\int_{\mathbb R}x^2Q(x)|v(x)|^2e^{-2yx}\,dx\,dy\\
&\le32A_0M_\theta\|v\|_2^2.
\end{aligned}
\tag{7.5}
\]
因 \(F(\gamma_i)\) 实，沿竖线积分得到
\( |\operatorname{Im}F(w_i)|\le\delta_i\sqrt{B_i}\)。代入 (7.5) 即得 (7.3)。所有无穷和均为非负项，故该证明同时给出收敛性。证毕。

特别地，对任意 \(T>0\)，若所有满足 \(\gamma_i\le T\) 且 \(\operatorname{Im}F(w_i)\ne0\) 的标签都有 \(\delta_i\le d\)，则
\[
4\sum_{\gamma_i\le T}m_i[\operatorname{Im}F(w_i)]^2
 \le Kd^2\log(4+T)\,\|q\|_\nu^2.
\tag{7.6}
\]

### 7.3 与已审移动窗口的联合结论

设 \(Hq=-\varepsilon q\)、\(\|q\|_\nu=1\)，\(0<\varepsilon<1/2\)。采用上述最终 Chebyshev 优化
\[
L_\varepsilon=\log(e/\varepsilon),\quad
\mathfrak M(\varepsilon)=\varepsilon^{-1}\sqrt{L_\varepsilon},\quad
T_\varepsilon=\exp(C_2\mathfrak M(\varepsilon)).
\tag{7.7}
\]
完整负平方总量至少 \(\varepsilon\)，而 \(\gamma_i>T_\varepsilon\) 的部分至多 \(\varepsilon/4\)。故窗口内负平方至少 \(3\varepsilon/4\)。将 (7.6) 用于该有限窗口中非零负平方标签的最大 \(\delta_i\)，得到存在一个实际标签满足
\[
\boxed{0<\gamma_i\le T_\varepsilon,\quad
\operatorname{Im}F(w_i)\ne0,\quad
\delta_i\ge\sqrt{\frac{3\varepsilon}{4K\log(4+T_\varepsilon)}}.}
\tag{7.8}
\]
由于 \(\log(4+e^{C_2\mathfrak M})\le C_3\mathfrak M\)，其中 \(C_3\) 是固定常数，进一步有
\[
\boxed{\delta_i\ge c\,\frac{\varepsilon}{[\log(e/\varepsilon)]^{1/4}}.}
\tag{7.9}
\]
这里 \(c>0\) 只依赖固定真实 theta 源、真实零点局部计数常数及已审窗口常数。

此结论给同一个活动零点的高度与离轴距离联合约束，不假设零点分离、简单性或 \(1/\Xi'\) 的控制。常数尚未数值化。它没有排除该剩余区域，也不提供 Weil 形式的非负性；本节作为上述移动窗口定理的联合定位推论，不给出 RH 排除。

## 8. 真实低态的 ε 一致空间局域化：截断交换子与双指数尾

2026-10-11。保持上述相同的真实自伴算子、完整 Γ 跳跃核及所有素数幂移位。本稿给出归一低态在移动空间窗口内的定量局域化，与已经证明的固定紧集质量逃逸配合使用。**未排除低态，未证明 RH；本稿不把空间逃逸本身当成矛盾。**

### 8.1 固定对象与结论

在此前准确定义的酉 \(v\) 表示中，

\[
P_\varepsilon v=0,\qquad
P_\varepsilon=B+\varepsilon-\mathcal V,
\qquad B=M_m b(D)M_m\ge0,
\quad\|v\|_2=1,
\quad0<\varepsilon<1/2.
\]

这里 \(m=\sqrt{\Phi/(2h)}\)、\(h=\cosh(x/2)\)，并且

\[
\mathcal V=C_0M_{m^2}+S_m,\qquad
S_m=\sum_{n\ge2}\alpha_nM_m(\tau_{\log n}+\tau_{-\log n})M_m,
\quad\alpha_n=\Lambda(n)/\sqrt n.
\]

已证真实低态 \(v\in H^\infty\)。对本稿需要的粗尾，本稿第1–2节真实 theta/Chebyshev 估计给固定 \(C_W>0\)，

\[
W(x):=|C_0|m(x)^2+
m(x)\sum_{n\ge2}\alpha_n[m(x-\log n)+m(x+\log n)]
\le C_W\exp[-(\pi/4)e^{2|x|}],
\tag{8.1.1}
\]

且 \(|\langle u,\mathcal Vu\rangle|\le\int W|u|^2\)。

#### 空间局域化定理

存在只依赖原固定真实算子的 \(C>1\)，使对每个上述归一低态与 \(R\ge1\)，只要

\[
C_W\exp[-(\pi/4)e^{2R}]\le\varepsilon/2,
\tag{8.1.2}
\]

就有

\[
\boxed{\|\mathbf1_{\{|x|>R+1\}}v\|_2
\le C\varepsilon^{-1}\exp[-(\pi/8)e^{2R}].}
\tag{8.1.3}
\]

因此对任意 \(0<\eta\le1\)，可取

\[
\boxed{R_{\varepsilon,\eta}=
\max\left\{1,\frac12\log\left[\frac8\pi\log\frac{C}{\varepsilon\eta}\right]\right\}}
\tag{8.1.4}
\]

使 \(\|\mathbf1_{\{|x|>R_{\varepsilon,\eta}+1\}}v\|_2\le\eta\)。固定 \(\eta\) 后，窗口半径仅以 \(\tfrac12\log\log(1/\varepsilon)+O_\eta(1)\) 增长。

### 8.2 Γ 截断交换子是小 Hilbert–Schmidt 算子

取固定的偶光滑截断 \(0\le\chi_R\le1\)，满足

\[
\chi_R=0\ (|x|\le R),\qquad
\chi_R=1\ (|x|\ge R+1),\qquad
\|\chi_R'\|_\infty\le C_\chi
\]

且全部固定阶导数界与 \(R\ge1\) 无关。

真实 Γ 乘子相差一个局部常数后具有跳跃表达

\[
b(D)f(x)=c_bf(x)+\int_0^\infty k(t)
[2f(x)-f(x-t)-f(x+t)]dt,
\qquad k(t)=\frac{e^{-t/2}}{1-e^{-2t}}.
\tag{8.2.1}
\]

这与此前源算子 \(A\) 的准确核相同；加入 \(C_0\) 只改变局部乘法常数，后者与 \(\chi_R\) 交换。先在 Schwartz 测试函数上计算，再延拓，有

\[
[B,\chi_R](x,y)=m(x)m(y)k(|x-y|)
[\chi_R(x)-\chi_R(y)]
\quad(x\ne y).
\tag{8.2.2}
\]

因为

\[
|\chi_R(x)-\chi_R(y)|\le\min(2,C_\chi|x-y|),
\qquad \sup_{t>0}k(t)\min(2,C_\chi t)<\infty,
\]

Γ 核的 \(1/t\) 奇性被准确消去。差分非零时至少 \(|x|>R\) 或 \(|y|>R\)，因此

\[
\|[B,\chi_R]\|_{\rm HS}^2
\le C\|m\|_2^2\|m\mathbf1_{\{|x|>R\}}\|_2^2.
\tag{8.2.3}
\]

完整 theta 给 \(m(x)\le C r e^{-ar}\)，\(r=e^{2|x|}\)、\(a=\pi/2\)。换元积分即得

\[
\|m\mathbf1_{\{|x|>R\}}\|_2^2
\le C(1+e^{2R})e^{-\pi e^{2R}}.
\]

故吸收固定多项式因子后，

\[
\boxed{\|[B,\chi_R]\|_{2\to2}
\le C\exp[-(\pi/4)e^{2R}].}
\tag{8.2.4}
\]

该结论没有把原 Γ 算子本身当成有界算子；只有消去奇性后的交换子被证明有界。

### 8.3 完整素数交换子的 Schur 尾

记正对称移位核的行和

\[
W_S(x)=m(x)\sum_{n\ge2}\alpha_n[m(x-\log n)+m(x+\log n)]\le W(x).
\]

对右乘 \(\chi_R\) 的算子 \(S_m\chi_R\)，行和不超过 \(\|W_S\|_\infty\)，列和不超过
\(\sup_{|x|>R}W_S(x)\)，因为核对称且 \(\chi_R\) 支撑在尾部。因此 Schur 估计给

\[
\|S_m\chi_R\|_{2\to2}
\le\sqrt{\|W_S\|_\infty\sup_{|x|>R}W_S(x)}.
\tag{8.3.1}
\]

对离散移位核，该估计也可直接验证：在每个 \(x\) 对正权移位和用 Cauchy–Schwarz，再对平方积分并将 \(x\pm\log n\) 换元，得到同一行和/列和乘积。全部交换由正项及已有算子范数可和性支持。

\(\chi_RS_m=(S_m\chi_R)^*\)，而 \(C_0m^2\) 与 \(\chi_R\) 交换。结合 (8.1.1)，

\[
\boxed{\|[\mathcal V,\chi_R]\|_{2\to2}
\le C\exp[-(\pi/8)e^{2R}].}
\tag{8.3.2}
\]

由 (8.2.4)、(8.3.2)，

\[
\boxed{\|[P_\varepsilon,\chi_R]\|_{2\to2}
\le C_{\rm com}\exp[-(\pi/8)e^{2R}],}
\tag{8.3.3}
\]

常数与 \(\varepsilon\)、\(R\) 和所选归一态无关。

### 8.4 原方程的尾部强制性

置 \(u=\chi_Rv\)。该截断一般不保留原来的零均值约束；这里使用的是已经准确成立的全 \(L^2(dx)\) 强方程 \(P_\varepsilon v=0\) 及其全空间闭实现，而不是只在零均值子空间中的压缩弱方程。因此允许以 \(u\) 测试。

已证 \(v\in H^\infty\)，固定光滑截断保存这些空间；乘 \(m\) 后再作用对数乘子属于 \(L^2\)。故 \(u\in\operatorname{Dom}(P_\varepsilon)\)，并且

\[
P_\varepsilon u=[P_\varepsilon,\chi_R]v.
\tag{8.4.1}
\]

另一方面 \(B\ge0\)，\(u\) 支撑于 \(|x|>R\)，且 (8.1.2) 保证其上 \(W\le\varepsilon/2\)。所以

\[
\operatorname{Re}\langle u,P_\varepsilon u\rangle
\ge\varepsilon\|u\|_2^2-\int W|u|^2
\ge\frac\varepsilon2\|u\|_2^2.
\]

代入 (8.4.1)、(8.3.3) 与 \(\|v\|_2=1\)，得到

\[
\frac\varepsilon2\|u\|_2^2
\le C_{\rm com}e^{-(\pi/8)e^{2R}}\|u\|_2.
\]

若 \(u=0\) 已完成；否则约去 \(\|u\|_2\)。因 \(\chi_R=1\) 于 \(|x|\ge R+1\)，即得 (8.1.3)。

最后增大固定 \(C\)，使 \(C\ge2C_{\rm com}\)、\(C^2\ge C_W\)，并保证 (8.1.4) 对数合法。则
\(e^{-(\pi/8)e^{2R_{\varepsilon,\eta}}}\le\varepsilon\eta/C\)，(8.1.3) 给尾范数至多 \(\eta\)。同时

\[
C_We^{-(\pi/4)e^{2R_{\varepsilon,\eta}}}
\le(C_W/C^2)\varepsilon^2\eta^2
\le\varepsilon/2,
\]

故先前使用的尾部强制条件也已验证，没有循环选择。证毕。

### 8.5 与阈值空间逃逸的准确联合解释

[已证的阈值紧性](REPORT.md)给：若归一低态 \(\varepsilon_j\downarrow0\)，则对每个固定 \(R\)，
\(\|\mathbf1_{[-R,R]}v_j\|_2\to0\)。本稿同时给其质量不能在固定误差下跑出

\[
|x|\le\tfrac12\log\log(1/\varepsilon_j)+O_\eta(1)
\]

的移动窗口。因此真实潜在态的空间逃逸已被限制到一个明确、缓慢扩大的尺度。

两条结论彼此相容，不构成排谱。要继续排除仍须利用在这个移动空间窗口与已得移动零点窗口之间的真实算术耦合；本稿没有新增该联合符号估计，也不将局域化换称成低态不存在。

本稿只使用已证闭实现、\(H^\infty\)、原 Γ 跳跃表达、theta 尾和全素数 Schur 界。交换子与局域化推导的独立核验见 [REFEREE.md](REFEREE.md)，常数尚未数值化。
