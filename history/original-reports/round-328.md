## Round 328 — Elliptic-complex candidate has a direct contradiction

核验 Xian Wang 与 Luoyi Fu 的 “Toward a Proof of the Riemann Hypothesis:
Insights from Elliptic Complex Analysis”，2026-02-28，PDF
https://rxiv.org/pdf/2603.0014v1.pdf，SHA-256
dd37c8ab0a1ba2f0f2d5fe837573195561b3e1ad504f1b41e2e1aae5f719d830。
稿件的第 9 节声称通过 \(\lambda=-q^2\to0^-\) 证明 RH。

命题 9.5(2) 给出了一个可直接击破的内部反检验。它声称：若
\(s=\Delta+i z/q_1\) 是某个 \(C_{\lambda_1}\) 上的 \(\xi\) 零点，则对
任意 \(q_2>0\)，\(s'=\Delta+i z/q_2\) 也是相应的零点。取
\(q_1=1\)、\(\Delta=1/2\)，并取 Hardy 定理保证存在的临界线零点
\(\xi(1/2+i\gamma)=0\)，令 \(z=\gamma\)。命题便推出
\[
\xi\!\left(\frac12+i\frac{\gamma}{q_2}\right)=0
\quad\text{for every }q_2>0.
\]
当 \(q_2\to\infty\) 时，这些不同零点在 \(1/2\) 聚积；但 \(\xi\) 是非零
整函数，零点必须孤立。这说明 Proposition 9.5(2) 本身不可能成立，
所以建立在它之上的“椭圆对应”和反证不能证明 RH。

稿件最后的式 (82) 还有独立的代数矛盾。稿件先写
\(\tan\alpha=\tan\beta/q\)。若反设的零点确实离开临界线，则
\(\tan\alpha\) 是有限数，于是
\[
\tan\beta=q\tan\alpha\longrightarrow0\qquad(q\to0^+),
\]
而不是稿件随后断言的 \(\beta\to\pi/2\) 和
\(\tan\beta\to\infty\)。因此式 (82) 的矛盾结论不由其前提推出。

这些是稿件自身定义和已知 Hardy 定理之间的直接矛盾；没有给出 RH 的
无条件证明，也没有给出 RH 的无条件否证。

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
