# Complete main-seed mixed-force endpoint for A=16, k=3

This certifies the endpoint of the FULL original head mixed density for
MAIN phi. It does not replace phi by Cphi. The complete future-prefix
error is paid separately in the augmented source certificate. No original
Schur sign follows from the endpoint alone.

Use the stable source and notation of
[FILTERED_K3_COMPLETE_PRIME_POLE_DEBIT.md](FILTERED_K3_COMPLETE_PRIME_POLE_DEBIT.md):

    b=log2, z=pi exp(2y), A=16, k=3,
    phi(y)=2z c(z)exp(-z)u(z)/W(y),
    F(z)=phi(y)/(2z)=c(z)exp(-z)u(z)/W(y).

Thus phi(y)dy=F(z)dz. Write L_phi(x) for the complete head mixed density
of the odd source supported above b. At the right endpoint,

    L_phi(b)=-2 integral [kappa(y-b)-kappa(y+b)]phi(y)dy
       +2 sum_n alpha_n[phi(log n-b)-phi(log n+b)]
       -8 sinh(b/2)ell(phi), alpha_n=Lambda(n)/sqrt(n). (1)

The Gamma integral is absolutely convergent: phi is supported in
z>=16>4pi, a positive distance from the head boundary. Every prime power
and the full pole in (1) are retained.

## 1. An exact rational-power Gamma kernel, without a Gamma-index cutoff

The Gamma difference in (1) is exactly

    K(z)=z^(3/4)[(4pi)^(1/4)/(z-4pi)
                            -(pi/4)^(1/4)/(z-pi/4)]. (2)

Consequently its endpoint contribution is -2 integral_16^infinity F(z)K(z)dz.
This identity sums the entire exponential Gamma ladder. There is no
remaining truncation in its ladder index.

The validated source cells supply, around their exact midpoint z0 with
exact half-width h, a degree24 polynomial P_F and a uniform remainder r_F:

    |F(z0+w)-P_F(w)|<=r_F, |w|<=h.

The stored outward midpoint/width intervals enclose those exact numbers;
the underlying exact cells partition [16+10^(-5),128], including all W
branches. The main1059 cells and extra54 onset cells are both used.

For a pole p equal to4pi or pi/4, the Taylor coefficients Y_j of
(z0+w)^(3/4)/(z0+w-p) are evaluated by the exact recurrence

    P_0=z0^(3/4), P_j=P_(j-1)(3/4-j+1)/(j z0),
    Y_0=P_0/(z0-p), Y_j=(P_j-Y_(j-1))/(z0-p).         (3)

Combining the two rows in (3) gives the degree32 Taylor polynomial P_K
of (2), with every coefficient enclosed by interval arithmetic.
The unit complex disc around every midpoint stays above both poles.
A Cauchy bound on that disc is

    M_K=(z0+1)^(3/4)[(4pi)^(1/4)/(z0-4pi-1)
                         +(pi/4)^(1/4)/(z0-pi/4-1)],
    |K-P_K|<=M_K h^33/(1-h).                         (4)

The right sides use the full outward interval for z0 and h, taking an
upper endpoint. All h<.117. Hence the integral of P_F P_K is computed
exactly as a finite polynomial integral with interval coefficients, and
its full absolute error is bounded by

    2h[r_F M_K + (sum_(j=0)^24 |F_j|h^j) M_K h^33/(1-h)]. (5)

This retains the source remainder multiplied by the complete K, not only
by a truncated kernel. Directed sequential summation encloses all cells.

## 2. The missing onset and far Gamma wing

On 0<=s=z-16<=.001, the elementary Bessel Poisson integral gives
|g(s)|<=s^(9/4)/Gamma(13/4), while the stable convolution measure has
variation at most1+sqrt6<7/2. Also
Gamma(13/4)=(45/64)Gamma(1/4)>(45/64)integral_0^1(1-v)v^(-3/4)dv=9/4>1. Therefore
|u(16+s)|<=(7/2)s^(9/4).

