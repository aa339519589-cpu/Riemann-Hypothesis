## Round 324 — Semilocal spectral descent claim: missing spectral limit

核验工作区文件 `work/semilocal-claimed-proof.pdf`，题为 “A Proof of the
Riemann Hypothesis for the Riemann Zeta Function — Weil Positivity via
Semilocal Spectral Descent”，Christian Franchi Viceré，2026-04-12，6 页，
SHA-256 `f2624e1a23c058595ae28e823f226f8a5fe815aa9f4ed4ffd1e78fbd3d2a3b34`。
稿件声称：有限半局部算子的谱实性与正性，经 \(N\to\infty\)、
\(\lambda\to\infty\) 以及场的极限，得到全局 Weil 正性。

该声称没有闭合，理由是：

1. 稿件把 Connes–Consani–Moscovici 的有限秩算子结果当成了有限半局部
   “谱实性”定理的充分依据；但原论文 arXiv:2511.22755 的摘要只报告
   有限算子的数值谱收敛，并明确指出对该收敛的严格证明本身将推出 RH。
   这不能被当作已经完成的 \(N\to\infty\) 定理。
2. Theorem 1 的有限矩阵在减去最小特征值 \(\epsilon_N\) 后可得到一个
   有限自伴对象；其谱零点是截断、平移后的半局部对象。稿件没有证明
   它们在极限中与全局 \(\Xi\) 的零点及重数逐一对应。
3. Theorem 3 对固定紧支撑测试函数至多说明有限算术场项的稳定性；它
   没有证明内层 \(N\to\infty\) 极限存在，也没有证明相应算子、行列式或
   谱测度的极限。对固定有限素数集使用支配收敛不能替代随后
   \(S\to\) all primes 的统一控制。
4. 稿件显示的三重极限
   \[
   Q_W=\lim_{S\to\mathrm{all}}\left\{\lim_{\lambda\to\infty}
   \left[\lim_{N\to\infty}Q^N_{W,\lambda}\right]\right\}\ge 0
   \]
   没有给出内层极限存在、正性在变化的形式/算子下保持、各局部归一化
   一致，或极限次序可交换的证明。
5. Theorem 4 直接把 Weil 显式公式的场求和收敛写成结论，不能补上
   上述谱识别和极限缺口；Theorem 5 的密度与连续性也只能在前述全局
   Weil 二次型已被建立后使用。四个测试函数与有限 \(S,N,\lambda\) 的
   数值表不改变这些全称解析命题的状态。

因此，这份文件没有产生新的无条件 RH 证明定理；其关键承重步骤仍是
有限对象到全局 \(\Xi\) 的严格谱极限与 Weil 正性传递，尚未证明。

来源：稿件引用的原始论文 https://arxiv.org/abs/2511.22755。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
