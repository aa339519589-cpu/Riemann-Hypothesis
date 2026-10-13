# Independent referee check: conditional global mean-periodicity (49)

Date: 2026-10-13. I checked [the global convolution companion](GLOBAL_MEAN_PERIODIC.md) from the displayed conditional tail premise through the finite-part Carleman continuation. This note does not prove the proposed tail premise. No external source was needed; the checks are direct and use the existing reflected-energy/reference results and the elementary Chebyshev bound for the full Mangoldt sum.

## Weighted ratio tail and constants

Assume
\[
F_g(R)=\int_R^\infty |g(x)|^2dx\le C e^{A R}e^{-2\pi e^{2R}},\qquad g=\psi r,
\]
and \(\psi(x)\asymp e^{13x/2}e^{-\pi e^{2x}}\). Then
\[
w_B=e^{-Bx}\psi^{-2}\asymp e^{-(B+13)x}e^{2\pi e^{2x}},\qquad
w'_B=O((1+e^{2x})w_B).
\]
Stieltjes integration by parts is correctly signed:
\[
\int_a^T w_B|g|^2=w_B(a)F_g(a)-w_B(T)F_g(T)+\int_a^T w'_B F_g.
\]
The boundary product is \(O(e^{(A-B-13)T})\); the derivative majorant is \(O((1+e^{2x})e^{(A-B-13)x})\). Thus the stated sufficient condition is \(B>A-11\). It is sufficient, not a necessary threshold for the actual integral; replace “integrable precisely under” with “this displayed majorant is integrable when” to avoid suggesting necessity. For the supplied candidate \(A=16\), \(B=6\) works: the derivative majorant is \(O(e^{-x})\).

The bounded interval \([1,R_0]\) is controlled by the already established positive reference: its diagonal \(D_R\) is strictly positive away from zero, while \(D_R(x)\asymp x\) at zero. Hence the reference norm gives local \(L^2\) away from zero and \(\int_0^1x|r|^2<\infty\). This baseline finite-reference-energy fact should be named alongside (1); it is not supplied by (1) alone.

For the second weighted estimate, \(w_0=e^{x/2}/\psi\asymp e^{-6x}e^{\pi e^{2x}}\); multiplying its derivative bound by the assumed \(F_g\) gives a majorant \(C(1+e^{2x})e^{(A-6)x}e^{-\pi e^{2x}}\), integrable for every fixed finite \(A\). The equality \(w_0|g|^2=\psi e^{x/2}|r|^2\) and the endpoint reference bound prove (4).

## Full reflected row and load estimate

The bound \(L(x)\le C_L e^{x/2}\) needed for the advertised choices \(B=6,C=7\) is valid, although the cited reflected-prime report states the weaker \(C(1+x)e^{x/2}\). Here is the sharper complete-prime derivation. Use the elementary Chebyshev estimate \(\Psi(Y)=\sum_{n\le Y}\Lambda(n)\le C Y\), which includes all prime powers. On shells \(e^{x+k}<n\le e^{x+k+1}\), \(k\ge0\),
\[
\sum_{e^{x+k}<n\le e^{x+k+1}}\frac{\Lambda(n)}{\sqrt n}\psi(\log n-x)
\le C e^{x/2} e^{(k+1)/2}\sup_{k\le s\le k+1}\psi(s).
\]
The sum over \(k\) converges by the double-exponential theta tail, uniformly for \(x\ge0\). This proves \(L(x)\le C_L e^{x/2}\), and also \(\int_0^\infty\psi L<\infty\). If this sharper Chebyshev derivation is not included or cited, choose \(B=6+\epsilon,C=7+\epsilon\) instead to absorb the coarser polynomial row factor; the downstream Cauchy/change-of-variable argument still works.

For \(F(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x)r(d_n-x)\), weighted row Cauchy is exact:
\[
|F(x)|^2\le L(x)\sum_{d_n>x}\alpha_n\psi(d_n-x)|r(d_n-x)|^2.
\]
For \(x\ge1\), put \(y=d_n-x\). Tonelli gives
\[
\int_1^\infty e^{-Cx}|F(x)|^2dx
\le C_L\int_0^\infty\psi(y)|r(y)|^2 e^{(C-1/2)y}
       \sum_{n>e^{y+1}}\Lambda(n)n^{-C}dy.
\]
Dyadic shells plus \(\Psi(Y)\ll Y\) give \(\sum_{n>Y}\Lambda(n)n^{-C}\ll_CY^{1-C}\) for every \(C>1\); the remaining factor is \(e^{y/2}\), exactly the integrable weight in (4). For \(A=16,B=6,C=7\), all exponents match. Applying this same estimate to labels \(n>N\), then dominated convergence, proves convergence of full prime-power partial rows in \(L^2(e^{-Cx}dx)\). No ordinary Dirichlet series is used.

