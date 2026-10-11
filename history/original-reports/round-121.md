## Round 121 — two local repairs: the coefficient nonvanishing calculation and the logarithmic sampling lemma

This round closes two small pieces of the audit of *Overdetermined Weil
Systems*, while keeping the global status unchanged.  The first correction is
algebraic and uses the formulas printed in that manuscript; the second is a
self-contained proof of the discrete exponential-polynomial lemma that the
manuscript invokes incorrectly.

### 121.1 The manuscript's “only \(A=B=0\)” elimination is false as stated

The appendix writes, for an off-line zero \(\rho=\sigma+i\gamma\) with
\(\gamma>0\), \(0<\sigma<1/2\),

\[
 A=\sigma\log|\rho|-\gamma\arg\rho,
 \qquad
 B=\sigma\arg\rho+\gamma\log|\rho|,
\]

and, in the displayed coefficient formulas, the first two coefficients
vanish only if

\[
 \frac{A}{A^2+B^2}
 +\frac{A+\gamma\pi}{(A+\gamma\pi)^2+(B-\sigma\pi)^2}=0,
 \qquad
 \frac{B}{A^2+B^2}
 +\frac{B-\sigma\pi}{(A+\gamma\pi)^2+(B-\sigma\pi)^2}=0.
 \tag{121.1}
\]

The text then claims that (121.1) forces \(A=B=0\).  That claim is not an
algebraic consequence of the equations.  Put

\[
 v=(A,B),\qquad w=(A+\gamma\pi,B-\sigma\pi),
 \qquad r^2=\|v\|^2,\quad R^2=\|w\|^2.
\]

Provided the displayed denominators are nonzero, (121.1) is exactly

\[
 \frac{v}{r^2}+\frac{w}{R^2}=0.
 \tag{121.2}
\]

Thus \(w=-k v\) for \(k=R^2/r^2>0\).  Since

\[
 w-v=(\gamma\pi,-\sigma\pi),
 \qquad R^2=k^2r^2,
\]

the definition of \(k\) gives \(k=k^2\), hence \(k=1\).  Consequently the
nonzero algebraic solution is

\[
 (A,B)=\left(-\frac{\gamma\pi}{2},\frac{\sigma\pi}{2}\right),
 \qquad
 (A+\gamma\pi,B-\sigma\pi)
 =\left(\frac{\gamma\pi}{2},-\frac{\sigma\pi}{2}\right).
 \tag{121.3}
\]

So the manuscript's stated elimination is false even before one uses the
special definitions of \(A\) and \(B\).  The nonvanishing conclusion can,
however, be repaired for an actual \(\rho\).  Indeed, on the chosen logarithm
branch,

\[
 A+iB=(\sigma+i\gamma)(\log|\rho|+i\arg\rho)=\rho\log\rho.
\]

Equation (121.3) would therefore imply

\[
 \rho\log\rho=\frac{i\pi}{2}\rho.
\]

Since \(\rho\ne0\), this gives \(\log\rho=i\pi/2\), hence
\(\rho=i\) on the principal branch and therefore \(\sigma=0\), contradicting
\(0<\sigma<1/2\).  Also \(A=B=0\) itself would give
\(\rho\log\rho=0\), so \(\log\rho=0\) and \(\rho=1\), contradicting
\(\gamma>0\).  Thus the first two coefficients cannot vanish simultaneously
for an actual zero in the stated open off-line strip, but this requires the
compatibility argument above; the manuscript's printed “only \(A=B=0\)” step
is not a valid proof.

This repair is local.  It does not repair the preceding admissibility and
regularization failures recorded in Rounds 118 and 120, and it does not turn
those formal coefficient identities into valid Weil-test identities.

### 121.2 A complete discrete exponential-polynomial lemma

The manuscript also appeals to the identity theorem after observing that
\(\log n\to+\infty\).  Infinity is not a finite accumulation point, so that
argument is invalid.  The underlying statement is nevertheless true in the
finite-dimensional setting relevant to the appendix.

**Lemma.**  Let \(\lambda_1,\ldots,\lambda_m\) be distinct complex numbers and
let

\[
 P(t)=\sum_{j=1}^{m}c_j e^{\lambda_j t}.
\]

If \(P(\log n)=0\) for every sufficiently large integer \(n\), then all
\(c_j=0\).

**Proof.**  We induct on the number of distinct real parts among the
\(\lambda_j\).  Let \(\alpha\) be the largest real part and write the maximal
real-part group as

\[
 G(t)=\sum_{\Re\lambda_j=\alpha}c_j e^{i\Im\lambda_j t}.
\]

After division by \(e^{\alpha t}\), the hypothesis gives, at
\(t_n=\log n\),

\[
 G(t_n)
 =-\sum_{\Re\lambda_j<\alpha}c_j
   e^{(\Re\lambda_j-\alpha)t_n}e^{i\Im\lambda_j t_n}
 \longrightarrow0.
 \tag{121.4}
\]

The derivative of \(G\) is bounded on the real line.  For
\(t\in[t_n,t_{n+1}]\), the interval length
\(\log(n+1)-\log n\to0\); therefore (121.4) and the mean-value estimate imply
\(G(t)\to0\) as \(t\to+\infty\), not merely along the logarithmic sample.

Let the distinct frequencies in \(G\) be
\(\beta_1,\ldots,\beta_q\), with coefficients \(d_1,\ldots,d_q\).  For
\(L>0\),

\[
 \frac1L\int_T^{T+L}|G(t)|^2\,dt
 =\sum_{a,b}d_a\overline{d_b}
   e^{i(\beta_a-\beta_b)T}
   \frac{e^{i(\beta_a-\beta_b)L}-1}
        {i(\beta_a-\beta_b)L},
 \tag{121.5}
\]

where the diagonal quotient is \(1\).  For fixed \(T\), letting \(L\to\infty\)
leaves \(\sum_a|d_a|^2\), because the off-diagonal quotients tend to zero.
On the other hand \(G(t)\to0\) and \(G\) is bounded, so for every
\(\varepsilon>0\) one can choose \(T\) with \(|G(t)|<\varepsilon\) for all
\(t\ge T\); the left side of (121.5) is then at most \(\varepsilon^2\).
Thus \(\sum_a|d_a|^2=0\), so every maximal-group coefficient is zero.

Remove that group and repeat.  Induction over the finitely many real parts
proves \(c_j=0\) for all \(j\).  \(\square\)

This lemma repairs only the discrete linear-independence substep.  It supplies
neither the missing valid test-function approximation nor the passage from a
formal finite coefficient identity to the complete zero sum.  The global RH
implication therefore remains open in the audited route.

**Round-121 result:** two local statements are now precise: the coefficient
nonvanishing can be salvaged by a corrected compatibility argument, and the
logarithmic sampling lemma is proved without the invalid identity-theorem
step.  Neither result closes the admissibility, convergence, finite selected
branch, or infinite off-line branch required for an unconditional RH proof.

**RH status:** no unconditional proof has been produced.
