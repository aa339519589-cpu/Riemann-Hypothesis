# 全部物理平方层的二次 dual：联合 Möbius 列抵消及直接混合界的限制

本文改进 [A] Part III 的完整非主二次 dual 分支，保持原线性配对、
全部物理平方层、两支局部系数、字符零延拓和原补偿素数窗口。
新增输入是已经验收的固定 7/8 定理 [Q]，仅用于真实算术 Möbius 列。
正文同时证明该输入所需的平滑移线推论。本文不处理主/unit-core 或
一般 cubic/sextic 分支，不证明完整临界低端界或 RH。
同期更强的双线性分支界，以及两种方法直接合并的预算，见第 8 节。

## 1. 对象与结论

固定原重缩放子集 \(J\)、ray 类 \(\sigma\) 与 Mellin 参数 \(\nu\)，置

\[
X'\asymp Z^{17/48-d},\quad Y'\asymp Z^{23/48-d},\quad
P\asymp Z^{1/6-d},\quad Q=q_{b_*}X'Y',\quad0\le d\le1/6.
\tag{1}
\]

采用 [A] Part III 的准确 \(S_{\rm quad}(T)\)：在原 R4 线性配对中，
仅将 Gaussian 尺度改为 \(Tq_D\)，\(0<T\le Z\)，其他变量、字符和
slots 不变；作准确 \(m\)-Poisson 后，选择全部

\[
H=\varepsilon v^3a^6,\qquad v\ne1\text{ 好平方自由},
\tag{2}
\]

其中 \(\varepsilon\) 为任意单位，\(a\) 为任意好理想，允许 \((v,a)>1\)。
\(S_{\rm quad}(T)\) 包括全部物理 \(n\)，不只是 \(n=1\)。
原标记是 \(D\mid cn\)（等价于 \(D\mid cn^3\)）；也可以独立采用 [E]
的新 core 标记 \(D\mid cn_0\)，其中 \(n=n_0r^2\)、\(n_0\) 平方自由。
下面结论对这两个准确对象分别成立，不以一个振荡行支配另一个行。

**定理。** 对每个 \(\epsilon>0\)，存在有限阶 \(C_\epsilon\)，一致有

