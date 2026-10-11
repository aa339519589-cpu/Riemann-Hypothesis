# 原种子 theta 刚性及其不能自动传给本征态的准确边界

2026-10-11。延续真实删素—反射研究，保留已有谱对象。本轮只读继承原仓库 `74add2e1350dd4414d83dd46a4e10be8aeb7b42f` 的研究续篇及本轮已经形成的多项式反模型报告；不覆盖旧文件。

**状态：NO NEW UNCONDITIONAL RH THEOREM PROVED。** 本步证明一个确实排除多项式反模型的精确 theta/Mellin 刚性引理；并完成它向真实亚临界本征态转移时的循环审查。结论是：核的精确算术类可以识别，但“所有亚临界本征源仍在同一类”没有得到证明，而且此保类断言已承载 RH 的全部排谱难题。因此否决把该保类断言作为推导步骤。

这属于 Hamburger 型唯一性机制的一个直接特例，不主张文献首次。本文给出自足证明，不把已知唯一性定理当成零点定位定理。

## 1. 固定对象与本轮实际新增

本轮采用第五轮的 x 尺度：

\[
\Phi_n(x)=(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})
e^{-\pi n^2e^{2x}},\qquad \Phi=\sum_{n\ge1}\Phi_n.
\]

Fourier 约定为 \(\widehat f(z)=\int f(x)e^{izx}dx\)，并有
\(\widehat\Phi(z)=\xi(1/2+iz)\)。定义双边 Mellin 变换及固定完成因子

