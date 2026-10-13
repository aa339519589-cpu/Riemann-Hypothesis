# Independent mathematical review: the complete Green bound 21/20

Date: 2026-10-14 (UTC+8). The complete proof in
[GREEN_BAND_LOG_COST.md](GREEN_BAND_LOG_COST.md), preserved at commit
`75bb1a284a8b23b3dedf3580b356ee7f220b23f0`, passes this independent review
under its explicitly cited original-domain, full-tail and finite-height
inputs. In particular its conclusions are

\[
\|\mathcal Ua\|^2\le
\left(8705+544\log\frac{1+\varepsilon}{\varepsilon}\right)\|a\|_P^2,
\qquad
0\le K\le\frac{21}{20}I.
\tag{R1}
\]

The first estimate holds on the entire actual band
\(E_\varepsilon=\operatorname{Ran}\mathbf1_{[1+\varepsilon,\infty)}(T^*T)\),
including arbitrary mixtures and all multiplicities. Its form identity
and the stated one-sided spectral-count comparison also pass. The
interval \((1,21/20)\), the coefficient-one comparison and RH remain open.

The archived draft's original pending-review status and provenance are
left intact. This document supplies the subsequent mathematical review;
it does not rewrite the archived source or claim that a matching file hash
proves a theorem.

## 1. Exact polar normalization and the new complete-theta estimate

With the source conventions in the paper, \(\int w=1/8\) and
\(\int wr=0\). Direct expansion gives

\[
P_{\rm pole}[r]=4\iint w(x)w(y)|r(x)-r(y)|^2\,dx\,dy
=\int w|r|^2-8\left|\int wr\right|^2=\int w|r|^2.
\tag{R2}
\]

Thus the centered polar variance is available with coefficient exactly
one. No full-line factor is hidden in this positive-wing identity.

We independently differentiated the complete positive theta summands
\(f_n=e^{x/2}(4u_n^2-6u_n)e^{-u_n}\), \(u_n=\pi n^2e^{2x}\), and obtained

\[
q_n=-f_n'/f_n=2u_n-\frac92-\frac6{2u_n-3},\qquad
q_n'=4u_n+\frac{24u_n}{(2u_n-3)^2}\le4u_n+8.
\]

For \(p_n=f_n/\Phi\), differentiating the actual weights, rather than
holding them fixed, gives

\[
q'=\sum_np_nq_n'-\operatorname{Var}_{p}(q_n)
\le\sum_np_nq_n',\qquad q=-\Phi'/\Phi.
\tag{R3}
\]

Normal convergence pays these differentiations at and beyond zero. The
whole \(n\ge2\) theta tail is bounded by a geometric series: its adjacent
ratio is at most \((3/2)^6e^{-15}<1/4\), and its sum is less than
\((4/3)64e^{-9}<1/64\). These follow already from \(e^3>20\).
Keeping the first positive denominator term yields
\(\sum p_nu_n\le(65\pi/32)e^{2x}\). Consequently

\[
q'<34e^{2x},\qquad q(0)=0,
\qquad q(x)\le17(e^{2x}-1).
\]

The coth simplification in the draft is exact:
\(\coth(x/2)(e^{2x}-1)=e^{2x}(1+e^{-x})^2\). Hence

\[
\frac{\psi}{m^2\sinh(x/2)}\le136e^{2x},\qquad
2\int_0^R\frac{|\psi r_a|^2}{m^2}\,dx
\le272e^{2R}\|a\|_P^2.
\tag{R4}
\]

The last factor two is precisely the odd full-line norm conversion.
All theta summands and their tails are retained.

## 2. Mixed spectral parameters, full rows and original domains

The source equation has auxiliary eigenvalue \(-2\delta\), where
\(\delta=1-\lambda^{-1}\). On the whole finite band the correct parameter
is the operator \(\Delta=I-(T^*T)^{-1}\), with
\(\Delta\ge\delta_0I\), \(\delta_0=\varepsilon/(1+\varepsilon)\).
The draft's column equation

\[
\mathcal BV+2V\Delta
=2C_0M_{\mu^2}V+2\mathcal FV
+8|e\rangle\langle e|V-2\mathcal RV(I-\Delta)
\tag{R5}
\]

has the correct signs, both forward rows, the entire reflected row and
the coefficient-eight half-line pole. The pole vanishes on the centered
image, but retaining its row bound is valid. No commutation through \(V\)
is used.

The sharp cutoff need only preserve the established auxiliary form
domain. The complete Gamma cross-form block is bounded there. For its
outer restriction \(\mathcal B_R\ge0\), the cutoff equation therefore gives
\(\mathcal B_RX_R+2X_R\Delta=Y_R\) in the weak form sense. On each
\(\Delta\)-eigenvector, the bounded right side puts the column in
\(D(\mathcal B_R)\). Thus the unique solution is the operator-norm integral

\[
X_R=\int_0^\infty e^{-t\mathcal B_R}Y_Re^{-2t\Delta}\,dt,
\qquad \|X_R\|\le\frac{\|Y_R\|}{2\delta_0}.
\tag{R6}
\]

