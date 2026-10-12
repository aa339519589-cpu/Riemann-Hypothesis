# Narrow-cutoff tail lower bound for the full source form

## Result and scope

Let
\[
T=a(D)-S,\qquad
(Sf)(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       \{f(x+\log n)+f(x-\log n)\},
\]
with the complete prime-power sum, and write \(a(t)=b(t)-C_0\), where
\[
b(t)=\operatorname{Re}\psi\!\left(\tfrac14+\tfrac{it}{2}\right)
      -\psi(\tfrac14),\qquad
C_0=\gamma+\tfrac{\pi}{2}+3\log2+\log\pi>0.
\]
Use the exact odd source zero mode
\[
f_0=(D^3-D/4)\Phi,\qquad Tf_0=0.
\]
For \(a_k=\frac12\log k\), set \(R_k=a_k-k^{-1}\). Suppose \(\chi_k\) is real, even, smooth, \(0\le\chi_k\le1\), equals \(1\) on \(|x|\le R_k\), equals \(0\) on \(|x|\ge a_k\), and has the stated derivative bounds \(\|\chi_k^{(j)}\|_\infty\le C_jk^j\). Define
\[
r_k=(1-\chi_k)f_0.
\]
Then there are absolute \(c,C>0\) and \(K\) such that for every \(k\ge K\),
\[
\boxed{\quad
q_T[r_k]\ge \bigl(\log k-C\bigr)\|r_k\|_2^2>0,
\qquad
\|r_k\|_2^2\ge c\,k^{19/2}e^{-2\pi k}.
\quad}
\tag{1}
\]
The lower bound is unconditional and uses every prime power. It is a statement only about this explicit tail vector and the full source form \(q_T\); it gives no lower bound for an actual inverse-weighted coupling or Schur quotient, no full-operator sign, and no RH conclusion.

For each fixed \(k\), \(r_k\) is smooth and Schwartz: it vanishes on \([-R_k,R_k]\), agrees with \(f_0\) on \(|x|\ge a_k\), and differs from \(f_0\) only on a compact transition. Thus the complete prime correlation series converges absolutely. For example, for large \(d\), at least one of \(|x|\), \(|x+d|\) is at least \(d/2\), and the double-exponential tails give
\[
\int |r_k(x)r_k(x+d)|\,dx
\le 2\|r_k\|_1\sup_{|y|\ge d/2}|r_k(y)|
\le C_k e^{-c e^d}.
\]
Multiplication by \(\Lambda(n)/\sqrt n\le\log n/\sqrt n\), with \(d=\log n\), is summable. The form identity below is therefore legitimate for each \(k\).

## Uniform theta-tail facts and the mass of \(r_k\)

In the centered coordinate \(x\), put \(u=\pi e^{2x}\). For the \(m\)-th theta summand, the exact formula from the source calculation is
\[
f_0(x)=e^{x/2}\sum_{m\ge1}F_1(m^2u)e^{-m^2u},
\quad
F_1(u)=-uG(u),
\]
\[
G(u)=32u^4-360u^3+1056u^2-810u+90.
\tag{2}
\]
The previously checked inequalities \(G(12)>0\) and \(G'(u)>0\) for \(u\ge12\) imply \(F_1(u)<0\) there. For all sufficiently large \(u\), \(|F_1(u)|\asymp u^5\). Once \(u\) is large, all terms in (2) have the same negative sign; the \(m=1\) term gives a lower bound, and
\(\sum_{m\ge1}m^{10}e^{-(m^2-1)u}=O(1)\) gives an upper bound. Hence, with constants independent of \(x\),
\[
c e^{x/2}u^5e^{-u}
\le -f_0(x)\le C e^{x/2}u^5e^{-u}
\quad (u\ge U_0).
\tag{3}
\]
In particular, \(f_0(x)<0\) for \(x\ge R_k\) once \(k\) is large, since
\[
u(R_k)=U_R:=\pi k e^{-2/k}\longrightarrow\infty.
\tag{4}
\]
Oddness gives the opposite sign on the negative tail.

Changing variables \(u=\pi e^{2x}\), so \(dx=du/(2u)\) and \(e^x=(u/\pi)^{1/2}\), (3) gives the one-sided tail estimates
\[
\int_{\pi e^{2x}\ge U}|f_0(x)|^2\,dx
\asymp U^{19/2}e^{-2U},
\qquad
\int_{\pi e^{2x}\ge U}|f_0(x)|\,dx
\le C U^{17/4}e^{-U}
\tag{5}
\]
for all large \(U\). For the first formula, the transformed squared integrand is a constant times \(u^{19/2}e^{-2u}\); for the second it is bounded by a constant times \(u^{17/4}e^{-u}\). The standard fixed-power exponential tail bounds follow, for example, by splitting into unit intervals starting at \(U\).

Because \(r_k=f_0\) for \(x\ge a_k\), (3) on \(a_k\le x\le a_k+k^{-1}\) yields
\[
\|r_k\|_2^2
\ge 2\int_{a_k}^{a_k+k^{-1}}|f_0(x)|^2\,dx
\ge c\,k^{19/2}e^{-2\pi k}.
\tag{6}
\]
Indeed, on this interval \(u\in[\pi k,\pi k e^{2/k}]\), whose length in the \(u\)-variable is bounded above and below by positive constants; the transformed squared integrand is \(\asymp u^{19/2}e^{-2u}\).

The same tail estimates give a concentration inequality needed only for the low-frequency bound:
\[
\|r_k\|_1\le 2\int_{R_k}^\infty |f_0(x)|\,dx
\le C U_R^{17/4}e^{-U_R},
\]
whereas
\[
\|r_k\|_2^2\ge2\int_{a_k}^\infty |f_0(x)|^2\,dx
\ge c(\pi k)^{19/2}e^{-2\pi k}.
\]
Since \(U_R=\pi k e^{-2/k}\) and \(0\le\pi k-U_R\le2\pi\), it follows that
\[
\boxed{\quad \|r_k\|_1^2\le \frac{C}{k}\|r_k\|_2^2.\quad}
\tag{7}
\]
No lower bound on \(\chi_k\) inside the transition is needed: the upper estimate uses only \(0\le1-\chi_k\le1\), and the lower estimate uses \(1-\chi_k=1\) for \(x\ge a_k\).

## Gamma lower bound with the full leading coefficient

The exact positive series for \(b\) is
\[
b(t)=\sum_{j\ge0}
\frac{(t/2)^2}{(j+1/4)((j+1/4)^2+(t/2)^2)}.
\tag{8}
\]
For fixed \(t\), the summand as a function of \(v=j+1/4>0\),
\[
\frac{(t/2)^2}{v(v^2+(t/2)^2)},
\]
is decreasing. Therefore its left-endpoint sum dominates its integral:
\[
b(t)\ge
\int_{1/4}^{\infty}
\frac{(t/2)^2}{v(v^2+(t/2)^2)}\,dv
=\tfrac12\log(1+4t^2).
\tag{9}
\]

Since \(\tfrac12\log(1+4t^2)\ge\log(2|t|)\) for \(t\ne0\), compare this lower bound pointwise with \(\log(2k)\):
\[
b(t)\ge \log(2k)-\mathbf1_{\{|t|<k\}}\log(k/|t|).
\tag{10a}
\]
For \(|t|<k\), the right side is \(\log(2|t|)\); for \(|t|\ge k\), it is \(\log(2k)\le\log(2|t|)\). The total loss from the correction term is finite and, by \(|\widehat r_k(t)|\le\|r_k\|_1\) and (7), bounded by
\[
\frac1{2\pi}\int_{|t|<k}\log(k/|t|)|\widehat r_k(t)|^2\,dt
\le\frac{\|r_k\|_1^2}{2\pi}
   \int_{-k}^{k}\log(k/|t|)\,dt
=\frac{k}{\pi}\|r_k\|_1^2
\le C\|r_k\|_2^2,
\]
since \(\int_{-k}^{k}\log(k/|t|)\,dt=2k\). Thus integration of (10a) gives
\[
\langle r_k,b(D)r_k\rangle
=\frac1{2\pi}\int b(t)|\widehat r_k(t)|^2\,dt
\ge \bigl(\log(2k)-C\bigr)\|r_k\|_2^2.
\tag{10b}
\]
The constant subtraction in \(a(D)=b(D)-C_0\) contributes exactly \(-C_0\|r_k\|_2^2\).

## Full prime-power term: same-side debit is exponentially small

For real \(r_k\), symmetry of the shifts gives
\[
q_T[r_k]
=-C_0\|r_k\|_2^2+\langle r_k,b(D)r_k\rangle
-2\sum_{n\ge2}\alpha_n I_{k,n},
\quad
I_{k,n}=\int_{\mathbb R}r_k(x)r_k(x+\log n)\,dx,
\quad
\alpha_n=\frac{\Lambda(n)}{\sqrt n}.
\tag{11}
\]
The sum is over all integers with nonzero von Mangoldt weight, hence all prime powers and no truncation at \(n=k\).

Write \(r_{k,+}=r_k|_{(0,\infty)}\). By (3)–(4), \(r_{k,+}\le0\) on \([R_k,\infty)\); by oddness, \(r_k\ge0\) on \((-\infty,-R_k]\), and \(r_k=0\) on \([-R_k,R_k]\). For \(d>0\), the correlation separates into a same-side term and a negative cross-tail term:
\[
I_k(d)
=2J_k(d)+I_k^{\mathrm{cross}}(d),\qquad
J_k(d)=\int_{R_k}^\infty r_k(x)r_k(x+d)\,dx\ge0,
\quad I_k^{\mathrm{cross}}(d)\le0.
\tag{12}
\]
The factor \(2\) is the equality of the positive-positive and negative-negative overlaps by oddness. The only other possible overlap has \(x\le-R_k\) and \(x+d\ge R_k\), where the factors have opposite signs. Thus it helps, rather than hurts, the lower bound on \(q_T\). In particular,
\[
-2\alpha_n I_{k,n}\ge-4\alpha_n J_k(\log n).
\tag{13}
\]

For \(d=\log n\), Cauchy–Schwarz and \(|r_k|\le|f_0|\) give
\[
J_k(d)
\le \|r_{k,+}\|_2
   \left\|f_0\,\mathbf1_{[R_k+d,\infty)}\right\|_2.
\tag{14}
\]
Also \(\|r_{k,+}\|_2\ge\|f_0\,\mathbf1_{[a_k,\infty)}\|_2\). Set
\[
U_n=\pi e^{2(R_k+\log n)}
=\pi k n^2e^{-2/k}.
\]
The two-sided tail comparison (5) therefore implies
\[
\frac{\|f_0\,\mathbf1_{[R_k+\log n,\infty)}\|_2}
     {\|f_0\,\mathbf1_{[a_k,\infty)}\|_2}
\le C n^{19/2}e^{-(U_n-\pi k)}
\le C n^{19/2}e^{-\frac{\pi}{2}k(n^2-1)}
\qquad(n\ge2,\ k\ge K).
\tag{15}
\]
For the last inequality, take \(K\) large enough that \(e^{-2/k}\ge3/4\); then
\(n^2e^{-2/k}-1\ge\frac23(n^2-1)\) for \(n\ge2\).
Combining (14)–(15),
\[
J_k(\log n)
\le C n^{19/2}e^{-\frac{\pi}{2}k(n^2-1)}
        \|r_{k,+}\|_2^2.
\tag{16}
\]
Use \(\Lambda(n)\le\log n\) and sum over all integers \(n\ge2\), which only enlarges the prime-power sum. Equations (13) and (16) give
\[
-2\sum_{n\ge2}\alpha_n I_{k,n}
\ge -C\|r_k\|_2^2
\sum_{n\ge2}(\log n)n^9e^{-\frac{\pi}{2}k(n^2-1)}
\ge -C e^{-c k}\|r_k\|_2^2.
\tag{17}
\]
This estimate discards the favorable opposite-sign cross-tail correlations and controls every potentially negative same-side correlation. It uses no prime distribution theorem.

Finally combine (10b), (11), and (17):
\[
q_T[r_k]\ge
\bigl(\log(2k)-C-C_0-Ce^{-ck}\bigr)\|r_k\|_2^2
\ge\bigl(\log k-C'\bigr)\|r_k\|_2^2.
\]
Together with (6), this proves (1), and the coefficient makes the form strictly positive for all sufficiently large \(k\).

## What this does not prove

The positive tail energy is not a positivity theorem for \(T\): it tests one \(k\)-dependent vector \(r_k\). The full source identity \(Tf_0=0\) is used only to certify that the specified \(f_0\) is the exact zero mode; the lower bound itself follows from its explicit theta tail, the positive digamma series, and the sign/correlation analysis of the complete prime sum. Neither the cutoff mode \(\chi_kf_0\) nor \(r_k\) supplies an estimate for \(\|C_k^{-1/2}B_k\|\) or an actual inverse-weighted Schur debit. No weighted \(1/m\) transfer, full-H sign, or RH statement is inferred.
