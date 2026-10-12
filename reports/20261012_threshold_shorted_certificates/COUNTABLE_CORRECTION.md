# Countable-mode threshold shorting with a coercive canonical defect

Date: 2026-10-12. Mathematical continuation of the finite rank shorting and the theta boundary-frame construction. This note extends the exact defect shorting to the closed Riesz span of an explicit infinite family of true threshold modes. For the canonical prime-tail allowance the countable correction is a bounded operator at every fixed parameter choice. A quantitative finite-mode norm estimate is also given. The remaining negative-index problem is not solved.

The input references are the finite-mode theorem and audit in
[RANK_ONE_SHORTING.md](../20261012_adaptive_spectral_tail/RANK_ONE_SHORTING.md) and
[REPORT.md](REPORT.md),
and the true Riesz frame and source-tail bound in
[theta boundary-frame REPORT.md](../20261012_theta_boundary_frame/REPORT.md) and
[its audit](../20261012_theta_boundary_frame/AUDIT.md).
The forms below use the original full even space and the original maximal form domain.

## 1. The actual defect and the canonical coercivity

Fix integers \(J\ge1,N\ge2\). Set
\[
c_J=\sum_{j=0}^{J-1}(j+\tfrac14)^{-1},\qquad
R_J(x)=\sum_{j=0}^{J-1}e^{-(2j+1/2)|x|},
\]
and
\[
p_N(x)=m(x)\sum_{n=2}^{N}\alpha_n
       \{m(x+\log n)+m(x-\log n)\},\quad
\alpha_n=\Lambda(n)/\sqrt n.
\]
Use the explicit canonical allowance from the adaptive spectral-tail report,
\[
\delta_N=\delta_N^{(0)}
 =\frac{20A_*}{9}(N+1)^2e^{-\pi(N+1)},\qquad
A_*=4\pi^2\frac{125}{121}.
\tag{1}
\]
The bounded comparison is \(K_\varepsilon=\varepsilon I+A_{J,N}\), where
\[
A_{J,N}=-\delta_N I+(c_J-C_0)M_{m^2}-M_{p_N}-M_m(R_J*)M_m.
\tag{2}
\]
Let \(D_{J,N}=H-A_{J,N}\).

On the exact original closed form domain \(\mathcal Q(H)\), the defect identity from the threshold shorting report is
\[
\begin{aligned}
d_{J,N}[v]
={}&\langle M_m v,b_{\ge J}(D)M_m v\rangle\\
&+\sum_{n=2}^{N}\alpha_n
  \int_{\mathbb R}m(x)m(x+\log n)
       |v(x+\log n)-v(x)|^2\,dx\\
&+\langle v,(\delta_N I-S_{>N})v\rangle .
\end{aligned}
\tag{3}
\]
The first term is the remaining positive Gamma multiplier as a closed form. No requirement that \(b(D)M_m v\in L^2\) is imposed for every \(v\in\mathcal Q(H)\). The second term is the exact retained-prime edge form, and \(S_{>N}\) is the actual complete omitted-prime operator. Thus (3) preserves every theta mode and every prime power; it does not truncate \(H\).

Here is the sharpened tail estimate which makes the countable correction bounded. For \(x>0\),
\(\log x/\sqrt{x}\le2/e<3/4\). For \(n\ge N+1\ge3\),
\[
\frac{(n+1)^2e^{-\pi(n+1)}}{n^2e^{-\pi n}}
\le\frac{16}{9}e^{-3}<\frac1{10},
\]
using \(\pi>3\) and \(e>8/3\). The original envelope estimate
\(\|S_{>N}\|\le2A_*\sum_{n>N}\log n\,n^{3/2}e^{-\pi n}\) therefore gives
\[
\|S_{>N}\|
 \le\frac32 A_*\sum_{n>N}n^2e^{-\pi n}
 \le\frac53 A_*(N+1)^2e^{-\pi(N+1)}
 =\frac34\delta_N.
\tag{4}
\]
Consequently
\[
D_{J,N}\succeq\gamma_N I,\qquad \gamma_N:=\delta_N/4>0,
\tag{5}
\]
on the full original form domain. Indeed the first two terms of (3) are nonnegative and the last is at least \((\delta_N-\|S_{>N}\|)\|v\|^2\).

The canonical allowance in (1) matters. For an arbitrary valid but smaller allowance, (3) still gives the usual nonnegative defect and finite-mode form shorting, but (4)-(5) need not hold. Every bounded countable-operator statement below uses exactly the canonical choice (1).

## 2. The selected true threshold Riesz span and its domain

