## Round 109 — dense range of the critical synthesis is unconditional, but exact weighted range is not

The positive-proportion theorem audited in Round 104 gives a useful unconditional upgrade to the functional-analytic part of the Bombieri route.  Let \(\Gamma_C\) be the set of distinct ordinates of simple zeros on the critical line.  The theorem
\[
\text{at least }\left(\frac23-o(1)\right)N(T,2T)
\text{ zeros are simple and on the line}
\]
([arXiv:2608.13637](https://arxiv.org/abs/2608.13637)) together with the Riemann--von Mangoldt formula implies
\[
N_C(T)\gg T\log T.
\tag{109.1}
\]
Only a fixed positive proportion is needed here.

For the operator \(A\) in (103.1), take \(g\in L^2(I)\) and
\[
G_g(z)=\int_I g(u)e^{izu}\,du.
\]
This is an entire function of finite exponential type.  The elementary Cauchy--Schwarz estimate on the bounded interval \(I\) gives
\[
|G_g(x+iy)|\leq |I|^{1/2}\|g\|_2\,e^{R|y|}
\]
for some \(R<\infty\) depending only on \(I\).  Jensen's formula therefore gives, for every nonzero \(G_g\),
\[
n_{G_g}(T)=O_I(T),
\tag{109.2}
\]
where \(n_{G_g}(T)\) counts zeros in \(|z|\leq T\).  Since (109.1) is superlinear, \(G_g(\gamma)=0\) for every \(\gamma\in\Gamma_C\) forces \(G_g\equiv0\).  Fourier uniqueness then forces \(g=0\).  Consequently
\[
\ker A^*=\{0\},
\qquad
\overline{\operatorname{Ran}A}=L^2(I)
\tag{109.3}
\]
holds unconditionally; the earlier finite-exception assumption is not needed for this density statement.

The same operator remains Hilbert--Schmidt because
\[
\sum_{\gamma\in\Gamma_C}\frac1{\frac14+\gamma^2}<\infty.
\]
It has infinite rank, since every finite collection of distinct exponentials is linearly independent on an interval.  Hence it is compact and cannot have closed dense range: if its range were closed, (109.3) would make it onto \(L^2(I)\), which is impossible for a compact operator onto an infinite-dimensional Hilbert space.

This sharpens the diagnosis rather than closing it.  Every \(h\in L^2(I)\) is approximable by critical weighted sums, but the particular off-line packet must belong to the nonclosed exact range.  Equivalently, the dual estimate (103.6), or the spectral integrability condition (25.2), is still required.  The positive-proportion theorem supplies no lower sampling bound with the weights \(d_\gamma^{-1}\).

**Established:** unconditional dense range of the critical weighted synthesis, using only a positive-proportion theorem and finite-exponential-type zero counting; compactness and nonclosedness of the same operator.

**Failure / missing step:** exact weighted range membership or nonmembership for an off-line packet; no weighted coercive/sampling inequality follows from density.

**Route decision:** use (109.3) to remove density as a false obstruction and focus the Bombieri proof exclusively on the nonclosed-range estimate (103.6)/(25.2), together with the finite-section rate.

**RH status:** no unconditional proof has been produced.
