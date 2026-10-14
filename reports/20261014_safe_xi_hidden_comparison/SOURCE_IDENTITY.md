# Division-free dynamic xi-tail completion of the full Gamma/prime form

This identity uses the same actual source and matches the complete prime
conditional-variance coefficient to the Gamma source evolution. All seed
quotients are evaluated beyond log 2, where xi is positive. The missing
first label is retained in a finite, generally signed transport defect.
No positivity of that defect, invariant original metric, or RH conclusion
is asserted.

## 1. Source evolution and the positive shifted tail

Keep f=g-r_0 psi, phi=Mf, Cphi=f from
[the positive divisor budget](DIVISOR_PALM.md).
The changed pole moment of f is retained throughout. Let

    D0=L_+-X-C0/2,     D=D0-F_+,
    C0=log pi-digamma(1/4),   (Xu)(x)=x u(x),
    L_+a(x)=integral_0^infinity kappa(h)[a(x)-a(x+h)]dh,
    F_+a(x)=sum_d alpha_d a(x+log d).

The published source intertwinings give DC=CD0. Use the source evolutions

    phi_t=S0_t phi,    xi_t=S0_t xi,
    f_t=Cphi_t=S_t f,  psi_t=Cxi_t=S_t psi.

Thus partial_t phi_t=-D0 phi_t and partial_t f_t=-D f_t, and the same
relations hold for xi_t and psi_t. Write

    R_t=f_t/psi_t,
    b_(t,n)(x)=n^(-1/2)xi_t(x+log n),
    a_(t,n)(x)=phi_t(x+log n)/xi_t(x+log n), n>=2.

For every t>=0, x>=0, n>=2, b_(t,n)>0. In Gaussian coordinates
z=pi exp(2x), xi_t=B c_t with

    c_t(z)=8z^3-30z^2+15z
                +t(3(4z^2-6z)+1/2)+t^2(6z-3/2)+t^3.

Every displayed summand is positive for z>=4pi. Also psi_t>0 for x>0;
for t>0 it is positive at x=0 as well. This does not assert xi_t(x)>0
on its unshifted first band.

Define the finite tail quadratic and its defect

    Q_t(x)=sum_(n>=2)b_(t,n)(x)a_(t,n)(x)^2,
    H_t(x)=f_t(x)^2/psi_t(x),   E_t=Q_t-H_t.             (1)

At t=0, H_0=psi R^2 is defined by its zero trace at x=0. No unshifted
phi_t^2/xi_t is introduced.

For a positive ground w on a future ray set

    G_w u(x)=integral kappa(h)w(x+h)/w(x)
                                             [u(x)-u(x+h)]dh,
    Gamma_G(u)=2uGu-G(u^2).

The observed G_(psi_t) additionally has every prime jump with rate
alpha_d psi_t(x+log d)/psi_t(x). Put

    Gamma_tail,t(x)=sum_(n>=2)n^(-1/2)xi_t(x+log n)
                  Gamma_(G_(xi_t))(phi_t/xi_t)(x+log n),

where the inner generator is PURE Gamma and only uses future points
beyond log 2. Thus Gamma_tail,t>=0. Finally let

    V_div,t(x)=sum_d alpha_d psi_t(x+log d) Var_(t,d)(a;x), (2)

with the positive divisor conditional law of the companion note, now
using xi_t. All prime powers and their common-seed compatibility remain.

## 2. Exact dynamic coefficient-one identity

For x>0, with right differentiation at t=0, one has

    psi_t Gamma_(G_(psi_t))(R_t)
       =Gamma_tail,t+(partial_t+D0)E_t-V_div,t.          (3)

Here D0 acts on E_t as a SOURCE operator. E_t is not treated as a
nonnegative variance, and psi_t is not replaced by the original psi
metric at positive t.

Proof. A translated base source u_t(x+log n) obeys

    partial_t u_t(x+log n)=-D0[u_t(.+log n)](x)
                                  +(log n)u_t(x+log n),

because [D0,tau_(log n)]=(log n)tau_(log n). The source product identity

    2a D0(wa)-a^2 D0w-D0(wa^2)=w Gamma_(G_w)(a)

therefore gives, after summing the POSITIVE tail,

    (partial_t+D0)Q_t
       =sum_(n>=2)(log n)b_(t,n)a_(t,n)^2-Gamma_tail,t.  (4)

Both f_t and psi_t solve the same observed source equation, so

    (partial_t+D0)H_t=F_+H_t
                                 -psi_t Gamma_(G_(psi_t))(R_t). (5)

The exact divisor/Palm identity with c=0 is

    sum_(n>=2)(log n)b_(t,n)a_(t,n)^2
                              =F_+H_t+V_div,t.         (6)

Subtracting (5) from (4) and using (6) proves (3). In particular the
arithmetic coefficient is exactly one; there is no diagonal prime sum
removed without its conditional variance.

There is also exact constant-null gauge invariance. Replacing f by
f+c psi replaces phi_t by phi_t+c xi_t and gives

    E_t -> E_t-2c phi_t-c^2 xi_t.

Since phi_t and xi_t solve the D0 source equation, (partial_t+D0)E_t
is UNCHANGED. Gamma_tail,t and V_div,t are unchanged as well. This
checks the known constant-ratio null direction without dividing by xi_1.

## 3. The original integrated form, with its full wall and pole

