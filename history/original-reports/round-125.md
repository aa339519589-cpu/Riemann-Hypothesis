## Round 125 — rapid-decay local kernels show that coefficient growth alone cannot restore uniqueness

The local nonuniqueness obstruction is stronger than the earlier boundary
corrected examples.  It persists with a pure real-frequency system and with
coefficients decreasing faster than every power.

Fix \(0<a<\pi\), \(I=(-a,a)\), and choose a nonzero
\(2\pi\)-periodic \(C^\infty\) function \(\psi\) whose support is contained in
the complementary arc \((a,\pi)\) (with the endpoints understood
periodically).  Its Fourier coefficients

\[
 c_n=\frac1{2\pi}\int_{-\pi}^{\pi}\psi(u)e^{inu}\,du
\]

satisfy, for every \(m\geq1\),

\[
 |c_n|\leq C_m(1+|n|)^{-m},
 \tag{125.1}
\]

by repeated integration by parts.  In particular the Fourier series
\(\psi(u)=\sum_{n\in\mathbb Z}c_ne^{-inu}\) converges absolutely and uniformly.
Put

\[
 d_n=n^2+\tfrac14,\qquad w_n=d_nc_n.
\]

Choosing \(m\geq4\) in (125.1) gives \(w\in\ell^2(\mathbb Z)\), and the exact
weighted synthesis identity is

\[
 \sum_{n\in\mathbb Z}\frac{w_n}{n^2+\tfrac14}e^{-inu}
 =\psi(u)=0\qquad(u\in I),
 \tag{125.2}
\]

while \(w\ne0\).  The coefficient sequence is not merely admissible for the
Bombieri weight; it has arbitrarily strong polynomial decay.

This is a model on \(\mathbb Z\), not a statement about the actual critical
ordinates.  Its exact conclusion is narrower and useful: no uniqueness
theorem based only on real frequencies, the factor
\((\tfrac14+n^2)^{-1}\), \(\ell^2\) control, local vanishing, and any finite
order coefficient-decay estimate can exclude the zero-collapse relation.
Any successful finite Section-11 exclusion must therefore use an
arithmetic property of the actual zeta ordinates or the provenance of the
selected finite eigenvectors.  A general nonharmonic-series uniqueness
theorem for a series vanishing on the whole real line would not apply to the
local identity (125.2).

**Established:** the abstract local weighted coefficient class contains
nonzero, rapidly decaying pure-critical kernels.

**Remaining load-bearing statement:** prove a zeta-specific range
nonmembership/selected-branch estimate; coefficient decay and local
completeness by themselves are insufficient.

**RH status:** no unconditional proof has been produced.