\[
\mathcal M f(s)=\int_{\mathbb R}f(x)e^{(s-1/2)x}dx,
\qquad
G(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\]

对真实核，\(\mathcal M\Phi(s)=\xi(s)=G(s)\zeta(s)\)。在 \(\Re s>1\)，定义
\(D_f(s)=\mathcal M f(s)/G(s)\)。这里 G 没有零点或极点。

实际新增的三个精确陈述是：

1. 使用**完全不变的单高斯二次种子**时，任何多项式增长系数序列，只要其完整模态和是偶函数，系数就必须全部相同。
2. 对偶、双指数衰减 f，如果固定 G 的商 D_f 是某右半平面绝对收敛的普通 Dirichlet 级数，则 f 只能是常数倍 Φ。特别地，非零零极点矩本征源不可能同时属于这个类。
3. 真实双向素数移位的逐项双边 Mellin 积分，在任何直线上都没有绝对交换区间。因而不能从同一源方程直接推出第 2 项的 Dirichlet 保类性质。

## 2. 高斯测试函数分离偶温和分布

### 引理 1

若 T 是实轴上的偶温和分布，并且对每个 \(t>0\) 有

\[
\langle T,e^{-\pi t x^2}\rangle=0,
\tag{2.1}
\]

则 \(T=0\)。

### 证明

映射 \(t\mapsto e^{-\pi t x^2}\) 在任意紧子区间 \(t>0\) 内可于 Schwartz 拓扑逐次微分。于 t=1 微分任意次，得到

\[
\langle T,x^{2k}e^{-\pi x^2}\rangle=0\quad(k\ge0).
\]

由于 T 偶，所有奇次幂的配对也为零。考虑

\[
H(z)=\langle T,e^{-\pi x^2}e^{-2\pi izx}\rangle,
\qquad z\in\mathbb C.
\]

高斯因子保证括号中的函数及其每阶 z 导数，在 z 的紧集上有一致 Schwartz 半范数界；因此 H 是整函数。其在零点处的所有导数都是前述零配对，故 H 恒等于零。

在实轴上，H 是温和分布 \(e^{-\pi x^2}T\) 的 Fourier 变换。Fourier 单射性给
\(e^{-\pi x^2}T=0\)。对每个紧支光滑测试函数 \(\varphi\)，函数
\(e^{\pi x^2}\varphi\) 仍紧支光滑，所以 \(\langle T,\varphi\rangle=0\)。故 T=0。证毕。

此引理中的“偶”不可遗漏：奇分布自动消灭全部中心高斯，却未必为零。

## 3. 原单模态与全反射迫使整数系数恒定

### 定理 2（原种子 theta 刚性）

设 \(a_n\in\mathbb C\) 且存在 C,A 使 \(|a_n|\le C(1+n)^A\)。定义

\[
F_a(x)=\sum_{n\ge1}a_n\Phi_n(x).
\]

该和及任意固定阶导数在实轴紧集上一致绝对收敛。如果 \(F_a(x)=F_a(-x)\) 对全部实 x 成立，则存在 \(c\in\mathbb C\) 使

\[
\boxed{a_n=c\ \ (n\ge1),\qquad F_a=c\Phi.}
\tag{3.1}
\]

不需要假设正性、RH、任何零点位置或临界谱隙。

### 证明：第一步，准确恢复 theta 反射

令

\[
U_a(x)=e^{x/2}\sum_{n\ge1}a_ne^{-\pi n^2e^{2x}}.
\]

原模态的二次多项式形状准确给出

\[
\boxed{(\partial_x^2-1/4)U_a(x)=F_a(x).}
\tag{3.2}
\]

这是本轮真正使用而多项式变形没有保留的种子数据。若 F_a 偶，则
\(V(x)=U_a(x)-U_a(-x)\) 满足 \(V''-V/4=0\)，且 V 奇。故某常数 C 满足

\[
V(x)=C\sinh(x/2).
\]

取 \(a_0=-C\)，定义

\[
\Theta_a(t)=a_0+2\sum_{n\ge1}a_ne^{-\pi n^2t},\qquad t>0.
\]

于是 \(e^{x/2}\Theta_a(e^{2x})=a_0e^{x/2}+2U_a(x)\) 是偶函数，等价于

\[
\boxed{\Theta_a(t)=t^{-1/2}\Theta_a(1/t)\quad(t>0).}
\tag{3.3}
\]

零项 a₀ 不是任意补入的自由参数；它由 (3.2) 的反射缺陷 C 唯一确定。

### 第二步，提升为真正的 Fourier 自对偶分布

采用本节标准 Fourier 约定
\(\mathcal F\varphi(\xi)=\int\varphi(x)e^{-2\pi ix\xi}dx\)。令

\[
\mu=a_0\delta_0+\sum_{n\ge1}a_n(\delta_n+\delta_{-n}).
\]

多项式增长使 μ 是偶温和分布。高斯 Fourier 公式与 (3.3) 给

\[
\langle\widehat\mu,e^{-\pi t x^2}\rangle
=t^{-1/2}\Theta_a(1/t)=\Theta_a(t)
=\langle\mu,e^{-\pi t x^2}\rangle.
\]

引理 1 应用于偶分布 \(\mu-\widehat\mu\)，得到

\[
\widehat\mu=\mu.
\tag{3.4}
\]

### 第三步，整数支撑的刚性

因为 μ 是整数点的 δ 质量和、没有 δ 导数，准确有 \(e^{2\pi ix}\mu=\mu\)。Fourier 变换遂给 \(\widehat\mu\) 为 1 周期温和分布。这里不能对任意“支撑于整数”的含 δ 导数分布作同样推断。由 (3.4)，μ 自身也 1 周期。

在任意单个整数点附近取支撑长度小于 1 的测试函数，再逐次平移整数，周期性说明该点的 δ 权重与原点相同。因此 \(a_n=a_0\) 对所有 n 成立，得到 (3.1)。证毕。

### 排除多项式反模型的准确含义

对 \(K=P(\partial^2)\Phi/P(1/4)\)，如果 K 还能表示为上述同种子的 \(F_a\)，定理 2 迫 K=cΦ。Fourier 变换给
\([P(-z^2)/P(1/4)-c]\Xi(z)=0\)，所以多项式 P 必恒定。已归一极点矩再给 c=1。

本结论没有要求任何有限采样、有限矩或源方程的近似。恰是“同一个原始种子 + 全整数模态 + 全实轴偶性”这组无限信息排除了变形。

## 4. 固定 Gamma 因子的 Dirichlet 类刚性

### 引理 3：一个单模态的完整 Mellin 变换

对 \(\Re s>1\)，换元 \(u=\pi n^2e^{2x}\) 得

\[
\int_{\mathbb R}\Phi_n(x)e^{(s-1/2)x}dx
=n^{-s}\pi^{-s/2}
\{2\Gamma(s/2+2)-3\Gamma(s/2+1)\}
=n^{-s}G(s).
\tag{4.1}
\]

同一换元也给
\(\int|\Phi_n(x)|e^{(\sigma-1/2)x}dx=C_\sigma n^{-\sigma}\)，其中 \(0<C_\sigma<\infty\)。因此绝对收敛的普通 Dirichlet 级数允许在这一步真正换序。

### 定理 4

设 f 为偶连续函数，并且对每个实 σ 有
\(\int|f(x)|e^{(\sigma-1/2)x}dx<\infty\)。假如在某个右半平面有

\[
D_f(s)=\frac{\mathcal Mf(s)}{G(s)}
=\sum_{n\ge1}a_nn^{-s},
\tag{4.2}
\]

右侧在该半平面绝对收敛，则

\[
\boxed{f=c\Phi,\qquad a_n=c\quad(n\ge1).}
\tag{4.3}
\]

### 证明

在任一绝对收敛直线 \(\Re s=\sigma_0\) 上，\(|a_n|\le Cn^{\sigma_0}\)，所以定理 2 的多项式增长条件满足。令 \(F_a=\sum a_n\Phi_n\)，固定另一条 \(\sigma>\max(1,\sigma_0)\) 的直线。引理 3 的绝对积分估计保证 F_a 经 \(e^{(\sigma-1/2)x}\) 加权后属于 L¹，并且

\[
\mathcal M F_a(\sigma+it)
=G(\sigma+it)\sum a_nn^{-\sigma-it}
=\mathcal M f(\sigma+it)
\quad(t\in\mathbb R).
\]

L¹ Fourier 唯一性说明 \(f=F_a\) 几乎处处；两边连续，故处处相同。f 偶，定理 2 遂给 (4.3)。证毕。

### 有限微分族的更弱检验

只对有限多项式微分族，有更简单的必要条件：

\[
D_K(s)=\frac{P((s-1/2)^2)}{P(1/4)}\zeta(s).
\tag{4.4}
\]

因为 \(\zeta(\sigma)\to1\)，单单要求 D_K(σ) 在 \(\sigma\to+\infty\) 有界就迫 P 恒定。普通绝对收敛 Dirichlet 级数在右端趋于其首系数，这一点从任一固定绝对收敛直线上的支配收敛直接得到。

不能把这个“有限微分族中有界即刚性”的结论推广到任意 f；下一节给出严格区别。

## 5. 与真实亚临界本征态的接口，以及已否决的循环步骤

继承真实本征态定义：\(Lq=\lambda q\)，\(0<\lambda<1/2\)，q 实偶，
\(f=\Phi q\)，\(g=2hq\)，\(h=\cosh(x/2)\)。已建立的条件是

\[
q\in\mathcal S(\mathbb R),\quad f\text{ 及固定阶导数双指数衰减},\quad
\int f(x)e^{\pm x/2}dx=0.
\tag{5.1}
\]

### 推论 5

任何满足 (5.1) 的非零偶 f，其固定 Gamma 商 D_f **不可能**在任何右半平面成为绝对收敛的普通 Dirichlet 级数。

证明：若是，定理 4 给 f=cΦ；但极点矩给 \(0=\int fe^{x/2}=c/2\)，所以 f=0，矛盾。

因此，拟议转移步骤

> “真实算子来自精确 theta/Mellin 结构，所以每个亚临界本征源 f 的 D_f 仍是普通 Dirichlet 级数”

并非由核的刚性得到的推论。结合已有的 RH⇔无亚临界本征态，它与 RH 等价：若它成立，推论 5 排除全部非零态；若 RH 成立，根本没有这些态，陈述空真。

**本步明确否决这一保类断言作为证明步骤。** 本文没有用“核唯一”等价替代“全部零点在临界线”。接下来的检查转向能否从源方程合法导出该类，得到以下严格交换障碍。

## 6. 双向素数算子没有可供逐项 Mellin 化的绝对公共域

令

\[
Sf(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
[f(x-\log n)+f(x+\log n)].
\]

### 命题 6

对任意非零 f，若其每个实指数加权 L¹ 范数有限，则对**任何**实 σ 都有

\[
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\int_{\mathbb R}e^{(\sigma-1/2)x}
\{|f(x-\log n)|+|f(x+\log n)|\}\,dx=\infty.
\tag{6.1}
\]

### 证明

分别换元，左侧准确等于

\[
\left(\int_{\mathbb R}|f(y)|e^{(\sigma-1/2)y}dy\right)
\sum_{n\ge2}\Lambda(n)(n^{\sigma-1}+n^{-\sigma}).
\tag{6.2}
\]

第一因子严格正且有限。第一个素数幂级数的绝对收敛要求 \(\sigma<0\)；第二个要求 \(\sigma>1\)。二者没有交集。端点发散例如由无条件 \(\psi(X)\sim X\) 或 ζ 的简单极点及正系数得到。因此 (6.1) 成立。

它排除的是把完整 S 在某个双边 Mellin 直线上逐项写成两个收敛对数导数的那一步；并不排除有额外证明的分布正则化或单侧延拓。精确源方程的存在和局部素数和的收敛，不能补出一个不存在的全轴绝对交换区间。

## 7. 真本征态已有的弱 Mellin 归一并不能承担排极点

### 引理 7

设 q 有界且 \(q(x)\to0\) 当 \(x\to+\infty\)，令 f=Φq。则

\[
\frac{\mathcal Mf(\sigma)}{\xi(\sigma)}\longrightarrow0,
\qquad D_f(\sigma)\longrightarrow0\quad(\sigma\to+\infty).
\tag{7.1}
\]

证明：定义概率测度

\[
d\mu_\sigma(x)=\frac{\Phi(x)e^{(\sigma-1/2)x}}{\xi(\sigma)}dx.
\]

对固定 R 和 \(\sigma>1/2\)，分母在 \([R+1,R+2]\) 的积分给
\(\mu_\sigma(({-\infty},R])\le C_Re^{-(\sigma-1/2)}\to0\)。
因此质量逃向正无穷，\(\int q\,d\mu_\sigma\to0\)。这就是第一式；第二式再用 \(\xi/G=\zeta\to1\)。

真实亚临界态已满足此引理，但它只证明实轴端的极限，没有给出复域普通 Dirichlet 级数表示。

### 一个精确的弱条件反例

这不是亚临界本征态反例，只用于严格界定 (7.1)、极点矩和光滑衰减能推出多少。

任取 \(a>0,0<\delta<1/2\)，令
\(g_0(x)=\cos(ax)\cosh(\delta x)\)，\(f_0=\Phi g_0/(2h)\)。取非零、非负、偶的
\(b\in C_c^\infty((-1,1))\)，并置

\[
d=\frac{\int f_0h}{\int bh},\quad
f=f_0-db,\quad q=f/\Phi,\quad g=2hq.
\tag{7.2}
\]

准确有：q 实偶、Schwartz，f 及全部固定阶导数双指数衰减，两个极点矩均为零，并且 (7.1) 成立。另一方面

\[
g=g_0-2hd\,b/\Phi,
\]

修正项紧支。故单侧 Laplace 变换的亚纯延拓为

\[
\int_0^\infty e^{-wx}g(x)dx
=\frac14\sum_{\epsilon,\eta\in\{\pm1\}}
\frac1{w-\epsilon\delta-i\eta a}-H(w),
\tag{7.3}
\]

H 整函数。四个极点互不相同，留数全为 1/4，特别有两个不可去的右半平面极点 \(w=\delta\pm ia\)。

原 Φ 的精确 theta/Γζ 身份在此完全没有改动，但一般态的弱 Mellin 归一不会迫使 g 的右半平面极点可去。这个例子**没有**被声称满足完整本征方程或全部平移正交；正是那些尚待利用的约束，必须承担真正排极点的证明。

## 8. 本轮验收与仍剩的承重命题

- 已证明：原种子+全偶反射的系数刚性；固定 Gamma 的绝对 Dirichlet 类刚性；双向素数算子的全轴绝对 Mellin 交换障碍。
- 已排除：把核的唯一性直接传给本征源，或者把实轴有界/趋零的 Mellin 商当作普通 Dirichlet 级数。
- 已明确：有限多项式反模型确实被原种子/Dirichlet 类排除；因此该结构比“正偶+极点矩+同源方程”严格更强。
- 未证明：从真实本征方程得到一个不等价偷换 RH 的新约束，消去每个活动离轴系数或其右半平面 Laplace 留数。

所以本轮不能将“找到足够识别 Φ 的数据”称为“证明 Φ 的 Fourier 零点全实”。若继续，必须在真实本征方程上新增可独立证出的量化估计；不得重新引入本节已否决的 Dirichlet 保类公设。

## 9. 来源、复核边界

- 继承：`history/source-materials/RH_研究续篇_20261011.md` 的附录 5–8、13–15，以及本轮 `polynomial_source_countermodel` 研究：真实算术源方程不能唯一识别 Fourier 零点集合。
- 一般背景：[Burnol, Deux extensions de Théorèmes de Hamburger](https://arxiv.org/abs/1106.4749)。该文研究 Dirichlet 级数函数方程与温和分布的联系；本文定理 2、4 作为该类经典唯一性思想的直接特例，不主张新创。
- 标准公式：[DLMF §20.7(viii), theta transformations](https://dlmf.nist.gov/20.7#viii)；[DLMF §27.4, Euler products and Dirichlet series](https://dlmf.nist.gov/27.4)。本文的分布、ODE 和交换证明均实际写出，没有把文献的 RH 等价判据当作正性证明。
- 所附准确代数脚本仅检查种子微分、Gamma 归一代数和 Laplace 极点留数，不承担分布唯一性及全量词。首次检查因 SymPy 未将 sinh 自动化为指数而未通过字面零判断；显式作等价指数改写后重新运行通过，没有改动数学身份。本文新推导尚未进行形式化内核验证。
