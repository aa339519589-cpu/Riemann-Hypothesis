# Positive all-prime future intertwining and the exact eta defect

This note proves an all-prime positive **one-sided** generator intertwining.
It also computes its exact eta/Phi derivative-ladder defect and carré identity.
It does not prove positivity of the original two-sided odd source form, does
not dispose of its reflected terms or pole, and does not construct a pairwise
Gamma coupling coherent under simultaneous divisibility conditioning.

## 1. Definitions and an absolute Gamma row

On x>=0 write z=pi exp(2x) and define

    kappa(h)=exp(-h/2)/(1-exp(-2h)),
    (L_+ f)(x)=int_0^infinity kappa(h)[f(x)-f(x+h)]dh,
    B(x)=exp(x/2)exp[-pi exp(2x)],
    (Cf)(x)=sum_(n>=1)n^(-1/2)f(x+log n),
    (F_+f)(x)=sum_(n>=2)Lambda(n)n^(-1/2)f(x+log n),
    Theta=CB,   Xf(x)=xf(x),
    C0=log pi-digamma(1/4).

Only positive half-line future shifts occur. Our initial common domain consists
of B times a smooth function whose derivatives have at most polynomial growth
in exp(2x), and their C-images. Compactly supported smooth multipliers suffice
for every intertwining assertion. On this domain the source and its first
several derivatives have Gaussian theta tails. All displayed future series,
including logarithmic label weights, converge absolutely locally uniformly;
the local first derivatives control the integrals at h=0.

The exact absolute row is

    (L_+B)(x)/B(x) = x+C0/2.                            (1)

Indeed, with u=exp(2h)-1,

    kappa(h)dh = (1+u)^(-1/4)du/(2u),
    kappa(h)B(x+h)/B(x)dh = exp(-zu)du/(2u).

If S has the Gamma(1/4,1) probability density, then
`(1+u)^(-1/4)=E exp(-Su)`. Frullani's integral gives

    int_0^infinity [(1+u)^(-1/4)-exp(-zu)]du/u
      = log z-E log S=log z-digamma(1/4).

The expectation-interchange is legitimate: the integral of the absolute
Frullani difference for fixed S equals |log(z/S)|, whose Gamma expectation
is finite. This proves (1), including its constant.

## 2. Arithmetic commutator and exact source intertwining

Set

    D0=L_+-X-C0/2,       D=L_+-F_+-X-C0/2.

Then, on the stated source domain,

    D0 B=0,       D C=C D0,       D Theta=0.             (2)

The only arithmetic identity needed is

    [C,X]f=sum_n (log n)n^(-1/2)f(x+log n)=F_+ C f,

which follows from `sum_(d|n)Lambda(d)=log n`. Translation invariance gives
`L_+ C=C L_+`. These identities prove (2) with every prime power retained.
The exchanges at h=0 follow from the differentiated theta majorant; for
large h the Gaussian tail is integrable against kappa. No critical-line
Euler product or inverse-zeta domain is invoked.

## 3. Positive future ground generators

For a scalar multiplier v and u define

    G_B v(x)=int_0^infinity kappa(h) B(x+h)/B(x)
                                      [v(x)-v(x+h)]dh,

    G_Theta u(x)=int_0^infinity kappa(h) Theta(x+h)/Theta(x)
                                      [u(x)-u(x+h)]dh
       +sum_(n>=2)Lambda(n)n^(-1/2)Theta(x+log n)/Theta(x)
                                      [u(x)-u(x+log n)],

    T_B v(x)=C(Bv)(x)/Theta(x).

All jump rates and the averaging weights in T_B are nonnegative and T_B 1=1.
The exact source intertwining (2) becomes

    G_Theta T_B v = T_B G_B v.                          (3)

Proof: `D0(Bv)=B G_Bv` and `D(Theta u)=Theta G_Theta u`, because
D0 B=D Theta=0. Substitute C(Bv)=Theta T_Bv into (2).

For bounded C^1 v with bounded derivative these integrals are pointwise
finite. For the continuous B rate,

    kappa(h) B(x+h)/B(x)
       <= exp[-pi(exp(2h)-1)]/(1-exp(-2h)).

For Theta, its future ratio is a positive Gaussian-fiber average of the B
ratio and obeys the same bound. Also, with theta(z)=sum_n exp(-n^2z),

    n^(-1/2)Theta(x+log n)/Theta(x)=theta(n^2z)/theta(z)
       <= 2 exp[-pi(n^2-1)],  z>=pi.

To see the factor 2, use `theta(w)<=exp(-w)/(1-exp(-3w))`
for w>=pi and theta(z)>=exp(-z). Thus the complete discrete rate, even
weighted by log n, is summable uniformly on x>=0. These facts establish a
positive conservative jump-generator core. They are not, by themselves,
a proof of any chosen closed-generator or semigroup uniqueness theorem.

There is an especially simple continuous generator in Gaussian scale.
Put w(z)=v((1/2)log(z/pi)). The change u=z(exp(2h)-1) gives

    G_B w(z)=(1/2)int_0^infinity exp(-u)
                                      [w(z)-w(z+u)]du/u. (4)

