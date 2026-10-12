# Independent mathematical review 27: tracked line plus full collar

## Verdict and scope

The claimed positivity of the compression to
\[
\operatorname{span}\{g_k\}\oplus\mathcal N_k,
\qquad g_k=\chi_k f_0,
\]
is justified for all sufficiently large integer \(k\), conditional on the displayed source identification and on a fixed cutoff family satisfying the hypotheses below. The scalar margin is genuinely positive: it is at least
\((\delta\log k-C)\|r_k\|_2^2\), with a fixed \(\delta>0\).

The main proof now includes the complete post-coefficient prime series reproduced below. Its cutoff range and fixed derivative hypotheses are explicit.

This result is exactly a one-old-line/full-new-collar compression. It does not short or eliminate the remaining old modes, prove positivity on the entire next source window, establish an all-depth sign, or imply RH.

## Hypotheses and source/form domain

Use
\[
a_k=\tfrac12\log k,\quad h_k=a_{k+1}-a_k,
\quad R_k=a_k-k^{-1},\quad
g_k=\chi_kf_0,\quad r_k=(1-\chi_k)f_0,
\]
where \(\chi_k\) is real, even, smooth, \(0\leq\chi_k\leq1\), equals one for \(|x|\leq R_k\), vanishes for \(|x|\geq a_k\), and has fixed-in-\(k\) bounds
\(\|\chi_k^{(j)}\|_\infty\leq C_j k^j\). Constants below may depend on those fixed derivative constants and the fixed theta normalization. Put
\[
T=a(D)-S,\quad
(Sf)(x)=\sum_{n\geq2}\alpha_n\{f(x+\log n)+f(x-\log n)\},\quad
\alpha_n=\Lambda(n)/\sqrt n,
\]
with the full prime-power sum, \(a(t)=b(t)-C_0\), and
\[
b(t)=\operatorname{Re}\psi(\tfrac14+\tfrac{it}{2})-\psi(\tfrac14),
\qquad C_0=\gamma+\tfrac\pi2+3\log2+\log\pi.
\]
The source form is the odd support compression
\[
A_{k+1}=P_{k+1}TP_{k+1}-2|s_{k+1}\rangle\langle s_{k+1}|,
\qquad s(x)=\sinh(x/2),
\]
as a form. SOURCE_FORM.md defines exactly this form, normalization and coefficient 2. The review applies to that explicitly defined source form. It is important that this is the polar-inclusive source operator; it is not the repository's even weighted operator \(H\).

The domain citation is appropriate. `SHARP_WINDOW_DOMAIN.md` proves the maximal Gamma difference-form domain splits under the sharp old/collar support projections by first truncating the positive kernel and then passing to the limit. Its referee, `REFEREE_DOMAIN.md`, verifies that the active prime translations on each fixed window are finite bounded perturbations, and that the polar rank-one term is bounded there. Consequently the induced old and collar form domains are a direct sum, the old-to-collar block is bounded for fixed \(k\), and completing the collar square on that restricted form domain is legitimate. This does not assert positivity of any full-old Schur form.

## Tail scalar and old polar term

The exact whole-line source equation is used before localization. Pairing \(Tf_0=0\) with \(g_k\) and \(r_k\) in the complete symmetric form, and using real-valuedness and symmetry, gives
\[
q_T[g_k]=q_T[r_k].
\]
This is not a truncation of the prime sum. For each fixed \(k\), the theta tails make the complete prime correlations absolutely convergent, so both pairings are defined.

The lower-tail lemma `../20261012_narrow_theta_tail/NARROW_TAIL_LOWER.md` applies with precisely the cutoff range and support conditions above. It proves
\[
q_T[r_k]\geq(\log k-C)\|r_k\|_2^2,
\quad \|r_k\|_2^2\geq c k^{19/2}e^{-2\pi k},
\quad \|r_k\|_1^2\leq Ck^{-1}\|r_k\|_2^2,
\quad \|r_k'\|_2\leq Ck\|r_k\|_2.
\]
The lower lemma controls the full Gamma symbol and every prime power; its sign argument drops only the favorable opposite-tail correlations. The matching upper lemma `../20261012_narrow_theta_tail/NARROW_TAIL_UPPER.md` is also in scope: its Gamma estimate uses only the fixed first-derivative bound, and its prime upper bound enlarges the complete prime-power sum to all integer shifts. Together they give
\[
q_T[r_k]=(\log k+O(1))\|r_k\|_2^2.
\]

Global polar neutrality follows by integration by parts and decay:
\(\langle s,f_0\rangle=0\), hence \(\langle s,g_k\rangle=-\langle s,r_k\rangle\). The theta tail gives
\[
|\langle s,g_k\rangle|\leq Ck^{-1/4}\|r_k\|_2.
\]
Therefore the old scalar for the actual coefficient-2 polar-inclusive form is
\[
a_{A,k}=q_T[g_k]-2|\langle s,g_k\rangle|^2
=(\log k+O(1))\|r_k\|_2^2.
\]
The \(O(1)\) constants here and below are uniform in \(k\) for the fixed cutoff family.

## Full collar diagonal

