# Exact positive cut-current factorization of every signed reference load

This gives an exact factorization of the reference Green correction on
its whole normalized load space. It is **not** a proof of `K <= I` or RH.

## 1. The actual reference and its completed source space

Use `reports/20261013_full_prime_green_reference/REFERENCE_INVERSE.md` and
`CORRECTION_WITH_SIGNED_PATHS.md`. Let `d = log 2`. At fixed
`t in (0,d)` put `x_j=t+jd` and

\[
 w_j=\psi(x_j)\sinh(x_j/2),\qquad
 c_j=2\alpha_2\psi(x_j)\psi(x_{j+1}),\qquad
 D_j=w_j+c_j+c_{j-1},\quad c_{-1}=0.
\]

Let `A_t` have neighbor entries `c_j/sqrt(D_j D_{j+1})`.
The cited reference proves uniformly `||A_t|| <= rho < 1`. Its normalized
Green operator is `(I-A_t)^{-1}`. The unnormalized Green entries, not an
unweighted bounded operator assertion, are

\[
 g_t(i,j)=D_i^{-1/2}[(I-A_t)^{-1}]_{ij}D_j^{-1/2}.
\]

The signed-path report proves

\[
 g_t(i,j)=\frac{p_{\min(i,j)}s_{\max(i,j)}}{\mathcal W},
\tag{1}
\]

where `p_0=1`, `p_1=D_0/c_0`, `p` solves the homogeneous recurrence,
`p_j` is strictly increasing, `s_j` is strictly positive and decreases to
zero, and

\[
 \mathcal W=c_j(p_{j+1}s_j-p_js_{j+1})>0
\]

is independent of `j`. All objects below depend on `t`; we suppress it.

## 2. The path interactions telescope into weighted cut currents

Define

\[
 a_j=c_jp_jp_{j+1}>0.
\]

The Wronskian identity gives

\[
 \frac{s_j}{p_j}-\frac{s_{j+1}}{p_{j+1}}
 =\frac{\mathcal W}{a_j}.
\]

Since `s_j -> 0` and `p_j >= 1`, the ratio on the left telescopes all the
way to infinity. Therefore

\[
 \frac{s_m}{\mathcal Wp_m}=\sum_{k\ge m}\frac1{a_k},
 \qquad
 \boxed{g_t(i,j)=p_ip_j\sum_{k\ge\max(i,j)}\frac1{a_k}.}
\tag{2}
\]

In particular every tail resistance in (2) is finite. For an arbitrary
finitely supported complex vertex load `Q`, expand the finite vertex sums
and use (2):

\[
 \boxed{\quad
 \sum_{i,j}\overline{Q_i}g_t(i,j)Q_j
 =\sum_{k\ge0}\frac1{a_k}
     \left|\sum_{j=0}^{k}p_jQ_j\right|^2.
 \quad}
\tag{3}
\]

This is an exact sum of squares, not a bound obtained by discarding mixed
terms. Every signed interaction occurs inside the same prefix sum. The
weights `p_j` are essential: replacing the weighted prefix by an ordinary
unweighted cut current is not an identity for this killed chain.

For example, an oriented dipole `Q=delta_i-delta_j`, `i<j`, contributes

\[
 \sum_{m\le k}p_mQ_m=
 \begin{cases}
 0,& k<i,\\
 p_i,&i\le k<j,\\
 p_i-p_j,&k\ge j.
 \end{cases}
\tag{4}
\]

Thus even after both endpoints have been passed, the transformed cut
current has a strictly negative tail. For ordered disjoint dipoles
`i<j<k<l`, these tails produce exactly

\[
 (\delta_i-\delta_j)^*g_t(\delta_k-\delta_l)
 =\frac{(p_i-p_j)(s_k-s_l)}{\mathcal W}<0.
\]

The positive squares in (3) therefore coexist with the strictly negative
edge cross-coefficients. Formula (3) explains rather than erases them.

## 3. Extension to the entire actual normalized load space

