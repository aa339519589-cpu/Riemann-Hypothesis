# Full-prime tail contraction and finite coalescing current paths

## Scope

The coherent operational flow constructed in
`COHERENT_OPERATIONAL_RAY_CURRENTS.md` has a genuine all-prime contraction
on its physical-state tail. Every fixed pair of its rays coalesces in finite
operational time almost surely, including starts at the origin entrance.
The same actual-source current differences consequently admit finite
pre-coalescence path-square representations. This does not establish a sign
for the original odd-source form: its full covariance and storage terms
remain exactly those of the cited coherent-current identity.

## 1. The source weight and the shared flow

Throughout,

    c(z)=8z^3-30z^2+15z,
    theta(z)=sum_(m>=1)c(m^2z)exp(-m^2z),
    z=pi exp(2x),   psi(x)=exp(x/2)theta(z).

Thus theta means the COMPLETE physical source weight theta_c, not the
Gaussian theta sum and not an individual polynomial summand. It is positive
for z>pi and has a simple zero at pi.

Write H for the positive operational generator; the Markov generator is -H:

    Hv(z)=int_(y>z) theta(y)/(2(y-z))[v(z)-v(y)]dy
       +sum_(n>=2)Lambda(n)theta(n^2z)[v(z)-v(n^2z)].       (1)

The coherent continuous arrows use intensity `ds theta(y)dy da/2`, and
state z accepts a destination y when y>z and a<1/(y-z). For each n, the
common prime field has intensity `Lambda(n) ds da`, with acceptance
`a<theta(n^2z)` and destination n^2z. These are exactly the full rates in (1).
All accepted n, including all prime powers, are retained.

For a pair of states let d(z,w)=|z-w| and let L^(2) be the Markov generator
of the coupled pair. The next two sections prove the pointwise tail estimate

    L^(2)d(z,w) <= -(1/8) int_(min(z,w))^(max(z,w)) theta(s)ds,
                                      z,w>=4.           (2)

This is contraction in the common OPERATIONAL clock. No corresponding
same-time Wasserstein contraction for the separate physical clocks is claimed.

## 2. Exact continuous drift and the full prime bound

Suppose 4<=z<w. Continuous arrows preserve the order. Their one-state drift
is `b_cont(z)=(1/2)int_z^infinity theta(y)dy`, so the pair-distance drift is
exactly

    L_cont^(2)d(z,w)=b_cont(w)-b_cont(z)
                  =-(1/2)int_z^w theta(s)ds.             (3)

For n>=2 and s>=4, theta(n^2s) is decreasing. Indeed every summand derivative
has the sign of

    c'(q)-c(q)=-8q^3+54q^2-75q+15<0, q>=16.

For example the first two terms are `-q^2(8q-54)`, already
negative on this range, and `-75q+15<0` as well.

