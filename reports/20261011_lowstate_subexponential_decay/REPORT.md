# 真实低态的近指数 Fourier 刚性：Γ 对数阶被对数权交换子准确抵消

2026-10-11。保留完整 theta、全部素数幂移位和原 Γ 乘子，证明真实亚临界本征态的近指数 Fourier 衰减。**RH 与亚临界谱排除均未证明。**

## 1. 固定真实对象与结论

沿用

\[
\Phi(x)=\sum_{n\ge1}(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})e^{-\pi n^2e^{2x}},
\quad h(x)=\cosh(x/2),\quad
m(x)=\sqrt{\Phi(x)/(2h(x))}.
\]

设非零实偶 \(q\in\operatorname{Dom}(L_+)\) 满足真实亚临界本征方程 \(L_+q=\lambda q\)、\(0<\lambda<1/2\)。这里 \(L_+\) 是完整真实跳跃算子在偶子空间的限制；以下简记为 L。置

\[
\varepsilon=1/2-\lambda>0,\quad v=\sqrt{2\Phi h}\,q,
\quad f=mv=\Phi q,\quad F(z)=\int_{\mathbb R}f(x)e^{izx}\,dx.
\]

继承 [附录 5 第 2–3 节](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/history/source-materials/RH_%E7%A0%94%E7%A9%B6%E7%BB%AD%E7%AF%87_20261011.md#L1438-L1633) 的准确算子、弱阶强制估计 (G) 与正则性结论 (R)，其域核验见 [附录 6](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/history/source-materials/RH_%E7%A0%94%E7%A9%B6%E7%BB%AD%E7%AF%87_20261011.md#L1823-L2224)：

\[
Pv=0,\quad P=M_m b(D)M_m+\varepsilon-V,\quad v\in\bigcap_{s\ge0}H^s(\mathbb R),
\tag{I.1}
\]

\[
V=C_0M_{m^2}+\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\sum_{\pm}M_{m(x)m(x\pm\log n)}\tau_{\pm\log n},
\quad (\tau_d u)(x)=u(x+d),
\tag{I.2}
\]

其中 \(b(\xi)=\Re\psi(1/4+i\xi/2)-\log\pi+C_0\)、\(C_0=\gamma+\pi/2+3\log2+\log\pi\)，故 \(b\ge0\)、\(b(\xi)=O(\log(2+|\xi|))\)。取 Fourier 约定 \(\widehat f(\xi)=\int f(x)e^{ix\xi}dx\)，并定义 \(\langle\xi\rangle=(1+\xi^2)^{1/2}\)。在形式域上

\[
\langle u,Pu\rangle\ge\frac\varepsilon2\|u\|_2^2
-C_\varepsilon\|u\|_{H^{-1}}^2.
\tag{I.3}
\]


本文使用上面的已证强制估计；以下重复记为

\[
\operatorname{Re}\langle u,Pu\rangle
\ge\frac\varepsilon2\|u\|_2^2-C_\varepsilon\|u\|_{H^{-1}}^2.
\tag{1.1}
\]

附录 A 的完整 theta 证明提供某 \(a>0\) 及统一指数 Fourier 包络：

\[
|\widehat m(t)|+|\widehat{m^2}(t)|+
\sum_{n\ge2,\pm}|\widehat{a_{n,\pm}}(t)|\le C e^{-a|t|}.
\tag{1.2}
\]

该证明包括：完整核在窄复条带的零自由性、正支平方根、全 \(x\) 的双指数包络，以及所有真实移位系数的 \(e^{-cn}\) 水平积分界。没有将逐个 \(n\) 解析性误作统一可和性。

定义固定偶函数

\[
\ell(t)=\log(e+|t|),\qquad
\omega(t)=\int_0^{|t|}\frac{dr}{\log(e+r)}.
\tag{1.3}
\]

当 \(|t|\to\infty\)，有 \(\omega(t)\sim |t|/\log|t|\)。

### 定理 1

存在只依赖真实固定系数的常数 \(c_*>0\)，对每个上述真实亚临界本征态有

\[
\boxed{e^{c_*\varepsilon\omega(D)}v\in L^2(\mathbb R).}
\tag{1.4}
\]

因而对任意有限 \(B>0\)，

\[
\boxed{\sup_{|\operatorname{Im}z|\le B}
e^{c_*\varepsilon\omega(\operatorname{Re}z)}|F(z)|<\infty.}
\tag{1.5}
\]

对固定 \(\varepsilon_0>0\)，所有 \(\varepsilon\ge\varepsilon_0\) 的归一态 \(\|v\|_2=1\) 可统一选取指数 \(c_*\varepsilon_0\)，且其 (1.4)、(1.5) 常数也统一有界。此处只声称本征态的统一界，不额外声称任意谱子空间向量的同一估计。

式 (1.4) 严格加强全部非解析 Gevrey 权：对每个 \(0<\alpha<1\)、\(A>0\)，\(A|t|^\alpha=o(\omega(t))\)。本稿没有证明真正的 \(e^{c|D|}\) 权，也没有把近指数频率衰减误作空间尾 \(g=2hq\) 的温和性。

## 2. 对数权的两个准确差商界

### 引理 2

对全部实 \(\xi,\eta\)，令 \(k=\xi-\eta\)，则

\[
|\omega(\xi)-\omega(\eta)|\le\omega(k)\le|k|,
\tag{2.1}
\]

\[
|\omega(\xi)-\omega(\eta)|
\le C\frac{|k|\ell(k)}{\ell(\eta)}.
\tag{2.2}
\]

并且 \(\ell(\xi)\le C\ell(k)\ell(\eta)\)。

证明：\(\omega\) 在正半轴递增、凹且 \(\omega(0)=0\)，所以次可加；结合 \(||\xi|-|\eta||\le|k|\) 得 (2.1)。若 \(|k|\le|\eta|/2\)，线段 \(\eta+\theta k\) 不穿零，且 \(|\eta+\theta k|\ge|\eta|/2\)。均值定理给

\[
|\omega(\xi)-\omega(\eta)|\le C|k|/\ell(\eta),
\]

强于 (2.2)。若 \(|k|>|\eta|/2\)，则 \(\ell(\eta)\le C\ell(k)\)，用 (2.1) 即得 (2.2)。最后 \(|\xi|\le|\eta|+|k|\)，故 \(\ell(\xi)\le\ell(\eta)+\ell(k)\le2\ell(\eta)\ell(k)\)，因为 \(\ell\ge1\)。证毕。

## 3. 统一截顶权与准确的一对对数交换子估计

固定 \(0<\tau\le a/2\)，定义

\[
W_N(\xi)=\exp[\tau\min(\omega(\xi),N)],\qquad
K_{a_0,N}=[W_N,M_{a_0}]W_N^{-1}.
\tag{3.1}
\]

这里 \(a_0\) 表示一般系数，不是 (1.2) 的条带常数。截顶权不要求光滑；固定 \(N\) 时有界可逆，并保存每个 Sobolev 空间。

### 引理 3

对 (1.2) 中的每个系数 \(a_0\)，有对 \(N\) 一致的

\[
\|K_{a_0,N}\ell(D)\|_{2\to2}
+\|\ell(D)K_{a_0,N}\|_{2\to2}
\le C_{a_0}\tau.
\tag{3.2}
\]

对全部素数幂系数，常数 \(C_{a_{n,\pm}}\) 可绝对求和。

证明：截顶映射 1-Lipschitz，由引理 2 得交换子的 Fourier 核界

\[
|\widehat{a_0}(k)|
\left|\frac{W_N(\xi)}{W_N(\eta)}-1\right|
\le C\tau|\widehat{a_0}(k)|\,
|k|\ell(k)e^{\tau|k|}/\ell(\eta).
\tag{3.3}
\]

对右乘 \(\ell(D)\)，分母直接消去；对左乘 \(\ell(D)\)，利用 \(\ell(\xi)/\ell(\eta)\le C\ell(k)\)。两者均由 Young 不等式归约至

\[
C\tau\int|\widehat{a_0}(k)|\,|k|\ell(k)^2e^{\tau|k|}\,dk.
\tag{3.4}
\]

由 (1.2)、\(\tau\le a/2\)，该积分除去 \(\tau\) 后统一有限，且全部移位常数的和有限。证毕。

## 4. Γ 的对数阶在共轭误差中恰好消去

因真实 \(b(\xi)=O(\ell(\xi))\)，乘子 \(b/\ell\) 在 \(L^2\) 有界。记 \(K_N=K_{m,N}\)。直接展开共轭得到准确身份

\[
R_N:=W_NPW_N^{-1}-P
=M_m bK_N+K_NbM_m+K_NbK_N-\Delta V_N,
\tag{4.1}
\]

\[
\Delta V_N=C_0K_{m^2,N}+
\sum_{n\ge2,\pm}K_{a_{n,\pm},N}\tau_{\pm\log n}.
\]

引理 3 同时控制 \(bK_N\) 与 \(K_Nb\)，不是只控制其中一个方向。又因 \(\ell\ge1\)，\(\|K_N\|\le C\tau\)。全部平移在 \(L^2\) 等距，因此存在只依赖固定真实系数的 \(C_*>0\)，使

\[
\boxed{\sup_N\|R_N\|_{2\to2}\le C_*(\tau+\tau^2)
\qquad(0<\tau\le a/2).}
\tag{4.2}
\]

这一步正是新的闭合机制：对数权差商提供 \(\ell(\eta)^{-1}\)，准确抵消 Γ 乘子的 \(\ell\) 阶。不需要用任意小正幂损失替代它。

## 5. 真实强制估计吸收误差

取

\[
c_*:=\min\{a,1,(8C_*)^{-1}\}>0,\qquad \tau=c_*\varepsilon.
\tag{5.1}
\]

因 \(0<\varepsilon<1/2\)，有 \(\tau\le a/2\)、\(\tau<1\)，且

\[
C_*(\tau+\tau^2)\le2C_*\tau\le\varepsilon/4.
\]

置 \(u_N=W_Nv\)。已有 \(v\in H^\infty\)，故固定 \(N\) 时 \(u_N\in H^\infty\)，\(b(D)(mu_N)\in L^2\)，并由原闭形式实现得 \(u_N\in\operatorname{Dom}(P)\)。没有依赖 \(W_N\) 的光滑性，也没有使用尚未证明的无限权入域。

由 \(Pv=0\)、(4.1)，\(Pu_N=-R_Nu_N\)。将 (4.2) 吸收进 (1.1)，得到

\[
\frac\varepsilon4\|u_N\|_2^2
\le C_\varepsilon\|u_N\|_{H^{-1}}^2.
\tag{5.2}
\]

对固定 \(K\ge1\)，直接在 Fourier 侧拆分平方范数，

\[
\|u_N\|_{H^{-1}}^2
\le\langle K\rangle^{-2}\|u_N\|_2^2
+e^{2\tau\omega(K)}\|v\|_2^2.
\]

选择与 \(N\) 无关的 \(K\)，使 \(C_\varepsilon\langle K\rangle^{-2}\le\varepsilon/8\)。于是

\[
\sup_N\|W_Nv\|_2^2
\le\frac{8C_\varepsilon}\varepsilon
e^{2\tau\omega(K)}\|v\|_2^2<\infty.
\tag{5.3}
\]

单调收敛给 (1.4)。若 (1.1) 恰可取 \(C_\varepsilon=0\)，则 (5.2) 已直接迫使 \(v=0\)，无需另选 \(K\)。

若 \(\varepsilon\ge\varepsilon_0>0\)，使用固定算子 \(P_{\varepsilon_0}\) 的 Gårding 常数即可：\(P_\varepsilon=P_{\varepsilon_0}+(\varepsilon-\varepsilon_0)I\) 仍满足以 \(\varepsilon_0/2\)、\(C_{\varepsilon_0}\) 写的 (1.1)。取统一 \(\tau=c_*\varepsilon_0\)，以上整个推导对归一态统一成立。

## 6. 源的水平复条带估计及完整零点尾

对 \(|b|\le B\)，令 \(a_b(x)=e^{-bx}m(x)\)。同一 theta 条带移线证明给 \(|\widehat{a_b}(t)|\le C_Be^{-a|t|}\)，必要时把最初固定 \(a\) 缩小一次，仍对全部有限固定 \(B\) 可用。

卷积先由 L² Fourier 恒等式成立；绝对收敛与 L² 平移连续性给出连续函数，因此该式与真正连续的 F 在每个实 t 一致，可以代入每个复零点。因为 \(\omega\) 次可加，

\[
e^{\tau\omega(t)}|F(t+ib)|
\le\frac1{2\pi}\int
e^{\tau\omega(t-\eta)}|\widehat{a_b}(t-\eta)|
e^{\tau\omega(\eta)}|\widehat v(\eta)|\,d\eta.
\]

由 \(\omega(k)\le|k|\)、\(\tau\le a/2\) 及 Cauchy–Schwarz，右侧被统一有限常数控制，得到 (1.5)。

取 \(\Xi\) 的全部零点集 \(Z\)（不假设其为实数），重数为 \(m_w\)。对任意固定 \(k\ge0\)，零点计数和 (1.5) 给

\[
\boxed{\sum_{w\in Z,\,|\operatorname{Re}w|>T}
m_w(1+|w|)^k|F(w)|
\le C_{k,v,\varepsilon}\exp[-\tfrac12c_*\varepsilon\omega(T)].}
\tag{6.1}
\]

证明只需把 (1.5) 的指数拆成两半，一半控制 \(T\)，余下加权和绝对收敛。全零点展开 \(\varepsilon g=-\sum_wm_wF(w)e^{-iwx}\)、\(g=2hq\)，因此其 \(k\) 阶导数尾另乘 \(e^{|x|/2}/\varepsilon\) 即得。

## 7. 本结果可用来做什么，以及还缺什么

正向新增的是一个真实本征态必须满足的近指数频率条件，指数率可取固定常数乘谱距 \(\varepsilon\)。因此它比仅知任意幂衰减更适合对真实全零点选择方程的无限高频部分作严格估计。固定距离阈值的归一态还有统一版本。

仍有两个准确限制：

1. \(C_\varepsilon\) 以及最终范数常数在 \(\varepsilon\downarrow0\) 时没有得到有效统一控制，而近指数率 \(c_*\varepsilon\) 本身亦趋零；因此不能由固定精度的有限截断排除所有贴近阈值的态。
2. 即便任何固定 \(\varepsilon\) 的高频尾被强力压低，某个有限活动离轴零点上的 \(F(w)\ne0\) 仍与 (1.5) 相容。单侧 Laplace 留数 \(-m_wF(w)/\varepsilon\) 不会仅因高频衰减自动消失。

故本稿没有把近指数正则性称为 RH 证明，也没有把它重写成 RH 等价的“全部活动系数消失”假设。下一承重步骤仍须把完整真实算术方程与这个频率约束结合，取得跨越 \(\varepsilon\downarrow0\) 的符号控制或活动系数消失定理。

## 8. 自足性与继承边界

本稿新的对数权差商、双向交换子、全部真实移位求和、共轭域、吸收和复 Fourier 推导均已写出；仅继承此前独立审核过的准确算子、\(H^\infty\) 与 Gårding 输入；theta 条带引理在附录 A 完整证明。尚未进行形式化内核验证，不主张新文献优先权。

## 附录 A：真实 theta 系数的统一解析包络

### 引理 A

存在 \(a,c,C,A>0\)，使 \(m\) 在 \(|\operatorname{Im}z|<2a\) 中有与实轴正平方根一致的全纯延拓，并在闭条带 \(|\operatorname{Im}z|\le a\) 满足

\[
|m(x+iy)|\le C e^{A|x|}\exp(-c e^{2|x|}).
\tag{A.1}
\]

此外，若 \(a_{n,\pm}(x)=\Lambda(n)n^{-1/2}m(x)m(x\pm\log n)\)，则对某 \(a_1,c_1,C_1>0\)，

\[
|\widehat m(t)|\le C_1e^{-a_1|t|},\quad
|\widehat{m^2}(t)|\le C_1e^{-a_1|t|},\quad
\sum_{n\ge2,\pm}|\widehat{a_{n,\pm}}(t)|\le C_1e^{-a_1|t|}.
\tag{A.2}
\]

### 证明

首先固定任意 \(0<a_0<\pi/4\)。theta 级数在 \(|\operatorname{Im}z|<\pi/4\) 的紧集上正规收敛，因而全纯。原核实轴偶性通过恒等原理提升为该条带内的 \(\Phi(z)=\Phi(-z)\)。

令 \(u=\pi e^{2z}\)。当 \(x\to+\infty\)、\(|y|\le a_0\) 时，第一模态为 \(e^{z/2}(4u^2-6u)e^{-u}\)，无零；其余模态与它的比值之和在绝对值上由

\[
C\sum_{n\ge2}n^4\exp[-\pi(n^2-1)e^{2x}\cos(2a_0)]
\]

控制，统一趋于零。故在某 \(x\ge R\) 的闭半条带内 \(\Phi\) 无零。偶反射给 \(x\le-R\) 的同样结论。在剩余紧实段 \([-R,R]\)，已知 \(\Phi>0\)，连续性给一个零自由复邻域。取更小条带即可使整个条带无零。

\(2h(z)\) 在 \(|\operatorname{Im}z|<\pi\) 无零，且整个条带单连通，故 \(\Phi/(2h)\) 有全纯对数与平方根；选取实轴正支。前述 theta 包络、偶性及 \(|h(x+iy)|\ge\cos(y/2)\cosh(x/2)\) 给 (A.1)，必要时再次缩小条带。

对 \(d=\log n\)，置 \(r=e^{2|x|}\)、\(s=e^{2|x\pm d|}\)。有 \(rs\ge n^2\)、\(r+s\ge2n\)。将 (A.1) 的有限指数前因子吸收入一部分 \(e^{-c(r+s)}\)，可得统一水平线积分界

\[
\int_{\mathbb R}|a_{n,\pm}(x+iy)|\,dx
\le C\frac{\Lambda(n)}{\sqrt n}e^{-c'n}
\quad(|y|\le a'),
\tag{A.3}
\]

其中 \(0<a'<a\) 固定。详细地，保留的一部分指数用于 \(r+s\ge2n\) 给 \(e^{-c'n}\)，另一部分以 \(e^{-c''r}\) 控制 \(x\) 积分。该包络也让移位 Fourier 积分的矩形竖边在 \(x\to\pm\infty\) 时消失。

在 Fourier 积分中向上或向下移动固定距离 \(a'\)，得到

\[
|\widehat{a_{n,\pm}}(t)|\le
C\Lambda(n)n^{-1/2}e^{-c'n}e^{-a'|t|}.
\]

由 \(\Lambda(n)\le\log n\) 可对全部真实素数幂求和。\(m,m^2\) 同理。这证明 (A.2)。这里证明的是统一全体移位系数估计，不是逐个 \(n\) 的解析性。证毕。


## 来源与使用范围

- [《RH 研究续篇》附录 5、6](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/history/source-materials/RH_%E7%A0%94%E7%A9%B6%E7%BB%AD%E7%AF%87_20261011.md#L1408-L2224)：准确酉算子、域、\(H^\infty\) 正则性与 (1.1)；[附录 7、8](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/history/source-materials/RH_%E7%A0%94%E7%A9%B6%E7%BB%AD%E7%AF%87_20261011.md#L2228-L2700)：完整全零点展开与活动留数。
- [theta/Dirichlet 刚性](../20261011_theta_dirichlet_rigidity/REPORT.md)：固定种子刚性不可自动传给本征源。本稿没有使用被否决的保类断言。
- 标准 theta 变换背景：[DLMF §20.7](https://dlmf.nist.gov/20.7)。本文只用继承已证的实轴偶性，复条带提升、非零性、全体移位估计与指数权交换子均在正文证明。

本文未进行形式化内核验证。主要结论由上述解析证明承担，未用有限数值测试替代无限量词。