All objects in the rest of the note are evaluated at t=0. Define

    G_tail=2 integral_0^infinity psi(x)Gamma_tail,0(x)dx,
    T_E=2 integral_0^infinity psi(x)[E_dot(x)+D0E(x)]dx,
    D_div=2 integral_0^infinity psi(x)V_div,0(x)dx,

where E_dot is the fixed-x right source derivative in (3). Let

    P_Gamma^future[R]
       =2 integral_(0<x<y) kappa(y-x)psi(x)psi(y)
                                            [R(x)-R(y)]^2 dxdy,
    H_Gamma^diff[R]
       =integral_(x,y>0) kappa(x+y)psi(x)psi(y)
                                            [R(x)-R(y)]^2 dxdy.

The original odd Gamma energy is
P_Gamma=P_Gamma^future-H_Gamma^diff. Integrating (3) against 2psi gives

    P_Gamma^future[R]+P_F[R]=G_tail+T_E-D_div.           (7)

Consequently the COMPLETE original source form is

    h[f]=G_tail+T_E-D_div-H_Gamma^diff[R]
                             +P_pole[R]-N[R],         (8)

    P_pole[R]=integral sinh(x/2) f(x)^2/psi(x)dx
                              -8 ell(f)^2,
    ell(f)=integral sinh(x/2)f(x)dx,
    N[R]=2 integral [L(x)/psi(x)]f(x)^2 dx-2<f,F_r f>.

Thus (8) cancels the original future prime energy EXACTLY once. One must
not independently spend P_F in a different inequality after replacing its
occurrence by (7). All of D_div, the odd Gamma wall, the complete reflected
prime term, and the CHANGED pole of f are retained. Only G_tail is asserted
nonnegative in (8); T_E has no sign established.

## 4. Honest paired adjoint and the finite omitted-label defect

The transport can be displayed without a claim about an operator-adjoint
domain. With common Gamma cutoffs first, paired Fubini gives

    T_E=2 integral psi E_dot+2 integral E D0^dagger psi,  (9)

    D0^dagger psi(x)
       =integral_0^x kappa(h)[psi(x)-psi(x-h)]dh
        +psi(x)integral_x^infinity kappa(h)dh
        -(x+C0/2)psi(x).

An equivalent expression from the COMPLETE odd source identity
T psi=sinh(x/2)/2 is

    D0^dagger psi
       =sinh(x/2)/2+(3Phi+Theta/2)-2x psi
                    -H_kappa psi-F_r psi+F_-^+psi,     (10)

    H_kappa psi(x)=integral_0^infinity kappa(x+y)psi(y)dy.

All these terms are paired with the theta-tailed E; no divergent backward
Theta row is used. Formula (10) retains the full reflected row F_r psi=L.
It also shows why a positive value of E at the origin is not an automatic
positive transport boundary term: D0^dagger psi tends to zero at x=0.
Indeed 3Phi(0)+Theta(0)/2=H_kappa psi(0)+L_0.

For the actual fixed origin anchoring, R(0)=0 and

    E(0)=Q(0)=sum_(n>=2)n^(-1/2)phi(log n)^2/xi(log n)>=0. (11)

The actual two-moment wall gap controls this tail together with the first
seed sample, but (11) is not substituted for the full integral (9).
For example f=c psi gives E_t=-c^2 xi_t and the transport is identically
zero, despite E(0)>0 when c is nonzero. The actual anchoring removes that
particular null source but does not authorize omitting (9).

## 5. Domain and the time-zero boundary distinction

For the actual source R is bounded and constant-plus-H^s for every s<1.
On u>=log2 the future inverse gives phi(u)/xi(u) bounded, with weighted
H^s and Holder estimates. The shifted seed xi is comparable to psi there,
and all integer coefficients and their fixed derivatives have Gaussian
index tails. The same holds on compact positive time intervals for
phi_t,xi_t, using their explicit Gamma-addition source kernel.

Hence the sums Q_t and Gamma_tail,t converge absolutely. Near a Gamma
increment h=0, every squared multiplier difference is bounded in an
integrated H^s seminorm, or locally by h^(2alpha) for some alpha>0;
this pays kappa(h)~1/(2h). For h>=1 the bounded ratios and theta weights
suffice. The complete shifted-label tails are summable. All terms in
(7)-(9) are finite: Q and its source derivative have theta tails; H=psi R^2
and its fixed-x derivative have the same weighted regularity; the original
Gamma, pole and N terms are finite by the actual source theorem.

More explicitly the pointwise derivative used above is

    E_dot=Q_dot+2R Df-R^2 Dpsi.                        (12)

It is locally integrable against psi and theta-controlled at infinity.
Near zero the actual anchoring gives R(x)=O(x^alpha), while Df and Dpsi
have finite traces, so the last two terms in (12) vanish at the origin.
Common compact spatial, label, and Gamma cutoffs prove the product rules;
the stated actual Holder/weighted Sobolev estimates and theta bounds
remove them. Formula (9) follows by the same paired cutoff passage.

There is a nonuniform trace issue which (3) does not conceal. Generally
f_t(0)=O(t), psi_t(0)~t[3Phi(0)+Theta(0)/2], so R_t(0) need not tend to
R(0). The derivative E_dot in (3), (7), and (12) is the derivative at
FIXED x>0 followed by its integrable extension, not an asserted derivative
of the separate time-zero trace. Nor is R_t asserted to be an evolution
contractive in the fixed original P metric. The identity evaluates its
full signed defect instead of importing either assertion.
