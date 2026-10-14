# Exact triangular divisor transport for the same current-label contrasts

This concerns the full-band eta CURRENT-ADAPTED field, not its singular
canonical seed quotient. Subtracting two genuine hidden current equations
eliminates their complete common source and reset forcing. The remaining
continuous deficit and true-divisor row form an honest probability kernel.
All prime powers, origin qualifications and the actual killed terminal are
retained. No original-form upper sign is inferred.

## 1. Dependencies and conventions

Use the full positive eta-score lift and honest operational entrance in
`../20261014_first_label_current_approximation/HIDDEN_LIFT.md` and
`../20261014_first_label_current_approximation/ENTRANCE.md`.
The SAME actual current field is constructed in
`../20261014_first_label_current_approximation/CURRENT_FIELD.md`.
Its globally bounded fixed-label versions are justified, including all
refresh re-births and the origin holding current, in
`../20261014_first_label_coercive_correction/GLOBAL_LABEL_CONTROL.md`
(the independently reviewed global label theorem in that package).
The ordering a_n>a_1 used below is proved in
`../20261014_first_label_coercive_correction/RESET_FORCING.md`.

Put s=psi/Phi, beta=K/psi, K=3Phi+Theta/2 and

    p_n(x)=n^(-1/2)eta(x+log n)/Phi(x),
    w_n(x)=E_(x,n) I_x, T w=u=r-c_infinity,
    v=w_1, Delta_n=w_n-v.

All positive generators below have Markov generator equal to their negative.
For x>0 define the continuous label generator and finite divisor row

    G_n F(x)=int_(y>x) q_n(x,dy)[F(x)-F(y)],
    q_n(x,dy)=kappa(y-x) eta(y+log n)/eta(x+log n)
                                      s(y)/s(x) dy,
    lambda_d(x)=Lambda(d)s(x+log d)/s(x),
    L_n(x)=sum_(d|n,d>=2)lambda_d(x).                         (1)

Every genuine prime-power divisor participates in (1). Thus L_1=0.
The reset scores a_n are the full positive scores of that lift; T a=beta.
The published global current bound gives, for each fixed n,

    sup_(x>=0)|w_n(x)|<=C_sigma ||u||_(H^sigma)(1+log n).       (2)

The finite-label fields are continuous, and their equations hold in the
extended, stopped-martingale sense. No claim that all psi w_n are original-P
vectors is used here.

## 2. The exact continuous mass deficit is a probability completion

For n>=2, the complete theta posterior ratio
rho_n=p_n/p_1=n^(-1/2)eta(x+log n)/eta(x) is strictly decreasing in x.
Indeed with z=pi exp(2x),

    rho_n=n^2 (2n^2 z-3)/(2z-3) exp[-(n^2-1)z],
    d(log rho_n)/dz
      =-(n^2-1)-6(n^2-1)/[(2n^2 z-3)(2z-3)]<0.

Consequently q_n=q_1 rho_n(y)/rho_n(x), and q_1-q_n is nonnegative.
Its total mass is finite: the bracket 1-rho_n(y)/rho_n(x) cancels the
Gamma 1/(y-x) singularity, and both far rows have Gaussian decay.
Write this mass M_n(x).

There is an exact, not estimated, identity

    M_n=L_n-a_n+a_1.                                         (3)

One verification keeps the whole Gamma row. Let D0=L_+-X-C0/2 be the
future Gamma operator without prime shifts, and set S_n=psi p_n.
The Gaussian differential identity and the score product rule give

    D0 S_n/S_n=L_n-a_n,     D0 S_1/S_1=-a_1.

Equivalently, if A_n^Gamma is the nonnegative Gamma score increment, then
D0 S_n/S_n=log n-beta_n-A_n^Gamma, while

a_n=beta_n+A_n^Gamma+L_n-log n; here
sum_(d|n)Lambda(d)=log n includes all prime powers. Applying the same product
rule to S_n=S_1 rho_n gives

    D0 S_n/S_n=-a_1+G_1 rho_n/rho_n=-a_1+M_n,

which proves (3). Since a_n>a_1, one has 0<M_n<L_n. Therefore

    P_n(x,dy)=[(a_n-a_1)delta_x(dy)+(q_1-q_n)(x,dy)]/L_n     (4)

is an HONEST probability measure supported on [x,infinity). Its atom at x
is essential; it is the exact complement of the extra continuous row.
For n=2, writing lambda=lambda_2, (3) is

    (a_2-a_1)+M_2=lambda.                                    (5)

Thus the reset-score difference and the continuous mismatch use exactly
the same true prime2 mass, rather than independent scalar budgets.

## 3. Exact same-source triangular contrast equation

The full hidden current drift equation at label n is

    G_n w_n+sum_(d|n)lambda_d[w_n-w_(n/d)(x+log d)]
                 +beta w_n-T[a w]=G_psi u.                   (6)

The complete reset and source rows on the right of the rearranged (6) are
the SAME for every n. Subtracting the label1 equation yields

    (G_n+beta+L_n)Delta_n
      =(G_1-G_n)v+sum_(d|n)lambda_d[w_(n/d)(x+log d)-v(x)]
      =sum_(d|n)lambda_d w_(n/d)(x+log d)-L_n P_n v(x).       (7)

