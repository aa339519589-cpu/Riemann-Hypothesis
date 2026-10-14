# Positive all-prime forward rays for the same actual ratio

This note gives a genuine stochastic realization of the original-psi future
jump generator and its plateau boundary. It does not replace the full original
Green form by the future generator or assert a favorable sign for the retained
past, reflection, Gamma-wall and pole terms.

## 1. Exact generator in the physical coordinate

Let z=pi exp(2x), and put

    c(z)=z(8z^2-30z+15),
    theta_c(z)=sum_(n>=1)c(n^2z)exp(-n^2z).

The exact identity psi(x)=exp(x/2)theta_c(z) gives theta_c(z)>0 for z>pi.
Although c itself has a small negative interval at the endpoint, the COMPLETE
theta_c is positive; no individual signed summand is used as a jump rate.

For x>0, the original-psi future positive generator is

    G_psi r(x)=int_0^infinity kappa(h)psi(x+h)/psi(x)
                                          [r(x)-r(x+h)]dh
       +sum_(n>=2)alpha_n psi(x+log n)/psi(x)
                                          [r(x)-r(x+log n)].       (1)

With F(z)=r(log(z/pi)/2), this is exactly

    G F(z)=int_0^infinity theta_c(z+v)/[2v theta_c(z)]
                                          [F(z)-F(z+v)]dv
       +sum_(n>=2)Lambda(n)theta_c(n^2z)/theta_c(z)
                                          [F(z)-F(n^2z)].         (2)

The continuous change of variables is v=z(exp(2h)-1). Its Jacobian, the factor
exp(h/2) in psi, and kappa(h) cancel to give precisely 1/(2v). Thus (2) includes
the complete Gamma kernel and every prime-power jump with its actual weight.

## 2. Nonexplosion and an explicit plateau approach

Fix any starting point z0>pi. On z>=z0, the function theta_c(z) is smooth,
strictly positive, and

    theta_c(z)=c(z)exp(-z)[1+O(poly(z)exp(-3z))].           (3)

There are finite constants, depending on z0, such that

    0<theta_c(z+v)/theta_c(z)<=C(1+v)^3exp(-v),
                                      z>=z0, v>=0.      (4)

The continuous jump kernel therefore has uniformly bounded first and second
moments. The prime jump moments are also uniformly bounded, because their
terms are polynomial multiples of exp(-(n^2-1)z). Moreover the total first and
second jump moments obey

    b(z)=1/2 int_0^infinity theta_c(z+v)/theta_c(z)dv
         +z sum_n Lambda(n)(n^2-1)theta_c(n^2z)/theta_c(z)
          -->1/2,
    q(z)=1/2 int_0^infinity v theta_c(z+v)/theta_c(z)dv
         +z^2 sum_n Lambda(n)(n^2-1)^2theta_c(n^2z)/theta_c(z)
          -->1/2.                                      (5)

Dominated convergence in (4) proves the continuous limits; the Gaussian prime
bounds prove the other terms tend to zero without using RH or a prime cutoff.

Construct the increasing pure-jump process Z_t with generator -G by thinning
a Poisson random measure with the dominating continuous Levy density
C(1+v)^3exp(-v)/(2v), together with the summable dominating prime clocks. The
small jumps have finite total variation because int_0^1 v dv/v is finite.
Local smoothness of the rates gives the standard successive bounded-jump
construction; its limit is obtained by letting the small-jump cutoff decrease.
For a fully explicit nonexplosion estimate, stop at the first crossing of R.
The first-moment bound gives E Z_(t stopped)<=z0+Bt, and hence the probability
of crossing R before fixed t is at most (z0+Bt)/R. Letting R increase proves
nonexplosion, including the multiplicative prime jumps.

There is a constant a>0 such that the continuous density in (2) is at least
a on v in [1,2], uniformly for z>=z0. This follows from compact continuity and
its strictly positive limiting density exp(-v)/(2v). Thus a fixed state-free
Poisson stream of jumps of size at least one can be included in the thinning
construction. Consequently Z_t tends to infinity almost surely.

