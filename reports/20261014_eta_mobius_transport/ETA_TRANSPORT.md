# Exact eta Gamma transport row and centered divisor compensation

This note works on the positive half-line and with the genuine positive eta
lift of Phi. It proves an exact logarithmic coefficient match and retains the
rational, odd-reflection, mixed-transport, and Jensen terms. It does not assert
that their sum has a favorable sign. The Phi-ground expressions below are not
silently identified with the original psi-ground P,N forms; the full ground
change, pole, and terminal terms remain necessary in any application.

## 1. Positive integer fibers and their consistent star coupling

For x>=0 put z=pi exp(2x), P(z)=4z^2-6z, and

    eta_n(x)=exp(x/2) P(n^2 z)exp(-n^2 z),
    Phi(x)=sum_(n>=1)eta_n(x),   p_n(x)=eta_n(x)/Phi(x).

Thus eta_n=n^(-1/2)eta_1(x+log n). All these weights are positive on this
half-line. No positivity of eta_1 on the entire real line is used.

The weights p_n strictly decrease in x for n>=2, while p_1 increases.
Here is a short complete proof. Their logarithmic scores are

    s(w)=9/2+6/(2w-3)-2w,   p_n'/p_n=s(n^2 z)-E_p s(N^2 z).

With w_n=P(n^2 z)exp(-n^2 z),

    w_n/w_1 <=2 n^4 exp[-pi(n^2-1)].

The terms n>=3 obey

    sum_(n>=3)(n^2-4)w_n/w_1
       <=2 sum_(n>=3)n^6 2^[-3(n^2-1)]
       <=4*729/2^24 <1.

The last bound follows because the ratio of consecutive displayed terms is
at most `(4/3)^6 2^(-21)<1/2`. The n=1 term of the centered n^2 sum is -3,
and n=2 contributes zero. Hence E_p N^2<4. Strict convexity of
`u -> 1/(2zu-3)` gives `E_p s(N^2 z)>s(4z)`, and s is strictly decreasing.
This proves the assertions about p_n'.

For 0<=x<=y define the coupling pi_xy by

    pi(n,n)=p_n(y), n>=2;  pi(1,1)=p_1(x),
    pi(n,1)=p_n(x)-p_n(y), n>=2; all other entries zero.    (1)

Its marginals are p(x),p(y). These pairwise couplings are one consistent
inhomogeneous Markov process: state 1 is absorbing and a state n>=2 survives
from x to y with probability p_n(y)/p_n(x). The survival probabilities multiply.
This does NOT assert the stronger law obtained by conditioning both endpoints
on a common divisor and shifting x,y simultaneously; that law is not used here.

## 2. Exact finite Gamma mismatch rate

Write

    kappa(h)=exp(-h/2)/(1-exp(-2h)),
    R_w(h)=exp(9h/2) [1-3exp(-2h)/(2w)]/[1-3/(2w)]
                         *exp[-w(exp(2h)-1)],
    beta(w)=(2w-1/2)/(2w(w-3/2))=(4w-1)/P(w).

For w,z>3/2 an exact convergent integral is

    int_0^infinity kappa(h)[R_z(h)-R_w(h)]dh
        = (1/2)log(w/z)+beta(z)-beta(w).                 (2)

To prove it put u=exp(2h)-1 and a=3/(2z). The first summand becomes

    kappa(h)R_z(h)dh
      = [1/(2u)+(2-a)/(2(1-a))+u/(2(1-a))]exp(-zu)du.

The singular constants cancel in the difference. Frullani's elementary
integral gives half the logarithm; the other two elementary Laplace integrals
sum to beta(z). This proves (2) with all eta polynomial corrections retained.

For x>0 define

    T_n(x)=int_0^infinity kappa(2x+h)R_(n^2z)(h)dh,
    J_n(x)=int_0^infinity [kappa(h)-kappa(2x+h)]
                  [Phi(x+h)/Phi(x)-R_(n^2z)(h)]dh.       (3)

Then the COMPLETE odd-Gamma row is

    J_n=log n-E_p log N + E_p beta(N^2z)-beta(n^2z)
                         +T_n-E_p T_N.                 (4)

Normal convergence of the theta sums, including their local first derivatives,
justifies averaging (2) and subtracting the finite odd-reflection integrals.
In particular `E_p J_N=0`. The monotonicity proved above gives J_n>=0 for n>=2.
The negative n=1 mean compensation must not be discarded.

For an entirely explicit odd-reflection term put q=exp(-4x), a=3/(2w),
b=1-q and E1(t)=int_t^infinity exp(-u)du/u. For x>0,

    T(w;x)=exp(-x)/(2(1-a)) * [1/w^2+(1+q-a)/w
                   +q(q-a)exp(wb)E1(wb)],
    T_n(x)=T(n^2z;x).                                   (5)

This follows from the same substitution and polynomial division of
`[(1+u)^2-a(1+u)]/(1+u-q)`. At x=0 the individual T_n diverge. Only the
grouped differences in (4) have a finite limit there; define them directly by

    T_n-E_p T_N = int_0^infinity kappa(2x+h)
           [R_(n^2z)(h)-sum_m p_m(x)R_(m^2z)(h)]dh.

The bracket vanishes linearly at h=0, and Gaussian index moments pay its
coefficient. This definition is also finite at x=0. The original kernel gives
J_n(0)=0. No separate infinite T_n value is assigned at the origin.

## 3. The correction has a genuine theta primitive

Let

    Theta(x)=exp(x/2)sum_(n>=1)exp[-pi n^2 exp(2x)].

