## Round 291 — Chen's newest angular-monotonicity manuscript has a sign error and an unproved off-line zero bound

审计对象：Zhuo Chen, *Proof of the Generalized Riemann Hypothesis via Angular
Monotonicity of the Completed L-function*, Zenodo DOI
``10.5281/zenodo.22137644``，2026-08-28。该记录的文件包括正文
``grh_angular_monotonicity.pdf``（下载 SHA-256
``fca8c5a6d0675021783a99a9cc3d13708de1a9fefe3f36cd0cfed40edb17aa1f``）
和 TeX 源（SHA-256
``f96372b226cce6a30ef511c14fa15ae8222ca144453bfeb13598d83e8f6a630a``）。

正文试图用 \(\xi_K=\xi\Lambda\) 的角单调性推出 GRH，进而也会覆盖其
\(\xi\) 因子中的 RH。Appendix 的 Hadamard 计算写成：若
\(\rho_K=\tfrac12+\delta+i\gamma\)、\(s=\tfrac12+ir\)，则
\[
g_K'(r)=-\Re\sum_{ρ_K}\frac1{(\delta+i(γ-r))^2}
 =\sum_{ρ_K}\frac{δ^2-(γ-r)^2}
 {(δ^2+(γ-r)^2)^2}.
\]
但直接计算给出
\[
-\Re\frac1{(δ+iΔ)^2}
 =\frac{Δ^2-δ^2}{(δ^2+Δ^2)^2},
\qquad Δ=γ-r,
\]
即 displayed equality 的分子符号相反。正确式在 \(δ=0\) 时给出
\(1/(γ-r)^2>0\)，这才与正文随后声称的“临界线零点贡献为正”一致；
当前稿同一附录的公式和文字因此不能同时成立。

更根本的缺口在于，稿件从 Riemann--von Mangoldt 的纵向计数公式直接声称
\[
g_K'(r)\ge
\frac{\log^2(r/2\pi)+\log^2(qr/2\pi)}{4\pi^2}
-K\log(qr).
\]
然而每个零点对该导数的贡献依赖横向偏移 δ，而
\(N_Λ(T)\) 只给出按 γ 计数。一个满足函数方程对称的非临界成对位置
\(ρ_±=\tfrac12±δ+ir\) 在 \(r) 处的合计贡献是
\[
2\frac{0^2-δ^2}{(δ^2+0^2)^2}=-\frac2{δ^2},
\]
并可随 δ\to0^+ 变得任意负。因而“纵向零点密度产生正的
\(\log^2 r\) 主项”不自动给出一个只损失 \(O(\log r)\) 的下界；必须提供
对横向位置、近临界线零点和该奇异核的完整显式积分估计。稿件只列出
“Ingham--Huxley 型 zero-density estimates”，没有给出这一步的定理、积分、
常数或适用范围。

稿件的常数叙述还有内部不一致：Appendix 先把 (L) 部分的 Riemann--von
Mangoldt 余项写成 \(K_{Λ,\mathrm{main}}\approx0.49\)，随后又承认离临界线
零点还需额外 \(K_{Λ,\mathrm{offline}}\lesssim0.3\)；但实际用于
\(g_Λ'\) 的 displayed bound 仍只减去 \(0.49\log(qr)\)，没有说明额外项
已被吸收。于是文中在 \(r=10^6\) 得到的“\(g_Λ'>0\)”不是由已写出的
估计推出的。公开记录列出的文件也没有附录所声称的三个完整区间验证脚本，
只有正文、TeX、JSON 和复核草稿，故有限网格声明不能填补解析缺口。

所以该稿的角单调性主定理及其 GRH/RH 蕴含仍未被无条件证明。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
