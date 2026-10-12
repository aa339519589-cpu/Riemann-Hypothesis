# A true-theta prime-energy Mellin theorem: all power moments and the sharp p=-5 transition

Date: 2026-10-12. Final research objective remains an **unconditional complete proof of the Riemann hypothesis**. This manuscript gives a *new exact arithmetic estimate* inside the original full theta / Gamma / prime Weil operator: a uniform-integrability theorem that was explicitly **not** supplied by the earlier weak convergence of the moving-prime energy measure. It evaluates the moments of the actual prelimit prime energies, identifies the sharp negative-moment threshold and computes its logarithmic coefficient at the threshold.

**Status: NO NEW UNCONDITIONAL RH THEOREM PROVED.** No off-line zeta zero is excluded by this computation. It is not an optimization of the percentage of zeros on the line or of an auxiliary gap constant.

## 1. Actual full operator and exact critical family

Keep the original positive even theta source
\[
\Phi(x)=\sum_{n\ge1}
(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})e^{-\pi n^2e^{2x}},
\qquad\widehat\Phi(z)=\Xi(z)=\xi(1/2+iz).
\]
Set \(h=\cosh(x/2),\ p(x)=2\Phi(x)h(x),\ m=\sqrt{\Phi/(2h)}\), so \(d\nu=p(x)dx\) is a probability measure and \(Uq=\sqrt p\,q\) is the original isometry. The true prime-power edge energies are
\[
E_n(q)=\frac{\Lambda(n)}{\sqrt n}
\int_{\mathbb R}\Phi(x)\Phi(x+\log n)
\bigl|q(x+\log n)-q(x)\bigr|^2dx,\qquad n\ge2.
\tag{1}
\]
They are *all* retained, including composite prime powers. Let \(a_*=\tfrac12\log2,\ t=a_*-\delta,\ 0<\delta<a_*/2\), and define
\[
f_t=\Phi(\cdot+t)+\Phi(\cdot-t)-2\cosh(t/2)\Phi,\quad
q_t=f_t/\Phi,\quad v_t=f_t/m=Uq_t.
\tag{2}
\]
The exact source identities and the norm-convergent true-theta derivative expansion in [REPORT.md](REPORT.md) give \(Lq_t=q_t/2\), and hence \(\mathcal E(q_t)=\|v_t\|_2^2/2\) on the original even mean-zero domain. The following moment proofs use only the **explicit functions (2), their theta tails and the exact edge energy (1)**; the spectral interpretation identifies their use for RH but is not needed for the arithmetic estimates.

The true source tail yields
\[
\|v_t\|_2^2\sim\frac3{128}\delta^{-5/2}, \quad
v_t(x)=2\pi e^{5x/2-9t/2}
e^{-c_t e^{2x}}\,[1+o(1)]\quad (x\to+\infty),
\quad c_t=\pi(e^{-2t}-1/2)\sim\pi\delta .
\tag{3}
\]
The tail approximation is uniform for \(t\) in a fixed left neighborhood of \(a_*\). The full v_t is even. These precise facts were proved in [REPORT.md](REPORT.md), not inferred from a finite theta cutoff.

## 2. New exact theorem: the genuine weighted prime jump-rate asymptotic

For every fixed real \(s\), define the positive *complete* weighted prime rate
\[
\lambda_s(x)=\frac1{2h(x)}\sum_{n\ge2}
\Lambda(n)n^{s-1/2}\bigl[\Phi(x-\log n)+\Phi(x+\log n)\bigr].
\tag{4}
\]
Every series converges absolutely and locally uniformly, by the complete real theta double-exponential tails. It is even and positive.

**Theorem 1 (all real Mellin powers, no RH input).** For every real \(s\),
\[
\boxed{\lambda_s(x)\sim \xi(1+s)e^{s|x|}
\quad(|x|\to\infty),}
\tag{5}
\]
and there is a finite constant \(C_s\) such that
\[
\boxed{0<\lambda_s(x)\le C_s e^{s|x|}\quad(x\in\mathbb R).}
\tag{6}
\]
The completed factor \(\xi(1+s)=\xi(-s)>0\) is the genuine completed zeta function evaluated on the *real* axis; (5) does not assert any zero-free result in the critical strip.

