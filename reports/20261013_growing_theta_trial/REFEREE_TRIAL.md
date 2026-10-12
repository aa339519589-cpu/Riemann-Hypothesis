# 独立数学审稿：Laguerre 尾部试向量与条件性 Schur 上界

审阅对象：`LAGUERRE_SCHUR_TRIAL.md` 的最终修订稿；profile 输入为 `GROWING_JET_FRAME.md`。审阅只覆盖本 witness 及其指定接口，没有重审已经单独通过的 growing-profile 定理。

## 裁定

**通过，按文中明确写出的条件性结论。** 对任意固定非零 (W\in C_c^\infty(0,\pi))，修订稿构造的 collar 向量满足

\[
\|y_k\|_2^2\longrightarrow 2\int_0^\pi |W(s)|^2e^{-2s}\,ds>0,
\]

并给出一个 full-old-space 试向量 (v_k)，使完整 polar-inclusive 新窗口二次型 \(\mathfrak A_{a_{k+1}}[v_k+y_k]=o(1)\)。因此**若** full old block 对其全旧形式域 coercive-positive，实际 full-old Schur 变分量满足 \(\operatorname{Schur}_{k+1}[y_k]\le o(1)\)。coercivity 是假设，不是本 witness 的结论；全文也没有推出 Schur 的正负号、全窗正性或 RH。

## 逐项核验

**Laguerre 半轴逼近。** 变量变换给出

\[
e^{-2s}ds=\frac{e^{4\pi}}2e^{-x}dx,
\qquad x=2(s+2\pi),
\]