Put rho(s)=theta(n^2s). The simultaneous prime jump occurs at rate
Lambda(n)rho(w), and multiplies the distance by n^2. The remaining lower-only
rate is Lambda(n)[rho(z)-rho(w)]. Its distance increase is
`|n^2z-w|-(w-z)`, which is at most (n^2-1)z regardless of whether it crosses
w. Consequently

    L_n^(2)d <= Lambda(n)(n^2-1)
                     [(w-z)rho(w)+z(rho(z)-rho(w))]
              <= Lambda(n)(n^2-1)
                     int_z^w [rho(s)-s rho'(s)]ds.       (4)

The second inequality uses the decrease of rho, and separately
`(w-z)rho(w)<=int_z^w rho(s)ds` and
`z(rho(z)-rho(w))<=int_z^w s[-rho'(s)]ds`.
This pays prime jumps that reverse the pair order; their effect is not omitted.

## 3. A rational certificate for the complete prime row

For s>=4,

    theta(s)>=c(s)exp(-s)>=(23/16)s^3 exp(-s),             (5)

because `c(s)/s^3=8-30/s+15/s^2` is increasing there and equals 23/16 at 4.
Every theta summand in (5) is positive in this range. For q>=16,

    c(q)-q c'(q)+q c(q)=8q^4-46q^3+45q^2 <=8q^4.         (6)

Therefore the complete row in (4), denoted A(s), obeys

    A(s)=sum_(n>=2)Lambda(n)(n^2-1)
                              [theta(n^2s)-n^2s theta'(n^2s)]
        <=8s^4 sum_(k>=2) k^8 exp(-k^2s)
                              sum_(n|k,n>=2)Lambda(n)(n^2-1).

Only a positive, absolutely convergent all-integer regrouping was used.
For every k>=2,

    sum_(n|k,n>=2)Lambda(n)(n^2-1)
      <=log(k) sum_(n|k)n^2
      <=2k^2 log(k)<=k^3.                                (7)

Here `sum_j>=1 j^-2<=2` follows by the integral test, and
`log k<=k/2` follows from its value and derivative at k=2. It follows that

    A(s)/theta(s)
      <=(128/23)s sum_(k>=2) k^11 exp(-(k^2-1)s)
      <=(512/23) sum_(k>=2) k^11 exp(-4(k^2-1)) <3/8.     (8)

The second inequality holds termwise because `s exp(-(k^2-1)s)` decreases
for s>=4. For a completely rational verification of the strict last bound,
the positive Taylor sum through degree seven gives e^4>50. Successive terms
of the series in (8) have ratio at most

    r=(3/2)^11/50^5 <1.

Its first term is less than 2^11/50^3, and direct rational arithmetic gives

    (512/23)(2^11/50^3)/(1-r) <3/8.

The accompanying checker proves this inequality without a floating-point
prime cutoff. Combining (3), (4), and (8) proves (2), with strict slack.

## 4. Compact entrance and an honest finite stopping time

No deterministic entry time into the tail is assumed. Consider the fixed
subset of the continuous Poisson arrows

    5<=y<=6,    0<a<1/(6-pi).

Its rate is the positive finite constant
`lambda_*=[2(6-pi)]^-1 int_5^6 theta(y)dy`. Any state in [pi,4] accepts every
such arrow and is sent above 4. A state already above 4 cannot decrease.
Therefore, if T is the first time both states lie in [4,infinity), then T
is a stopping time and is bounded by the first such Poisson-arrow time.
In particular T is finite almost surely and has finite mean. This argument
also works for an initial state pi; its genuine operational holding time is
retained, not silently replaced by zero physical time.

After T, (2), nonexplosion, and the bounded jump moments make the distance
a nonnegative supermartingale. Localization followed by Fatou suffices for
the supermartingale property. It has a finite almost-sure limit and is bounded
on the entire post-T path almost surely. No use is made of a last prime jump
as a stopping time. All subsequent prime events remain in (2).

## 5. Almost-sure coalescence, not merely distance contraction

For distinct states z<w the simultaneous continuous-arrow rate is

    lambda_coal(z,w)=(1/2)int_w^infinity theta(y)/(y-z)dy. (9)

An accepted such arrow sends both states to the same destination. Once equal,
pathwise uniqueness makes them stay equal under every continuous and prime
field.

For every finite R there is c_R>0 such that, when z,w>=4 and |z-w|<=R,

    lambda_coal(z,w)>=c_R theta(z),
    theta(min(z,w))>=c_R theta(z)                         (10)

after reducing c_R if necessary, where the z on the right in the first
inequality can be either member of the pair. To verify this, integrate (9)
over `max(z,w)+[1,2]`. The denominator is at most R+2, while the ratios
`theta(a+v)/theta(a)` are bounded below uniformly for a>=4 and
0<=v<=R+2. Positivity on compact sets and the exact asymptotic
`theta(a)=c(a)exp(-a)(1+O(poly(a)exp(-3a)))` prove this ratio bound.

Each marginal has infinite total physical clock

    int_0^infinity theta(Y_s)ds=infinity                 (11)

almost surely. This is the established nonexplosion/time-change theorem for
the original positive forward process; the entrance hold contributes zero
clock but is finite and is followed by an interior trajectory. Consequently,
on a path with bounded post-T gap and no coalescence, (9)-(11) force the
integrated coalescence rate to be infinite.

For rigor, stop additionally when the gap exceeds an integer R. The number
of simultaneous continuous arrows before that stop or before coalescence
is at most one. Its compensator therefore has expectation at most one,
by finite cutoffs followed by monotone convergence. It is finite almost
surely. This contradicts the preceding infinite-rate conclusion on the event
of no coalescence and no R exit. Almost every path has bounded post-T gap,
so taking the countable union over R proves

    tau_coal(z,w)<infinity almost surely                 (12)

for each fixed initial pair. Prime events may themselves cause equality;
that only stops the argument earlier. No finite mean coalescence time is
asserted. Pairwise almost-sure statements suffice for all the finite weighted
edge integrals by Fubini; no common exceptional set for all starts is needed.

## 6. Finite pre-coalescence current squares for the same actual source

Let u=r-c_infinity be the actual bounded H^s ratio, s>1/2, and
`v(z)=u(log(z/pi)/2)`. Its complete operational current is

    I_z=lim_(S->infinity) int_0^S Hv(Y_s^z)ds

in L2 and almost surely, with E I_z=v(z) and variance J(z). This includes
the origin holding current described in the coherent-current note. After
coalescence, the two trajectories and all their future current integrands
are identical. Therefore

    I_z-I_w=int_0^(tau_coal) [Hv(Y_s^z)-Hv(Y_s^w)]ds,      (13)

and the right-hand side is an L2 random variable. It is an ordinary finite
interval integral on each path: the trajectories remain in a finite state
band up to the finite stopping time, and the actual Holder regularity makes
Hv locally bounded. The individual infinite currents need not converge
absolutely; no such assertion is used to cancel their identical tails.

Thus the coherent edge energy is exactly the nonnegative path square

    E_coh(z,w)
      =E|int_0^(tau_coal)[Hv(Y_s^z)-Hv(Y_s^w)]ds|^2
      =[v(z)-v(w)]^2+J(z)+J(w)-2C(z,w).                  (14)

The stopped difference-martingale isometry also gives

    Var(I_z-I_w)
      =E int_0^(tau_coal) Gamma^(2)[v(z)-v(w)](Y_s^z,Y_s^w)ds.

For example, at z<w its continuous carre rate is the exact positive sum

    int_z^w theta(y)/(2(y-z))[v(y)-v(z)]^2dy
    +int_w^infinity (theta(y)/2)
             [1/(y-w)-1/(y-z)][v(y)-v(w)]^2dy
    +lambda_coal(z,w)[v(z)-v(w)]^2.                     (15)

The prime carre rate similarly consists of common-jump squared differences
at the minimum acceptance rate, plus each single-ray squared increment at
the residual acceptance rate. Every term is nonnegative, and its expected
time integral is finite by the two marginal current-energy bounds.

## 7. What this does and does not settle

The original reflected-prime and Gamma-wall edges can now be lifted to the
explicit finite pre-coalescence paths (13), with no independent infinity
endpoint or assumed finite resistance chain. This is an actual common-source,
all-prime construction. It also proves a strict quantitative tail coupling
inequality independently of the top-state extremal property.

It does NOT make the original signed edge coefficients positive. The exact
identity remains

    h[g]=P_coh-H_coh-N_coh+4int psi(K0-xpsi)J
                           +8C_P-2C_H-2C_N,
    K0=3Phi+Theta/2,

and its full supercritical Q_delta version has the coefficients stated in
the coherent-current note. In particular the signed local storage and the
specific prime-reflected covariance C_N have not disappeared. Wasserstein
contraction controls physical-state distances, not the whole original source
quadratic form on these arbitrary actual H^s ratios. K<=1 remains unproved.
