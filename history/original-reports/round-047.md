## Round 47 — zero-collapse automatically yields a weighted-range relation

The source estimates give more than a merely hypothetical weighted model in
the zero-collapse case. Assume there are finitely many off-critical ordinates
and take the negative finite-section branch with

\[
 \lambda_N<0,
 \qquad \lambda_N\longrightarrow0.
\tag{47.1}
\]

Let \(C_N\) denote the critical ordinates in \(\Gamma_N\), let \(E\) be the
fixed finite off-critical set, and put

\[
 d_\gamma=\tfrac14+\gamma^2,
 \qquad
 q_{\gamma;N}=\frac{w_{\gamma;N}}{\sqrt{d_\gamma}}
 \quad(\gamma\in C_N).
\tag{47.2}
\]

Extend \(q_N\) by zero to all critical ordinates. Since
\(\sum|w_{\gamma;N}|^2=1\) and \(d_\gamma\geq\tfrac14\),

\[
 \|q_N\|_2\leq2.
\tag{47.3}
\]

Write the source's boundary-corrected function as

\[
 F_N(u)=Z_N(u)-g_N(u),
 \qquad
 g_N(u)=a_Ne^{u/2}+b_Ne^{-u/2},
\tag{47.4}
\]

and define the weighted critical synthesis

\[
 A_Nq_N(u)=\sum_{\gamma\in C_N}
 \frac{q_{\gamma;N}}{\sqrt{d_\gamma}}e^{-i\gamma u}
 =\sum_{\gamma\in C_N}\frac{w_{\gamma;N}}{d_\gamma}e^{-i\gamma u}.
\tag{47.5}
\]

The off-critical packet is

\[
 h_{E,N}(u)=\sum_{\gamma\in E}\frac{w_{\gamma;N}}{d_\gamma}e^{-i\gamma u},
\]

so, with \(h_N=g_N-h_{E,N}\),

\[
 A_Nq_N-h_N=F_N.
\tag{47.6}
\]

Bombieri's equation (10.4) gives

\[
 \frac14\|F_N\|_{L^2(-t,t)}^2
 +\|F_N'\|_{L^2(-t,t)}^2
 \leq |\lambda_N|,
\]

and therefore

\[
 \|A_Nq_N-h_N\|_{L^2(-t,t)}\leq2\sqrt{|\lambda_N|}.
\tag{47.7}
\]

The endpoint equations determine \(a_N,b_N\) from \(Z_N(t),Z_N(-t)\). The
uniformly absolutely convergent \(d_\gamma^{-1}\)-series and the finite
coordinate convergence imply, after the same subsequence extraction, that
\(a_N,b_N\) and \(h_{E,N}\) converge in \(L^2(-t,t)\) to a limit \(a,b,h_E\).
Hence \(h_N\to h:=ae^{u/2}+be^{-u/2}-h_E\).

Define the infinite weighted synthesis

\[
 Aq(u)=\sum_{\gamma\in\Gamma_C}
 \frac{q_\gamma}{\sqrt{d_\gamma}}e^{-i\gamma u}.
\tag{47.8}
\]

It is Hilbert--Schmidt because

\[
 \|A\|_{\mathrm{HS}}^2
 =2t\sum_{\gamma\in\Gamma_C}\frac1{d_\gamma}<\infty.
\tag{47.9}
\]

Extract a weakly convergent subsequence \(q_N\rightharpoonup q\) in
\(\ell^2(\Gamma_C)\). Hilbert--Schmidt compactness gives
\(Aq_N\to Aq\) strongly, and (47.9) also gives
\(\|A_N-A\|_{2\to2}\to0\). Thus

\[
 A_Nq_N\longrightarrow Aq\quad	ext{in }L^2(-t,t).
\tag{47.10}
\]

Combining (47.6)--(47.10) proves the exact source-faithful range relation

\[
 h=Aq,
 \qquad q\in\ell^2(\Gamma_C),
\tag{47.11}
\]

for every zero-collapse subsequence. This is a genuine deduction: it uses the
finite eigenvector normalization, the source's local energy estimate, and the
compact weighted synthesis, not an arbitrary replacement of the coefficient
class.

There is one remaining quantitative distinction. Equation (47.7) controls the
moving target \(h_N\) at the \(\sqrt{|\lambda_N|}\) scale. The source gives no
rate for \(h_N\to h\), so it does not yet imply

\[
 \|A_Nq_N-h\|=O(\sqrt{|\lambda_N|})
\tag{47.12}
\]

for the fixed limiting target. The exact infinite range membership (47.11) is
nevertheless established.

**Established:** the zero-collapse branch forces a nonzero source-generated
weighted \(\ell^2\) local relation, with a uniformly bounded finite-section
coefficient cost; the finite residual is controlled at the source energy scale.

**Remaining load-bearing statement:** exclude (47.11) for the actual critical
zeta ordinates, or obtain a convergence-rate theorem upgrading (47.7) to the
fixed-target estimate (47.12) and then use a quantitative range obstruction.

**RH status:** no unconditional proof has been produced.