故 \(\phi_n(s)=\sqrt2e^{-2\pi}L_n(x)\) 的归一化正确。目标函数变换后支撑在 \((4\pi,6\pi)\)，所以 Laguerre Sturm--Liouville 算子反复分部积分没有端点项，并给出任意阶谱系数衰减。恒等式 \(L_n'=-\sum_{j<n}L_j\) 确实给 \(\|L_n'\|_{L^2(e^{-x})}=\sqrt n\)；与系数加权平方和作 Cauchy--Schwarz 后，半轴上的普通一阶导数误差是 \(O(m^{1-p})\)。这项估计不靠退化的 \(x|F'|^2\) Laguerre 能量，因此端点 \(x=0\) 没有漏控。多项式权重和固定阶导数由 Laguerre 三项递推及任意阶系数衰减控制。

内积已明示为共轭线性于第一槽，且展开系数现为 \(c_n=\langle\phi_n,W_0\rangle\)，所以复值 (W) 的投影方向正确。该系数方向适用于所有复值 W。

**首频密度、缩放与物理导数。** 由首频多项式的首项

\[
f_0(x)=e^{x/2}\mathcal F_0(u)e^{-u}+\text{higher frequencies},
\quad \mathcal F_0(u)=-32u^5(1+O(u^{-1})),
\]

有 \(f_0\sim-32\pi^{-1/4}u^{21/4}e^{-u}\)。在 \(u=U+s\ge U-2\pi\) 上，其余 theta 频率相对首频及其一次导数为 \(O(u^Me^{-3u})=O(U^{-1})\)，误差在整条所需尾区间一致。配合 \(dx=du/(2u)\) 与 \(\sigma_k^2=(512/\sqrt\pi)U^{19/2}e^{-2U}\)，得到

\[
d\nu_k=(u/U)^{19/2}e^{-2s}(1+O(U^{-1}))ds,
\qquad f_0/\sigma_k=-\sqrt{2U}(u/U)^{21/4}e^{-s}(1+O(U^{-1})).
\]

指数、幂次和常数因子一致；首项为负也与报告的幅度符号吻合。并且 \(f_0'/f_0=O(u)\) 在该尾区间成立。特别地，(W\ne0) 时用首条密度在紧支撑上积分，正好得到上面的严格正范数极限。

因此实际密度满足 \(d\nu_k\le C(1+s_+)^{19/2}e^{-2s}ds\)。取 (A=2)，式 (10) 中导数转换的额外 \((1+s_+)\) 因子与权重合计使最高幂为 \(19/2+4=13.5<24\)；(H^1_{24}) 控制确实够用。由

\[
z_k=\sigma_k^{-1}f_0H_k,
\qquad z_k'=\sigma_k^{-1}f_0\big[(f_0'/f_0)H_k+2uH_k'\big],
\]

以及 \(u/U\le C(1+s_+)\)，得到 \(\|z_k\|_2\le C\epsilon_{0,k}\)、\(\|z_k'\|_2\le Ck\epsilon_{1,k}\)。这给出后续 Gamma 估计所需的真实全尾 (H^1\) 控制。

**增长速率与 Gamma 项。** 对 (m_k=\lfloor(\log k)^{1/4}\rfloor) 取任意固定 (r>2)，Laguerre 误差为 \(\epsilon_{0,k}=O(m_k^{-r})\)、\(\epsilon_{1,k}=O(m_k^{1-r})\)。故

\[
(\log k)\epsilon_{0,k}^2=O((\log k)^{1-r/2})\to0,
\qquad \epsilon_{1,k}^2\to0.
\]

并且 \(\epsilon_{0,k}^2\log(1+\epsilon_{1,k}/\epsilon_{0,k})\to0\)。独立通过的 growing-profile 逼近误差为 \(k^{-1}e^{O(m_k^2\log(m_k+2))}\|P_{m_k}\|_{H^1_{24}}=k^{-1+o(1)}\)，因 \(m_k^2\log m_k=o(\log k)\) 且固定 (W) 的 \(\|P_{m_k}\|_{H^1_{24}}=O(1)\)。其 Taylor、remote-tail 与 omitted-frequency 点态估计也足以给出 (A_k=k^{o(1)}) 的统一 profile envelope；报告没有从加权 (H^1) 单独误推点态界。

Gamma 符号上界 \(b(t)\le4+\tfrac12\log(1+4t^2)\le\log k+4+2(t/k)^2\) 的常数与缩放正确。Plancherel 后的双侧式 (12) 配合上述物理 (H^1) 控制，使 \(|\mathfrak q_\Gamma[z_k]|\le C((1+\log k)\epsilon_{0,k}^2+\epsilon_{1,k}^2)=o(1)\)。这里处理的是有限 Gamma 能量的具体残差，不要求存在全局闭的 (T=a(D)-S) 算子。

**完整 signed prime 与 polar 项。** 对正翼支撑在 \([R_k,\infty)\) 的奇函数，按两个同翼区间及负翼到正翼的交叉区间拆分后，

\[
\mathfrak p[z]=-4\sum_{n\ge2}\alpha_n\operatorname{Re}J_n
              +2\sum_{n\ge2}\alpha_n\operatorname{Re}C_n
\]

系数和交叉符号正确。same-wing 关系 \(s'=n^2(U+s)-U\) 给指数 \(e^{-c(n^2-1)U}\)；跨翼 AM--GM 给 \(s_1+s_2\ge2\pi(n-k)\)。交叉区间从 \(n\ge\lceil ke^{-2/k}\rceil=k-1\) 起。写 (n=k+j\) 后 (j\ge-1)，其端点宽度满足 \(kL_n\le C(j+2)\)；所用的 (j+2) 正好支付 (n=k-1) 这一非空交叉区间。再以 \(\alpha_n\le\log n/\sqrt n\) 扩大到全整数并对指数尾求和，得 \(\sum\alpha_n|C_n|\le CA_k^2\log k/\sqrt k\)。同翼项为 \(CA_k^2e^{-c k}\)。这覆盖所有素数幂和两个纵翼；(A_k=k^{o(1)}) 时总贡献为 (o(1))。

点态振幅 (0b) 与 envelope (20) 给

\[
|\ell(z_k)|\le Ck^{-1/4}A_k,
\qquad 2|\ell(z_k)|^2=O(k^{-1/2}A_k^2)=o(1).
\]

所以全尾二次型 \(\mathfrak t[z_k]=\mathfrak q_\Gamma[z_k]+\mathfrak p[z_k]-2|\ell(z_k)|^2=o(1)\) 的三项均在其实际定义域内：Gamma 能量有限，prime 相关绝对收敛，polar 积分绝对存在。开头的配对类条件已明确列出这三点；文本没有假定该源表达式在整个未加权 (L^2) 上闭合。

**精确消去及 full-old 变分解释。** 对有限 theta jet 组合 (F_k\)，由已定义的完整源恒等式 (T f_0=0)、(T) 与偶阶导数/平移的交换性，得到 (T G_k=0)；分部积分给每个 (f_j) 的 polar functional 为零，故 \(\ell(G_k)=0\)。对本案出现的所有交叉配对，theta 导数双指数尾或上面的残差 envelope 使 prime 级数绝对收敛；Gamma 极化由 (H^1) 有限性控制，polar 极化绝对有限。因此 Hermitian 复极化

\[
q[a]-q[b]=\operatorname{Re}\mathfrak t[a-b,a+b]
\]

适用，式 (28) 确实等于零。\(v_k+y_k\) 光滑紧支撑在下一窗，因而其全源形式等于 \(\mathfrak A_{a_{k+1}}\)；\(r_k-y_k\) 不是紧支撑向量，报告正确地只把 \(\mathfrak t[r_k-y_k]\) 当成按三项定义的全尾形式，而未写成未定义的有限窗算子形式。

[SHARP_WINDOW_DOMAIN.md，§§1–4](../20261012_localized_odd_schur/SHARP_WINDOW_DOMAIN.md) 给出 old/collar 最大 Gamma 形式域直和、bounded cross block 和 Schur 变分公式的域依据。报告现把 \(\inf\) 的范围写成全旧形式域 \(\mathcal D_{\rm old}\)，并把 coercive-positive 条件放在等式之前。因此试向量确实给全旧 Schur 上界，不是 fixed-pivot 或受限 (Q_k) 上界。这个 old coercivity 仍是独立假设，文中没有证明它。

## 结论边界

固定非零 (W) 的 collar 范数有严格正极限，故 \(o(1)\) 上界不是向零向量缩放得到的平凡式。通过后仍只得到条件性 Schur 上界 \(\operatorname{Schur}_{k+1}[y_k]\le o(1)\)，没有下界，不能确定其符号；也没有推出全窗口正性或任何 RH 结论。Growing-profile 输入按任务约定采纳其独立审稿 PASS，本审稿未重跑其证明。