For `q in ell^2` set `Q_j=sqrt(D_j) q_j` and define

\[
 (\mathcal C_tq)_k
 =\frac1{\sqrt{a_k}}\sum_{j=0}^{k}p_j\sqrt{D_j}\,q_j.
\tag{5}
\]

For finitely supported `q`, (3) is

\[
 \|\mathcal C_tq\|^2
 =\langle q,(I-A_t)^{-1}q\rangle.
\tag{6}
\]

Consequently `C_t` extends boundedly, with

\[
 \frac1{1+\rho}\|q\|^2
 \le\|\mathcal C_tq\|^2
 \le\frac1{1-\rho}\|q\|^2.
\tag{7}
\]

For each fixed output coordinate the sum in (5) is finite, so the extended
operator still has exactly the displayed coordinate formula. No
unnormalized `ell^2` requirement on `Q` is imposed. Measurability follows
from the recurrence for `p_j(t)` and the measurable coefficients. The
uniform bound in (7) gives a bounded direct integral

\[
 \mathcal C=\int_0^d{}^\oplus\mathcal C_t\,dt,
 \qquad
 \boxed{(I-A)^{-1}=\mathcal C^*\mathcal C.}
\tag{8}
\]

One may prove (8) first on functions supported in finitely many fiber
coordinates, then use their density and the uniform bound. This avoids
interchanging a conditionally convergent sum of signed edge interactions.

## 4. Equivalent ground transform and explicit potential recovery

For every finitely supported ratio vector `v`, the same recurrence gives

\[
 \sum_jw_j|v_j|^2+\sum_jc_j|v_j-v_{j+1}|^2
 =\sum_ja_j\left|\frac{v_j}{p_j}
                         -\frac{v_{j+1}}{p_{j+1}}\right|^2.
\tag{9}
\]

Indeed the coefficient of `|v_j|^2` on the right is
`(c_jp_{j+1}+c_{j-1}p_{j-1})/p_j=D_j`; its mixed coefficient is
`-2c_j`. Equation (9) extends to the reference completion by closing the
right-hand transform of finite vectors, not by admitting arbitrary
boundary values at infinity.

For a load in Section 3 put `S_k=sum_{j<=k}p_jQ_j`. The reference solution
has

\[
 \boxed{v_i=p_i\sum_{k\ge i}\frac{S_k}{a_k}.}
\tag{10}
\]

The series is absolutely convergent by Cauchy--Schwarz using (2)--(3).
For finite loads this follows directly by expanding (2), and for all
loads follows by continuity of each coordinate evaluation. In particular,

\[
 a_k\left(\frac{v_k}{p_k}-\frac{v_{k+1}}{p_{k+1}}\right)=S_k.
\tag{11}
\]

The recovered solution has `v_i/p_i -> 0`: the tail in (10) is bounded by

\[
 \left(\sum_{k\ge i}\frac{|S_k|^2}{a_k}\right)^{1/2}
 \left(\sum_{k\ge i}\frac1{a_k}\right)^{1/2}\longrightarrow0.
\]

Thus this is an exact weighted Gauss law with the boundary condition
selected by the actual reference inverse.

## 5. Application to the full signed Gamma/prime correction

For every actual reflected current `h in K_N`, take the full and reference
potentials `u` and `u_0` with pole mean zero, put `v=u_0-u`, and define

\[
 q=(I-A)\mathcal U(\sqrt D\,v).
\]

This is the completed aggregate load from the signed-path report, so it
exists without assuming the individual Gamma or prime divergences are
ordinary functions. Define

\[
 Q_j(t)=\sqrt{D_j(t)}q_j(t),\qquad
 S_k(t)=\sum_{j=0}^kp_j(t)Q_j(t).
\]

The exact correction is therefore

\[
 \boxed{\quad
 \Gamma_R[h]-\Gamma_P[h]
 =G[u]+\int_0^{\log2}\sum_{k\ge0}
       \frac{|S_k(t)|^2}{c_k(t)p_k(t)p_{k+1}(t)}\,dt.
 \quad}
\tag{12}
\]

