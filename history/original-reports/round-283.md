## Round 283 — Velez Version 5 still assumes the load-bearing semilocal norm identity

审计对象：Simón Vélez, *A proof of the Riemann Hypothesis*, Zenodo
Version v5, DOI \`10.5281/zenodo.21184595\`，PDF SHA-256
\`76d29c31739b58bb781b687d3f93c032f217f3ca00207bb8765b7882cd2deece\`。

Section 5 的确给出一个有限支撑下的代数事实：若
\(\operatorname{supp} C_{F,G}\subset[-R,R]\) 且 \(X>e^R\)，则
\[
q_X(F,G)=\langle L_{\rm arith},C_{F,G}\rangle.
\]
这只说明有限 prime-power 截断在支撑耗尽后等于定义的算术二次型；没有产生
正性。

正性完全依赖 Proposition 6.1。其证明先定义
\[
\mathcal H_X=L^2(C_X,d^\times u)\ominus\mathcal H_X^{0,1},
\qquad
\Phi_X(F)=U_X(g_F)\eta_X,
\]
其中 \(\eta_X\) 被描述为“cutoff-renormalized completed vacuum vector”，
据称由外部文献中的局部 basic vector 经过 infrared/ultraviolet cutoff 和
pole projection 得到。论文没有给出这个向量的具体定义、存在性、归一化、
收敛方式、所属域或 pole projection 的闭性/正交性证明。随后只写道把
semilocal expansion 应用于 \(h_{F,G}\) “gives”：
\[
\langle\Phi_X(F),\Phi_X(G)\rangle_{\mathcal H_X}
=P_{\rm pole}(h_{F,G})-W_\infty(h_{F,G})
-2\sum_{(p,k)\in\mathcal P_X}
\log p\,p^{-k/2}C_{F,G}(k\log p),
\]
即所需的
\(\langle\Phi_X(F),\Phi_X(G)\rangle=q_X(F,G)\)。

这个等式不是由前面已写出的定义推出的中间计算：必须先建立同一个
\(\mathcal H_X\) 中的 renormalized vector，证明 pole compression 的实际
内积，逐项得到 \(p^{-k/2}\) 的 prime-power 系数，并证明所有 cutoff/finite
part 极限和无剩余项。Section 6 没有这些推导；Appendix D 只是再次把同一
等式 (D.1) 作为“normalized semilocal expansion”后的结论。故
Proposition 6.1 仍是把目标正性写成范数的未证明断言，不能推出 Theorem 7.1
或 RH。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
