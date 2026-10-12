# Referee review: averaged principal series and contraction

## Verdict and scope

**The §6 Dirichlet-series construction and triangular contraction are valid as conditional statements.** The exact auxiliary average, the original and core slot factors, coefficient-norm estimates, convolution identity, and allowance for the jumps in \(k\) all check. The important qualification is in transferring a bound from the *literal principal row* to the double-residue signal: if the safe contour line is \(\sigma_{\rm safe}\) and its power-error saving is \(m_0\), then the error is

\[
O\!\left(Z^{\sigma_{\rm safe}-c_{\rm exp}-m_0}\right).
\]

It supports contraction at \(\sigma_*\) only if

\[
\boxed{\sigma_{\rm safe}-m_0\le \sigma_* .}
\]

The statement that the row error is \(O(Z^{\sigma_*-c_{\rm exp}-m})\) is correct when the safe line itself is chosen to be \(\sigma_*\), or when a separate margin gives the boxed inequality. It does not follow for arbitrary \(\sigma_*=1/2+\delta\) from a fixed known safe line above (for example) \(0.875\). The local coefficient contraction remains valid for any fixed \(\sigma_*>1/2\); it is this external row-to-signal error that restricts its application.

This review does not supply the still-missing matching averaged low bound for the literal principal row or the whole probe, and therefore does not close the high/low comparison or prove RH.

## Exact auxiliary series

From (10), the normalized local factor is exactly

\[
\frac{h_p}{c_p}=\frac{1-r_p}{1-\alpha_p-\beta_p},\quad
c_p=\frac{P-1}{P+1},\quad
\alpha_p=(1-P^{-1})P^{-s},\quad
\beta_p=\kappa(p)P^{1-6s},\quad
r_p=\kappa(p)P^{2-6s}.
\]

At a fixed \(\sigma_*>1/2\), the coefficient norm of \(\alpha_p+\beta_p\) is at most \(P^{-\sigma_*}+P^{1-6\sigma_*}<0.4\) for \(P\ge7\); at \(P=7\) the limiting worst case is below \(0.4\), and it decreases with \(P\) and \(\sigma_*\). Thus the geometric expansion of the denominator is absolutely convergent in the Dirichlet coefficient norm. The numerator difference \(\alpha_p+\beta_p-r_p\) has norm \(O(P^{-\sigma_*})\), since \(P^{1-6\sigma_*},P^{2-6\sigma_*}\le P^{-\sigma_*}\). The constant coefficient is exactly \(c_p\), and every nonconstant local index is at least \(P\).

Averaging the finite products with the actual positive elementary-symmetric probabilities is legitimate by the triangle inequality. It gives the constant

\[
a_{R,0}=\mathbb E_J\prod_{p\in J}c_p\ge(1-2/P_0)^k\to1,
\]

and the nonconstant coefficient tail is at most

\[
a_{R,0}\big[(1+CP_0^{-\sigma_*})^k-1\big].
\]

Equal integer indices from different prime ideals are combined only after expansion and are correctly paid for by the triangle inequality. The first nonconstant support is at \(n\ge P_0\). With \(P_0=(\log R)^{64}\) and \(k\ll \log R/\log\log R\), the relative tail is \(O((\log R)^{1-64\sigma_*}/\log\log R)=o(1)\) for every fixed \(\sigma_*>1/2\).

## Original and core slot factors

Equations (35) and (36) match the separate source formulas. In the original case, the numerator of \(B_{p,\rm orig}+1\) has indices \(P^5,P^6,P\), with coefficient norms bounded by

\[
P^{2-5\sigma_*}+P^{1-6\sigma_*}+P^{-\sigma_*}\le3P^{-\sigma_*}.
\]

The core numerator has indices \(P,P^6\) and norm at most \(2P^{-\sigma_*}\). In each case the denominator is the same geometric-series factor \(1-\alpha_p-\beta_p\), and \(U_{p,\star}=-B_{p,\star}\) has constant coefficient one. This preserves the original source's \(-P^{-1}\) compensation and uses the core marked sum separately, as required.

The normalized slot weights are nonnegative and sum to one, so averaging within each slot preserves constant one and the \(O(P_i^{-\sigma_*})\) tail. The product across slots is exact because the physical tuple weights factor. For fixed \(\lambda>0\), auxiliary prime norms are \(O((\log Z)^{64})\) while physical slot norms are \(\gg Z^{\ell_i}\); hence the supports are disjoint for sufficiently large \(Z\). The full series

\[
\mathcal A_{Z,\star}(s)=\mathcal M_{R(Z)}(s)V_{\star,Z}(s)
\]

