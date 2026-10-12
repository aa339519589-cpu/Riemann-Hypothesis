# An exclusive s-unit prime marker for the half-damped observation

Status: independently reviewed and frozen. This defines a new finite arithmetic observation. Its principal factor, local dynamic errors and complete cubic positive-proof transfer below have passed independent source review. It is not asserted to be the original two-term probe or to bound the full nonprincipal sum.

The complete half-damped observation, local notation and two different original/core marker polynomials are fixed in [HALF_DAMPED_PROBE.md](HALF_DAMPED_PROBE.md). The source local table is the pinned [September-30 QRH source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex). For the low-side proof below, the exact all-n cubic organization is [QUADRATIC_DUAL_N1.md, Part VI](QUADRATIC_DUAL_N1.md#part-vi-the-complete-cubic-good-core-sector-with-all-physical-indices), its marked all-scale proof is Part XVI, and the final existential improvement is Part XXX. Their finite-order reciprocal-L hypothesis Q and original radial/common-weight quantifiers remain in force; the user-supplied formal input is documented in [FORMAL_INPUT_Q.md](FORMAL_INPUT_Q.md), without any independent build claim here.

## 1. Exact finite physical operation

Fix the original target eta=1 throughout; all six original frequency units epsilon remain included. Start with the half-damped physical row (extra q_n^(-1/2)). For each of the original disjoint prime slots, replace the marked condition p|cn by

 p|cn AND p does not divide the ORIGINAL physical s.

For the core variant replace p|c n0 by p|c n0 AND p does not divide s, where n=n0 r_phys^2. Keep the original unmarked rescaled negative term, its coefficient and all three scale changes exactly as before. Marked terms still use Z->ZP; unmarked rescaled terms still use the original X/P,Y/P shift and coefficient. Multiple slots impose these finite tests together. This remains a finite signed combination of independently defined physical sums, with the same sharp inverse, fixed bad data, windows and additive convention.

Here s in the divisibility test is the physical column label; the high-contour variable below is named x. No high Fourier frequency has been substituted for physical s in this test.

## 2. Complete local marked table

Use the half-damped source notation R',V,W,D and j=v_p(u) from [HALF_DAMPED_PROBE.md, §2](HALF_DAMPED_PROBE.md). Put t=e0+3l. The exclusive marked sum is exactly the positive-index table with k=v_p(s)=0. Thus

 Pstar_ex=(1-R')^(-1){R'(1-P^(-1))/(1-V)-1_(j=0)D
             +1_(j=2)a_p rho^(-3)P^(1-3x)
             +1_(j=3)b_p^2 rho^(-4)P^(3/2-4x)
             -1_(j=5)a_p^2 P^(2-6x)}.                 (1)

The full unmarked P is UNCHANGED. Consequently the exact holomorphic replacement at a selected prime is

 G_ex=(1-V)(1-W)[P^x Pstar_ex-P^(-w)P]/(1-D).          (2)

The overall slot factor is the same P^(z-1). Formula (2), not the old simplified G expression with a renamed Pstar, retains the correct unmarked complement.

For the core variant remove from (1) the first even family

 F_ex,first=[R'(1-P^(-1))/(1-V)
                          -1_(j=5)a_p^2P^(2-6x)]/(1-R'),

and put G_ex,core=G_ex-P^x(1-V)(1-W)F_ex,first/(1-D). All finite masks and local zero cases follow from this literal restriction of the original table.

At u=1,w=1,z=1/6, write d=P^(-x), r=kappa(p)P^(2-6x), v=P^(-1) and N=1-(1-v)d-vr. Then

 Pstar_ex=(r-d)/(1-r),
 B_ex=P^x Pstar_ex/P-v=((1-v)/(1+v))(r/d-1)/N-v.

For the core marker Pstar_ex,core=-d/(1-r), so

 B_ex,core=-((1-v)/(1+v))/N-v.                         (3)

Both are -1+O_delta(P^(-min(1,1/2+delta))) on Re x>=1/2+delta, uniformly in height. The same full unmarked principal H_half=L^S(6x-2,kappa)E_half/zeta_K^S(2) remains in the residue. The original positive slot sums S_i(Z), A_T(Z) and their prime-ray normalization are unchanged. Thus each of these new selected principal factors is nonzero throughout every fixed closed Re x>=1/2+delta for sufficiently large Z, exactly as in the reviewed half-damped principal argument.

## 3. Dynamic errors at z=1/6+e

Fix delta,delta_w>0 and a in [1/2+delta,1-delta_w]. Fix positive e<min(10^(-3),delta_w/12) before application, and take

 x_r=a+16e, w_r=1-a-6e, z_r=1/6+e.                  (4)

The actual H factors are the reviewed half-damped ones. Their uniform defect bounds imply |H_p-1|<1/2 at all sufficiently large selected primes; the threshold may depend on e and the fixed margins. The bad set S need not be changed. Define B_ex=G_ex/H only on these selected primes in this safe dynamic region, and keep the original main slot -sum W_i P^(z-1)bar chi_p(u).

At an unramified prime let E_ex=Pstar_ex+D and F_rem=Pstar_full-Pstar_ex. Directly from (1),

 E_ex=R'[(1-P^(-1))/(1-V)-D]/(1-R'),
 F_rem=[-(P-1)P^(-x-w)V/(1-V)+W R']/(1-R').          (5)

The same algebra as in the original normalized cancellation, now keeping the full unmarked complement, gives

 G_ex+bar chi_p(u)H
 =[(1-V)(1-W)/(1-D)]{
 (bar chi_p(u)-P^(-w))[V/(1-V)-D]
 +(P^x+bar chi_p(u)-P^(-w))E_ex
 +(bar chi_p(u)-P^(-w))F_rem}.                        (6)

In particular the strict second-family F_rem is NOT multiplied by P^x. On (4), the sufficient exponents are

 -a-16e, -1-6e, 2-5a-86e, -1-16e,

and smaller terms. They are all at most -1/2, uniformly in the fixed a interval. Thus the unramified slot error is O(P_i^(z_r-1/2+epsilon)).

At a ramified prime only the four terms in (1) remain. After multiplying by P^(z-1+x) and separating P^z, their exponents are bounded by

 common R': 1-5a-86e;
 j=2: -2a-32e;
 j=3: 1/2-3a-48e;
 j=5: 1-5a-80e.

The explicit rescaled complement has normalized size O(P^(-1-w_r)|H_p|). Each is below -1/2. There is now NO strict (e0,l,k,m)=(1,0,1,0) selected term, since k=1 is forbidden. The core difference has only the common R' and j=5 bounds already listed. All ramified slots are therefore paid by their divisor-many labels without the old strict-label conductor allocation.

Assume exactly the original retained-row bound |L(1-w,bar psi_u^*)|<<U^epsilon for the actual primitive nonprincipal numerator, at retained heights, with U~Nu. One use of its ordinary primitive functional equation, with its genuine deleted-factor cost, gives for either marker and every subset I of error slots

 |L^S(w,chi_u) product_(i in I)D_i,ex|
 <<U^(a-1/2+O(e)+epsilon)(3+T1)^C
                      product_(i in I)P_i^(z_r-1/2+epsilon). (7)

The stated reflected-value hypothesis and all selected heights are retained. Equation (7) does not estimate the original main-slot correlations over E_b. The improvement over the original two-term marker is the allowed line (4); the old marker has a true local -P^(a-1) error there.

## 4. The actual complete cubic low transfer: fixed allocations

Use precisely the reviewed nonflat complete cubic physical organization, now with half-damping already included. Keep the same fixed square layer r_phys, n0=F2 E4, shared divisor g, common coprimality divisor e0, fixed ordinary-mask divisor f, common reciprocal c2 column and common smooth s2 column. Here e0 denotes that ideal and is unrelated to the small real contour buffer e in (4).

For the original marker, the priority is r_phys,n0,g,e0,c2; for the core marker omit r_phys. The new s-unit test has the following exact consequences before any analytic estimate:

- A slot assigned to g or e0 is zero, since that prime already divides physical s.
- A slot assigned to n0's E4 branch is zero. A slot assigned to F2 has s-valuation zero already, by the original odd local table.
- A slot assigned to r_phys is a fixed-prime condition at that fixed square layer. First kill its branches with p dividing E4 g j e0, since these fixed factors already divide physical s. For the remaining fixed selected primes, let R0 be their squarefree product, so R0 divides rad(r_phys). Impose their s-unit condition before expanding the ordinary t-column mask: replace rad(k a') by rad(k a' R0), then expand once over f dividing this union. Do not duplicate a prime already in the old mask. The new mu(f)psi_w(f) is still a fixed-f row factor; if (f,w)>1 its original character value is zero. In particular the new R0 or f does NOT automatically add a hole to c2, which may share these primes. Its true scales are L=U_l/(N^3 B G q_e0), S=Y'/(B G q_j^2 q_e0 q_f). Thus the full-e0 estimate has exactly the outside factors q_f^(Re v-1) q_j^(2Re v-2), both nonpositive since the actual reciprocal contour is fixed below 1. The number of new f choices is divisor-small in k a' r_phys. The old physical r power q_r^(4-6b-3J(b)), with the further half-damping q_r^(-1), remains strictly summable and absorbs this divisor-small cost. These are the actual (17)--(19) scales in Part VI and (3),(14),(17) in Part XVI of [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md), rather than a comparison of entire signed sums.
- For a slot assigned to c2, priority and the original c2 masks already make its prime coprime to n0,g,e0,a' and to the square-layer mask h (hence j,k and the actual f|rad(k a')). In the original-marker priority it is also coprime to r_phys. In the core priority it may divide r_phys; that allowed branch is retained. Its original c2 mask still gives p not dividing h, hence p not dividing j,k. It still does not divide the fixed physical-s factors just listed. Its new condition is therefore exactly p not dividing the free s2 column.

