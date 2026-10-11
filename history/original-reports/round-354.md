## Round 354 — Connes 的渐近截断公式不能推出 Velez 的有限截断 Gram 等式

把 Velez Proposition 6.1 与其引用的 Connes [3, §VII, Theorem 4]
逐项对照。Connes 的定理对截断参数 \(\Lambda\to\infty\) 给出的是
\[
 \operatorname{Trace}(R_\Lambda U(h))
 =2h(1)\log'\Lambda
   +\sum_{v\in S}\int'_{k_v^\times}\frac{h(u^{-1})}{|1-u|}\,d^\times u
   +o(1),
\]
其中 \(R_\Lambda=\widehat P_\Lambda P_\Lambda\)，并非对某个有限
\(X\) 的精确等式。Connes 在同一节的全局情形还明确把相应公式写成
“natural to expect”，而不是已经证明的定理。

Velez 在 Proposition 6.1 / Appendix D 中却声称：对固定的支持耗尽
\(X\)，令
\[
 H_X=L^2(C_X,d^\times u)\ominus H_X^{0,1},\qquad
 \Phi_X(F)=U_X(g_F)\eta_X,
\]
即可得到没有误差项的
\[
 \langle\Phi_X(F),\Phi_X(G)\rangle
 =P_{\rm pole}(h_{F,G})-W_\infty(h_{F,G})
 -2\sum_{p^k\le X}\log(p)p^{-k/2}C_{F,G}(k\log p).
\]
从引用的公式到这一步至少缺少四项独立证明：

1. 从 \(L^2(C_X)\) 中的对象到函数 \(g_F\) 的明确等距嵌入；
2. 所谓 cutoff-renormalized vacuum vector \(\eta_X\) 的存在、定义域和有限范数；
3. 极限参数 \(\Lambda\) 与有限参数 \(X\) 的对应关系；
4. Connes 公式中的 \(o(1)\) 为零，或其误差在 pole projection 后精确抵消的证明。

这些不是记号整理：若第 4 项成立，正是需要证明的全局 Weil 正性信息；若不成立，
则不能把半局部 trace asymptotic 当作 \(q_X\) 的 Gram 分解。因此 Proposition 6.1
的证明没有闭合，依赖它的 Theorem 7.1 和 Theorem 8.1 不能作为 RH 证明。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
