## Round 256 — A/B result: the exact active-reserve balance (V_q=C_q-J_q) is fully rederived

This audit continues the Part 3 source checked in Round 255. Let an active
episode enter at \(a\) with potential \(E=\Psi(a)\) and workload
\(Y_a=Y(a)>0\). Let \(A\) be the smooth service primitive between
events, let \(A''>0\), and let the event times and weights after \(a\)
be \((\ell_i,w_i)\), with \(w_i=\Lambda(n_i)/\sqrt{n_i}\). Define
\[
P_0(a,t)=\sum_{a<\ell_i\le t}w_i,
\qquad
P_1(a,t)=\sum_{a<\ell_i\le t}(\ell_i-a)w_i,
\]
\[
S_0(a,t)=\int_a^t A''(u)\,du,
\qquad
S_1(a,t)=\int_a^t(u-a)A''(u)\,du.
\]
Between events the workload decreases with derivative \(-A''\), and each
event raises it by its weight. Therefore, at every horizon in the same
episode,
\[
Y(t)=Y_a-S_0(a,t)+P_0(a,t).
\]
Since \(\Psi'=-Y\), direct integration (or finite summation followed by
integration) gives
\[
\Psi(t)=E-(t-a)Y(t)-S_1(a,t)+P_1(a,t).
\]
Indeed, substituting the expression for \(Y(t)\) reduces the right side to
\(E-\int_a^t[Y_a-S_0(a,u)+P_0(a,u)]\,du\), because
\((t-a)S_0(a,t)-S_1(a,t)=\int_a^tS_0(a,u)\,du\) and
\((t-a)P_0(a,t)-P_1(a,t)=\int_a^tP_0(a,u)\,du\).

Let \(s=\ell_q\) be the current active event, put
\(P=P_0(a,s)\), and define the frozen recovery time \(\tau> s\) by
\[
S_0(a,\tau)=Y_a+P.
\]
Strict increase of \(S_0\) makes \(\tau\) unique. The current-event
smoothed cost is
\[
J_q=\int_a^sP_0(a,t)\,dt.
\]
Finite-sum integration, with the current event contributing zero because
\(s-s=0\), yields
\[
P_1(a,s)=(s-a)P-J_q.
\]
Freeze the stream after \(s\). At \(\tau\) the frozen workload is zero,
so the frozen continuation has value
\[
V_q=E-S_1(a,\tau)+P_1(a,s).
\]
Define the exact capacity
\[
C_q=E-S_1(a,\tau)+(s-a)P.
\]
Substituting the identity for \(P_1(a,s)\) gives the exact balance
\[
V_q=C_q-J_q.
\]
This is an unconditional identity; it uses no zero-location assertion and
does not assert the sign of either side.

The identity is therefore added to the VERIFIED PROOF CHAIN. It removes no
quantifier by itself: the remaining RH load-bearing statement is still
\(J_q\le C_q\) at every recovery witness, equivalently \(V_q\ge0\).
The source provides no RH-independent proof of that universal comparison.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步产生了一个已完整核验的精确 reserve-balance 恒等式，但没有产生新的无条件 RH 证明进展。
