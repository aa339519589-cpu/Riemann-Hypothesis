# Exact negative essential spectrum of the infinitely theta-shorted comparator

Date: 2026-10-12. Full original aim: unconditional RH. This is a new theorem about the original full-theta, full-prime **lower comparator**, not a theorem about negative eigenvalues of the original Weil operator H. It closes the open fixed-N essential-spectrum question explicitly identified in the last section of COUNTABLE_CORRECTION.md.

## 1. Inherited objects and quantifiers

Let \(\mathcal H=L^2_{\rm even}(\mathbb R,dx)\), \(H=B-V\) be the original selfadjoint operator with all prime powers and complete Gamma multiplier. Use the selected true critical Riesz span \(W\subset\ker H\cap\operatorname{Dom}H\) and its infinite-rank orthogonal projection \(P\). Set \(Q=I-P\). The source-tail theorem, theta boundary-frame REPORT.md Eq. (5.1), says
\[
\|M_m(P-P_M)\|_1\le 2^{-147}16^{-M}\quad(M\ge1).
\tag{1}
\]
Since \(M_mP_M\) is finite rank, it follows that
\[
M_mP\in\mathfrak S_1(\mathcal H).
\tag{2}
\]
Here \(\mathfrak S_1\) denotes trace class. The projection P itself remains noncompact.

Fix finite \(J\ge1,N\ge2\), and retain the canonical, strictly positive full omitted-prime allowance
\[
\delta=\delta_N=\frac{20A_*}{9}(N+1)^2e^{-\pi(N+1)}>0.
\]
In the notation of COUNTABLE_CORRECTION.md, define
\[
c_J=\sum_{j=0}^{J-1}(j+\tfrac14)^{-1},\quad
R_J(x)=\sum_{j=0}^{J-1}e^{-(2j+1/2)|x|},
\]
\[
p_N(x)=m(x)\sum_{n=2}^N\frac{\Lambda(n)}{\sqrt n}
[m(x+\log n)+m(x-\log n)],
\]
\[
g(x)=(c_J-C_0)m(x)^2-p_N(x),\qquad
T=M_m(R_J*)M_m.
\tag{3}
\]
The original *bounded* comparison and exact full-original defect are
\[
A=-\delta I+M_g-T,\qquad K_\varepsilon=\varepsilon I+A,\qquad D=H-A.
\tag{4}
\]
The defect identity in the earlier countable-shortening report includes every omitted prime power and proves \(D\succeq\delta I/4\) on the original form domain. For the inclusion \(i:W\to\mathcal H\), set
\[
C=D|_W=-A|_W,\qquad E=i^*C=P D|_W\succeq(\delta/4)I_W,
\qquad F_\infty=CE^{-1}C^*.
\tag{5}
\]
This is the existing *exact bounded infinite-mode* correction, not a finite-rank surrogate. In particular \((K_\varepsilon+F_\infty)w=\varepsilon w\) for every \(w\in W\).

Set \(g_-=\inf_{\mathbb R}g(x)\) and \(g_+=\sup_{\mathbb R}g(x)\).

## 2. Main theorem

**Theorem.** For every fixed finite \(J\ge1,N\ge2\) and every real \(\varepsilon\),
\[
\boxed{\sigma_{\rm ess}(K_\varepsilon+F_\infty)
=\{\varepsilon\}\cup
[\varepsilon-\delta+g_-,\ \varepsilon-\delta+g_+].}
\tag{6}
\]
Moreover \(g_-<0\le g_+\). Consequently, for every
\[
\boxed{0<\varepsilon<\delta-g_-}
\tag{7}
\]
the *lower comparison* \(K_\varepsilon+F_\infty\) has an infinite-dimensional negative spectral subspace. In particular it has negative essential spectrum for **every** \(0<\varepsilon<\delta\). Its infinite true-critical W block simultaneously has exact eigenvalue \(\varepsilon\).

### Proof, part A: compact Gamma convolution and source-local trace class

