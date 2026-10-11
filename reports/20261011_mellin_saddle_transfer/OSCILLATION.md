# 正负部分的准确增长阶与实轴振荡

本附录在 [选择方程桥接](../20261011_qrh_selection_bridge/REPORT.md) 已声明的完整选择输入 S 与标准零点条带下，证明真实低态的正、负部分各自保留完整的右端指数增长阶，并将其传递为 Mellin 商实射线上正、负部分的准确幂次阶。鞍点估计采用 [本目录报告](REPORT.md)。外部 7/8 输入 Q 仅用于收紧最后的数值范围；本附录不重新证明 S，也不排除低态，因此不构成 RH 闭合。

沿用记号
\[
h(x)=\cosh(x/2),\qquad g(x)=2h(x)q(x),\qquad
g_+=\max(g,0),\quad g_-=\max(-g,0).
\]
对右半轴函数，令
\[
\tau(u)=\inf\{b\in\mathbb R:\ u(x)=O(e^{bx})\text{ as }x\to+\infty\}.
\]

S 与标准条带给出的输入包括：\(q,g\) 为实函数，\(0<\alpha\le1/2\)、\(c=1/2-\alpha\ge0\)，
\[
|g(x)|\le C e^{\alpha x},\qquad \tau(g)=\alpha,
\]
以及源变换的初始 Laplace 恒等式和全平面亚纯延拓
\[
F_g(s):=\int_0^\infty e^{-sx}g(x)\,dx
=C_g(s)=-\varepsilon^{-1}\sum_w\frac{n_wa_w}{s+iw}.
\tag{1}
\]
活动集合 \(\{w:a_w\ne0\}\) 的虚部上确界为 \(\alpha\)。每个活动点给出 \(C_g\) 的不可去极点 \(p_w=-iw\)，其实部为 \(\operatorname{Im}w\)，留数非零。这里不要求上确界被达到；它可以等于 \(1/2\)，尽管每个实际零点均严格在标准条带内。初始恒等式在 \(\operatorname{Re}s>1/2\) 成立；在 \(\operatorname{Re}s>\alpha\)，原积分和 \(C_g\) 均全纯，故恒等式由唯一性延拓到该半平面。

## 无实轴极点

若 \(p_w=-iw\) 为实数，则 \(w\) 纯虚。因此 \(\Xi(w)=\xi(1/2+iw)=0\) 会给出一个实零点 \(\beta=1/2+iw\in(0,1)\)（等价地，\(\beta=1/2-\operatorname{Im}w\)）。这不可能发生。对实数 \(0<\beta<1\)，交错级数
\[
\eta(\beta)=\sum_{n\ge1}(-1)^{n-1}n^{-\beta}>0,
\]
例如将其按相邻两项分组，每一组均为正；而解析延拓恒等式
\[
\eta(\beta)=(1-2^{1-\beta})\zeta(\beta)
\]
中的因子 \(1-2^{1-\beta}<0\)，故 \(\zeta(\beta)<0\)。完成因子的其他因子在 \(0<\beta<1\) 有限且非零，所以 \(\xi(\beta)\ne0\)。因此 \(C_g\) 没有实轴极点，尤其在实点 \(s=\alpha\) 全纯。

## Laplace–Landau 引理

**引理。** 设 \(u\ge0\) 局部可积，且
\[
F(s)=\int_0^\infty e^{-sx}u(x)\,dx
\]
有有限的收敛横坐标
\[
a=\inf\{\sigma\in\mathbb R:F(\sigma)<\infty\}\in\mathbb R.
\]
则 \(F\) 不可能解析延拓到包含实点 \(a\) 的圆盘。

