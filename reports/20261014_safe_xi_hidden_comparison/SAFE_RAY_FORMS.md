# Safe xi-ray forms and exact Gamma ground transform

The comparison studied here is the hidden positive-tail inequality
G_tail >= D_div from the division-free dynamic xi completion. It is not the
full reflected Weil inequality. This note records the exact scalar Gamma primitive and ground transform used
in the global comparison in REPORT.md.

## 1. Exact safe-ray primitive

Put P(z)=4z^2-6z, c(z)=8z^3-30z^2+15z, B(x)=exp(x/2-pi exp(2x)),
and xi(x)=B(x)c(pi exp(2x)). On x>=b=log2, xi is strictly positive.
For z,w>=4pi define

    R_c,z(h)=exp(h/2)c(z exp(2h))/c(z)
                                      *exp[-z(exp(2h)-1)],
    beta_xi(z)=(3P(z)+1/2)/c(z).

Then the absolutely grouped integral is

    integral_0^infinity kappa(h)[R_c,z(h)-R_c,w(h)]dh
       =(1/2)log(w/z)+beta_xi(z)-beta_xi(w).              (1)

Indeed u=exp(2h)-1 changes the individual integrand to
c(z(1+u))exp(-zu)/(2u c(z)). The constant coefficients cancel, Frullani
pays the logarithm, and the three remaining monomials give

    beta_xi(z)=(24z^2-36z+1)/(2c(z)).

Writing r_+=(15+sqrt(105))/8 and r_-=(15-sqrt(105))/8 yields the positive
Stieltjes decomposition

    beta_xi(z)=1/(30z)
       +(11/15+sqrt(105)/42)/(z-r_+)
       +(11/15-sqrt(105)/42)/(z-r_-).                    (2)

Thus beta_xi is positive and decreasing on every safe ray. Crucially,

    C(xi beta_xi)=3Phi+Theta/2,
    E_(q^xi(x)) beta_xi(N^2z)=(3Phi+Theta/2)/psi,        (3)

where the conditional law q^xi is positive when x>=b. This is the exact
original future potential, not the eta-ground rational correction.

## 2. The complete hidden forms after collecting the starting labels

Let a(y)=phi(y)/xi(y) for y>=b, with phi=Mf the true common seed. Define

    W(y)=sum_(2<=n<=exp y)n^(-1/2)psi(y-log n),
    L(y)=sum_(2<=n<=exp y)(log n)n^(-1/2)psi(y-log n),
    W_Lambda(y)=sum_(2<=d<=exp y)alpha_d psi(y-log d).

The endpoints contribute zero because psi(0)=0. All W,L are positive for
y>b, and W is continuous, locally Lipschitz and piecewise smooth. The exact
positive Gamma tail form is

    G_tail[a]=2 integral_(b<y<t) W(y)xi(t)kappa(t-y)
                                                  [a(y)-a(t)]^2 dydt. (4)

For y>=b put q_m(y)=m^(-1/2)xi(y+log m)/psi(y), a_m=a(y+log m), and
R(y)=E_q a_m. Then

    D_div[a]=2 integral_b^infinity W_Lambda(y)psi(y)
                                                   Var_q(a_m)dy
       =2 integral_b^infinity L(y)xi(y)a(y)^2dy
          -2 integral_b^infinity W_Lambda(y)psi(y)R(y)^2dy.       (5)

The first equality is the complete conditional variance. For the second,
collect d*m=n and use sum_(d|n)Lambda(d)=log n. In particular the upper
estimate by the first diagonal is NOT an equality and cannot itself be
paid globally by G_tail: constant a has G_tail=D_div=0 but a positive
uncentered diagonal. We use the diagonal only for a lower reduction
which explicitly permits a negative compact head.

## 3. An exact positive-ground lower reduction

Set m(y)=W(y)xi(y), H(y)=sqrt(m(y))a(y), and

    J(y,t)=kappa(t-y)sqrt[W(y)xi(t)/(xi(y)W(t))], y<t.

Define the finite scalar row

    V_Gamma(y)=2 integral_0^infinity kappa(h)
       {xi(y+h)/xi(y)-sqrt[W(y)xi(y+h)/(xi(y)W(y+h))]}dh
      +2 integral_0^(y-b) kappa(h)
       {W(y-h)/W(y)-sqrt[W(y-h)xi(y)/(W(y)xi(y-h))]}dh,
    V_0(y)=V_Gamma(y)-2L(y)/W(y).                       (6)

For compactly supported smooth H in (b,infinity), direct square expansion
with common separation cutoffs gives

    G_tail[a]=2 integral_(y<t)J(y,t)[H(y)-H(t)]^2dydt
                       +integral_b^infinity V_Gamma(y)H(y)^2dy.

Together with (5), this gives the exact formula

    G_tail-D_div
       =2 integral_(y<t)J(y,t)[H(y)-H(t)]^2dydt
          +integral V_0 H^2
          +2 integral W_Lambda psi R^2.                (7)

The last positive square is retained. Dropping it is permissible only for
a lower bound, not for deciding the sign of the compact head.

The comparison function m^(-1/2) is not asserted to lie in the original
P domain. It is used only to expand (4). Its rows in (6) are finite:
near h=0 their brackets vanish at least linearly, also at one-sided
integer knots; at infinity the future terms have a theta tail; at y-h=b
the incoming square root is O(sqrt(y-h-b)). These observations justify
(7) on the indicated core without an unproved ground-state boundary term.
The completed-domain passage used in the global theorem is the capped
absolute-row argument in REPORT.md and CAPPED_COMPLETION.md. No original-P
membership of the comparison function is used.

