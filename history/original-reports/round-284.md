## Round 284 — Velez v5 cites the wrong Hilbert-space object for the needed Gram identity

进一步对照 Velez v5 与其引用的 Alain Connes,
\emph{Trace formula in noncommutative geometry and the zeros of the Riemann
zeta function}, Section VII（公开 PDF SHA-256
\`eed4e94271e66052ea0e695287be297fd59be745277a6b4e4fef3c98df35995a\`）。

Connes Section VII Theorem 4 的定义对象是
\[
X_S=\mathbb A_S/\mathcal O_S^\times,\qquad
L^2(X_S),
\]
并对作用在 \(L^2(X_S)\) 上的 cutoff 算子
\[
R_\Lambda=P_\Lambda\widehat P_\Lambda
\]
给出 \(\operatorname{Tr}(R_\Lambda U(h))\) 的 cutoff 极限和各局部主值项。
该定理不是一个关于任意 \(F,G\) 的 Gram 分解定理，也没有在其结论中给出
Velez 所需的向量 \(\eta_X\)。

Velez Proposition 6.1 却写成
\[
C_X=J_{S_X}/\mathcal O_{S_X}^\times,\qquad
\mathcal H_X=L^2(C_X,d^\times u)\ominus\mathcal H_X^{0,1},
\qquad
\Phi_X(F)=U_X(g_F)\eta_X.
\]
这里 \(C_S\) 是 \(S\)-idele class group，而 Connes Theorem 4 使用的是
idele 的加法商空间 \(X_S\)；二者不是同一个测度空间或同一个表示空间。
论文没有给出从 Connes 的 \(L^2(X_S)\)、\(R_\Lambda\) 及其 trace 极限到所写
\(L^2(C_X)\) Gram 内积的同构、压缩或正性推导。它也没有证明所谓
\(\mathcal H_X^{0,1}\) 是该 \(L^2(C_X)\) 中可取正交补的闭二维子空间。

因此，Appendix D 直接声称把 Connes 的 semilocal expansion 应用于
\(h_{F,G}\) 就得到式 (D.1)，在当前定义下缺少一个关键的空间/算子识别定理；
这是 Proposition 6.1 的独立承重缺口，而不是有限截断恒等式。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
