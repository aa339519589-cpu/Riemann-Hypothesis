# Local critical-line large values and a length-adapted zero-density refinement

Let N(σ,T) count the nontrivial zeros β+iγ of the Riemann zeta function, with multiplicity, satisfying β≥σ and 0<γ≤T. All exponent losses below are arbitrary positive fixed numbers; constants may depend on the fixed parameters and losses.

**Theorem.** Put η=1−σ and define
\[
 E(\sigma)=
 \begin{cases}
 180\eta/(661\sigma-468),&87/100\le\sigma\le696/797,\\
 639\eta/(2227\sigma-1557),&696/797\le\sigma\le219/250.
 \end{cases}\tag{1}
\]
For every fixed σ in this complete interval [.87,.876] and every ε>0,
\[
 \boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}T^{E(\sigma)+\varepsilon}.}
\]
The two branches agree at 696/797.

At σ=7/8, the exponent is 639/3133, strictly below the previously established coefficient-one double-Gram exponent 1629/7985. The exact difference is 1242/25017005. The improvement is strict on the entire displayed interval, not only at this sample point.

The additional input proved here is a **local** critical-line large-value estimate, derived from established Huxley exponential-sum bounds and the Atkinson/Halász method. A common moment threshold is then adapted to the detector length. No local beta bound is asserted to be a global exponent pair, and no improved full moment is inferred from a local level-set improvement.

The comparison is to the identified predecessor and the stated density-table/Kerr curves. It is not a claim of exhaustive worldwide novelty, effective constants, a finite-height exclusion, a percentage of actual zeros, or RH.

## 1. Inputs and notation

Let R_T(v) be the largest cardinality of a 1-separated subset of [T,2T] on which |ζ(1/2+it)|≥T^v. Write X≺Y for X≪_ε T^εY for every ε>0. This notation permits arbitrarily small power losses, not merely logarithmic factors.

We use the exponential-sum function β from [1]. The established Huxley rows needed here are
\[
 b_0(z)=(13+94z)/146,
 \quad1424/4747\le z\le87/275,
\]
\[
 b_1(z)=(11+191z)/244,
 \quad87/275\le z\le423/1295.\tag{2}
\]
They occur in [1, Theorem 4.16/Table 4.1], and also in Theorem 4.14. We use the established global exponent pair
\[
 v_4=(89/1282,997/1282),
\]
which gives
\[
 b_4(z)=89/1282+454z/641\qquad(0\le z\le1).\tag{3}
\]
Reflection of β gives β(1−z)=1/2−z+β(z). The model-phase definition includes 2√x and perturbations of this phase tending to zero in every fixed derivative.

The B-transform of v_4 is (178/641,365/641). Trudgian–Yang [2, Lemma 5.1] therefore supplies the global critical-line bound
\[
 R_T(V)\ll T^\epsilon(TV^{-6}+T^{A_0}V^{-q_0}),
 \quad A_0=543/178,\quad q_0=1727/89,\tag{4}
\]
where R_T(V) denotes a separated count at level V. The notation R_T(v) above uses the level V=T^v. We also use Bourgain's pointwise exponent 13/84, only to terminate dyadic level integration.

For the detector we retain the complete coefficient-one Gram and common-length reduction in [5], using the exponent pair (k,l)=(13/84,55/84). Those inputs and their source closures are restated in Section 5.

## 2. A local large-value estimate with the whole correlation range

**Proposition.** Set
\[
 v_0=161/1110,\quad v_1=131/900,\quad v_2=307/2100,
\]
and
\[
 (A_L,q_L)=(60/17,386/17),\qquad
 (A_H,q_H)=(213/80,67/4).
\]
Then
\[
 R_T(v)\prec T^{L(v)},\qquad
 L(v)=\begin{cases}A_L-q_Lv,&v_0\le v\le v_1,\\
 A_H-q_Hv,&v_1\le v\le v_2.
 \end{cases}\tag{5}
\]
The two affine pieces join, and they meet the second term of (4) at the outer endpoints.

### 2.1 Atkinson reduction and removal of maxima