\[
\boxed{|S_{\rm quad}(T)|\ll_\epsilon
(1+|\nu|)^{C_\epsilon}Z^\epsilon
\frac{Q}{Y'^{3/2}}\left(\frac{TP}{X'}\right)^{1/2}
\min\left\{1,\left(\frac{Y'}T\right)^{1/8}\right\},
\quad0<T\le Z.}
\tag{3}
\]

常数可依固定算术数据、原 slots、测试函数与 \(\epsilon\)，不依
\(Z,T,\nu\) 或移动字符模数。它也适用于原 core 标记的准确 Möbius
去卷积，按第 7 节的原归一化理解。在 \(T=Z\) 时，

\[
|S_{\rm quad}(Z)|\ll_\epsilon(1+|\nu|)^{C_\epsilon}
Z^{175/384-5d/8+\epsilon}.
\tag{4}
\]

完整有限补偿后的该分支贡献为

\[
\boxed{O_\epsilon(Z^{5/128+\epsilon}).}
\tag{5}
\]

[A] 已有的同一分支为 \(O(Z^{5/48+\epsilon})\)。这里改善了实际线性
分支的界，不是完整探针的界；(5) 仍比 \(Z^{-3/16+\epsilon}\) 大
\(29/128\) 次幂。

## 2. 7/8 输入的平滑算术推论

对固定 Eisenstein 数域的有限阶 Hecke 字符 \(\psi\)，令
\(L_{\mathfrak m}(s,\psi)\) 使用其实际模数 \(\mathfrak m\) 的零延拓。
由 [Q] 的无零定理和 [L] 的 logarithmic control，对每个固定
\(\delta,\epsilon>0\)，

\[
|L_{\mathfrak m}(s,\psi)^{-1}|\ll_{\delta,\epsilon}
\{q_{\mathfrak m}(2+|\Im s|)\}^{\epsilon},
\qquad\Re s\ge7/8+\delta.
\tag{6}
\]

这里必须使用包含全部删除 Euler 因子的模数，不能仅用原始 conductor
而允许另一个任意大的 imprimitive 模数。有限删除因子的逆由
\(\prod_{p\mid\mathfrak m}(1-q_p^{-\sigma_0})^{-1}
\ll_{\sigma_0,\epsilon}q_{\mathfrak m}^{\epsilon}\) 控制。
主字符的 \(s=1\) 极点在倒数中是可去零值，不产生留数。

**引理。** 设 \(w\in C_c^\infty(0,\infty)\) 固定。
对任意 \(X>0\)、实 \(\tau\)，一致有

\[
\left|\sum_a\frac{\mu(a)\psi(a)}{q_a}
w(q_a/X)(q_a/X)^{i\tau}\right|
\ll_{w,\delta,\epsilon}
X^{-1/8+\delta}q_{\mathfrak m}^{\epsilon}(1+|\tau|)^B.
\tag{7}
\]

**证明。** 在 \(\Re s>1\)，原零延拓给出准确 Euler 级数
\(\sum_a\mu(a)\psi(a)q_a^{-s}=1/L_{\mathfrak m}(s,\psi)\)。
对 \(w_\tau(u)=u^{-1+i\tau}w(u)\) 使用 Mellin 反演，则 (7) 左侧的
未取模表达式是

\[
\frac1{2\pi i X}\int_{(2)}
\widehat w_\tau(s)X^sL_{\mathfrak m}(s,\psi)^{-1}\,ds.
\tag{8}
\]

移线到 \(\Re s=7/8+\delta\)，其中可先取 \(0<\delta<1/8\)。
由 (6) 与固定紧支撑，Mellin 权在每个固定实条带任意幂次衰减，
其竖向移位 \(\tau\) 只造成多项式损失。水平边趋零，移线无留数。
新积分给 \(X^{-1/8+\delta}\)，得到 (7)，对所有 \(X>0\) 成立。
这不是截断 Perron 积分，也没有 Perron 尾误差。证毕。

这里的 Dirichlet 级数是实际 \(\mu\psi\) 算术级数；没有将谱本征源
自动视为普通 Dirichlet 类。新推论使用 [Q] 的已验证定理，未反向作为
该定理自身的证明输入；本文新增论证没有另外宣称 Lean 验收。

## 3. 全部物理层的残余列确实具有这个字符

继承 [A] 的准确平方层、mask 和 Poisson 换元：写 \(n=n_0r^2\)，
\(h\mid\operatorname{rad}r\)，\(j=(h,\operatorname{rad}s)\)、\(k=h/j\)。
存活项满足 \(j^2\mid s\)、\((s,k)=1\)、\((h,cn_0)=1\)。
频率变为 \(H'=H/r^6=\varepsilon v^3(a')^6\)，保持同一非主二次 core。
两支局部系数给 \(n_0\mid v\)、\((n_0,a')=1\)。置

\[
E=(c,n_0),\quad F=n_0/E,\quad
g=(c,\operatorname{rad}H')/E,\quad c=Egc_1.
\tag{9}
\]

全部存活项保留 \((c_1,n_0hH')=1\)。Ramanujan 因子只以 \(q_g\)
控制，消去 \(q_c^{-1}\) 中的 \(q_g^{-1}\)，留下原权
\(1/(q_{n_0}q_Eq_{c_1})\)，不是以 \(q_{Fg}\) 控制。

原第一 Poisson 的 inverse Gauss 与 primitive Gauss 因子已经准确消去。
对自由列 \(c_1\)，剩余相位是

\[
\mu(c_1)\eta(c_1)\overline{\chi_{c_1}(H')}.
\tag{10}
\]

这可以直接从 [P] 的 coefficientwise unit-factor 与 pair-phase 消去
核对：对自由列素数 \(p\mid c_1\)，有 \(p\nmid n_0H'\)，局部变量为
\(e_0=1,l=0,j=m=k_s=0\)。源 family table 的 \((1,2r)\)、\(r=0\)
行给 \(-\eta(p)\rho^{-1}\)，\(\rho=\chi_p(H')\)。因此没有残余
\(\alpha\)、inverse Gauss 或随 \(n_0\) 变化的非字符列因子。
\(n_0\) 的两支已冻结在 \(E,F\)，不能用单独一支代替它们。

展开自由 \(s\) 与 \(c_1\) 的互素 mask 后，固定其平方自由因子 \(e\)。
定义

\[
D_0=D/(D,gn_0r),\quad L=\operatorname{lcm}(e,D_0),\quad c_1=Lc_0.
\tag{11}
\]

core 标记时在 \(D_0\) 中去掉 \(r\)。不相容项先取零；其余项中
\(\mu(L)\eta(L)\overline{\chi_L(H')}\) 是固定标量。
\(c_0\) 的原 squarefree 和互素条件由 \(\mu(c_0)\) 与零延拓保存。
sextic reciprocity 把 (10) 写成有限阶 Hecke 字符；固定 ray 条件可作
固定有限 Fourier 展开。额外零延拓包括 \(LEgn_0hH'\)，实际模数满足

\[
q_{\mathfrak m}\ll(q_{H'}q_{n_0}q_hq_L)^C.
\tag{12}
\]

\(q_{n_0}\le q_{H'}^{1/3}\)、\(q_h\le q_r\)、\(q_L\le q_eq_D\ll Y'P\)。
故 (7) 的模数损失可统一计入 \(Z^\epsilon(q_{H'}q_r)^\epsilon\)。
此处没有把 moving prime 加入固定坏素数集。

## 4. 联合权重先分离，紧支撑留在每个模式中

准确全模数仍是 \(b_*scn_0^3\)。原耦合 Fourier 权是

\[
\widehat\Omega_\nu\left(\frac{\sqrt Q H'}{b_*scn_0^3}\right).
\tag{13}
\]

取 Gaussian 对数 annulus \(\ell\in\mathbb Z\)，

\[
C_\ell\asymp e^\ell TP/(q_{n_0}^3q_r^6),\quad
C_{1,\ell}=C_\ell/(q_Eq_g),\quad X_0=C_{1,\ell}/q_L.
\tag{14}
\]

在 \(x=q_{c_0}/X_0\)、\(y=q_s/Y'\) 的固定正 annuli 上，(13) 为
\(R_\nu(\lambda/(xy))\)，其中 \(R_\nu(u)=\widehat\Omega_\nu(z)\)
当 \(|z|^2=u\)。该函数径向，但不要求实或非负。

\[
\lambda=\frac{X'q_{H'}}{C_\ell q_{n_0}^3}
=\frac{q_{H'}}{K_\ell},\qquad
K_\ell=C_\ell q_{n_0}^3/X'
\asymp e^\ell TP/(q_r^6X').
\tag{15}
\]

特别地，\(K_\ell\) 与 \(n_0\) 无关。
包括 Gaussian、\(y^{-1/2+i\nu}\) 与原 cutoffs 的联合对数 profile
\(F_\lambda(x,y)\) 有统一半范数；对每个固定 \(A,N\)，其对数 Fourier
系数满足

\[
\int |\widehat F_\lambda(\tau,\zeta)|
(1+|\tau|+|\zeta|)^A\,d\tau d\zeta
\ll(1+|\nu|)^B e^{-c\ell^2}(1+\lambda)^{-N}.
\tag{16}
\]

这由固定 annuli 上的 Schwartz 导数界与对数分部积分得到。
其常数独立于所有移动范数标签。Gaussian annulus 的导数多项式也由
略弱的 \(e^{-c\ell^2}\) 吸收。

必须另外保留固定乘积 cutoffs \(\rho_x,\rho_y\)，它们在原 profile
支持上等于一。准确使用

\[
F_\lambda(x,y)=\rho_x(x)\rho_y(y)\frac1{(2\pi)^2}
\int\widehat F_\lambda(\tau,\zeta)x^{i\tau}y^{i\zeta}\,d\tau d\zeta.
\tag{17}
\]

于是每个分离模式仍是紧支撑的 \(c_0\) 和自由 \(s\) 和；不能反演后
只留下没有截断的纯范数幂。所有非光滑算术 masks 在分离前已固定。
固定坏模数上的两变量 ray 系数可先在固定有限群的乘积上 Fourier
分解为列字符与自由 \(s\) 的固定周期因子，总质量只造成固定常数。
每个模式的 \(c_0\) 因子用 (7)；自由 \(s\) 的原非主二次字符
\(\chi_v(\cdot)^3\) 用 [A] 的全正尺度第二 Poisson 界
\(O(\sqrt{q_v})\)。其测试函数导数仅有 \(\zeta\) 的多项式损失，固定
坏模数因子造成固定常数。(16) 吸收两处高度损失，同时保留 \(H'\) 尾。
没有先以依赖 \(c_0\) 的绝对值界代替 \(s\) 和后再声称 Möbius 抵消。

## 5. 标记 LCM 与自由 mask 因子的质量

由 (7)，原正项列质量 \(q_L^{-1}\) 改为

\[
q_L^{-1}X_0^{-1/8+\delta}
=C_{1,\ell}^{-1/8+\delta}q_L^{-7/8-\delta}.
\tag{18}
\]

先保留 \(\kappa=1/8-\delta\in(0,1/8)\)，则为
\(C_{1,\ell}^{-\kappa}q_L^{-1+\kappa}\)。
由 \(q_L\le q_eq_D\asymp q_eP\) 和 [A] 的真实 slot LCM 密度，

\[
\sum_D|w_D|/q_L\ll_\epsilon(q_rq_{H'})^\epsilon/q_e,
\tag{19}
\]

得到

\[
\sum_D|w_D|C_{1,\ell}^{-\kappa}q_L^{-1+\kappa}
\ll_\epsilon C_{1,\ell}^{-\kappa}P^\kappa q_e^{-1+\kappa}
(q_rq_{H'})^\epsilon.
\tag{20}
\]

代入 (14)，\(P\) 的幂准确消去，留下

\[
e^{-\kappa\ell}T^{-\kappa}
q_{n_0}^{3\kappa}q_r^{6\kappa}q_E^\kappa q_g^\kappa
q_e^{-1+\kappa}(q_rq_{H'})^\epsilon.
\tag{21}
\]

非空 \(s\) 支持仍强制
\(q_Fq_gq_j^2q_eq_f\ll Y'\)，其中 \(f\) 是 [A] 中固定的其余互素
mask 因子。理想计数给

\[
\sum_{q_e\ll Y'/(q_Fq_gq_j^2q_f)}q_e^{-1+\kappa}
\ll_\kappa\left(\frac{Y'}{q_Fq_gq_j^2q_f}\right)^\kappa.
\tag{22}
\]

即使右侧尺度小于一，非空项也只能发生在固定支持常数允许的范围，
同一计数界成立。\(g\) 的幂准确消去。新增共同因子为

\[
(Y'/T)^\kappa\,
q_{n_0}^{3\kappa}q_r^{6\kappa}q_E^\kappa q_F^{-\kappa}
q_j^{-2\kappa}q_f^{-\kappa}e^{-\kappa\ell}.
\tag{23}
\]

\(e\) 的求和在此只用绝对质量。虽然互素展开有 \(\mu(e)\)，但
\(\mu(c_1)\) 提取 \(L\) 后准确有

\[
\mu(e)\mu(\operatorname{lcm}(e,D_0))=\mu(D_0/(D_0,e)).
\tag{24}
\]

所以没有留下一个可直接再次使用 (7) 的自由 Möbius \(e\) 和。

## 6. 两支物理系数、平方层和全部尾部

[A] 的原正权为
\((q_{n_0}q_E)^{-1}q_r^{-5+\epsilon}/q_k\)。乘 (23) 后，原两支
\(E,F\) 的加权和是

\[
\sum_{n_0\mid v}\sum_{E\mid n_0}
q_{n_0}^{-1+3\kappa}q_E^{-1+\kappa}q_F^{-\kappa}
=\prod_{p\mid v}(1+q_p^{-2+4\kappa}+q_p^{-1+2\kappa})
\ll_\epsilon q_v^\epsilon.
\tag{25}
\]

当 \(\kappa\le1/8\)，两项指数分别至多 \(-3/2\)、\(-3/4\)。
有限 Euler 产品的任意小幂界可由分离有限个小范数素数证明，不需要
把 \(-3/4\) 的全素数和误称为收敛。
平方层成本为 \(q_r^{-5+6\kappa}\le q_r^{-17/4}\)，仍绝对可和；
\(h,j\) 的选择数、所有额外模数损失与原 \(g,f\) 除数数目用各自
任意小幂吸收。它们均保留原非单位零值。

由 (15)，[A] 的加权二次频率计数在 \(K_\ell\ge1\) 时为
\(O(K_\ell^{1/2+\epsilon})\)，在 \(K_\ell<1\) 时为
\(O(K_\ell^{1/2})\)。它使用完整 Schwartz 尾，未硬截断 \(H'\)。
在 (16) 中增加固定衰减阶可吸收 \((q_{H'}q_r)^\epsilon\)。
\(K_\ell\) 不含 \(n_0\)，所以 (25) 可在频率计数前完成。
\(e^{-\kappa\ell}\) 和小幂损失由 Gaussian annulus 和吸收，全部物理
层和傅里叶尾仍绝对可控。

当 \(T\ge Y'\)，所得 [A] 右侧多出 \((Y'/T)^\kappa\)。取
\(\delta>0\) 足够小，用
\((T/Y')^\delta\le Z^{O(\delta)}\) 吸入 \(Z^\epsilon\)，得到 (3) 的
\(1/8\) 指数。\(T<Y'\) 时用 [A] 原界，完成 (3) 的全尺度表述。
没有声称 \(7/8\) 边界无零，最终 \(Z^\epsilon\) 正是缓冲损失的预算。

## 7. 准确去卷积、原补偿与缺口

[E] 的 core 标记去卷积是同一物理 probe 的准确尺度和：外部理想
\(b\) 的系数为 \(\mu(b)\kappa_\eta(b)q_b^{-2}\)，
\(\kappa_\eta(b)=\eta(b)^6\overline{\alpha(b)}^6\)，尺度为 \(T=Z/q_b^6\)。
全模数提升把 \(H\) 乘 \(b^6\)，保持单位与非主二次 core，因此该分支
与去卷积相容。这个 \(b\) 不指固定 \(b_*\)。

当 \(q_b\le(Z/Y')^{1/6}\)，(3) 相对于原 \(q_b^{-5}\) majorant 多出
\((Y'/Z)^{1/8}q_b^{3/4}\)，于是 \(q_b^{-17/4}\) 的和收敛。
剩余尾用原 \(q_b^{-5}\) 界，理想计数给

\[
\sum_{q_b>(Z/Y')^{1/6}}q_b^{-5}
\ll(Y'/Z)^{2/3}\le(Y'/Z)^{1/8}.
\tag{26}
\]

因此同一改善通过准确去卷积，未把未经证明的负指数低端界逐项求和。

在 \(T=Z\)，原 \(25/48-d/2\) 减去
\(\frac18(1-23/48+d)=25/384+d/8\)，得到 (4)。
\(Q^{-1/2}\) 后指数为 \(5/128+3d/8\)。再乘原重缩放 tuple 的
\(O(Z^{d+\epsilon})\) 计数及 \(q_\rho^{-3/2}\asymp Z^{-3d/2}\)，成为
\(5/128-d/8+\epsilon\)，其最大值在 \(d=0\)，证明 (5)。
\(\widehat W_0(i\nu)\) 的任意阶衰减吸收固定多项式高度损失。

本文只控制完整非主二次类型。主/unit-core、一般 cubic/sextic 类型的
低端相关及全部非主高端比较仍未证明；不能将 (5) 扩展为整个 R4。
即使仅这一类型，\(5/128-(-3/16)=29/128\) 的差距也仍存在。

## 8. 与后续双线性方法的准确比较

仓库后续 [B] 的 Part IV–V 使用平方自由 quadratic 大筛与长光滑列
Poisson，给出同一完整非主二次类型的更强补偿界
\(O(Z^{-1/32+\epsilon})\)。本文 (5) 是不同输入的 Möbius 列估计，
不是该类型当前最强的界，也不能直接把两次节省相乘。

在 [B] 的公共系数接口中，列平方质量为 \(O(L_c^{-1+\epsilon})\)，
quadratic 大筛给列范数 \(O(Z^\epsilon\sqrt{1+V/L_c})\)。
若尝试同时使用 (7)，列中的 selected-slot 除数多项式必须先展开。
对分配到列的标记 \(D_C\)，提取它后该份质量为

\[
q_{D_C}^{-1}(L_c/q_{D_C})^{-\kappa}
=L_c^{-\kappa}q_{D_C}^{-1+\kappa}.
\tag{27}
\]

窗口内理想计数给 \(\sum_{D_C}q_{D_C}^{-1+\kappa}\ll P_C^\kappa\)，
其中 \(P_C\) 是列 slots 的总范数尺度。对 \(O(V)\) 个行，合法的
Möbius 范数上界因而是
\(O(Z^\epsilon\sqrt V(L_c/P_C)^{-\kappa})\)，不能直接对任意
divisor-bounded 公共列系数使用 \(\sqrt V L_c^{-\kappa}\)。

原 \(d=0\) 的主导 dyad 和 \(S\asymp V\) 转折有

\[
V=Z^{13/48},\quad C=ZP=Z^{7/6},\quad Y'=Z^{23/48},\quad
L_c=CV/Y'=Z^{23/24}.
\tag{28}
\]

允许全部 slots 分配到列，此时 \(P_C=P=Z^{1/6}\)。大筛上界在这个
尺度是 \(Z^\epsilon O(1)\)，而 Möbius 上界表达式的幂为

\[
\frac{13}{96}-\frac{19}{24}(1/8-\delta)
=\frac7{192}+\frac{19}{24}\delta>0.
\tag{29}
\]

所以逐块直接取两个现有上界的较小者，在这个主导尺度仍选择大筛，
并没有提供新的负幂。即使错误省去标记成本，幂也仍为
\(1/64+(23/24)\delta>0\)；省去成本仍不合法。
对该尺度，要使这一点态 Möbius 界严格小于大筛的 \(O(1)\)，需
\(\kappa>13/76\)，即一个更强的无零输入 \(\beta<63/76\)，已有
\(\beta=7/8\) 没有达到它。

这里比较的是可用的上界表达式，不是实际列范数的下界，也没有排除
新的混合相关方法。它只说明直接逐块取最小值没有改善 [B] 的主导
预算。该报告的 \(-1/32\) 距完整临界低端 \(-3/16\) 仍差 \(5/32\)，
主/unit-core 和一般 cubic/sextic 类型的缺口亦保留。

## 9. 固定来源与核验范围

[Q] [固定 7/8 输入的实际 Lean 验收](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/52ee48d3e2e4c5b0beeb3e4880eca86fb2208ce1/reports/20261011_qrh_selection_bridge/FORMAL_INPUT_Q.md)，
包括真实 Hecke/ray 目标及其公理依赖；验收来源为 `openai/math`
提交 `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`。

[P] 该固定提交的 [paper.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)：
第 3734–3752 行的全模数 Poisson，第 3927–4010 行的 coefficientwise
unit/pair cancellation，第 4082–4126 行的两支 odd 局部表。

[L] 同一 [固定 paper.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
第 1415–1640 行的 Hecke strip growth、logarithmic control 与删除 Euler
因子界；对应 `Hecke/ReciprocalGrowth.lean`、`Hecke/DeletionBounds.lean`。
这些是既有源输入，不是本文声称的新 logarithmic-control 定理。

[A] [全部物理层的准确二次分支](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/1e3001668867f1cc83f9375e2084c8b43263fe11/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md)，
Part III，以及该提交的对应 referee；本文继承其准确对象、两支物理
归一化、slot LCM 密度与全尺度二次 Poisson/尾部计数。

[E] [准确 Euler 去卷积与 core 标记](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/dfc211e29c3ac231ada82a640601753c9a119695/reports/20261011_qrh_selection_bridge/EULER_DECOMPLETION.md)，
Part II、IV 的平方层身份与物理去卷积定义。

[B] [后续公共系数双线性接口与完整二次分支](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/84725e7f210fbb45818dcbaae89339a6cc31bd9d/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md)，
Part IV–V。其大筛输入为 Goldmakher–Louvel 的
[Theorem 1.1 和 Corollary 1.2](https://arxiv.org/pdf/1112.1642)，
两端均为平方自由理想；第 8 节只比较这一公共系数接口的已给范数。

新增步骤为 (7)、(17)–(23) 的联合抵消、改进后的 (25)–(26) 求和及
(27)–(29) 的准确标记混合界比较。
`REFEREE_QUADRATIC_MOBIUS_GAIN.md` 记录独立逐式核验。
`check_quadratic_mobius.py` 只复算精确指数、局部 Möbius–LCM 身份与
缓冲幂符号；脚本通过不认证无限抵消、引用输入或 RH。
