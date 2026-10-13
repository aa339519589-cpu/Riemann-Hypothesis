# Independent theta-strip and eigenstate-tail audit

**Source baseline:** commit `015cc4f1b46faf41a5886971f12e83aa1cedfae6`.
**Audited sources:** [ACTUAL_FULL_GAMMA_CERTIFICATE.md](../20261012_adaptive_spectral_tail/ACTUAL_FULL_GAMMA_CERTIFICATE.md), Appendix B; [ACTUAL_NEGATIVE_BAND_COVERAGE.md](../20261012_adaptive_spectral_tail/ACTUAL_NEGATIVE_BAND_COVERAGE.md), Parts I–II and the interpolation-domain passages in Part III; the [odd operator-domain report](../20261013_odd_operator_domains/REPORT.md); and the Weil-domain passage in [FINITE_HEIGHT_GAP.md](../20261012_adaptive_spectral_tail/FINITE_HEIGHT_GAP.md).
**Verdict:** PASS for the requested analytic and domain inputs. I found no substantive gap in the actual theta branch, complete physical-prime tail, whole-band localization, parity transfer, or fixed-order eigenstate domain passage. The reports do not infer eigenstate smoothness from a qblog or from the logarithmic form domain: it is obtained from the positive-depth spectral-band estimate and then combined with a spatial tail. The certificate at a critical limiting depth, odd-block nonnegativity, and RH remain outside this result.

## 1. Actual holomorphic multiplier

Appendix B starts from the literal summand

\[
\Phi_n(z)=2\pi n^2e^{5z/2}(2\pi n^2e^{2z}-3)e^{-\pi n^2e^{2z}}.
\]

The series converges locally normally for \(|\Im z|<\pi/4\), since \(\Re e^{2z}>0\) there on compact sets. In the smaller strip \(|\Im z|<\pi/6\), for \(x=\Re z\ge0\) and \(t=e^{2x}\ge1\),

\[
\pi\Re(e^{2z})=\pi t\cos(2\Im z)>\tfrac32t,
\qquad |2\pi e^{2z}-3|\ge2\pi t-3>0.
\]

The ratio estimate displayed in the report follows directly by dividing the literal summands. Its last step is valid uniformly in \(t\ge1,n\ge2\):
\[
 n^2\frac{2\pi n^2t+3}{2\pi t-3}\le3n^4,
\]
using \(\pi>3\). The majorant terms \(n^4e^{-3(n^2-1)/2}\) have successive ratio at most \((3/2)^4e^{-15/2}<1\), so their geometric sum is at most the stated
\[
\frac{48e^{-9/2}}{1-(81/16)e^{-15/2}}<\frac35.
\]
I ran the existing [exact-Fraction checker](../20261012_adaptive_spectral_tail/full_gamma_certificate/check_theta_strip_constants.py); it returns `ALL_PASS`, with the ratio upper bound \(39068406334789555738738008338202624/72948430300416205277377935950067739<3/5\). The independent coefficient check is \(146432/1519<100\). This is the only arithmetic replay in scope; no numerical interval certificate was rerun.

Thus \(\Phi\) has no zero in the right half of the strip. Evenness on the real axis extends to the common holomorphy strip by the identity theorem, so the same holds on the left. \(2\cosh(z/2)\) has no zero in \(|\Im z|<\pi/6\). Since this strip is simply connected, \(\Phi/(2\cosh(z/2))\) has a unique holomorphic square root after specifying the positive value at zero; uniqueness makes it even and its real restriction is the original positive \(m\). No zero-free assertion about \(\Xi\) is involved.

For \(|y|\le1/2\), the first summand and the \(3/5\) remainder give the stated coefficient bound on \(|\Phi(x+iy)|\). The denominator estimate
\[
|2\cosh((x+iy)/2)|\ge 2\cos(1/4)\cosh(x/2)\ge(31/32)e^{|x|/2}
\]
is valid; \(\cos(1/4)\ge31/32\). The rational constant checked above then yields
\[
|m(x+iy)|^2\le100e^{4|x|-(3/2)e^{2|x|}}.
\]
Direct substitution \(u=e^{2|x|}\) gives the stated uniform bounds \(\int|m(x+iy)|dx<40/3\) and \(\int|m(x+iy)|^2dx<25\). These also justify contour shifts at height \(1/2\). For the Gaussian–trigonometric source used in the certificate, the finite coefficient sum is bounded on the shifted contour by \(e^{1/4-x^2}A_{1/2}\); hence (7) follows from the actual whole-line multiplier, not from a sampled or periodic continuation.

