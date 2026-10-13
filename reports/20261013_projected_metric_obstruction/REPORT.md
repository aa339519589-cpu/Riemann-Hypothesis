# The full theta projection does not symmetrize the reflected derivative

Date: 2026-10-13. Projection away from the closed span of all known theta-derivative zero modes does **not** repair the reflected-energy symmetry defect. We prove that the projection of certain oscillatory compact sources tends to zero uniformly against that entire closed span. Their projected differential pairing then has a nonzero imaginary part. The same obstruction holds for every positive linear combination of the positive ground form and the reflected-prime form.

This rules out these particular projected metrics as a way to make the source second derivative self-adjoint. It establishes no negative vector for the original Weil form and no RH conclusion. The known theta span is not assumed to be the entire kernel of the original operator.

## 1. Exact energies and the projected core relation

Use the complete theta source and normalization from [SOURCE_FORM.md](../20261012_localized_odd_schur/SOURCE_FORM.md) and the [reflected-energy report](../20261013_reflected_prime_energy/REPORT.md). Put
\[
 \psi=-\Phi'>0\quad(x>0),\qquad s_0(x)=\sinh(x/2),\qquad
 d_n=\log n,\quad \alpha_n=\Lambda(n)/\sqrt n,
 \quad\kappa(u)=\frac{e^{-u/2}}{1-e^{-2u}}.
\]
The positive source weight has a simple zero at zero,
\(\psi(x)=c_\psi x+O(x^3)\), \(c_\psi>0\), and
\(\psi(x)\asymp e^{13x/2}e^{-\pi e^{2x}}\) at infinity. These facts and all fixed-derivative theta tail bounds are proved in Section 6 of the linked reflected-energy report. The normalization gives
\(\int_0^\infty\psi(x)s_0(x)dx=1/8\).

Let \(\mathcal C\) be the smooth compact ratio core on the positive half-line with smooth even extension at zero. The associated odd source is \(g=\psi r\). Define the complete forms
\[
 N[r]=\sum_{n\ge2}\alpha_n\int_0^{d_n}
       \psi(x)\psi(d_n-x)|r(x)-r(d_n-x)|^2dx,
 \tag{1}
\]
\[
 P[r]=P_\Gamma[r]+P_{\rm pole}[r]+P_{\rm forward}[r],
 \tag{2}
\]
\[
 P_\Gamma[r]=\iint_{(0,\infty)^2}\psi(x)\psi(y)
 [\kappa(|x-y|)-\kappa(x+y)]|r(x)-r(y)|^2dxdy,
\]
\[
 P_{\rm pole}[r]=4\iint\psi(x)\psi(y)s_0(x)s_0(y)|r(x)-r(y)|^2dxdy,
 \quad
 P_{\rm forward}[r]=2\sum_{n\ge2}\alpha_n\int_0^\infty
 \psi(x)\psi(x+d_n)|r(x)-r(x+d_n)|^2dx.
\]
All three pieces of \(P\) are nonnegative. Every prime power is retained. On this core the exact odd source identity is
\(\mathfrak A[\psi r]=P[r]-N[r]\). The complete source form, including its coefficient-two polar term, commutes with \(\partial_x^2\) on compact odd tests; see [the operator-domain report](../20261013_odd_operator_domains/REPORT.md), equation (1). These are core identities, not an assertion that the two raw prime forms are separately finite on the entire original maximal domain.

Write \(v(r)=\nabla_Nr\), with components \(r(x)-r(d_n-x)\), and let
\(K_N=\overline{v(\mathcal C)}\) in the edge direct sum with measures
\(\alpha_n\psi(x)\psi(d_n-x)dx\). Its inner product is conjugate-linear in the first slot. For
\[
 f_j=\Phi^{(2j+3)}-\tfrac14\Phi^{(2j+1)},\qquad r_j=f_j/\psi,
\]
define
\[
 S_N=\overline{\operatorname{span}}\{v(r_j):j\ge0\},\qquad Q_N=I-P_{S_N}.
 \tag{3}
\]
The fixed theta jets have finite \(P\) and \(N\) energy and are limits of expanding smooth cutoffs in both energies. This follows from their at-most-exponential ratio growth, the theta weights, and the local Gamma estimate \(|\chi_R(x)-\chi_R(y)|\le C\min(1,|x-y|)\).