Finally write

    Z_t=z0+int_0^t b(Z_s)ds+M_t,
    E|M_t|^2=E int_0^t q(Z_s)ds<=Qt.

The dyadic martingale maximal inequality and Borel-Cantelli give M_t/t->0
almost surely. Combining this with Z_t->infinity and (5) gives

    Z_t/t ->1/2,
    X_t:=log(Z_t/pi)/2
       =log t/2-log(2pi)/2+o(1) almost surely.           (6)

The full arithmetic future rays therefore reach the same infinity boundary;
they are not separate independently budgeted prime chains.

The state space is the open wing x>0, equivalently z>pi. Every stated
construction starts strictly inside it and remains above its initial point.
No entrance law at z=pi is asserted: theta_c(pi)=0, so the displayed rate
quotients do not define an endpoint generator. Infinity is approached only
as t tends to infinity, not by a finite-time explosion. This homogeneous
process is distinct from the positive normalized filter
A_t(psi r)/A_t(psi), whose changing denominator does not give a semigroup.

## 3. The same actual source and lawful plateau subtraction

For the actual scalar source, the proved ratio theorem is

    r=c_infinity+u,  u in H^s(0,infinity) for every s<1,
    c_infinity=U(g)/U(psi), U(f)=int_0^infinity exp(x/2)f(x)dx.

For s>1/2, u is bounded, uniformly Holder, and tends to zero. Thus the lawful
U=0 null gauge g-c_infinity psi is EXACTLY the plateau-subtracted source, not
an unrelated choice of constant. Along the process (6),

    r(X_t)->c_infinity,   u(X_t)->0                     (7)

almost surely and in every finite Lp of the path law.

For any Holder exponent 0<alpha<s-1/2, the jump integral of the absolute
increment of u is finite and bounded on z>=z0. Near infinity its continuous
part is O(z^(-alpha)), by (4) and log(1+v/z)<=v/z; the prime part is even smaller.
Consequently the finite-horizon compensated-jump formula applies to this
SAME u and gives exactly

    u(x)-E_x u(X_t)=E_x int_0^t G_psi u(X_s)ds.           (8)

Taking the limit using (7) gives a signed improper potential representation.
It does NOT, by itself, prove absolute convergence of the infinite time
integral or permit termwise substitution of the separately large polar,
reflected and past terms of the actual source equation.

## 4. Positive discounted resolvents and retained current identity

For lambda>0 let

    R_lambda F(x)=E_x int_0^infinity exp(-lambda t)F(X_t)dt.

This is a positive kernel, and bounded data have an absolutely convergent
resolvent. The exact identities on the actual u are

    u-lambda R_lambda u=R_lambda G_psi u,
    Gamma_psi[u]=2u G_psi u-G_psi(u^2),
    R_lambda Gamma_psi[u]
       =2R_lambda(u G_psi u)-u^2+lambda R_lambda(u^2)>=0. (9)

Here Gamma_psi is the sum of continuous and complete-prime squared jump
increments, with exactly the rates in (1). Formula (7) and dominated Abel
convergence give lambda R_lambda u->0 and lambda R_lambda(u^2)->0. Thus (9)
keeps a genuine positive full forward-current quantity at every lambda.
The occupation argument below proves its zero-discount limit finite for the
same actual u. This requires the physical-coordinate block estimate; a bare
pointwise Holder estimate would not suffice.

The original source operator has

    D(psi r)=psi G_psi r-(3Phi+Theta/2)r,
    T_odd=D+D_half*+2X+H_kappa+F_r.

Therefore the full Green comparison still contains the half-line adjoint,
odd Gamma wall, reflected prime kernel and the exact polar rank-one term.
Neither positivity of R_lambda nor the common plateau in (7) pays those terms
automatically. They remain the explicit target for a joint signed factorization.


## 5. Finite all-prime current occupation for the actual source

Fix x0>0, z0=pi exp(2x0), and 1/2<s<1. There is a finite constant
C_(x0,s), independent of u, such that

    J_x0[u]:=E_x0 int_0^infinity Gamma_psi[u](X_t)dt
                   <=C_(x0,s)||u||_(H^s(0,infinity))^2.       (10)

