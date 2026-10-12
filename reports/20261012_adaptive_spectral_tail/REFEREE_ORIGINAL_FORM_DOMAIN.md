# Final independent audit: complete even jump-form domain

## Verdict

**The complete-domain realization in [ORIGINAL_FORM_FOUNDATION.md](ORIGINAL_FORM_FOUNDATION.md) is correct, conditional on its pointwise source identity**
\[
S\Phi=(b(D)-C_0)\Phi+\cosh(x/2).
\]
The source identity is a separate analytic claim; this audit concerns the kernel normalization, maximal-form closure and core, the full prime-power contribution, the exact unitary form identity, operator domains, and the ground state. No zero-location statement, including RH, is used or follows from these domain arguments.

The new even kernel
\[
k(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}},\qquad u\ne0,
\]
has the correct normalization. For \(u>0\),
\[
k(u)=\sum_{j\ge0}e^{-(2j+1/2)u},
\]
and
\[
2\int_0^\infty e^{-(2j+1/2)u}(1-\cos(tu))\,du
=\frac{(t/2)^2}{(j+1/4)((j+1/4)^2+(t/2)^2)}.
\]
Tonelli's theorem applies to the nonnegative integrand, giving exactly the displayed series for \(b(t)\). Near zero \(k(u)\sim(2|u|)^{-1}\), and at infinity it decays like \(e^{-|u|/2}\). Thus the integral converges for every \(t\), the second-difference operator in (1) has multiplier \(b(t)\), and \(\int_0^1(1-\cos(tu))du/u\) has the claimed logarithmic growth. Precisely, its sum with 1 is comparable to \(\log(2+|t|)\) for all real \(t\). Since \(b(0)=0\), the full logarithmic norm is \(\|g\|_2^2+(2\pi)^{-1}\int b(t)|\widehat g(t)|^2dt\), rather than the \(b\)-seminorm alone.

## Domain and core checks

The maximal jump form is closed with its stated finite-energy domain. The continuous difference map and the countable family of prime difference maps form a single map into the direct sum of weighted edge spaces. From convergence in \(L^2(\nu)\), a subsequence converges almost everywhere; positivity of the weights and translation invariance identify each edge-space limit with the difference of the limiting function. This is a maximal-domain argument and does not presume equality of minimal and maximal realizations.

The full prime sum, including every prime power, is controlled in both ways needed by the proof. The theta envelope yields
\[
\|M_m\tau_{\pm\log n}M_m\|
\le A_*n^2e^{-\pi n},
\]
so multiplication by \(\alpha_n=\Lambda(n)/\sqrt n\) gives a summable operator-norm series. Separately, expanding each jump square gives
\[
E_P(q)\le \int (S\Phi/h)|q|^2\,d\nu.
\]
The source identity and Schwartz decay of \((b(D)-C_0)\Phi\) make \(S\Phi/h\) bounded. These estimates cover all integer shifts in the definition, with no omitted-power or large-shift issue.

The maximal-form core argument is valid for complex-valued functions. Radial projection onto a disk and its residual are Lipschitz, so value truncations converge in the graph norm by dominated convergence. For bounded functions, the spatial cutoff error splits into a tail of the original difference and a cutoff-difference term. The latter is bounded by
\[
C\|q\|_\infty^2 R^{-2}\int_{\mathbb R}u^2k(u)\,du,
\]
which tends to zero; the prime part tends to zero by its \(L^2(\nu)\)-boundedness. The squared sum is controlled with \(|a+b|^2\le2|a|^2+2|b|^2\), so no cross term is being discarded.

After spatial truncation, compact support places the continuous weight on a compact set where it is bounded above and below by positive constants. The small-jump energy then controls the global logarithmic Sobolev norm, since
\[
\int_{|u|<1}\frac{\|q(\cdot+u)-q\|_2^2}{|u|}\,du
\]
has Fourier weight comparable to \(\log(2+|t|)\), after adding the \(L^2\) norm. Conversely, on a fixed compact support the weighted small-jump energy is bounded by that norm, and the \(|u|\ge1\) part is bounded by \(C\|q\|_2^2\). Standard even mollifiers therefore converge in the full continuous form norm; the prime part follows from (11). This proves that even \(C_c^\infty\) is a core for the **maximal** original form.

The source form is closed on
\[
\mathcal D=\{v\in L^2_{\rm even}:mv\in H_{\log}\}.
\]
Its core proof is also sound: cut off the source \(g=mv\), use the same logarithmic difference representation and weighted cutoff estimate, mollify the compactly supported source in \(H_{\log}\), then divide by \(m\) on a common compact set where \(m\) and \(1/m\) are smooth and bounded. This proves density in both the source-form norm and the original \(L^2\) norm. It does not assert that multiplication by \(m\) sends arbitrary \(L^2\) functions into \(H_{\log}\).

On the common even \(C_c^\infty\) core, the continuous ground-state identity and the prime-shift expansion have the stated factors. The scalar \(C_0\) terms cancel, and the pointwise source identity leaves \(\int\Phi h|q|^2=\tfrac12\|Uq\|_2^2\). Multiplication by \(\sqrt p\) maps even \(C_c^\infty\) bijectively to itself. Equality on the common core therefore extends to equality of the two closed forms and their full domains:
\[
U D(\mathcal E)=\mathcal D,
\qquad
\mathcal E(q)=\tfrac12\|Uq\|_2^2+\mathfrak b[Uq]-\langle Uq,VUq\rangle.
\]
This is a quadratic-form identity for every maximal finite-energy \(q\). It does not imply \(Uq\in D(B)\). Since \(V\) is bounded and self-adjoint, the associated operator is exactly
\[
ULU^{-1}=\tfrac12+B-V,\qquad D(ULU^{-1})=D(B).
\]

Finally, \(g_0=U1=\sqrt p\) has norm one, \(mg_0=\Phi\), and \(\Phi\in D(b(D))\) because it is Schwartz. The pointwise source identity gives
\[
(B-V)g_0=m[(b(D)-C_0-S)\Phi]=-mh=-\tfrac12g_0,
\]
so \(g_0\) is a genuine operator eigenvector of \(ULU^{-1}\) at zero. The strictly positive continuous jump density forces every zero-energy function to be constant, identifying the unique zero direction with \(q\equiv1\).

## Precise wording to preserve

For statements quantified over the full maximal finite-energy domain, use
\[
\boxed{\quad
\mathcal E(q)=\mathfrak q_{H+1/2}[Uq]
=\tfrac12\|Uq\|_2^2+\mathfrak b[Uq]-\langle Uq,VUq\rangle,
\qquad Uq\in D(\mathfrak b).
\quad}
\]
Write \(\langle Uq,(H+\tfrac12)Uq\rangle\) only when \(Uq\in D(H)=D(B)\). Likewise, state gap lower bounds on the form domain as form inequalities. The current manuscript already makes this distinction in Sections 6–7; retaining it is the only material wording constraint for downstream use. No substantive correction to the current complete-domain argument is required, subject to the stated source identity.
