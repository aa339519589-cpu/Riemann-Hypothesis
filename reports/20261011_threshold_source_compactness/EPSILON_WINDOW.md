# ε 常数的真实量化与一个受控移动零点窗口

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
