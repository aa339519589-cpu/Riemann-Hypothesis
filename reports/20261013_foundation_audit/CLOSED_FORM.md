# Independent Foundation / Closed-Form Audit 55

**Audited input:** commit `3c1f2b824dae3af1e2cf70eaa69ae7e25445631d`. The source reports are linked below. This review uses inner products conjugate-linear in their first slot.

**Verdict:** The specified original closed-form and domain foundation passes this independent audit. I found no substantive flaw in the source identity, complete-prime bounded perturbation, maximal jump-form identification, associated-operator domain, parity cores, or lower bound. The notation \(M_m S M_m\) should continue to mean the norm-convergent series of sandwiched shifts; no boundedness of the unweighted shift sum \(S\) on \(L^2(dx)\) is available or used.

This is an audit of the foundation requested here. It does not certify the later numerical/spectral gap reports, the separate essential-spectrum argument, or any full RH implication. These foundational results do not prove positivity of \(H\) on the ground-orthogonal space and do not prove RH. No Lean/formal verification is claimed.

## Checks

### 1. The Gamma multiplier and its true form domain

In reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md, lines 63–85, the constant subtraction is consistent:
\[
b(t)=\Re\psi(1/4+it/2)-\psi(1/4),\quad b(0)=0,\quad
b(t)=2\int_0^\infty k(u)(1-\cos tu)\,du,
\]
where \(k(u)=e^{-|u|/2}/(1-e^{-2|u|})\). The positive series displayed at lines 67–79 gives \(b\ge0\). The same kernel gives \(b(D)f=\int_0^\infty k(u)(2f-\tau_uf-\tau_{-u}f)\,du\) on a smooth core. Near zero \(k(u)\sim(2|u|)^{-1}\), so \(k\notin L^1\) there; the second difference, rather than an unjustified first-order integral, pays this singularity. Both \(\int u^2k(u)\,du\) and \(\int |u|k(u)\,du\) are finite.

The form and form domain at lines 223–243 are the right ones:
\[
\mathfrak b[v]=(2\pi)^{-1}\int b(t)|\widehat{mv}(t)|^2dt,\qquad
D(\mathfrak b)=\{v\in L^2_{\rm even}:mv\in H_{\log}\}.
\]
Because \(m\) is bounded and \(b(t)\asymp\log(2+|t|)\) for large \(|t|\), the norm \(\|v\|_2^2+\mathfrak b[v]\) is complete: an \(L^2\) limit \(v\) forces \(mv_j\to mv\) in source \(L^2\), while the weighted Fourier seminorm supplies the closed-multiplier limit. \(C_c^\infty\) is dense in \(L^2\), so the form is densely defined. The cutoff step controls the logarithmic difference norm with the integrable \(u^2k(u)\) moment; local mollification and division by \(m\) occur only on a fixed compact where \(m>0\). This pays the vanishing of \(m\) at infinity and proves the even form-core assertion (lines 237–243).

The associated operator must be defined by the representation theorem, not by requiring \(b(D)(mv)\in L^2\) for every form-domain vector. Precisely,
\[
v\in D(B)\iff v\in D(\mathfrak b)\ \text{and there is }w\in L^2
\text{ with }\mathfrak b(z,v)=\langle z,w\rangle
\text{ for every }z\in D(\mathfrak b);
\quad Bv=w.
\]
Distributionally this is the realization \(m\,b(D)(mv)\) when that expression represents the indicated physical \(L^2\) vector. The report explicitly makes this distinction at lines 243 and 279–284. Thus \(B\ge0\) is self-adjoint with the stated form domain; the formal product alone is not used to assign a larger domain.

### 2. The original maximal jump form and its domain

The closedness argument at foundation lines 192–221 is valid for the maximal finite-energy domain. The Gamma difference map and each prime difference map are viewed together in a direct sum of their weighted edge \(L^2\) spaces. If \(q_j\) is Cauchy in the form norm and converges in \(L^2(\nu)\), an almost-everywhere convergent subsequence identifies each edge-space limit with the difference of the limit \(q\). For a prime edge, translation preserves null sets; for the Gamma edge measure, the off-diagonal density is absolutely continuous with respect to \(dx\,dy\). This proves closedness without choosing a smaller domain.

