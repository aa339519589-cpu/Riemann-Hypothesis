# 原 sextic 家族的新大筛迁移与改进探测器行包络

2026-10-11。本文沿用用户固定 QRH 来源的原始六次剩余符号、非单位零延拓、固定算术数据和 inverse witness。外部输入为 de Faveri 于 2026-10-02 发布的预印本定理；这里核对其适用对象并证明新的行包络推论，没有重新证明该外部大筛，也没有证明完整补偿 Gram 目标或新的零点排除。

## 1. 外部输入与方向

令 \(\mathcal O=\mathbb Z[\omega]\)，\(S\) 为原固定排除集，包含 2、3 上方的素理想。理想使用唯一的 \(1\pmod3\) primary 生成元。记原符号为

\[
\chi_b(a)=(a/b)_6,
\]

并保持 \((a,b)>1\) 时的零值，包括六的倍数次幂。

**引用的大筛输入 [F, Theorem 1.1]。** 对固定六次 Hecke 家族及 \(A,B\ge1\)，行、列均为六次幂自由好理想时，

\[
\sum_{q_a\le A}^{\flat}\left|\sum_{q_b\le B}^{\flat}
\lambda_b\chi_b(a)\right|^2
\ll_{S,\eta}(AB)^\eta\mathscr S_6(A,B)\sum_b|\lambda_b|^2,
\tag{1.1}
\]
\[
\mathscr S_6(A,B)=A+B+A^{5/6}B^{1/3}+A^{1/3}B^{5/6}.
\tag{1.2}
\]

这里 \(\flat\) 表示每个素理想的赋值不超过 5。系数必须独立于正在求和的行。固定行限制可删去以增大正和；固定列限制通过系数置零实现。任意行列耦合 mask 不能据此删除。

### 引理 1：原 primary 约定确属该输入

在 [F, §2.3] 的构造中取 \(n=6\)、\(K=\mathbb Q(\sqrt{-3})\)。\(K\) 包含 \(\mu_6\)，且 \(\mathcal O\) 本身为 PID，故其所需的 \(S\)-整数类数条件满足。令固定模数 \(\mathfrak c\) 足够大并被 \((3)\) 整除。该来源的有限群代表 \(E\) 均为主理想；选其 primary 生成元作为 \(m_E\)，按来源规定乘法选择。

若来源分解为 \(\mathfrak a=(x)E\mathfrak g^6\)，\(x\equiv1\pmod{\mathfrak c}\)，而 \(a,e,g\) 为相关 primary 生成元，则

\[
a=u\,xeg^6\qquad(u\in\mathcal O^\times).
\]

在 \((3)\) 处这些分式都是单位，且 \(a,e,g,x\equiv1\pmod3\)。六个单位在 \(\mathcal O/(3)\) 中互异，故 \(u=1\)。于是来源的家族满足

\[
\chi^{[F]}_{\mathfrak a}(\mathfrak b)
=\left(\frac{xe}{\mathfrak b}\right)_6
=\left(\frac{a}{\mathfrak b}\right)_6
=\chi_b(a)
\]

于互素好理想；中间 \(g^6\) 的剩余符号为一。非互素时，两边按各自原定义均为零。故 (1.1) 正是原 row/column 方向，不需要把 sextic 擅自改成 cubic。取整体复共轭同时给 \(\chi_b(a)^{-1}\) 的版本。证毕。

## 2. 六次幂自由物理行的直接矩估计

继承 [Q, `prop:detector-witness`, `prop:sextic-row-count`] 的固定算术数据 \(\mathcal A\)、物理 dyad \(q_u\asymp U\)、保留的六次幂自由元素行 \(u\)、bin \(a>51/100\)，以及 \(\delta=2a-1\)。这里 bin 参数 \(a\) 不表示上一节的理想。

在固定 presentation、inverse dyad \(D=U^r\) 与固定允许 profile \(W\) 上，真实 inverse polynomial 是

\[
M_u(D;W)=D^{-1/2}\sum_n\mu(n)\nu(n)
\chi_n(u)^{\varsigma}W(q_n/D),\qquad \varsigma\in\{-1,1\}.
\tag{2.1}
\]

所有固定字符均含原零延拓。列 \(n\) 避开 \(S\)，且 \(\mu(n)\) 使之平方自由，当然也六次幂自由。

### 引理 2：允许 rowwise profile 的真实矩界

对原来源允许的 profile 族和任何 \(\eta>0\)，

