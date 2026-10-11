## Round 199 — A/B result: the stated graph-energy diagonal asymptotic is false

In Section 5 of Velez v5, the diagonal coefficient is
\[
W_X=\sum_{p^k\le X}(\log p)p^{-k/2},
\]
and the source states \(W_X\sim\log X\).  The \(k=1\) part alone has a
different asymptotic.  Writing
\(\theta(x)=\sum_{p\le x}\log p\), partial summation gives
\[
\sum_{p\le X}\frac{\log p}{\sqrt p}
=\frac{\theta(X)}{\sqrt X}
+\frac12\int_2^X\frac{\theta(t)}{t^{3/2}}\,dt.
\]
The prime number theorem \(\theta(t)\sim t\) therefore implies
\[
\sum_{p\le X}\frac{\log p}{\sqrt p}\sim2\sqrt X.
\]
The \(k=2\) contribution is \(O(\log X)\), and the sum of the
\(k\ge3\) contributions is bounded, since
\[
\sum_p\sum_{k\ge3}(\log p)p^{-k/2}
\le
\sum_p\frac{(\log p)p^{-3/2}}{1-p^{-1/2}}<\infty.
\]
Consequently
\[
W_X\sim2\sqrt X,
\]
not \(\log X\).

Thus the stated asymptotic used to describe the finite graph-energy
renormalization is false.  The exact identity
\[
E_{P_X}(F)=2W_X\|F\|_2^2
-2\sum_{p^k\le X}(\log p)p^{-k/2}C_F(k\log p)
\]
still shows that the raw graph energy has a divergent diagonal, but it does
not establish the source's finite-part replacement by \(D_\infty(F)\).
That replacement and the Proposition 6.1 Gram identity remain unproved.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