The last case is the only additional coupling requiring a proof. It cannot be discarded by merely saying a coefficient got smaller. The next section supplies its full-scale estimate.

## 5. The c2-slot holes and the full e0 sum

On the true reciprocal contour Re v=b+buffer>1/2, the exact marked reciprocal multiplier is

 product_(p selected in c2)
          [-bar psi_w(p)P^(-v)/(1-bar psi_w(p)P^(-v))]. (8)

All original zeros and the fixed common holes remain. For a squarefree product D of these actual selected primes, the additional s2-unit mask has the finite identity

 B_w(S;D)=sum_(d|D)mu(d)psi_w(d) B_w(S/Nd),            (9)

with the correct common rotation and norm test after s2=d t. This identity is applied to compact physical columns before any estimate. Its common rotations have the same uniformly controlled seminorms. If a selected prime is a genuine character nonunit, the branch is already zero.

Fix a subset J of the c2 slots used in d. Multiplying (8) by mu(d)psi_w(d) cancels the Gauss-free cubic numerator phase at precisely those primes. The contribution at p in J is

 P^(-v)/(1-bar psi_w(p)P^(-v)),                       (10)

with the actual unit zero mask still imposed. This bounded rational row factor must be retained; it is not replaced by a new independent character. Freeze these selected primes first. The remaining selected slots have exactly the old rational multipliers and their old positive moment bounds, even with these additional bounded row factors and holes. For high M their product scale is no larger than the old P_c<=C sqrt(M). For the old small-M treatment one may keep the old pointwise slot loss; discarding slots from its positive product only decreases that loss.