The statement uses the ORIGINAL log-coordinate Sobolev norm and the SAME
homogeneous process (2). It is not a claim that the transformed F is in an
unweighted Sobolev space in physical z.

### 5.1 Uniform occupation of physical unit blocks

Put a_k=z0+k and I_k=[a_k,a_k+1), k>=0. The process is increasing, so it
visits each block at most once, possibly skipping it. Upon entering a block,
the next jump of the state-free stream from Section 2 has size at least one
and therefore exits it. Its waiting time has mean 1/a, by the strong Markov
property of that Poisson stream. Hence

    E_z0 int_0^infinity 1_(I_k)(Z_t)dt <=1/a,
    E_z0 int_0^infinity H(Z_t)dt
          <=a^(-1) sum_(k>=0) sup_(z in I_k) H(z)             (11)

for any nonnegative H. Endpoint visits cause no problem: the holding-time
argument applies to the half-open block actually containing the state.

### 5.2 Local Sobolev control at the correct shrinking log scale

For any interval J and x,y in J, fractional Morrey gives

    |u(x)-u(y)|^2 <=C_s |x-y|^(2s-1) [u]_(dot H^s(J))^2.    (12)

Here the seminorm is the double integral of
|u(a)-u(b)|^2/|a-b|^(1+2s) over J times J. To see that the constant is
independent of J, subtract the mean, apply the fractional Poincare inequality
on a unit interval, extend by reflection with a fixed cutoff, and use the
Fourier Cauchy-Schwarz bound
int |exp(i xi h)-1|^2 |xi|^(-2s) dxi=C_s |h|^(2s-1).
Rescaling cancels the interval length exactly in (12).

Write F(z)=u(log(z/pi)/2). For z in I_k and 0<v<1, the two log arguments
belong to

    J_(k,0)=[log(a_k/pi)/2, log((a_k+2)/pi)/2]

and are separated by at most v/(2a_k). Consequently (4) and (12) give

    sup_(z in I_k) int_0^1 theta_c(z+v)/(2v theta_c(z))
                                     |F(z+v)-F(z)|^2 dv
       <=C_s a_k^(1-2s) [u]_(dot H^s(J_(k,0)))^2
                                      int_0^1 v^(2s-2)dv.     (13)

The last integral is finite precisely when s>1/2. The intervals J_(k,0)
have overlap at most three, because their images in physical z have length
two and consecutive left endpoints differ by one. In particular the sum of
their local squared seminorms is at most three times the global squared
seminorm; this follows directly by counting the double-integral indicators.
Also a_k^(1-2s)<=z0^(1-2s). Summing (13) over k is therefore finite.

For m>=1 and m<=v<m+1, use instead

    J_(k,m)=[log(a_k/pi)/2, log((a_k+m+2)/pi)/2].

The separation is at most (m+1)/(2a_k), and the kernel in (4) is bounded by
C exp(-m)(m+2)^3/m. Thus the corresponding block supremum is at most

    C_s exp(-m)(m+2)^(2s+1) a_k^(1-2s)
                                      [u]_(dot H^s(J_(k,m)))^2. (14)

The J_(k,m) overlap at most m+3 times. Sum first in k and then in m;
the exponential factor in (14) pays this additional polynomial factor.
This proves summability of all continuous squared-jump block suprema.

### 5.3 Every prime-power jump, with no cutoff interchange

The theta-polynomial estimates used in Section 2 give uniformly on z>=z0

    theta_c(n^2z)/theta_c(z)
                  <=C_(z0) n^6 exp(-(n^2-1)z), n>=2.

Hence the prime contribution satisfies

    sum_k sup_(z in I_k) sum_(n>=2) Lambda(n)
          theta_c(n^2z)/theta_c(z)|F(n^2z)-F(z)|^2
      <=4C_(z0)||u||_infinity^2
          sum_(n>=2) Lambda(n)n^6 exp(-(n^2-1)z0)
                                      /[1-exp(-(n^2-1))]<infinity. (15)

