# Referee 25: narrow-cutoff tail lower bound

## Verdict

The boxed estimate in NARROW_TAIL_LOWER.md is valid for the stated class of cutoffs, with constants independent of \(k\) and of the cutoff values. It is an unconditional lower bound for the one explicit vector \(r_k=(1-\chi_k)f_0\) in the full source quadratic form \(q_T\). The prime estimate retains all prime powers, and the cross-opposite-tail correlations have the favorable sign and are not discarded with the dangerous same-side terms.

The proof does not assume an earlier positivity theorem or RH. It does not prove that \(r_k\) is an eigenvector, nor does it estimate the inverse-weighted Schur quotient needed for the full P2 operator. It yields no sign theorem for \(T\), \(H\), or the original Weil operator.

## 1. Sign and two-sided theta tails

Write \(u=\pi e^{2x}\). The given exact theta differentiation formula is
\[
f_0(x)=e^{x/2}\sum_{m\ge1}F_1(m^2u)e^{-m^2u},\qquad
F_1(v)=-vG(v),
\]
\[
G(v)=32v^4-360v^3+1056v^2-810v+90.
\tag{2}
\]
The sign is easily certified on the required range \(v\ge32\): \(G(12)=183906>0\), and
\[
G'(v)=v^2(128v-1080)+2112v-810>0\qquad(v\ge12).
\]
Thus \(F_1(v)<0\) for \(v\ge32\). If \(u\ge32\), then \(m^2u\ge32\) for every theta mode \(m\), so every summand in (2), not just the first, is negative. This proves \(f_0(x)<0\) on the positive tail. Oddness gives \(f_0(x)>0\) on the negative tail.

For \(v\ge32\), elementary bounds on \(G(v)/v^4\) give \(c v^4\le G(v)\le C v^4\), hence \(c v^5\le |F_1(v)|\le C v^5\). For example,
\[
G(v)/v^4\ge32-360/32-810/32^3>20,
\quad
G(v)/v^4\le32+1056/32^2+90/32^4<34.
\]
The remaining theta modes are uniformly controlled by
\(\sum_{m\ge1}m^{10}e^{-(m^2-1)u}\le C\) for \(u\ge32\). The first mode gives the lower bound. Thus
\[
c e^{x/2}u^5e^{-u}\le -f_0(x)\le C e^{x/2}u^5e^{-u}
\qquad (u\ge32).
\tag{3}
\]
This explicitly checks the sign of the full theta sum; no cancellation assumption is being made.

With \(dx=du/(2u)\) and \(e^{x/2}=(u/\pi)^{1/4}\), the squared tail integrand is comparable to \(u^{19/2}e^{-2u}\), and the absolute tail integrand to \(u^{17/4}e^{-u}\). Therefore
\[
\int_{u(x)\ge U}|f_0(x)|^2dx\asymp U^{19/2}e^{-2U},\qquad
\int_{u(x)\ge U}|f_0(x)|dx\le C U^{17/4}e^{-U}.
\tag{4}
\]
These are one-sided estimates; oddness supplies the equal negative-side contributions.

For \(R_k=\frac12\log k-k^{-1}\), \(U_R=\pi k e^{-2/k}\to\infty\). The cutoff assumptions imply \(|r_k|\le|f_0|\) on \(|x|\ge R_k\), and \(r_k=f_0\) on \(|x|\ge a_k\). In particular it has the same sign as \(f_0\) on each tail for large \(k\). On \(a_k\le x\le a_k+k^{-1}\), \(u\in[\pi k,\pi k e^{2/k}]\), an interval of \(u\)-length bounded above and below by positive constants. Using (3) there gives
\[
\|r_k\|_2^2\ge2\int_{a_k}^{a_k+k^{-1}}|f_0(x)|^2dx
\ge c k^{19/2}e^{-2\pi k}.
\tag{5}
\]
The matching upper bound \(\|r_k\|_2^2\le Ck^{19/2}e^{-2\pi k}\) also follows from (4) at \(U_R=\pi k-O(1)\). Thus the exponent \(19/2\) is consistent for the squared \(L^2\) mass.