The sign of the continuous difference in the first line is positive.
In the second line its future part has been grouped with its EXACT current
mass, using (3). This is not an absolute-value replacement of a signed row.
Every target n/d is a smaller label. In particular,

    (G_2+beta+lambda)(w_2-w_1)
                 =lambda[v(x+log2)-P_2 v(x)].                (8)

Neither the canonical seed field nor a label-independent replacement of
the actual current is involved. The pole and original source forcing were
not set to zero: the identical complete source in (6) cancels on subtraction.

For domain clarity, (6) is the closed-current martingale equation. On a
compact positive x band, reset terms are absolutely paid by (2) and the
Gaussian newborn law; the divisor sum is finite. Stopping before their
first candidate isolates its continuous G_n equation. Also q_1-q_n is a
finite kernel with locally bounded mass and v is globally bounded, so the
bounded-kernel perturbation of the G_1 martingale equation gives its G_n
version. Hence (7) is a legitimate extended stopped equation, without
assuming classical differentiability of any w_n.

## 4. Positive killed representation and its actual terminal

Let Y be the increasing pure-continuous process with positive generator
G_n, n fixed. It is nonexplosive: its rates are bounded above by the label1
rates, and the same finite-variation jump construction and physical-z moment
bound used for that process apply on every x>=x0>0. Put

    b_n=beta+L_n,
    R_n F(x)=E_x int_0^infinity
                    exp[-int_0^t b_n(Y_j)dj] F(Y_t)dt.        (9)

The complete score inequality s'-2s>3 implies s(x+log d)/s(x)>d^2.
Every n>=2 has a prime divisor, so

    L_n(x)>=4 log2, x>0.                                    (10)

The stopped formula for (7) has a surviving terminal Delta_n(Y_t).
By (2) and (10), its absolute expected value is at most
C_n exp[-4(log2)t], and therefore tends to zero. Spatial localizations
are removed using nonexplosion and bounded fixed-label fields. This is an
ACTUAL terminal proof, not an inference from finite almost-sure killing.

The forcing in (7) is bounded in absolute value by C_n L_n. Since
R_n L_n<=R_n b_n=1, it is absolutely integrable. Thus exactly

    Delta_n=R_n{sum_(d|n)lambda_d w_(n/d)(.+log d)-L_n P_n v}. (11)

One equivalent probability description kills Y at rate beta+L_n.
At beta killing take payoff zero. At L_n killing choose a genuine divisor
d with probabilities lambda_d/L_n and, independently, a destination y
with law P_n(Y_tau,dy); take payoff

    Z_n=w_(n/d)(Y_tau+log d)-v(y).

Then Delta_n(x)=E_x Z_n. Any coupling of these two terminal draws gives
the same mean; it need not give the same variance. For the stated independent
draws the exact Jensen completion is

    |Delta_n(x)|^2+E_x|Z_n-E_x Z_n|^2=E_x|Z_n|^2.            (12)

There is no deleted killing mass or source-current remainder in (11)-(12).
This scalar first-split description is not asserted to be a joint original
flow on all initial x; that stronger coupling requires its own construction.

At x=0, (7)-(12) mean their genuine operational entrance extension.
Multiply every rate by theta=exp(-x/2)psi before taking the limit; theta/s
has finite positive limit, so the Gamma, divisor, reset and stay masses all
have the entrance limits from the cited lift. The holding source cancels
between the two equal-position currents exactly as in (6), rather than
being discarded. Alternatively all scalar bounds below follow at zero
by continuity of the finite-label currents from x>0.

## 5. A gauge-invariant all-label tail-oscillation bound

Let Omega(n) count prime factors with multiplicity, and define

    osc_x(v)=sup_(y,z>=x)|v(y)-v(z)|.

For complex or Hilbert-valued bounded v this is the diameter of its future
range. Then the SAME actual field satisfies

    |w_n(x)-w_1(x)|<=Omega(n) osc_x(v), n>=1.                 (13)

Proof is induction on Omega(n). For n=1 it is zero. In (11) insert
w_(n/d)(y+log d)=v(y+log d)+Delta_(n/d)(y+log d).
Because P_n is a probability supported in [y,infinity),

    |v(y+log d)-P_n v(y)|<=osc_y(v),
    |Delta_(n/d)(y+log d)|<=(Omega(n)-1)osc_y(v).

Y only increases, so osc_(Y_t)(v)<=osc_x(v). Integrating with
R_n L_n<=1 proves (13). This proof preserves the whole divisor tree;
there is no truncation to prime labels. In particular

    |w_n(x)|<=(2Omega(n)+1)sup_(y>=x)|w_1(y)|.                (14)

Since T w=u and variance minimizes distance to constants, (13) also gives
with A_j(x)=sum_(n>=2)p_n(x)Omega(n)^j,

    |w_1-u|<=A_1(x)osc_x(v),
    V_w(x)<=A_2(x)osc_x(v)^2.                               (15)

The complete Gaussian posterior bounds give A_j(x)<=C_j exp(-3pi exp(2x))
for each fixed j: use Omega(n)<=log n/log2 and sum the entire positive
Gaussian series. In contrast to a mere label norm estimate, (13)-(15) are
constant-gauge invariant and compare the current to its OWN first-label
future oscillation. As v tends to zero, all fixed-label currents do too.

Equations (7), (11), and the variance in (12) are constructive signed
transport identities. They do not yet compare their cross-edge squares
with the original full forward energy or the complete reflected/pole graph.
No Q_delta upper sign or RH exclusion is claimed.
