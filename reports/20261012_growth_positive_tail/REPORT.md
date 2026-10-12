# 完整竖向增长核的全参数正算术尾

2026-10-12。只读基线：`d74308ed56639ddf0505f1e50007f79337d367da`。
最终目标仍是对每个非平凡零点证明实部为 1/2。

本稿直接推进已有的完整 theta 增长核，而非把目标改为零点比例。
证明的新范围是：**对每个连续参数 0<y≤1/2，每个整数算术块 r≥2 的增长核偶延拓都有严格正的全实频率 Fourier 变换**。全部这些块的无限和也正定。此前已有 y=0 的一阶 Laguerre 算术尾正定性，以及全 y 的一阶斜率符号；本稿证明全 y 的二阶空间凸性，不把旧结论重复记为新增。

第一块与完整正尾的全频比较仍未证明，因此没有完成 RH 证明。新结论没有使用第五轮待完整复审的谱识别，也没有使用准 RH 输入、零点简单性或已知零点表。不主张文献首次。

## 1. 固定真实对象与完整身份

采用

\[
\Phi(x)=\sum_{n\ge1}(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})e^{-\pi n^2e^{2x}},
\quad\widehat\Phi(z)=\Xi(z)=\xi(1/2+iz).
\]

Fourier 约定为 \(\widehat f(k)=\int_\mathbb R f(x)e^{ikx}dx\)。定义

\[
W_y(x)=\int_\mathbb R\Phi(x/2+v)\Phi(x/2-v)\cosh(2yv)dv,
\qquad G_y(x)=\partial_yW_y(x).
\tag{1.1}
\]

完整 theta 的正偶性、双指数尾与 Jacobian 为 1 的换元给

\[
\widehat W_y(k)=|\Xi(k+iy)|^2,\qquad
\widehat G_y(k)=\partial_y|\Xi(k+iy)|^2.
\tag{1.2}
\]

若能证明完整 G_y 对每个 0<y≤1/2 正定，便得到 RH：固定 k 后，模平方沿上半竖线非减；若在 y0>0 为零，就在整段 [0,y0] 为零，与解析唯一性冲突。下半平面由反射处理。这项充分条件在旧稿中已有，本稿不把它当作新的排零定理。

记

\[
K_y(a)=\int_0^\infty e^{-a\cosh v}\cosh(yv)dv,
\quad H_y(a)=(a^4+9a^2)K_y(a)+6a^3\partial_aK_y(a),
\]
\[
d_y(r)=\sum_{d\mid r}\cosh\!\left(y\log(d^2/r)\right)
=r^{-y}\sigma_{2y}(r),\quad a_r(x)=2\pi r e^x.
\]

这里 K 是修正 Bessel 函数；其积分为 DLMF 10.32.9。完整源的精确展开为

\[
W_y(x)=\sum_{r\ge1}e^{x/2}d_y(r)H_y(a_r(x)).
\tag{1.3}
\]

该身份继承自 `reports/20261011_bessel_divisor_growth/REPORT.md` §3，并可直接复核：对 theta 双和的有序对 (n,m) 作换元 t=2v+log(n/m)，乘积的多项式因子准确为
\(e^{x/2}[a^4+9a^2-6a^3\cosh t]\)，a=2πnm e^x。积分的偶部分给 H_y，nm=r 的和给 d_y。

在 x 的任意紧实集和 y 的任意紧复集，原绝对积分与任意固定阶导数由
\(C(nm)^M e^{-c nm}\) 控制。因此展开、重排、参数微分均合法；没有把非偶的单个 theta 模态当成偶函数。

对 x≥0 定义实际增长块

