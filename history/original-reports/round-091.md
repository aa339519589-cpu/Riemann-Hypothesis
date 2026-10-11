## Round 91 — shrinking the prime scale for higher moments does not automatically bootstrap the finite certificate to RH

A possible continuation of the two-thirds argument is to evaluate higher prime-side moments. The cited 2026 paper records the relevant range: a \(k\)-th moment evaluation is available in the diagonal regime only when
\[
X^{k}\leq T^{2-\varepsilon},
\tag{91.1}
\]
whereas the one-window rank--trace certificate uses \(X\asymp T\) (and hence \(L=\log X\asymp\log T\)). At that scale, only the first nontrivial moment lies in the stated diagonal range.

The natural attempted workaround is to take \(X=T^\theta\) with \(\theta\leq(2-\varepsilon)/k\). But the same construction fixes the modulation spacing at
\[
h=\frac{2\pi}{L},\qquad L=\log X,
\tag{91.2}
\]
so the number of translates needed to cover a vertical window of length \(T\) is
\[
d\asymp \frac{T}{h}\asymp T\log X
=\theta\,T\log T.
\tag{91.3}
\]
The number of zeros in \([T,2T]\) is
\[
N(T,2T)\asymp T\log T.
\tag{91.4}
\]
Thus the high-moment choice \(\theta\asymp 1/k\) gives a compression whose dimension is only \(O(N/k)\). Its moment information concerns a shrinking subspace of the full zero packet; it does not yield a positive-definiteness statement for the remaining \(1-O(1/k)\) dimensions. Letting \(k\to\infty\) makes the available compression fraction tend to zero, not one.

This does not rule out a substantially different multiscale construction: one would need a compatible family of windows, control of all cross-scale terms, and a rank/inertia inequality that transfers the small-\(X\) moment data back to the entire \([T,2T]\) zero space. None of those transfer estimates follows from (91.1), and the source's sharpness result for the bandwidth-one certificate remains in force for the single-scale argument.

**Established:** the prime-side diagonal range and the logarithmic modulation-grid scaling; the one-scale rank--trace method has a finite bandwidth ceiling below \(1\).

**Failure / missing step:** the naive higher-moment bootstrap trades moment order for compression dimension and supplies no mechanism eliminating the residual off-line subspace.

**Route decision:** keep higher moments as a possible auxiliary branch only if a cross-scale transfer theorem is first proved. The immediate target remains a full Weil-positivity or exact weighted-range theorem that controls all dimensions simultaneously.

**RH status:** no unconditional proof has been produced.
