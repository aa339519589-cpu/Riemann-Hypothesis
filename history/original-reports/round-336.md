## Round 336 — PIHR X proves only an Abel-smoothed boundary statement

核验 Borros Arneth 的 “Boundary-Transform Factorization, Uniform Jordan
Pole-Zero Coalescence, and a Proof-of-Concept Closure Architecture for the
Riemann Hypothesis”，Zenodo record 22130541，
https://zenodo.org/records/22130541，文件 `PIHR-RH-X.pdf`。文件 MD5 为
fea188559a5d6b511717c5beed8524ea，SHA-256 为
0b5a0b4f293e753d3a91ba7d9ba3913fddbb4d5a6c5db7a81a40d945321fe43d。

Theorem 1 对固定 \(\lambda>0\)、\(\operatorname{Re}w>\lambda\) 给出缩放
Laplace 变换的渐近因子化
\[
\widehat P_{\lambda/s}(w/s)-\widehat{\mathcal R}_{\lambda/s}(w/s)
\longrightarrow
\lambda\left(\frac{B_\infty}{w}+\frac{\kappa}{w-\lambda}\right),
\]
且右端在实轴上为正。Theorem 3 由此只得到固定参数、足够大 \(s\) 时的
Abel-smoothed 积分为正。第 15 节明确指出，这个变换正性不等价于
\(P_{\lambda/s}(s)\ge\mathcal R_{\lambda/s}(s)\) 的点态不等式；不能把
正的 Laplace 变换直接逆推出未平滑的算术正性。

真正把变换结果推广到点态全临界带的 Candidate Lemma 4（式 (71)）在第
16 节明确写为 “has not been proved”。Conditional Theorems 6--8、
Candidate Theorem 9 都以它为前提；Candidate Lemma 10 还另外要求从
production dominance 到完整 passivity sandwich 的常数不损失传递。最终
Theorem 11 更直接地把这三个未闭合陈述作为假设，并在第 29 节明确称其为
conditional proof architecture。正文结论也明确写出 RH remains unproved。

因此，PIHR X 的无条件部分只是变换域边界层的局部辅助结果，未形成对所有
尺度的点态正性，更没有完成 RH 的无条件证明或否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
