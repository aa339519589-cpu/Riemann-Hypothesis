## Round 319 — Angular-monotonicity GRH candidate audit

核验对象：Zenodo 22137644（2026-08-28），标题为 “Proof of the
Generalized Riemann Hypothesis via Angular Monotonicity of the Completed
L-function”。正文、TeX、推导稿与作者附带的复核报告均已取得。
来源：https://zenodo.org/records/22137644。主要文件 SHA-256：

- `grh_angular_monotonicity.tex`：
  `f96372b226cce6a30ef511c14fa15ae8222ca144453bfeb13598d83e8f6a630a`；
- `grh_new_approach_draft.md`：
  `2b69fadcd290b5e1d78670d8b4208744c704f4024a1c8d2b59a1229307dac248`；
- `grh_K_derivation.md`：
  `9dd0cccc39da4f39cdfcfea69d61a8652d37c683441a4f73b21e92e0b98c5685`；
- `grh_review_report.md`：
  `a320d59335db48435247c5d2f50be00853ef84a4c6df2189af7290a385ff5eaa`。

承重断点如下：

1. 正文把 \(g_K'(r)\) 的下界写成带固定常数 \(K\) 的公式，但没有从
   零密度估计和 Riemann–von Mangoldt 余项给出完整显式推导。附带推导稿
   自己明确写出：离临界线零点的贡献无法按所需大小控制，\(K=0.5\)
   当前不可严格建立；取 \(K=1.0\) 仍需要尚未完成的常数定量化。
2. 正文的 Region 3 需要处理 \(L(1/2,\chi)=0\) 的情形。它承认
   \(L(1/2,\chi)\ne0\) 是未解决的 Chowla 猜想，却随后只给出形式性的
   Taylor/Cauchy 余项叙述和“直接数值网格”方案；没有给出覆盖整个区域的
   可独立复核的解析不等式。作者的复核报告也将这一点列为必须修正/补充。
3. 所谓“verified interval arithmetic”在 TeX 中只是计算计划和方法描述，
   并未随记录提供覆盖全域的区间证书及其可复核实现；有限网格或有限精度
   成功本身不可能推出对所有 \(r,\theta\) 的角单调性。
4. 即便暂时接受角单调性，最终由角单调性排除离线零点的推导还需要先
   严格证明该全称角单调性定理；因此不能用结论段的“Combining all three
   ranges”替代缺失的各区域证明。
5. 作者复核报告明确列出一个重大公式错误：\(g_\Lambda\) 的推导漏掉
   \(\tfrac12\log(qr/(2\pi))\) 主项；同时把 \(K=0.5\) 作为可用值的说法
   与其自己的推导相矛盾。报告结论是仍需修正和补充，而非已完成证明。

因此该候选没有给出 RH（更不用说 GRH）的完整、无条件、非循环证明，
也没有给出 RH 的无条件否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