Use the Atkinson upper bound, phase truncation and removal of partial-sum maxima in [3, Lemmas 7.1, 7.3 and Corollary 7.2]. Their use is confined to the following stated reduction, not to Theorem 9.1 outside its range.

Put V=T^v and G=V²(log T)^−100. Group the original separated points into clusters of comparable size F≥1 and select 2G-separated cluster centers. Atkinson and dyadic subdivision give a common length
\[
 T^{1/3}\ll N\ll T/G^2\, (\log T)^2.\tag{6}
\]
For a parameter W with N≤W≤√(TN) and N^{1/2}W²≤T^{3/2}, subdivide the height interval into O(√(TN)/W) pieces. The transformed phases are
\[
 \phi_\theta(x)=\sqrt{x}+\theta x^{3/2},\qquad
 \theta=-\pi N/(12t_0)=O(N/T).
\]
After removing maxima in the **summed** inequality and pigeonholing the polynomial magnitude, [3, (57)] gives a level Z and a total retained count R_1 satisfying
\[
 Z\succ F(TN)^{1/4},\qquad R_1 Z\succ R_T(v)(TN)^{1/4}.\tag{7}
\]
The polynomial coefficients are bounded, apart from arbitrarily small losses. The transformed spacing is ≫G√(N/T). Splitting each transformed set into 1-separated sets therefore uses
\[
 O(1+G^{-1}\sqrt{T/N})
\]
parts. Equation (6) makes the total number of parts ≺T/(GW). We do not replace (7) by a pointwise common-Z statement before removing maxima, and do not discard a harmful cluster factor.

### 2.2 Halász–Montgomery absorption