Absolute summation of the frozen primes in J costs at most

 product_(i in J) P_i^(1-Re v+epsilon).                (11)

Now perform the ENTIRE genuine finite e0 sum, with its original support, before using the all-scale estimate. In the reviewed proof L/S=C_*/Y_* is constant at the fixed outer data and joint norm mode. Its inverse-column factor is

 L^(Re v-1)=(C_*/Y_*)^(Re v-1) S^(Re v-1).

In the present branch the smooth column has scale S'=S/Nd. Therefore

 S^(Re v-1)=(Nd)^(Re v-1)(S')^(Re v-1).              (12)

The factor in (12) exactly cancels (11), up to the usual small powers, since Nd is comparable to product_(i in J)P_i on the actual fixed compact slot ratios. This is at the actual contour exponent Re v, not a cancellation of mismatched buffered exponents.

The positive dyadic e0 integral is in dS/S=dS'/S'. Its true finite support is retained first and can then be enlarged in the positive bound. The existing pointwise/eighth-moment minimum for B_w(S'), together with its genuine long-S' Poisson tail, supplies exactly the old M^J(b) all-scale envelope. No convenient single S' block replaces that full integral. The inverse denominator holes in (10) are uniformly bounded on the fixed positive contour and cost only the old divisor-small ambient factor. All fixed J choices are finite because the number of slots is fixed.

Thus the full c2-slot sum obeys the same all-e0 bound as in the reviewed marked dual proof. The other allocations in Section 4 obey its same or smaller positive envelopes. The n0/r half-damping factors and every already reviewed square/sixth-power tail remain unchanged. It follows that, for either exclusive marker, the complete nonflat cubic contribution retains the reviewed bound

 I_cubic,exclusive(Z)<<Z^(-271/32256-c+epsilon), c>0,  (13)

with the same conditional finite-order Q uses, actual selected E_b, sharp inverse and existential c as before. This proof does not assert pointwise domination between signed whole observations. It uses the exact additional mask (9) and the all-scale cancellation (11)--(12).

## Limits

The high and low statements above use the same new physical operation in Section 1. The existing n=1 sector is modified by this new prime mask, but no stronger low exponent is claimed. Principal visibility remains unconditional; (7) retains the source's reflected-value condition; (13) retains its existing Q dependence. Other core sectors, full nonprincipal high comparisons and any first-flat operation are not claimed here. The statements in this scope have passed independent source review; no full nonprincipal high estimate is included.


### The unchanged extreme row range in the original geometric exponent

Write X=Z^lx, Y=Z^ly, the product of slot norms as Z^ell, and h=1−lx+ell; the original final geometric choice has h=13/16. Let the dyadic good sixth-free row norm be U=Z^d. The pinned source equation `eq:stage-high-exponent` has, for fixed admissible row/prime data R,g and fixed a,sigma, the dependence

    E_sigma(d;R,g;z0)=a−sigma+h(z0−1/6)−a ly−ell/2+g
                         +d(R+a−1/2−z0).

Consequently, if those same row and prime bounds R,g are available, changing only the dynamic line gives the exact identity

    E_new−E_old=(h−d)(z_new−z_old).

Lowering z0 from 17/50 to 1/6+e improves this part of the exponent for d<h, but gives zero improvement at d=h. This is a bookkeeping identity under unchanged input bounds, not a proof that all required R,g estimates hold for the new observation. In particular the same-E_b signed main-slot correlation remains unbounded here, and the local error improvement alone does not close the full high comparison.
