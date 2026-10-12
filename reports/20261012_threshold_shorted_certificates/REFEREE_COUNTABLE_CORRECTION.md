# Referee check: coercive defect shorting on the theta Riesz span

Date: 2026-10-12. Independent mathematical check of the proposed fixed-(J,N) infinite shorting argument. This review concerns the canonical parameter choice and selected true-theta Riesz span.

## 1. Sharper omitted-prime bound and a scope qualification

Let
\[
\delta_N^{(0)}=\frac{20A_*}{9}(N+1)^2e^{-\pi(N+1)}
\]
be the explicit envelope in the adaptive spectral-tail report. For every x>0, the function log(x)/sqrt(x) has maximum 2/e at x=e^2. Since e>8/3,
\[
\log n\le \frac2e\sqrt n <\frac34\sqrt n.
\]
The same estimate used to define the displayed envelope gives, for n>=N+1>=3,
\[
\frac{(n+1)^2e^{-\pi(n+1)}}{n^2e^{-\pi n}}
\le \frac{16}{9}e^{-3}<\frac1{10}.
\]
Here the coarse 16/9 uses n>=3, and e>8/3 gives (16/9)e^-3 <= 3/32 <1/10. Thus
\[
\|S_{>N}\|
\le 2A_*\sum_{n>N}\log n\,n^{3/2}e^{-\pi n}
\le \frac34\,\delta_N^{(0)}.
\]
If the comparator uses delta_N=delta_N^(0), or any delta_N>=delta_N^(0), then
\[
\delta_N I-S_{>N}\succeq \frac{\delta_N}{4}I.
\]
The other terms of the exact defect form are nonnegative, so on the full original form domain
\[
D_{J,N}=H-A_{J,N}\succeq \gamma_N I,\qquad \gamma_N=\delta_N/4>0.
\]
The qualification matters: the 3/4 comparison is relative to the displayed analytic envelope (or a larger choice). It does not follow for an arbitrary smaller number that happens to be a valid upper bound on the actual tail.

## 2. Full-domain operator restriction and the infinite shorted operator

Fix J,N,delta_N as above, and write W=Ran(P_b), the closed Riesz span from the theta-frame report. Every frame vector is in ker H and in Dom H. The latter is inherited from the source identity and the original form/operator-domain foundation: for each selected real t<a_*, f_t=m v_t is a Schwartz combination of translates of Phi, b(D)f_t is in L2, and the translated source identity gives (A_source-S_source)f_t=0. Closedness of H then puts the L2 closure W in ker H and Dom H. Consequently P_b maps L2 boundedly into Dom H and
\[
D_{J,N}P_b=-A_{J,N}P_b
\]
is a bounded operator. This is the key domain fact; it does not apply to arbitrary source-L2 errors.

Let
\[
C=D_{J,N}|_W=-A_{J,N}|_W:W\to L^2,\qquad
E=P_bD_{J,N}|_W=P_bC:W\to W.
\]
Then E is bounded selfadjoint and E>=gamma_N I on W. In particular it is invertible, with ||E^-1||<=4/delta_N. Define the countable shorting
\[
F_\infty=C E^{-1}C^*.
\]
It is a bounded positive operator with
\[
\|F_\infty\|\le \frac{4\|A_{J,N}\|^2}{\delta_N},\qquad
0\preceq F_\infty\preceq D_{J,N}
\]
in the closed-form sense. The domination is the variational Cauchy--Schwarz bound over w in W. For the first M frame vectors, the public finite correction is exactly
\[
F_M=C P_M E_M^{-1}P_M C^*,\qquad
E_M=P_ME|_{W_M},\quad W_M=\operatorname{Ran}P_M.
\]
This is the basis-independent version of B_M G_M^-1 B_M^*. Since W_M increases densely in W and E is coercive, the variational formula proves F_M increases strongly to F_infinity. This repairs the finite defect-Gram invertibility issue for each fixed J,N: in an L2-orthonormal basis of W_M, G_M>=delta_N/4 I. For the reported nonorthogonal frame columns u_0,...,u_(M-1), the Riesz bound gives
\[
G_M\succeq (31\delta_N/128)I
\]
on coefficient space.

## 3. Exact Schur-complement norm error

Strong convergence is not operator-norm convergence at fixed N. Let Q_M=P_b-P_M and use the L2-orthogonal decomposition W=W_M\oplus(W\ominus W_M). In that decomposition write
\[
E=\begin{pmatrix}E_{11}&E_{12}\\E_{21}&E_{22}\end{pmatrix},\quad
S_M=E_{22}-E_{21}E_{11}^{-1}E_{12},\quad
R_M=Q_M-P_ME_{11}^{-1}E_{12}.
\]
Since E>=gamma_N I, the Schur complement satisfies S_M>=gamma_N I: for z in the tail space, <z,S_M z> is the minimum over x in W_M of <x+z,E(x+z)>, which is at least gamma_N||z||^2. The block inverse identity gives the exact formula
\[
F_\infty-F_M=(D_{J,N}R_M)S_M^{-1}(D_{J,N}R_M)^*.
\tag{1}
\]
In particular Q_M(F_infinity-F_M)Q_M=S_M, so
\[
\|F_\infty-F_M\|\ge \|S_M\|\ge \delta_N/4.
\tag{2}
\]
This is unavoidable: for fixed positive delta_N, finite-rank F_M cannot converge in norm to F_infinity. Indeed P_b F_infinity P_b=E>=gamma_N I on the infinite-dimensional W, so F_infinity is noncompact.

