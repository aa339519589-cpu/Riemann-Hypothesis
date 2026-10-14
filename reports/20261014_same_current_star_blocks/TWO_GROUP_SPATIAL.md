# The dominant current completion is an exact two-group spatial square

The positive left side of the dominant-current completion is exactly the
continuous-plus-true-divisor energy of one explicit field on the SAME full
hidden process. The incoming commutator and score potential are its moving
posterior terms, not independent surplus energies. This identification also
pays the domain of the genuinely higher-label projection.

Use the full eta posterior p, the current w, u=T w, v=w_1 and e=v-u. Write

    q=1-p_1, epsilon=q/p_1, omega=1/epsilon,
    mu=psi^2, m=mu/epsilon,
    w_tail=q^(-1)sum_(n>=2)p_n w_n,
    abar=q^(-1)sum_(n>=2)p_n a_n, beta=T a.

The verified finite-energy and actual weighted cutoff assertions are those
of [the dominant completion](DOMINANT_COMPLETION.md).
The all-prime generator G is positive (rate times value minus future
value). Its continuous rates are k(x,dy), its prime rates r_d(x),
d=log n with Lambda(n)>0, and b=G^*mu. All energy integrals below use ONE
future orientation, the same as that completion.

## 1. Two exact posterior conductance laws

Let k_n be the continuous rate at hidden label n. The full score lift gives

    p_n(x)k_n(x,dy)=k(x,dy)p_n(y).                    (1)

A true divisor n0 divides the hidden label, sends it to its quotient, and
moves the observed state from x to y=x+log n0. Its exact law is

    p_(n0 j)(x)lambda_(n0)(x)=r_(n0)(x)p_j(y).       (2)

Both (1) and (2) retain the original s(y)/s(x) factor. These are not
conductances for independently chosen label samples. In particular the
entire outgoing prime row is

    r_prime(x)=sum_(n0>=2)r_(n0)(x).

For the bounded label observable 1_(n=1), natural-filtration intertwining
and the true divisor/refresh channels give

    G p_1=p_1(beta-a_1)-sum_(n0>=2)r_(n0)(x)p_1(y).  (3)

The divisor term is negative because the positive generator applied to
this indicator equals minus the rate of entering label1. Self-refresh
candidates cancel in precisely p_1(beta-a_1). No prime power is omitted.
Equivalently,

    G_cont q=p_1[r_prime-q(abar-a_1)].               (4)

Indeed G_prime q=sum r_(n0)[q(x)-q(y)] and
beta-a_1=q(abar-a_1). This proves (4), including the sign of its potential.

## 2. The exact positive spatial factor

Define the two-group contrast

    d_1(x)=0, d_n(x)=-e(x)/q(x), n>=2.              (5)

Let E_sp[d] be its hidden continuous PLUS all true-divisor carre energy,
with refresh excluded but no spatial channel dropped. Equations (1)-(2)
give its two positive expressions explicitly:

 E_cont[d]=int mu(x)int k(x,dy)q(y)
                   |e(x)/q(x)-e(y)/q(y)|^2,

 E_div[d]=int mu(x)sum_(n0>=2)r_(n0)(x)
        {p_1(y)|e(x)/q(x)|^2
                +q(y)|e(x)/q(x)-e(y)/q(y)|^2}.     (6)

The p_1(y) term is the genuine death into label1. It cannot be treated as a
stay in the conditional-tail label space.

The exact factorization is

 E_sp[d]=F[e]+F_m[e]+int C_omega e^2
                              +int m(abar-a_1)e^2,         (7)

where F[e]=int mu Gamma_G[e], F_m[e]=int m Gamma_G[e], and

 C_omega=G^*(mu omega)-omega G^*mu
   =psi(x)int_0^x kappa(x-y)psi(y)[omega(x)-omega(y)]dy
       +psi(x)sum_(log n<x)alpha_n psi(x-log n)
                                    [omega(x)-omega(x-log n)].  (8)

Thus every term on the right of (7) is nonnegative, but their sum is ONE
spatial energy, not a collection of additional gains beyond E_sp[d].