For one 1-separated part of size R', with all polynomial magnitudes comparable to Z, duality and Cauchy give
\[
 R'^2 Z^2\le N\sum_{w,w'}\gamma_w\overline{\gamma_{w'}}
 \sum_{N<m\le2N}e((w-w')\phi_\theta(m/N)),
 \qquad |\gamma_w|=1.\tag{8}
\]
Thus the correlation sum has coefficients one, even though the original polynomials do not.

For 1≤|w−w'|≤N, the derivative has size comparable to |w−w'|/N, is monotone, and stays away from nonzero integers. Its sum is O(N/|w−w'|). Unit spacing pays the whole small-difference row by O(N²R' log T), including the diagonal. For larger differences, use the beta bounds for the model phase 2φ_θ, absorbing its fixed factor into the frequency. Since N≤T^{1−4v+o(1)} and v stays in the stated compact interval, θ→0 with all fixed derivative errors.

Write N=T^n and W=T^w at exponent level. It suffices to choose W so that, with a fixed small loss,
\[
 \sup_{n\le d\le w}d\,\beta(n/d)<(1-n)/2.\tag{9}
\]
The off-diagonal term in (8) is then absorbed using Z²/N≻F²T^{(1−n)/2}. Consequently R'≺N²/Z². Summing the parts and using both inequalities in (7) gives
\[
 R_T(v)\prec \frac{T^{1/2}N^{3/2}}{GWF}
 \le\frac{T^{1/2}N^{3/2}}{GW}.\tag{10}
\]

### 2.3 Paying every argument of β

Put
\[
 n_L=218/525,\quad n_M=94/225,\quad n_H=233/555.
\]
For n_L≤n≤n_M use, before a fixed small loss,
\[
 w_H(n)=61/40-35n/16,
\]
and for n_M≤n≤n_H use
\[
 w_L(n)=(73-125n)/34.\tag{11}
\]
The corresponding endpoint z=1−n/w ranges respectively over
[87/275,423/1295] and [102/335,87/275]. Reflection and (2) give
\[
 w\beta(n/w)\le(1-b)n+(a+b-1/2)w=(1-n)/2
\]
for the appropriate affine row a+bz. The selected formulas are exactly this balance.

To verify the full supremum in (9), define
\[
 F_b(z)=1+\frac{b(z)-1/2}{1-z}.
\]
For an affine row b(z)=a+bz, its derivative is (a+b−1/2)/(1−z)², positive for all three rows (2)–(3). Use b_4 from 0 to 102/335, b_0 from 102/335 to 87/275, and b_1 from 87/275 to 423/1295. These rows join exactly at both internal endpoints; b_1 also joins b_4 at 423/1295. All intervals lie inside their stated source ranges. Thus F_b is increasing on the complete cover. Every smaller difference in (9), including the reflected high-alpha portion, is paid by the endpoint balance. No local bound is inserted into an uncontrolled supremum.

For all smaller lengths 1/3≤n≤n_L, use the global B-transform pair and
\[
 w=\min\{(641-1015n)/356,\ 3/4-n/4\}.\tag{12}
\]
The first entry pays (9) by the global affine beta bound and the second pays phase truncation. Both are ≥n, and w≤(1+n)/2. Each formula in (11) satisfies all phase caps with a positive margin. They join at n_M; w_H joins the first entry of (12) at n_L.

The exponent in (10) is 1/2+3n/2−2v−w. In (12) it is the maximum of two affine functions increasing in n. In the H and L portions of (11), its n-slopes are respectively 59/16 and 88/17, both positive. Thus the complete range (6) is controlled at n=1−4v, producing precisely (5). The identities (1−n_H)/4=v_0, (1−n_M)/4=v_1 and (1−n_L)/4=v_2 give all endpoints.

Shrinking W by a fixed small power supplies strict absorption. The resulting loss is subsequently included in ε. Length endpoint log factors, small shifts in n, and compact uniformity are paid by the same fixed slack and a finite cover. This proves (5).

## 3. Two moments with one length-adapted threshold

Define L_0(v)=max{1−6v,A_0−q_0v}, and replace it by (5) on[v_0,v_2]. Call the resulting complete envelope L(v). It is continuous at all three joins and no larger than L_0. Its affine pieces all have positive intercepts and slopes strictly between −24 and −2.

Consequently L(v)/v is nonincreasing for positive v in the relevant range. Thus
\[
 rL(v/r)\le L(v)\qquad(0<r\le1)
\]
whenever the rescaled level is in range. The pointwise bound handles levels beyond that range. Dyadic height subdivision therefore extends estimates initially on[U,2U] to[0,U] with the same exponent. This radial closure is required before using moments in CDV.

For every fixed h∈[v_0,v_2] and H(U)=U^h, dyadic level integration gives
\[
 \int_0^U |\zeta(1/2+it)|^2\mathbf1_{|\zeta|\ge H(U)}\,dt
 \ll U^{L(h)+2h+\epsilon},\tag{13}
\]
\[
 \int_0^U |\zeta(1/2+it)|^{24}\mathbf1_{|\zeta|<H(U)}\,dt
 \ll U^{L(h)+24h+\epsilon}.\tag{14}
\]
Indeed L(v)+2v decreases above h, and L(v)+24v increases below h. The subunit contribution is O(U), and L(h)+24h>1. Both moments use the same threshold. These are truncated moments, not improved full moments.

The orders 2 and 24 are lawful in CDV, which requires each order to be at least2. Choose h after fixing σ, the detector length and subdivision parameters, and use H(T_0), not H(T), inside subdivisions. No threshold is selected separately for the two parts.

## 4. Parameters for the complete detector window

Let y=E(σ)/(4η), so
\[
 y=\begin{cases}45/(661\sigma-468),&87/100\le\sigma\le696/797,\\
 639/[4(2227\sigma-1557)],&696/797\le\sigma\le219/250.
 \end{cases}
\]
Set n_0=4y/3 and n_1=2y. As in [5], detector powering with ν=2 gives every n∈[n_0,n_1], with common multiset lengths N(A)≍N=T^n. Put
\[
 \alpha_2=E-2\eta n,\quad u=1-\alpha_2,
 \quad h(n)=\frac{(4\sigma-3)n}{2u}.\tag{15}
\]
The derivative of h(n) has the sign of (4σ−3)(1−E)>0. Define
\[
 c_j=\frac{2v_j(1-E)}{4\sigma-3-4\eta v_j},\qquad j=1,2,\tag{16}
\]
so h(c_j)=v_j. The exact certificate proves:
- on the lower σ branch, n_0≤c_1<c_2<n_1 and v_0<h(n_0)≤v_1;
- on the upper σ branch, n_0<c_2<n_1 and v_1≤h(n_0)<v_2.
Equality n_0=c_1 occurs only at the branch join and causes no missing interval.

On each local subwindow where h(n) lies in the L or H branch of (5), use its (A_j,q_j) and set
\[
 \alpha_1=\max\left\{0,
 \frac{uA_j-q_j(4\sigma-3)n/2+\alpha_2-E}{2}\right\}.\tag{17}
\]
For c_2≤n≤n_1, revert to the original common split from (4), with sixth and q_0 moments of exponents 1 and A_0, and set
\[
 \alpha_1=\max\left\{0,\frac{1+(9-12\sigma)n-E}{2},
 \frac{A_0-q_0(4\sigma-3)n/2-(A_0-1)\alpha_2-E}{2}\right\}.\tag{18}
\]
Finally δ_1=(1/2)T^−α1 and δ_2=T^−α2. The factor 1/2 ensures δ_1<1 even when α_1=0.

## 5. All detector and Gram terms retained

We use the coefficient-one Gram estimate of [5]: for a 1-separated set R in a length-U interval, N≤U,
\[
 Q(R,N)\ll U^\epsilon\bigl(|R|N^2+|R|^2U^{2k}N^{2(l-k)}\bigr).
\]
Its proof separates |t−t'|≤N, paid by the first derivative and spacing, from larger differences, paid by the exponent pair. CDV Lemma 4.2 makes both self-Gram polynomials coefficient one before this estimate is applied. The complete product has four terms, including the term requiring strict absorption. Their consequences, with k=13/84,l=55/84, are
\[
\begin{split}
 d_1&=2\eta n+\alpha_1+\alpha_2/2,\\
 d_2&=2k+(2+2l-2k-4\sigma)n+4\alpha_1-2k\alpha_2,\\
 d_3&=2k+(2+2l-2k-4\sigma)n+2\alpha_1+\alpha_2,
\end{split}\tag{19}
\]
and the indispensable absorption margin
\[
 g=(2\sigma-2l+2k)n-2k+k\alpha_2-2\alpha_1>0.\tag{20}
\]

For a common moment of order q' and exponent B, CDV Case 1 contributes the exponent
\[
 -2\alpha_1+(1-\alpha_2)B+\alpha_2-(4\sigma-3)q'n/2.
\]
Using B=A_j+(q'−q_j)h(n) from (13)–(14), both orders give exactly
\[
 -2\alpha_1+u[A_j-q_jh(n)]+\alpha_2.\tag{21}
\]
The **outer +α_2 is retained**. Equation (17) pays (21) by E. Equation (18) pays both original Case 1 terms on the other subwindow. The direct term δ_2^−1N^{2η} has exponent E identically.

The Case 2 lower interpolation has endpoints
\[
 N^{2\sigma}\delta_1^2RS,
 \qquad N^{2\sigma}\delta_1^{2/q'}\delta_2^{1-1/q'}
 R^{2-1/q'}S^{1/q'}.
\]
For every q'≥2, interpolation admits p=1/2 and p=1. Thus the order cancels from the three count rows (19), while the fourth product is absorbed only through (20). Changing the moment split has not changed or omitted a Case 2 term.

On each of the two or three subwindows, α_1 is a maximum of affine functions of n. Therefore all d_j are convex and g is concave. The certificate checks d_j≤E and g>0 at n_0,c_1,c_2,n_1 whenever applicable, with both adjacent definitions at each cut and every affine option separately. This proves the entire length window, not a sampled grid. It also checks 0≤α_1<1,0≤α_2<1 and n+α_2<1, ensuring N<T_0.

The original critical detector contour is retained. Class II is bounded using (4), with exponents
\[
 1-6(\sigma-1/2)y,\qquad A_0-q_0(\sigma-1/2)y.\tag{22}
\]
Both are at most E on the full σ interval. No local-LV estimate is needed for Class II.

The source closures below N=√T are exactly those of [5]: CDV Lemma 3.1's contour argument needs a fixed positive length exponent and polynomial upper length, not that lower bound; its subunit absorption uses σ>3/4 and n_0>0. The only removed N≥√T simplification was the Heath-Brown product, replaced by the coefficient-one Gram estimate. Common N(A)≍N, dyadic separation, the subunit |ζ|<1 split and all original smoothing losses remain.

## 6. Losses, comparisons and reproducibility

Choose all strict auxiliary losses first, including the W loss in Section 2 and a finite cover for the compact ranges of moment thresholds. Next take the original detector/smoothing losses sufficiently smaller than all positive parameter and absorption margins and the length conditions. Equalities in count exponents contribute only the final arbitrary ε. For any requested final ε these choices can be fixed so that their combined effect is below ε; no uniform constant as auxiliary losses tend to zero is asserted. Summing dyadic heights proves (1).

Write y_D=1629/[4(5831σ−4104)]. On the overlap σ≥.873, the predecessor [5] gives y_D. Below .873, report [6] gives y_D up to 8751/10033 and then y_H=948/(11929σ−8119). Exact positive-denominator cross multiplication proves y<y_D throughout and y<y_H on the additional overlap. Thus the complete interval improves the applicable published predecessors. The accompanying checker also compares 4y with 3/(2σ) and, above 7/8,3/(10σ−7). These are the applicable identified density-table/Kerr curves; the broader 3/(2σ) curve includes the later claimed source of that form. Its strict improvement here does not settle unrelated literature comparisons.

Run `python3 check_certificate.py`. It uses only the Python standard library and exact rational polynomial arithmetic. The endpoint signs are proved by Bernstein coefficients, not samples. It checks the whole beta-prefix cover, all phase caps, the continuous moment envelope, all length subwindows, both zero classes, parameter margins and the stated comparisons. The finite algebra does not prove its cited analytic inputs or worldwide novelty.

## References

[1] Analytic Number Theory Exponent Database, [beta chapter](https://teorth.github.io/expdb/blueprint/beta-chapter.html), Definition 4.1, reflection Lemma 4.10, Theorems 4.14 and4.16/Table4.1; [exponent-pair chapter](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html), pair v_4 and the standard B-process. The local rows are attributed to Huxley's 1993 theorem and 1996 book tables. We use only their displayed valid ranges.

[2] T. S. Trudgian and A. Yang, [Toward optimal exponent pairs](https://arxiv.org/html/2306.05599v3), Lemma 5.1, the two-term critical-line large-value estimate. Only that large-value lemma is used; its later moment optimizations are not needed here.

[3] A. de Faveri and M. Pandey, [The sixth moment of the Riemann zeta function](https://arxiv.org/html/2610.01035v1), §§7 and9, especially Lemmas 7.1,7.3, Corollary 7.2 and formulas (54)–(57),(63). The present argument uses their explicit reduction machinery, not their new large-value theorem outside its stated range and not their Iwaniec close-pair input.

[4] B. Chen, G. Debruyne and J. Vindas, [On the density hypothesis for L-functions associated with holomorphic cusp forms](https://ems.press/content/serial-article-files/48886), §§2–4 and Appendix A. Revista Matemática Iberoamericana 40 (2024), no. 6, 2179–2202, DOI 10.4171/RMI/1481. The proof uses its general common-threshold formulation (3.3) and the complete Case 1/Case 2 construction.

[5] [Exponent-pair double-Gram bounds in a zeta zero detector](../20261016_cdv_ep_gram_density/REPORT.md), published repository report. This supplies the already checked full detector/Gram replacement and its source closures; all changed moment and local-LV steps are proved above.

[6] [Full-diagonal variable-detector zero-density refinement](../20261016_cdv_full_diagonal_density/REPORT.md), the earlier complete detector specialization used only for the comparator below .873.
