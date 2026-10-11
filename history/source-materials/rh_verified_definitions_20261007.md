已完成源码层面的只读核验。**两个根条件仍是消费者的显式前提；最终 RH 接口还要求全部内部小行列式正性。**以下定义、量词和行号来自现存文件，本次未运行构建或内核审计。

源码目录：

```text
/Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal
```

下面所有自然数指标均允许取 `0`，另有不等式限制时除外；所有积分使用 Lebesgue 测度。

**实际无限核、累计流与 hazard。**令

\[
\begin{aligned}
G_0(t)&=\sum_{m=1}^{\infty}m^2e^{5t-\pi m^2e^{4t}},\\
\Phi(t)&=\sum_{m=1}^{\infty}
(2\pi^2m^4e^{9t}-3\pi m^2e^{5t})e^{-\pi m^2e^{4t}},\\
G_{k+1}(t)&=\int_t^\infty G_k(u)\,du,\\
C_k(t)&=G_k(t)-G_{k+1}(t),\\
H_k(t)&=\frac{C_k(t)}{C_{k+1}(t)}.
\end{aligned}
\]

源码给出 \(C_k(t)>0\)（\(t\ge0\)）及
\(C'_{k+1}(t)=-C_k(t)\)。这里包括全部无限 theta 模态。

对应位置：[ThetaOperator.lean（17、23 行）](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ThetaOperator.lean:17>)、[ActualRiemannKernel.lean（32、361、501 行）](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ActualRiemannKernel.lean:501>)、[ActualCumulativeZeroCrossingFlow.lean（25、29、46 行）](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ActualCumulativeZeroCrossingFlow.lean:25>)、[ActualCumulativeRootIntegral.lean（29 行）](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ActualCumulativeRootIntegral.lean:29>)。

**同一个实际行列式及根处多项式。**固定 \(q\in\mathbb N\)，定义

\[
\begin{aligned}
\mu_k^{q,t}&=C_{2(q+1+k)}(t),&
\nu_k^{q,t}&=C_{2(q+k)+1}(t),\\
\Delta_{q,r}(t)&=\det[\mu_{i+j}^{q,t}]_{0\le i,j<r},&
\varepsilon_r&=(-1)^{\binom r2},\\
F_{q,r}(t)&=\varepsilon_r\Delta_{q,r}(t).
\end{aligned}
\]

因此 \(F_{q,r}\) 对应代码
`actualEvenSignedCumulativeDifferenceDet (q + 1) r`，且 \(F_{q,0}=1\)。

令 \(p=p_{q,n,t}\) 为源码的 `formalOrthogonalPolynomial`。当
\(\Delta_{q,n}(t)\ne0\) 时，其自包含定义为

\[
p(X)=\frac{(-1)^n}{\Delta_{q,n}(t)}
\det\begin{pmatrix}
1&X&\cdots&X^n\\
\mu_0&\mu_1&\cdots&\mu_n\\
\vdots&\vdots&&\vdots\\
\mu_{n-1}&\mu_n&\cdots&\mu_{2n-1}
\end{pmatrix}.
\]

此时它是首一的 \(n\) 次多项式。源码采用全定义的除法；若下阶行列式为零，该多项式为零，不能仍称其首一。

若 \(p(X)=\sum_i p_iX^i\)，定义

\[
K_p(x)=\sum_{i,j=0}^{n}
p_ip_j\frac{x^{2(i+j)}}{(2(i+j))!}.
\]

对应位置：[根处矩序列（307、312 行）](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ActualCumulativeRootQuadraticForm.lean:307>)、[形式正交多项式（34、228 行）](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/FormalOrthogonalPolynomial.lean:228>)、[阶乘二次核（325 行）](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ActualCumulativeRootIntegral.lean:325>)；矩阵定义在 `ActualCumulativeZeroCrossingFlow.lean:53`，符号定义在 `FixedPointPropagation.lean:19`。

**两个准确的根条件。**记

\[
J_{q,n}(t;c)=(-1)^n\int_0^\infty
K_{p_{q,n,t}}(x)
\bigl(H_{2q}(t+x)-c\bigr)C_{2q+1}(t+x)\,dx.
\]

`ActualEvenCenteredHazardRootCondition q` 正是

\[
\boxed{\forall n\in\mathbb N\;\forall t\in\mathbb R,\quad
t\ge0\ \land\ F_{q,n+1}(t)=0
\ \Longrightarrow\
J_{q,n}\bigl(t;H_{2q}(t)\bigr)\ge0.}
\]

中心固定为 \(H_{2q}(t)\)。矩阵起点为 \(q+1\)，hazard 下标为 \(2q\)，密度下标为 \(2q+1\)。定义见 [ActualCumulativeRootClosure.lean:144](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ActualCumulativeRootClosure.lean:144>)。

`ActualEvenFlatRootSecondDerivativeCondition q` 正是

\[
\boxed{\forall n\in\mathbb N\;\forall t\in\mathbb R,\quad
t\ge0,\ F_{q,n+1}(t)=0,\ F'_{q,n+1}(t)=0
\ \Longrightarrow\
F''_{q,n+1}(t)<0.}
\]

这里是同一个 \(F\) 对实变量 \(t\) 的通常导数，条件包含 \(t=0\)。定义见 [同文件:159](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ActualCumulativeRootClosure.lean:159>)。

这两个定义**均没有额外的下阶非零前提**。但源码中的根处恒等式另需
\(\Delta_{q,n}(t)\ne0\)、\(F_{q,n+1}(t)=0\)、\(t\ge0\)，才给出对任意 \(c\in\mathbb R\)：

\[
\int_0^\infty K_p(x)C_{2q+1}(t+x)\,dx=0,
\qquad
F'_{q,n+1}(t)=-F_{q,n}(t)J_{q,n}(t;c).
\]

归纳消费者用下阶严格正性提供非零前提。这些恒等式没有证明 \(J\) 的目标符号。对应定理在 [ActualCumulativeRootIntegral.lean（1086、1206 行）](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ActualCumulativeRootIntegral.lean:1206>)。

**根条件消费者的覆盖范围。**源码定理

`actualEvenSignedCumulativeDifferenceDet_all_order_pos_of_centeredHazardRootConditions`

的准确接口是：对每个固定 \(q\)，上述两个条件同时成立，则

\[
\forall r\in\mathbb N\;\forall t\in\mathbb R,\quad
t\ge0\Longrightarrow F_{q,r}(t)>0.
\]

见 [ActualCumulativeRootClosure.lean:171](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ActualCumulativeRootClosure.lean:171>)。所用高时间端点的量词是“每个固定起点、固定阶数存在阈值”，不是统一阈值；见 `ActualCumulativeHighTimeAsymptotic.lean:1948、2005`。

实际 Xi 系数为

\[
\beta_k=\frac1{(2k)!}\int_0^\infty x^{2k}\Phi(x)\,dx
       =\frac{\pi}{2}C_{2k}(0).
\]

令 \(\widetilde\beta_k=\beta_k\)（\(k\ge0\)），负指标取零，并定义

\[
D_\beta(N,r)=\det[\widetilde\beta_{N+j-i}]_{0\le i,j<r}.
\]

源码给出的准确转换为

\[
D_\beta(q+r,r)=\left(\frac\pi2\right)^rF_{q,r}(0),
\qquad q\ge0,\ r>0.
\]

因此，即使对所有 \(q\) 证明两个根条件，这个消费者也只直接覆盖 **\(N\ge r\)**；最终需要的 \(1\le N<r\) 仍须补齐。对应位置：`ActualRiemannBeta.lean:22、28、165`，`ContiguousToeplitzDuality.lean:30`，`FirstModeCumulativeMargin.lean:8993`，以及 [实际高起点消费者:228](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ActualCumulativeRootClosure.lean:228>)。

**最终 RH 消费者。**最直接的源码接口是

\[
\boxed{
\bigl[\forall N,r\in\mathbb N,\quad
N>0\land r>1\Longrightarrow D_\beta(N,r)>0\bigr]
\Longrightarrow\mathrm{RiemannHypothesis}.}
\]

定理名为 `riemannHypothesis_of_riemannXi_interior_minors_pos`，见 [ActualRiemannRootExtractionClosure.lean:67](</Users/REDACTED/Library/Mobile Documents/com~apple~CloudDocs/Documents/Codex/2026-08-28/it-is-forbidden-to-stop-for/formal/Formal/RHFormal/ActualRiemannRootExtractionClosure.lean:67>)。源码用
\(D_\beta(0,r)=\beta_0^r>0\) 和 \(D_\beta(N,1)=\beta_N>0\) 补齐边界；没有阶数上界或零点单重假设。

其最终零点链使用

\[
\begin{aligned}
E(z)&=\frac1{16}-\frac{1+z^2}{64}
\Lambda_0\!\left(\frac12+\frac{iz}{2}\right),\\
B(w)&=\sum_{k=0}^{\infty}\beta_kw^k
     =E(\sqrt{-w}),\qquad B(-z^2)=E(z),
\end{aligned}
\]

其中 \(\Lambda_0\) 是完成 zeta 的去极点整函数：
\(\Lambda(s)+1/s+1/(1-s)\) 的整延拓，
\(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\)。源码将全部小行列式正性接到

\[
\forall w\in\mathbb C,\quad
B(w)=0\Longrightarrow\Im w=0\land\Re w\le0,
\]

再接到 Mathlib 的准确目标

\[
\forall s\in\mathbb C,\quad
\zeta(s)=0,\ 
\neg\exists m\in\mathbb N:\ s=-2(m+1),\
s\ne1
\Longrightarrow\Re s=\tfrac12.
\]

对应位置：`ActualRiemannXiEndpoint.lean:28、66、76、220`，`ActualRiemannXiTransform.lean:1190、1400`，`ActualRiemannRootExtractionClosure.lean:38、57`；Mathlib 定义在 `formal/.lake/packages/mathlib/Mathlib/NumberTheory/LSeries/RiemannZeta.lean:185`。

本次核验保留的承重缺口是：**真实积分的全量词符号、同一行列式的严格平坦根二阶条件，以及到全部低起点内部小行列式的覆盖。**源码和既有交接证据均未改写。