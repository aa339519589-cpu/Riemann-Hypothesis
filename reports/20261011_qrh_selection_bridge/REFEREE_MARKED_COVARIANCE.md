# 双标记协方差与固定 slot 完整零模：独立数学审核

## 判定

通过[《LCM covariance and the full marked resonance block》](MARKED_COVARIANCE.md)的(1)–(7)。不同标记的实际完整行、任意不同正尺度 U_D 和可选同一真实 Gauss 平方权均保留。结论为完整周期/扩张圆盘 Gram，不是原短窗口全部 Poisson 频率估计。

## 双标记局部代价

同核心 (c,v) 正交后，将 L=lcm(D,D′) 分入 c、v\c、其余 k 部分。落入 c、v 的交叉代价分别为 p⁻¹、p⁻²。其余部分若 p 同时属于两标记，则两侧 k 都需含 p，代价 p⁻⁴；若仅属于一个标记，则只一侧有此要求，代价 p⁻²。

混合尺度的余和是两个此前 S(V) 向量的 Hilbert 内积，Cauchy 与全正尺度统一界给同一固定常数，不要求 U、V 可比。全部非零交叉的原 mask 平均≤φ(L)/q_L；Gauss 正权亦由已证的准确局部式保持该界。

因此共同标记素数的余 Euler 因子≤1，单侧素数为 1+p⁻¹−2p⁻²。式(1)准确。对每边最多 K 个素因子的标记，余积可吸入 C_K；不能无条件声称独立于无限增长的 K。

## 完整固定 slot Schur

每个 D 必须在同一组固定、两两不交的 slot 中各选一个素数。如此，归一核 sqrt(q_Dq_D′)/q_lcm 的每行和才准确分解为式(5)。每 slot 的不同素数贡献 1/sqrt(q_pq_p′)；q_p≈P_i 与 ideal count O(P_i) 给固定统一 row-sum 常数，不需 PNT 或窗口素数下界。

Gram 为 Hermitian，故 row/column Schur 常数相同。V_D=√q_D B_D；原线性组合的系数相应为 z_D/√q_D。因此最终右侧恰为 C_slotsΣ|z_D|²/q_D，归一正确，没有丢失或多加 q_D。对有界乘积 slot 权，进一步的(7)同样正确。

这些式子联合控制同一 sextic 核内部的不同(E,F,c₀,n₀)贡献，没有将其伪称正交。但完整零模不等于短行；所有非零 Poisson 频率仍需独立估计。