Set \(\mathcal B_\psi r=(\psi r)''/\psi\). This maps \(\mathcal C\) into itself: numerator and denominator are odd and the denominator has a simple zero at zero. We study the projected core pairs
\[
 \mathscr R_N=\{(Q_Nv(r),\ Q_Nv(\mathcal B_\psi r)):r\in\mathcal C\}.
 \tag{4}
\]
Our conclusion is that no symmetric operator can have a graph containing all of (4). It does not require assuming that (4) already defines a single-valued operator or importing a zero-counting theorem.

## 2. Local compactness for the full closed jet unit ball

The complete source identities give \(Tf_j=0\) and
\(\ell(f_j)=\int_{\mathbb R}s_0(x)f_j(x)dx=0\). Hence, on every finite neutral jet combination,
\[
 P[r_u]=N[r_u]=\|u\|_{K_N}^2,\qquad u=v(r_u),\quad g_u=\psi r_u,
 \quad\int_0^\infty s_0g_u=0.
 \tag{5}
\]
The same identities follow first on cutoffs and then by the two-energy convergence stated above. These neutral jets span the same gradient space as all odd theta derivatives: \(\Phi'/\psi=-1\) has zero gradient, and
\(\Phi^{(2j+3)}=f_j+\Phi^{(2j+1)}/4\).

Expansion of the positive pole square gives, for an odd source with positive wing \(g\),
\[
 P_{\rm pole}[g/\psi]
 =\int_0^\infty W(x)|g(x)|^2dx-2|\ell(g)|^2,
 \qquad W(x)=\frac{s_0(x)}{\psi(x)},
 \quad\ell(g)=2\int_0^\infty s_0g.
 \tag{6}
\]
Therefore (5) and positivity of the three components imply
\[
 \int W|g_u|^2\le\|u\|_{K_N}^2,\qquad
 P_\Gamma[r_u]\le\|u\|_{K_N}^2.
 \tag{7}
\]
The source representative is unique: two finite neutral representations with the same gradient have zero \(N\) and therefore zero weighted source norm by (5)--(7).

These estimates extend to every \(u\in S_N\). For a jet sequence Cauchy in \(K_N\), (7) makes its sources Cauchy in \(L^2(Wdx)\). Their limit defines \(g_u\), independently of the sequence. The neutral moment passes to the limit because
\(\int s_0^2/W=\int\psi s_0<\infty\). An almost-everywhere subsequence identifies the limit gradients with \(v(g_u/\psi)=u\): reflection preserves null sets and there are countably many edge labels. Fatou's lemma for the positive Gamma kernel proves the second estimate in (7) for the limit. No pointwise representative for an arbitrary unrelated element of \(K_N\) is assumed.

Fix compact intervals \(I\Subset J\Subset(0,\infty)\). The first estimate in (7) controls \(\|r_u\|_{L^2(J)}\), because \(\psi s_0\) is bounded below on \(J\). For \(x,y\in J\), the second estimate controls the local increment integral
\[
 \int_{J^2,\ |x-y|<\delta}
       \frac{|r_u(x)-r_u(y)|^2}{|x-y|}\,dxdy
 \le C_J\|u\|_{K_N}^2.
 \tag{8}
\]
Indeed \(\psi\) is bounded above and below there, \(\kappa(x+y)\) is bounded, and \(\kappa(|x-y|)\ge c_J/|x-y|\) at small distance. The bounded subtraction is paid by the local \(L^2\) estimate.

Multiply by a smooth cutoff supported in \(J\), equal to one near \(I\). The cutoff differences pay the local singularity, and pairs outside \(J\) are separated from the cutoff support, so (8) controls the full truncated increment norm of this localized function. Its Fourier multiplier
\[
 \int_{|h|<\delta}\frac{|e^{ith}-1|^2}{|h|}dh
\]
grows like \(\log|t|\). Thus the localized Fourier \(L^2\) tail is uniformly small as the frequency cutoff tends to infinity. At each fixed frequency cutoff the operator from a bounded spatial interval is Hilbert--Schmidt. This proves relative compactness in \(L^2(I)\). Multiplication by smooth \(\psi\) preserves it. In particular,
\[
 \{g_u|_I:u\in S_N,\ \|u\|_{K_N}\le1\}
 \quad\hbox{is relatively compact in }L^2(I).
 \tag{9}
\]
The estimate is for the entire closed jet unit ball.

## 3. Vanishing high-frequency projections, with the complete prime tail

Put
\[
 L(x)=\sum_{n>e^x}\alpha_n\psi(d_n-x),\qquad V_N(x)=L(x)/\psi(x).
\]
For \(0\le x<\log2/2\) all labels are active and their theta-derivative sums converge locally normally. Consequently
\[
 V_N'(x)=-\frac{L(0)}{c_\psi x^2}+O(1)<0
\]
for sufficiently small positive \(x\), with \(L(0)>0\). Choose a fixed interval
\(I=(a,b)\), \(0<a<b<\log2/2\), within that region.

For any fixed real amplitude \(\phi\in C_c^\infty(I)\), define
\[
 g_{\phi,t}(x)=\phi(x)e^{itx},\quad
 r_{\phi,t}=g_{\phi,t}/\psi,\quad v_{\phi,t}=v(r_{\phi,t}).
 \tag{10}
\]
We prove
\[
 \|P_{S_N}v_{\phi,t}\|_{K_N}\longrightarrow0\qquad(t\to\infty).
 \tag{11}
\]
For any finite neutral jet and then every \(u\in S_N\), the exact reflected-source expansion is
\[
 \langle u,v_{\phi,t}\rangle
 =2\int V_N\overline{g_u}\phi e^{itx}dx
 -2\int_0^\infty\overline{g_u(x)}H_{\phi,t}(x)dx,
 \quad H_{\phi,t}(x)=\sum_{n\ge2}\alpha_n\phi(d_n-x)e^{it(d_n-x)}.
 \tag{12}
\]
The extension to the closed span is justified by (7) and the bounds below; it does not assume pointwise convergence of an infinite jet expansion.

On \(x\le R\), only finitely many reflected labels can meet \(I\), since \(n\le e^{R+b}\). Their supports are bounded away from zero: their left endpoints are at least \(\log2-b>0\). Each contribution is a fixed amplitude with carrier \(e^{-itx}\), times a scalar phase of modulus one. Equation (9) and a finite-net argument give the Riemann--Lebesgue limit uniformly over \(\|u\|\le1\) for this finite part. The direct first term in (12) has the same property on \(I\).

For the remaining complete tail, integer counting and \(\Lambda(n)\le\log n\) give
\[
 |H_{\phi,t}(x)|\le C_\phi(1+x)e^{x/2}\qquad(x\ge0),
 \tag{13}
\]
uniformly in \(t\). An active term has \(e^{x+a}<n<e^{x+b}\); its coefficient is at most \((x+b)e^{-(x+a)/2}\), and there are at most \(e^{x+b}\) terms. Hence, for \(\|u\|\le1\),
\[
 \left|\int_R^\infty\overline{g_u}H_{\phi,t}\right|
 \le C_\phi\left(\int_R^\infty
       (1+x)^2e^x\frac{\psi(x)}{s_0(x)}dx\right)^{1/2}
 \longrightarrow0
 \tag{14}
\]
as \(R\to\infty\), uniformly in \(u,t\). The theta tail pays this integral. Taking \(R\) large first and then \(t\) large proves (11). No fixed-rank truncation of \(S_N\) has been used.

## 4. A nonreal pairing after the full projection

Choose nonzero real \(\chi\in C_c^\infty(I)\), and abbreviate
\(v_{j,t}=v_{\chi^{(j)},t}\), \(j=0,1,2\). Since \(I+I\subset(0,\log2)\), every direct reflected source correlation between two such amplitudes vanishes. The exact pairings are
\[
 \langle v_{j,t},v_{k,t}\rangle
 =2\int_I V_N(x)\chi^{(j)}(x)\chi^{(k)}(x)dx.
 \tag{15}
\]
They are real, and \(\|v_{0,t}\|^2=2\int_I V_N\chi^2>0\) is independent of \(t\).

Differentiation gives
\[
 v(\mathcal B_\psi r_{\chi,t})=-t^2v_{0,t}+2itv_{1,t}+v_{2,t}.
\]
Thus (4) contains the pair
\[
 u_t=Q_Nv_{0,t},\qquad
 z_t=-t^2Q_Nv_{0,t}+2itQ_Nv_{1,t}+Q_Nv_{2,t}.
 \tag{16}
\]
Equation (11) holds for all three amplitudes. The term \(-t^2\|Q_Nv_{0,t}\|^2\) is exactly real; no estimate on a \(t^2\) projection error is required. The remaining projection corrections are \(o(t)\) and \(o(1)\), respectively. Consequently
\[
 \boxed{\quad
 \lim_{t\to\infty}\frac{\operatorname{Im}\langle u_t,z_t\rangle}{t}
 =4\int_I V_N\chi\chi'
 =-2\int_I V_N'\chi^2>0.
 \quad}
 \tag{17}
\]
Also \(\|u_t\|^2\to2\int_I V_N\chi^2>0\). Hence, for all sufficiently large \(t\), (4) contains a nonzero-input pair with nonreal diagonal pairing. No symmetric operator can agree with all projected-core pairs. If the projected core relation is realized as an operator, that operator is not symmetric.

The use of a complex carrier is merely convenient notation: its real and imaginary parts are real compact odd-source tests. The same nonzero skew pairing is therefore a real two-test obstruction, not an assumption about complex zeta zeros.

## 5. Positive combinations of the two exact energies also fail

Let \(a_0,b_0\ge0\), \(a_0+b_0>0\), and put
\(M=a_0P+b_0N\), with its edge gradient
\(v_M(r)=(\sqrt{a_0}\nabla_Pr,\sqrt{b_0}\nabla_Nr)\).
Let \(K_M=\overline{v_M(\mathcal C)}\) in the indicated positive
edge direct sum. The two-energy cutoff convergence places the jet images
in \(K_M\). Let \(S_M\subset K_M\) be their closed span, and
\(Q_M=I-P_{S_M}\). The exact mixed source-null identity gives
\[
 M(r_j,r)=(a_0+b_0)N(r_j,r)
\]
for every jet and core test, and by two-energy cutoff passage for all vectors of the closed jet subspace. It follows that
\[
 \|P_{S_M}v_M(r_{\phi,t})\|
 =\sqrt{a_0+b_0}\,\|P_{S_N}v_{\phi,t}\|\longrightarrow0.
 \tag{18}
\]
The pole-inclusive source identity \(\mathfrak A=P-N\) commutes with \(\partial_x^2\) on compact odd sources. Therefore its skew pairing is zero, and the raw skew pairings of \(P\) and \(N\) are equal. The raw skew pairing of \(M\) is \(a_0+b_0\) times that of \(N\). Applying the same three-amplitude calculation as in Section 4 yields
\[
 \boxed{\quad
 \lim_{t\to\infty}\frac1t\operatorname{Im}
 \langle Q_Mv_M(r_{\chi,t}),\ Q_Mv_M(\mathcal B_\psi r_{\chi,t})\rangle
 =-2(a_0+b_0)\int_I V_N'\chi^2>0.
 \quad}
 \tag{19}
\]
Thus neither \(P\), nor \(N\), nor any of their nonzero positive linear combinations makes this fully projected differential core symmetric. This is not a claim about the sign of the difference \(P-N\). The original Weil inequality and its full Green-load comparison remain unproved.
