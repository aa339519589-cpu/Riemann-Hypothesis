## Round 165 — a purported Bombieri-extrema proof fails at its first logarithmic asymptotic

I audited the current version of Xiao Lin's manuscript *A Proof of the
Riemann Hypothesis Using Bombieri's Equivalence Theorem* (arXiv:2108.02851v26,
26 August 2026):

<https://arxiv.org/pdf/2108.02851>

The load-bearing Lemma 1 asserts, for large \(y\),

\[
 \frac{U^{(n+k)}(y)}{U^{(n)}(y)}
 =\left(-\frac{\pi}{8}\right)^k\!\left(1+O(y^{-1})\right),
\tag{165.1}
\]

and derives this by writing

\[
 \log U(y)=\log \xi\!\left(\frac{1+iy}{2}\right)
\tag{165.2}
\]

and differentiating an asymptotic formula for \(\log\xi(s)\).  Here the
paper's normalization is \(U(y)=\Xi(iy)=\xi((1+iy)/2)\).  Equation (165.2)
cannot hold as a global large-\(y\) logarithmic asymptotic on the critical
line: \(U\) is real and has infinitely many unbounded real zeros.  Near any
zero \(y_0\) of order \(m\),

\[
 \frac{U'(y)}{U(y)}=\frac{m}{y-y_0}+O(1),
\tag{165.3}
\]

so the logarithmic derivative has a pole.  For arbitrarily large \(y_0\),
there are points arbitrarily close to \(y_0\) at which \(U'(y)\ne0\), and the
left side of (165.1) with \(n=0,k=1\) is then unbounded, whereas its claimed
right side is bounded and tends to \(-\pi/8\).  If \(U(y_0)=0\), the displayed
logarithm is itself undefined; choosing a local branch away from the zero does
not give a uniform estimate across such neighborhoods.

Thus the standard order-one growth estimate for \(\log\xi(s)\), even when
used on zero-free subdomains with a chosen branch, does not imply the
derivative-ratio estimate uniformly along a line containing zeros.  The later
claims that all critical-line zeros are simple and that every intervening
extremum has the required sign depend on (165.1), so the proposed proof does
not supply the missing Bombieri condition or an RH proof.

**Established:** this independent candidate has a concrete fatal gap before
its Cauchy--Riemann argument; its advertised conclusion cannot be imported as
an unconditional proof.

**Remaining load-bearing statement:** prove the extrema sign condition by a
valid global argument, or close one of the independent Weil/spectral bridges
already isolated above.  Neither has been established here.

**RH status:** no unconditional proof has been produced.