**证明。** 反设 \(F\) 在 \(B(a,r)\) 有全纯延拓。它与原积分在 \(\operatorname{Re}s>a\) 相接，故定义于
\[
U=\{\operatorname{Re}s>a\}\cup B(a,r)
\]
上的同一个全纯函数。取 \(s_0=a+r/4\)。有
\[
B(s_0,r/2)\subset U:
\]
若其中一点实部大于 \(a\)，它在右半平面；若实部不大于 \(a\)，则它到 \(a\) 的距离小于 \(3r/4<r\)。所以以 \(s_0\) 为中心的 Taylor 级数半径至少为 \(R=r/2>s_0-a=r/4\)。因为 \(s_0>a\)，在原积分半平面内求导得到
\[
\frac{(-1)^nF^{(n)}(s_0)}{n!}
=\frac1{n!}\int_0^\infty x^n e^{-s_0x}u(x)\,dx\ge0.
\]
对任意实数 \(z\in(s_0-a,R)\)，Taylor 级数在 \(z\) 处收敛到有限值。系数非负，Tonelli 定理给出
\[
\int_0^\infty u(x)e^{-(s_0-z)x}\,dx
=\sum_{n\ge0}\frac{z^n}{n!}
  \int_0^\infty x^ne^{-s_0x}u(x)\,dx<\infty.
\]
但 \(s_0-z<a\)，这与 \(a\) 是收敛横坐标矛盾。证毕。

## 正、负部分各自有增长阶 \(\alpha\)

**命题。** 在上述输入下，
\[
\boxed{\tau(g_+)=\tau(g_-)=\alpha.}
\tag{2}
\]

**证明。** 先反设 \(\tau(g_-)<\alpha\)。按下确界定义，存在某个 \(b<\alpha\) 及常数 \(C_b\)，使 \(g_-(x)\le C_b e^{bx}\) 对所有充分大的 \(x\ge0\) 成立；增大常数即可覆盖整个半轴。于是
\[
F_-(s)=\int_0^\infty e^{-sx}g_-(x)\,dx
\]
在 \(\operatorname{Re}s>b\) 全纯。令 \(a_+\) 为 \(g_+\) 的 Laplace 收敛横坐标，允许 \(a_+=-\infty\)。由 \(g_+\le |g|\le Ce^{\alpha x}\)，有 \(a_+\le\alpha\)。在 \(\operatorname{Re}s>1/2\)，
\[
F_+(s)=C_g(s)+F_-(s),\qquad
F_+(s)=\int_0^\infty e^{-sx}g_+(x)\,dx.
\tag{3}
\]
因 \(\max(a_+,b)\le\alpha\le1/2\)，两侧在半平面
\(\operatorname{Re}s>\max(a_+,b)\) 都亚纯；由亚纯恒等定理，(3) 在整个该半平面成立。右侧把 \(F_+\) 亚纯延拓到 \(\operatorname{Re}s>b\)，且 \(C_g\) 的每个活动极点在该区域都保留非零留数，因为 \(F_-\) 在那里全纯。

若 \(a_+<\alpha\)，包括 \(a_+=-\infty\)，取实数
\(\delta\) 满足 \(\max(a_+,b)<\delta<\alpha\)。由活动虚部的上确界定义，存在活动 \(w\) 使 \(\operatorname{Im}w>\delta\)。于是 \(p_w=-iw\) 满足 \(\operatorname{Re}p_w>\delta\)。式 (3) 的右侧在 \(p_w\) 有不可去极点，而原积分 \(F_+\) 在 \(\operatorname{Re}s>a_+\) 全纯，矛盾。因此 \(a_+\ge\alpha\)，从而 \(a_+=\alpha\)。这一步只用任意接近 \(\alpha\) 的活动极点，不用最右极点存在。

另一方面，式 (3) 的右侧在实点 \(s=\alpha\) 的邻域全纯：\(F_-\) 在 \(\operatorname{Re}s>b\) 全纯，\(C_g\) 没有实轴极点。它给出 \(F_+\) 穿过其有限收敛横坐标 \(a_+=\alpha\) 的全纯延拓，与上面的 Laplace–Landau 引理矛盾。故不可能有 \(\tau(g_-)<\alpha\)。结合 \(g_-\le |g|\le Ce^{\alpha x}\)，得到 \(\tau(g_-)=\alpha\)。