\[
g_{r,y}(x)=e^{x/2}\{d_y'(r)H_y(a_r(x))+d_y(r)\partial_yH_y(a_r(x))\}.
\tag{1.4}
\]

完整 G_y 偶，但各原始块未必偶。以下仅将 (1.4) 的正半轴限制作偶延拓。

## 2. 两个正积分的统一对数导数界

置 E_y(a)=∂_yK_y(a)。当 a>y²、y>0 时，

\[
\boxed{-\frac{K_y'(a)}{K_y(a)}\le1+\frac1{2(a-y^2)},\qquad
-\frac{E_y'(a)}{E_y(a)}\le1+\frac3{2(a-y^2)}.}
\tag{2.1}
\]

第一个式子在 y=0 同样成立。所有撇号在本节均指 a 微分。

### 证明

对非负权 w(v) 考察 e^{-a cosh v}w(v) 的积分。初等不等式为

\[
2(\cosh v-1)\le v\sinh v,\quad v^2\le2(\cosh v-1),\quad
z\tanh z\le z^2,\quad z\coth z\le1+z^2\quad(v,z\ge0).
\]

最后一式等价于 (1+z²)sinh z−z cosh z≥0；其导数为 z sinh z+z²cosh z≥0。第一式也可连续两次微分验证。

积分 \(\partial_v[vw(v)e^{-a\cosh v}]\)，两端边界项均为零，得到

\[
a\int_0^\infty v\sinh v\,w e^{-a\cosh v}dv
=\int_0^\infty(w+vw')e^{-a\cosh v}dv.
\tag{2.2}
\]

对于 w=cosh(yv)，有 vw'≤y²v²w；对于 w=v sinh(yv)，有
\(vw'/w=1+yv\coth(yv)\le2+y^2v^2\)。因此分别得到

\[
2(a-y^2)\int_0^\infty(\cosh v-1)w e^{-a\cosh v}dv
\le c\int_0^\infty w e^{-a\cosh v}dv,
\quad c=1\text{ 或 }3.
\]

除以正积分，加 1 即为 (2.1)。y=0 的第一个情形直接取 w=1。这里没有对趋零的 E_y 采用非一致数值除法。证毕。

## 3. Bessel 块的全参数二阶空间凸性

令 \(\mathscr D=1/2+a\partial_a\)、t=y²。由 Bessel 方程
\(K_y''=(1+t/a^2)K_y-K_y'/a\)，准确有

\[
\mathscr D^2H_y=A(a,t)K_y+B(a,t)K_y',
\tag{3.1}
\]
\[
A=a^6+(285/4+t)a^4+(225/4+39t)a^2,
\qquad B=15a^5+(165/2+6t)a^3.
\]

对全部 a≥12、0≤y≤1/2，定义

\[
P(a)=2(a-1/4)A(a,0)-[2(a-1/4)+3]B(a,1/4),
\]
\[
R(a)=2(a-1/4)\partial_tA-[2(a-1/4)+1]\partial_tB.
\tag{3.2}
\]

这两个多项式严格为正。准确因式为

\[
P(a)=\frac{a^2}{8}(16a^5-244a^4+840a^3-1629a^2-780a-225),
\]
\[
R(a)=\frac{a^2}{2}(4a^3-25a^2+150a-39).
\]

证明整个半轴上的符号，只需写 a=12+z。按最高次至常数的系数为

```
P(12+z): 2, 275/2, 3957, 489411/8, 1077537/2,
         20793231/8, 5703669, 2323566
R(12+z): 2, 215/2, 2355, 52881/2, 152892, 365256
```

每个系数都严格为正；这是全 a≥12 的有理证书，不是参数网格。

由于 A≥A(a,0)、0<B≤B(a,1/4)，用 (2.1) 中较大的比值上界得到

\[
\mathscr D^2H_y\ge\frac{P(a)}{2(a-1/4)}K_y>0.
\tag{3.3}
\]

对 (3.1) 作 y 微分，注意参数 t=y² 的导数项不能遗漏：

\[
\mathscr D^2\partial_yH_y=A E_y+B E_y'
+2y\{(\partial_tA)K_y+(\partial_tB)K_y'\}.
\]

因此 (2.1)、(3.2) 给对 0<y≤1/2 的准确下界

\[
\boxed{\mathscr D^2\partial_yH_y
\ge\frac{P(a)E_y+2yR(a)K_y}{2(a-1/4)}>0.}
\tag{3.4}
\]

这个正的额外项是本稿由 y=0 推到整个连续条带时保留的关键项。

## 4. 全部非首块的严格正定性

### 定理 A

对每个整数 r≥2 和每个 0<y≤1/2，g_{r,y} 在 [0,∞) 上严格凸、严格递减、严格正并趋于零。其偶延拓的 Fourier 变换在每个实频率 k 都严格为正。

### 证明

a_r(x)≥4π>12，并且 d_y(r)>0、d_y'(r)≥0。空间二次微分准确为

\[
g_{r,y}''(x)=e^{x/2}\{d_y'(r)\mathscr D^2H_y(a_r(x))
+d_y(r)\mathscr D^2\partial_yH_y(a_r(x))\}>0
\]

由 (3.3)–(3.4) 得到。Bessel 正积分及 Gaussian 包络给 g、g' 趋零，且各固定阶导数可积。于是 g' 从负侧严格递增至 0，g 从正侧严格递减至 0。

更具体地，令 c=g''>0，则

\[
g(x)=\int_x^\infty(s-x)c(s)ds\qquad(x\ge0).
\tag{4.1}
\]

每个三角核 (s−|x|)_+ 的 Fourier 变换是 2(1−cos ks)/k²。因此 k≠0 时

\[
\boxed{\widehat{g_{r,y}(|\cdot|)}(k)
=\frac2{k^2}\int_0^\infty[1-\cos(ks)]g_{r,y}''(s)ds>0.}
\tag{4.2}
\]

严格性来自 g'' 在整个正半轴严格为正。k=0 时为
\(2\int_0^\infty g_{r,y}>0\)。Gaussian 尾保证 s²g'' 可积，故 (4.1) 的 Fourier 交换合法。由显式非负谱密度即得正定性，不需要把点态正性误当成正定性。证毕。

### 定理 B：完整正尾与端点 y=0

定义

\[
\mathcal R_y(x)=\sum_{r\ge2}g_{r,y}(|x|).
\]

则 0<y≤1/2 时此和在 L¹ 与一致范数中收敛，为正定函数，且其 Fourier 变换处处严格为正。归一化族 \(\mathcal R_y/y\) 在 y=0 有 L¹ 连续延拓。

#### 无穷和的控制

由 cosh v≥1+v²/2、sinh(yv)≤yv cosh(yv)，对 a≥12、0≤y≤1/2 得到固定常数 C：

\[
K_y(a)\le Ce^{-a}a^{-1/2},\qquad E_y(a)\le Cy e^{-a}a^{-3/2}.
\]

例如将 e^{v/2} 通过 v/2≤av²/4+1/(4a) 吸收进 Gaussian 即可。结合 (2.1)，H_y、∂_yH_y 分别有界于
\(Ca^{7/2}e^{-a}\)、\(Cy a^{7/2}e^{-a}\)。

除数权满足

\[
d_y(r)\le d(r)r^{1/2},\qquad
0\le d_y'(r)\le y(\log r)^2d(r)r^{1/2}.
\]

利用 e^{x/2}=(a/(2πr))^{1/2} 与 dx=da/a，得到

\[
\frac{\|g_{r,y}(|\cdot|)\|_1}{y}
\le C d(r)(1+\log^2r)(1+r^3)e^{-2\pi r},
\tag{4.3}
\]

以及同类一致范数上界，右侧多一个固定 r 次幂。d(r)≤r 已足以求和。固定空间导数的包络同理。每项 g_{r,y}/y 在 y=0 有极限；(4.3) 给支配收敛。因此无穷和、Fourier 变换与 y↓0 极限都已控制。

由定义，\(G_y(x)/y\to4\mathcal K_1(x/2)\)。所以定理 B 的 y=0 极限与旧的一阶 Laguerre 正算术尾相容，而非改变尺度或归一化。

## 5. 正向结果之后继续检验首块补偿

完整身份现在成为

\[
\boxed{\partial_y|\Xi(k+iy)|^2
=\widehat{g_{1,y}(|\cdot|)}(k)+\widehat{\mathcal R_y}(k),
\qquad\widehat{\mathcal R_y}(k)>0.}
\tag{5.1}
\]

这使全 y 的非首算术部分有了真实正积分表示，但不能删除首块。

令 \(a_r(y)=-g_{r,y}'(0)>0\)（r≥2）。完整 theta 反射和可逐项求导给

\[
g_{1,y}'(0)=\sum_{r\ge2}a_r(y)>0.
\tag{5.2}
\]

首块的 Fourier 变换因而最终为负，精确主项是
\(-2g_{1,y}'(0)/k^2\)。正尾具有相反的同量主项。更高的代数项也由全部奇阶反射身份消去。此前“固定有限前缀最终为负”的结论原样保留。

所以本稿随后尝试的直接估计“只保留各正块的一条粗正下界”没有自动完成 (5.1) 的符号；必须证明误差在反射抵消之后仍是正确的一侧。正尾严格为正不等于它严格大于首块的负部。

当前未证明的具体剩余比较仍是

\[
\widehat{\mathcal R_y}(k)\ge-\widehat{g_{1,y}(|\cdot|)}(k)
\quad(k\in\mathbb R,\ 0<y\le1/2).
\tag{5.3}
\]

(5.3) 不是本稿结论，也没有被加入已证明清单。只有完成它或另一条全零点机制，才能完成 RH。

## 6. 实际复算、依赖与复核

`check_growth_tail.py` 已在 Python 3.13.5、SymPy 1.14.0 下执行，`exact_check.json` 保存真实输出。检查内容：Bessel 两次空间导数的全部多项式、两条移位多项式的全部正有理系数、双曲不等式的导数身份、三角核 Fourier 常数。它不代替积分换序或无穷量词的解析证明。

```sh
python check_growth_tail.py --output new_exact_check.json
```

输出排他创建，不覆盖已有文件。未作形式化内核验收；`AUDIT.md` 是同次自查，不冒称外部独立审稿。

来源：
- 当前仓库 `reports/20261011_bessel_divisor_growth/REPORT.md` §§1、3、6，固定提交 d74308ed：完整身份、正确增长目标和反射抵消。
- 当前仓库 `reports/20261011_laguerre_arithmetic_tail/REPORT.md` §6，同固定提交：仅 y=0 的旧正算术尾。
- NIST DLMF 10.32.9，Bessel 正积分：https://dlmf.nist.gov/10.32#E9 。
- NIST DLMF 10.25.1，Bessel 微分方程：https://dlmf.nist.gov/10.25#E1 。
- G. Gasper，arXiv:0801.2996，增长判据与 Bessel 平方积分背景：https://arxiv.org/html/0801.2996 。
