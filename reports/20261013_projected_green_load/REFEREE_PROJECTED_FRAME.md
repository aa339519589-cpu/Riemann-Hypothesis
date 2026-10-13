# Independent referee: growing theta-jet frame after fixed exact Q projection

审阅对象：[PROJECTED_FRAME.md](PROJECTED_FRAME.md)（2026-10-13）。

## 结论

**就文中所声明的固定 $d$、精确 $Q_k$ 投影后的 growing-profile 定理和 pointwise envelope 而言，PASS。** 我没有发现实质性错误。作者没有把结论外推到 $Q_k$ 限制 Schur 符号或其正性；这条范围边界是必要且正确的。

独立核查覆盖了：原 theta strip 上的 $L^2$-值平移全纯性及由此得到的全局高阶 jet 范数、固定维 cut Gram 逆界和投影系数增长、带旧 jet 投影的缩放 Taylor 矩阵及其 shifted-binomial 节点行列式、Taylor 余项和远尾、所有 $n\ge2$ theta 频率、精确 $Q_k$ 正交，以及最后的 pointwise envelope。

## 核查要点

1. **原 theta strip 足以给出全局 jet 的 growing-index $L^2$ 界。** 在任意闭窄条 $|\operatorname{Im}z|\le\sigma<\pi/4$ 上，正实方向有 $\cos(2\operatorname{Im}z)\ge\cos(2\sigma)>0$；对 theta 级数任意一个固定阶导数逐项微分只添多项式因子，$n=1$ Gaussian 可抽出 $e^{-c_\sigma e^{2x}}$，其余 $n$-和由二次指数求和控制。实轴上的 theta/Jacobi 偶性，加上 $\Phi(z)$ 和 $\Phi(-z)$ 在对称连通条带上全纯，给出条带内的偶性；因此可将正尾估计反射为负尾估计。这里没有假设一个未证明的全平面 even analytic extension，也不需要接触条带边界。于是对每个紧复平移集，$f_0(\cdot+z)$ 及其所需固定阶差商有统一平方可积控制，支配收敛给出 $G(z)=f_0(\cdot+z)\in L^2$ 的全纯性和在 $|z|\le\sigma$ 上的有界性。取例如 $\sigma=\pi/8$ 作 Banach 值 Cauchy 估计，确得
$$
\|f_j\|_2=\|G^{(2j)}(0)\|_2
\le C_\sigma(2j)!\sigma^{-2j}
\le e^{Cj\log(j+2)}.
$$
将实轴 Jacobi 偶性明确引用到原 theta 定义即可；后面的条带内偶性是由恒等定理推出，不是另行假定。

2. **固定旧 Gram 逆界和 $p_{ij,k}$ 增长正确。** 每个固定 $f_i$ 属于 $L^2$，且 $\chi_k\to1$ 点态、$|\chi_k|\le1$，故固定 $d$ 的 cut Gram 矩阵由支配收敛趋于完整 Gram 矩阵。Fourier 变换的共同因子 $\Xi$ 是非零 entire function；它在某个实开区间不为零，所以任何 $f_0,\ldots,f_{d-1}$ 的 $L^2$ 线性关系会使相应有限次 $t^2$ 多项式在区间上为零，系数全为零。极限 Gram 正定，逆在足够大的 $k$ 上一致有界。正规方程右端满足 $|b_{rj,k}|\le\|f_r\|_2\|f_j\|_2$，结合上一步即得式 (6) 的 uniform-in-$k$ growing-$j$ 控制。

3. **精确投影与 projected Taylor matrix 的缩放正确。** $v_{j,k}=\chi_k f_j-P_{E_k}(\chi_kf_j)$ 按投影定义精确属于 $Q_k$；未截断的 $\widetilde f_{j,k}$ 仍是固定系数的 exact source zero mode。旧列中最高多项式次数为 $2d-2$，而高列缩放分母是 $U^{2(d+\ell)}$，因此最差旧多项式扰动为 $P_{d,m}U^{-2}$（后续列更小）。高列低次商项各少一个 $U$，有理项由 Cauchy 界控制；投影系数的 $e^{C_dm\log(m+2)}$ 损失仍被显示的矩阵误差吸收。binomial-Vandermonde 节点是 $2d,2d+2,\ldots,2d+2m-2$。因节点差为 $2(j-i)$，且行多项式首项系数为 $1/q!$，
$$
\det V^{(d)}
=\frac{2^{m(m-1)/2}\prod_{r=1}^{m-1}r!}
        {\prod_{q=0}^{m-1}q!}