Likewise the entire Theta generator is

    G_Theta w(z)=1/[2 theta(z)] int_0^infinity theta(z+u)
                                      [w(z)-w(z+u)]du/u
       +sum_(n>=2)Lambda(n)theta(n^2z)/theta(z)
                                      [w(z)-w(n^2z)].   (5)

Thus (3) intertwines the additive Gamma-subordinator generator (4) with a
single positive generator containing both the continuous Gamma and ALL
multiplicative prime-power jumps. Positivity here is a future evolution
statement, not positivity of the original reflected quadratic form.

## 4. The eta/Phi ladder has only an explicit covariance defect

Put

    P(z)=4z^2-6z,
    eta=(d^2/dx^2-1/4)B=B P(z),
    Phi=C eta=(d^2/dx^2-1/4)Theta,
    beta(z)=(4z-1)/P(z)=1/(6z)+5/[6(z-3/2)].

All eta and Phi weights are positive on x>=0. No positivity of eta on the
whole line is asserted. The derivative commutators are
`[D0,d/dx]=[D,d/dx]=I`; consequently

    D0 eta=2B'=-beta(z)eta,
    D Phi=2Theta'=-betabar(x)Phi,
    betabar(x)=C(beta eta)(x)/Phi(x).                    (6)

Here and below beta in a shifted argument means beta(pi exp(2x)).
The same identities can also be verified from the convergent absolute row

    L_+eta/eta=x+C0/2-beta(z).

Define the positive pure-forward generators

    G_eta v=int_0^infinity kappa(h)eta(x+h)/eta(x)
                                      [v(x)-v(x+h)]dh,

    G_Phi u=int_0^infinity kappa(h)Phi(x+h)/Phi(x)
                                      [u(x)-u(x+h)]dh
       +sum_(n>=2)Lambda(n)n^(-1/2)Phi(x+log n)/Phi(x)
                                      [u(x)-u(x+log n)],

    T_eta v=C(eta v)/Phi.

They obey the EXACT potential intertwining

    (G_Phi-betabar)T_eta=T_eta(G_eta-beta),              (7)

or, equivalently,

    G_Phi T_eta v-T_eta G_eta v=-Cov_(p(x))(beta,v).      (8)

In (8), the probability weights and fiber values are

    p_n(x)=n^(-1/2)eta(x+log n)/Phi(x),
    v_n(x)=v(x+log n),    beta_n(x)=beta(n^2z).

The covariance is `E_p(beta_n v_n)-E_p beta_n E_p v_n`.
Indeed (6) gives `D0(eta v)=eta(G_eta-beta)v` and
`D(Phi u)=Phi(G_Phi-betabar)u`, so (7) follows from DC=CD0.
No sign is assigned to this covariance, despite beta being positive bounded.

The eta future rates are bounded by a fixed polynomial in exp(2h) times the
Gaussian bounds from Section 3, because z>=pi>3/2. Their complete discrete
rates likewise have a polynomial-in-n factor times exp[-pi(n^2-1)]. Thus
all statements hold on the same compact smooth multiplier core, and on
polynomial-growth multiplier classes wherever their shifted first derivatives
have corresponding local majorants.

## 5. Exact carré identity, with all conditional-variance terms retained

For a positive jump generator G use the convention

    Gamma_G(v)=2v Gv-G(v^2)
              =int rate(x,dy)[v(x)-v(y)]^2 >=0.

Let T=T_eta, u=Tv, V=T(v^2)-u^2, and H_n=v_n-u. Then

    Gamma_(G_Phi)(u)
      =T Gamma_(G_eta)(v)+G_Phi V
         -2 Cov_T(v,G_eta v)+Cov_T(beta,H^2).            (9)

Here `Cov_T(v,G_eta v)=T(v G_eta v)-(Tv)T(G_eta v)`, with
G_eta evaluated at the shifted fiber point; and
`Cov_T(beta,H^2)=E_p(beta_n H_n^2)-betabar E_p H_n^2`.

For completeness, substitute (8) twice into

    2u G_Phi u-G_Phi(u^2)
      =2u G_Phi Tv-G_Phi T(v^2)+G_Phi V.

Use `G_eta(v^2)=2vG_eta v-Gamma_(G_eta)(v)`. The two beta
covariances combine as
`Cov(beta,v^2)-2u Cov(beta,v)=Cov(beta,(v-u)^2)`, proving (9).
Thus the nonnegative lifted carré does NOT stand alone: the variance
transport, the covariance with G_eta, and the beta covariance are mandatory.
No inequality follows merely by omitting them.

## 6. The exact remaining boundary issue

Equations (2)-(9) do not compare the original two-sided odd form with zero.
The actual form includes odd reflection, the forcing row associated with
`(a-S)Phi=-cosh(x/2)`, and the full rank-one pole. Restricting to x>=0
retains none of these automatically. The same-source eta lift is available
for an actual odd g through its genuine unanchored future inverse f=Mg and
v=f/eta, but extending (9) to that form domain requires its actual regularity
and energy domination, not just the pointwise identity Cf=g.

Even though Theta is positive on the full real line, its negative-wing
asymptotic is of order exp(-x/2). Consequently the backward all-prime row
`sum_n Lambda(n)n^(-1/2)Theta(x-log n)` diverges at each fixed x.
One may not turn (3) into a two-sided Theta ground factorization by integrating
this row separately. In particular neither an ordinary L2 contraction nor
K<=1 is claimed here.