**Proof.** By evenness take \(x\to+\infty\), \(X=e^x\). The forward-shift branch \(\Phi(x+\log n)\) is \(o(X^s)\) after division by \(2h(x)\), for every fixed s, by the explicit Gaussian-in-\(nX\) theta bound. For the backward branch put \(u=n/X\). Its exact algebra is
\[
X^{-s}\lambda_{s,-}(x)
=\frac{X^{1/2}}{2h(x)}
\frac1X\sum_{n\ge2}\Lambda(n)
\left(\frac nX\right)^{s-1/2}
\Phi\left(-\log\frac nX\right).
\tag{7}
\]
The prefactor tends to one. The unconditional prime number theorem gives vague convergence
\(X^{-1}\sum_{n\ge2}\Lambda(n)\delta_{n/X}\to du\) on \((0,\infty)\). The test
\(\phi_s(u)=u^{s-1/2}\Phi(-\log u)\)
is continuous, is \(O_s(u^{s-5}e^{-\pi/u^2})\) as \(u\downarrow0\), and is \(O_s(u^{s+4}e^{-\pi u^2})\) as \(u\to\infty\). The elementary bound \(\psi(Y)=\sum_{n\le Y}\Lambda(n)\ll Y\) and partial summation give uniform small-u and large-u tails; thus vague convergence upgrades to convergence against this exact noncompact test, for each fixed s. The limit is
\[
\int_0^\infty u^{s-1/2}\Phi(-\log u)du
=\int_{\mathbb R}\Phi(y)e^{-(s+1/2)y}dy
=\xi(-s)=\xi(1+s).
\tag{8}
\]
The last equality uses the exact theta Mellin transform and the unconditional functional equation, not any Euler product inside the critical strip. As \(\Phi>0\), the limit is strictly positive. This proves (5). Positivity, continuity and the positive finite limit of \(\lambda_s(x)e^{-s|x|}\) then give (6). □

For s=0 this recovers only the *leading* \(1/2\) of the previously known stronger \(\lambda_0(x)=1/2-e^{-|x|}/2+O(e^{-2|x|})\). The entire real-parameter family (5), including arbitrarily negative s, is the new arithmetic input here.

## 3. Actual (not just limiting-distribution) weighted energies

Define, for each fixed real s and \(\delta=a_*-t\),
\[
\boxed{M_s(\delta)=
\frac{\delta^{s/2}}{\|v_t\|_2^2}
\sum_{n\ge2}n^s E_n(q_t).}
\tag{9}
\]
Each sum converges for every fixed \(t<a_*\), s real. Since all terms are nonnegative, \(M_s(\delta)\) is well-defined and positive. Unlike the Mellin moments of the *limiting* prime-scale probability measure in the previous [PRIME_ENERGY_SCALING.md](PRIME_ENERGY_SCALING.md), (9) is a moment of the **actual original finite-t full prime-power energy measure**.

Introduce the signed weighted shift
\[
S_s f=\sum_{n\ge2}\Lambda(n)n^{s-1/2}
[f(\cdot+\log n)+f(\cdot-\log n)]
\tag{10}
\]
on the smooth double-exponentially decaying true sources \(f_t\). Expanding the real squares in the genuine edge form (1) and changing integration variables gives the exact, **all-prime** identity
\[
\boxed{\sum_{n\ge2}n^sE_n(q_t)
=\int_{\mathbb R}|v_t(x)|^2\lambda_s(x)dx
-\langle f_t,S_s f_t\rangle.}
\tag{11}
\]
No positive prime cross term is discarded in the derivation.

**Lemma 2 (uniformly bounded full weighted cross term).** For every fixed s,
\[
\sup_{a_*/2\le t\le a_*}
\left|\langle f_t,S_s f_t\rangle\right|<\infty.
\tag{12}
\]
Indeed fix any \(a>\max(0,s+1/2)\) and set \(F_t(x)=e^{a|x|}|f_t(x)|\). The family \(\|F_t\|_2\) is uniformly bounded throughout the closed t interval because its *slowest* theta source tail at the endpoint still has exponent \(-(\pi/2)e^{2|x|}\). Since \(|x|+|x+d|\ge d\),
\[
\int|f_t(x)f_t(x+\log n)|dx
\le n^{-a}\|F_t\|_2^2 .
\]
Now \(\sum_{n\ge2}\Lambda(n)n^{s-a-1/2}<\infty\); the von Mangoldt series here is taken only in its honest absolute convergence range. This proves (12) and the legal changes of sums in (11). □

## 4. Exact power moments for every s greater than -5

**Theorem 2 (uniform integrability, sharp open range).** For *every fixed* real \(s>-5\),
\[
\boxed{
\lim_{\delta\downarrow0}M_s(\delta)
=\frac{\xi(1+s)}{(2\pi)^{s/2}}
\frac{\Gamma((s+5)/2)}{\Gamma(5/2)}.}
\tag{13}
\]
Thus the moments of the **actual positive prime-energy measures** converge to the Mellin moments of the explicit limiting measure from PRIME_ENERGY_SCALING.md. Weak convergence alone had not justified this statement, especially for \(s<0\) or \(s>0\).