The inherited full row bound is exactly
\(\|Y_R\|\le256e^RM(R)\|V\|\), with
\(M(R)=128e^{7R/2-\pi e^{2R}/2}\). Its complete prime-power and Gamma tails
apply unchanged because \(\|I-\Delta\|\le1\). Together with
\(\|V\|^2\le193\), this yields the draft's dimension-free tail

\[
\|\mathbf1_{x>R}V|_{E_\varepsilon}\|^2
\le193\,2^{28}\delta_0^{-2}e^{9R-\pi e^{2R}},\qquad R\ge7/5.
\tag{R7}
\]

This agrees with equation (4) of the already published
[WHOLE_SUPERCRITICAL_BAND.md](../20261013_full_prime_green_reference/WHOLE_SUPERCRITICAL_BAND.md),
which obtains the same bound using a positive Lyapunov inverse. The
dimension-free logarithmic order and minmax mechanism were already
published there. The new contributions here are (R4), the explicit
constant in (R1), and the complete numerical threshold 21/20.

Using \(\mu^2/m^2\le2048e^{3x}\), Stieltjes integration of (R7) gives the
half-line physical tail with coefficient \(193\,2^{40}\). Its boundary
term at infinity vanishes; \(2\pi e^{2R}-12>84\) pays the integral. Adding
(R4) and doubling only the half-line tail gives exactly

\[
\|\mathcal Ua\|^2\le
\left[272e^{2R}+193\,2^{41}\delta_0^{-2}e^{12R-\pi e^{2R}}\right]\|a\|_P^2.
\tag{R8}
\]

The full source already has finite logarithmic Gamma form. Physical
\(L^2\), now supplied by (R8), puts it in the original odd physical form
domain and identifies its complete form value with \(P-N\). An original
operator-domain assertion is unnecessary. The resulting strict negative
form identity proves injectivity on the band. Form minmax, including the
closed threshold \(-\varepsilon/C_\varepsilon\), and the polar decomposition
of \(T\) give the stated spectral-count inequality.

## 3. Explicit constants and the whole-space threshold

Set \(L_0=\log(1/\delta_0)\) and \(e^{2R}=32+2L_0\). The tail coefficient
in (R8) is bounded by

\[
193\,2^{41}e^{2L_0}(32+2L_0)^6e^{-\pi(32+2L_0)}
<2^{79}e^{-96}e^{-29L_0/8}<1.
\]

The central coefficient is \(272(32+2L_0)\), proving the constants
\(8705\) and \(544\) without a band-dimension factor.

For the separate threshold conclusion, take a genuine \(\lambda\ge21/20\)
eigen-source with \(P[r]=1\), set \(\varepsilon=\lambda-1\), and note
\(\delta_0=\delta\ge1/21\). At \(R=7/5\), (R8) and the certified tail give

\[
\|u\|^2<272\cdot17+\frac{2\cdot193\cdot21^2}{1000}
=\frac{2397113}{500}<5000.
\]

The original odd bound \(H_o\ge-10^{-5}I\) is Section 1, equation (2), of
[THREE_HALVES_BOUND.md](../20261013_full_prime_green_reference/THREE_HALVES_BOUND.md).
With the exact form normalization \(\mathfrak h_o[u]=-(\lambda-1)\), it
contradicts \(\lambda-1\ge1/20\), with margin

\[
\frac1{20}-\frac{2397113}{50000000}
=\frac{102887}{50000000}>0.
\]

The established compactness of \((K-I)_+\) makes every spectral point above
one an actual finite-multiplicity eigenvalue. Thus this exclusion applies
to the entire Green operator, not a finite matrix. Equivalently,
\(N\le(21/20)P\) on the actual completion and
\(\Gamma_P[h]\le(21/20)\|h\|_N^2\) on all reflected currents.

## 4. Reproduction, provenance and remaining boundary

The archived proof's SHA-256 is
`3ad61b007cc8775c7f07613172c62ed61475dceae1fc20aebf0aab4bc424f3e2`.
Its three manifest entries were checked against the actual fetched files.
The [user's scalar script](verify_green_band.py) was independently read and
executed; its output was byte-identical to [verification.json](verification.json).
A separately written standard-library Fraction calculation independently
checked the complete theta-tail geometric bound, the rational coefficient
\(939/28\), \(e^{14/5}<17\), the physical-tail scalar, the logarithmic
constants and the strict threshold margin. Both calculations use rational
Machin bounds for \(\pi\) and Taylor sums with explicit remainder bounds.
The existing published script is sufficient for reproduction, so no
duplicate script or second copy of the proof is added.

The mathematical review separately checked the source normalization,
theta variance, auxiliary forms and Sylvester domain passage, full rows,
physical embedding and minmax. Scalar execution and file matching are not
substitutes for these arguments. No proof-assistant certification is claimed.

The finite-height input remains the previously used verification through
height \(3\cdot10^{12}\); no additional zeta-zero computation or exclusion
is asserted. As \(\varepsilon\downarrow0\), the transferred physical depth
still tends to zero. The actual \(\kappa^{-2}\) sampling cost and signed
low/high coupling in INFINITE_HIGH_TAIL.md are not settled by the band
norm estimate. In particular the full comparison \(K\le I\) remains open.
