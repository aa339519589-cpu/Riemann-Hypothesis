## Round 364 — 正确 Ξ 核的正性可由 Jacobi 自对偶和逐项符号严格证明

继续使用 Round 363 的记号

\[
 S_k(x)=\sum_{n\ge1}n^k e^{-xn^2},
 \qquad P(x)=2xS_4(x)-3S_2(x).
\]

先写全 theta 和

\[
 \vartheta(x):=\sum_{m\in\mathbb Z}e^{-xm^2}=1+2S_0(x).
\]

Jacobi 变换为

\[
 \vartheta(x)=\sqrt{\frac\pi x}\,\vartheta\!\left(\frac{\pi^2}{x}\right).
\]

令 \(y=\pi^2/x\)。由 \(S_0'(x)=-S_2(x)\)、
\(S_0''(x)=S_4(x)\)，对变换式逐项求导，得到精确的自对偶恒等式

\[
 P(x)=\pi^{5/2}x^{-5/2}P(y),
 \qquad y=\frac{\pi^2}{x}.
\]

另一方面，直接展开 \(P\) 有

\[
 P(x)=\sum_{n\ge1}n^2(2xn^2-3)e^{-xn^2}.
\]

当 \(x\ge3/2\) 时，对每个 \(n\ge1\)，
\(n^2(2xn^2-3)\ge0\)，并且至少一个项严格为正，所以 \(P(x)>0)。
当 \(0<x<3/2\) 时，

\[
 y=\frac{\pi^2}{x}>\frac{2\pi^2}{3}>\frac32,
\]

故前一段已经给出 \(P(y)>0\)；自对偶恒等式的系数
\(\pi^{5/2}x^{-5/2}\) 为正，于是 \(P(x)>0\)。因此

\[
 \boxed{P(x)>0\quad\text{for every }x>0.}
\]

结合
\(\Phi(u)=2\pi^{-1/4}x^{5/4}P(x)\)，还严格得到

\[
 \boxed{\Phi(u)>0\quad\text{for every }u\in\mathbb R.}
\]

这一步闭合了正确 \(\Xi\) 核对数曲率判据中的正性前提，但没有推出
\(\mathcal C(x)\le0\)，也没有推出 Weil 全局正性或 RH。因此当前 RH
承重命题仍记为

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