All summands are nonnegative, so Tonelli is legitimate. The elementary
bound Lambda(n)<=log n suffices, and Sobolev embedding bounds the infinity
norm by ||u||_(H^s). Combining (11), (13)-(15) proves (10).

## 6. Honest zero-discount signed current, with its exact variance

The compensated-jump martingale for the same actual u is

    M_t^u=u(X_t)-u(x0)+int_0^t G_psi u(X_v)dv.

Its predictable quadratic variation has expectation

    E|M_t^u|^2=E int_0^t Gamma_psi[u](X_v)dv<=J_x0[u].

Thus M_t^u converges almost surely and in L2 to M_infinity^u. Since
u(X_t)->0 both almost surely and in L2, the COMPLETE signed future current
has the ordinary limit

    int_0^t G_psi u(X_v)dv -> I_u:=u(x0)+M_infinity^u
                                    almost surely and in L2,
    E I_u=u(x0),       Var(I_u)=J_x0[u].                  (16)

This is stronger than a merely formal Abel potential. It does not say that
int_0^infinity |G_psi u(X_v)|dv is finite, or license splitting G_psi u
into separately nonintegrable pieces of the source equation.

The squared-source Dynkin identity additionally gives

    2 E int_0^t u(X_v)G_psi u(X_v)dv
       =E int_0^t Gamma_psi[u](X_v)dv+u(x0)^2-Eu(X_t)^2,
    lim_(t->infinity) E int_0^t u(X_v)G_psi u(X_v)dv
       =[J_x0[u]+u(x0)^2]/2.                            (17)

The limit in (17) is a limit of the complete mixed expression, not an
absolute-integrability assertion. Monotone convergence also yields
R_lambda Gamma_psi[u]->J_x0[u] as lambda decreases to zero. All pole,
reflection and half-line adjoint corrections to the original form still
remain to be represented and signed; (10)-(17) alone do not prove h>=0.

## 7. A uniform starting-point estimate for complete-form integration

The constant in (10) can be controlled at the origin without starting a
process there. In fact

    J_x[u]<=C_s(1+1/x)||u||_(H^s(0,infinity))^2, x>0.       (18)

To prove it, use the global two-sided comparison

    c_1(z-pi)(1+z)^2 exp(-z)<=theta_c(z)
                        <=c_2(z-pi)(1+z)^2 exp(-z), z>pi. (19)

The quotient is positive and continuous on every compact interior interval.
At pi it has a strictly positive limit, because psi'(0)>0 and
z-pi=2pi x+O(x^2); at infinity its limit is 8 by the polynomial asymptotic.
This proves (19) with fixed positive constants.

The continuous ratio is consequently bounded above by
C(1+1/(z-pi))(1+v)^3 exp(-v), while it is bounded below by c exp(-v)
on v in [1,2]. Thus the state-free stream rate a in (11) can be chosen
independently of the starting point. Similarly,

    theta_c(n^2z)/theta_c(z)
        <=C n^6(1+1/(z-pi))exp(-(n^2-1)z).

Repeat the proof of Section 5 with these constants. The additional factor
is at most 1+1/(z0-pi) along the whole ray, and
z0^(1-2s)<=pi^(1-2s). Finally z0-pi>=2pi x0, proving (18).
More precisely the same argument gives

    J_x[u]<=C_s(1+1/(z-pi)){
          z^(1-2s)[u]_(dot H^s(x,infinity))^2
                         +exp(-3z)||u||_infinity^2}.       (20)

This estimate is only an upper bound for finite occupation. It does not
assert a process entrance law at x=0 or identify any positive invariant
measure for the increasing process.


## Dependencies and normalization

The fixed-depth hypothesis used in Sections 3--7 is the published
[actual ratio and plateau theorem](../20261014_actual_ratio_multipliers/REPORT.md).
The original odd source and full-prime conventions are those of the
[canonical source transfer](../20261013_canonical_gamma_activity/FINITE_SOURCE_TRANSFER.md).
The exact future identities for D, including Dpsi=-(3Phi+Theta/2), are derived
without an additional external hypothesis in the [current-form appendix](CURRENT_FORM.md).
No positive entrance law at the excluded point x=0 is needed in this report.