The core proof also pays both spatial infinity and the diagonal singularity. Value truncation uses the 2-Lipschitz residual of radial projection and dominated convergence. For bounded \(q\), the cutoff error is controlled by
\[
C\|q\|_\infty^2R^{-2}\int u^2k(u)\,du
\]
after the autocorrelation bound; the prime contribution tends to zero by the bounded prime-form estimate (foundation lines 182–213). On a common compact, \(k(u)\asymp |u|^{-1}\) near zero, and Plancherel identifies the small-jump norm with the logarithmic Sobolev norm. Compactly supported mollification therefore gives the asserted compact-smooth core (lines 215–221).

For odd functions, the same full-line proof works with even cutoffs, radial value truncation, and an even mollifier: each operation preserves oddness. Equivalently, parity projection commutes with the full form and sends a full-line \(C_c^\infty\) core to even and odd cores. There is no half-line folding in the definition of \(B\) or of the original jump form, so no boundary condition at \(x=0\) is silently imposed. The singularity is the diagonal \(x=y\), already paid by the difference quotient; all full-line jump edges remain present.

### 3. Full signed physical \(V\), all prime powers

The theta envelope in foundation lines 159–180 and REPORT lines 48–78 has the correct constants. For \(z=|x|\),
\[
m(x)^2\le A_*e^{4z-\pi e^{2z}},\qquad A_*=4\pi^2(125/121).
\]
For \(x\ge0\), dropping the negative part of each theta summand, using \(2h(x)\ge e^{x/2}\), and bounding the normalized \(n^4e^{-\pi(n^2-1)e^{2x}}\) tail by a geometric series with ratio at most \(16e^{-3\pi}<4/125\) gives \(125/121\); evenness supplies the other half-line.

For \(d=\log n\), put \(r=e^{2|x|}\), \(s=e^{2|x+d|}\), \(u=\sqrt{rs}\). The triangle inequality gives \(u\ge n\), while the envelope and \(r+s\ge2u\) give
\[
m(x)m(x+d)\le A_*u^2e^{-\pi u}\le A_*n^2e^{-\pi n}
\quad(n\ge2),
\]
since \(u^2e^{-\pi u}\) decreases for \(u\ge2\). Hence
\[
\|M_m\tau_{\pm\log n}M_m\|
=\operatorname*{ess\,sup}_x m(x)m(x\pm\log n)
\le A_*n^2e^{-\pi n}.
\]
Using \(0\le\Lambda(n)\le\log n\) proves absolute convergence in operator norm of the whole signed shift series, since \(\sum_{n\ge2}\log n\,n^{3/2}e^{-\pi n}<\infty\). The REPORT's stronger tail bound follows: for \(n\ge3\), consecutive \(n^2e^{-\pi n}\) terms have ratio below \(1/10\), and \(\log n\le\sqrt n\), yielding
\[
\|V-V_N\|\le(20A_*/9)(N+1)^2e^{-\pi(N+1)}.
\]
The index is every integer \(n\ge2\), with \(\Lambda(n)=0\) except prime powers, so no prime power is omitted. Each symmetric shift pair is self-adjoint, and the sum plus real multiplication \(C_0M_{m^2}\) is bounded self-adjoint. The reports do not need, and do not establish, boundedness of unweighted \(S\) on \(L^2\); \(S\) is used pointwise on theta sources, while \(V\) is defined by the convergent weighted series.

The prime jump form is separately bounded on \(L^2(\nu)\): the elementary \(|q-q'|^2\le2(|q|^2+|q'|^2)\) estimate gives
\[
E_P(q)\le\int (S\Phi/h)|q|^2\,d\nu,
\]
and the source identity makes \(S\Phi/h=1+A\Phi/h\) bounded. This justifies the prime part of the original form-core cutoff argument.

### 4. Source identity and exact form equality

