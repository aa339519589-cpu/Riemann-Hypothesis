# Independent mathematical referee: projected energy metrics

Date: 2026-10-13. I checked [the report](REPORT.md), its projected-core argument, its complete
prime sums, and the positive-combination extension against the public
reflected-energy report and the odd operator-domain report. The proof
passes. The projection estimate is uniform over the closed theta-jet
span, and the nonsymmetry conclusion is stated at the right level: it is
a nonreal diagonal pairing in the projected core relation, so no
symmetric operator can contain that relation. No injectivity assertion
or zero-counting theorem is needed. This result concerns the proposed
metrics only; it proves no sign for the original Weil form.

## Source representatives and closed-span estimates

The forms use all labels \(n\ge2\), with
\(d_n=\log n\) and \(\alpha_n=\Lambda(n)/\sqrt n\). The source
coordinates \(g=\psi r\) give the exact reflected polarization
\[
 N_s[g,h]
 =2\int_0^\infty V_N(x)\overline{g(x)}h(x)\,dx
  -2\sum_{n\ge2}\alpha_n\int_0^{d_n}
          \overline{g(x)}h(d_n-x)\,dx,\qquad
 V_N=L/\psi,
\]
as in the public reflected-energy report. Its diagonal coefficient and
the cross-term coefficient in the candidate are correct.

For an odd source, \(\ell(g)=2\int_0^\infty s_0g\). Expanding the positive
pole square gives
\[
 P_{\rm pole}[g/\psi]
 =\int_0^\infty \frac{s_0}{\psi}|g|^2\,dx-2|\ell(g)|^2.
\]
Thus neutral finite jet combinations obey
\(\int W|g|^2\le N[r]\), with \(W=s_0/\psi\), and also
\(P_\Gamma[r]\le N[r]\), by the exact mixed null-source identity and
positivity of the three components of \(P\). The factors agree with
\(\int_0^\infty\psi s_0=1/8\) and the full-line normalization of
\(\ell\).

These estimates extend to the closed jet span: an \(N\)-Cauchy sequence
of finite neutral combinations is Cauchy in \(L^2(Wdx)\); the moment is
continuous since \(\int s_0^2/W=\int\psi s_0<\infty\). Local \(L^2\)
convergence of ratios identifies every reflected edge gradient almost
everywhere. Fatou applies to the nonnegative Gamma kernel. This gives
the needed source representative and closed-span bounds without extending
a separate \(P-N\) subtraction to the original maximal source domain.

On each compact interval away from zero, the pole estimate bounds the
ratio in \(L^2\), and the Gamma kernel controls increments by
\(|x-y|^{-1}\). The resulting localized Fourier multiplier grows like
\(\log(2+|t|)\); its high-frequency tail is uniformly small, and each
bounded-frequency restriction from compact support is Hilbert--Schmidt.
So the source unit ball is locally relatively compact in \(L^2\). This
is the needed uniform compactness for all vectors of the closed jet span,
not merely for finite jet truncations.

For the cross-term tail, if \(\phi\) is supported in
\(I=(a,b)\subset(0,\log2/2)\), an active label has
\(e^{x+a}<n<e^{x+b}\). Counting all integers and using
\(\Lambda(n)\le\log n\) yields
\[
 \left|\sum_{n\ge2}\alpha_n\phi(d_n-x)e^{it(d_n-x)}\right|
 \le C_\phi(1+x)e^{x/2}.
\]
Weighted Cauchy--Schwarz with \(W=s_0/\psi\) leaves the tail
\[
 C_\phi\left(\int_R^\infty
 (1+x)^2e^x\frac{\psi(x)}{s_0(x)}\,dx\right)^{1/2},
\]
which tends to zero by the stated theta tail. For \(x\le R\) only
finitely many labels occur, and their image intervals begin no lower
than \(\log2-b>0\). Thus local compactness and uniform
Riemann--Lebesgue apply on every interval used. This verifies the
projection decay for the entire closed span and for amplitudes
\(\chi,\chi',\chi''\).

## Nonreal projected pairing

The complete sum defining \(L\) is locally normally differentiable near
zero, because all labels are active there and the theta terms decay
faster than exponentially in \(n\). With \(L(0)>0\),
\(\psi(x)=c_\psi x+O(x^3)\), and the corresponding derivative
expansions, the quotient satisfies
\[
 V_N'(x)=-\frac{L(0)}{c_\psi x^2}+O(1)<0
\]
on a short interval. The candidate correctly requires the derivative
remainder for \(L'\) in this calculation.

For \(g_t=\chi e^{itx}\) supported in that interval, the reflected
cross term vanishes when paired with any of
\(\chi^{(j)}e^{itx}\), since the support sum lies below \(\log2\).
Consequently
\[
 \operatorname{Im}N_s[g_t,g_t'']
 =4t\int_I V_N\chi\chi'\,dx
 =-2t\int_I V_N'\chi^2\,dx>0.
\]
With the conjugate-linear-first-slot convention, the \(-t^2\) term in
the projected carrier identity is real exactly. The \(2it\) projection
correction is \(o(t)\) because both relevant projected amplitudes tend
to zero; the last correction is \(o(1)\). The limit in the candidate
therefore has the correct sign and factor. A nonreal diagonal pairing
rules out every symmetric operator whose graph contains all the
projected core pairs, even if those pairs have not separately been shown
to define a single-valued operator. The real and imaginary parts of the
carrier also give the equivalent two-real-test obstruction.

## Positive combinations

For \(M=a_0P+b_0N\), \(a_0,b_0\ge0\), \(a_0+b_0>0\), the direct-sum
gradient \((\sqrt{a_0}\nabla_P,\sqrt{b_0}\nabla_N)\) has the right
normalization. The jet/core mixed identity gives
\[
 \langle\nabla_M s,\nabla_M r\rangle_M
 =(a_0+b_0)N(s,r),\qquad
 \|\nabla_M s\|_M=\sqrt{a_0+b_0}\,\|\nabla_N s\|_N
\]
on the jet span. Taking the supremum over its unit ball proves the
candidate's exact projection scaling
\[
 \|P_{S_M}\nabla_M r\|_M
 =\sqrt{a_0+b_0}\,\|P_{S_N}\nabla_N r\|_N.
\]
This remains valid at either endpoint \(a_0=0\) or \(b_0=0\).

Finally, the compact odd-source commutation of the polar-inclusive
\(\mathfrak A=P-N\), established in the public operator-domain report,
implies
\[
 P_s[g,g'']-P_s[g'',g]
 =N_s[g,g'']-N_s[g'',g].
\]
Both forms are Hermitian, so their imaginary diagonal pairings agree.
It follows that
\(\operatorname{Im}M_s[g,g'']=(a_0+b_0)
\operatorname{Im}N_s[g,g'']\), with no positivity assumption on
\(\mathfrak A\). Combining this identity with the scaled projection
decay yields exactly the candidate's limit
\[
 \lim_{t\to\infty}\frac1t
 \operatorname{Im}\langle Q_Mv_M(r_{\chi,t}),
                 Q_Mv_M(\mathcal B_\psi r_{\chi,t})\rangle_M
 =-2(a_0+b_0)\int_I V_N'(x)\chi(x)^2\,dx>0.
\]
I find no factor or domain gap in this extension. The conclusion is
limited to nonsymmetry of these projected metrics; it does not imply a
negative vector for \(P-N\), a failure of the Weil inequality, or RH.
