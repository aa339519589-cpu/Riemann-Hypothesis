## Round 146 — a symmetric high-frequency model with \(T\log T\) critical density

The Round-143 toy model can be made hostile to the usual proposed repairs.
Fix \(0<T<\pi\), choose a real \(C^\infty\) cutoff \(\chi\) supported in
\((-\,\pi,\pi)\) and equal to \(1\) on \([-T,T]\), and let

\[
 O_N=\{\pm(N+i/N),\ \pm(N-i/N)\}.
\]

This is the same fourfold symmetry as the centered zeta zero parameter
\(\gamma\).  Give every \(\eta\in O_N\) the coefficient \(w_\eta=1\), put
\(d_\xi=\tfrac14+\xi^2\), and define

\[
 P_N(u)=\sum_{\eta\in O_N}\frac{1}{d_\eta}e^{-i\eta u},
 \qquad
 g_N(u)=\chi(u)P_N(u),
\tag{146.1}
\]

with \(g_N\) extended periodically with period \(2\pi\).  Let

\[
 g_N(u)=\sum_{n\in\mathbb Z}a_{n,N}e^{-inu}
\]

be its Fourier series and set

\[
 w_{n,N}=-d_n a_{n,N}\quad(n\in\mathbb Z).
\tag{146.2}
\]

Because \(g_N\) is \(C^\infty\), the sequence
\((w_{n,N})_{n\in\mathbb Z}\) is in \(\ell^2\).  On \([-T,T]\), (146.1) gives

\[
 \sum_{\eta\in O_N}\frac{w_\eta}{d_\eta}e^{-i\eta u}
+ \sum_{n\in\mathbb Z}\frac{w_{n,N}}{d_n}e^{-inu}
 =P_N(u)-g_N(u)=0.
\tag{146.3}
\]

To make the critical model have the same coarse counting order as the zeta
zeros, enlarge \(\mathbb Z\) by, for each integer \(k\ge2\), the distinct
points

\[
 k+\frac{j}{\lfloor\log(k+2)\rfloor+1},
 \qquad 1\le j\le\lfloor\log(k+2)\rfloor,
\tag{146.4}
\]

and add their negatives.  The resulting real symmetric set has
\(N_C(R)\asymp R\log R\), but all added coordinates are assigned coefficient
zero.  Thus the relation (146.3) survives unchanged even after imposing
zeta-like symmetry and counting density.

The weighted critical mass remains uniformly bounded as \(N\to\infty\).
Indeed, Parseval identifies it, up to the fixed Fourier normalization, with
\(\|(\tfrac14-\partial_u^2)g_N\|_{L^2(-\pi,\pi)}^2\).  Since
\(d_\eta\asymp N^2\), the four terms in \(P_N\) have size \(O(N^{-2})\);
two derivatives restore at most \(N^2\).  The cutoff derivative terms are
smaller, so

\[
 \sum_{n\in\mathbb Z}|w_{n,N}|^2=O(1).
\tag{146.5}
\]

The four off-line coordinates have total squared mass \(4\).  After
normalization, a fixed positive fraction of the mass therefore remains
off-line, while the height tends to infinity and
\(|\operatorname{Im}(N+i/N)|=1/N\to0\).

This model is not a zeta zero set and does not satisfy Bombieri's finite
eigenvector provenance.  Its role is narrower and exact: fourfold symmetry,
the critical \(T\log T\) counting scale, polynomially weighted
\(\ell^2\)-control, and local compactness still do not imply the required
range exclusion.  The missing theorem must use the actual zeta arithmetic or
the exact finite-section eigenvector equations, not just these coarse
properties.

**Established:** the hostile escape model survives the standard symmetry,
counting-density, and weighted-\(\ell^2\) repairs.

**Remaining load-bearing statement:** derive a zeta-specific estimate from the
finite-section eigenvector equation that prevents this kind of high-frequency
local cancellation.  No such estimate has been established.

**RH status:** no unconditional proof has been produced.
