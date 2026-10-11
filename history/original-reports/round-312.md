## Round 312 — Part 3 v3 reproducibility contract keeps G1 open

对 Part 3 v3 配套 ZIP 作进一步核验。ZIP SHA-256 为
430d206c76d90fbc88a6d18ed4ee8603aeacadd9c7b999f136a2dc9ce218ee10。
README 明确把 Part-3 all-active inequality 列为 open，并说明有限谱构造
与诊断程序都不证明 infinite tail。contracts/PROOF_OBLIGATION_LEDGER.json
将 G1 的 current_status 设为 open，且所需的 J-hat≤C_q 仅是 preferred
sufficient interface；verification/focused_g1_audit.json 仍将
rh_proved=false、infinite_tail_proved=false。

该合同文件与正文的状态一致：精确恒等式、有限证书和浮点审计均没有
把 G1 的全称上界升级为已证定理。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