Use the actual full-theta vectors from the theta boundary-frame report. In its notation,
\[
c_j=2^{-128}256^{-j},\quad
t(c)=-\tfrac12\log(\tfrac12+c/\pi),\quad
v_c=\frac{\Phi(\,\cdot+t(c))+\Phi(\,\cdot-t(c))
                -2\cosh(t(c)/2)\Phi}{m},
\quad
u_j=\frac{v_{c_j}}{\|v_{c_j}\|_2}.
\tag{6}
\]
That report proves the all-dimension Riesz bounds
\[
\frac{31}{32}\sum_j|a_j|^2
\le\Big\|\sum_j a_j u_j\Big\|_2^2
\le\frac{33}{32}\sum_j|a_j|^2
\tag{7}
\]
for finite sequences and hence by completion for \(\ell^2\). Each \(u_j\) is a true vector in \(\ker H\cap\operatorname{Dom}H\), from the full theta source identity and the established translation-to-derivative expansion. Set
\[
W=\overline{\operatorname{span}}\{u_j:j\ge0\},\qquad
P=P_W,\qquad
W_M=\operatorname{span}\{u_0,\ldots,u_{M-1}\},\quad P_M=P_{W_M},
\quad Q_M=P-P_M.
\tag{8}
\]
The report proves \(W\subset\ker H\) and an explicit geometric bound on
\(\|M_m(P-P_M)\|_1\), stated in Section 5 below. No such source-tail estimate is claimed here for the closure of the derivative modes \(w_r\) as a whole; \(W\) is specifically the selected Riesz span (8), which is enough for the construction.

Since \(H\) is closed and \(W\subset\ker H\), every element of \(W\) belongs to \(\operatorname{Dom}H\), with \(H|_W=0\). In particular \(P\) maps \(L^2\) boundedly into the graph domain of \(H\). For the bounded perturbation \(A_{J,N}\), the operator \(D_{J,N}=H-A_{J,N}\) is selfadjoint on exactly \(\operatorname{Dom}H\); the form domain in (3) remains exactly \(\mathcal Q(H)\).

## 3. Exact countable shorting: form theorem and bounded canonical version

First, the countable form statement does not need the sharpened allowance. Let \(D\ge0\) be any defect from (3) for any valid \(\delta_N\), and let \(\mathscr W\) be the algebraic span of any countable chosen true threshold vectors in \(\operatorname{Dom}H\). Define
\[
\mathcal M=\overline{D^{1/2}\mathscr W}^{\,L^2},\qquad
q_\infty[v]=\|P_\mathcal M D^{1/2}v\|^2
\quad(v\in\mathcal Q(H)).
\tag{9}
\]
Then
\[
q_\infty[v]
=\sup_{w\in\mathscr W,\ w\ne0}
 \frac{|d[w,v]|^2}{d[w]}
\le d[v],
\qquad
d[v]-q_\infty[v]
=\inf_{w\in\mathscr W}d[v-w].
\tag{10}
\]
These follow by orthogonal projection in the defect-energy Hilbert space. If \(\mathscr W_M\) is an increasing finite span and \(F_M\) its finite Gram correction, then \(q_\infty[v]=\sup_M\langle v,F_Mv\rangle\). For \(w\in\mathscr W\),
\[
q_\infty(w,v)=d(w,v)=\langle Dw,v\rangle.
\tag{11}
\]
Thus \(q_\infty+d_A+\varepsilon\|\cdot\|^2\), where \(d_A[v]=\langle Av,v\rangle\), is a one-sided lower comparison to \(H+\varepsilon\) on the exact original domain, for every \(\varepsilon>0\), and it is exact with eigenvalue \(\varepsilon\) on every selected mode.

This general form correction is closable. Put \(T=P_\mathcal M D^{1/2}\) on \(\mathcal Q(D)\). Its adjoint domain contains \(\mathcal M^\perp\) and \(\mathcal M\cap\mathcal Q(D)\). The latter is dense in \(\mathcal M\), since \(D^{1/2}w\in\mathcal Q(D)\) for each \(w\in\operatorname{Dom}D\) and these vectors generate \(\mathcal M\). Hence \(T\) is closable. Its closed-form extension agrees with (9) on \(\mathcal Q(H)\). This handles arbitrary valid tail allowances without silently changing the original \(H\) form domain.

