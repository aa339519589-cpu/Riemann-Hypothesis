# Exact conditional-variance star reduction on the safe xi ray

This note concerns the hidden component G_tail-D_div only. It retains the
constant latent null direction and does not prove this component is positive.
In particular it does not remove the transport, odd-boundary, reflected-prime,
or pole terms in the original source identity.

## 1. Forms and the exact star identity

Put b=log 2, z(y)=pi exp(2y), c(z)=8z^3-30z^2+15z, and
xi(y)=exp(y/2-z(y))c(z(y)). Thus xi>0 for y>=b. Define

    W(y)=sum_(2<=n<=exp y) n^(-1/2) psi(y-log n),
    L(y)=sum_(2<=n<=exp y) (log n)n^(-1/2) psi(y-log n),
    W_Lambda(y)=sum_(2<=d<=exp y) Lambda(d)d^(-1/2)psi(y-log d).

The complete theta identity psi(y)=sum_(m>=1)m^(-1/2)xi(y+log m)
gives the probability law

    q_m(y)=m^(-1/2)xi(y+log m)/psi(y), m>=1.

For a real latent field a on [b,infinity), put
R(y)=sum q_m(y)a(y+log m). The complete divisor form is

    D_div[a]=2 integral_b^infinity W_Lambda(y)psi(y)
                               Var_(q(y))(a(y+log m))dy.

Define the genuinely centered star form

    D_star[a]=2 integral_b^infinity W_Lambda(y)
       sum_(m>=2)m^(-1/2)xi(y+log m)[a(y)-a(y+log m)]^2dy.

The variance identity about the label m=1 gives exactly

    D_star-D_div=2 integral W_Lambda psi [R(y)-a(y)]^2dy >=0. (1)

Thus both forms vanish on constant a. Equation (1), rather than deletion
of the conditional mean, is the basis of the estimate below.

## 2. Exact arithmetic diagonal after the ground normalization

Let H(y)=sqrt(W(y)xi(y))a(y) and define

    R_prop(y)=L(y)-W_Lambda(y),
    O(y)=[W_Lambda(y)/W(y)] [psi(y)-xi(y)]/xi(y),
    c_m(y)=[W_Lambda(y)/W(y)]m^(-1/2)
           sqrt(W(y)/W(y+log m))sqrt(xi(y+log m)/xi(y)).

Collecting d*m=n with d>=2 and m>=2 gives

    R_prop(y)=sum_(4<=n<=exp y)(log n-Lambda(n))
                                      n^(-1/2)psi(y-log n). (2)

In particular R_prop>=0 and is identically zero below log 4. Direct
expansion of the nonnegative star squares gives

    D_star[a]=2 integral [R_prop/W+O]H^2
                  -4 sum_(m>=2) integral_b^infinity
                                      c_m(y)H(y)H(y+log m)dy. (3)

For example, the incoming diagonal is R_prop/W, not L/W: the missing
Lambda(n) is precisely the label m=1 which disappeared in (1).
All identities hold first on compactly supported H inside (b,infinity).

## 3. Complete-row bounds with explicit rational constants

For every integer m>=2, inclusion of the labels mn in W(y+log m) gives

    W(y+log m)>=m^(-1/2)W(y).                            (4)

Also W_Lambda/W<=y. For z>=4pi>12 one has
c(z)>=4z^3 and c(m^2z)<=8m^6z^3. Consequently

    xi(y+log m)/xi(y)<=2m^(13/2)exp[-(m^2-1)z],
    c_m(y)<=sqrt(2)y m^3 exp[-(m^2-1)z/2].             (5)

For m>=2 the ratio of successive terms m^3 exp[-(m^2-1)z/2]
is at most (3/2)^3 exp(-30)<1/2. Hence the forward row satisfies

    C_f(y):=sum_(m>=2)c_m(y)
       <=16sqrt(2)y exp(-3z/2)
       <=16sqrt(2)(log 2)exp(-6pi)<24/20^6.             (6)

Here and below we use only sqrt(2)<3/2, log 2<1, log 4<3/2,
pi>3, and exp(3)>20. The function y exp(-3z(y)/2) decreases for y>=b.

For the incoming row C_i(t)=sum_(2<=m<=exp(t-b))c_m(t-log m),
there is no contribution when t<log 4. Otherwise, writing Z=pi exp(2t)
and N=exp(t-b), (5) gives

    C_i(t)<=sqrt(2)t exp(-3Z/8)sum_(2<=m<=N)m^3
       <=sqrt(2)t [Z^2/(16pi^2)]exp(-3Z/8).

The last expression decreases for t>=log 4: its logarithmic derivative
is 1/t+4-3Z/4<0. Its value at log 4 therefore gives

    C_i(t)<=16sqrt(2)(log 4)exp(-6pi)<36/20^6.           (7)

Similarly the successive ratio of m^6 exp[-(m^2-1)z] is below 1/2, so

    [psi(y)-xi(y)]/xi(y)<=256exp(-3z),
    O(y)<=256y exp(-3z)<=256(log 2)exp(-12pi)<256/20^12. (8)

Combining (6)-(8) gives the entirely rational strict inequality

    sup O + sup C_f + sup C_i
       <256/20^12+60/20^6 <1/1000000.                  (9)

No prime tail or integer label has been omitted in these estimates.

## 4. Bounded residual and improved lower potential

The inequality 2|H(y)H(t)|<=H(y)^2+H(t)^2, followed by the exact
incoming change of variable, gives

    |D_star[a]-2 integral (R_prop/W)H^2|
       <=2 integral O H^2
          +2 integral (C_f+C_i)H^2
       <(2/1000000)||H||_2^2.                          (10)

Thus, in particular,

    D_div[a]<=2 integral [(L-W_Lambda)/W]H^2
                                  +(2/1000000)||H||_2^2. (11)

Equation (10) is a bounded-operator estimate for the star remainder, not
for D_div minus that diagonal: their difference still includes the full
nonnegative square (1). The mixed star term need not itself be positive.

With the exact Gamma ground expansion from
SAFE_RAY_FORMS.md, put

    V_1=V_Gamma-2(L-W_Lambda)/W.

Then the safe hidden form obeys

    G_tail-D_div >=2 integral_(y<t)J(y,t)[H(y)-H(t)]^2dydt
                    +integral [V_1-2/1000000]H^2.      (12)

Compared with the earlier uncentered potential V_0, this adds the exact
positive function 2W_Lambda/W. On b<y<log 4, V_1=V_Gamma.
This removes a spurious first-label diagonal globally; it does not assert
that V_1 has a positive sign in the compact head.

The bounded residual in (10) extends to every H in L2. The multiplication
term is interpreted on its natural domain; R_prop/W<=y. On the actual
common-seed class, a is bounded with the established weighted Sobolev
control and W xi has a theta tail, so integral yH^2 is finite. Tonelli
applies to the nonnegative conditional and star forms, and (3) extends
by common compact cutoffs using (9)-(10). The Gamma lower bound then
passes by the already-established common-cutoff domain argument. These
steps neither place an unbounded auxiliary ground function in the
original P domain nor change the actual source.

Finally, constant a remains a decisive test: D_star=D_div=G_tail=0.
Any eventual head/tail sign certificate must preserve that null direction
and the full mixed block; (12) alone is not such a certificate.
