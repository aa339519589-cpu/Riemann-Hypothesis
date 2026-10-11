## Round 333 — New vorton–FUP poster does not establish the scattering transfer

核验 Mikhail I. Aksman 的 “THE SPECTRAL RESOLUTION OF THE RIEMANN
HYPOTHESIS: Automorphic Scattering, Fractal Uncertainty, and Coercive Vorton
Geometry”，Zenodo record 22136739，https://zenodo.org/records/22136739，
文件 `rh_spectral_fup_v2.pdf`。文件 MD5 为
7ee979585aaa8c98dcc9a916638e5df2，SHA-256 为
00b82f337220402be1a9e1d08780357fdf0b8138d04fc948328ad2afb8258542。

稿件把结论依次建立在 Lemma 2.1、Lemma 3.2、Theorem 3.3 和
Theorem 4.2--4.3 上，但这些承重环节没有由定义推出：

1. 若 \(K_a\) 是正半径的有限核心管状邻域，则它含有开集，在尺度
   \(r<a\) 时不可能在每个点的每个球内都找到与 \(K_a\) 不相交的固定比例
   空球；若把式 (1) 的全空间正尾部也算进拓扑支持，则支持反而不再是所需
   的低维孔隙集。故 Lemma 3.2 的“对所有 \(r\in[h,h_0]\)、对所有
   \(a<a_0\) 统一孔隙性”没有成立的定义基础。Ahlfors--David 测度估计本身
   也不能替代这一全尺度空球结论。
2. 式 (3) 的交换子含有 \(\Delta\varphi_a\) 与
   \(\nabla\varphi_a\) 项。仅由物理空间的代数尾部或傅里叶变换的指数衰减，
   不能推出在未给出频率截断、符号估计和算子域的情况下
   \(\|[P,\varphi_a]\|_{H^m\to H^{m-1}}\le Ce^{-a/h}\)。稿件没有完成
   这个全局算子范数估计。
3. Theorem 3.3 只能在已证明的统一 \(\delta\)-正则/孔隙假设下调用 FUP；
   即使得到某个 \(h^{\beta}\) 衰减，也没有给出从传播估计到
   \(\|(P_a-s(1-s))^{-1}\|\le C\log|\Im s|\) 对所有 \(\Re s>1/4\) 的
   参数、时间和域估计。Proposition 4.1 实际上直接把所需的
   resonance-free half-plane 写成结论。
4. Theorem 4.2 把强 resolvent 收敛归因于 Phragmén--Lindelöf 原理，但
   Phragmén--Lindelöf 的复函数增长估计不等于自伴算子族的强 resolvent
   收敛；也没有证明共振/极点在 \(a\to0\) 时按所需方式一致收敛。因而
   Theorem 4.3 的“无正则化共振”结论仍未证明。

式 (8) 的散射矩阵恒等式至多说明：若存在 \(\xi(\rho)=0\) 且
\(\Re\rho>1/2\)，则相应分母会在 \(\Re s>1/4\) 产生极点。要由此得到 RH，
必须先无条件证明该整半平面的共振空缺；稿件没有做到这一点。附录中
\(X_0(163)\) 的有限点数值检验不能补上全局解析传递。

因此，这份新海报没有给出从模曲面定义到 zeta 零点全称定位的无条件证明，
也没有给出 RH 的无条件否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