For every collar vector \(y\) in the natural Gamma form domain, the total support measure is \(2h_k=\log(1+1/k)\leq1/k\), so
\(\|y\|_1^2\leq k^{-1}\|y\|_2^2\). The exact series for \(b\) gives
\(b(t)\geq\tfrac12\log(1+4t^2)\). Almost everywhere,
\[
b(t)\geq\log(2k)-\mathbf1_{\{|t|<k\}}\log(k/|t|).
\]
Using \(|\widehat y(t)|\leq\|y\|_1\) with the unnormalized transform and
\(\int_{-k}^k\log(k/|t|)\,dt=2k\), the low-frequency loss is at most
\((k/\pi)\|y\|_1^2\leq C\|y\|_2^2\). This is a form-domain estimate for arbitrary collar \(y\); it does not assume \(y\in H^1\). Thus the Gamma diagonal is bounded below by \((\log k-C)I\).

The prime diagonal is exactly zero. Distances within one wing are below \(h_k<\log2\); distances between opposite wings lie strictly in
\((2a_k,2a_{k+1})=(\log k,\log(k+1))\), which contains no \(\log n\) for integer \(n\). The endpoint sets have measure zero. This excludes every prime power from the collar-to-itself block, without truncating any nonzero interaction. Moreover
\[
\|s_{\rm new}\|_2^2
=\sinh(a_{k+1})-\sinh(a_k)-h_k=O(k^{-1/2}),
\]
so the true polar debit is at most \(2\|s_{\rm new}\|_2^2\|y\|_2^2=O(k^{-1/2})\|y\|_2^2\). The actual polar-inclusive collar operator therefore satisfies
\[
D_{A,\rm new}\geq(\log k-C)I
\]
on its full induced form domain.

## Complete pointwise prime-row series

The required row is \(b_k=P_{\rm new}A_{k+1}g_k\). First, the generic multiplier estimate in `GAMMA_LOG_REMAINDER.md` applies to \(r_k\): the just-listed \(L^1\) and \(H^1\) bounds give
\[
\|(a(D)-\log k)r_k\|_2\leq C\|r_k\|_2.
\]
The lemma concerns the actual coefficient-one logarithmic Gamma symbol and the operator domain of this particular \(H^1\cap L^1\) vector. It is not being applied to arbitrary collar vectors.

For completeness the prime row has the following explicit post-coefficient pointwise majorant. Fix \(x\in[a_k,a_{k+1}]\), and enlarge each sum to every integer index, using \(\alpha_n\leq\log n/\sqrt n\). For positive shifts, the tail envelope, \(u_+=\pi e^{2(x+\log n)}\geq\pi kn^2\), and \(e^{(x+\log n)/2}\leq Ck^{1/4}n^{1/2}\), divided by \(\|r_k\|_2\geq c k^{19/4}e^{-\pi k}\), give
\[
\frac{\alpha_n|r_k(x+\log n)|}{\|r_k\|_2}
\leq C\sqrt{k}(\log n)n^{10}e^{-\pi k(n^2-1)}.
\]
Hence the entire positive-shift series is bounded uniformly in \(x\) by
\[
C\sqrt{k}\sum_{n\geq2}(\log n)n^{10}e^{-\pi k(n^2-1)}
\leq C\sqrt{k}e^{-3\pi k}
\sum_{n\geq2}(\log n)n^{10}e^{-\pi(n^2-4)}
=O(e^{-c k}).
\]

For a negative shift, \(x-\log n\leq a_{k+1}-\log2<R_k\) for sufficiently large \(k\); it is either in the central zero interval or in the negative tail. In the tail case
\(n\geq e^{x+R_k}\geq ke^{-1/k}>k-1\), so the integer index has the form \(n=k+j\), \(j\geq0\). Put \(z=\log n-x\). Then
\[
\frac{\pi n^2}{k+1}\leq U=\pi n^2e^{-2x}\leq\frac{\pi n^2}{k},
\qquad e^{z/2}\leq n^{1/2}k^{-1/4}.
\]
The theta envelope gives
\[
\frac{|r_k(x-\log n)|}{\|r_k\|_2}
\leq C\sqrt{k}(1+j/k)^{21/2}
\exp\!\left[-\pi\left(\frac{(k+j)^2}{k+1}-k\right)\right].
\]
For \(j\geq1\), \((k+j)^2/(k+1)-k\geq j\); for \(j=0\) it is greater than \(-1\). Multiplying by the coefficient before summing yields the explicit required post-coefficient series
\[
\boxed{\quad
\sum_{j\geq0}\frac{\alpha_{k+j}|r_k(x-\log(k+j))|}{\|r_k\|_2}
\leq C\sum_{j\geq0}(\log(k+j))(1+j/k)^{10}e^{-\pi j}
\leq C\log k.
\quad}
\]
For the last inequality, take \(k\) large so \((1+j/k)^{10}\leq e^{10j/k}\leq e^{\pi j/2}\), and use \(\log(k+j)\leq\log k+j/k\). These bounds are uniform in \(x\); all prime powers are retained by the all-integer enlargement. Combining both shift directions and integrating over the two wings, whose total measure is \(2h_k\asymp k^{-1}\), proves
\[
\|P_{\rm new}Sr_k\|_2\leq C\frac{\log k}{\sqrt{k}}\|r_k\|_2.
\]

