# A small coefficient for the complete centered reset forcing

This is a SAME-field estimate for the actual current-adapted eta lift, not a
claim that its signed reset forcing vanishes. It uses the audited complete
posterior bounds in `../20261014_first_label_current_approximation/GAMMA_ERROR.md` and the full
score inequality in
`../20261014_first_label_current_approximation/DIVISOR_RESET.md`.

Write s=psi/Phi, beta=K/psi, K=3Phi+Theta/2. The full positive reset rates
are p_m a_m, with

    a_n=beta_n+G_n+D_n,
    beta_n=(4n^2z-1)/(4n^4z^2-6n^2z), z=pi exp(2x),
    G_n=int_0^infinity kappa(h) eta(x+log n+h)/eta(x+log n)
                                      [s(x+h)/s(x)-1]dh,
    D_n=sum_(d|n) Lambda(d)[s(x+log d)/s(x)-1].                 (1)

All three pieces are nonnegative for x>0. The full-band identity is
T a=beta. Let h_n=w(x,n)-u(x), so T h=0, and put

    R_a(x)=T[a|h|^2], eps(x)=(1-p_1)/p_1.

**Theorem.** Uniformly for x>0,

    a_n>a_1 for n>=2,
    T[1_(n>=2)a_n] < beta/50,
    T[(a-a_1)^2/a] < beta/50.                                (2)

Consequently the complete centered forcing satisfies

    |T[a(w-u)]|^2 <= beta R_a/50.                            (3)

This applies to complex or Hilbert-valued currents. In particular the exact
first-label drift equation retains the forcing T[a(w-u)], but controls it
with a coefficient strictly below 1/50 of the SAME reset square. Multiplying
(3) by psi(x)^2/beta(x) and integrating pays its entire weighted L2 dual
norm by (1/50)int psi^2 R_a. That reset square must not be spent again as an
independent free gain.

## 1. Tail labels have larger reset rate than label one

The complete score inequality s'-2s>3 gives, for d>=0,

    s(x+d)>exp(2d)s(x)+(3/2)[exp(2d)-1].                       (4)

Every n>=2 has a prime divisor p>=2. Its divisor term alone gives

    a_n>=log(2)[s(x+log2)/s(x)-1]
        >log(2)[3+9/(2s(x))].                                (5)

The s denominator in (5) is essential. On the other hand positivity and
T a=beta imply a_1<=beta/p_1. Also

    (beta/p_1)s=K/(Phi p_1)
       =[3+Theta/(2Phi)]/p_1
       <=(3+1/36)(401/400)=43709/14400.                       (6)

Indeed Theta/Phi<=1/(4z^2-6z)<=1/18, because all positive theta summands
have n^2z>=z>3, and the previous Gamma note gives p_1>400/401.
Since log2>69/100,

    (9/2)log2>621/200>43709/14400.

Multiplying (5) by s and comparing (6) proves a_n>beta/p_1>=a_1.
The argument is on x>0; its operationally scaled version extends to the
honest entrance by the already established rate limits.

## 2. The full tail reset mass is paid by the exact prime row

The rational function beta_n decreases with n. Therefore

    T_tail beta_n <=(1-p_1)beta_1
                   =eps p_1 beta_1<=eps T beta_n.             (7)

The exact Gamma flux identity in (1), with p_n(x) eta_n(x+h)/eta_n(x)
replaced by Phi(x+h)p_n(x+h)/Phi(x), gives

    T_tail G_n
      =int kappa(h) Phi(x+h)/Phi(x)
           [s(x+h)/s(x)-1] [1-p_1(x+h)]dh
      <=eps(x) T G_n.                                       (8)

Here all tail coordinates decrease by the proved complete-posterior
monotonicity. No actual-source derivative is used. The divisor mean is

    T D_n
      =sum_(d>=2) alpha_d Phi(x+log d)/Phi(x)
                                [s(x+log d)/s(x)-1]
      <= F_+psi(x)/psi(x),
    F_+psi(x)=sum_(d>=2)alpha_d psi(x+log d).                  (9)

There is no divisor contribution at label one. Equations (7)-(9) and
T a=beta show

    T_tail a / beta <=eps(x)+F_+psi(x)/K(x).                  (10)

This is a grouped estimate for ALL continuous and prime-power reset
channels, not a truncation to a first-prime model.

## 3. Uniform all-prime row bound

Use theta_c and k(z)=exp(-x/2)K from the Gamma note. The exact forward prime
row is

    F_+psi/K=[sum_(d>=2)Lambda(d)theta_c(d^2 z)]/k(z).

Since c(q)=8q^3-30q^2+15q<=8q^3 for q>=3, and k(z)>=6z^2 exp(-z), the
COMPLETE divisor identity sum_(d|l)Lambda(d)=log l yields

    F_+psi/K
       <=(4/3)z sum_(l>=2)l^6 log(l)exp(-(l^2-1)z).            (11)

All true prime powers are included before this identity; none are assigned
independent signs or discarded. For z>=pi>3,

    sum_(l>=2)l^6 log(l)exp(-(l^2-1)z)
      <exp(-3z)[64(7/10)+sum_(l>=3)l^7 exp(-3(l^2-4))]
      <45 exp(-3z).                                         (12)

The tail in brackets is at most twice its first term 3^7 exp(-15), and
4374/2^15<1/5. Its successive ratio is below (4/3)^7 exp(-21)<1/2.
Thus (11) is at most 60z exp(-3z). The exact exponential lower bound from
the Gamma note is exp(471/50)>11200, so monotonicity of z exp(-3z) gives

    F_+psi/K <60(157/50)/11200<7/400.                         (13)

Together with eps<1/400, (10) proves T_tail a<beta/50.

Finally a_n>a_1 on every tail label implies

    (a_n-a_1)^2/a_n<=a_n, n>=2,
    (a_1-a_1)^2/a_1=0.

This proves the third bound in (2). Since T h=0, the forcing is EXACTLY
T[(a-a_1)h]. Weighted Cauchy--Schwarz with weight a proves (3), retaining
its full value and sign in the source equation.

No claim about Q_delta positivity, a neutral projection, or the sign of the
variance-transport term follows just from (3).