The actual theta \(m>0\) is smooth, even, bounded and in \(L^2\). Because \(|R_J|\le J\), the full-line integral-kernel Hilbert-Schmidt estimate is
\[
\|T\|_{\mathfrak S_2}^2
\le\iint m(x)^2J^2m(y)^2\,dx\,dy=J^2\|m\|_2^4<\infty.
\tag{8}
\]
So T is compact on the even space. This says nothing about compactness of the *unbounded full Gamma* B.

The finite-prime \(p_N\), \(m^2\), and their difference \(g\) are continuous, bounded, even and tend to zero at both spatial infinities. Since
\[
g/m=(c_J-C_0)m-p_N/m\in L^\infty,
\]
the actual source trace class (2) gives
\[
M_gP=M_{g/m}M_mP\in\mathfrak S_1,\quad
TP=M_m(R_J*)M_mP\in\mathfrak S_1.
\tag{9}
\]
Selfadjointness makes \(PM_g\) trace class as well. We have *not* claimed multiplication by nonzero g is compact; it is generally not.

### Proof, part B: identify the noncompact part of the exact countable repair

Since H vanishes on W, (4)–(5) give
\[
C=\delta i+L,\qquad L=(-M_g+T)i\in\mathfrak S_1(W,\mathcal H).
\tag{10}
\]
Hence
\[
E=\delta I_W+i^*L,\qquad
E^{-1}-\delta^{-1}I_W=-\delta^{-1}E^{-1}i^*L\in\mathfrak S_1(W).
\tag{11}
\]
The inverse is a true bounded inverse because \(E\ge\delta I_W/4\). The following identity is exact:
\[
F_\infty-\delta P
=L E^{-1}C^*
+\delta i(E^{-1}-\delta^{-1}I_W)C^*
+iL^*.
\tag{12}
\]
All three terms are trace class, so
\[
\boxed{F_\infty=\delta P+\mathfrak S_1.}
\tag{13}
\]
In particular it is a *trace-class* perturbation of a noncompact projection, stronger than the previous noncompactness observation.

### Proof, part C: the exact block reduction

For \(w\in W\), selfadjointness of D and the definition of E give \(C^*w=Ew\). Thus
\[
F_\infty w=CE^{-1}Ew=Dw=-Aw.
\]
Consequently \((A+F_\infty)P=P(A+F_\infty)=0\) exactly. On the complete even space,
\[
A+F_\infty
= -\delta Q+M_g+\mathcal C,
\quad \mathcal C=-T+(F_\infty-\delta P)\text{ is compact}.
\tag{14}
\]
Therefore, with \(\mathcal H_Q=Q\mathcal H\),
\[
A+F_\infty
=0_W\ \oplus\
\big[-\delta I_{\mathcal H_Q}+(QM_gQ)|_{\mathcal H_Q}
+\text{compact}\big].
\tag{15}
\]

### Proof, part D: the entire essential spectrum of compressed multiplication

We prove
\[
\boxed{\sigma_{\rm ess}((QM_gQ)|_{\mathcal H_Q})=[g_-,g_+].}
\tag{16}
\]
The spectrum lies in the interval by the Rayleigh bounds for real multiplication \(M_g\).

For the opposite inclusion, fix any \(\lambda\) in the closure of the range of g. Let \(\eta_j\downarrow0\). Continuity, parity and \(g(x)\to0\) furnish bounded symmetric nonempty open sets \(S_j\), with
\[
|g(x)-\lambda|<2\eta_j\quad(x\in S_j).
\tag{17}
\]
The space \(\mathcal L_j\) of even \(L^2\) functions supported in \(S_j\) is infinite-dimensional. Choose even compactly supported \(\chi_j\) equal to one on \(S_j\). Positivity of m on this compact region implies \(\chi_j/m\) is bounded, and by (2)
\[
P\chi_j=(\chi_jP)^*,\quad
\chi_jP=M_{\chi_j/m}(M_mP)\in\mathfrak S_1.
\tag{18}
\]
Thus the restriction of P to \(\mathcal L_j\) is compact. Fix an orthonormal basis \(h_1,h_2,\ldots\) of the even Hilbert space. Choose unit \(\varphi_j\in\mathcal L_j\) orthogonal to \(h_1,\ldots,h_j\) and with \(\|P\varphi_j\|<\eta_j\). Such a vector exists: there is an infinite orthonormal sequence inside those finite-codimension constraints, and its image under compact \(P\chi_j\) converges to zero.

