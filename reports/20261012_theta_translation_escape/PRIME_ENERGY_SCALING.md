# Exact moving-prime energy law on genuine critical RH equality modes

Date: 2026-10-12. **Unconditional auxiliary theorem** using the genuine theta source, the full Gamma jump form, all von Mangoldt prime-power jumps, and the classical prime number theorem (PNT). The only inputs about the Weil operator are the original theta/source identities from round 5 and the sharp true-kernel theta translation established in REPORT.md. No RH assumption, off-axis zero data, finite-prime replacement, or truncation of the actual energy is used.

**Mathematical status: NO NEW UNCONDITIONAL RH THEOREM PROVED.** This report identifies how the full true arithmetic jump energy of *exact critical equality vectors* moves to primes of scale \((a_*-t)^{-1/2}\), and computes its limiting probability law and exact Mellin moments. It is not a claim that all vectors obey the desired sharp Poincaré inequality.

## 1. Full original objects and a singular exact equality family

With the original positive even Jacobi theta source \(\Phi\), put
\[
h=\cosh(x/2),\quad p=2\Phi h,\quad m^2=\Phi/(2h),
\quad \widehat\Phi(z)=\Xi(z),\quad a_*=\tfrac12\log2 .
\]
For \(0<t<a_*\), define
\[
f_t(x)=\Phi(x+t)+\Phi(x-t)-2\cosh(t/2)\Phi(x),\quad
q_t=f_t/\Phi,\quad v_t=f_t/m=Uq_t .
\tag{1}
\]
The analytic true theta source identity \((A-S)\Phi=-h\) and the closed original form domain imply, by the norm-convergent critical derivative expansion of REPORT.md,
\[
H v_t=0,\qquad Lq_t=\tfrac12 q_t,\qquad \int q_t\,d\nu=0.
\tag{2}
\]
This is exact for every t in the displayed open interval, with all primes retained. Hence the real-even complete energy is saturated:
\[
\boxed{\mathcal E(q_t)=\tfrac12\|q_t\|_{L^2(\nu)}^2
=\tfrac12\|v_t\|_2^2.}\tag{3}
\]

Put \(\delta=a_*-t\downarrow0\), \(c_t=\pi(e^{-2t}-1/2)\sim\pi\delta\). The *full* theta first-mode tail and REPORT.md yield
\[
\boxed{\|v_t\|_2^2\sim\frac3{128}\delta^{-5/2}.}\tag{4}
\]
For \(x\to+\infty\), uniformly as \(t\uparrow a_*\),
\[
v_t(x)=2\pi e^{5x/2-9t/2}e^{-c_te^{2x}}(1+o(1)),
\tag{5}
\]
and v_t is even in x. This is an **actual spectral equality family**, not a trial vector replacing the zeta source.

Split the original Dirichlet form exactly into
\[
\mathcal E=\mathcal E_\Gamma+\mathcal E_P,\qquad
\mathcal E_P(q)=\sum_{n\ge2}\mathcal E_n(q),
\]
\[
\mathcal E_n(q)=\frac{\Lambda(n)}{\sqrt n}
\int_{\mathbb R}\Phi(x)\Phi(x+\log n)
|q(x+\log n)-q(x)|^2dx.
\tag{6}
\]
All summands are nonnegative. The Gamma part is the exact real continuous-jump term from round 4.

## 2. Gamma-shaped escape of the equality-state Hilbert mass

Define a probability law on the positive half-line via
\[
\mathbb P_t(dx)=2|v_t(x)|^2\,dx/\|v_t\|_2^2,\qquad x>0
\]
(the factor two follows from parity), and the rescaled coordinate
\[
Z_t=2c_t e^{2x}.
\tag{7}
\]

