## Round 276 — SAM canonical record: the installed Theta completion is sign-independent

审计对象：SAM Research Project, *RH Work to Date -- Version 1*,
2026-08-15，公开记录：
https://github.com/iwtbotiwtwot/riemann-hypothesis-program/blob/main/RH_WORK_TO_DATE_V1_2026-08-15.md
，下载文本 SHA-256
\`66a40caaa82b57487620054e0bd591358b8a1187ab05696a139c87e1d9ae6606\`。
该记录也是本任务所附 canonical project record 的公开副本。

记录的“Current public posture”明确写出
\[
\texttt{program state = PROOF\_CLAIM\_SUBMISSION},\qquad
\texttt{external validation = NONE\_RECORDED}.
\]
它列出的目标闭合式是
\[
Q_\xi(h)=\left\|(I-\Pi_{\rm common})\mathcal W_{\rm dir}h\right\|^2,
\]
但该记录没有把这个式子作为已经完成的外部可核验定理；完整定义、域、收敛和蕴含仍被留在未独立验证的 proof-claim manuscript 中。

更直接地，记录第 21--23 节的 Phase E 审计给出了当前完成谓词的精确反例族。对每个正有理数 \(\varepsilon\)，
\[
G_\varepsilon=\operatorname{diag}(\varepsilon,-\varepsilon),
\qquad
H_\varepsilon=\frac14J G_\varepsilon J^{\mathsf T}
\]
通过已安装的对称、receipt、delivery、payload 和 AFC2 交集检查，同时
\[
\operatorname{inertia}(G_\varepsilon)=(1,1,0),
\qquad
\operatorname{inertia}(H_\varepsilon)=(1,1,2).
\]
因此这些信息保留了负惯性；它们没有强制 \(G_{\rm Weil}\) 为正，也没有推出
\[
G_{\rm Weil}=J^{\mathsf T}H_\Theta J
\]
这一仍被记录为待问的正 Gram/incidence 恒等式。正交、对称和信息交付条件本身不能替代正权或正性定理。

所以该 canonical record 记录的是一个公开的 RH proof claim 及其明确的未闭合接口；它不包含无条件 RH 证明。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
