# Mathematical review: compressed complete mixed smoothing

Reviewed text: [Actual-vector compression improves the complete mixed smoothing bound](COMPRESSED_MIXED_SMOOTHING.md).

Disposition: pass after correcting the quoted origin interval to
\((0,\epsilon/2)\) and requiring \(2b<\epsilon/2\), as in the final text.
An independent model-assisted read-through checked the complete mixed
estimate and its scalar \(H^s\), \(s<1/8\), consequence against the
cited source, origin-domain, tail and full-prime/Gamma inputs. This is
not proof-assistant verification or external human peer review.

The positive compressed operator is legitimate: the complete reflection
is a self-adjoint contraction, so \(0\preceq I-\Theta\mathcal R\Theta
\preceq2I\). The commutator decomposition retains all labels.
The cutoff commutator costs \((t/b)\log(1+a/t)\), and the localized
\(E=Z-C\) bounds apply on both sides of the compressed reflection.
Finite propagation puts both \(v_b\) and \(Z^2v_b\) where \(\Theta=1\),
making the compressed mixed pairing exactly the full one on that vector.

The sharp cutoff is used only inside bounded \(L^2\) operator pairings.
Its error is paid by
\(\|v_0\|^2\le Cb\|g/x\|_{L^2(0,2b)}^2\), followed by the actual
\(\delta\|g/x\|_2\le C\sqrt{P_0}\) estimate. Restoring the true
weight on the original full vector costs linearly in \(T_\delta\).
The factor \(2\delta\) agrees with
\(N[r]=2\langle v,Hv\rangle\). No \(T_\delta^2\) term is inserted.

With the displayed parameters and each fixed \(\beta<1/2\),
\(\varepsilon_0+\sqrt{\eta_b}=O_\beta(N^{-\beta/2})\).
The origin error is \(O(N^{-1/4})\). The inherited complete prime-tail
and Gamma lower-loss argument still applies with \(a=b/16\), and its
remaining penalties are smaller than \(N^{-1/4}\). Dyadic summation
requires \(2s<\min(\beta/2,1/4)\), giving every \(s<1/8\).
The local fractional-origin extension uses a strictly larger intermediate
source exponent below \(1/8\), so its constants and range are consistent.

The argument is conditional on the cited upstream mathematical theorems.
It proves no whole-band estimate, endpoint exponent, strict negative
variation, supercritical exclusion, or RH conclusion.
