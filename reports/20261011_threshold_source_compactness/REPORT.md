# 阈值附近的真实源紧性、空间逃逸与有限零点块的非浅谱捕获

2026-10-11。保持完整 theta、全部素数幂、Γ 对数乘子与原谱问题。本稿给出不依赖近指数权常数的阈值紧性，并把已有真实逆采样恒等式写成有限谱窗下界。**这些是阈值诊断及可承重接口，不排除真实低态，不证明 RH；不主张一般紧性或谱论思想的文献优先权。**

## 1. 准确空间与继承输入

令 \(h=\cosh(x/2)\)、\(d\nu=2\Phi h\,dx\)，并取实偶零均值空间

\[
\mathcal H=\{q\in L^2(\nu):q(-x)=q(x),\ \nu(q)=0\}.
\]

真实自伴算子为 \(H=L|_{\mathcal H}-1/2\)。其负谱位于 \((-1/2,0)\)，为有限重离散本征值，唯一可能的负谱积聚点是 0。置

\[
\mathcal Uq=\sqrt{2\Phi h}\,q=v,\qquad m=\sqrt{\Phi/(2h)},\qquad f=mv=\Phi q.
\]

在酉像空间 \(\mathcal K=\mathcal U\mathcal H\subset L^2(dx)\) 上，继承准确实现

\[
\widetilde H=\mathcal U H\mathcal U^{-1}=B-\mathcal V,
\qquad B=M_m b(D)M_m\ge0,
\tag{1.1}
\]

\[
\mathcal V=C_0M_{m^2}+
\sum_{n\ge2}\alpha_nM_m(\tau_{\log n}+\tau_{-\log n})M_m,
\qquad \alpha_n=\Lambda(n)/\sqrt n.
\tag{1.2}
\]

这里 \(b\ge0\)、\(b(t)=\log(1+|t|)+O(1)\)，且 \(m>0\) 处处、\(m\) 双指数趋零。完整 theta 包络已经给

\[
\sum_{n\ge2,\pm}\alpha_n
\|m(x)m(x\pm\log n)\|_\infty<\infty.
\tag{1.3}
\]

因此 \(\mathcal V\) 有界，且 (1.2) 在全 \(L^2\) 算子范数绝对收敛。\(B\)、\(\mathcal V\) 单独不必保存 \(\mathcal K\)；以下身份先在原全空间实现中解释，谱投影则只取 \(\widetilde H|_{\mathcal K}\)，没有暗中要求各项都约化该子空间。

记 \(E_-=\mathbf1_{(-1/2,0)}(\widetilde H)\)，以及 \(E_\eta=\mathbf1_{(-\eta,0)}(\widetilde H)\)，在 \(\mathcal K^\perp\) 上延拓为零。