**Proof.** By Lemma 2 and (3), the normalized weighted cross term in (11) has absolute value
\[
O_s\!\left(\frac{\delta^{s/2}}{\|v_t\|_2^2}\right)
=O_s(\delta^{(s+5)/2})=o(1)
\quad(s>-5).
\tag{14}
\]
Write \(I_s(t)=\int |v_t(x)|^2e^{s|x|}dx\). Exact substitution in the uniform theta first-mode tail (3), followed by \(u=2c_t e^{2x}\), gives for \(s>-5\)
\[
I_s(t)\sim4\pi^2e^{-9a_*}
\Gamma((s+5)/2)(2c_t)^{-(s+5)/2}.
\tag{15}
\]
All fixed spatial compacts contribute O(1), negligible compared with (15). The \(\Gamma\) integral is finite precisely when s>-5; for this open range the true theta asymptotic has an integrable rescaled majorant on both ends.

Theorem 1 gives \(\lambda_s(x)=\xi(1+s)e^{s|x|}[1+o_{|x|\to\infty}(1)]\). Given any \(\eta>0\), pick a fixed R so the ratio differs from \(\xi(1+s)\) by at most \(\eta\) for \(|x|>R\). The compact \([-R,R]\) contributes O(1) to \(\int|v_t|^2\lambda_s\), while \(I_s(t)\to\infty\) by (15). Letting t approach the endpoint and then \(\eta\to0\),
\[
\int |v_t|^2\lambda_s\,dx
\sim\xi(1+s)I_s(t).
\tag{16}
\]
Divide (15) by its s=0 counterpart, use \(c_t/\delta\to\pi\), and multiply by \(\delta^{s/2}\):
\[
\lim_{\delta\downarrow0}\delta^{s/2}I_s(t)/I_0(t)
=(2\pi)^{-s/2}\Gamma((s+5)/2)/\Gamma(5/2).
\]
Combine (11), (14) and (16). □

The proof uses the complete real theta source, the unconditional PNT and full prime energy, not a candidate zero-free hypothesis. It also yields convergence on any fixed compact subset of s>-5 for which the elementary theta/PNT envelopes are selected uniformly; pointwise s is all that is needed for the theorem.

## 5. Borderline logarithmic divergence with an exact zeta(5) coefficient

**Theorem 3 (critical exponent).** At the precise exponent s=-5,
\[
\boxed{
M_{-5}(\delta)
\sim 40\sqrt2\,\zeta(5)\,\log(1/\delta)
\quad(\delta\downarrow0).}
\tag{17}
\]
In particular the moment diverges. This sharp coefficient is not a property of an arbitrary weakly convergent family: it uses the actual θ first-mode norm singularity and the **complete** prime-rate asymptotic.

**Proof.** As before, Theorem 1 gives
\(\lambda_{-5}(x)\sim\xi(-4)e^{-5|x|}=\xi(5)e^{-5|x|}\).
Using (3) directly at the borderline yields
\[
\boxed{
\int |v_t(x)|^2e^{-5|x|}dx
\sim 4\pi^2\,2^{-9/2}\,\log(1/\delta).}
\tag{18}
\]
The factor follows by doubling the positive x integral and putting \(r=e^{2x}\):
\[
4\pi^2e^{-9t}\int_1^\infty r^{-1}e^{-2c_t r}dr
=4\pi^2\,2^{-9/2}\log(1/c_t)+O(1).
\]
The first-mode relative error is uniformly \(O(e^{-2x})\) in the escaping x region and is integrable after insertion of the weight e^{-5x}, so it does not alter the logarithmic coefficient. The full prime-rate ratio tends to its real completed-zeta constant; comparison beyond a fixed large spatial R and compact O(1) terms then give
\[
\int|v_t|^2\lambda_{-5}dx
\sim4\pi^2\,2^{-9/2}\xi(5)\log(1/\delta).
\tag{19}
\]
The source cross term is O(1) by Lemma 2 and hence lower-order relative to the logarithm. Meanwhile \(\delta^{-5/2}/\|v_t\|_2^2\to128/3\). Thus
\[
M_{-5}(\delta)\sim
\frac{128}{3}\cdot4\pi^2\,2^{-9/2}\xi(5)\log(1/\delta).
\]
The exact completed-zeta identity
\(\xi(5)=15\zeta(5)/(2\pi^2)\)
reduces the coefficient to \(40\sqrt2\,\zeta(5)\). □