=2^{m(m-1)/2}.
$$
cofactor/Hadamard 界连同 $4^{d+\ell}$ 列缩放给出 $e^{C_dm^2}$ 的逆界。$m\le(\log k)^{1/4}$ 时，$U^{-1}e^{C_dm^2+C_dm\log(m+2)}=o(1)$ 对全体允许的 $m$ 由同一个充分大的 $k_{d,A}$ 保证。式 (16) 的缩放方向正确，给出精确 Taylor 匹配及式 (17) 的系数界。

4. **$q<m$ 的零导数边界情形已一致处理，Taylor 余项抵消成立。** 对次数低于导数阶的单项式，$\binom vq=0$，所以 Taylor 矩阵中高行的该项消失；Taylor 余项里当 $m>2i$ 时旧 $Q_i$ 的 $m$ 阶导数也确实为零。非零时，高列次数最多 $2(d+\ell)$，导数最多贡献 $U^{2(d+\ell)-m}$，与 $a_\ell$ 中的 $U^{m-1-2(d+\ell)}$ 合成 $U^{-1}$。旧多项式项的最差幂为 $U^{2i-2(d+\ell)-1}\le U^{-3}$。有理项由阶 $m$ Cauchy 界再多给至少一个 $U^{-1}$。求和因子并入 $e^{C_dm^2\log(m+2)}$ 后，式 (19)–(20) 及固定区间加权 gamma 矩估计成立。

5. **远端、完整 theta profile 误差及 pointwise envelope 都支付了 growing 系数。** 式 (21) 对 $s\ge U/2$ 的包络把高列商多项式、旧固定次数项和有理项都覆盖。平方后的权重被积函数对数导数是
$$
\frac{4(m+d)+2}{U+s}+\frac{A}{1+s}-2,
$$
在统一的 $U\gg_{d,A}m$ 阈值后小于 $-1$；端点贡献至多 $e^{C_{d,A}m^2\log(m+2)+C_dm\log U-cU}$。对于完整 theta 商，$n=2$ 相对首项恰带 $e^{-3u}$，其 $(1+n)^{4(d+m)+14}$ 因子为 $e^{O_d(m)}$；$n\ge3$ 的二次指数在 $U\gg_d m$ 后给可和控制，一阶 $u$ 导数增加的 $n^2$ 已包含在幂预算内。商法则因此给出式 (23)；再乘 $a_\ell$、投影系数并积分，所有额外 $O_d(m\log U)$ 幂损失仍由 $e^{-cU}$ 吸收。最后，从 (20) 得到中段多项式包络；在 $s\ge U/2$，式 (21) 中 $U^m(1+s/U)^{2(m+d)+1}\le C^{O(m+d)}(1+s)^{2(m+d)+1}$，故有式 (25) 的全域包络。系数到 polynomial norm 转换用移位 Legendre 基：单项式系数和至多 $e^{Cm\log(m+2)}$，权在 $[0,1]$ 上有正下界，所以 $\|\beta\|_2\le e^{C_Am\log(m+2)}\|P_\beta\|_{H^1_A}$；此损失可并入所有声明的指数常数。

6. **源项幂次与反射界正确。** 在正尾 $e^{x/2}=(u/\pi)^{1/4}$ 且 $|\Theta_0(u)|\le Cu^5e^{-u}$，于是 $|f_0|\le Cu^{21/4}e^{-u}$。因 $u=U+s$、$s\ge s_{R,k}>-2\pi$ 且 $U\ge1$，可用 $u^{21/4}\le C U^{21/4}(1+s_+)^{21/4}$，得到式 (26)。乘以 $|1-\chi_k|\le1$ 给同一正尾界；对称 cutoff 以及各 $\widetilde f_{j,k}$ 的奇性给负尾反射界。

## 范围边界

由投影定义得到的是每个 growing trial vector 的**精确旧空间正交**。它不提供 $\|v_{P,k}\|_2$ 的增长界，也不提供 growing-dimensional exterior-tail fraction、restricted Green inverse 的界、$Q_k$-restricted Schur 符号或其正性。稿件明确不作这些声称，故本 PASS 不应延伸解释为 full old-space Schur 结论。

## 便于独立复核的微小补充

正式稿已给出 Jacobi 恒等式的 DLMF 来源、原核的精确归一化及偶性推导；新增段落也已通过复核。式 (23) 到 (24) 的幂次可将最坏情形明写为：theta 误差的 $u^{2(d+m)+8}$ 与 $a_\ell$ 的 $U^{m-1-2(d+\ell)}$ 最多留下 $U^{3m+O_d(1)}$，而现有 $O_d(m\log U)$ 记号足以覆盖它。此处不存在指数预算缺口。
