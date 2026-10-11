## Round 255 — A/B result: Part 3 supplies a verified smoothed-cost identity, while the capacity comparison remains open

Source audited: Rainer Andreas Mittermeier, *The Remaining Riemann-Hypothesis Tail: Exact Reserve Reduction and Smoothed von Mangoldt Bounds at Prime-Power Checkpoints — Part 3*,
[Zenodo record 22076071](https://zenodo.org/records/22076071), PDF SHA-256
74ee615e634490f8431bd6731411ef2e177025d1a00bcf2f35008506d77c6e26.
The source states explicitly that the all-event comparison \(J_q\le C_q\) is
still open. The exact identity defining the scalar cost can nevertheless be
closed independently.

### VERIFIED PROOF CHAIN addition

Let an active episode enter at \(a\), let \(s=\log q\) be a current
prime-power event, and let the intervening event times be \(\ell_i=\log n_i\)
with weights \(w_i=\Lambda(n_i)/\sqrt{n_i}\). Define
\[
M_a(t)=\sum_{a<\ell_i\le t}w_i,
\qquad
J_q=\int_a^s M_a(t)\,dt.
\]
The sum is finite on \([a,s]\), so finite-sum integration gives
\[
J_q=\sum_{a<\ell_i\le s}w_i(s-\ell_i)
=\sum_{x<n\le q}\frac{\Lambda(n)}{\sqrt n}\log\frac qn,
\qquad x=e^a.
\]
Every term is nonnegative, so \(J_q\ge0\).

There is also an exact classical integral form. Put
\(\psi(y)=\sum_{n\le y}\Lambda(n)\),
\(\Delta_x\psi(y)=\psi(y)-\psi(x)\), and
\[
f(y)=y^{-1/2}\log\frac qy.
\]
The Stieltjes measure \(d\psi\) has mass \(\Lambda(n)\) at each integer
\(n\), while \(f(q)=0\) and \(\Delta_x\psi(x)=0\). Stieltjes
integration by parts therefore gives
\[
J_q=\int_{(x,q]}f(y)\,d(\Delta_x\psi)(y)
=-\int_x^q\Delta_x\psi(y)f'(y)\,dy
=\int_x^q\frac{\Delta_x\psi(y)}{y^{3/2}}
\left(1+\frac12\log\frac qy\right)dy.
\]
This identity is unconditional and uses no assertion about zero locations.
It is a valid scalar compression of the intervening prime-power schedule and
is added to the VERIFIED PROOF CHAIN.

### Remaining RH load-bearing claim

The exact identity does not give the required upper bound
\[
J_q\le C_q
\]
at every recovery witness. The front-loading estimate and finite-spectral
envelopes are one-sided bounds that may leave positive slack; the source
gives no RH-independent theorem showing that any such bound fits inside
the moving capacity for all future witnesses. Hence the scalar identity
does not close the RH criterion.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步产生了一个已完整核验的 smoothed-cost 恒等式，但没有产生新的无条件 RH 证明进展。