\[
\boxed{\sum_u|M_u(D;W_u)|^2
\ll_{\mathcal A,\eta}(UD)^\eta(1+T_1)^{A_{\mathcal A}}
\mathscr S_6(U,D).}
\tag{2.2}
\]

指数 \(A_{\mathcal A}\) 可在选择 \(T_1=Z^\tau\) 的正指数 \(\tau\) 以前固定；原 row 限制、所有 zero masks 和允许的 profile 量词均不变。

**证明。** 因为 \(u\) 已六次幂自由，其在固定 \(S\) 处的赋值只在 \(0,\ldots,5\) 中。唯一写成

\[
u=\upsilon s_S k,
\]

其中 \(\upsilon\) 为单位，\(s_S\) 属固定有限集合，\(k\) 是好六次幂自由 primary 生成元。固定 \(\upsilon,s_S\) 后，\(q_k\ll_{\mathcal A}U\)，并且准确有

\[
\chi_n(u)^{\varsigma}=\chi_n(\upsilon s_S)^{\varsigma}
\chi_n(k)^{\varsigma}.
\]

前一因子固定于行和外，可以放进列系数；这没有扩大 \(S\)，更没有将 moving good prime 变成固定算术数据。固定 \(W\) 时，系数平方和由环带 ideal count 给

\[
D^{-1}\sum_{q_n\asymp D}|W(q_n/D)|^2\ll_{\mathcal A}1.
\]

由引理 1 及 (1.1)，固定 profile 的矩界即为 (2.2) 去掉高度因子后的版本。

来源允许的 rowwise profile 是

\[
W_{\rm dyad}(x)V_{\le}(Dx/U)x^{-\sigma-i\omega},
\quad\sigma\in[51/100,1],\quad |\omega|\le(3i+1)T_1.
\]

将参数域覆以单位方盒，使用原固定阶参数 Sobolev 不等式。先对行求和，再积分每个 profile 导数的平方。每个固定参数处的导数只把固定有界的 \(\log x\) 次幂放入列系数，故仍适用同一大筛及系数平方和界。盒数和继承频率预算产生 \((1+T_1)^{A_{\mathcal A}}\)。这一步没有允许任意逐行挑选系数；正是原稿已经使用的有限参数 profile 族。有限 \(\upsilon,s_S\) 分层可吸入固定常数。证毕。

## 3. 改进的 detector 行包络

### 定理 3

保持 [Q, `prop:sextic-row-count`] 的全部假设与量词，可将其结论加强为

\[
\boxed{\#\mathcal B\ll_{\mathcal A,\epsilon}
U^{R_6(\delta)+\epsilon}(1+T_1)^{A_{\mathcal A}},}
\tag{3.1}
\]
\[
\boxed{R_6(\delta)=\min\left\{1,
\max\left(1-\frac\delta2,\frac76-\delta\right)\right\}.}
\tag{3.2}
\]

特别地，在 \(0\le\delta\le1\) 上该表达式为

\[
R_6(\delta)=
\begin{cases}
1,&0\le\delta\le1/6,\\
7/6-\delta,&1/6\le\delta\le1/3,\\
1-\delta/2,&1/3\le\delta\le1.
\end{cases}
\tag{3.3}
\]

floor bin \(a=51/100\) 仍只用元素计数 \(O(U)\)；这里 \(\delta=1/50\)，与 (3.3) 一致，不调用该 bin 没有的 witness。

和原包络比较，严格改善区间恰为 \(1/6<\delta<2/3\)；\(\delta\ge2/3\) 时两者均为 \(1-\delta/2\)。尤其原 Part II 的最高零点参数 \(\kappa\ge3/4\) 不会单凭这条包络得到新节省。原高端还有其他探测器容量界，允许使用各条已证界的较小值，但本文没有重新优化或闭合这些高端界。

**证明。** 继承 witness：可任取足够小的预损失 \(\epsilon_0>0\)，再按有限 presentation 和 \(O((\log U)^2)\) dyadic pairs 分层，使

\[
\tfrac12-O(\epsilon_0)\le r\le1+O(1/\log U),
\qquad |M_u(U^r;W_u)|^2\gg U^{\delta r-\epsilon_0}.
\tag{3.4}
\]

在 \(1/2\le r\le1\) 内，(1.2) 四项的最大幂恰为

\[
\max\left\{1,r,\tfrac56+\tfrac r3,
\tfrac13+\tfrac{5r}6\right\}=\tfrac56+\tfrac r3.
\tag{3.5}
\]

