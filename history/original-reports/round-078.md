## Round 78 — the Xi-kernel log-concavity manuscript proves at most a TP2 condition, and its global tail step is not closed

I audited the version-2 preprint [*On the Log-Concavity of the Riemann Xi
Kernel*](https://www.preprints.org/manuscript/202604.0159) and its
[verification script](https://github.com/gershonavi/xi-log-concavity/blob/main/verify.py).
The paper itself correctly states that log-concavity is only a necessary
condition and that the passage from \(\mathrm{TP}_2\) to
\(\mathrm{TP}_\infty\) remains open. Therefore this route does not prove RH.
There is also a specific gap in the claimed analytic proof of the
log-concavity statement.

### I. The claimed conclusion is weaker than RH

The manuscript's Theorem 1 is
\[
 Q_\Phi(u):=\Phi''(u)\Phi(u)-\Phi'(u)^2<0.
\tag{78.1}
\]
This is strict log-concavity, or \(\mathrm{TP}_2\). The source explicitly
states that RH requires the stronger \(\mathrm{TP}_\infty\) condition and
that higher-order inequalities remain open. A second-order Turán inequality
cannot be promoted to the full Laguerre--Pólya property without an additional
argument.

### II. The relative derivative bounds used in the analytic proof cannot hold on the stated domain

For the paper's single-term function, constants do not affect the argument,
so write
\[
\phi_1(u)=\pi e^{5u/2}\bigl(2\pi e^{2u}-3\bigr)e^{-\pi e^{2u}},
\qquad x=\pi e^{2u}.
\tag{78.2}
\]
After removing positive factors, \(\phi_1\) is
\[
 x^{5/4}(2x-3)e^{-x}.
\]
The equation \(\phi_1'(u)=0\) reduces exactly to
\[
 8x^2-30x+15=0.
\tag{78.3}
\]
Its root with \(x\ge\pi\) is
\[
 x=\frac{15+\sqrt{105}}8,\qquad
 u=\frac12\log\!\left(\frac{15+\sqrt{105}}{8\pi}\right)
 \approx0.002266979577835944.
\tag{78.4}
\]
Likewise, \(\phi_1''(u)=0\) reduces to
\[
 32x^3-224x^2+330x-75=0,
\tag{78.5}
\]
whose root with \(x\ge\pi\) gives
\[
 u\approx0.237301534812532055.
\tag{78.6}
\]
Consequently, the manuscript's assertion that analogous estimates such as
\[
 \frac{|R'(u)|}{|\phi_1'(u)|}\le\varepsilon,\qquad
 \frac{|R''(u)|}{|\phi_1''(u)|}\le\varepsilon
\tag{78.7}
\]
hold throughout \(u\ge0\) cannot be true as written: the denominators vanish
at (78.4) and (78.6), while the corresponding tail numerators are not shown
to vanish there. The proof would need uniform absolute estimates that remain
valid at those points, followed by an explicit comparison with
\(|Q_{\phi_1}|\).

The paper's alternative argument does not supply that replacement. It gives
tail values at \(u=0\), then asserts that the ratio improves for every
\(u>0\), but it does not derive a uniform bound for all derivative cross terms.
The public verify.py script certifies the compact interval \([0,1/2]\) by
interval arithmetic and, for the entire region \([1/2,\infty)\), only
evaluates the tail comparison at \(u=1/2\); it contains no proof that the
comparison is monotone on the unbounded region. Thus even the claimed
analytic log-concavity proof has an unclosed global estimate, independently
of the larger \(\mathrm{TP}_2\)-to-\(\mathrm{TP}_\infty\) gap.

**Established:** the manuscript supplies a useful candidate \(\mathrm{TP}_2\)
calculation and an independently checkable compact interval computation.

**Failure / missing step:** its all-\(u\) derivative-relative estimate is
invalid at the explicit zeros (78.4) and (78.6), and the replacement
unbounded-region estimate is not supplied.

**Remaining load-bearing statement:** prove all higher-order total-positivity
inequalities, or another theorem that directly forces every zero of
\(\Xi\) to be real. The manuscript does neither.

**RH status:** no unconditional proof has been produced.