Then, on x>=0,

    eta_n(x) beta(n^2z)
      =-2 d/dx {exp(x/2)exp[-pi n^2exp(2x)]},
    Phi(x) E_p beta(N^2z)=-2Theta'(x),
    Phi(x) E_p T_N(x)=int_x^infinity kappa(x+y)Phi(y)dy.  (6)

Poisson's theta relation yields

    Theta(-x)=Theta(x)+sinh(x/2),  Theta'(0)=-1/4.        (7)

Thus the rational and odd-reflection averages in (4) have explicit whole-theta
and terminal representatives. They are not unspecified error bounds. Neither
(6) nor (7) alone identifies them with the full source pole energy.

## 4. Exact centered quadratic identity, with both mixed terms retained

Take one real latent field v on the positive half-line and set

    Z_n(x)=v(x+log n),
    u(x)=E_p Z_N(x),   H_n(x)=Z_n(x)-u(x),
    V(x)=E_p H_N(x)^2.

The actual-source application is v=f/eta_1 with the genuine unanchored future
inverse f=M g, so g=Phi u. The fields then obey the exact compatibility
`Z_n(x+log d)=Z_(dn)(x)`. No constant Gaussian coefficient replacement occurs.
The identities below hold first with bounded smooth latent data and convergent
cutoff integrals; passing to actual data requires the established latent second-
moment/form bounds, not independent subtraction of divergent terms.

Put K(x,y)=kappa(|x-y|)-kappa(x+y), W(x,y)=Phi(x)Phi(y)K(x,y). Define

    G_Phi[u]=2 int_(x<y) W(x,y)|u(x)-u(y)|^2 dxdy,
    G_star=2 int_(x<y) W sum_(n,m)pi_xy(n,m)
                                      |Z_n(x)-Z_m(y)|^2 dxdy,
    G_diag=2 int_(x<y) W sum_n p_n(y)|Z_n(x)-Z_n(y)|^2 dxdy,
    M_xy=sum_n[p_n(x)-p_n(y)]H_n(x),
    Mix=4 int_(x<y) W[u(x)-Z_1(y)]M_xy dxdy.

The Jensen defect D_J=G_star-G_Phi is nonnegative, with the exact expression

    D_J=2 int_(x<y)W Var_(pi_xy)[Z_N(x)-Z_M(y)]dxdy.      (8)

Expanding the star transfers in (1), centered at the TRUE fiber mean u(x), gives

    G_Phi[u]=G_diag+2 int_0^infinity Phi(x)^2
                         E_p[J_N(x)H_N(x)^2]dx+Mix-D_J. (9)

For clarity, the pointwise transfer difference relative to G_diag is

    sum_(n>=2)[p_n(x)-p_n(y)]
       {H_n(x)^2-H_1(x)^2
          +2[u(x)-Z_1(y)][H_n(x)-H_1(x)]}.

The first terms integrate using (3); `E_p J=0` incorporates the n=1
compensation exactly. This proves (9). The mixed term and the negative Jensen
defect in (9) have NOT been dropped or assigned a favorable sign.

## 5. Exact cancellation with the divisor-variance term

Let `P_d(x)=sum_(d|n)p_n(x)=d^(-1/2)Phi(x+log d)/Phi(x)` and V_d be the
conditional variance of Z_N(x) given d|N. The complete forward-prime Phi form is

    F_Phi[u]=2 sum_(d>=2) Lambda(d)/sqrt(d)
       int_0^infinity Phi(x)Phi(x+log d)|u(x)-u(x+log d)|^2dx.

Conditional expectation and `sum_(d|n)Lambda(d)=log n` give exactly

    F_Phi[u]=2 int Phi^2 [E_p(log N H_N^2)
                                    -sum_d Lambda(d)P_d V_d]dx. (10)

Using (4), the row in (9) minus the density in (10) is exactly

    sum_d Lambda(d)P_d(V_d-V)
                  +Cov_p(T_N-beta(N^2z),H_N^2).          (11)

Here `sum_d Lambda(d)P_d=E_p log N`; there is no coefficient loss in the
logarithmic term. Combining (9)-(11) yields the full candidate identity

    G_Phi[u]-F_Phi[u]
       =G_diag+2 int Phi^2 {sum_d Lambda(d)P_d(V_d-V)
                 +Cov_p(T_N-beta(N^2z),H_N^2)}dx
          +Mix-D_J.                                    (12)

Equation (12) is an EXACT SIGNED identity, not a positivity assertion. It
retains the full centering, conditional variances, rational correction,
odd-reflection correction, mixed transport, and Jensen defect.

For the SAME translated latent field, V_d(x)=V(x+log d). Also
`Phi E_p log N=F_+Phi`, where `F_+Phi=sum_d Lambda(d)/sqrt(d) Phi(x+log d)`.
Changing variables in the first term of (11) therefore gives the further exact
complete-prime identity

    2 int Phi^2 sum_d Lambda(d)P_d(V_d-V)dx
       =2 int_0^infinity Phi(x)V(x)
                         [F_-^+Phi(x)-F_+Phi(x)]dx,      (13)

where `F_-^+Phi(x)=sum_(log d<x)Lambda(d)/sqrt(d)Phi(x-log d)`.
The reflected labels log d>x are NOT part of F_-^+ and are not silently added.
They, the original pole, and the Phi-to-psi ground change must be retained in
any proposed deduction about the original signed P-N form. A nonnegative
completion of those remaining terms is still open.

## 6. Complete original-source application

The actual-source integration and complete reflected, archimedean-wall, mass, and pole terms are proved in [REPORT.md](REPORT.md). The independent full Gamma-domain argument is [DOMAIN.md](DOMAIN.md). Neither this transport identity nor the positive coupling is asserted to sign the full source form.