The incidence Cauchy estimate (6) has no missing factor: multiplying the row Cauchy inequality by \(\psi/L\) integrates to exactly the displayed reflected energy \(N[r]\). Thus \(W\in L^2((0,1),x\,dx)\), locally \(L^2\) away from zero, and exponentially weighted \(L^2\) at infinity. The equality \(W=Lr-F\) is valid in the latter weighted space by the bounds just proved and agrees with the weak edge divergence on compact tests.

## Endpoint distribution and the moment-to-zero step

The odd extension definition is valid at the endpoint: \(\varphi(x)-\varphi(-x)=O(x)\), and
\[
\int_0^1x|W(x)|dx\le
 (\int_0^1x|W|^2)^{1/2}(\int_0^1x)^{1/2}<\infty.
\]
It therefore defines a local distribution of order at most one; no \(W\in L^1_{loc}\) assertion is needed.

For compact \(\zeta\)-sets in any closed substripe of \(|\Im\zeta|<\pi/4\), every \(\zeta\)-derivative of
\[
\Phi(x+\zeta)-\Phi(x-\zeta)
\]
is \(O(x)\) as \(x\downarrow0\), since \(\Phi^{(k)}(-\zeta)=(-1)^k\Phi^{(k)}(\zeta)\). At infinity the real part of the theta exponential has decay \(e^{-c e^{2x}}\) uniformly on such a compact substrip. Cauchy-Schwarz with the exponential weighted \(L^2\) tail of W justifies all derivatives and proves holomorphy on the full open strip. With the stated convolution convention,
\[
(\Phi*W_o)(\zeta)=\int_0^\infty W(x)[\Phi(x-\zeta)-\Phi(x+\zeta)]dx=-\mathcal F(\zeta),
\]
so the sign is correct.

There are two distinct inputs to the moment argument. First, \(M_0=0\) follows directly from edge antisymmetry, not from (1):
\[
\int_0^\infty\psi W
=\sum_n\alpha_n\int_0^{d_n}\psi(x)\psi(d_n-x)[r(x)-r(d_n-x)]dx=0.
\]
This exchange is justified absolutely by Cauchy-Schwarz, since the absolute sum is bounded by \(N[r]^{1/2}(\int\psi L)^{1/2}\). As \(\psi=-\Phi'\), this gives \(M_0=\int W\Phi'=0\).

Second, \(M_{j+1}=M_j/4\) requires theta-jet orthogonality; it does not follow from the integrated-g tail. For the intended supercritical Green eigen-source this follows from the preexisting exact inputs: the mixed identity \(P(r_j,r)=N(r_j,r)\) for the theta-jet ratios, extended to the actual source by their energy-domain membership, and the eigenrelation \(N(r,z)=\lambda P(r,z)\) with \(\lambda>1\). Substituting \(z=r_j\) yields \(N(r,r_j)=0\). The weak divergence identity is
\[
N(r,r_j)=2\int_0^\infty \overline{W(x)}\psi(x)r_j(x)dx
         =2\int_0^\infty \overline{W(x)}f_j(x)dx.
\]
Thus \(\int W f_j=0\), so \(M_{j+1}-M_j/4=0\). The note should explicitly state/cite this supercritical orthogonality chain (or list \(r\perp_N S_N\) as a baseline hypothesis); calling (1) the “sole additional premise” is fine only if this is clearly part of the already established eigen-source setup.

All moments converge: near zero each odd theta derivative is \(O(x)\), and at infinity it decays double-exponentially. Then \(\mathcal F\) is odd, its even derivatives at zero vanish, and \(\mathcal F^{(2j+1)}(0)=2M_j\). Hence all Taylor coefficients vanish and the identity theorem gives global vanishing in the connected strip. No factor of two is missing: the two odd-derivative terms in the bracket contribute equally. In particular this yields the all-real-center convolution identity conditional on the baseline source orthogonality and (1).

## Finite-part Carleman transform and Fourier convention

The finite part is a valid order-one distribution. For a test \(\varphi\), its subtracted integrand is \(O(x)W(x)\) at zero, and the tail is finite by local compact support. For \(\Im\zeta>C/2\), the transform integral converges at infinity by Cauchy-Schwarz from \(e^{-Cx}|W|^2\in L^1\); the same \(O(x)\) cancellation makes it holomorphic at the finite endpoint. The reflected subtraction cancels exactly, so \(W_o=W_+^\eta-W_+^\eta\!\check{}\).