Then \(\varphi_j\rightharpoonup0\) and \(\|(M_g-\lambda)\varphi_j\|\le2\eta_j\). The unit vectors
\[
\psi_j=Q\varphi_j/\|Q\varphi_j\|\in\mathcal H_Q
\]
also converge weakly to zero, satisfy \(\|\psi_j-\varphi_j\|\to0\), and obey
\[
\|(QM_gQ-\lambda)\psi_j\|
\le\frac{(2+\|g\|_\infty)\eta_j}{\sqrt{1-\eta_j^2}}
\longrightarrow0.
\tag{19}
\]
Weyl's singular-sequence criterion proves the lower inclusion. Since the image of continuous real g is an interval and its closure is \([g_-,g_+]\), (16) holds, including \(\lambda=0\). The latter matters: the zero block on W alone cannot determine whether the *Q block* has zero in its essential spectrum.

Now (15), compact-perturbation invariance of selfadjoint essential spectrum, and the infinite dimension of W yield
\[
\sigma_{\rm ess}(A+F_\infty)
=\{0\}\cup[-\delta+g_-,-\delta+g_+].
\]
A scalar shift by \(\varepsilon I\) proves (6). QED.

### Proof, part E: the original prime 2 makes the left endpoint strictly lower

The true first-theta-mode tail gives
\[
m(x)\sim2\pi e^{2x}e^{-(\pi/2)e^{2x}}
\quad(x\to+\infty).
\tag{20}
\]
For \(d=\log2\),
\[
\frac{m(x-d)}{m(x)}
\sim\frac14\exp[(3\pi/8)e^{2x}]\longrightarrow+\infty.
\tag{21}
\]
All retained prime-power coefficients are nonnegative and \(N\ge2\) includes the strictly positive \(\alpha_2=\Lambda(2)/\sqrt2\). Hence
\[
\frac{g(x)}{m(x)^2}
=(c_J-C_0)-\sum_{n=2}^N\frac{\Lambda(n)}{\sqrt n}
\frac{m(x+\log n)+m(x-\log n)}{m(x)}
\le (c_J-C_0)-\alpha_2\frac{m(x-\log2)}{m(x)}
\to-\infty.
\tag{22}
\]
Therefore \(g(x)<0\) for some finite x, \(g_-<0\), and \(g_+\ge0\) since g tends to zero. Equation (7) then forces an essential negative spectral interval in the lower comparison. QED.

## 3. Precise consequence for the attempted full RH proof

This settles one outstanding fixed-parameter question in COUNTABLE_CORRECTION.md: the exact countable theta shorting **cannot** remove the comparator's negative essential spectrum as \(\varepsilon\to0^+\) with J and N held fixed. The entire essential spectrum, not just the isolated candidate level \(-\delta\), is now explicit. A fixed-parameter one-negative-direction certificate is therefore ruled out, even if every mode in the selected infinite W is repaired exactly.

The allowed escape \(N=N(\varepsilon)\to\infty\), together with \(J(\varepsilon)\) and possibly other comparison changes, requires separate analysis. The theorem cannot be used to rule it out. And since \(\mathcal K_\varepsilon\preceq H+\varepsilon I\) is a **lower** bound, negative essential spectrum of \(\mathcal K_\varepsilon\) does not give an actual negative eigenvalue of H, an off-line zeta zero, or a refutation of RH.

**New unconditional auxiliary result, assuming the independently recorded original theta-source projection theorem. NO NEW UNCONDITIONAL RH THEOREM PROVED.**

Dependencies retained verbatim: countable-shortening COUNTABLE_CORRECTION.md Eqs. (1)–(5),(8),(12)–(16), and theta boundary-frame REPORT.md Eq. (5.1). All new trace-class, Weyl, and strict-prime asymptotic deductions are supplied in full above. No preexisting file has been edited or reinterpreted.