交换 \(g_+\)、\(g_-\) 的角色，使用 \(F_-(s)=F_+(s)-C_g(s)\)，同一论证给出 \(\tau(g_+)=\alpha\)。证毕。

## 传递到 \(q\) 与 Mellin 商

定义 \(q_+=\max(q,0)\)、\(q_-=\max(-q,0)\)。因 \(h(x)>0\) 且
\[
\frac12e^{-x/2}\le \frac1{2h(x)}
=\frac{e^{-x/2}}{1+e^{-x}}\le e^{-x/2}\qquad(x\ge0),
\]
有 \(q_\pm=g_\pm/(2h)\)，从 (2) 得
\[
\boxed{\tau(q_+)=\tau(q_-) =\alpha-\tfrac12=-c.}
\tag{4}
\]

令 \(x_\sigma=\frac12\log(\sigma/(2\pi))\)。继承的带指数权鞍点估计给
\[
D_{\Phi q}(\sigma)=q(x_\sigma)+E(\sigma),\qquad
E(\sigma)=O(\sigma^{-c/2-1}).
\tag{5}
\]
对实 \(\sigma>1\)，\(D_{\Phi q}(\sigma)\) 为实连续函数。置
\[
D_\pm(\sigma)=\max(\pm D_{\Phi q}(\sigma),0),\qquad
Q_\pm(\sigma)=q_\pm(x_\sigma).
\]
正部映射是 1-Lipschitz，故
\[
|D_\pm(\sigma)-Q_\pm(\sigma)|\le |E(\sigma)|.
\tag{6}
\]

由于 \(\sigma=2\pi e^{2x_\sigma}\) 将充分大的实 \(x\) 双射到充分大的实 \(\sigma\)，(4) 等价于 \(Q_\pm\) 的实射线幂次下确界均为 \(-c/2\)。具体地，对每个 \(\eta>0\)，\(Q_\pm=O(\sigma^{-c/2+\eta})\)；再由 \(D_\pm\le Q_\pm+|E|\)，得到 \(\beta(D_\pm)\le-c/2\)。反过来，若某个 \(D_\pm=O(\sigma^{-c/2-\eta})\) 对某个 \(\eta>0\) 成立，则 (6) 给出相应 \(Q_\pm=O(\sigma^{-c/2-\min(\eta,1)})\)，与 (4) 矛盾。因此
\[
\boxed{\beta(D_+)=\beta(D_-)=-\frac c2,}
\qquad
\beta(u):=\inf\{b:\ u(\sigma)=O(\sigma^b)\text{ 对充分大实 }\sigma\}.
\tag{7}
\]
这表示准确的幂次下确界，不表示点态渐近式
\(D_\pm(\sigma)\sim C\sigma^{-c/2}\)。特别地，对每个 \(\eta>0\)，
\[
\limsup_{\sigma\to\infty}\sigma^{c/2+\eta}D_+(\sigma)
=\limsup_{\sigma\to\infty}\sigma^{c/2+\eta}D_-(\sigma)=+\infty.
\tag{8}
\]
所以 \(D_{\Phi q}\) 在任意远的实正射线上都取正值和负值。由其实连续性，交替选取两种符号点并应用介值定理可得实射线上无穷多个零点。

结论 (2)、(4)、(7) 及无穷实零点结论均以 S、标准条带和真实核的鞍点估计为前提。它们在 \(c=0\) 时也成立。若另外引用 Q，则 \(\alpha\le3/8\)、\(c\ge1/8\)，使 (7) 的共同幂次阶位于 \((-1/4,-1/16]\)；不用 Q 时范围为 \((-1/4,0]\)。这些结论刻画潜在低态的双侧增长和 Mellin 商振荡，并未排除这些低态，也没有推出 RH。

