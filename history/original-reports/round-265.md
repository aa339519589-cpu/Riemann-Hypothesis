## Round 265 — A-result: the checkpoint potential has an exact smoothed von Mangoldt representation

This audit independently derives the classical bridge stated in Part 5 of
Mittermeier's checkpoint series. Put
\[
\psi_{1/2}(u)=\sum_{n\le u}\frac{\Lambda(n)}{\sqrt n},
\qquad
\eta(u)=\psi_{1/2}(u)-2\sqrt u+\alpha,
\qquad
\alpha=\frac{\zeta'(1/2)}{\zeta(1/2)}.
\]
The exact service-clock expansion on the arithmetic branch is
\[
A'(\log u)=2\sqrt u-\alpha+R_A(u),
\qquad
R_A(u)=2\sum_{m\ge1}\frac{u^{-(4m+1)/2}}{4m+1}.
\]
Since \(Y=-\Psi'\) and the arithmetic prefix contributes
\(\psi_{1/2}(u)\), this gives the exact synchronization
\[
Y(t)=\eta(e^t)-R_A(e^t).
\]
The series for \(R_A\) converges absolutely for \(u\ge1\), so termwise
integration against \(du/u\) is justified on every finite interval and on
\([1,\infty)\).

For \(X\ge1\), define
\[
S(X)=\int_0^X\bigl(\psi_{1/2}(u)-2\sqrt u\bigr)\frac{du}{u}.
\]
Finite-sum integration gives
\[
S(X)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn-4\sqrt X.
\tag{265.1}
\]
Indeed, the \(n\)-th step of \(\psi_{1/2}\) contributes
\(\Lambda(n)n^{-1/2}\log(X/n)\), while
\(\int_0^X2u^{1/2}\,du/u=4\sqrt X\). Also
\[
\int_0^1\bigl(\psi_{1/2}(u)-2\sqrt u\bigr)\frac{du}{u}=-4.
\tag{265.2}
\]
Using \(\Psi(0)=0\), the synchronization, and \(u=e^t\), we obtain
\[
\Psi(\log X)
=-\int_1^X\bigl(\psi_{1/2}(u)-2\sqrt u+\alpha-R_A(u)\bigr)\frac{du}{u}.
\]
By (265.1)--(265.2),
\[
\int_1^X\bigl(\psi_{1/2}(u)-2\sqrt u\bigr)\frac{du}{u}=S(X)+4.
\]
Furthermore,
\[
\int_1^X R_A(u)\frac{du}{u}
=4\sum_{m\ge1}\frac{1-X^{-(4m+1)/2}}{(4m+1)^2}
=C-\rho_\infty(X),
\]
where
\[
C=4\sum_{m\ge1}\frac1{(4m+1)^2}
=\frac{\pi^2}{4}+2G-4,
\qquad
\rho_\infty(X)=4\sum_{m\ge1}
\frac{X^{-(4m+1)/2}}{(4m+1)^2}.
\]
Here \(\sum_{m\ge0}(4m+1)^{-2}=\pi^2/16+G/2\), obtained by splitting
the odd reciprocal-square sum into its mod-\(4\) even-character
components. Therefore, with
\[
L=C-4=\frac{\pi^2}{4}+2G-8,
\]
the exact identity is
\[
\boxed{\;
\Psi(\log X)=L-\alpha\log X-S(X)-\rho_\infty(X)
\;}.
\tag{265.3}
\]
The remainder satisfies
\[
0<\rho_\infty(X)\le\rho_\infty(1)=C,
\qquad
\rho_\infty(X)=\frac4{25}X^{-5/2}+O(X^{-9/2}).
\]
The endpoint check is exact:
\(S(1)=-4\), so the right side of (265.3) is
\(L+4-C=0=\Psi(0)\).

Consequently, using the independently established Suzuki equivalence
\(\mathrm{RH}\Longleftrightarrow\Psi(t)\ge0\) for all real \(t\), RH is
equivalent to the classical inequality
\[
S(X)+\alpha\log X+\rho_\infty(X)\le L
\qquad(X\ge1).
\]
This round contributes a complete exact dictionary and explicit tail
remainder to the VERIFIED PROOF CHAIN. It does not prove the inequality:
that inequality is the same universal RH content in a different variable.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步产生了一个已完整核验的精确 Chebyshev 桥接恒等式，但没有产生新的无条件 RH 证明进展。