The Mellin computation at foundation lines 27–55 matches \(\xi(s)\) under the stated Fourier convention and gives \(\int \Phi e^{\pm x/2}=1/2\), hence \(Uq=\sqrt{2\Phi h}\,q\) is unitary and \(mUq=\Phi q\). The contour proof at lines 87–157 correctly uses \(\eta>1/2\) so the Dirichlet series for \(-\zeta'/\zeta\) converges absolutely on the shifted lines. Before returning to the real line, it replaces
\[
\xi(s)(-\zeta'/\zeta)(s)
=-\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta'(s),
\]
which removes every zeta-zero pole algebraically. On the swept region \(\Re s>0\), the only remaining pole is \(s=1\); its residue \(1/2\) yields the two terms \(\frac12e^{\mp x/2}\). The derived partial-summation bound on \(\zeta'\) is polynomial on the fixed strip, and Stirling supplies exponential Gamma decay on the horizontal edges. Log differentiation of \(\xi(s)=\xi(1-s)\) then gives the real-axis multiplier \(a(t)\), by analytic continuation across zeros. This establishes \(S\Phi=A\Phi+h\) without a zero-free estimate or RH assumption.

Expanding the positive Gamma and prime jump squares gives equations (13)–(15) at foundation lines 245–269 with the signs and constants consistent:
\[
\mathcal E(q)=\tfrac12\|Uq\|_2^2+\mathfrak b[Uq]-\langle Uq,VUq\rangle
\quad(q\in C_c^\infty).
\]
Both sides are closed and have the corresponding compact-smooth cores, and \(U\) maps compact smooth functions bijectively to compact smooth functions. Equality therefore extends to the whole maximal jump-form domain; it is not merely a test-function or finite-shift identity (lines 271–290).

### 5. Parity graph cores, \(H\), and the spectral statement actually proved

The odd-domain report lines 150–179 gives a valid graph-core extension. Since \(m\) and \(b\) are even and \(V\) is a symmetric \(\pm d_n\) shift sum, reflection reduces both \(B\) and \(V\). The commutator estimate follows directly from
\[
\|[b(D),\chi_R]\|\le
\|\chi_R'\|_\infty\int_{\mathbb R}|u|k(|u|)\,du=O(R^{-1}).
\]
The associated-form identity first proves \(\chi_Rv\in D(B)\) and then graph convergence for \(v\in D(B)\); it does not assume the generally false stronger condition \(mv\in D(b(D))\). For compactly supported \(v\), \(f=mv\) has \(b(D)f\in L^2\): it is locally \(L^2\) by dividing the represented \(Bv\) by positive \(m\) on compact sets, and outside a fixed collar it is the off-support convolution \(-k*f\), which has exponential tails. Mollifying \(f\) in the \(b(D)\) graph norm and dividing by \(m\) only on the common compact support yields the smooth graph core. Even cutoffs and mollifiers preserve both parities. A bounded perturbation preserves this core, so \(C_c^\infty\) in the even and odd sectors is a graph core for \(B\) and \(H\); conjugation by \(U\) gives the corresponding graph core for the original jump operator.

Because \(V\) is bounded self-adjoint, the form sum \(H=B-V\) is self-adjoint on exactly \(D(B)\). More strongly, the exact jump identity gives \(H\ge-\tfrac12 I\) on the full parity-preserving space. The normalized vector \(g_0=\sqrt p\) is in \(D(B)\) (\(mg_0=\Phi\in\mathcal S\)) and satisfies \(Hg_0=-\tfrac12g_0\). Equality in the positive jump form forces the original \(q\) to be constant, so this bottom eigenvalue is simple in the full space. These claims are supported by foundation lines 279–305 and the odd report lines 35–61, 332–356. They do not establish \(H\ge0\) on \(g_0^\perp\); the remaining sign problem is not resolved by this audit.

## Dependencies and limitations

The proof depends on the complete theta/Jacobi identity (including positivity, evenness, and double-exponential tails), Mellin inversion/analytic continuation, the functional equation for \(\xi\), standard digamma identities and growth, Stirling estimates in fixed strips, and \(\Lambda(n)\le\log n\). I checked the displayed DLMF identities and asymptotics cited in the foundation against NIST DLMF §§25.4, 5.11, 5.5, and 5.4; the contour proof itself derives the required \(\zeta'\) vertical bound rather than assuming a reciprocal-zeta bound. The functional-analytic steps use the closed-form representation theorem, the bounded self-adjoint perturbation theorem, Plancherel, and standard cutoff/mollifier convergence in the logarithmic Fourier norm.

No material repair is required for the audited claims. A helpful editorial tightening is to define \(V\) first as the explicit norm-convergent weighted series and reserve \(M_mSM_m\) for shorthand, so a reader cannot mistake \(S\) itself for an \(L^2\)-bounded operator. The audit establishes an unconditionally valid realization of the original even/odd operator and its domains, not the still-missing RH-bearing positivity statement.


## Linked mathematical inputs

- [Original source identity, maximal jump form and form domain](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md).
- [Complete-prime tail and original operator realization](../20261012_adaptive_spectral_tail/REPORT.md).
- [Odd-parity extension and graph-core proof](../20261013_odd_operator_domains/REPORT.md).

For complex sources the normalized mean pairing is $\langle e_0,Uq\rangle=\int q\,d\nu$ in the convention used here. Reversing the two slots conjugates the mean; its zero condition is unchanged.