For an independent consistency check, the right side of (13) has simple pole as \(s\downarrow-5\), with residue \(80\sqrt2\zeta(5)\). It is **twice** the coefficient in (17), as expected from \(\Gamma((s+5)/2)\sim2/(s+5)\) and the boundary layer in the actual theta integral. This is an algebraic check, not an alternative proof that allows exchanging the limits \(s\downarrow-5\) and \(\delta\downarrow0\).

## 6. Below -5: endpoint energy and a genuine divergence power

At \(t=a_*\), the source \(f_{a_*}\) remains a rapidly decreasing entire-real theta combination, while \(v_{a_*}=f_{a_*}/m\) grows like \(2\pi e^{5|x|/2-9a_*/2}\) and is not in L². The expression \(E_n(q_{a_*})\) defined by the **literal positive edge integral (1)** is nevertheless meaningful whenever the corresponding integral converges. No spectral eigenstate or Hilbert normalization is asserted at this endpoint.

**Theorem 4.** For each fixed real \(s<-5\), the *weighted complete original endpoint prime energy*
\[
\mathcal W_s=\sum_{n\ge2}n^s E_n(q_{a_*})
\tag{20}
\]
converges, satisfies \(0<\mathcal W_s<\infty\), and
\[
\boxed{
M_s(\delta)\sim\frac{128}{3}\,\mathcal W_s\,
\delta^{(s+5)/2}\longrightarrow\infty .}
\tag{21}
\]

**Proof.** The explicit true theta tails imply the uniform endpoint inequality
\[
|v_t(x)|^2\le C e^{5|x|}
\quad(a_*/2\le t\le a_*).
\]
Theorem 1 gives \(\lambda_s(x)\le C_se^{s|x|}\). Thus for s<-5 the weighted diagonal in (11) is dominated by the integrable function \(C_se^{(s+5)|x|}\). By dominated convergence it tends to \(\int|v_{a_*}|^2\lambda_s\). The cross term in (11) also converges by its absolutely summable majorant from Lemma 2, since \(f_t\to f_{a_*}\) in every fixed exponentially weighted L² space. The resulting limit is exactly the sum of endpoint positive edge integrals by Tonelli. It is finite and positive: \(q_{a_*}\) is not constant or periodic, so at least the n=2 edge has strictly positive energy. Finally (3) implies
\(\delta^{s/2}/\|v_t\|_2^2\sim(128/3)\delta^{(s+5)/2}\), proving (21). □

Equations (13), (17), (21) identify the **exact** transition at s=-5:
- s>-5: finite explicit moment limit;
- s=-5: logarithmic divergence with zeta(5) coefficient;
- s<-5: power divergence with an explicit endpoint edge-energy constant.

No finite prime cutoff, omission of the source cross term, or unproved exchange of limits was used.

## 7. Why this matters for the actual full RH target

The previous moving-prime law showed weak convergence of the energy distribution for a special known equality family, but explicitly declined to claim convergence of unbounded moments. Theorem 2 supplies the **missing uniform-integrability control**, while Theorems 3–4 prove it cannot extend through s=-5. The positive prime-energy measure has exact arithmetic tails controlled by completed-zeta moments, and its sharp source escape exponent fixes the only Mellin boundary.

These identities are genuine full-\(\zeta\), full-theta, full-prime facts. They constrain any proposal that reweights or renormalizes the complete Weil jumps as the spectral parameter approaches the critical threshold. However, they concern known equality modes, not arbitrary real-even test functions, and do **not** prove \(E(q)\ge\frac12\mathrm{Var}_\nu(q)\) or exclude the hypothetical subcritical spectrum. A future RH proof still must control *all* test vectors, including the orthogonal complement of the true theta equality modes.

**Acceptance: unconditional true-prime Mellin moment theorem; NO NEW UNCONDITIONAL RH THEOREM PROVED.**

### Source dependencies and verification scope

The literal source and edge definitions are in rounds/05/REPORT-pages-01-05.txt; the original jump-rate identity is in rounds/05/REPORT-pages-06-10.txt; the theta translation family and its Hilbert singularity are in this directory's REPORT.md; its previously proved weak energy law is PRIME_ENERGY_SCALING.md. The only additional arithmetic input is the classical unconditional prime number theorem for \(\psi(X)\), used strictly in its legitimate domain as a real weighted counting theorem. No literature-priority, external referee or formal proof-assistant verification is claimed.