The convolution/Fourier signs and normalization check as stated, provided the same unnormalized convention is used for both transforms:
\[
\Xi(\zeta)=\int\Phi(t)e^{i\zeta t}dt,\qquad
B(\zeta)=\int Z(t)e^{i\zeta t}dt.
\]
For \(Z=\Phi*W_+^\eta\), set \(u=t-x\); then \(e^{i\zeta t}=e^{i\zeta u}e^{i\zeta x}\), giving \(B=\Xi\mathcal W_+^\eta\), with no \(2\pi\) factor. A rigorous Fubini step should retain the combined finite-part kernel \(\Phi(t-x)-\eta(x)\Phi(t)\): it is \(O(x)\) near zero, while the exponential weight controls infinity. Splitting the two near-zero terms before using Fubini would be unjustified for a potentially nonintegrable W.

The opposite half-line representation and theta tails give double-exponential decay of every fixed derivative of Z at both ends, so B is entire. Therefore \(B/\Xi\) is meromorphic with possible poles only at zeros of the nonzero entire \(\Xi\), of order at most the zero multiplicity. Changing \(\eta\) changes \(W_+^\eta\) by \(c\delta_0\), hence changes its transform by the constant c and changes Z,B by \(c\Phi,c\Xi\). This is only a degree-zero polynomial ambiguity, not a higher polynomial; it does not change the possible pole set. The normalization is internally consistent with \(\Xi=\widehat\Phi\) as defined in the source convention; there is no extra factor when this same transform defines both \(\Xi\) and B.

## Verdict / edits recommended

The conditional derivations are sound, including the threshold \(B>A-11\), the reflected-load change of variables, endpoint distribution, strip analyticity, moment recurrence, convolution sign, and meromorphic continuation. I found no RH or zero-location implication. I recommend three precision edits to the working note: (i) change “integrable precisely” to “the majorant is integrable when”; (ii) show/cite the Chebyshev shell proof of \(L\ll e^{x/2}\) if retaining the exact B=6,C=7 choices (the public reflected-prime report only states a coarser polynomial loss); and (iii) spell out that jet orthogonality is inherited from the \(\lambda>1\) Green eigenrelation and the exact mixed identity, rather than a consequence of tail premise (1). For the Fourier product, state that the combined compensated kernel is used in Fubini.

This review treats the tail premise as an input. The separate [tail report](REPORT.md) and [tail audit](REFEREE_TAIL.md) establish it for the intended supercritical eigen-source.

## Additional independent audit

I rechecked the weighted change of variables, endpoint pairings, and Fourier
normalization directly against the candidate and the two referenced Green
reports. **Disposition: pass, conditional on (1) and the stated inherited
Green-eigen-source properties.** I found no fatal mathematical gap in
(3)--(20).

In particular, in (10) the factor α_n=Λ(n)n^{-1/2} combines with
e^{-(C-1/2)d_n} to give exactly Λ(n)n^{-C}; the Chebyshev tail then
leaves precisely the e^{y/2} weight in (4). The endpoint bounds use only
∫ x|W|^2, which does give ∫ x|W|<∞, and do not accidentally assert
W∈L^1 near zero. With the convention Ξ(ζ)=∫Φ(t)e^{iζt}dt, changing
variables t=u+x in the compensated convolution gives the positive factor
e^{iζx}; hence there is no sign or 2π discrepancy in (20). Retaining
Φ(t-x)-η(x)Φ(t) as one kernel near zero is essential and the note
does so.

Two inherited hypotheses should remain visible in any reuse of the result:
the positive reference-energy bound supplies local ratio control and
(2), while the λ>1 eigen-current in S_N^⊥ plus the established mixed
theta-jet identity supplies (13). Neither follows from the sharpened tail
premise alone. The full-prime Green report, §2, does explicitly prove the
row estimate L(x)\le C_L e^{x/2} by Chebyshev shells, so this is a citation
or presentation improvement rather than a missing estimate; citing that
section is enough to support the concrete B=6,C=7 specialization. Finally,
the condition B>A_δ-11 is the threshold for integrability of the displayed
majorant, not a necessary threshold for the actual weighted ratio integral.

No RH or zero-location conclusion follows. The source-tail hypothesis (1) is proved in the separately reviewed tail report; it remains a dependency of this audit.

## Publication clarifications

The final companion cites the full-prime row bound, explicitly derives jet orthogonality from the eigenrelation, treats the exponent condition as sufficient, and retains the combined finite-part kernel. Its application to the actual eigen-source uses the separately established source-tail theorem, rather than claiming the tail follows from convolution.
