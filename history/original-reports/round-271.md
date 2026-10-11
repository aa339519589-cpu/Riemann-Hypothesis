## Round 271 — Chua v5: Nicolas-criterion halving induction is not established

审计对象：Cheong Siong Chua, *Nicolas Criterion and Riemann Hypothesis*, 2026-06-22, Zenodo record 20790544，PDF SHA-256
\`4e2b6e8dab8eed4f031310a065bd800cf47ccff11b62b529a0dfc9a220b92c53\`。

稿件的目标是用 Nicolas 的第二判据证明：对充分大的素数阶乘 \(N_k\)，令
\[
G_k=\frac{N_k}{\phi(N_k)},\qquad
R_k=e^\gamma\log\log N_k+e^\gamma(2+\beta)\sqrt{\log N_k},
\]
若某个 \(k\) 满足 \(G_k>R_k\)，则应推出
\[
G_{\lfloor k/2\rfloor}>R_{\lfloor k/2\rfloor}.
\]
随后稿件声称反复取 \(\lfloor k/2\rfloor\) 会把一个大指标的违例传到有限检查范围，从而得到矛盾。

独立检查显示，Nicolas 判据本身只给出：若 RH 为假，则存在无穷多个（充分大的）指标 \(k\) 发生违例；它不自动给出“每一个违例都能传递到 \(\lfloor k/2\rfloor\)”这一性质。稿件的 Lemma 1--3 只提供若干带 \(O(e^{-c\sqrt{\log P_k}})\) 误差的乘积和对数比渐近式。要从这些式子推出严格的违例传递，必须额外证明一个带明确符号和余量的估计，例如把
\[
G_k-R_k>0
\]
转换成对 \(G_{\lfloor k/2\rfloor}-R_{\lfloor k/2\rfloor}\) 的严格正下界，并证明所有渐近误差都被该余量吸收。稿件没有给出这种估计；其 Lemma 4 直接把含 \(O(\cdot)\) 的渐近比较提升为严格不等式，且没有控制违例量可能任意接近零的情形。

因此，末页“由一个大 \(k\) 的违例按归纳必然降到 \(k<k_0\)”的结论没有逻辑依据。有限范围的数值检查也不能补上这个无限指标上的严格传递缺口。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