这些输入来自公开 [《RH 研究续篇》附录 5、6](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/cbe98c3b3d4d2e64bafa79bf155db55af21bc8af/history/source-materials/RH_%E7%A0%94%E7%A9%B6%E7%BB%AD%E7%AF%87_20261011.md#L1408-L2224) 及 [原闭谱实现](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/cbe98c3b3d4d2e64bafa79bf155db55af21bc8af/rounds/05/REPORT-pages-01-05.txt)；本稿不把它们重新登记为新结果。

## 2. 不依赖 ε 的源族紧性

### 定理 1

\[
\boxed{M_mE_-:L^2(dx)\longrightarrow L^2(dx)\text{ 是紧算子。}}
\tag{2.1}
\]

其证明给出对负谱单位球的两个统一尾：若 \(u=E_-u\)、\(\|u\|_2\le1\)，令 \(f=mu\)、\(\widehat f=F\)，则

\[
\int_{|x|>R}|f(x)|^2dx\le\sup_{|x|>R}m(x)^2\longrightarrow0,
\tag{2.2}
\]

\[
\int_{|t|>T}|F(t)|^2\frac{dt}{2\pi}
\le\frac{\|\mathcal V\|}{\beta(T)}\longrightarrow0,
\quad\beta(T)=\inf_{|t|>T}b(t)\sim\log T.
\tag{2.3}
\]

公式 (2.3) 只对足够大、\(\beta(T)>0\) 的 \(T\) 使用。

### 证明

负谱全部位于有界区间，故 \(E_-\) 的像落在 \(\operatorname{Dom}(\widetilde H)\) 中；有界扰动 (1.1) 进而保证落在 \(\operatorname{Dom}(B)\) 中。因 \(\langle u,\widetilde H u\rangle\le0\)，

\[
\|b(D)^{1/2}(mu)\|_2^2
=\langle u,Bu\rangle
=\langle u,\widetilde H u\rangle+\langle u,\mathcal V u\rangle
\le\|\mathcal V\|.
\tag{2.4}
\]

这给 (2.3)；(2.2) 直接来自 \(\|u\|_2\le1\)。源的 \(L^2\) 范数统一有界于 \(\|m\|_\infty\)。

为逐项核实紧性，对实平移 \(s\)，Plancherel 与频率拆分给

\[
\|f(\cdot+s)-f\|_2^2
\le s^2T^2\|m\|_\infty^2
+4\|\mathcal V\|/\beta(T).
\]

先选大 \(T\)，再选小 \(s\)，得到统一平移连续性。结合 (2.2)，Riesz–Fréchet–Kolmogorov 紧性判据得到负谱单位球的源像相对紧，即 (2.1)。证毕。

这里确实使用 Γ 对数符号趋于无穷，不能仅由 \(m\to0\) 就宣布乘法算子紧。

## 3. 阈值源统一塌缩，并强迫 Hilbert 质量逃向空间无穷

### 推论 2

当 \(\eta\downarrow0\) 时，

\[
\boxed{\|M_mE_\eta\|_{2\to2}\longrightarrow0.}
\tag{3.1}
\]

对每个固定 \(R<\infty\)，

\[
\boxed{\|\mathbf1_{[-R,R]}E_\eta\|_{2\to2}\longrightarrow0.}
\tag{3.2}
\]

此外

\[
\|\mathcal V E_\eta\|_{2\to2}\to0,\qquad
\|B E_\eta\|_{2\to2}\to0,
\qquad
\|b(D)^{1/2}M_mE_\eta\|_{2\to2}\to0.
\tag{3.3}
\]

### 证明

谱定理给 \(E_\eta\to0\) 强收敛，因为交集谱集为空，0 被排除。紧算子 \(K=M_mE_-\) 与自伴强趋零投影满足 \(\|KE_\eta\|\to0\)：先以有限秩逼近 \(K\)，再在有限维空间使用强收敛即可。因此 (3.1) 成立。

\(m\) 在 \([-R,R]\) 上的最小值为正，故

\[
\|\mathbf1_{[-R,R]}E_\eta\|
\le(\min_{[-R,R]}m)^{-1}\|M_mE_\eta\|,
\]

证明 (3.2)。

式 (1.2) 的每个固定移位项右乘 \(E_-\) 后都是紧算子，例如

\[
M_m\tau_dM_mE_-=M_m\tau_dK.
\]

由 (1.3) 的算子范数可和性，\(\mathcal VE_-\) 也是紧算子，所以第一项 (3.3) 成立。再用

\[
B E_\eta=\widetilde H E_\eta+\mathcal V E_\eta,
\qquad \|\widetilde H E_\eta\|\le\eta,
\]

得第二项。最后正闭形式给

\[
\|b(D)^{1/2}M_mE_\eta\|^2
=\|E_\eta B E_\eta\|\le\|BE_\eta\|\to0.
\]

所有右侧都是已证有界算子，不涉及对无界 \(B\) 的未经证明范数操作。证毕。

### 准确解释

若归一真实本征态 \(v_j\) 满足 \(\widetilde Hv_j=-\varepsilon_jv_j\)、\(\varepsilon_j\downarrow0\)，则其源 \(f_j=mv_j\) 强趋零，而且 \(v_j\) 在每个固定空间紧集的 \(L^2\) 质量趋零。结论不要求不同态预先选成正交序列。

这说明已有近指数权常数退化不是唯一问题：自然归一化下源本身必塌缩为零。不能假定 \(\|f_j\|_2\) 有统一正下界，也不能从源族相对紧性提取非零源极限。但 (3.2) 并未证明空间逃逸不可能。

对任意固定复紧集 \(K\) 及固定阶 \(j\)，还有

\[
\sup_{z\in K}|F_{v_n}^{(j)}(z)|\longrightarrow0.
\tag{3.4}
\]

可用 \(F_v^{(j)}(z)=\int(ix)^jm(x)v(x)e^{izx}dx\) 的 \(L^2\) 评价核证明：这些核在 \(z\in K\) 上构成紧集，\(v_n\rightharpoonup0\)，因此配对统一趋零。相同论证给所有 \(E_\eta\) 单位向量上的统一版本。

## 4. 固定真实离轴标签的激活不能全部逃入浅谱

本节改回 \(\mathcal H\) 中的 \(q\) 表示。条件地选定实际存在的 \(k\ge1\) 个不同离轴四元组代表

\[
w_i=\gamma_i+i\delta_i,\quad\gamma_i>0,\quad0<\delta_i<1/2,
\]

重数为 \(m_i\)。其余离轴零点可无限，不假设简单零点。定义

\[
b_i(x)=-\frac{\sin(\gamma_i x)\sinh(\delta_i x)}{2h(x)},
\quad v_i=2\sqrt{m_i}\,b_i,
\quad \mathsf Vc=\sum_i c_iv_i.
\]

继承 [真实 theta 除法与 Weil 极化的准确逆采样](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/cbe98c3b3d4d2e64bafa79bf155db55af21bc8af/reports/20261011_zero_selection/REPORT.md)（§§1–3；完整核投影与显式插值源见其§2）：

\[
v_i\in\operatorname{Ran}(H)\cap\operatorname{Dom}(H^\dagger),\quad
\mathsf U=H^\dagger\mathsf V,
\quad \mathsf U^*\mathsf V=-I_k.
\tag{4.1}
\]

若 \(Hq_n=-\varepsilon_nq_n\) 是全部负谱的实标准正交本征基，令 \(c_n=\mathsf V^*q_n\)，则已有

\[
\mathsf A:=\sum_n\frac{c_nc_n^*}{\varepsilon_n}=I_k+\mathsf C_+\succeq I_k,
\tag{4.2}
\]

其中 \(\mathsf C_+\succeq0\)，全矩阵绝对收敛。这里 \(\mathsf V\) 是有限标签列算子，与 §§1–3 的真实势算子 \(\mathcal V\) 不同。

### 定理 3：有限标签的非浅谱捕获

对每个 \(\eta>0\)，

\[
\boxed{\sum_{\varepsilon_n<\eta}\frac{c_nc_n^*}{\varepsilon_n}
\preceq\eta\mathsf U^*\mathsf U,\qquad
\sum_{\varepsilon_n\ge\eta}\frac{c_nc_n^*}{\varepsilon_n}
\succeq I_k-\eta\mathsf U^*\mathsf U.}
\tag{4.3}
\]

若 \(\mathsf P\) 的列是已知真实插值向量 \(p_i\in\operatorname{Dom}(H)\)，满足 \(Hp_i=-v_i\)，则

\[
\mathsf U=-(I-\Pi_0)\mathsf P,\qquad
\mathsf U^*\mathsf U\preceq\mathsf P^*\mathsf P.
\tag{4.4}
\]

因而可以取完全由这些实际插值源范数给出的

\[
\eta_I=\frac1{2\|\mathsf P\|^2}>0,
\]

并得到

\[
\boxed{\sum_{\varepsilon_n\ge\eta_I}\frac{c_nc_n^*}{\varepsilon_n}
\succeq\tfrac12 I_k.}
\tag{4.5}
\]

该谱带远离阈值，只有有限个本征值，故必须包含至少 \(k\) 个按重数计的真实低态。

### 证明

自伴性与 \(H\mathsf U=\mathsf V\) 给

\[
c_n=\mathsf V^*q_n=\mathsf U^*Hq_n=-\varepsilon_n\mathsf U^*q_n.
\]

因此

\[
\sum_{\varepsilon_n<\eta}\frac{c_nc_n^*}{\varepsilon_n}
=\sum_{\varepsilon_n<\eta}\varepsilon_n
(\mathsf U^*q_n)(\mathsf U^*q_n)^*
\preceq\eta\mathsf U^*\mathsf U,
\]

其中最后一步是 Bessel 不等式。与 (4.2) 相减得到 (4.3)。\(Hp_i=-v_i\) 给 (4.4)，保留完整核投影 \(\Pi_0\)，没有把导数阈值族当成完整核。代入即可得 (4.5)。

负谱只可能在 0 积聚，因此 \(\varepsilon_n\ge\eta_I\) 的态只有有限个；其评价矩阵的和若秩至少 \(k\)，所含本征向量数至少为 \(k\)。这些常数并非对全部零点标签统一。证毕。

### 插值源是准确完整 theta 对象

这些 \(p_i\) 不是未指定的广义逆。已有构造可取实偶整 Fourier 源

\[
F_{p_i}(z)=
\frac{\Xi(z)}{[(z^2-w_i^2)(z^2-\bar w_i^2)]^{m_i}}
(z^2+1/4)(a_i+b_i z^2),
\]

其中这里的实系数 \(a_i,b_i\) 通过
\(F_{p_i}(w_i)=i/(2\sqrt{m_i})\) 确定；其他所选与未选零点评价皆为零。\(\operatorname{Im}(w_i^2)\ne0\) 保证两实参数可解。真实有限次零点除法已证明 \(p_i\in\operatorname{Dom}(H)\)、\(Hp_i=-v_i\)。此处不需要知道 \(\Pi_0\) 才能使用范数上界 \(\|\mathsf P\|\)。

若还希望限定过深谱，对任意 \(R>0\)，Bessel 不等式给

\[
\sum_{\varepsilon_n>R}\frac{c_nc_n^*}{\varepsilon_n}
\preceq R^{-1}\mathsf V^*\mathsf V.
\]

因此双边谱窗满足

\[
\sum_{\eta\le\varepsilon_n\le R}\frac{c_nc_n^*}{\varepsilon_n}
\succeq I_k-\eta\mathsf P^*\mathsf P-R^{-1}\mathsf V^*\mathsf V.
\tag{4.6}
\]

## 5. 与空间逃逸互补：完整负平方质量必须移向高零点

本节给出同一完整 Weil 形式下的归一化后果。对全部实际离轴四元组取代表，保持 §4 的 \(v_i=2\sqrt{m_i}b_i\)、\(u_i=H^\dagger v_i\)。对有限标签集 \(I\)，令 \(\mathsf U_I\)、\(\mathsf V_I\) 为对应列算子，并记 \(\mathsf S_I=\mathsf U_I^*\mathsf U_I\)。

对任意归一真实低态 \(Hq=-\varepsilon q\)，

\[
\mathsf V_I^*q=-\varepsilon\mathsf U_I^*q,\qquad
\frac{\|\mathsf V_I^*q\|^2}{\varepsilon}
=\varepsilon\|\mathsf U_I^*q\|^2
\le\varepsilon\|\mathsf S_I\|.
\tag{5.1}
\]

完整真实 Weil 形式与实偶性给

\[
-\varepsilon=\langle Hq,q\rangle
=\mathcal P(q)-\sum_{i\in\mathcal I_{\rm off}}|\langle q,v_i\rangle|^2,
\qquad\mathcal P(q)\ge0.
\tag{5.2}
\]

其中 \(\mathcal P\) 包含所有实零点正平方及各离轴四元组的实部正平方；负项规范准确为

\[
|\langle q,v_i\rangle|^2=4m_i[\operatorname{Im}F_q(w_i)]^2.
\]

对每个真实低态，全和由已证源系数衰减和零点计数绝对收敛。由 (5.1)–(5.2)，

\[
\boxed{\sum_{i\notin I}
\frac{4m_i[\operatorname{Im}F_q(w_i)]^2}{\varepsilon}
\ge1-\varepsilon\|\mathsf S_I\|.}
\tag{5.3}
\]

特别地，如果实际存在归一态列 \(q_j\)、\(\varepsilon_j\downarrow0\)，则对每个固定高度 \(T\)，取 \(I\) 为 \(\gamma_i\le T\) 的有限离轴标签集，得到

\[
\liminf_{j\to\infty}\sum_{\gamma_i>T}
\frac{4m_i[\operatorname{Im}F_{q_j}(w_i)]^2}{\varepsilon_j}\ge1.
\tag{5.4}
\]

这不只是未能证明频率紧性，而是条件于该态列存在时，准确证明了缩放后的负平方质量必逃向无限零点高度。

同时，对任意固定真实零点 \(w\)，完整复评价向量 \(k_w\in\operatorname{Ran}H\) 给（在实 Hilbert 空间的复化中解释，等价于分别使用实部、虚部的实评价向量）

\[
F_{q_j}(w)=-\varepsilon_j\langle q_j,H^\dagger k_w\rangle,
\qquad F_{q_j}(w)/\varepsilon_j\longrightarrow0.
\tag{5.5}
\]

这里使用谱投影证明的 \(q_j\rightharpoonup0\)，不必事先选择正交序列。因此 \(F/\sqrt\varepsilon\) 在固定标签也趋零，不能把它误作保留固定非零留数的归一。

每个序列 \(z_j(i)=2\sqrt{m_i/\varepsilon_j}\operatorname{Im}F_{q_j}(w_i)\) 属于 \(\ell^2\)、范数至少 1、固定坐标趋零，所以该族不可能在 \(\ell^2\) 强相对紧。**没有证明其范数统一有上界，因此不声称它们在全 \(\ell^2\) 中弱趋零。**

本节条件于存在 \(\varepsilon_j\downarrow0\) 的真实态列，不断言这种列存在。它与 §4 完全相容：固定有限标签的反向激活由某些非浅态承担，而越来越浅的态把自身必要的负平方质量移向更高标签。

## 6. 结论的联合使用边界

- 真实源的 \(L^2\) 紧性和近阈值统一塌缩已经成立，不必等近指数权的 \(\varepsilon\)-常数变为统一。
- 近阈值态必须把 Hilbert 质量移向空间无穷；固定复紧集的源值均趋零。不能据此推断归一态本身强趋零。
- 任意固定有限组真实离轴标签的满秩反向激活，可以由一个离开阈值的有限真实谱窗捕获，并有实际 theta 插值范数给出的界。
- 这些固定标签界没有对零点高度统一。它们与近阈值态的活动负平方质量移向越来越高的零点标签完全相容，不能拿两个不同极限顺序制造矛盾。

所剩的最短承重点是同时控制移动空间尾、移动零点窗口与 \(\varepsilon\downarrow0\) 的耦合。只重复证明固定 \(\varepsilon\) 的更强光滑性，或假设固定源范数有正下界，都不能解决它。本稿没有新增这一联合算术估计。

## 7. 继承关系与证明范围

已回看旧《全零点选择关系的反向激活与有限秩零态》及其复核：逆采样、全谱逆权下界、逐标签反向激活及留数的 \(\varepsilon\) 因子是继承结果。本稿 §4 明确定位为这些准确输入的有限谱窗推论，不把原恒等式再次包装成新证明。§§2–3 的源紧性、算子范数塌缩和空间逃逸为本轮直接写出的推导。

本文的新增推导为 §§2–5，评价向量属于 \(\operatorname{Ran}(H)\) 是上述明确引用的输入。未作形式化内核验证，未给出无条件 RH 排零结论。