The n=2 term of the positive W row gives
W>=exp(y/2)c(z/4)exp(-z/4)/2. On this interval,
c(z)<31000, c(z/4)>=92, and exp(y/2)>1. Using exp(3)>20 yields

    |F(16+s)|<s^(9/4)/50.                            (6)

Indeed 2*31000*(7/2)/(92*20^4)<1/50. Here c increases on[4,17].
For y>=x_A=(1/2)log(16/pi), one has 0<K<=kappa(y-b)<5, because
pi<16/5. Thus the omitted onset 0<s<10^(-5) contributes in absolute value
less than

    (1/5)(10^(-5))^(13/4)/(13/4)<3.461*10^(-18).      (7)

The complete global real estimate in the prime/pole debit note gives
|F(z)|<=70z exp(-3z/4) for z>=48. The omitted Gamma wing z>=128 is at most

    700 exp(-96)[128/(3/4)+1/(3/4)^2]
                                     <2.452*10^(-37). (8)

Combining (2)-(8) gives the COMPLETE Gamma endpoint interval

    [-1.3036028749424737*10^(-8),
     -1.3036028696319868*10^(-8)].                    (9)

## 3. Exact finite prime endpoint values and both complete prime tails

At reflection label n the required argument is z=pi n^2/4. Its first
nonzero prime-power endpoint is n=5; this differs from the first
pure-phi reflected QUADRATIC overlap, which is n=7. Below n=13 the
nonzero reflected labels are precisely5,7,8,9,11.
At forward label n the argument is z=4pi n^2; labels2,3 lie below128.

Each of these seven point values is directly enclosed using the validated
stable u series/ODE and the complete W row, rather than a midpoint source
sample. The interval evaluator for W keeps its full theta remainder.
At an integer W knot its additional row equals psi(0)=0, so the chosen
closed-side value is the actual continuous W value.

For every omitted reflected integer n>=13, use |phi(z)|<=140z^2exp(-3z/4),
3<pi<4, and alpha_n<=n. The complete absolute reflected tail is at most

    280 sum_(n>=13)n^5 exp(-9n^2/16)
      <=280*13^5 exp(-9*13^2/16)/(1-q_r),
    q_r=(14/13)^5 exp[-9(2*13+1)/16],
                                     <5.393*10^(-34). (10)

Similarly the complete forward tail n>=4 is at most

    71680 sum_(n>=4)n^5 exp(-9n^2)
      <=71680*4^5 exp(-9*4^2)/(1-q_f),
    q_f=(5/4)^5 exp[-9(2*4+1)],
                                     <2.125*10^(-55). (11)

The displayed consecutive-ratio bounds decrease thereafter. Bounding all
integers enlarges the absolute sum and omits no prime powers.
The resulting complete prime endpoint interval is

    [5.100682608095165*10^(-5),
     5.100682608095166*10^(-5)].                      (12)

## 4. Full same-source pole and certified total

The independently replayed complete main-seed pole interval is

    ell(phi) in [1.2552581056326414*10^(-10),
                 1.2572581244325613*10^(-10)].

Multiplying by the exact negative coefficient -8sinh(b/2) gives

    [-3.5560629819525774*10^(-10),
     -3.5504060745288805*10^(-10)].                   (13)

Equations (9), (12), and (13), including every tail bound, yield

    L_phi(b) in [5.099343444590403*10^(-5),
                5.099343501164789*10^(-5)].          (14)

For use with exact decimal/rational interval consumers one may safely
widen this to

    0.00005099343444 < L_phi(b) < 0.00005099343502.   (15)

The output is MAIN phi's endpoint. It does not include the Cphi-phi
mixed-force error, a trace-neutral change, or a head inverse. Those must
be added in the same-source augmented certificate rather than silently
identified with (14).

## Reproducibility

Run `certify_filtered_main_force_endpoint.py --out filtered_main_force_endpoint.json`.
The script records hashes of the exact cell, pole, interval-arithmetic,
and stable-series inputs in its output. Polynomial operations use directed
binary64 intervals; the scalar analytic coefficients and tails use
90-digit interval arithmetic, with explicit outward binary conversion.
It does not infer a sign from midpoint values or finite-prime samples.