## 2. Whole-band regularity and physical tails

Part I of `ACTUAL_NEGATIVE_BAND_COVERAGE.md` uses the original closed realization \(H=B-V\), with bounded, norm-convergent complete signed-prime perturbation and \(D(H)=D(B)\). Its weighted moments are for the actual paired coefficients \(m(x)m(x+\log n)\), summed over all prime powers; the exponential theta envelope makes that complete sum finite. The regularized Fourier multiplier is first shown to preserve the original operator domain at each fixed regularization parameter. Only then is the double-commutator identity applied. The Lyapunov inverse is taken for the operator \(K=-H|_{\operatorname{Ran}Q_\kappa}\ge\kappa\), so it proves a bound on the entire spectral projection, including arbitrary mixtures of different negative eigenvalues. The recursion and monotone regularization yield \(\|\langle D\rangle^rQ_\kappa\|<\infty\) for each fixed positive depth and each fixed order. No eigenbasis-wise estimate is being summed, and no regularity is assumed at depth zero.

Part II also works on the whole band. Before multiplying by a sharp cutoff, every vector of \(\operatorname{Ran}Q_\kappa\) is in \(D(H)\), since the spectral interval is bounded. The cutoff argument then uses the logarithmic Gamma form: its cross-boundary kernel is controlled by the two half-line Carleman operators (\(\pi/2\) each for the singular part) plus the integrable remainder. This gives form-domain invariance and the exact cutoff identity. It does **not** infer \(H^1\) from a discontinuous cutoff. The displayed \(D(R)=10000t(R)e^{R/2}\) is a full-space operator bound for the complete signed physical-prime operator \(\|1_{|x|\ge R}V\|\), with no source or prime truncation; \(E(R)=10t(R)e^{-R/2}\) pays the full Gamma cross. The constants convert to \(70000y^{5/4}e^{-\pi y/2}\) and \(70y^{3/4}e^{-\pi y/2}\) under \(y=e^{2R}\).

For a band vector, the identity \(B_\chi=D_q-(AK+KA)/2+E_\gamma\) is a closed-form identity. Positivity of \(B_\chi\), the full-prime bound, and the Gamma-cross bound give \(AK+KA\le2(zD(R)+E(R))I\). Applying the positive Lyapunov inverse gives \(z^2\le D(R)^2/\kappa^2+2E(R)/\kappa\). This is an operator inequality on the mixed band, not separate localization estimates for individual eigenvectors. The radius in Part II makes the central restriction injective and preserves the negative form after paying the pole term.

The claimed sharp-cutoff operator-domain passage is also supported by the associated-form criterion: polarizing the bounded Gamma cross identity and pairing against central form-domain tests represents the central operator by the eigen-equation plus bounded Gamma, prime, and pole cross terms. The central bounded perturbation leaves its operator domain equal to that of its Gamma restriction. This is the needed central-domain statement; no derivative rule for an indicator cutoff is used.

## 3. Fixed-order eigenstate tails and the Weil passage

The odd-domain report correctly starts with a genuine eigenvector in the original operator domain, not a smooth-core surrogate. The full-line realization reduces into even and odd parts: \(m\), \(b(D)\), the symmetric \(\pm\log n\) shifts, and the even cutoffs commute with reflection. The fixed-depth commutator and localization proofs use no parity-specific estimate. The odd eigenvector is automatically orthogonal to the even ground. Thus the even-band bounds restrict to the odd block with the same constants; conversely the even actual eigenvectors used in the Weil bridge are covered directly by \(Q_\kappa\).

