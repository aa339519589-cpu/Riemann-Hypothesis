# Complete prime-power grouping: tail variances and an AR(1) signed kernel

These exact identities retain every power of each prime. They do not
prove the coefficient-one comparison or RH.

## 1. Positive weighted tail coordinates

Fix a prime `p`, put `d=log p`, `a=p^(-1/2)`, and, for `0<t<d`, define

\[
 x_j=t+jd,\quad q_j(t)=a^j\psi(x_j),\quad u_j(t)=r(x_j),
\]
\[
 M_m(t)=\sum_{j\ge m}q_j(t),\quad
 \mu_m(t)=\frac{\sum_{j\ge m}q_j(t)u_j(t)}{M_m(t)},\quad
 V_m(t)=\sum_{j\ge m}q_j(t)|u_j(t)-\mu_m(t)|^2.
\tag{1}
\]

The masses are positive. All expressions are finite on the ratio core;
theta tails also allow the theta-jet ratios. Set

\[
 b_m=a^{-2m},\qquad \Delta b_0=1,\qquad
 \Delta b_m=a^{-2m}-a^{-2(m-1)}\quad(m\ge1).
\]

The complete forward `p`-power energy has the exact hierarchical
factorization

\[
 \boxed{P_{F,p}[r]
 =2d\int_0^d\sum_{m\ge0}\Delta b_m M_m(t)V_m(t)\,dt.}
\tag{2}
\]

To prove it, the pair `i<j` has actual forward weight

\[
 a^{j-i}\psi(x_i)\psi(x_j)
 =q_iq_j b_i
 =q_iq_j\sum_{m\le i}\Delta b_m.
\]

Interchanging nonnegative sums and using weighted variance gives

\[
 \sum_{i<j}b_iq_iq_j|u_i-u_j|^2
 =\sum_m\Delta b_m\sum_{m\le i<j}q_iq_j|u_i-u_j|^2
 =\sum_m\Delta b_m M_mV_m.
\]

Thus (2) keeps the extra long-range within-fiber coercivity omitted by
the simpler bound `P_F,p >= 2d integral M_0 V_0`.

## 2. Reflected powers reduce to one paired-fiber mean mismatch

Write a bar on the argument for reflection of the base point:
`bar t=d-t`. The exact reflected `p`-power form is

\[
 N_p[r]=da\int_0^d\sum_{j,l\ge0}
 q_j(t)q_l(\bar t)|u_j(t)-u_l(\bar t)|^2\,dt.
\tag{3}
\]

Indeed the original reflection index is `k=j+l+1`, and its actual
von Mangoldt coefficient is `d a^{j+l+1}`. Integrating over all `t in
(0,d)` double counts unordered endpoint pairs exactly as the original
reflected definition does; no further factor of two is inserted.

The two-population variance identity gives

\[
 \boxed{\begin{aligned}
 N_p[r]={}&2da\int_0^d M_0(\bar t)V_0(t)\,dt\\
 &+da\int_0^dM_0(t)M_0(\bar t)
              |\mu_0(t)-\mu_0(\bar t)|^2\,dt.
 \end{aligned}}
\tag{4}
\]

Before using the `t <-> bar t` symmetry, the variance terms are
`M_0(bar t)V_0(t)+M_0(t)V_0(bar t)`. Formula (4) is exact for complex
ratios as well as real ones.

Combining (2) and (4), with
`H_p(t)=M_0(t)-aM_0(d-t)`, gives

\[
\begin{aligned}
 P_{F,p}[r]-N_p[r]
 ={}&2d\int_0^dH_p(t)V_0(t)\,dt\\
 &+2d\int_0^d\sum_{m\ge1}\Delta b_mM_m(t)V_m(t)\,dt\\
 &-da\int_0^dM_0(t)M_0(\bar t)
                 |\mu_0(t)-\mu_0(\bar t)|^2\,dt.
\end{aligned}
\tag{5}
\]

One must not assume `H_p>=0`. The exact theta source gives the rigorous
strict bound `H_2(3 log(2)/4)<-2/3`. The full analytic tail proof and exact
rational checks are in `PRIME_TWO_MASS_IMBALANCE.md` and
`check_factorizations.py`. This is an obstruction to the naive first-term
variance payment, not a negative vector for the complete form.

