## Round 260 — B-result: the local recovery window does not imply \(J_q\le C_q\)

The exact identities in Rounds 256--259 can be stress-tested without any
zeta-specific approximation. Take the strictly convex service primitive
\[
A(t)=\frac{t^2}{2},\qquad A'(t)=t,\qquad A''(t)=1
\]
on \(t\ge0\). Let an active episode enter at \(a=0\) with
\[
E=\frac15,\qquad Y_a=\frac12.
\]
Insert an intervening event at
\[
\ell_1=\frac25,\qquad w_1=\frac45,
\]
and take the current event at
\[
s=1,\qquad w_q=\frac15.
\]
Choose the next event at \(\ell_{q+1}=2\). All event weights are positive,
and the entry potential and entry workload are positive.

The post-current workload is
\[
Y_q=Y_a-A'(s)+w_1+w_q
=\frac12-1+\frac45+\frac15
=\frac12.
\]
The next-event service gap is
\[
\delta_q=A'(2)-A'(1)=1,
\]
so \(0<Y_q<\delta_q\). The frozen workload after \(s\) is
\(3/2-t\), and therefore recovers at \(t=3/2\), strictly before the next
event. Thus this is an exact strict-recovery instance of the local
recovery-window conditions.

The post-entry terminal load and the smoothed timing cost are
\[
P=w_1+w_q=1,\qquad
J_q=(s-\ell_1)w_1
=\left(1-\frac25\right)\frac45
=\frac{12}{25}.
\]
The frozen recovery time is determined by
\(S_0(0,\tau)=Y_a+P\), hence \(\tau=3/2\), and
\[
S_1(0,\tau)=\int_0^{3/2}u\,du=\frac98,
\qquad
P_1(0,s)=\frac25\frac45+1\frac15=\frac{13}{25}.
\]
Consequently,
\[
V_q=E-S_1(0,\tau)+P_1(0,s)
=\frac15-\frac98+\frac{13}{25}
=-\frac{81}{200}<0.
\]
The exact capacity is
\[
C_q=E-S_1(0,\tau)+(s-a)P
=\frac15-\frac98+1
=\frac{3}{40}>0,
\]
but
\[
J_q=\frac{12}{25}>\frac{3}{40}=C_q,
\qquad
V_q=C_q-J_q.
\]
This is a hostile counterexample to the inference from the local
recovery-window data, positive entry potential, and strict convexity to the
reserve inequality. It is not a counterexample to the Riemann hypothesis:
the event schedule and service primitive here are an abstract admissible
model, not the prime-power schedule and archimedean reservoir of the zeta
function. Its precise conclusion is that those already-proved structural
conditions do not themselves control the intervening area \(J_q\).