For a fixed eigenvalue \(\lambda<0\), the report takes \(\kappa\le|\lambda|\). Its spatial estimate is
\[
T_\kappa(R)^2=D(R)^2/\kappa^2+2E(R)/\kappa,
\]
which decays faster than every exponential in \(R\) at fixed \(\kappa>0\). A smooth cutoff \(\eta_R\), equal to one outside \([-R,R]\), has uniformly bounded Sobolev multiplier norm; its \(L^2\) norm is bounded by \(T_\kappa(R-1)\), while its \(H^s\) norm is bounded by the band constant. The standard Gagliardo–Nirenberg interpolation therefore gives (5a) for every integer \(\ell<s\). Since \(\eta_R=1\) with zero derivatives on \(|x|\ge R\), the estimate is exactly for the tail of \(\partial^\ell w\). Summing shells proves \(e^{a|x|}\partial^\ell w\in L^2\) for every fixed \(a,\ell\). The constants may depend on \(\kappa,s,\ell\); no critical-depth or uniform-in-order claim is needed.

The theta series and its positive real lower bound imply, for every fixed \(k\),
\[
|m^{(k)}(x)/m(x)|+|m(x)(m^{-1})^{(k)}(x)|\le C_ke^{2k|x|}.
\]
One obtains this by differentiating the dominant \(n=1\) term and the normally convergent \(n\ge2\) remainder on each tail; on a compact interval use positivity of \(m\). The report does not display the constants \(C_k\), but only their finite existence is used. Combined with the weighted derivative tails, this gives the physical \(L^2\) differential powers \(G^jw,(-G^*)^jw\), and \(\partial^j(mw)\in H^1\) for every fixed \(j\).

The source eigen-equation \(T(mw)=\lambda w/m\) is used locally in distributions. The report explicitly avoids asserting that \(w/m\) or the unweighted source-side prime/Gamma expression is globally in \(L^2\). Differentiation is justified locally by the smooth representative and locally normally convergent complete theta-shift series; multiplication back by \(m\) gives the physical \(L^2\) vector. Closed-form pairing against the parity-preserving smooth graph core and the associated-operator criterion then puts each fixed \(G^jw\) in \(D(H_{\rm full})\). The pole-inclusive even-order identity similarly pays the rank-one term in physical \(L^2\) and does not claim a global identity on the maximal form domain.

For the even Weil extension, the same input chain gives all weighted derivatives of \(f=mv\) in \(L^1\cap L^2\), and hence of \(h=f*\widetilde f\). Expanding smooth cutoffs converge in weighted derivative norms. Four integrations by parts provide an integrable \((1+|t|)^{-4}\) majorant on the full zero strip; the complete Jensen count controls the zero sum with multiplicity. The Gamma and pole terms pass by the same derivative and weighted \(L^1\) bounds. The full prime series passes by \(|h(\pm\log n)|\le n^{-2}\|e^{2|x|}f\|_2^2\), leaving a summable \(\log n\,n^{-5/2}\) majorant. This is a valid passage from the compact-smooth Weil identity to an actual even band eigenstate. It does not make the off-critical zero terms positive; that step still uses the stated complete finite-height hypothesis and the separately evaluated tail inequality.

## 4. Sharp jumps and scope

The sharp indicator cutoff need not map into \(H^1\), and the audited proofs make no such assertion. It maps the logarithmic source form domain by the Carleman cross estimate. In Part III, the central trial function \(z\) can have an endpoint jump; its source \(mz\) is compactly supported BV, so \(|\widehat{mz}(t)|\le TV(mz)/|t|\). Since \(b(t)=O(\log(2+|t|))\), both the logarithmic form integral and the stronger \(L^2\) norm of \(b(D)(mz)\) converge. This is the appropriate associated-operator domain argument. The interpolation error has zero endpoint trace and is extended by zero in \(H^1\); the Poincare step is applied to that error, not to the jumped cutoff or trial source.

**Limits:** this audit validates source/domain prerequisites only. The weighted tail and derivative constants deteriorate as \(\kappa\downarrow0\); there is no \(\kappa=0\) regularity statement. The finite-height Weil argument and its interval-arithmetic output were not rerun here. The odd-domain report itself correctly concludes that its ladder and parity-transfer constraints do not exclude a negative odd eigenstate. No RH conclusion follows from this audit.
