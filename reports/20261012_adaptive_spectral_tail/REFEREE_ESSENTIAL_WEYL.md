# Independent audit of the Weyl-packet argument

## Verdict and scope

**The Weyl construction in §2 is mathematically sound for every fixed \(\lambda\ge0\) on the full even space.** It proves \(\sigma_{\rm ess}(B)=[0,\infty)\), provided the separately assigned relative-compactness argument for \(V(B+1)^{-1}\) is correct. The packet estimates account for the very large carrier frequency forced by the rapidly decaying theta weight, and the reflected lobe causes no missing nonlocal term: the multiplier error is estimated globally in \(L^2\) for each lobe and then combined by the triangle inequality. I do not audit §1's relative-compactness proof here. The result supplies no exclusion of negative discrete spectrum for \(H\), no critical half-gap, and no RH conclusion.

The current formulas are correct. For a fully self-contained presentation, I recommend adding the short derivations below, especially for \(b'\), normalization, and the high-frequency tail.

## Theta weight and the chosen width

The leading \(r=1\) term of the actual theta series gives, as \(x\to+\infty\),

\[
 m(x)^2=4\pi^2 e^{4x-\pi e^{2x}}(1+O(e^{-x})),\qquad
 (\log m^2)'(x)=4-2\pi e^{2x}+O(e^{-x}).
\]

The \(O(e^{-x})\) correction includes the denominator \(2\cosh(x/2)\); the second component of \(\Phi\) contributes only at relative order \(e^{-2x}\), and \(r\ge2\) is exponentially smaller still. These estimates and their differentiated versions are uniform on \([X-e^{-3X},X+e^{-3X}]\). Consequently,

\[
\sup_{|x-X|\le e^{-3X}}|\log m(x)^2-\log m(X)^2|
\le O(e^{2X})e^{-3X}=O(e^{-X}),
\]

so exponentiation proves the displayed relative estimate (1). Evenness gives its negative-side version. Thus the chosen width is small enough despite the large logarithmic derivative. The same explicit tail shows \(m,m',m''\to0\), uniformly on any fixed-width interval translated to either infinity.

## Carrier frequency, modulation estimate, and domain

The positive series makes \(b\) continuous and strictly increasing on \((0,\infty)\). It is unbounded by \(b(t)=\log t+O(1)\), hence for each fixed \(\lambda>0\) there is a unique \(k_j>0\) with \(b(k_j)=\lambda/m(X_j)^2\). Since \(m(X)^2\sim4\pi^2e^{4X-\pi e^{2X}}\),

\[
\log k_j=b(k_j)+O(1)=\lambda/m(X_j)^2+O(1),
\]

so \(k_jw_j\to\infty\) overwhelmingly fast; in particular every fixed inverse power of \(k_jw_j\) beats every fixed power of \(w_j^{-1}=e^{3X_j}\).

For clarity, differentiating the positive series with \(a_j=j+1/4\) and \(y=t/2\) gives

\[
b'(t)=\sum_{j\ge0}\frac{y a_j}{(a_j^2+y^2)^2}.
\]

For large \(y\), split at \(a_j=y\): the first part is bounded by \(y^{-3}\sum_{a_j\le y}a_j=O(y^{-1})\), and the tail by \(y\sum_{a_j>y}a_j^{-3}=O(y^{-1})\). Thus \(0\le b'(t)\le C/t\). This proves the low-modulation estimate for \(|\eta|\le k_j/2\), since \(k_j+\eta\) stays comparable to \(k_j\):

\[
\|(b(D)-b(k_j))(\varphi_{j,+}e^{ik_j(\cdot-X_j)})\|_{\rm low}
\le (C/k_j)\|\varphi_{j,+}'\|_2=O((k_jw_j)^{-1}).
\]

The negative carrier has the same estimate because \(b\) is even. One can obtain the stated high-tail bound directly from the positive series:

\[
0\le b(t)\le\frac{t^2}{4}\sum_{j\ge0}(j+1/4)^{-3}<18t^2.
\]

On \(|\eta|>k_j/2\), this bounds \(|b(\pm k_j+\eta)-b(k_j)|\) by \(C\eta^2\). Scaling \(z=w_j\eta\) and using Schwartz decay of \(\widehat\varphi(z)\) then gives, for any chosen fixed \(N\) after taking enough Schwartz decay,

\[
\|(b(D)-b(k_j))(\varphi_{j,+}e^{ik_j(\cdot-X_j)})\|_{\rm high}
\le C_N w_j^{-2}(k_jw_j)^{-N}.
\]

This tends to zero despite the factor \(w_j^{-2}\), because \(k_jw_j\) grows much faster than any exponential in \(X_j\). The same full-symbol estimate proves \(b(t)\le18t^2\) used at \(\lambda=0\).

For the operator domain, each constructed \(v_j\) is in \(C_c^\infty\), including after multiplication by \(m^{-1}\), since \(m\) is smooth and positive on the compact support. Hence \(mv_j=c_jr_j\in C_c^\infty\), and the logarithmically growing multiplier maps it into the operator domain of \(b(D)\); then multiplication by bounded \(m\) gives \(v_j\in D(B)\). This is the correct direct domain argument and does not require identifying an operator domain from the form domain.

## Normalization, evenness, and absence of a missed cross-lobe term

The two supports are disjoint for large \(X_j\). On either support, (1) gives \(m^{-2}(x)=m(X_j)^{-2}(1+O(e^{-X_j}))\). Also, after changing variables to the fixed bump coordinate,

\[
\int \varphi(y)^2\cos^2(k_jw_j y)\,dy\longrightarrow\tfrac12\|\varphi\|_2^2
\]

by the Riemann–Lebesgue lemma and \(k_jw_j\to\infty\). Thus \(\|m^{-1}r_j\|_2\asymp m(X_j)^{-1}\), so \(c_j\asymp m(X_j)\to0\), as claimed. The modulation phases are reflected correctly, and evenness of \(\varphi\) makes \(r_j\) and \(v_j\) even. Because \(b\) is even, \(b(D)\) preserves parity. There is no unaccounted interaction between the two distant lobes: applying the Fourier multiplier to their sum and bounding the two global errors separately by the triangle inequality already includes all nonlocal leakage.

The operator identity in the positive-energy case is exact:

\[
(B-\lambda)v_j
=c_jM_m(b(D)-b(k_j))r_j
+\lambda\left(\frac{m^2}{m(X_j)^2}-1\right)v_j.
\]

The first term tends to zero by the global modulation estimate, boundedness of \(m\), and \(c_j\to0\). The second tends to zero by (1) and \(\|v_j\|_2=1\). Both supports escape, so the normalized packets are weakly null.

## Endpoint zero

For the normalized fixed-width even bump pair translated to \(\pm X_j\), the supports escape and the norm is one. The symbol bound gives

\[
\|Bv_j\|_2\le18\|m\|_\infty\|(mv_j)''\|_2.
\]

On the two fixed-width supports, the bump and its first two derivatives are uniformly bounded, while \(m,m',m''\to0\) uniformly. The product rule therefore yields \(\|(mv_j)''\|_2\to0\), proving the Weyl condition at zero. The even reflection introduces no extra term for the same reason as above: the bound is applied to the full even function on the line.

## Minor presentation additions

1. State the derivative-series split proving \(b'(t)=O(1/t)\), or cite a precise digamma derivative asymptotic. This makes the local-symbol estimate independently checkable.
2. Show the one-line Riemann–Lebesgue calculation for \(c_j\asymp m(X_j)\), since (1) alone controls the weight but not the oscillatory carrier norm.
3. Derive \(b(t)\le18t^2\) from \(b(t)\le(t^2/4)\sum(j+1/4)^{-3}\); this justifies both the high-tail estimate and the zero-endpoint bound without relying on an external report.

These are compact justification additions, not changes to the construction or its conclusion.

Publication note: [ESSENTIAL_SPECTRUM.md](ESSENTIAL_SPECTRUM.md) incorporates the requested global symbol correction and packet justifications. Each review retains its separate assigned scope.
