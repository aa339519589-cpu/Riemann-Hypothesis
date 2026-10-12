# Restricted positivity: one tracked odd zero mode and the entire next collar

## Result and exact scope

Let
\[
a_k=\tfrac12\log k,\qquad h_k=a_{k+1}-a_k=\tfrac12\log(1+1/k),
\]
take a real even smooth cutoff \(0\le\chi_k\le1\), with \(\chi_k=1\) on \(|x|\le a_k-k^{-1}\), \(\chi_k=0\) on \(|x|\ge a_k\), and fixed uniform derivative bounds \(\|\chi_k^{(j)}\|_\infty\ll_j k^j\), and set
\[
g_k=\chi_k f_0\quad\text{(old line)},\qquad
r_k=(1-\chi_k)f_0,\qquad
f_0=\Phi'''-\tfrac14\Phi',\qquad Tf_0=0,
\]
where \(T=a(D)-S\) contains the exact Gamma multiplier and all prime powers. Let the full new odd collar be
\[
\mathcal N_k=L^2_{\rm odd}\bigl((a_k,a_{k+1})\cup(-a_{k+1},-a_k)\bigr).
\]
Use the exact form definition in [SOURCE_FORM.md](SOURCE_FORM.md):
\[
A_{k+1}=P_{k+1}TP_{k+1}-2|s_{k+1}\rangle\langle s_{k+1}|,
\qquad T=a(D)-S,
\]
as a form on the odd support window, with \(s(x)=\sinh(x/2)\), the complete prime-power translation sum in \(S\), and the coefficient \(2\) on the true polar rank one. The operator and its coefficient are defined in `SOURCE_FORM.md`; the maximal Gamma form splits over the sharp old/collar supports, while the finite localized prime sum and polar term are bounded on each fixed window, as checked in `REFEREE_DOMAIN.md`.

**Theorem (restricted block).** For all sufficiently large integer \(k\), the restriction of the exact polar-inclusive \(A_{k+1}\) form to
\[
\operatorname{span}\{g_k\}\oplus\mathcal N_k
\]
is positive, where \(g_k=\chi_kf_0\) and \(\mathcal N_k\) is the whole odd new collar. The proof uses the narrow-tail lower lemma
\[
q_T[r_k]\ge(\log k-C)\|r_k\|_2^2,
\tag{1}
\]
from `../20261012_narrow_theta_tail/NARROW_TAIL_LOWER.md`, whose hypotheses are exactly the cutoff assumptions above. The proof also supplies the matching upper estimate, the full old-to-collar row, and a coercive lower bound on the actual polar-inclusive collar block.

The conclusion concerns only the tracked one-dimensional old vector and the entire next collar. It does not eliminate the rest of the old window and does not exclude negative directions in that complement.

## Exact tail identity and two-sided tail energy

The source equation \(Tf_0=0\), paired against \(g_k\) and \(r_k\) in the full symmetric Gamma-plus-prime form, gives
\[
q_T[g_k]=q_T[r_k].
\tag{3}
\]
This identity uses the whole-line source equation and the complete prime sum; the compact support of \(g_k\) does not justify dropping the \(n\ge k\) terms from the tail form.

For this width-\(1/k\) cutoff the theta estimates give
\[
\|r_k\|_2^2\asymp k^{19/2}e^{-2\pi k},\qquad
\|r_k\|_1^2\ll k^{-1}\|r_k\|_2^2,\qquad
\|r_k'\|_2\ll k\|r_k\|_2.
\tag{4}
\]
The lower and upper mass bounds follow from \(|f_0(x)|\asymp e^{x/2}U^5e^{-U}\), \(U=\pi e^{2x}\), on the tail and from \(r_k=f_0\) for \(|x|\ge a_k\); the transition starts at \(a_k-k^{-1}\), where \(U=\pi k e^{-2/k}=\pi k+O(1)\). The derivative estimate includes \(\chi_k'f_0\), with \(\|\chi'_k\|_\infty\ll k\). These are the estimates in the narrow-tail calculation, with the upper bound also derived below.

The reviewed narrow-tail lower lemma gives (1). For completeness, the upper bound has two parts. The positive series for \(b(t)=a(t)+C_0\) and upper sum-integral comparison give
\[
b(t)\le 4+\tfrac12\log(1+4t^2).
\]
Use Plancherel, Jensen for \(u\mapsto\log(1+4u)\), and \(\|r'_k\|_2\ll k\|r_k\|_2\) to get
\[
\langle r_k,b(D)r_k\rangle\le(\log k+C)\|r_k\|_2^2.
\tag{5}
\]
For the prime term write, for \(d>0\),
\[
I_k(d)=\int r_k(x)r_k(x+d)dx=2J_k(d)+I_k^{\rm cross}(d),
\quad J_k(d)\ge0,\quad I_k^{\rm cross}(d)\le0.
\]
The same-side contribution to \(-2\sum\alpha_n I_k(\log n)\) is nonpositive, so only the opposite-tail correlation can increase the upper bound. This cross term is empty unless \(n\ge k-1\). If it is nonempty, the two positive tail arguments add to \(d=\log n\), and the exact theta envelope gives
\[
|f_0(x)f_0(d-x)|\le C n^{21/2}e^{-2\pi n}.
\]
Its integration interval has length \(d-2(a_k-k^{-1})\le(n-k+2)/k\). After division by the lower mass in (4),
\[
\frac{|I_k^{\rm cross}(\log n)|}{\|r_k\|_2^2}
\le C(n-k+2)(n/k)^{21/2}e^{-2\pi(n-k)}.
\]
Summing with \(\alpha_n\le\log n/\sqrt n\), over all integers \(n\ge k-1\) and hence all prime powers, gives
\[
q_S[r_k]\le C\frac{\log k}{\sqrt k}\|r_k\|_2^2.
\tag{6}
\]
The local term \(-C_0\|r_k\|_2^2\) is bounded, and (5)–(6) prove
\[
\boxed{q_T[g_k]=q_T[r_k]=(\log k+O(1))\|r_k\|_2^2.}
\tag{7}
\]

## New-collar diagonal block

For \(y\in\mathcal N_k\), the total support length is \(2h_k\ll k^{-1}\), so
\[
\|y\|_1^2\le 2h_k\|y\|_2^2\ll k^{-1}\|y\|_2^2.
\]
The lower digamma bound
\[
b(t)\ge\tfrac12\log(1+4t^2)\ge\log(2|t|)\quad(t\ne0)
\]
gives, for every \(t\),
\[
b(t)\ge \log(2k)-\mathbf1_{\{|t|<k\}}\log(k/|t|).
\]
The correction is integrable at zero. With the unnormalized Fourier transform used in the tail estimate, \(|\widehat y(t)|\le\|y\|_1\), so
\[
\frac1{2\pi}\int_{|t|<k}\log(k/|t|)|\widehat y(t)|^2dt
\le \frac{k}{\pi}\|y\|_1^2\le C\|y\|_2^2.
\]
Thus
\[
\langle y,a(D)y\rangle
=\langle y,b(D)y\rangle-C_0\|y\|_2^2
\ge(\log k-C)\|y\|_2^2.
\tag{8}
\]
The prime-shift diagonal on the collar is **exactly zero**. Same-wing distances are less than \(h_k<\log2\). Opposite-wing distances lie strictly between
\[
2a_k=\log k\quad\text{and}\quad2a_{k+1}=\log(k+1).
\]
There is no integer \(n\) in \((k,k+1)\); endpoint alignments have measure zero. This covers all prime powers. The actual polar term is negative, but
\[
\|s_{\mathrm{new}}\|_2^2
=\sinh(a_{k+1})-\sinh(a_k)-h_k=O(k^{-1/2}),
\]
so its worst-case debit is \(2|\langle s_{\mathrm{new}},y\rangle|^2\ll k^{-1/2}\|y\|_2^2\). Therefore
\[
\boxed{D_{A,\mathrm{new}}\ge(\log k-C)I\quad\text{on }\mathcal N_k.}
\tag{9}
\]

## Old scalar and exact old/new row

The global polar neutrality \(\langle s,f_0\rangle=0\) gives
\[
\langle s,g_k\rangle=-\langle s,r_k\rangle.
\]
Using \(|s(x)|\ll e^{|x|/2}\) and the theta tail on \(|x|\ge a_k-k^{-1}\),
\[
|\langle s,g_k\rangle|\ll k^{-1/4}\|r_k\|_2.
\tag{10}
\]
Indeed, on the positive tail the absolute overlap is bounded by
\(C\int_{U_R}^\infty u^{9/2}e^{-u}du\ll U_R^{9/2}e^{-U_R}\), where \(U_R=\pi k e^{-2/k}\); comparison with \(\|r_k\|_2\ge c k^{19/4}e^{-\pi k}\) gives the factor \(k^{-1/4}\). The negative tail contributes the same amount.
The old polar-inclusive scalar is therefore
\[
a_{A,k}:=\langle g_k,A_{k+1}g_k\rangle
=q_T[g_k]-2|\langle s,g_k\rangle|^2
=(\log k+O(1))\|r_k\|_2^2.
\tag{11}
\]

On the new collar, \(r_k=f_0\). Fourier localization of the tail gives the stronger operator estimate
\[
\|(a(D)-\log k)r_k\|_2\ll\|r_k\|_2.
\tag{12}
\]
Indeed, for \(|t|<k\), \(|a(t)-\log k|\ll1+\log(k/|t|)\); use \(|\widehat r_k(t)|\le\|r_k\|_1\) and (4) to pay the logarithmic square. For \(|t|\ge k\), \(|a(t)-\log k|\ll1+\log(|t|/k)\ll1+|t|/k\); use (4)'s \(H^1\) estimate. This controls the full Gamma multiplier, not a truncated symbol.

The full prime sum on the collar obeys
\[
\|\mathbf1_{\mathrm{new}}S r_k\|_2
\ll \frac{\log k}{\sqrt k}\|r_k\|_2.
\tag{13}
\]
Here is a direct full-sum bound. For \(x\in[a_k,a_{k+1}]\), positive-shift arguments have \(\pi k n^2\le U=\pi e^{2(x+\log n)}\le\pi(k+1)n^2\). The theta envelope, divided by the lower mass bound in (4) and multiplied by \(\alpha_n\), is at most \(C\sqrt{k}\,\log n\,n^{10}e^{-\pi k(n^2-1)}\); its sum over \(n\ge2\) is \(O(e^{-ck})\). For a negative shift to meet the support of \(r_k\), \(x-\log n\le-(a_k-k^{-1})\), hence \(n\ge e^{a_k+(a_k-k^{-1})}=ke^{-1/k}>k-1\), so the integer index satisfies \(n\ge k\). The other support possibility, \(x-\log n\ge a_k-k^{-1}\), would force \(\log n\le h_k+k^{-1}<\log2\), impossible for \(n\ge2\). Write \(n=k+j\), \(j\ge0\), and \(z=\log n-x\). On this collar, \(z\ge0\),
\[
\pi\frac{n^2}{k+1}\le U(z)=\pi n^2e^{-2x}\le\pi\frac{n^2}{k},
\qquad e^{z/2}\le n^{1/2}k^{-1/4}.
\]
The theta envelope and \(\|r_k\|_2\ge c k^{19/4}e^{-\pi k}\) imply
\[
\frac{|r_k(x-\log n)|}{\|r_k\|_2}
\le C\sqrt{k}\left(\frac nk\right)^{21/2}
 \exp\!\left[-\pi\left(\frac{n^2}{k+1}-k\right)\right]
\le C\sqrt{k}\left(1+\frac jk\right)^{21/2}e^{-\pi j},
\]
because \(n^2/(k+1)-k\ge j\) for \(j\ge1\), while the \(j=0\) exponent is bounded below by \(-1\). After multiplication by the exact prime-power coefficient and enlargement to all integer indices, the pointwise sum is bounded by
\[
\begin{aligned}
\sum_{n\ge k}\frac{\alpha_n|r_k(x-\log n)|}{\|r_k\|_2}
&\le C\sum_{j\ge0}\log(k+j)(1+j/k)^{10}e^{-\pi j}\\
&\le C\sum_{j\ge0}(\log k+j/k)e^{-(\pi-10/k)j}\\
&\le C'\log k
\end{aligned}
\]
for all sufficiently large \(k\). The prefactor \(\sqrt{k}\) is canceled by \(\sqrt n=\sqrt{k}\sqrt{1+j/k}\), so the power is exactly \(10\). This enlargement includes every prime power. The collar has length \(h_k\asymp k^{-1}\), so its \(L^2\) norm gains \(k^{-1/2}\). Odd reflection gives the same estimate on the negative collar. This proves (13) without truncating the prime sum.

Let \(B_A^*g_k\) denote the old-to-new row of the polar-inclusive block. The exact source zero gives
\[
\Pi_{\mathrm{new}}Tg_k=-\Pi_{\mathrm{new}}Tr_k
=-\log k\,r_{\mathrm{new}}+O_{L^2}(\|r_k\|_2),
\]
by (12)–(13). The polar row is a further error
\[
2|\langle s,g_k\rangle|\|s_{\mathrm{new}}\|_2
\ll k^{-1/2}\|r_k\|_2
\]
by (9)–(10). Thus
\[
\boxed{B_A^*g_k=-\log k\,r_{\mathrm{new}}+e_k,\qquad
\|e_k\|_2\ll\|r_k\|_2.}
\tag{14}
\]

## Tail mass left outside the new collar

The new part is \(r_{\mathrm{new}}=f_0\) on \([a_k,a_{k+1}]\) and its odd reflection. The rest of \(r_k\) includes the exterior \(|x|\ge a_{k+1}\), where it is exactly \(f_0\). With \(U(x)=\pi e^{2x}\), the theta tail mass satisfies
\[
M(U):=\int_{\pi e^{2x}\ge U}|f_0(x)|^2dx\asymp U^{19/2}e^{-2U}.
\]
The whole \(r_k\) has \(\|r_k\|_2^2\le2M(U_R)\), with \(U_R=\pi k e^{-2/k}\), while its exterior has mass \(2M(\pi(k+1))\). Since
\[
\pi(k+1)-U_R\longrightarrow3\pi,
\]
their ratio has a positive lower limit up to the fixed comparison constants. Consequently there exists \(\delta>0\), independent of \(k\) and the cutoff transition, such that
\[
\boxed{\|r_{\mathrm{new}}\|_2^2\le(1-\delta)\|r_k\|_2^2.}
\tag{15}
\]

## Restricted two-block Schur margin

Let \(\mathfrak a_{k+1}\) be the exact polar-inclusive form of \(A_{k+1}\), and let
\[
\mathcal Q_{\mathrm{new}}=\operatorname{Dom}(\mathfrak a_{k+1})\cap\mathcal N_k,
\]
the induced source form domain on the entire odd collar. The sharp-window form-domain splitting in `REFEREE_DOMAIN.md` shows that
\(\mathcal X_k=\operatorname{span}\{g_k\}\oplus\mathcal Q_{\mathrm{new}}\)
is the corresponding closed form domain on the support-restricted subspace; the supports are disjoint. Let \(D_{A,\mathrm{new}}\) be the positive self-adjoint operator associated with the restricted collar form, and \(b_k=B_A^*g_k\). From (9), it satisfies \(D_{A,\mathrm{new}}\ge(\log k-C)I\) for all large \(k\). With inner product linear in the second entry, completion of the new block gives
\[
\mathfrak a_{k+1}[\alpha g_k+y]
=\langle D_{A,\mathrm{new}}^{1/2}
 (y+\alpha D_{A,\mathrm{new}}^{-1}b_k),
 D_{A,\mathrm{new}}^{1/2}(y+\alpha D_{A,\mathrm{new}}^{-1}b_k)\rangle
+|\alpha|^2\bigl(a_{A,k}-\langle b_k,D_{A,\mathrm{new}}^{-1}b_k\rangle\bigr).
\tag{16}
\]
The domain is preserved: \(b_k\in L^2(\mathcal N_k)\), and the coercive inverse maps it into \(D(D_{A,\mathrm{new}})\), hence into the collar form domain. No full-old-space projection is used.

By \(D_{A,\mathrm{new}}\ge(\log k-C)I\), (14), and (15),
\[
\begin{aligned}
\langle b_k,D_{A,\mathrm{new}}^{-1}b_k\rangle
&\le\frac{\|b_k\|_2^2}{\log k-C}\\
&\le\frac{(\log k)^2\|r_{\mathrm{new}}\|_2^2
             +C\log k\|r_k\|_2^2+C\|r_k\|_2^2}{\log k-C}\\
&\le\bigl((1-\delta)\log k+C'\bigr)\|r_k\|_2^2.
\end{aligned}
\tag{17}
\]
Together with (11), this yields
\[
a_{A,k}-\langle b_k,D_{A,\mathrm{new}}^{-1}b_k\rangle
\ge(\delta\log k-C'')\|r_k\|_2^2>0
\]
for sufficiently large \(k\). Equations (9), (16) then prove that the **restricted form on \(\mathcal X_k\)** is positive for all large \(k\).

## Scope and unresolved complement

The argument controls one tracked old vector \(g_k=\chi_kf_0\) against the entire next collar. It does **not** eliminate the orthogonal complement of \(g_k\) in the old window. In particular, it is not a positivity theorem for the full old/new block on \(L^2_{\rm odd}(-a_{k+1},a_{k+1})\), does not bound the later full-old Schur correction, and does not exclude any remaining negative index. It proves no all-depth sign theorem and no RH conclusion.

The tail-energy inputs are [the lower bound](../20261012_narrow_theta_tail/NARROW_TAIL_LOWER.md) and [the upper bound](../20261012_narrow_theta_tail/NARROW_TAIL_UPPER.md). The collar geometry, prime-diagonal zero, and full prime row are independently checked in [REFEREE_TRACKED_MODE.md](REFEREE_TRACKED_MODE.md). The conclusion concerns exactly the source form defined in [SOURCE_FORM.md](SOURCE_FORM.md) and its induced form domain. All displayed estimates retain the full theta source, the exact Gamma symbol, and the complete prime-power sum.
