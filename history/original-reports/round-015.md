## Round 15 — the claimed polar-term scaling is contradicted by the constant mode

The same proposed route also claims that the even-sector norm of the polar
term is \(O(\log\lambda)\). This is incompatible with the exact semilocal
formula.

Write \(L=2\log\lambda\), use the coordinate \(y=\log(\lambda u)\in[0,L]\),
and take the normalized even constant mode

\[
V_0(u)=L^{-1/2}.
\]

From the pole block of the Weil form,

\[
\Pi_\lambda(f,f)=2\operatorname{Re}
 \left(\widehat f(i/2)\,\overline{\widehat f(-i/2)}\right),
\]

the two evaluations on \(V_0\) are equal and exactly

\[
\widehat V_0(i/2)=\widehat V_0(-i/2)
=\frac{4\sinh(L/4)}{\sqrt L}.
\]

Consequently,

\[
\langle V_0,\Pi_\lambda V_0\rangle
=\frac{32\sinh^2(L/4)}{L}
=\frac{8e^{L/2}}{L}-\frac{16}{L}+O(e^{-L/2}/L).
\]

Since \(V_0\) is normalized,

\[
\|\Pi_\lambda\|_{\mathrm{even}}
\geq \frac{32\sinh^2(L/4)}{L}
\asymp \frac{\lambda}{\log\lambda},
\]

not \(O(\log\lambda)\). The same value is the \((0,0)\) entry of the exact
pole matrix in the source calculation.

The numerical script underlying the contrary scaling uses the same prefactor
\(\lambda^{-1/2}\) for both \(\widehat V_n(i/2)\) and
\(\widehat V_n(-i/2)\). In the \(y\)-coordinate the second evaluation carries
\(\lambda^{+1/2}\), and the orthonormal basis also carries \(L^{-1/2}\). The
constant mode already detects the missing factor: the exact pole energy grows
like \(e^{L/2}/L\). Finite-dimensional output that shows \(O(L)\) therefore
does not certify the continuum polar operator or the asserted eventual
spectral-gap estimate.

This is separate from the noncompactness failure in Round 14. Even if one
replaced the prime operator by a valid compact surrogate, the proposed bound
used to dominate the polar term would still need to be replaced by an estimate
of the correct \(\lambda/\log\lambda\) scale (or by a genuine cancellation in
the *full* Weil operator, not in the polar term alone). The claimed
Krein–Rutman closure remains unavailable.

### Round 15 status

**Established:** the exact constant-mode evaluation gives a lower bound
\(\|\Pi_\lambda\|_{\rm even}\ge 32\sinh^2(L/4)/L\), contradicting the claimed
\(O(\log\lambda)\) polar scaling.

**Not established:** a valid all-scale simplicity/evenness theorem, ground-state
identification, or an unconditional proof of RH.