**Lemma 1.** As \(t\uparrow a_*\),
\[
\boxed{Z_t\Longrightarrow Z,\qquad
\mathbb P(Z\in dz)=
\frac{z^{3/2}e^{-z}}{\Gamma(5/2)}\,dz,\ z>0.}\tag{8}
\]
Indeed (5), the substitution \(z=2c_t e^{2x}\) and the exact norm asymptotic (4) give this density after normalization. To justify weak convergence, first restrict z to compact positive intervals, where the first-mode approximation is uniform; then use the same exponential majorant and the gamma integral to control both ends. Compact x regions have vanishing normalized mass. No zero counting or RH input occurs.

## 3. Exact prime-energy algebra and a bounded cross term

For bounded real weights g(n√δ), write
\[
\mathcal E_{P,g}(q_t)=\sum_{n\ge2}g(n\sqrt\delta)\mathcal E_n(q_t),
\]
\[
\lambda_{P,g,\delta}(x)=\frac1{2h(x)}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(n\sqrt\delta)
[\Phi(x+\log n)+\Phi(x-\log n)].
\tag{9}
\]

**Lemma 2 (no discarded cross terms).** With \(S_{g,\delta}\) denoting the indicated signed-weight prime translation sum on its Schwartz source,
\[
\boxed{\mathcal E_{P,g}(q_t)
=\int_{\mathbb R}|v_t(x)|^2\lambda_{P,g,\delta}(x)dx
-\langle f_t,S_{g,\delta}f_t\rangle.}\tag{10}
\]
This follows exactly by expanding each square (6) and changing variables in its two diagonal terms. For every bounded g,
\[
\boxed{|\langle f_t,S_{g,\delta}f_t\rangle|
\le C\,\|g\|_\infty,\quad a_*/2\le t\le a_*,\ 0<\delta<a_*/2,}
\tag{11}
\]
with C independent of t and δ.

Proof of (11). For every a>1/2, setting \(F_t(x)=e^{a|x|}|f_t(x)|\), the triangle inequality \(|x|+|x+d|\ge d\) gives
\[
\int|f_t(x)f_t(x+d)|dx\le e^{-ad}\|F_t\|_2^2.
\]
The family \(f_t\) is uniformly double-exponentially decreasing for real t on the compact interval, so \(\sup_t\|F_t\|_2<\infty\). Since
\(\sum_{n\ge2}\Lambda(n)n^{-a-1/2}<\infty\) for a>1/2, the complete von Mangoldt cross sum is absolutely bounded. Thus (11) is uniform even when the cutoff moves with δ; it is NOT an unproved finite-prime remainder assertion. After division by (4), its contribution is \(O(\delta^{5/2})\).

The unweighted true jump rate is
\[
\lambda_P(x)=\lambda_{P,1,\delta}(x)=\frac{S\Phi(x)}{2h(x)}
=\frac12-\frac12e^{-|x|}+O(e^{-2|x|})\quad (|x|\to\infty).
\tag{12}
\]
It is positive and bounded. The final asymptotic is already derived from the true source identity in round 5 §6.2; it also follows directly by inserting the first theta moment
\(\int\Phi(y)e^{y/2}dy=1/2\) into the large-x \(e^{-(x-y)/2}\) leading term of the genuine Gamma kernel. The local Gamma jump singularity must be kept in the canceling difference near y=x, where the theta terms are super-exponentially small; it is not permissible to integrate its individual positive and negative pieces there.

## 4. All Gamma energy becomes negligible; the prime energy carries one half

**Theorem A (sharp Gamma-versus-prime split).** In the full original Dirichlet form,
\[
\boxed{
\frac{\mathcal E_\Gamma(q_t)}{\|q_t\|_\nu^2}
\sim\frac{2\sqrt2}{3}\sqrt{\delta},
\qquad
\frac{\mathcal E_P(q_t)}{\|q_t\|_\nu^2}
=\frac12-\frac{2\sqrt2}{3}\sqrt{\delta}+o(\sqrt\delta).}
\tag{13}
\]
In particular the limiting prime share of the exact one-half equality energy is ALL of that one-half, rather than an arbitrary finite collection of jumps.

