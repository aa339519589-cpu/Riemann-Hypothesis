# Coefficient-one reset occupation in the same observed current

This note uses the full-band eta-score hidden process, including its honest
operational entrance. Its hidden field is the conditional mean of the SAME
complete original-psi current. It is not the singular canonical Mobius
quotient; in particular all divisor squares of this field must remain.
The result is a positive conditional-variance budget. The exact signed
transport and original boundary graph are retained in [REPORT.md](REPORT.md);
this budget alone does not prove the full signed source comparison.

## 1. Inputs, clocks and notation

Use the original theta functions B, eta=B''-B/4, Theta=C B, Phi=C eta,
psi=-Phi', where C f(x)=sum_(n>=1)n^(-1/2)f(x+log n). Write

    kappa(h)=exp(-h/2)/(1-exp(-2h)),
    K(x)=3Phi(x)+Theta(x)/2,
    theta(x)=exp(-x/2)psi(x),
    p_n(x)=n^(-1/2)eta(x+log n)/Phi(x),
    T F(x)=sum_n p_n(x)F(x,n).

All p_n are positive on x>=0. Let G be the original positive future
Gamma/all-prime generator, and H=theta G its operational version. Positive
generator means the Markov semigroup is exp(-t H). The exact full-band
hidden generator A is the operational scaling of A_star in
[the full-band eta-score lift](HIDDEN_LIFT.md).
It has positive continuous, genuine divisor, and full-refresh reset channels,
and

    H T=T A.                                                    (1)

The arbitrary-label filtering statement, not merely its common-seed
restriction, is used. At positive x the reset rate from n to m is

    p_m(x)d_m(x), d_m=theta(x)a_m(x)>0,
    dbar(x)=T d=theta beta_psi=exp(-x/2)K(x)=:k(x).                (2)

Here a_m=beta_m-q_m is as defined in that lift. At x=0 the genuine operational
extension in [the entrance note](ENTRANCE.md)
has d_n(0)=p_* b_n, where p_*=psi'(0), and k(0)=K(0)=:K_*.
There is no division by psi(0) in (1)-(2).

Let u=r-c_infinity be the SAME actual plateau-subtracted ratio. Its complete
source includes the unchanged pole form; this psi null subtraction need
not preserve pole centering. The proved regularity is u in H^s, 1/2<s<1,
and u tends to zero. On operational rays define

    I_x=lim_(t->infinity)int_0^t H u(X_v)dv,
    E I_x=u(x), Var(I_x)=J(x).

The current limit is in L2 and almost surely, including the real holding
current at x=0. We use the proved global bound sup J<infinity and J(x)->0
at infinity. The latter follows directly from the tail estimate (20) in
[the ray theorem](../20261014_positive_reflected_storage/FORWARD_RAYS.md).
The honest entrance and global bound are proved in
[the operational current note](../20261014_coherent_prime_ray_bridges/COHERENT_OPERATIONAL_RAY_CURRENTS.md).

## 2. A finite current-adapted field through the origin

For the hidden process started from a particular (x,n), set

    w(x,n)=E_(x,n) I_x,    V(x)=T(w^2)(x)-u(x)^2.                (3)

This is well defined for every finite n and every x>=0. Indeed the law with
initial label p(x) has the original observed path law. Each individual label
law is dominated by that mixture with factor 1/p_n(x). Thus the SAME
observed current exists in L2 under each initial label law. Conditional
Jensen gives, without any canonical seed quotient,

    T w=u,  0<=V<=J,  T w^2<=u^2+J.                             (4)

There is a version of w continuous in x for every fixed n. One direct
justification is to use finite-time potentials w_t=E int_0^t H u. Their
forcing is continuous and bounded by the actual Holder/theta estimates,
and the operational hidden process is Feller on compact sets, including its
entrance. The observed conditional remaining second moment is
E[u(X_t)^2+J(X_t)]. It tends to zero uniformly in the initial observed x:
choose a sufficiently large spatial level where u^2+J is small, and use a
fixed positive operational arrow beyond that level to bound the probability
of not exiting by exp(-c t). The same estimate divided by the positive
minimum of p_n on a fixed compact interval proves compact-uniform convergence
of w_t to w for that n. Thus its Levy jumps are actual differences of values.
Only the extended martingale-domain statements below are needed.