There is also a parameter-explicit upper estimate using the source-tail result. Put
\[
\tau_M=2^{-147}16^{-M},\qquad
\kappa_N=\|p_N/m\|_\infty,\qquad m_\infty=\|m\|_\infty<3,
\]
and
\[
L_{J,N}=m_\infty(|c_J-C_0|+c_J)+\kappa_N.
\]
The report proves ||M_m Q_M||_1<=tau_M, hence ||M_m Q_M||<=tau_M. Since
\[
A_{J,N}=-\delta_N I+(c_J-C_0)M_{m^2}-M_{p_N}-M_m(R_J*)M_m,
\qquad \|R_J*\|=c_J,
\]
and H Q_M=0, one gets
\[
D_{J,N}Q_M=\delta_N Q_M+T_{J,N}Q_M,\qquad
T_{J,N}=-(c_J-C_0)M_{m^2}+M_{p_N}+M_m(R_J*)M_m,
\]
with
\[
\eta_M:=\|T_{J,N}Q_M\|\le L_{J,N}\tau_M.
\tag{3}
\]
The p_N term is valid because M_{p_N}Q_M=M_{p_N/m}M_mQ_M; p_N/m is bounded for finite N. Also
\[
\|A_{J,N}\|\le \bar A_{J,N}:=
\delta_N+m_\infty^2(|c_J-C_0|+c_J)+m_\infty\kappa_N.
\]
For example, \(\kappa_N\le2m_\infty\sum_{2\le n\le N}\alpha_n\le 2m_\infty(N-1)\), so all constants are explicit.

From (3), P_MD Q_M=P_MTQ_M has norm at most eta_M, ||D Q_M||<=delta_N+eta_M, ||D P_M||<=||A||, and ||E_M^-1||<=4/delta_N. Therefore
\[
\|D R_M\|
\le \delta_N+\eta_M\left(1+\frac{4\bar A_{J,N}}{\delta_N}\right).
\]
Combining with (1) yields the requested finite-M norm estimate
\[
\boxed{\;
\|F_\infty-F_M\|
\le \frac4{\delta_N}
\left[
\delta_N+L_{J,N}2^{-147}16^{-M}
\left(1+\frac{4\bar A_{J,N}}{\delta_N}\right)
\right]^2 .\;}
\tag{4}
\]
The factor 4/delta_N is real and cannot be suppressed. The source tail alone does not make (4) vanish for fixed N; (2) proves that no such fixed-N vanishing norm tail is possible.

If M is chosen so that
\[
L_{J,N}2^{-147}16^{-M}
\le \frac{\delta_N^2}{\delta_N+4\bar A_{J,N}},
\tag{5}
\]
then (4) gives ||F_infinity-F_M||<=16 delta_N. An explicit sufficient choice is
\[
M\ge \max\!\left\{1,\left\lceil
\log_{16}\!\frac{2^{-147}L_{J,N}(\delta_N+4\bar A_{J,N})}{\delta_N^2}
\right\rceil\right\}.
\tag{6}
\]
Thus one may let N tend to infinity and choose M by (6), obtaining a vanishing cross-parameter error because delta_N tends to zero. With J fixed or growing at most polynomially in N, the displayed envelope gives delta_N≈N^2e^(-pi N), while L and A-bar are O(N+log J); (6) asks for M≈(2pi/log 16)N+O(log N). This is an explicit way to balance the inverse-defect factor against the true-theta source tail. It is not a same-N operator-norm limit.

## 4. Remaining threshold limitation

For each fixed (J,N), the improved delta/4 coercivity makes the countable shorting and its inverse-defect Gram well-defined, and the public source-tail estimate gives (4). Yet the coercivity constant collapses as N grows. The finite signed Birman--Schwinger trace condition needed to prove at most one negative direction is still unproved. The comparison of F_infinity with F_M does not by itself bound the signed trace of T-Y_M Y_M* or prove its required sign. The positive-depth gaps and the unknown negative spectrum of H on e_0-perpendicular intersect W-perpendicular remain unresolved.



Publication note: [COUNTABLE_CORRECTION.md](COUNTABLE_CORRECTION.md) contains the reviewed fixed-parameter coercivity, all-mode correction and exact Schur error, preserving the general form construction separately from the canonical bounded version. It explicitly retains the fixed-N noncompactness obstruction and the unproved negative-index condition.