Since \(Tf_0=0\), on the collar
\[
P_{\rm new}Tg_k=-P_{\rm new}Tr_k
=-\log k\,r_{\rm new}+O_{L^2}(\|r_k\|_2),
\]
where \(r_{\rm new}=P_{\rm new}r_k=P_{\rm new}f_0\). Adding the polar row costs at most
\(2\|s_{\rm new}\|_2|\langle s,g_k\rangle|=O(k^{-1/2}\|r_k\|_2)\). Thus the actual full row is
\[
b_k=-\log k\,r_{\rm new}+e_k,
\qquad \|e_k\|_2\leq C\|r_k\|_2.
\]

## Exterior mass and Schur margin

Let \(M(U)\) be the one-sided squared theta-tail mass. The verified theta envelope gives
\(M(U)\asymp U^{19/2}e^{-2U}\). Since \(|r_k|\leq|f_0|\) and \(r_k=f_0\) for \(|x|\geq a_k\),
\[
\|r_k\|_2^2\leq2M(U_R),\qquad
\|r_k\|_{L^2(|x|\geq a_{k+1})}^2=2M(\pi(k+1)),
\quad U_R=\pi k e^{-2/k}.
\]
The latter exterior is disjoint from the new collar and belongs to \(r_k\). Since \(\pi(k+1)-U_R\to3\pi\), the two-sided comparison constants in \(M(U)\asymp U^{19/2}e^{-2U}\) imply a strictly positive lower bound on the exterior-to-total mass ratio. Therefore a fixed \(\delta>0\) exists, independent of the transition shape, with
\[
\|r_{\rm new}\|_2^2\leq(1-\delta)\|r_k\|_2^2.
\]
This \(\delta\) may be very small; only strict positivity is used.

The restricted domain is \(\operatorname{span}\{g_k\}\oplus\mathcal Q_{\rm new}\), with \(\mathcal Q_{\rm new}\) the induced collar form domain. Let \(D=D_{A,\rm new}\). The collar lower bound makes \(D^{-1}\) bounded for large \(k\), and for \(b_k\in L^2\), \(D^{-1}b_k\in\operatorname{Dom}(D)\), so the square completion preserves the form domain. It gives
\[
\mathfrak a[\alpha g_k+y]
=\|D^{1/2}(y+\alpha D^{-1}b_k)\|_2^2
+|\alpha|^2\left(a_{A,k}-\langle b_k,D^{-1}b_k\rangle\right).
\]
Using \(D\geq(\log k-C)I\), \(b_k=-\log k\,r_{\rm new}+e_k\), and the mass fraction,
\[
\begin{aligned}
\langle b_k,D^{-1}b_k\rangle
&\leq\frac{\|b_k\|_2^2}{\log k-C}\\
&\leq\bigl((1-\delta)\log k+C'\bigr)\|r_k\|_2^2.
\end{aligned}
\]
Here the cross term in \(\|b_k\|^2\) is \(O(\log k)\|r_k\|_2^2\), because \(\|r_{\rm new}\|_2\leq\|r_k\|_2\). Since \(a_{A,k}=(\log k+O(1))\|r_k\|_2^2\), the restricted scalar Schur margin is
\[
a_{A,k}-\langle b_k,D^{-1}b_k\rangle
\geq(\delta\log k-C'')\|r_k\|_2^2>0
\]
for all sufficiently large \(k\). Together with \(D>0\), this proves positivity on the stated compression.

## Item-by-item disposition

- **Cutoff:** real, even, \(0\leq\chi_k\leq1\), exact core/vanishing radii, and fixed \(C_j\) are stated; this repairs the only hypothesis omission identified by Referee 25.
- **Tracked line and tail:** \(g_k=\chi_kf_0\), \(r_k=(1-\chi_k)f_0\); the exact whole-line null identity gives equal \(T\)-energies, and the lower/upper tail lemmas apply with their stated domains.
- **Old scalar:** the coefficient-2 polar debit is included and is lower order, so \(a_{A,k}=(\log k+O(1))\|r_k\|_2^2\).
- **New diagonal:** the arbitrary-form-domain Gamma lower bound, exact zero prime diagonal, and coefficient-2 polar debit give \(D_{A,\rm new}\geq(\log k-C)I\).
- **Full row:** the pointwise post-coefficient sum is displayed above; it covers every integer majorant and hence all prime powers. The resulting row is \(-\log k\,r_{\rm new}+O_{L^2}(\|r_k\|_2)\).
- **Mass reserve:** the exterior \(|x|\geq a_{k+1}\) supplies a fixed positive fraction of \(\|r_k\|_2^2\), yielding the stated \(\delta\).
- **Domain and conclusion:** the sharp-window source form splits on its maximal domain, permitting the restricted square completion. No remainder of the old space is eliminated or controlled.

The theorem is therefore accepted only in this restricted, conditional source-form scope. No full old-space positivity or RH status is changed.