Here is a direct algebraic proof. Since 1+1/epsilon=1/q, the contribution
of F+F_m at an observed edge x->y is (e_x-e_y)^2/q_x. For a continuous
edge subtract the first square in (6):

 (e_x-e_y)^2/q_x-q_y(e_x/q_x-e_y/q_y)^2
      =(q_x-q_y)e_x^2/q_x^2
                      -(1/q_y-1/q_x)e_y^2.          (9)

After integration, the last term is exactly minus the continuous incoming
commutator in (8), since omega=1/q-1. For a divisor edge subtract its full
second expression in (6):

 (e_x-e_y)^2/q_x
       -{p_1(y)e_x^2/q_x^2+q_y(e_x/q_x-e_y/q_y)^2}
      =-p_1(x)e_x^2/q_x^2-(1/q_y-1/q_x)e_y^2.       (10)

The last term again is the entire prime incoming commutator. Therefore

 F[e]+F_m[e]-E_sp[d]+int C_omega e^2
       =int mu e^2/q^2 [G_cont q-p_1 r_prime]
       =-int m(abar-a_1)e^2,

where the last equality is exactly (4). This proves (7).

## 3. Actual domain passage and the higher projection

The existing dominant-completion proof establishes finiteness of EVERY
term on the right of (7) for this SAME actual e, including the exponentially
growing m, by a common compact weak test and a complete incoming-row
cutoff argument. It does not infer F_m finiteness merely from a Gaussian
amplitude bound. The algebra (9)-(10) can first be used at finite spatial
cutoffs; the same incoming commutator boundary is (8). Its absolute cutoff
majorants were proved in that argument. Positive-kernel monotone limits
in (6) therefore give (7) and E_sp[d]<infinity. Equivalently (7) identifies
its form closure; no classical pointwise drift of d is required.

Now define the genuine group projection and residual

    U_1=v, U_n=w_tail (n>=2),
    Z_1=0, Z_n=w_n-w_tail (n>=2).

Then

    w=U+Z, U=v+d, Delta:=w-v=d+Z,
    T U=u, T Z=0, T(U Z)=0,
    T Z^2=R_high, Var_p U=e^2/epsilon.              (11)

Since E_sp[Delta] is already finite, (7) and the quadratic triangle bound
give E_sp[Z]<infinity. The exact full-refresh square of Z is

    E_reset[Z]=int mu[sum_(n>=2)p_n a_n Z_n^2
                                            +beta R_high]=R_high,a, (12)

which is also finite by the already established same-current reset domain.
Hence U and Z have genuine finite full hidden energy. Their pointwise
orthogonality in (11) does NOT imply energy orthogonality: the posterior
moves, and divisor events cross the two groups.

## 4. The remaining signed Schur slot, with no duplicated square

The actual dominant completion states

 F[e]+F_m[e]+int C_omega e^2+int m(abar-a_1)e^2
      =E_sp[Delta]+int b R_high+R_high,a-2C_high,

where C_high is the exact centered higher mismatch covariance. Substituting
(7) and Delta=d+Z yields precisely

    0=E_sp[Z]+2E_sp(d,Z)+int b R_high+R_high,a-2C_high.       (13)

All four terms in (13) are from the SAME Z and the SAME actual field. The
positive dominant energy has canceled against its own contribution on the
right; it has not paid an additional reflected/pole debit. The cross energy
in (13) need not vanish despite T Z=T(U Z)=0. Its continuous part, for
example, contains

 int mu(x)int k(x,dy)[-e(x)/q(x)+e(y)/q(y)]
                                      sum_(n>=2)p_n(y)Z_n(x),

which is not killed by sum p_n(x)Z_n(x)=0. The genuine divisor term also
has its n0->1 branch, as displayed in (6).

The matched higher-current split gives a positive representation for these
contrasts, but it does not assign a sign to the full (13). The original
reflected/pole graph B_delta remains in Q_delta=2F-B_delta; no part of it
has been dropped or supplied by a second use of (7). This note supplies an
exact positive factor and a paid projection domain, not a full-form sign.