therefore has constant \(a_{R(Z),0}\), relative tail \(\theta_Z=O(kP_0^{-\sigma_*}+\sum_iP_i^{-\sigma_*})=o(1)\), and no nonconstant support below \(P_0\). This is valid for both markers and remains uniform at jumps of \(k\); no continuity in \(R\) is needed. For all large \(Z\), one fixed \(\theta<1\) and one \(a_*>0\) work. The resulting absolute-series bound proves the averaged numerator is holomorphic and nonzero on \(\Re s\ge\sigma_*\).

## Convolution, contraction, and small arguments

On \(\Re s=2\), the coefficient series is absolutely convergent, and the Gaussian height factor makes the fixed kernel integrable. Fubini therefore yields exactly

\[
f_{R,Z,\star}(Z)=\sum_{n\ge1}a_{Z,\star}(n)n^{-c_{\rm exp}}f(Z/n).
\]

The exponent identity \(C(s)=s-c_{\rm exp}\) gives the factor \(n^{-\sigma_*}\) in the contraction estimate. Isolating the \(n=1\) term and taking the running supremum proves the stated geometric contraction. It is pointwise in \(Z\), so the floor in \(k\), varying \(R=Z^\lambda\), and varying slot distributions do not invalidate it.

The fixed-signal small-\(T\) bound is sound for the intended \(1/2<\sigma_*<1\): moving the inverse Mellin contour right to any \(\sigma'>2\) gives \(f(T)=O(T^{\sigma'-c_{\rm exp}})\) as \(T\downarrow0\), hence \(|f(T)|T^{-q}=O(T^{\sigma'-\sigma_*})\). For the lemma's more general wording with arbitrary \(\sigma_*>1/2\), specify \(\sigma'>\max(2,\sigma_*)\); then the same argument makes the exponent positive. Continuity handles the rest of every compact \(T\)-interval. This is a minor wording repair, not an obstruction in the stated application.

## Safe-line error and the valid descent

The comparison in the source §9 is made on a fixed safe line \(\sigma_{\rm safe}\). Its retained contour and finite-slot errors have the form

\[
O\!\left(Z^{C(\sigma_{\rm safe})-m_0}\right)
=O\!\left(Z^{\sigma_{\rm safe}-c_{\rm exp}-m_0}\right),
\quad 0<m_0<\min\{\ell_y d_w,h\eta,\kappa_P\},
\]

with the slot term omitted when there are no slots. Suppose the literal averaged principal row has a separate low bound \(O(Z^{\sigma_{\rm low}-c_{\rm exp}})\). The exact double-residue signal is then bounded at exponent

\[
\sigma_{\rm transfer}=\max\{\sigma_{\rm low},\;\sigma_{\rm safe}-m_0\}.
\]

The coefficient contraction can be run at that fixed exponent whenever it exceeds \(1/2\). In particular, if the available row low bound is already at a chosen \(\sigma_*=1/2+\delta\), transfer to that exponent requires \(\sigma_{\rm safe}-m_0\le\sigma_*\). If only a safe-line-sized row bound is available, the contour error does not lower its exponent, and contraction transfers only the safe-line-sized bound.

There is a conditional abscissa-descent scenario. Let \(\beta_*>1/2\) be the supremum of the real parts of target zeta zeros, with \(\beta_*<1\), and suppose the reciprocal is holomorphic with the required polynomial-height bound on a safe line \(\sigma_{\rm safe}=\beta_*+\varepsilon<1\). If one can choose a fixed saving with

\[
\varepsilon<m_0<\beta_*-\tfrac12+\varepsilon,
\]

then \(\sigma_{\rm new}=\sigma_{\rm safe}-m_0\) lies strictly between \(1/2\) and \(\beta_*\). The full coefficient contraction is valid at \(\sigma_{\rm new}\), and the §9 error is exactly of the permitted order \(O(Z^{\sigma_{\rm new}-c_{\rm exp}})\). Thus a matching literal-row low bound at \(Z^{\sigma_{\rm new}-c_{\rm exp}}\) would transfer to the fixed signal below the zero abscissa. To see why that would detect a pole, put \(g(y)=e^{c_{\rm exp}y}f(e^y)\). The descended bound gives \(g(y)=O(e^{\sigma_{\rm new}y})\) as \(y\to+\infty\), while the small-argument contour shift gives \(g(y)=O(e^{\sigma' y})\) as \(y\to-\infty\) for every fixed \(\sigma'>2\). Its bilateral Laplace transform therefore converges on \(\sigma_{\rm new}<\Re s<\sigma'\) and, by Mellin/Fourier inversion on the line \(\Re s=2\), agrees there with \(K(s)=e^{(s-5/6)^2}H_{S_0,\mathrm{half}}(s)/\zeta_K^{S_0}(s)\). That transform is holomorphic in the strip, contradicting a pole at any target zero with real part above \(\sigma_{\rm new}\); the Gaussian and half-damped factor do not cancel it.

This scenario is conditional in two independent ways: the chosen line must satisfy the safe reciprocal polynomial bound, and a matching averaged low bound at the descended exponent must actually be proved. Taking a line merely known safe above \(0.875\) does not yield descent below a zero abscissa near \(0.5\) unless its power saving exceeds the gap. The present source explicitly leaves the matching whole-probe/averaged low theorem open, so the descent is a possible use of §6, not a completed argument.

## Recommended text correction

Use distinct symbols \(\sigma_{\rm safe}\) and \(\sigma_*\) in the final paragraph of §6. State that the literal-row transfer at \(\sigma_*\) is available when the §9 line is chosen at \(\sigma_*\), or more generally when \(\sigma_{\rm safe}-m_0\le\sigma_*\). This avoids turning the valid conditional contraction into an unsupported claim of transfer from a fixed safe line to every \(\sigma_*>1/2\).

## Final audit of the abscissa-descent supplement

The new `PRINCIPAL_ABSCISSA_DESCENT.md` and corrected §6 pass the safe-line and error-exponent check, conditional on the accepted Q input and the still-missing same-row low bound. The Q input used here includes the fixed-field zero-free statement for both factors in \(\zeta_K(s)=\zeta(s)L(s,\chi_{-3})\), so \(\beta^*\le7/8\); this makes \(\sigma_{\rm safe}=\beta^*+\varepsilon<1\) possible. The pole-cleared function \(F_K(s)=(s-1)\zeta_K(s)\) is zero-free on the stated outer disk. Its center value is of size \(\asymp 1+|t|\), the ideal-counting estimate supplies polynomial upper growth on the disk, and Borel–Carathéodory across the fixed radius gap \(\varepsilon/2\) gives polynomial lower control. Multiplying by the finite deleted Euler factors preserves that bound. Constants may depend on the fixed \(\varepsilon\), as required; no uniformity as \(\varepsilon\downarrow0\) is used.

The contour parameters are consistent. Once \(\beta^*>1/2\) is fixed, \(\delta_x\) has a positive limit as \(\sigma_{\rm safe}\downarrow\beta^*\). The choices of \(\varepsilon_{\rm aux},d_w,\eta\) leave strict negative exponents in both displayed local bounds. Choosing \(\kappa_P\) using \(\delta_{\min}\) keeps the finite-slot saving valid throughout the safe-line neighborhood. One can then fix \(m_0<\min\{\ell_y d_w,h\eta,\kappa_P,(\beta^*-1/2)/4\}\), followed by \(0<\varepsilon<m_0/2\). This gives \(1/2<\sigma_{\rm new}=\beta^*+\varepsilon-m_0<\beta^*\), and the §9 error has exactly exponent \(\sigma_{\rm new}-c_{\rm exp}\). The constants in the reciprocal estimate can depend on this now-fixed \(\varepsilon\). The \(k\)-floor and all ensemble/slot bounds remain uniform because they use only the displayed pointwise bounds and \(k\ll\log R/\log\log R\), not continuity of \(k\) or of the coefficient family.

The source contour sequence still has exactly four \((w,z)\) pieces after the \(x\)-shift: double residue, retained \(w\)-line with \(z=1/6\) residue, \(w=1\) residue with retained \(z\)-line, and the doubly retained contour. The \(s=1\) Dedekind pole is a zero of the reciprocal, not a crossed pole. The new polynomial bound pays the horizontal joins, and the retained-piece savings and slot discrepancy are all included in \(m_0\). The pole contradiction in the supplement is also valid: the descended large-\(T\) bound and the arbitrarily strong small-\(T\) bound make the bilateral Mellin transform holomorphic on a strip containing \(\Re s=2\), where it equals \(K(s)\); a target pole to the right of \(\sigma_{\rm new}\) is impossible.

Thus the abscissa descent is a valid conditional route if a matching low bound is established for the exact averaged principal signal or the literal averaged principal row at the descended exponent. No such bound is currently proved, so this remains conditional and does not prove RH.

One minor generality issue remains in the main note's contraction lemma: it states arbitrary \(\sigma_*>1/2\), then chooses only \(\sigma'>2\) for the small-\(T\) contour shift. For the application here \(\sigma_*<1\), this is sufficient. To make the lemma as worded fully general, specify \(\sigma'>\max\{2,\sigma_*\}\), or restrict its statement to \(1/2<\sigma_*<2\).

Publication note: [AVERAGED_PRINCIPAL_CONTRACTION.md](AVERAGED_PRINCIPAL_CONTRACTION.md) now specifies the small-argument shift sigma'>max(2,sigma_*), and [PRINCIPAL_ABSCISSA_DESCENT.md](PRINCIPAL_ABSCISSA_DESCENT.md) contains the final safe-line proof audited above. The matching low theorem remains an explicit assumption.
