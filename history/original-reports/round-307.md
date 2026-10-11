## Round 307 — The finite-spectral coefficient leaves a growing slack

对 Part 3 Theorem 5.6 的上界系数作直接代数核验。该定理使用
c_T = (π/T)coth(π/(2T))，e_T = π/(T−1)，A_T = c_T+e_T。
对 z>0 有 tanh(z)<z，故 coth(z)>1/z，从而 c_T>2；而 T≥10^7
时 e_T>0。因此在允许的 T 区间内始终有 A_T−2>0。

定理所用 prefix envelope 是 U_T(u)=A_T√u−α+d_T；正文明确保留的
finite-spectral slack 是 D_{T,x}=d_T+(A_T−2)√x。由于 T 的允许
上限 H* 是固定有限值，单靠这组有限谱上界时，A_T−2 在允许区间上
有正下界，故该 slack 随 x→∞ 增长；它不能单独推出所有未来事件的
J_q≤C_q。取与状态 cap 的最小值仍只是一个有效的有限事件上界，
并未证明全称式 J-hat_pin≤C_q；原文第 23 页明确写着 “No proof
of (93) is given”。
