# Final-current contour and normalization review

## Verdict and scope

**Pass for the claims reviewed in §§1–2 and §7 of [ORIGINAL_FORM_FOUNDATION.md](ORIGINAL_FORM_FOUNDATION.md).** The inserted Mellin calculation fixes the exact normalization issue noted in the prior review, and the revised treatment of (7) now makes clear that the paired products are continued across zeros. The source identity

\[
S\Phi=A\Phi+\cosh(x/2)
\]

has the correct factors and signs. Its contour proof uses no zero-location hypothesis, no reciprocal-zeta bound, and no assumption of simple zeros. The ground-state normalization and operator identity in §7 also check. This review does not assess §§3–6, the separate spectral certificate, or any claimed critical half-gap; it establishes no conclusion about RH.

## Mellin transform, Fourier convention, and kernel constants

For \(\Re s>1\), substituting \(u=\pi r^2e^{2x}\) into the two terms of \(\Phi\) gives respectively

\[
2\pi^{-s/2}r^{-s}\Gamma(2+s/2),\qquad
-3\pi^{-s/2}r^{-s}\Gamma(1+s/2).
\]

The stated sum of their absolute integrals is finite for \(\Re s>1\), so termwise integration is justified. The bracket reduces exactly:

\[
2\Gamma(2+s/2)-3\Gamma(1+s/2)
=(s-1)\Gamma(1+s/2)
=\tfrac12s(s-1)\Gamma(s/2).
\]

Thus the Mellin integral is \(\xi(s)\), with no missing scale or factor. Since the exponent is \(e^{(s-1/2)x}\), setting \(s=1/2+it\) matches the stated transform \(\widehat\Phi(t)=\int\Phi(x)e^{itx}dx\). The double-exponential tails justify its entire continuation. At \(s=0,1\), \(\xi(0)=\xi(1)=1/2\), giving

\[
\int p(x)\,dx=\int\Phi(x)(e^{x/2}+e^{-x/2})\,dx=1.
\]

The kernel representation is also normalized correctly. With \(a_j=j+1/4\), the digamma difference gives

\[
b(t)=\sum_{j\ge0}\frac{(t/2)^2}{a_j(a_j^2+(t/2)^2)}
=2\int_0^\infty \frac{e^{-u/2}}{1-e^{-2u}}(1-\cos(tu))\,du.
\]

The expansion of \(k\) has rates \(2j+1/2=2a_j\), yielding exactly the displayed series. Therefore (1) has symbol \(a(t)=b(t)-C_0\). The digamma value at \(1/4\) gives \(b(0)=0\) and the stated value of \(C_0\).

## Contours, zero cancellation, and residues

For \(\Phi(x+\log n)\), Fourier inversion contributes \(n^{-it}\); on \(\Im t=-\eta\), the parameter \(s=1/2+it\) has real part \(1/2+\eta>1\), giving the absolutely convergent Dirichlet series. For \(\Phi(x-\log n)\), the factor is \(n^{it}\); on \(\Im t=+\eta\), \(s=1/2-it\) has the same real part. Since \(\eta>1/2\), both prime sums converge absolutely, and strip decay of \(\Xi\) justifies the exchanges and the initial shifts.

The functional equation is applied before the return contours: \(\Xi(t)=\xi(1/2+it)=\xi(1/2-it)\). On either sweep, the exact identity

\[
G(s):=\xi(s)\frac{-\zeta'}{\zeta}(s)
=-\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta'(s)
\]

removes every zeta-zero pole before deformation, at every multiplicity. In the swept half-strip \(1/2\le\Re s\le1/2+\eta\), \(\Gamma(s/2)\) has no pole and the only pole of \(G\) is at \(s=1\). From \(\zeta'(s)\sim-(s-1)^{-2}\), its residue there is \(+1/2\).

The change of variables contributes the signs in (6): for the lower contour, \(ds/dt=i\) and \(\operatorname{Res}_t=-i e^{-x/2}/2\), so \(I_-=I_{\mathbb R,+}+e^{-x/2}/2\). For the upper contour, \(ds/dt=-i\) and \(\operatorname{Res}_t=+i e^{x/2}/2\), so \(I_+=I_{\mathbb R,-}+e^{x/2}/2\). Their sum is \(\cosh(x/2)\), with the correct factor.

The partial-summation identity (5a) is valid for \(\Re s>0\). Differentiating its absolutely convergent integral on a fixed positive-real-part strip bounds \(\zeta'(s)\) polynomially in \(|\Im s|\), away from the already treated pole. Stirling then makes the horizontal contour edges vanish through exponential gamma decay. This supplies the needed growth estimate without a zero-free region or a bound on \(1/\zeta\).

Logarithmic differentiation of \(\xi(s)=\xi(1-s)\) gives (7) with the rational terms canceled. On the critical line the paired digamma terms equal \(\Re\psi(1/4+it/2)\), leaving precisely \(a(t)\). The draft now states that the quotient identity is meromorphic, and that each multiplied product is continued through zeros using (5) (or its \(1-s\) version). Thus the real-line sum is the continued function \(\Xi(t)a(t)\), even at critical-line zeros; no individual undefined quotient is evaluated there. Its inverse Fourier transform is \(A\Phi\), as asserted.

## Ground state in §7

The identities \(mg_0=\Phi\), \(mh=g_0/2\), and \(A-S\) applied to \(\Phi\) give

\[
(B-V)g_0=M_m(A-S)\Phi=-\tfrac12g_0.
\]

The operator-domain justification is sufficient: \(\Phi\in\mathcal S\) and \(b\) has logarithmic growth, so \(b(D)\Phi\in L^2\) and \(g_0\in D(B)\); the prime contribution is the bounded operator from (10), with its value on \(\Phi\) identified by the pointwise source identity after multiplication by \(m\). Since \(\|g_0\|_2^2=\int p=1\), (17) gives \((ULU^{-1})g_0=0\) with the stated sign and normalization. Strict positivity of \(\Phi(x)\Phi(y)k(x-y)\) off the diagonal implies that zero continuous jump energy forces \(q(x)=q(y)\) for almost every pair, hence \(q\) is constant almost everywhere.

No remaining correction is needed in the reviewed sections. The prior requested clarifications are both present in the current draft.
