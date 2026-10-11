## Round 110 — zero-count density alone cannot imply weighted range exclusion

To stress-test the strengthened density argument, construct an explicit
high-density model.  For every integer \(n\ge2\), put
\[
L_n=\lfloor\log n\rfloor
\]
and add the \(L_n\) points \(n+j/(L_n+1)\), \(1\le j\le L_n\), together
with their negatives, to \(\mathbb Z\).  Call the resulting symmetric
discrete set \(\Lambda_{\mathrm{hd}}\).  The added points lie in disjoint
unit intervals, and
\[
N_{\Lambda_{\mathrm{hd}}}(T)
=2T+2\sum_{2\le n\le T}\lfloor\log n\rfloor+O(\log T)
=2T\log T+O(T).
\tag{110.1}
\]
Thus this model has the same superlinear \(T\log T\) order that produced
(109.1).

Let \(I=(-a,a)\) with \(0<a<\pi\), and let \(b\ne0\).  Choose a smooth
\(2\pi\)-periodic function \(G\) that agrees with \(e^{bu}\) on \(I\).
Its Fourier coefficients \(c_n\) decrease faster than every power of
\(|n|\).  For the weighted synthesis over \(\Lambda_{\mathrm{hd}}\), set
\[
q_n=\sqrt{\tfrac14+n^2}\,c_n\quad(n\in\mathbb Z),
\qquad q_\lambda=0\quad(\lambda\in\Lambda_{\mathrm{hd}}\setminus\mathbb Z).
\]
Then \(q\in\ell^2(\Lambda_{\mathrm{hd}})\) and
\[
\sum_{\lambda\in\Lambda_{\mathrm{hd}}}
\frac{q_\lambda}{\sqrt{\tfrac14+\lambda^2}}e^{-i\lambda u}
=\sum_{n\in\mathbb Z}c_ne^{-inu}
=G(u)
=e^{bu}
=e^{-i(ib)u}\qquad(u\in I).
\tag{110.2}
\]
Therefore the off-real exponential \(e^{-i(ib)u}\) lies in the exact
weighted range even though the frequency set has \(T\log T\) density, the
weighted synthesis is Hilbert--Schmidt, and its range is dense and nonclosed.

This is not a counterexample involving the actual zeta ordinates.  It is a
decisive hostile check on the proposed inference: (109.1), finite exponential
type, completeness, compactness, and the algebraic weight do not by
themselves exclude an off-line packet.  Any successful exclusion of (103.6)
must use additional arithmetic information specific to the critical
ordinates, not merely their counting function or density.

**Established:** an explicit \(T\log T\)-density weighted exponential model
with exact off-real range membership.

**Failure / missing step:** no transfer from the model to the actual critical
ordinates; the required zeta-specific weighted sampling/nonmembership theorem
remains unproved.

**Route decision:** retain (103.6)/(25.2) as the exact target and reject any
argument that invokes only superlinear density or unweighted completeness.

**RH status:** no unconditional proof has been produced.
