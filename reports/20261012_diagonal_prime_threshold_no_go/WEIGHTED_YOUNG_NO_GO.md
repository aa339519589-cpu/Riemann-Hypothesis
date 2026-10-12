# Weighted Young no-go at the exact half-gap

Date 2026-10-12. This supplements REPORT.md. It is a theorem about a specific comparison scheme for the original theta/Gamma/prime operator, not a proof of RH.

## The true vectors

Use the unchanged original even operator H and its actual normalized ground mode e0=sqrt(2 Phi cosh(x/2)), with H e0=-e0/2. Let e1 be the L2-normalized version of
\[
v_1=\sqrt{2\Phi(x)\cosh(x/2)}
\left(\frac{\Phi''(x)}{\Phi(x)}-\frac14\right).
\]
The full theta explicit formula gives H e1=0, and integration by parts gives <e0,e1>=0. All modes belong to the original operator domain. The real e0 is positive everywhere.

The first critical mode e1 changes sign: the actual certified theta bounds give Phi(0)>0 and Phi''(0)<0; so e1(0)<0. The first theta mode dominates at +infinity, where Phi''/Phi~4pi²exp(4x) tends to +infinity. Hence e1 is eventually positive. It is analytic and not identically zero. For the fixed shift d=log 2, there is a nonempty compact interval I of positive length ell on which
\[
e_1(x)\le-a<0,\quad e_1(x+d)\ge b>0,\quad
0<e_0(x),e_0(x+d)\le M,\quad
m(x)m(x+d)\ge\mu>0.                                     \tag{1}
\]
Proof of existence: choose a negative-sign point x0 avoiding the countable set of all lattice shifts of real zeros. Since e1(x0+nd)>0 for large n, at some first n the sign changes from negative to positive across d. Continuity supplies I and uniform constants.

## Any weighted prime-edge majorant has a nonzero unavoidable defect

Let alpha=log(2)/sqrt(2)>0. For **any** measurable theta(x)>0 for which the ensuing quadratic form is defined, the weighted Young inequality for the actual prime n=2 gives the exact nonnegative defect
\[
P_\theta[z]=\alpha\int m(x)m(x+d)
\left|\sqrt{\theta(x)}z(x)
-\theta(x)^{-1/2}z(x+d)\right|^2dx.                    \tag{2}
\]
The weight theta may depend arbitrarily on epsilon and may tend to zero or infinity. For any real u,v of *opposite signs* and theta>0,
\[
|\sqrt\theta u-v/\sqrt\theta|^2\ge4|uv|,             \tag{3}
\]
by AM-GM. Thus no tuning of theta can eliminate the n=2 defect where a test function crosses sign during that shift.

## Uniform rank-two obstruction

On the true two-dimensional space W=span(e0,e1), take z=Ae0+Be1, so ||z||²=A²+B². Pick a fixed delta in (0,min(a,b)/(2M)]. Define
\[
\mathfrak C_\theta[z]=\tfrac12A^2+P_\theta[z].
\]
If |A|>=delta|B|, then
\[
\mathfrak C_\theta[z]\ge
\frac{\delta^2}{2(1+\delta^2)}\|z\|^2.                 \tag{4}
\]
If |A|<delta|B|, the signs of z(x),z(x+d) are opposite for all x in I and |z(x)z(x+d)|>=ab B²/4. Equations (1)-(3) then give
\[
P_\theta[z]\ge\alpha\mu\ell ab B^2
\ge\frac{\alpha\mu\ell ab}{1+\delta^2}\|z\|^2.       \tag{5}
\]
Consequently the strictly positive constant
\[
c_*=\min\left\{
\frac{\delta^2}{2(1+\delta^2)},
\frac{\alpha\mu\ell ab}{1+\delta^2}
\right\}>0
\]
satisfies
\[
\boxed{\tfrac12A^2+P_\theta[z]\ge c_*\|z\|^2
\quad\text{for all real z in W and all theta>0}.}     \tag{6}
\]
There is no dependence on J, N, epsilon, or the diagonalizing weight.

**Theorem.** Suppose a valid selfadjoint lower comparison K_(epsilon,theta) to the original H+epsilon is constructed by replacing the actual n=2 prime shift by the weighted Young diagonal majorant, while all other steps incur only nonnegative form defects. Then
\[
H+\epsilon-K_{(\epsilon,\theta)}\succeq P_\theta,
\]
and, since H is diagonal with eigenvalues -1/2 and 0 on W,
\[
\langle z,K_{(\epsilon,\theta)}z\rangle
\le\epsilon\|z\|^2-\left(\tfrac12A^2+P_\theta[z]\right)
\le(\epsilon-c_*)\|z\|^2.
\]
Thus for **every** 0<epsilon<c_* and **every** choice of theta_epsilon,
\[
\boxed{\operatorname{ind}_-K_{(\epsilon,\theta)}\ge2.} \tag{7}
\]
This includes weights tuned to saturate the ground state and all choices of Gamma/remaining-prime truncation. If K is congruent to I-T through a positive boundedly invertible multiplier, T necessarily has at least two eigenvalues above one, so a rank-one inertia certificate cannot continue to epsilon=0.

The original H was *not* proved to have negative spectrum. The bound only rules out this weighted-diagonal comparison scheme. Exact signed prime shifts, including the adaptive original resolvent method, are not ruled out.

Input verification: the source identity and mode domain in rounds/05, and the exact theta derivative signs in reports/20261011_universal_factor_obstruction/certificate_portable.json. The remaining proof is elementary quadratic form algebra and continuity. No external review or formal verification is claimed. **NO NEW UNCONDITIONAL RH THEOREM PROVED.**