For the canonical allowance (1) and the selected closed Riesz span (8), the same construction is bounded. Define
\[
C=D_{J,N}|_W=-A_{J,N}|_W:W\longrightarrow L^2,\qquad
E=P D_{J,N}|_W=P C:W\longrightarrow W.
\tag{12}
\]
The restriction \(C\) is bounded because \(H|_W=0\), so \(C=-A|_W\) and \(\|C\|\le\|A\|\). For \(u,w\in W\),
\(\langle u,Ew\rangle=d[u,w]\), hence \(E\) is bounded selfadjoint. The coercivity (5) implies \(E\succeq\gamma_N I_W\), so \(E^{-1}\) exists and \(\|E^{-1}\|\le4/\delta_N\). The exact all-mode correction is the bounded positive operator
\[
\boxed{F_\infty=C E^{-1}C^*,\qquad
\|F_\infty\|\le\frac{4\|A_{J,N}\|^2}{\delta_N}.}
\tag{13}
\]
It is the same energy projection in (9): the map \(T_0=D^{1/2}|_W:W\to L^2\) is bounded and bounded below, \(E=T_0^*T_0\), and
\(P_\mathcal M=T_0E^{-1}T_0^*\). Since \(T_0^*D^{1/2}v=C^*v\), equation (9) equals \(\langle v,F_\infty v\rangle\). In particular
\[
0\preceq F_\infty\preceq D_{J,N}
\quad\text{on the full form domain},\qquad
F_\infty w=D_{J,N}w\quad(w\in W).
\tag{14}
\]
No basis, generalized inverse, or finite-dimensional approximation occurs in (13).

For every \(\varepsilon>0\), \(A_{J,N}\) and \(F_\infty\) are independent of \(\varepsilon\), and
\[
K_\varepsilon+F_\infty\preceq H+\varepsilon I
\quad\text{on }\mathcal Q(H),\qquad
(K_\varepsilon+F_\infty)w=\varepsilon w\quad(w\in W).
\tag{15}
\]
The original \(H\), its domain and maximal form are unchanged. The correction is not compact: its compression to \(W\) is
\[
P F_\infty|_W=E\succeq(\delta_N/4)I_W
\tag{16}
\]
on an infinite-dimensional space.

## 4. Finite Gram matrices: strong convergence but no fixed-parameter norm convergence

For each \(M\), put \(E_M=P_M E|_{W_M}\). It is positive definite and the finite exact correction is
\[
F_M=C P_M E_M^{-1}P_M C^*.
\tag{17}
\]
This is precisely \(B_MG_M^{-1}B_M^*\) in an orthonormal basis of \(W_M\). It increases strongly to \(F_\infty\), by the variational formula (10). The matrix in an orthonormal basis satisfies
\[
G_M\succeq(\delta_N/4)I.
\]
If the frame columns \(u_0,\ldots,u_{M-1}\) are used directly, (7) gives the coefficient-space bound \(G_M\succeq(31\delta_N/128)I\). Thus the inverse defect Gram is uniformly controlled in \(M\) for each fixed canonical \(J,N\).

Strong convergence must not be upgraded to norm convergence. Decompose \(W=W_M\oplus(W\ominus W_M)\), write \(E_{ij}\) for the blocks, and set
\[
S_M=E_{22}-E_{21}E_{11}^{-1}E_{12},\qquad
R_M=Q_M-P_ME_{11}^{-1}E_{12}.
\]
The Schur complement identity is
\[
F_\infty-F_M=(D_{J,N}R_M)S_M^{-1}(D_{J,N}R_M)^*.
\tag{18}
\]
Minimizing the \(E\)-energy over the first block shows \(S_M\succeq(\delta_N/4)I\) on the tail block. Further \(Q_M(F_\infty-F_M)Q_M=S_M\), so
\[
\boxed{\|F_\infty-F_M\|\ge\delta_N/4.}
\tag{19}
\]
This lower bound holds for every \(M\) at fixed \(N\). It also follows from noncompactness (16). The geometric source-tail result does not imply same-\(N\) operator-norm convergence.

## 5. Explicit joint \(M,N\) error using the actual theta source tail

The theta boundary-frame report proves, for the projections (8),
\[
\|M_m Q_M\|_1\le\tau_M,\qquad \tau_M=2^{-147}16^{-M}.
\tag{20}
\]
This is the proved tail for the selected true Riesz span \(W\). We do not transfer it to the closure of all derivative modes.

Set
\[
\kappa_N=\|p_N/m\|_\infty,\quad m_\infty=\|m\|_\infty<3,
\]
\[
L_{J,N}=m_\infty(|c_J-C_0|+c_J)+\kappa_N,\qquad
\bar A_{J,N}=\delta_N+
 m_\infty^2(|c_J-C_0|+c_J)+m_\infty\kappa_N.
\tag{21}
\]
Then \(\|A_{J,N}\|\le\bar A_{J,N}\). The finite sum gives
\(\kappa_N\le2m_\infty(N-1)\), so these constants are explicit.

