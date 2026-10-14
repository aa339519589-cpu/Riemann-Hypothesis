# A capped Lyapunov completion of the hidden xi comparison

The cap and global constant projection below complete the comparison once
three explicit scalar inequalities are inserted. Those inequalities are proved
in HEAD_SCALAR.md, BULK_COMPACT.md and BULK_RHO.md; the integrated theorem
and its full original-source limitation are in REPORT.md.

Use b=log2, Y=b+31/100, m=W xi, and V_Gamma,V_1 from the exact safe-ray
Gamma and divisor-star notes. The positive Gamma generator in L2(m) is

    L_Gamma a(y)=2 integral_(t>y) kappa(t-y)xi(t)/xi(y)[a(y)-a(t)]dt
               +2 integral_(b<t<y)kappa(y-t)W(t)/W(y)[a(y)-a(t)]dt.

It satisfies G_tail[a]=<a,L_Gamma a>_(L2(m)). Define

    epsilon=10^(-6), K=1000,
    k(y)=min(m(y)^(-1/2),K) for b<y<=Y,
    k(y)=m(y)^(-1/2) for y>=Y,
    h(y)=1+epsilon k(y),
    rho(y)=epsilon/(sqrt(m(y))+epsilon).

## 1. The cap is confined to a tiny left collar

The certified head concavity gives psi(s)>=s psi(.31)/.31>6s on 0<s<=.31.
The separate outward endpoint checker certify_xi_lyapunov_cap.py proves

    psi(.31)>2, xi(b+.31)>10^(-5),
    xi(b+.03)>.03, xi(b+.0001)>1/20.                    (1)

The xi score is strictly negative on this safe ray. Hence on
.03<=s<=.31 one has m(b+s)>4s*10^(-5)>=1.2*10^(-6).
On .0001<=s<=.03 one has m(b+s)>.12s>=1.2*10^(-5).
Thus the cap set {y<=Y:m(y)<10^(-6)} lies inside (b,b+.0001).
The same endpoint checker gives psi'(0)<17 and xi(b)<1/10. Concavity
and decreasing xi then yield m(b+s)<1.7s, so the cap contains
0<s<=5*10^(-7). The pending head scalar check therefore needs only the
compact interval 5*10^(-7)<=s<=.31, not a limit at the singular endpoint.
In particular k agrees continuously with m^(-1/2) near Y and

    1<=h<=1001/1000 on the entire head (b,Y).           (2)

At every point outside the cap, reducing the comparison function on the
left can only increase its positive-generator value. Since
L_Gamma(m^(-1/2))=V_Gamma m^(-1/2), this gives

    L_Gamma h/h >= rho V_Gamma                         (3)

there, including all y>=Y. This is an exact row comparison, not an
L2-domain assertion about the unbounded auxiliary comparison function.

## 2. The complete cap row is harmless

Inside the cap, k=K and k<=K on the entire head. Therefore only t>Y can
contribute negatively to L_Gamma k, and

    L_Gamma k(y)>=-(2/xi(y)) integral_Y^infinity
                                      kappa(t-y)sqrt(xi(t)/W(t))dt. (4)

For t>=Y, the n=2 summand gives W(t)>=xi(t-b)/sqrt2, because
psi(t-b)>=xi(t-b)>0. With z=pi exp(2t), one has z/4>=5 and
c(z/4)>=2(z/4)^3, c(z)<=8z^3. Consequently

    sqrt(xi(t)/W(t))<=sqrt(512)exp(-3z/8)<23exp(-3z/8).

Moreover z(Y)>20, t-y>.3, kappa(t-y)<3, and xi(y)>1/20 by (1).
Since z'=2z,

    integral_Y^infinity exp(-3z(t)/8)dt
       <=exp(-3z(Y)/8)/[(3/4)z(Y)] <1/(400*15).

Here exp(3)>20 gives exp(7.5)>400. Substitution in (4) yields

    L_Gamma k(y)>-40*3*23/(400*15)>-1,
    L_Gamma h(y)/h(y)>-10^(-6)                         (5)

throughout the cap. All future labels and Gamma jumps remain present.

## 3. The certified scalar inequalities

The following explicit scalar inputs suffice for the entire hidden sign:

    V_Gamma(y)>=-100sqrt(m(y)),            head outside cap;        (A)
    rho(y)V_Gamma(y)>=10^(-5),             Y<=y<=log4;  (B)
    V_1(y)-(1-rho(y))V_Gamma(y)>=10^(-5),   y>=log4.    (C)

Their uniform certificates are supplied by the three notes cited above. In (B) the proper
arithmetic diagonal is identically zero; in (C) it is retained exactly.
Equations (3)-(5), together with (A)-(C), give

    L_Gamma h/h -2(L-W_Lambda)/W
       >=-10^(-4) on the head,
       >=10^(-5) outside the head.                     (6)

## 4. Exact global constant projection and mixed-block completion

For an arbitrary real latent a, subtract the unique constant c for which

    integral_b^Y m(y)[a(y)-c]/h(y)dy=0.

Both G_tail and D_star are unchanged by this global constant subtraction.
Write a_0=a-c and v=a_0/h. The positive ground identity gives exactly

    G_tail[a_0]=2 integral_(y<t)W(y)xi(t)kappa(t-y)
                               h(y)h(t)[v(y)-v(t)]^2dydt
                     +integral (L_Gamma h/h)m a_0^2.    (7)

The first term retains every mixed head/tail edge. Dropping only its
nonnegative edges outside the head, using h>=1, the certified head gap,
and the chosen mean gives

    first term >=(3/4000) integral_b^Y m v^2
       >=[3/(4000*(1001/1000)^2)] integral_b^Y m a_0^2. (8)

The audited divisor-star residual is less than 2*10^(-6)||a_0||_(L2(m))^2.
Combining (6)-(8) therefore proves

    G_tail[a]-D_div[a] >=G_tail[a]-D_star[a]
       >=[3/(4000*(1001/1000)^2)-102/10^6]
                                         integral_b^Y m(a-c)^2
                           +(8/10^6) integral_Y^infinity m(a-c)^2. (9)

Both coefficients are strictly positive. This is a full constant-projected
comparison, not a claim that the uncentered head potential is positive.

The ground identity is valid directly for finite-Gamma fields with
integral(1+y)m a_0^2 finite. Indeed the absolute grouped row
integral rate(y,t)|1-h(t)/h(y)| is bounded on the capped origin collar,
locally bounded at the integer knots, and O(1+y) at infinity after splitting
at distance 1/z. It uniformly dominates all common separation-cutoff
potentials. Dominated convergence for their weighted pairing, and monotone
convergence for the nonnegative transformed kernel, establish the exact
identity without an infinity-minus-infinity subtraction. The star residual
is L2 bounded and its diagonal is at most y, so the same class admits its
exact full-row expansion. This includes the established actual common-seed
fields and the explicit polynomial theta jets. No unbounded auxiliary
comparison function is used as an original-P trial. The other signed terms
of the original dynamic xi identity remain; this is not an RH proof.
