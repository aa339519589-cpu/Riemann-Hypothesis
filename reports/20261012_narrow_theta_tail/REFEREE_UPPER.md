# Referee 25: matching upper bound for the narrow-tail test

## Verdict

The upper bound in NARROW_TAIL_UPPER.md is valid for the specified cutoff family. The Gamma contribution is \(\log k+O(1)\) because the exact digamma symbol has a pointwise logarithmic lower envelope and the low-frequency loss is integrable against the \(L^1\) Fourier bound. The only positive part of the negative prime-shift contribution comes from opposite-tail overlaps, which require \(n\ge k-1\); its all-integer majorant is \(O((\log k)/\sqrt{k})\). Same-side overlaps have the opposite sign and may be dropped only for this upper bound.

The conclusion is
\[
q_T[r_k]\le(\log k+C)\|r_k\|_2^2,\qquad
q_T[r_k]=(\log k+O(1))\|r_k\|_2^2
\]
when combined with the separately audited lower bound. This is still a single test-vector estimate. It supplies no inverse-weighted Schur quotient, full-operator sign, or RH conclusion. The Gamma upper constant depends on the fixed uniform cutoff derivative constant \(C_1\); for an absolute \(C\), that cutoff bound must be fixed uniformly across the family.

## 1. Tail and \(H^1\) bookkeeping

The lower-tail note gives, for \(u=\pi e^{2x}\ge32\),
\[
|f_0(x)|\asymp e^{x/2}u^5e^{-u}.
\]
Using \(dx=du/(2u)\), this gives squared \(L^2\) tail scale \(U^{19/2}e^{-2U}\), \(L^1\) tail scale at most \(U^{17/4}e^{-U}\), and (from one derivative of the theta summands) squared \(L^2\) derivative-tail scale at most \(U^{23/2}e^{-2U}\). These exponents are consistent:
\[
e^x u^{10}\frac{du}{2u}\asymp u^{19/2}du,\qquad
e^{x/2}u^5\frac{du}{2u}\asymp u^{17/4}du,
\]
and differentiation contributes one further factor \(u\) to \(f_0\).