From (2), write
\[
D_{J,N}Q_M=\delta_N Q_M+T_{J,N}Q_M,\quad
T_{J,N}=-(c_J-C_0)M_{m^2}+M_{p_N}+M_m(R_J*)M_m.
\tag{22}
\]
Here \(H Q_M=0\) on the actual operator domain; all vectors in \(W\) are genuine kernel vectors. Since
\(M_{p_N}=M_{p_N/m}M_m\), \(\|R_J*\|=c_J\), and (20),
\[
\eta_M:=\|T_{J,N}Q_M\|\le L_{J,N}\tau_M,\qquad
\|P_M D_{J,N}Q_M\|\le\eta_M,\quad
\|D_{J,N}Q_M\|\le\delta_N+\eta_M.
\tag{23}
\]
Also \(\|D_{J,N}P_M\|\le\|A_{J,N}\|\le\bar A_{J,N}\) and
\(\|E_{11}^{-1}\|\le4/\delta_N\). Hence
\[
\|D_{J,N}R_M\|
\le\delta_N+\eta_M\left(1+\frac{4\bar A_{J,N}}{\delta_N}\right).
\tag{24}
\]
Combining (18), (24), and \(\|S_M^{-1}\|\le4/\delta_N\) yields
\[
\boxed{
\|F_\infty-F_M\|
\le\frac4{\delta_N}
\left[\delta_N+
L_{J,N}2^{-147}16^{-M}
\left(1+\frac{4\bar A_{J,N}}{\delta_N}\right)\right]^2.}
\tag{25}
\]
In particular, if
\[
L_{J,N}2^{-147}16^{-M}
\le\frac{\delta_N^2}{\delta_N+4\bar A_{J,N}},
\tag{26}
\]
then
\[
\|F_\infty-F_M\|\le16\delta_N.
\tag{27}
\]
An explicit sufficient choice is
\[
M\ge\max\!\left\{1,\left\lceil
\log_{16}\frac{2^{-147}L_{J,N}(\delta_N+4\bar A_{J,N})}{\delta_N^2}
\right\rceil\right\}.
\tag{28}
\]
Thus a coupled limit \(N\to\infty\), \(M=M(J,N)\to\infty\) can have vanishing error \(16\delta_N\). With \(J\) fixed or polynomially growing, \(\delta_N\asymp N^2e^{-\pi N}\) and \(L,\bar A=O(N+\log J)\), so (28) requires
\(M=(2\pi/\log16)N+O(\log N)\). This joint estimate is fully compatible with (19): fixed-\(N\) norm convergence is impossible, and the vanishing bound is only after the coercivity parameter \(\delta_N/4\) itself tends to zero.

## 6. Exact domain and unresolved negative index

For each fixed canonical \(J,N\), (13)-(15) give a bounded selfadjoint all-mode repaired comparison on the unchanged full original even space and an exact one-sided inequality on \(\mathcal Q(H)\). The original prime tail was paid in full in (3)-(5). The norm estimate (25) controls approximation of this correction, not the sign of its spectrum.

The correction \(F_\infty\) is noncompact by (16), so the finite-rank compact signed Birman--Schwinger trace test in the rank-one report does not directly extend to it. Neither (5) nor (25) shows that \(K_\varepsilon+F_\infty\) has at most one negative direction. In particular, they do not exclude negative essential spectrum or other discrete negative directions on \(e_0^\perp\); the possible survival of the \(-\delta_N\) essential level in the complement has not been resolved. The Riesz span \(W\) is an explicit infinite-dimensional subspace of \(\ker H\), not a proved basis of \(\ker H\). No positivity of \(H\) on \(e_0^\perp\), critical \(1/2\) gap, or RH conclusion follows.

The verified advance is narrower but concrete: the canonical full-prime defect is coercive by \(\delta_N/4\); this makes the exact countable shorting over the selected true theta Riesz span bounded at each fixed \(J,N\), with controlled inverse Grams and the explicit joint truncation bound (25)-(28). The all-\(\varepsilon\) sign/inertia step remains open.


Independent verification of the canonical defect, all-mode operator and truncation estimate is [REFEREE_COUNTABLE_CORRECTION.md](REFEREE_COUNTABLE_CORRECTION.md). The full maximal-domain realization is [ORIGINAL_FORM_FOUNDATION.md](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md). No priority claim is made for abstract projection or Schur identities.
