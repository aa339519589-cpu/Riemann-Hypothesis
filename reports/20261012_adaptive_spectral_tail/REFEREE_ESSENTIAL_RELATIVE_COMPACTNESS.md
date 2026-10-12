# Independent audit: relative compactness and essential-spectrum transfer

## Verdict

The relative-compactness argument in the pre-revision draft of [ESSENTIAL_SPECTRUM.md](ESSENTIAL_SPECTRUM.md) is sound on the full even space. In particular,
\[
V(B+1)^{-1}\text{ is compact},
\]
including the complete prime-power sum. The resolvent identity then gives compact resolvent difference and hence \(\sigma_{\rm ess}(H)=\sigma_{\rm ess}(B)\). This verifies the perturbation-transfer step; the claimed value \(\sigma_{\rm ess}(B)=[0,\infty)\) rests on the separate Weyl-packet argument, which is outside this audit's assigned scope. The proof uses both spatial tails throughout and makes no form-to-operator-domain inference.

## Relative compactness on both tails

For \(u=(B+1)^{-1}f\), the form resolvent estimate bounds \(\|u\|_2^2+\mathfrak b[u]\). Therefore \(g=mu\) is bounded in the logarithmic Sobolev norm: its \(L^2\) norm is bounded because \(m\) is bounded, and its \(b\)-weighted Fourier term is exactly \(\mathfrak b[u]\). The sum of this term and \(\|g\|_2^2\) is equivalent to the \(H_{\log}\) norm. If \(\chi\) is compactly supported and smooth, then
\[
\chi u=(\chi/m)g.
\]
Here \(\chi/m\) is a smooth compactly supported multiplier because \(m\) is strictly positive on each compact set. Such multiplication is bounded on \(H_{\log}\). The resulting family is supported in a fixed compact interval and bounded in \(H_{\log}\); its embedding into \(L^2\) is compact. One direct proof is to truncate Fourier frequencies at \(T\): the high-frequency tail is uniformly \(O((\log(2+T))^{-1/2})\), and the low-frequency projection restricted to a bounded spatial interval is Hilbert-Schmidt. Thus the resolvent is locally compact in \(L^2\) on every bounded interval, including intervals on the negative side.

It follows that \(M_{m^2}(B+1)^{-1}\) is compact: localize to \([-R,R]\), use local compactness there, and bound the complement by
\[
\sup_{|x|>R}m(x)^2\,\|(B+1)^{-1}\|,
\]
which tends to zero as \(R\to\infty\). This is a two-sided tail estimate; it uses \(m(x)\to0\) as \(x\to+\infty\) and as \(x\to-\infty\).

For fixed \(d\), the weighted translation is multiplication by \(m(x)m(x+d)\) followed by translation. On a bounded output interval, the translated resolvent output is relatively compact by local compactness on the corresponding translated input interval. Outside \([-R,R]\), the coefficient has supremum tending to zero, since both \(m(x)\) and \(m(x+d)\) tend to zero at either end. Hence each \(M_m\tau_{\pm d}M_m(B+1)^{-1}\) is compact as a map from the even space to full \(L^2\); an individual direction need not preserve parity. The symmetric prime sum preserves evenness.

The bound
\[
\alpha_n\|M_m\tau_{\pm\log n}M_m\|
\le A_*\Lambda(n)n^{3/2}e^{-\pi n}
\]
is summable over every integer \(n\ge2\). Thus the tail after any cutoff \(N\) tends to zero in operator norm, uniformly without omitting prime powers. Composing the partial sums with \((B+1)^{-1}\) gives finite sums of compact operators; the norm limit is compact. Together with the \(C_0M_{m^2}\) term, this proves the asserted compactness of \(V(B+1)^{-1}\).

## Resolvents and essential spectrum

Since \(V\) is bounded and self-adjoint, \(H=B-V\) is self-adjoint on \(D(B)\). For nonreal \(z\),
\[
V(B-z)^{-1}
=V(B+1)^{-1}(B+1)(B-z)^{-1}
\]
is compact; the second factor on the right is bounded. The resolvent identity
\[
(H-z)^{-1}-(B-z)^{-1}=(H-z)^{-1}V(B-z)^{-1}
\]
therefore has compact right-hand side. Weyl invariance gives \(\sigma_{\rm ess}(H)=\sigma_{\rm ess}(B)\). If the separately audited Weyl sequences establish \(\sigma_{\rm ess}(B)=[0,\infty)\), the manuscript's conclusions for \(H\) and, by the unitary shift, for \(L\) follow. Below zero, this leaves room for discrete eigenvalues of finite multiplicity accumulating only at zero; the argument does not prove the critical half-gap or RH.

## Necessary correction

The opening sentence of Section 1 says \(b(t)\asymp\log(2+|t|)\) without restricting \(t\). Read globally, this is false because \(b(0)=0\) while \(\log 2>0\). Replace it with either
\[
1+b(t)\asymp\log(2+|t|)\qquad(t\in\mathbb R),
\]
or “\(b(t)\asymp\log(2+|t|)\) for \(|t|\ge1\), and the \(L^2\) term supplies the low frequencies.” The proof actually uses the correct norm combination \(\|g\|_2^2+\mathfrak b[u]\), so this is a precision fix, not a defect in the compactness argument. The manuscript correctly uses the inverse \(1/m\) only after a compact cutoff, and it does not infer operator-domain membership from form-domain membership.

Publication note: [ESSENTIAL_SPECTRUM.md](ESSENTIAL_SPECTRUM.md) incorporates the requested global symbol correction and packet justifications. Each review retains its separate assigned scope.
