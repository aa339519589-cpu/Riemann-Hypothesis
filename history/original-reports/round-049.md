## Round 49 — audit of the Zenodo 22113226 polylogarithm/Herglotz proof claim

I audited the version-1.25 manuscript and its supplied scripts:
https://zenodo.org/records/22113226. The verdict is **不成立 as an
unconditional proof**.

### I. The advertised decomposition is an exact tautology

With

\[
 z_1=2-\sqrt2,\qquad z_2=\sqrt2-1,\qquad
 c_n=1-z_1^n-z_2^n,
\]

we have \(z_1+z_2=1\), and for \(\Re s>1\)

\[
\begin{aligned}
 \operatorname{Li}_s(z_1)+\operatorname{Li}_s(z_2)
 +\sum_{n\ge1}\frac{c_n}{n^s}
 &=\sum_{n\ge1}\frac{z_1^n+z_2^n+c_n}{n^s}\\
 &=\sum_{n\ge1}\frac1{n^s}
 =\zeta(s).
\end{aligned}
\tag{49.1}
\]

The positivity of \(c_n\) gives a positive kernel partition, but (49.1)
imposes no new restriction on \(\zeta\), its zeros, or its logarithmic
derivative. In the region \(\Re s>1\), the bound on
\(\zeta'/\zeta\) used by the manuscript is already the ordinary Euler-product
triangle inequality.

### II. The central angular inequality is RH in local form

The manuscript defines

\[
 T(r,\theta)=\frac{\partial}{\partial\theta}
 \log\left|\xi\!\left(\tfrac12+re^{i\theta}\right)\right|.
\]

Suppose an off-critical zero \(\rho\) has
\(\rho-\tfrac12=r_0e^{i\theta_0}\) with
\(0<\theta_0<\pi/2\), and has multiplicity \(m\). Locally,

\[
 \xi(s)=(s-\rho)^m h(s),\qquad h(\rho)\ne0.
\]

Along the circle \(s(\theta)=\tfrac12+r_0e^{i\theta}\),

\[
 T(r_0,\theta)
 =m\,\Re\!\left(
 \frac{ir_0e^{i\theta}}{r_0e^{i\theta}-r_0e^{i\theta_0}}
 \right)+O(1)
 =\frac{m}{\theta-\theta_0}+O(1).
\tag{49.2}
\]

Thus \(T(r_0,\theta)\to+\infty\) as
\(\theta\downarrow\theta_0\) from above. The reflected zero supplied by the
functional equation handles the opposite side of the critical line. Hence

\[
 T(r,\theta)\le0\ \text{for every }r>0,\ 0<\theta<\pi/2
 \quad\Longrightarrow\quad \text{RH}.
\tag{49.3}
\]

This implication is valid, but it makes the claimed global angular inequality
the entire RH-bearing lemma. A finite computation of \(T\) away from unknown
zeros cannot establish it.

### III. The supplied “interval verification” is not an interval proof

The code audit gives three independent failures.

1. \`subregion_C_interval.py\` sets \`N_PHI = 3\` and evaluates only
   \(\phi_k(r)=k/(3r)\), \(k=1,2,3\). The target region is the whole interval
   \(0<\phi\le\phi_{\max}(r)\). No monotonicity or enclosure in the
   \(\phi\)-direction is proved, so three curves do not cover the intervening
   continuum.

2. The same script computes the alleged second-derivative bound from endpoint
   finite differences:
   \[
   D_2=\frac{|T_r(r_{\rm hi})-T_r(r_{\rm lo})|}
   {r_{\rm hi}-r_{\rm lo}},
   \]
   and multiplies it by a declared safety factor. Endpoint samples do not bound
   the derivative inside a cell, and a safety factor is not a theorem. The
   zeta derivatives are also obtained by finite differences of ordinary
   \`mpmath\` evaluations, not by certified interval enclosures.

3. \`region2_verified_v2.py\` uses central finite differences for first and
   second derivatives and explicitly treats center values multiplied by a
   safety factor as a “rigorous” cell bound. \`subregion_C_extended.py\` uses
   ordinary double-precision complex evaluations and a golden-section search
   with a single-peak assumption. Neither supplies a proof over the continuum.

Beyond the finitely checked height, a zero-density estimate controls how many
zeros occur, not a positive lower bound for
\(\left|\xi(\tfrac12+re^{i\theta})\right|\) in the asserted region. Such a
lower bound is exactly what would be needed to make \(\xi'/\xi\) uniformly
bounded there; (49.2) shows why it cannot be assumed before RH.

**Established:** the three-term identity (49.1) is correct, and the implication
(49.3) from angular monotonicity to RH is correct.

**Failure / error:** the manuscript does not prove angular monotonicity. Its
finite-difference scripts neither enclose the full \((r,\theta)\) region nor
certify the derivative bounds required for cell arguments.

**Remaining load-bearing statement:** an unconditional, noncircular proof of
the global angular inequality, including all possible pole neighborhoods.
The claimed Herglotz property, Hankel positivity, and Jacobi operator all
depend on that missing statement.

**RH status:** no unconditional proof has been produced.
