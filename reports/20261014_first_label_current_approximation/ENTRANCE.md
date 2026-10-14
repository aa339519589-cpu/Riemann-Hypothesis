# Exact operational entrance for the full-band eta lift

This is the origin completion of the positive full-band eta-score lift,
not a positive boundary term for the reflected Weil form. It uses the same
eta link and original observed process. No singular canonical quotient or
higher-neutral trace repair is required for this entrance law.

## 1. Operational clock and the complete entrance law

Use [the full-band lift](HIDDEN_LIFT.md), with
p_n=n^(-1/2)eta(x+log n)/Phi(x), s=psi/Phi, A_star and G_psi. Put

    theta_c(x)=psi(x)exp(-x/2),
    H=theta_c G_psi, A_op=theta_c A_star,
    p=psi'(0), Phi0=Phi(0), K0=3Phi(0)+Theta(0)/2,
    a0=p/Phi0.

The common clock is label-independent, so H T=T A_op holds on the same
arbitrary-label core. Write p_n^0=p_n(0), and retain the complete numbers

    b_n=a0^(-1){integral_0^infinity kappa(y)
                      eta(log n+y)/eta(log n) s(y)dy
                        +sum_(d|n)Lambda(d)s(log d)}.   (1)

They are positive, grow at most polynomially in n, and E_(p^0)b=K0/p.
The origin limits of all three hidden jump channels exist. At x=0 they are

    Gamma: Phi0 kappa(y)eta(log n+y)/eta(log n)s(y)dy,
                 (0,n)->(y,n);
    divisor: Phi0 Lambda(d)s(log d), d|n,
                 (0,n)->(log d,n/d);
    reset: p p_m^0 b_m,
                 (0,n)->(0,m).                       (2)

The total spatial exit rate conditional on n is p b_n. The reset candidate
rate is K0. All of these are finite for a fixed starting label. In particular
s(y)=O(y) removes the Gamma diagonal singularity at the origin itself.

The operational process is well defined also from the initial law p^0.
The reset rate theta_c beta_psi=K exp(-x/2) is globally bounded. Reset label
tails remain uniformly Gaussian, including x=0; (1) gives that endpoint
bound. Between resets divisor labels decrease and Gamma has a uniformly
bounded first displacement moment after the operational scaling. A bounded
number of Poisson reset candidates on compact time intervals, together with
the finite-label/nonexplosion argument of the full-band lift, constructs the
process. There is no infinite-rate hidden reset at the entrance.

Let tau be the first observed spatial exit from zero. The killed generator
on origin labels, with its cemetery value set to zero, is

    A_wall F(n)=[K0+p b_n]F(n)-p E_(p^0)[b F].          (3)

It has the exact left eigenmeasure identity

    E_(p^0)[A_wall F]=K0 E_(p^0)F.                    (4)

Consequently p^0 is a quasistationary law, and starting from it

    P(tau>t,N_t=n)=exp(-K0 t)p_n^0.                   (5)

One can verify (5) directly in the killed forward equations; uniqueness
follows by the positive finite-label truncation and Gaussian-tail limit.
The hidden reset candidates need not preserve p^0 by themselves. It is the
COMBINED reset and spatial killing that yields (5).

The complete joint exit measure is

    Law(tau in dt, X_tau in dy, N_tau=m)
       =exp(-K0 t)dt
          [kappa(y)psi(y)dy
                 +sum_d alpha_d psi(log d)delta_(log d)(dy)]p_m(y).
                                                               (6)

For Gamma exits this follows from
p_n^0 Phi0 eta(log n+y)/eta(log n)s(y)=psi(y)p_n(y).
For a divisor d, use the initial label n=dm and
p_(dm)^0 Phi0 Lambda(d)s(log d)=alpha_d psi(log d)p_m(log d).
Thus every prime power and the full continuous Gamma law occur with their
original coefficients. In particular

    tau~Exp(K0),
    Law(X_tau)=mu0=[kappa(y)psi(y)dy
                  +sum_d alpha_d psi(log d)delta_(log d)]/K0,
    Law(N_tau | tau,X_tau)=p_(X_tau).                 (7)

The holding time and observed exit location are independent. The posterior
before exit is p^0 by (5), and afterwards it is the original full-band eta
posterior by (6) and the already proved filtering. Cylinder induction gives
the full natural-observed-filtration statement through the entrance.
This is a positive hidden realization of the exact operational entrance
law, without dividing by xi_1 or changing the observed psi generator.