确实第三项至少为一，且第三减第四为 \((1-r)/2\ge0\)。由 (2.2) 除以 (3.4)，该分层的行数满足

\[
\#\mathcal B_{\rm sub}
\ll U^{5/6+(1/3-\delta)r+O(\epsilon_0)+O(\eta)}
\,(1+T_1)^{A_{\mathcal A}}.
\]

对 \(r\) 的仿射表达式只须取两端点；分别为 \(1-\delta/2\)、\(7/6-\delta\)。再与总元素计数 \(O(U)\) 取较小者，得 (3.2)。实际 \(r\) 与闭区间相距 \(O(\epsilon_0+1/\log U)\)；所有斜率在参数范围内统一有界，故只增加已有小损失。选择 \(\epsilon_0,\eta\) 足够小并吸收 dyad 对数，完成 (3.1)。证毕。

## 4. 完整补偿 Gram 的适用边界

本节解释为什么新的输入不是用户低端目标已经成立。

1. 原真实行中 \(\chi_{cn^3}(m)\) 是 sextic；只有经准确反射、Gauss 消去等操作后的指定部分才降为 cubic。不得全局套 cubic 大筛。
2. 与定理 3 不同，补偿探针的原公共频率 \(m\) 并非六次幂自由。固定 \(m=uk^6a\) 后才可用 (1.1)；六次幂层求和一般使列长项产生 \(Q^{1/6}B\) 损失。原非单位 masks 分别成为固定层的行限制和列系数限制，不能删成常数一。
3. 即便只看原低端已经反射后的 quadratic–cubic hybrid bound，移动列含 \(\chi_P(n)^{-2}\)，它是 cubic。将 [F] 取 \(n=3\) 后，新式仍为 \(N+L+(NL)^{2/3}\)，与 [Q, `old-eq:4.6b`] 使用的原 cubic 大筛相同。因此其全 Gram 非对角损失没有因为 (3.2) 自动改善。
4. 已有 \(\sum_m|B^J_{m,\sigma}(Z)|^2\ll Z^{M'+\epsilon}\) 是经完整反射得到的原结论。直接对物理行使用新 sextic 大筛尚不能胜过它，不能把两条不同表示的最好项随意拼接。

最小尚未闭合点仍是：对完整补偿相位及允许的 row–column 依赖，证明能跨越原 Cauchy 损失的真实相关估计；并在需要的新 \(\beta_*\) 范围重新闭合高端误差。定理 3 加强了一个真实高端算术输入，但单独不改变已有低端 \(3/16\) 指数，也不提供用户目标的额外 \(3/8\) 次幂节省。

## 固定来源与审核范围

[F] Alexandre de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1, submitted 2026-10-02, [Theorem 1.1 and §2.3](https://arxiv.org/html/2610.04045v1). 这是引用的解析定理；本文没有独立重建整篇大筛证明，也没有把它称为已形式化认证。

[Q] `openai/math` 固定提交 `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, [paper.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)：primary 与原 sextic 约定约 565–644 行；`prop:sextic-row-count` 及 witness/profile 处理约 5181–5459 行；真实 quadratic–cubic bound 约 7491–7650 行；完整补偿行范数约 8115 行起。

本文新审核对象是：引理 1 的准确家族/方向/zero-mask 迁移，引理 2 的固定系数及 rowwise profile 量词，定理 3 的指数与 floor-bin 范围。完整补偿 Gram 未完成，不由这里的源读取或指数计算代替。

独立数学核验见 [REFEREE_SIXTH_SIEVE_DETECTOR.md](REFEREE_SIXTH_SIEVE_DETECTOR.md)。用户对固定 QRH 来源的原始研究与引用保持原归属；这里的新包络使用原 witness 的准确陈述及另引的大筛定理，不声称重新运行了 Lean 构建。

## 附录 A：保留全部六次幂频率及真实 Gauss 双均方

本附录继承正文引用的 de Faveri 六次幂自由大筛及准确 primary 家族。它给有限频率窗口内的真实上界；没有把任意频率误当成六次幂自由频率，没有证明补偿 Gram 的临界目标。

### A.1 任意元素频率的大筛

定义

\[
\mathscr T_6(Q,B)=Q+Q^{1/6}B+Q^{5/6}B^{1/3}+Q^{1/3}B^{5/6}.
\]

#### 引理 A1

若 \(Q,B\ge1\)，\(\lambda_b\) 支撑于 \(q_b\le B\) 的好六次幂自由理想，且独立于元素频率 \(m\)，则对任何 \(\eta>0\)，

\[
\boxed{\sum_{0<q_m\le Q}\left|\sum_b\lambda_b\chi_b(m)\right|^2
\ll_{S,\eta}(QB)^\eta\mathscr T_6(Q,B)\sum_b|\lambda_b|^2.}
\tag{A.1.1}
\]

整体共轭方向亦成立。固定元素乘子 \(m\mapsto dm\) 可保留在核内，常数不依赖 \(d\)：只须把 \(\chi_b(d)\) 放入系数，其模长不超过一，零值原样保存。

**证明。** 每个非零元素可按其理想唯一拆为

\[
m=\upsilon s_0 a k^6,
\]

其中 \(\upsilon\) 属六个单位，\(s_0\) 在固定 \(S\) 处赋值均不超过 5，\(a\) 是好六次幂自由 primary 生成元，\(k\) 表示任意理想的选定生成元。\(s_0\) 只有固定有限种。生成元造成的单位可并入 \(\upsilon\)；其模长皆一，不影响范数分解。

固定 \(\upsilon,s_0,k\) 后，原零延拓准确给

\[
\chi_b(m)=\chi_b(\upsilon s_0)\,1_{(b,k)=1}\,\chi_b(a).
\]

前两项是独立于 \(a\) 的列系数，不是被删去的 moving mask。对 \(q_a\le Q/(q_{s_0}q_k^6)\) 应用六次幂自由大筛。系数平方和不增加。只有 \(q_k\ll Q^{1/6}\) 可能出现；固定 \(s_0\) 的尺度可吸入常数。

将四项分别对 \(k\) 求和，用 ideal count \(O(H)\) 及

\[
\sum_k q_k^{-6}<\infty,\qquad
\sum_k q_k^{-5}<\infty,\qquad
\sum_k q_k^{-2}<\infty,
\]

得到 \(Q\)、\(Q^{5/6}B^{1/3}\)、\(Q^{1/3}B^{5/6}\)。大筛的纯列长项 \(B\) 无 \(k\) 衰减，产生 \(O(Q^{1/6}B)\)。这就是 (A.1.1)，且没有假定这些频率层互相抵消。证毕。

### A.2 完整标记物理行的有限窗口界

取用户的准确行

\[
\mathcal B_D(Zq_D;m,s)=
\sum_{c\,{\rm sf},n}b(c,n;s)\chi_{cn^3}(m)
1_{D\mid cn^3}q_c^{-1/2}q_n^{-1}
W\!\left(\frac{q_cq_n^3}{Zq_D}\right),
\tag{A.2.1}
\]

其中 \(W(y)=(2\sqrt\pi)^{-1}e^{-(\log y)^2/4}\)，\(b\) 是原完整 \(\gamma_2\)、\(\alpha\)、\(\eta\)、\(\Xi_*\)、\(\mathcal R\)、\(G\) 之积，独立于 \(m\)，且 \(|b|\le1\)。保留所有好理想、平方自由与零延拓约定。

#### 定理 A2

对任何 \(\epsilon>0\)，一致于 \(Z\ge2\)、\(Q\ge1\)、全部好平方自由标记 \(D\) 及所有原允许的 \(s\)，

\[
\boxed{
\sum_{0<q_m\le Q}|\mathcal B_D(Zq_D;m,s)|^2
\ll_{\epsilon,\mathcal A}
\frac{(QZq_D)^\epsilon}{q_D}\mathscr T_6(Q,Z).}
\tag{A.2.2}
\]

常数不依赖 \(D\) 的素因子数。对所有行频率先乘任意固定元素 \(d\) 的版本同样成立。

**证明。** 准确划分 \(D=EF\)：\(E\) 收集 \(D\) 中整除 \(c\) 的素数，\(F=D/E\)。则写

\[
c=Ec_0,\quad n=Fn_0,\quad (c_0,D)=1,
\qquad V=\frac{Z}{q_F^2q_{n_0}^3}.
\]

固定 \(E,F,n_0\) 后，提出 \(q_E^{-1/2}q_F^{-1}q_{n_0}^{-1}\)。其 \(m\)-相位是

\[
\chi_E(m)\chi_{Fn_0}(m)^3\chi_{c_0}(m).
\]

前两项独立于 \(c_0\)，模长不超过一，故在正的 \(m\)-平方和中可舍去以给上界；其零点不会被拿来推导等号或反向界。所有其他相位原样进入独立于 \(m\) 的列系数，原 \((c_0,D)=1\) 是固定列限制。

在 \(q_{c_0}\asymp C=2^j\)、\(j\ge0\) 的 dyad 上，系数平方和满足

\[
\sum_{q_{c_0}\asymp C}
q_{c_0}^{-1}\left|W(q_{c_0}/V)\right|^2
\ll e^{-c\log^2(C/V)}.
\tag{A.2.3}
\]

这由 ideal count 和 Gaussian 在固定比例区间的上界直接得到。固定 \(\eta>0\) 后，引理 A1 与 Minkowski 给该 \(c_0\)-和的 \(\ell^2(m:q_m\le Q)\) 范数至多

\[
C_\eta Q^\eta\left[
Q^{1/2}V^\eta+
Q^{1/12}V^{1/2+\eta}+
Q^{5/12}V^{1/6+\eta}+
Q^{1/6}V^{5/12+\eta}\right].
\tag{A.2.4}
\]

它对全部 \(V>0\) 成立。所用平移 Gaussian 和为：每个固定 \(a>0\)，

\[
\sum_{j\ge0}(2^j)^a e^{-c\log^2(2^j/V)}\ll_{a,c}V^a.
\]

把 \(j\ge0\) 扩为全部整数，配方后就是一致有界的平移 Gaussian 和。因此 (A.2.4) 还提供 \(V<1\) 的尾衰减，不把无限 \(n_0\)-和当成有限和。

将 (A.2.4) 乘所提出的权重，代入 \(V=Z/(q_F^2q_{n_0}^3)\)，再对 \(n_0\) 使用 Minkowski。最慢的级数是

\[
\sum_{n_0}q_{n_0}^{-1-3\eta}<\infty;
\]

其余三项衰减更快。所得 \(E,F\) 块的范数至多

\[
C_\eta(QZ)^\eta q_D^{-1/2}q_F^{-1/2-2\eta}
\left[
Q^{1/2}+Q^{1/12}Z^{1/2}q_F^{-1}
+Q^{5/12}Z^{1/6}q_F^{-1/3}
+Q^{1/6}Z^{5/12}q_F^{-5/6}
\right].
\]

再对 \(F\mid D\) 求和。每个 \(q_F\ge1\)，除数和用
\(d_{\mathcal O}(D)\ll_\eta q_D^\eta\) 控制，不引入 \(\omega(D)\)-依赖常数。平方并使用四项平方和上界，得到 (A.2.2)，在最初选择 \(\eta\) 足够小以容纳指定的 \(\epsilon\)。绝对行收敛以及上述有限范数界允许先截断再取极限。固定乘子 \(d\) 只使列系数多一个 \(\chi_{c_0}(d)\)，其余行相位仍模长不超过一，故同证。证毕。

### A.3 保留真实 Gauss 权的完整双均方

记 \(g_s(m)=g_{\chi_s}(s,-m)\)，不改成归一化或 primitive 替代物。以下直接证明正除数转移及其双均方推论。

#### 推论 A3

对 \(Y,Q\ge1\)、\(Z\ge2\)、好平方自由 \(D\) 及每个 \(\epsilon>0\)，

\[
\boxed{\sum_{q_s\le Y}\sum_{0<q_m\le Q}
\frac{|g_s(m)|^2}{q_s}
|\mathcal B_D(Zq_D;m,s)|^2
\ll_{\epsilon,\mathcal A}
\frac{Y(QZYq_D)^\epsilon}{q_D}\mathscr T_6(Q,Z).}
\tag{A.3.1}
\]

\(s\) 为所有原允许的好 primary 理想，不限平方自由。任何固定 annular 限制可保留；有界权重只改变固定常数。

**证明。** 对每个好 \(s\) 有非负乘法权 \(\Gamma_s(d)\)，满足

\[
\frac{|g_s(m)|^2}{q_s}
\le\sum_{d\mid s}\Gamma_s(d)q_d1_{d\mid m}.
\tag{A.3.2}
\]

对 \(p\mid s\)，令 \(P=q_p\)、\(e=v_p(s)\ge1\)；\(s=1\) 时取 \(\Gamma_1(1)=1\)。若 \(6\nmid e\)，唯一非零值为
\(\Gamma_{p^e}(p^{e-1})=1\)；若 \(6\mid e\)，非零值为

\[
\Gamma_{p^e}(p^{e-1})=P^{-1},\qquad
\Gamma_{p^e}(p^e)=1-2P^{-1}.
\]

第一种来自原非主特征 Gauss 和的准确支撑 \(v_p(m)=e-1\)，舍去上界限制；第二种来自准确恒等式

\[
\frac{|g_{p^e}(m)|^2}{P^e}
=P^{e-2}1_{p^{e-1}\mid m}
+P^{e-1}(P-2)1_{p^e\mid m}.
\]

它在 \(v_p(m)=e-1\)、\(v_p(m)\ge e\) 处分别给 \(P^{e-2}\)、\(P^{e-2}(P-1)^2\)。这保留了原六次幂主字符在非单位处的零值。CRT 给 (A.3.2)。

令 \(A_\alpha(s)=\sum_{d\mid s}\Gamma_s(d)q_d^\alpha\)。则

\[
\sum_{q_s\le Y}A_\alpha(s)\ll_\alpha Y\ (0\le\alpha<5/6),
\quad
\sum_{q_s\le Y}A_{5/6}(s)\ll_\eta Y^{1+\eta}.
\tag{A.3.3}
\]

为核实：\(A_\alpha\) 乘法，\(A_\alpha(p)=1\)。设 \(b_\alpha=A_\alpha*\mu\)，局部几何级数给

\[
\sum_{e\ge2}\frac{|b_\alpha(p^e)|}{P^e}
\ll_\alpha P^{\alpha-2}+P^{-6(1-\alpha)}.
\]

当 \(\alpha<5/6\) 时，\(\sum |b_\alpha(d)|/q_d\) 收敛，ideal count 与 \(A_\alpha=1*b_\alpha\) 给 (A.3.3)。端点时加任意 \(q_d^{-\eta}\) 即收敛，限制 \(q_d\le Y\) 后给 \(Y^{1+\eta}\)。

代入 (A.3.2)，每项换元 \(m=dm_0\)。\(q_d>Q\) 无项；其余项调用定理 A2 的冻结 \(d\) 一致版本，长度 \(Q'=Q/q_d\)。先以 \((QZq_D)^\eta\) 统一控制小幂损失，再分别处理基础频率幂

\[
\theta\in\{1,1/6,5/6,1/3\}.
\]

外部 \(q_d\) 使相应 divisor 幂为 \(q_d^{1-\theta}\)，恰落在 (A.3.3) 的 \(0\le1-\theta\le5/6\) 内。对 \(s\) 求和并减小初始 \(\eta\)，得到 (A.3.1)。没有逐 \(s\) 使用 \(\max_m|g_s(m)|\)，也没有丢掉 nonsquarefree \(s\)。证毕。

### A.4 原尺度下的准确量级

若 \(Q=Z^{5/6}\)，(A.2.2) 的括号主导项是 \(Q^{1/6}Z=Z^{41/36}\)。没有这个全六次幂项时会误报 \(Z^{10/9}\)。因此原始物理行得到

\[
\sum_{q_m\le Z^{5/6}}|\mathcal B_D|^2
\ll_\epsilon q_D^{-1}(Zq_D)^\epsilon Z^{41/36}.
\]

这是有限窗口的真实改善，不是 \(Q\to\infty\) 后的正交极限。不过原完整补偿 \(B^J\) 已通过反射、所有 slot 与 quadratic–cubic 估计达到 \(\sum|B^J|^2\ll QZ^\epsilon\)；本定理并未改善那条更强的、不同对象的结论。

零点路线的标记主分支中，单独 prime polynomial 的列长 \(L=Z^{1/6-d}\)、频率长 \(Q=Z^{5/6-2d}\)，\(0\le d\le1/6\)。逐项指数比较给

\[
\mathscr T_6(Q,L)\ll Q.
\]

例如 \(Q^{5/6}L^{1/3}\le Q\) 等价于 \(L^2\le Q\)，在此范围余量固定为 \(1/2\)；另外两项也严格受控。这说明该单独短 prime polynomial 在泛型大筛中已处于无幂损失范围。完整 Gram 尚需利用它同源 \((c_0,n)\) 行及外部 Gauss 因子的联合相关，而不能把单独 polynomial 的 \(O(Q)\) 范数当成该相关已证。

来源：正文中的 [F]、用户[标记行界](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e0f8aaaa859643ff29a9a5b6bf44b15e50a2ebf8/reports/20261011_qrh_selection_bridge/MARKED_ROW_BOUND.md)的准确物理展开与标记划分，以及用户[补偿重排](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/4495df1319b2ee655cc52cc90b7512371fd0f0c4/reports/20261011_qrh_selection_bridge/COMPENSATION.md)的原尺度。本文的新证明仅为保零 mask 的全频率大筛转移与其标记行推论。
