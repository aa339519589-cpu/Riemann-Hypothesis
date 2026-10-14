# A full-band positive eta-score lift and natural-filtration posterior

This construction uses the ORIGINAL positive future generator G_psi on every
x>0, including the interval where the first xi seed is negative. It never
uses xi as a probability density. It does not identify a positive hidden
square with the original reflected form. This package uses only the
current-adapted field, not the singular canonical quotient.

## 1. Positive link and score

Use the notation and complete theta sums of
[the score lemma](THETA_SCORE.md):

    p_n(x)=n^(-1/2)eta(x+log n)/Phi(x),
    s(x)=psi(x)/Phi(x),
    beta_n(x)=(4n^2z-1)/(4n^4z^2-6n^2z), z=pi exp(2x),
    beta_bar=E_p beta, beta_psi=K/psi, K=3Phi+Theta/2.

Every p_n and beta_n is positive. The proved estimate
s'(x)-2s(x)>3 makes s strictly increasing, with
s(0)=0 and s(x)>0 for x>0. Let T F(x)=sum_n p_n(x)F(x,n).
All generator conventions are positive: the Markov process has generator
minus the operator displayed below.

The positive G_Phi generator and the exact rows D Phi=-beta_bar Phi,
D psi=-beta_psi psi are established in
[the published foundational intertwining](../20261014_future_gamma_prime_semigroup/FOUNDATIONAL_INTERTWINING.md)
and [the complete original source/current identity](../20261014_positive_reflected_storage/CURRENT_FORM.md).
Here G_psi has continuous rate kappa(h)psi(x+h)/psi(x) and prime-power
rate Lambda(d)d^(-1/2)psi(x+log d)/psi(x).

First form the stationary eta lift A_eta. Its Gamma and divisor channels are

    A_eta,G F(x,n)=integral kappa(h) eta(x+log n+h)/eta(x+log n)
                                  [F(x,n)-F(x+h,n)]dh,
    A_eta,d F(x,n)=sum_(d|n)Lambda(d)
                                  [F(x,n)-F(x+log d,n/d)],

and use the full reset with rate p_m(x)beta_m(x) from n to m. The exact
arbitrary-label identity is

    G_Phi T=T A_eta.                                  (1)

Indeed the future-value coefficients agree by the continuous weight identity
and p_(dm)(x)=d^(-1/2)Phi(x+log d)p_m(x+log d)/Phi(x). For explicit verification of the remaining current coefficient, the complete
Gamma row identity is

    int kappa(h)[Phi(x+h)/Phi(x)
              -eta(x+log n+h)/eta(x+log n)]dh
       =log n-E_p log N+E_p beta-beta_n.

It follows from L_+eta/eta=x+C0/2-beta and its complete theta sum in the
published foundational calculation. The observed prime row is E_p log N
by sum_(d|n)Lambda(d)=log n; the hidden divisor row is log n. Thus the
remaining coefficient is E_p beta-beta_n. Its average against F is
-Cov_p(beta,F), exactly the average of the full reset. The Gamma singularity
is grouped before this subtraction. This proves (1) for arbitrary label
fields, not merely common-seed fields.

Put h(x,n)=s(x),

    q_n=(A_eta h)(x,n)/s(x), a_n=beta_n-q_n.            (2)

Resets do not move h, and all spatial jumps move x forward. Therefore
q_n<=0 LABELWISE, and a_n>0. Applying (1) to s and using
D Phi=-beta_bar Phi, D psi=-beta_psi psi gives

    E_p q=G_Phi s/s=beta_bar-beta_psi,
    E_p a=beta_psi.                                   (3)

No first-seed signed weight occurs in (1)-(3).

## 2. Three positive channels on the full positive half-line

Define A_star by the following rates:

    Gamma: kappa(h) eta(x+log n+h)/eta(x+log n)
                                     *s(x+h)/s(x),
           (x,n) -> (x+h,n);
    divisor: Lambda(d)*s(x+log d)/s(x), d|n,
           (x,n) -> (x+log d,n/d);
    reset: p_m(x)a_m(x),
           (x,n) -> (x,m).                            (4)

Self resets may be included with zero increment. Their candidate total rate
is exactly beta_psi(x), independent of the starting label. Then

    G_psi T=T A_star                                 (5)

on bounded smooth controlled arbitrary-label fields. To verify the sign,
the h-scaled A_eta generator satisfies

    G_psi T F=T A_eta^h F+Cov_p(q,F).

The added reset with rates p_m(-q_m) has exactly the displayed covariance as
its average. Combined with the old eta reset, its rates are p_m a_m as in
(4). This proves (5). All primes, every divisor, and the original psi rate
are retained.

Fix any epsilon>0. On x>=epsilon, beta_psi is bounded. The Gamma channel has
finite variation, with locally Lipschitz coefficients in the jump norm, and
its first logarithmic displacement moment is bounded uniformly in the label
and x>=epsilon. For example eta(x+log n+h)/eta(x+log n) is bounded by a
constant times exp(9h/2)exp[-pi exp(2epsilon)(exp(2h)-1)], while
s(x+h)/s(x)<=C_epsilon exp(2h). This bounds h times the Gamma jump measure
by an integrable envelope independent of n and x. Standard Poisson
small-jump truncation therefore gives its unique nonexplosive path between
discrete events.

Resets are dominated by a fixed-rate Poisson process. Between two resets,
every divisor event strictly decreases n, so only finitely many such events
are possible, although their rates need not be bounded uniformly in n.
Each reset samples one finite integer with probability p_m a_m/beta_psi.
This normalized law has uniformly Gaussian label tails on x>=epsilon.
Indeed q_n is bounded by a constant times a polynomial in n and log n,
while p_n has a polynomial prefactor times exp[-z(n^2-1)]. The normalization
is also controlled: beta_psi(x)^(-1)<=C_epsilon(1+z), since
beta_psi~3/(2z) at infinity and is strictly positive on compact intervals.
For n>=2 the extra polynomial z is absorbed by weakening the Gaussian
exponent; hence its tail beyond label M tends to zero uniformly in x.
Consequently the process (4) is nonexplosive and unique for every finite
starting label. This also gives uniqueness for initial Gaussian mixtures.

For completeness, the exact full filtering assertion is not inferred only
from one-time averaging. If Q_t is the hidden semigroup and P_t the original
G_psi semigroup, then

    T Q_t=P_t T.                                     (6)

One proof uses the forward equations: P_t(x,dy)p_n(y) solves the hidden
forward equation by (5). Uniqueness follows from the preceding construction.
One can justify the measure calculation first with localized x, finitely
many labels and Gamma jumps larger than a cutoff. On a fixed time interval,
the probability of seeing a label above M is bounded by the initial tail
plus the expected number of resets times the uniform reset tail. Both tend
to zero as M tends to infinity. The Gamma first-moment envelope removes the
small-jump cutoff, and nonexplosion removes spatial localization. Thus no
boundary condition at infinite label is being inserted in (6).

Since T M_b=M_b T for every bounded function of the observed x, induction
through successive Q_t and observed multiplication kernels proves the
finite-cylinder posterior. Cadlag paths and a bounded monotone-class
argument give

    Law(N_t | sigma(X_u:0<=u<=t))=p_(X_t).             (7)

The observed X has exactly P_t. This construction works for each starting
x>0. It does not assert that a finite canonical hidden-square entrance law
exists at x=0.


The honest operational completion at x=0 is proved in [ENTRANCE.md](ENTRANCE.md).
It supplies the same natural-filtration posterior at the wall; no signed
first-xi seed or singular canonical quotient is assigned a probability law.