The additive Markov property gives a CLOSED hidden martingale

    M_t=int_0^t H u(X_v)dv+w(X_t,N_t)
        =E[I_x | full hidden history through t].                (5)

Its optional projection onto the observed history is
int_0^t H u(X_v)dv+u(X_t), by the full posterior theorem. The remainder
w(X_t,N_t) tends to zero in L2, since the integral and (5) both converge to
I_x. Orthogonality of its initial conditional expectation and subsequent
martingale increments gives the exact variance identity

    J(x)=V(x)+E_(x,p)int_0^infinity Gamma_A[w](X_t,N_t)dt.        (6)

Gamma_A is the sum of squared w jumps with the ORIGINAL continuous,
divisor, and reset rates. This is proved first as the bracket of (5), then
identified through the Levy system and positive truncations. No classical
generator-domain claim is required. In particular every divisor square of
w remains; generally it is not zero. The extended drift equation is

    A w(x,n)=H u(x),                                            (7)

with its continuous and divisor parts kept grouped if their individual
drift domains are not known. The canonical field phi/(eta s) need not be
square integrable at the wall and is never substituted for w.

## 3. Exact coefficient-one refresh dissipation

For any probability p and nonnegative d with E d=k<infinity, the refresh
operator is

    A_r F(n)=sum_m p_m d_m(F_n-F_m)=k F_n-E(dF).

Let h=F-E F and v=E h^2. Then, whenever finite,

    Cov_p(F,A_r F)=k v,
    E Gamma_r[F]=E(d h^2)+k v.                                 (8)

The second equality follows by expanding
sum_(n,m)p_n p_m d_m(h_n-h_m)^2 and using E h=0. It extends as an identity
of nonnegative extended quantities by truncation and L2 approximation.
It is NOT a stationarity assertion about p. In particular

    T Gamma_r[w]>=k V.                                         (9)

In (6), all channel occupations are nonnegative. Filtering at each time
and Tonelli therefore prove the coefficient-one SAME-field bound

    J(x)>=V(x)+R_H(k V)(x),                                    (10)
    R_H F(x)=E_x int_0^infinity F(X_t)dt.

It holds at EVERY x>=0. The origin holding interval is part of R_H. At x>0,
the equivalent physical-clock form is

    J(x)>=V(x)+R_G(beta_psi V)(x), beta_psi=K/psi.                (11)

Equation (11) must not be applied at zero after discarding the operational
hold. The exact, stronger remainder in (10) is

    J=V+R_H{T Gamma_cont[w]+T Gamma_div[w]
                            +T[d(w-u)^2]+k V}.                 (12)

All terms here are the same current and the same eta posterior.
This is not an additional gain on top of an already spent current J.
In particular it is not the 49/101 selection bound for a different xi lift.

For clarity, the associated signed transport equation is

    Gamma_H[u]=T Gamma_A[w]+H V,                                (13)
    (H+k)V<=Gamma_H[u].                                        (14)

These hold in the extended potential or stopped-resolvent sense: (13)
follows either from (1), (7), and the product identity, or from the two
martingale brackets and (6). No unproved differentiability of V is used.
The covariance of w with its complete drift is zero; hence the exact
GROUPED covariance constraint is

    Cov_p(w,A_cont w+A_div w)=-k V.                             (15)

When individual terms are not integrable, (15) means the common localized
martingale/product limit, not separate improper integrals. Notice the sign:
(H+k) is a genuinely killed operator. It is not identified with the source
operator D, since D(psi f)=psi G f-K f involves G-beta_psi instead.