**Proof.** Equation (3) and (10) at g=1 give
\[
\mathcal E_\Gamma(q_t)
=\int(\tfrac12-\lambda_P(x))|v_t(x)|^2dx
+\langle f_t,Sf_t\rangle.
\tag{14}
\]
The second term is O(1) by Lemma 2. By (12), the leading integrand at spatial infinity is \(\frac12e^{-|x|}|v_t(x)|^2\), with error O(e^(-2|x|)|v_t|²). The same first-mode substitution used for (4), now with one factor e^(-|x|), gives
\[
\int_{\mathbb R}e^{-|x|}|v_t(x)|^2dx
\sim2^{-9/2}\delta^{-2},\qquad
\int_{\mathbb R}e^{-2|x|}|v_t(x)|^2dx
=O(\delta^{-3/2}).
\tag{15}
\]
On fixed spatial compact sets both relevant integrals are O(1). Hence
\[
\mathcal E_\Gamma(q_t)
\sim2^{-11/2}\delta^{-2}.
\]
Divide by (4) to obtain
\(2^{-11/2}/(3/128)=2\sqrt2/3\) times \(\delta^{1/2}\). The second statement of (13) follows from the *exact* total equality (3). □

## 5. Every shorter-than-square-root moving prime prefix is negligible

**Theorem B (true moving-cutoff bound).** For some absolute finite C and all \(a_*/2\le t<a_*\), \(N\ge2\),
\[
\boxed{
0\le\sum_{2\le n\le N}\mathcal E_n(q_t)
\le C N^5\log(2N).}\tag{16}
\]
Consequently
\[
\boxed{
0\le\frac{\sum_{n\le N}\mathcal E_n(q_t)}{\|q_t\|_\nu^2}
\le C'\delta^{5/2}N^5\log(2N).}\tag{17}
\]
For every fixed \(\eta\in(0,1/2)\), any moving cutoff satisfying \(N(\delta)\le\delta^{-1/2+\eta}\) obeys
\[
\boxed{\frac{\sum_{n\le N(\delta)}\mathcal E_n(q_t)}{\|q_t\|_\nu^2}\longrightarrow0.}\tag{18}
\]
Therefore the complete **remaining** prime powers above that cutoff account for asymptotically one half of the full unit-norm equality energy.

**Proof.** The exact theta first-mode upper and lower bounds and \(|t|\le a_*\) imply the all-real envelope
\[
\frac{|f_t(x)|^2}{\Phi(x)}\le C e^{(9/2)|x|}.
\tag{19}
\]
The denominator retains the positive COMPLETE theta series; on each tail the two translates have slowest squared exponential \(e^{-\pi e^{2|x|}}\), which cancels the denominator's \(e^{-\pi e^{2|x|}}\). Adjust C on a compact central interval.

Expand the prime difference square and use \(|A-B|^2\le2|A|^2+2|B|^2\). With \(d=\log n\) this yields
\[
\mathcal E_n(q_t)\le 2\alpha_n\int
\frac{|f_t(x)|^2}{\Phi(x)}
[\Phi(x+d)+\Phi(x-d)]dx.
\]
Since \(|x|\le|x\pm d|+d\) and Φ has every real exponential moment,
\[
\int e^{(9/2)|x|}\Phi(x\pm d)dx
\le n^{9/2}\int e^{(9/2)|y|}\Phi(y)dy.
\]
Thus
\[
\mathcal E_n(q_t)\le C\alpha_n n^{9/2}
=C\Lambda(n)n^4.
\]
Sum with \(\Lambda(n)\le\log n\) to obtain (16), then use (4) and (13) for the asserted normalized limits. This is a uniform bound for an actually MOVING prefix, not merely a fixed-N statement. □

## 6. The limiting law of the actual arithmetic energy across moving primes

Define a finite positive measure on (0,∞) by
\[
\mathfrak M_t
=\frac1{\|q_t\|_\nu^2}
\sum_{n\ge2}\mathcal E_n(q_t)\,
\delta_{n\sqrt{\delta}}.
\tag{20}
\]
It has total mass tending to 1/2 by Theorem A.

Let Z have the Gamma(5/2,1) law from Lemma 1 and let Y be **independent** of Z, with the genuine theta-tilted probability density
\[
\boxed{\mathbb P(Y\in dy)=2\Phi(y)e^{-y/2}\,dy.}\tag{21}
\]
Normalization uses the actual completed zeta moment \(\int\Phi(y)e^{-y/2}dy=\xi(0)=1/2\). Define the positive random variable
\[
\boxed{\mathsf S=\sqrt{\frac{Z}{2\pi}}\,e^{-Y}.}\tag{22}
\]

**Theorem C (full-von-Mangoldt prime-energy scaling).** As \(t\uparrow a_*\), the positive measures converge weakly on \((0,\infty)\):
\[
\boxed{\mathfrak M_t\ \Longrightarrow\
\tfrac12\,\operatorname{Law}(\mathsf S).}\tag{23}
\]
Equivalently, for every bounded continuous \(g:(0,\infty)\to\mathbb R\),
\[
\boxed{
\lim_{t\uparrow a_*}
\frac{\sum_{n\ge2}g(n\sqrt\delta)\mathcal E_n(q_t)}
{\|q_t\|_\nu^2}
=\frac12\mathbb E\,g(\mathsf S).}\tag{24}
\]
Thus the actual energies concentrate on prime powers with \(\log n=\frac12\log(1/\delta)+O(1)\), in a nondegenerate, fully explicit arithmetic/theta distribution. The phrase "concentrate" refers to the normalized positive energy measures (20), not to an RH-zero location claim.

### Proof via the true PNT and controlled moving scales

For a bounded compactly supported continuous g, consider a sequence \(x\to+\infty\), \(\delta\downarrow0\) with
\(\kappa=e^x\sqrt\delta\to\kappa_0\in(0,\infty)\). The \(\Phi(x+\log n)\) branch in (9) is super-exponentially small after division by \(2h(x)\). Put \(X=e^x,\ u_n=n/X\) in the other branch:
\[
\begin{aligned}
&\frac1{2h(x)}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\Phi(x-\log n)g(n\sqrt\delta)\\
&\hspace{4mm}=
\frac{X^{1/2}}{2h(x)}
\frac1X\sum_{n\ge2}\Lambda(n)\,
u_n^{-1/2}\Phi(-\log u_n)g(\kappa u_n).
\end{aligned}
\tag{25}
\]
The unconditional PNT says the positive rescaled measures
\(X^{-1}\sum_{n\ge2}\Lambda(n)\delta_{n/X}\)
converge vaguely to Lebesgue measure on \((0,\infty)\). The test \(u^{-1/2}\Phi(-\log u)g(\kappa u)\) is continuous and rapidly vanishing at zero and infinity. Its tails are bounded uniformly by elementary Chebyshev \(\psi(X)\ll X\) plus partial summation: near zero it is \(O(u^{-5}e^{-\pi/u^2})\), and near infinity \(O(u^4e^{-\pi u^2})\). As \(\kappa\) stays in a compact positive interval, these bounds and the continuity of g give sequentially uniform convergence in (25). Since \(X^{1/2}/(2h(x))\to1\), the limit is
\[
\int_0^\infty u^{-1/2}\Phi(-\log u)g(\kappa_0u)\,du
=\int_{\mathbb R}\Phi(y)e^{-y/2}g(\kappa_0e^{-y})dy.
\tag{26}
\]
This is exactly \(\frac12\mathbb E_Y[g(\kappa_0e^{-Y})]\). No analytic continuation of the Euler product into the critical strip is invoked: (25) is an ordinary PNT asymptotic of the actual positive von Mangoldt coefficients.

By Lemma 1, under the normalized full-even Hilbert mass, the positive spatial coordinate x escapes and \(Z_t=2c_te^{2x}\Rightarrow Z\). On any compact positive Z-window,
\[
e^x\sqrt\delta=
\sqrt{\frac{Z_t\delta}{2c_t}}
\longrightarrow\sqrt{\frac Z{2\pi}}
\]
uniformly with the moving x relation. Equation (26) therefore applies jointly. Moreover, for bounded g, \(|\lambda_{P,g,\delta}(x)|\le\|g\|_\infty\lambda_P(x)\), and λ_P is bounded globally. Dominated convergence after the gamma-window truncation gives
\[
\frac1{\|v_t\|_2^2}\int |v_t(x)|^2
\lambda_{P,g,\delta}(x)dx
\longrightarrow\frac12\mathbb E_{Z,Y}
g\Bigl(\sqrt{Z/(2\pi)}e^{-Y}\Bigr).
\]
The exact prime cross term is \(O(1)/\|v_t\|_2^2\to0\) by (11), proving (24) for \(g\in C_c((0,\infty))\).

Finally the total masses of (20) tend to 1/2 by Theorem A, which equals the total mass of the limit. Vague convergence of finite positive measures on the locally compact space \((0,\infty)\), together with convergence of their total masses, yields weak convergence and hence (24) for all bounded continuous g. □

## 7. Completed-zeta moment identity for the limiting prime scale

The limiting variable in (22) has explicit Mellin moments. For every real p>-5, independence, the Gamma law, and the EXACT completed-zeta Mellin identity give
\[
\begin{aligned}
\mathbb E\,\mathsf S^p
&=(2\pi)^{-p/2}
\frac{\Gamma(5/2+p/2)}{\Gamma(5/2)}
\int_{\mathbb R}2\Phi(y)e^{-(p+1/2)y}dy\\
&=\boxed{
\frac{2\xi(1+p)}{(2\pi)^{p/2}}\,
\frac{\Gamma(5/2+p/2)}{\Gamma(5/2)}.}
\end{aligned}\tag{27}
\]
Here \(\xi(-p)=\xi(1+p)\) is the unconditional functional equation, and \(\xi(s)>0\) for real s by the positive theta Mellin integral. The restriction p>-5 is sharp because Z has Gamma shape 5/2 at zero; the Y law has all real exponential moments.

For instance,
\[
\boxed{\mathbb E\,\mathsf S=\frac{4\sqrt2}{9},\qquad
\mathbb E\,\mathsf S^2=\frac{15\zeta(3)}{4\pi^2}.}\tag{28}
\]
These are moments of a **limiting prime-energy scale**, not a zeta-zero theorem. No claim of literary priority or independent formal verification is made.

## 8. What remains to prove RH

The limits (13), (18), (23) and (27) rigorously describe an explicit family **already lying at the critical 1/2 eigenvalue**. They show that its sharp energy depends on prime powers escaping with \(n\asymp (a_*-t)^{-1/2}\), so neither fixed prime cutoffs nor sub-square-root moving cutoffs capture it. They do NOT control arbitrary mean-zero vectors, potential eigenvectors in (0,1/2), or the off-axis zeros.

A full RH proof still requires the universal inequality
\(\mathcal E(q)\ge\frac12\mathrm{Var}_\nu(q)\)
(or a logically independent complete zero-location theorem). The present scaling law exposes the arithmetic multi-scale mechanism any such proof must preserve; it does not assume that preserving it is sufficient.

Sources: fifth-round original identity and prime jump-rate tail in rounds/05/REPORT-pages-01-05.txt and rounds/05/REPORT-pages-06-10.txt §6.2; exact critical translation and its singularity in this directory's REPORT.md; classical unconditional PNT/Chebyshev estimates; the standard Jacobi theta Mellin transform \(\mathcal M\Phi=\xi\). The proof is analytic, not a finite numerical experiment. A separate internal audit must not be confused with external referee acceptance.