The identities can be summed over primes on the actual core without
introducing a divergent free diagonal: each nonnegative part of (2) is
bounded by `P_F`, and each nonnegative part of (4) is bounded by `N`.
In (5), keep the two pieces defining `H_p` separately when checking
absolute integrability. They are bounded by the respective forward and
reflected variance totals.

## 3. The exact remaining Gamma/pole payment

Let `H_+=max(H,0)` and `H_-=max(-H,0)`. The desired sign `P>=N` is exactly

\[
\begin{aligned}
 P_\Gamma[r]+P_{\rm pole}[r]
 &+2\sum_p d\int_0^d\left[
 H_{p,+}V_0+\sum_{m\ge1}\Delta b_m M_mV_m\right]dt\\
 &\ge\sum_p da\int_0^dM_0(t)M_0(\bar t)
                 |\mu_0(t)-\mu_0(\bar t)|^2dt
 +2\sum_p d\int_0^dH_{p,-}V_0\,dt.
\end{aligned}
\tag{6}
\]

This isolates the unpaid pieces into paired-fiber mean mismatch and the
negative part of an explicit mass imbalance. It is a new coordinate
form of the remaining comparison, not a proof of it. A generic
Cauchy--Schwarz estimate that is strict on the neutral theta jets cannot
by itself prove (6), because all those jets must remain equality cases.

## 4. Exact AR(1) factorization of the signed prime source adjacency

The raw source correlations admit an independent factorization. For a
compact positive-wing source `g=psi r`, define the fiber vector
`g_t=(g(t+jd))_(j>=0)`, the geometric vector `v=(a^j)_(j>=0)`, and

\[
 T_a(i,j)=a^{|i-j|}.
\]

On `L2((0,d);ell2)` set

\[
 (\mathcal B_pg)_t=T_ag_t-av\langle v,g_{d-t}\rangle.
\tag{7}
\]

The source mixed terms from all powers of `p`, with the exact conventions
of the reflected-prime report, are

\[
\begin{aligned}
 &-4d\sum_{k\ge1}a^k\operatorname{Re}
       \int_0^\infty\overline{g(x)}g(x+kd)dx\\
 &\qquad+2d\sum_{k\ge1}a^k
       \int_0^{kd}\overline{g(x)}g(kd-x)dx\\
 &\hspace{12mm}=-2d\int_0^d
       \langle g_t,[(\mathcal B_p-I)g]_t\rangle dt.
\end{aligned}
\tag{8}
\]

The reflected integral and the right side are real by endpoint symmetry.
For `0<t<d/2`, put

\[
 z_\pm(t)=\frac{g_t\pm g_{d-t}}{\sqrt2}.
\]

Then the two folded blocks of `B_p` are `T_a-avv*` on `z_+` and
`T_a+avv*` on `z_-`. Let

\[
 v_m(j)=\mathbf1_{j\ge m}a^{j-m}.
\]

The elementary geometric covariance identity is

\[
 T_a=vv^*+(1-a^2)\sum_{m\ge1}v_mv_m^*.
\]

Consequently

\[
 \boxed{\quad
 \langle z,(T_a\mp avv^*)z\rangle
 =(1\mp a)|\langle v,z\rangle|^2
 +(1-a^2)\sum_{m\ge1}|\langle v_m,z\rangle|^2.
 \quad}
\tag{9}
\]

These are bounded, strictly positive operators on `ell2`. Equivalently,
with `S` the unilateral lower shift and `L=(I-aS)^{-1}`,

\[
 T_a\mp avv^*=L\,\operatorname{diag}
       (1\mp a,1-a^2,1-a^2,\ldots)\,L^*.
\tag{10}
\]

Their inverses are explicit tridiagonal operators obtained by inverting
(10). This is an exact factorization of the signed reflected/forward
**adjacency**, not positivity of the full source deficit: (8) has a
minus sign and the indispensable subtraction of `I`.

In particular, one must never separate `sum_p log(p) I` from the
subtracted block in (8). On a compact source supported inside `(0,R)`,
all terms of (8) vanish for `log p>2R`, because the original source
correlations have no overlap. The compensated block expression must
retain that cancellation.

## 5. Scope

The prime-power grouping offers genuinely noncompact fiber means and
tails, so it is not excluded by the neutral-jet constraints.
It also exposes exactly why positivity of an AR(1) covariance is not
already the desired positivity: its source contribution is a compensated
negative adjacency, and the Gamma/pole payment in (6) remains unknown.
