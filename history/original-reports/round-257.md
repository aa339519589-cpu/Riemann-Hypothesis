## Round 257 — A-result: the pre-event front-loading bound for \(J_q\) is exact

Keep the notation of Round 256. Let \(s=\ell_q\) be the current event,
let \(w_q\) be its positive weight, and write

\[
P_q^-:=\sum_{a<\ell_i<s}w_i=P-w_q,
\qquad
M_a(t):=P_0(a,t).
\]

For every \(t<s\), the events counted by \(M_a(t)\) are a subset of the
events strictly preceding \(s\), so \(0\le M_a(t)\le P_q^-\). The value at
the single endpoint \(t=s\) has no effect on the integral. Consequently,

\[
J_q=\int_a^sM_a(t)\,dt\le(s-a)P_q^-.
\]

The bound has an exact deficit. Each event \(\ell_i<s\) contributes to
\(M_a(t)\) on the interval \([\ell_i,s]\), whose length is
\(s-\ell_i\). Therefore

\[
J_q=\sum_{a<\ell_i<s}(s-\ell_i)w_i,
\]

and hence

\[
(s-a)P_q^- - J_q
=\sum_{a<\ell_i<s}(\ell_i-a)w_i\ge0.
\]

This is a complete unconditional front-loading estimate for the smoothed
cost. It does not imply \(J_q\le C_q\), because the exact capacity \(C_q\)
can be smaller than the one-sided envelope \((s-a)P_q^-\). Thus the
unresolved universal comparison remains

\[
J_q\le C_q
\quad\Longleftrightarrow\quad
V_q\ge0.
\]

The estimate is added to the VERIFIED PROOF CHAIN as an auxiliary theorem.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步产生了一个已完整核验的前置上界及其精确差值，但没有产生新的无条件 RH 证明进展。