The \(L^1\) bookkeeping is
\[
\|r_k\|_1\le C U_R^{17/4}e^{-U_R},\qquad
\|r_k\|_2^2\ge c(\pi k)^{19/2}e^{-2\pi k}.
\]
Since \(0\le\pi k-U_R\le2\pi\), this proves
\[
\|r_k\|_1^2\le Ck^{-1}\|r_k\|_2^2.
\tag{6}
\]
It uses no lower bound on \(1-\chi_k\) in the transition.

If an \(H^1\) estimate is intended, differentiating (2) gives
\[
f_0'(x)=e^{x/2}\sum_{m\ge1}
\left(\tfrac12F_1(v)+2v(F_1'(v)-F_1(v))\right)e^{-v},
\qquad v=m^2u.
\]
The bracket is a degree-six polynomial bounded by \(Cv^6\) on \(v\ge32\), so \(|f_0'(x)|\le C e^{x/2}u^6e^{-u}\). Its squared tail is \(O(U^{23/2}e^{-2U})\). If \(\|\chi_k'\|_\infty\le C_{\chi,1}k\), the cutoff term \(\chi_k'f_0\) contributes at most \(C_{\chi,1}^2k^2 U_R^{19/2}e^{-2U_R}\). Hence, with the stated uniform first-derivative bound,
\[
\|r_k'\|_2^2\le C(C_{\chi,1}) k^{23/2}e^{-2\pi k}
\le C(C_{\chi,1})k^2\|r_k\|_2^2.
\]
This optional \(H^1\) control is not used in the form lower bound; \(r_k\in\mathcal S\) for each fixed \(k\) already makes the form well-defined.

## 2. Frequency uncertainty and the exact Gamma lower bound

The positive series for \(b\) is
\[
b(t)=\sum_{j\ge0}
\frac{(t/2)^2}{(j+1/4)((j+1/4)^2+(t/2)^2)}.
\]
As a function of \(v=j+1/4\), each summand is decreasing. Its left-endpoint sum therefore dominates the integral from \(1/4\) to infinity:
\[
b(t)\ge\int_{1/4}^{\infty}
\frac{(t/2)^2}{v(v^2+(t/2)^2)}\,dv
=\frac12\log(1+4t^2).
\tag{7}
\]
The integral is exact.

For \(t\ne0\), (7) implies the stronger pointwise bound
\[
b(t)\ge\log(2|t|).
\]
Consequently, for every \(k\ge1\),
\[
b(t)\ge\log(2k)-\mathbf1_{\{|t|<k\}}\log(k/|t|).
\]
For \(|t|<k\) the right side is \(\log(2|t|)\); for \(|t|\ge k\) it is \(\log(2k)\le\log(2|t|)\). Since \(|\widehat r_k(t)|\le\|r_k\|_1\), the entire low-frequency correction is integrable and satisfies
\[
\frac1{2\pi}\int_{|t|<k}\log(k/|t|)|\widehat r_k(t)|^2dt
\le\frac{\|r_k\|_1^2}{2\pi}\int_{-k}^{k}\log(k/|t|)dt
=\frac{k}{\pi}\|r_k\|_1^2
\le C\|r_k\|_2^2
\]
by (6). Thus
\[
\langle r_k,b(D)r_k\rangle
\ge(\log(2k)-C)\|r_k\|_2^2.
\tag{8}
\]
After subtracting \(C_0\|r_k\|_2^2\), the Gamma contribution to \(q_T\) is at least \((\log k-C)\|r_k\|_2^2\), after absorbing \(\log2\) into the constant. This proves the updated leading coefficient \(1\); the older half-mass argument was valid but not sharp.

## 3. Complete prime-power correlation and signs

For real \(r_k\), the two shifts in each \(n\)-summand have equal correlation by translation, hence
\[
q_T[r_k]=-C_0\|r_k\|_2^2+\langle r_k,b(D)r_k\rangle
-2\sum_{n\ge2}\alpha_n I_k(\log n),
\quad I_k(d)=\int r_k(x)r_k(x+d)\,dx.
\tag{9}
\]
This includes every \(n\) with \(\Lambda(n)>0\). Absolute convergence for fixed \(k\) follows from Schwartz decay and the stated double-exponential tail bound.

For \(d>0\), the same-side terms are
\[
J_k(d)=\int_{R_k}^{\infty}r_k(x)r_k(x+d)\,dx\ge0
\]
on the positive side, and the equal positive copy on the negative side. The only opposite-side overlap has a negative-tail factor \(r_k(x)\ge0\) and a positive-tail factor \(r_k(x+d)\le0\). Thus
\[
I_k(d)=2J_k(d)+I_k^{\rm cross}(d),\qquad I_k^{\rm cross}(d)\le0,
\]
so
\[
-2\alpha_n I_k(\log n)\ge-4\alpha_n J_k(\log n).
\tag{10}
\]
Dropping the cross term is legitimate only in this direction: it is favorable for a lower bound. The same-side term is the entire adverse part and must be controlled.

By Cauchy--Schwarz, \(|r_k|\le|f_0|\), and \(r_k=f_0\) on \([a_k,\infty)\),
\[
J_k(\log n)
\le\|r_{k,+}\|_2
\|f_0\mathbf1_{[R_k+\log n,\infty)}\|_2,
\qquad
\|r_{k,+}\|_2\ge\|f_0\mathbf1_{[a_k,\infty)}\|_2.
\]
The square root of (4)'s \(L^2\) tail is \(U^{19/4}e^{-U}\). With
\(U_n=\pi k n^2e^{-2/k}\), it follows that
\[
\frac{\|f_0\mathbf1_{[R_k+\log n,\infty)}\|_2}
{\|f_0\mathbf1_{[a_k,\infty)}\|_2}
\le C n^{19/2}e^{-(U_n-\pi k)}
\le C n^{19/2}e^{-\frac{\pi}{2}k(n^2-1)}.
\tag{11}
\]
For the last inequality, when \(k\) is large \(e^{-2/k}\ge3/4\), and
\(n^2e^{-2/k}-1\ge\frac23(n^2-1)\); the displayed \(\pi/2\) exponent is a valid weaker bound. Combining (10)–(11), using \(\alpha_n\le(\log n)/\sqrt n\), and summing over all integers \(n\ge2\) gives
\[
-2\sum_{n\ge2}\alpha_n I_k(\log n)
\ge-C\|r_k\|_2^2
\sum_{n\ge2}(\log n)n^9e^{-\frac{\pi}{2}k(n^2-1)}
\ge-Ce^{-ck}\|r_k\|_2^2.
\tag{12}
\]
The last series is \(O(e^{-3\pi k/2})\) for \(k\ge1\), since after factoring out \(e^{-3\pi k/2}\) the remaining sum is bounded by the convergent series with \(k=1\). Replacing prime powers by all integers is only an upper bound on this adverse sum; no prime-power term is dropped.

Equations (8), (9), and (12) prove
\[
q_T[r_k]\ge(\log k-C)\|r_k\|_2^2.
\]
Together with (5), this is strictly positive for all sufficiently large \(k\), and has the claimed squared-mass scale \(k^{19/2}e^{-2\pi k}\).

## 4. What the test does not certify

Although \(Tf_0=0\), \(r_k=f_0-\chi_k f_0\) is not thereby a zero mode: \(Tr_k=-T(\chi_kf_0)\), with no estimate here making that term zero. The result is a Rayleigh-form lower bound on one \(k\)-dependent test vector. It does not bound an actual inverse-weighted Schur quotient such as \(\|C_k^{-1/2}B_k\|\), and does not transfer through an unproved \(1/m\) map or a different source metric. In particular it proves no operator sign for \(T\) or \(H\), no positivity of the full source short, and no RH consequence. This limitation is essential rather than a missing final sentence.

**Review outcome.** No fatal error found in the claimed narrow-tail lower bound under its cutoff assumptions. The exact sign/correlation and norm bookkeeping should be stated as above; the valid conclusion is the test-vector estimate (1), no stronger operator claim.