All Gamma/prime and prime/prime interactions occur in `Q` before taking
any square. For smooth ratios whose aggregate divergence is a function,
`Q_j(t)=Q_G[u](t+j log 2)`; the completed definition above is primary.

The same formula with the reflected load
`Q_j=2 psi(x_j) W_h(x_j)` gives `Gamma_R[h]` itself. Thus both sides of the
reference comparison can be computed with the same explicit cut-current
map, without a sign-invalid path-counting argument.

## 6. What remains, and why this is not a critical-sign proof

The coefficient-one target is still

\[
 G[u]+\int_0^{\log2}\sum_{k\ge0}\frac{|S_k(t)|^2}{a_k(t)}\,dt
 \ge\Gamma_R[h]-\|h\|_N^2
 \quad(h\perp S_N).
\tag{13}
\]

The transform provides the full left side as explicit nonnegative
squares, but (13) is a comparison with a generally positive reference
excess. Nonnegativity alone is insufficient. Using (7) alone recovers a
scalar spectral bound already available in the reference report and
therefore provides no new coefficient-one result.

Unlike a proposed local sum-of-squares representation of `P-N`, (12)
is not contradicted by the simultaneous neutral theta-jet identities: it factors a
positive **correction**, and its input is the global aggregate divergence
of the full potential, not a finite-stencil functional of the original
ratio.

## 7. A stable local recurrence for the global cut transform

The potentially large factors `p_j` need not be evaluated explicitly.
Define normalized pivots

\[
 \gamma_j=\frac{c_jp_{j+1}}{D_jp_j}.
\]

The left boundary and homogeneous recurrence give

\[
 \gamma_0=1,\qquad
 \gamma_{j+1}=1-\frac{\beta_j^2}{\gamma_j},\qquad
 0<\gamma_j\le1.
\tag{14}
\]

Moreover `gamma_j>=1-rho`, uniformly in the fiber and index: `gamma_j`
is the final diagonal Schur complement of the leading principal section
of `I-A_t`, whose lower bound is `(1-rho)I`. Let `B_t` be the lower
bidiagonal operator

\[
 (B_tz)_j=\sqrt{\gamma_j}\,z_j
             -\sqrt{1-\gamma_j}\,z_{j-1},\qquad z_{-1}=0.
\tag{15}
\]

Its rows have squared norm one, and
`sqrt(gamma_j(1-gamma_(j+1)))=beta_j`. Therefore

\[
 \boxed{I-A_t=B_tB_t^*,\qquad \mathcal C_t=B_t^{-1}.}
\tag{16}
\]

For completeness, `B_t` is bounded by its bidiagonal formula;
`B_tB_t^*>= (1-rho)I` makes it onto. The nonzero diagonal and its first
row imply recursively that its kernel is zero. Hence it is invertible.
Its inverse agrees with (5), because multiplying (5) by (15) telescopes
all prefix terms. Equivalently one may compute the transformed load by

\[
 z_0=q_0,\qquad
 z_j=\frac{q_j+\sqrt{1-\gamma_j}\,z_{j-1}}
            {\sqrt{\gamma_j}}.
\tag{17}
\]

All cancellations of signed loads take place in the numerator of (17).
The transformation is globally bounded even though it is computed by a
one-step recurrence. It is not an unsigned path sum or a diagonal norm
estimate.

For the reference solution `eta=(I-A_t)^(-1)q`,

\[
 z=B_t^*\eta,\qquad
 z_j=\sqrt{a_j}\left(\frac{v_j}{p_j}
                         -\frac{v_{j+1}}{p_{j+1}}\right),
 \quad v_j=\eta_j/\sqrt{D_j}.
\tag{18}
\]

Thus the explicit cut-current factorization is exactly a uniformly
invertible Cholesky transform on the whole normalized source space, not
only a formal identity for finite vectors. The direct-integral version
has the same uniform estimates. Equations (14)--(18) do not alter the
unproved comparison (13).