The cutoff derivative term is
\[
r_k'=(1-\chi_k)f_0'-\chi_k'f_0.
\]
The first term has \(L^2\) size \(O(k^{23/4}e^{-\pi k})\); the second has size at most \(C_1k\cdot O(k^{19/4}e^{-\pi k})\). Since \(\|r_k\|_2\ge c k^{19/4}e^{-\pi k}\), this proves
\[
\|r_k'\|_2\le C(C_1)k\|r_k\|_2.
\tag{3}
\]
Thus \(r_k\in H^1\) and its normalized Fourier second moment is \(O(C_1^2 k^2)\). Only \(\chi_k'\) is used; higher derivative bounds are unnecessary for this form estimate.

## 2. Gamma upper bound with leading coefficient one

The positive series is
\[
b(t)=\sum_{j\ge0}g_t(j+\tfrac14),\qquad
g_t(v)=\frac{(t/2)^2}{v(v^2+(t/2)^2)}.
\]
For \(t\ne0\), \(g_t\) is positive decreasing. The upper sum-integral comparison
\[
\sum_{j\ge0}g_t(j+\tfrac14)
\le g_t(\tfrac14)+\int_{1/4}^{\infty}g_t(v)dv
\]
is correct: on every interval \([j+\tfrac14,j+\tfrac54]\), \(g_t(v)\le g_t(j+\tfrac14)\). Direct calculation gives
\[
g_t(\tfrac14)=\frac{16t^2}{1+4t^2}\le4,\qquad
\int_{1/4}^\infty g_t(v)dv=\frac12\log(1+4t^2),
\]
so
\[
b(t)\le4+\tfrac12\log(1+4t^2).
\tag{4}
\]
At \(t=0\) this remains true.

For the probability measure
\[
d\mu_k(t)=\frac{|\widehat r_k(t)|^2}{2\pi\|r_k\|_2^2}\,dt,
\]
Jensen applies because \(s\mapsto\log(1+4s)\) is concave. Plancherel gives \(\int t^2\,d\mu_k=\|r_k'\|_2^2/\|r_k\|_2^2\), so (3)–(4) imply
\[
\frac{\langle r_k,b(D)r_k\rangle}{\|r_k\|_2^2}
\le4+\tfrac12\log(1+4C(C_1)^2 k^2)
=\log k+O_{C_1}(1).
\]
Subtracting \(C_0\) preserves this \(\log k+O(1)\) upper bound for \(a(D)\).

## 3. Prime correlations and the cutoff \(n\ge k-1\)

For \(d>0\), \(r_k\) is nonpositive on the positive tail, nonnegative on the negative tail, and vanishes in the central interval. The two same-side overlaps are equal and nonnegative:
\[
J_k(d)=\int_{R_k}^{\infty}r_k(x)r_k(x+d)dx\ge0.
\]
The only opposite-side overlap has negative sign, so
\[
I_k(d)=2J_k(d)+I_k^{\rm cross}(d),\qquad I_k^{\rm cross}(d)\le0.
\]
Since the prime part of \(q_T=\langle r,(a(D)-S)r\rangle\) is \(-2\sum_n\alpha_nI_k(\log n)\), it equals
\[
-4\sum_n\alpha_nJ_k(\log n)
+2\sum_n\alpha_n|I_k^{\rm cross}(\log n)|.
\]
The same-side term is nonpositive in \(q_T\) and is discarded for an upper bound; the cross term is the only adverse contribution. A cross interval exists only if
\[
\log n\ge2R_k=\log k-2/k,
\quad n\ge ke^{-2/k}.
\]
For \(k\ge2\), \(k-2<ke^{-2/k}\le k-1\), so an integer \(n\) in the full prime-power sum must satisfy \(n\ge k-1\). This cutoff is valid and does not exclude any positive cross overlap.

Its length obeys
\[
L_{k,n}=\log(n/k)+2/k\le (n-k+2)/k.
\]
For \(n\ge k\), use \(\log(n/k)\le(n-k)/k\); for \(n=k-1\), use \(\log(1-1/k)\le-1/k\).

On an opposite-tail pair, reparameterize by the two positive tail coordinates \(x_1=-x\) and \(x_2=x+\log n\). Then \(x_1,x_2\ge R_k\), \(x_1+x_2=\log n\), and
\[
u_1u_2=\pi^2n^2,\qquad
u_1+u_2\ge2\pi n,\qquad
e^{(x_1+x_2)/2}=\sqrt n.
\]
The theta envelope therefore gives
\[
|r_k(x)r_k(x+\log n)|
\le |f_0(x_1)f_0(x_2)|
\le C n^{21/2}e^{-2\pi n}.
\]
Multiplying by the overlap length yields
\[
|I_k^{\rm cross}(\log n)|
\le C\frac{n-k+2}{k}n^{21/2}e^{-2\pi n},
\qquad n\ge k-1.
\]
After multiplying by \(\alpha_n\le(\log n)/\sqrt n\) and dividing by
\(\|r_k\|_2^2\ge c k^{19/2}e^{-2\pi k}\), the full cross contribution is at most
\[
Ck^{-1/2}\sum_{j\ge-1}(j+2)\log(k+j)(1+j/k)^{10}e^{-2\pi j}
=O\!\left(\frac{\log k}{\sqrt k}\right).
\]
For \(j\ge0\), \((1+j/k)^{10}\le e^{10j/k}\) and
\(\log(k+j)\le\log k+j/k\); for \(j=-1\) the single term is \(O(\log k)\). The exponential series is uniformly summable for large \(k\). Enlarging the Mangoldt-supported sum to every integer \(n\ge k-1\) is an upper bound and keeps every prime power.

Combining this vanishing relative prime contribution with (9) proves the claimed matching upper bound. The full prime-power operator is not truncated or replaced by a density estimate.

## 4. Scope of the matched asymptotic

Together with the lower-bound note's coefficient-one Gamma estimate, the result gives \(q_T[r_k]/\|r_k\|_2^2=\log k+O(1)\) for this particular cutoff tail. It does not show that \(r_k\) is an eigenvector or a minimizing vector for any Schur complement. In particular, it does not bound an expression such as \(\|C_k^{-1/2}B_k\|\), and no operator sign follows.

**Review outcome.** No fatal error found in the stated upper bound or in the \(n\ge k-1\) cross-tail summation. The coefficient-one Gamma estimate is valid under the uniform \(H^1\) cutoff bound; make its dependence on the fixed \(C_1\) explicit if the cutoff family is not fixed.

