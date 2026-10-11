## Round 278 — SAM public verifier validates finite custody, not the infinite Weil form

审计对象：公开 bundle
\`RHP-EXPORT-20260815-0008/verify.py\`，原始文件：
\`https://raw.githubusercontent.com/iwtbotiwtwot/riemann-hypothesis-program/main/artifacts/slcv20r_weil_inertia/RHP-EXPORT-20260815-0008/verify.py\`，
文件 SHA-256
\`dd61d122c5a031fe7c06832732e5789093ce13493753c8d20cb2f8cecbc1bd39\`。

逐行核对可见，验证器的工作范围是有限、离散且已冻结的数据：

1. 读取 Phase A--E 的 JSON 结果，核对状态、语义哈希、内部 artifact
   seal、控制计数和归属文本；
2. 在四个有理数
   \(\varepsilon\in\{1,\tfrac12,\tfrac1{10},\tfrac1{1024}\}\)
   上构造
   \[
   G_\varepsilon=\operatorname{diag}(\varepsilon,-\varepsilon),\qquad
   H_\varepsilon=\tfrac14JG_\varepsilon J^{\mathsf T},
   \]
   并检查有限矩阵恒等式
   \(J^{\mathsf T}H_\varepsilon J=G_\varepsilon\)、有限方向的二次型、
   对称核和反对称限制；
3. 核对 Phase E 的冻结状态为 \`STOPPED_AT_PHASE_E\`，且
   \`phase_f_open=false\`，然后输出有限检查全部通过的 PASS 消息。

代码没有定义 \(\mathcal H_{\rm write}\) 的全域内积或完备化，没有定义任意
\(h\) 的 \(\mathcal W_{\rm dir}h\)，没有定义全域
\(\Pi_{\rm common}\)，没有证明
\[
Q_\xi(h)=
\left\|(I-\Pi_{\rm common})\mathcal W_{\rm dir}h\right\|^2,
\]
也没有证明有限矩阵族收敛到该 \(Q_\xi\)、交换极限与无限素数/整数求和，
或得到全域 Weil 正性。相反，同一验证器明确执行的
\(G_\varepsilon\) 族具有
\[
\operatorname{inertia}(G_\varepsilon)=(1,1,0),\qquad
\operatorname{inertia}(H_\varepsilon)=(1,1,2),
\]
所以所核对的有限数据本身保留负惯性；通过这些检查不可能推出无限维正性。

结论：\`124/124\`（以及各 Phase 的冻结计数）是数据完整性和有限代数检查，
不是 \(Q_\xi\ge0\) 的全域证明，更不是 RH 的证明或否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
