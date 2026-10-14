# An explicit positive bulk bound for the exact xi-tail scalar potential

For the EXACT W,L,V_0 of
[the safe-ray reduction](SAFE_RAY_FORMS.md),
this note proves

    V_0(y)>1/5,                       y>=3.            (1)

All integer rows remain complete. This is a component estimate for the hidden
Gamma/divisor comparison, not the full reflected form. The remaining compact
interval below 3 and the head/tail mixed block are separate questions.

## 1. Certified complete-integer Riemann-sum constants

Write X=exp(y), I0=integral_0^infinity exp(-t/2)psi(t)dt, and set

    F(u)=u^(-1/2)psi(-log u), 0<u<1,
    G(u)=-F(u)-uF'(u).

Extend F by zero outside [0,1]. F vanishes at both endpoints, F'(1-)=-p,
p=psi'(0), while G(1-)=p and G'(1-)=0. The complete outward interval checker
`certify_xi_bulk_constants.py`, including explicit theta-index and t>=2
integral tails, proves

    I0>3/4, p<17, Var(F')<80, Var(G')<500.             (2)

Here the variation of F' includes its endpoint jump p, while Var(G') is on
(0,1); G itself has the displayed endpoint jump. The explicit expressions
used by the checker are

    F''(u)=u^(-5/2)[3psi/4+2psi'+psi''],
    G''(u)=u^(-5/2)[-3psi/8-psi'/4+3psi''/2+psi'''].

The endpoint-zero trapezoidal estimate, with the periodic Bernoulli kernel
bounded by 1/8, gives

    |X^(-1)sum_(n>=1)F(n/X)-I0| <=10/X^2,
    |X^(-1)sum_(n>=1)G(n/X)| <=17/(2X)+500/(8X^2).    (3)

At a knot the second estimate applies to either one-sided derivative. The
G endpoint jump contributes its sawtooth coefficient, of magnitude at most
p/(2X); this term is not omitted. The first estimate can also be obtained
by integrating the trapezoidal Peano kernel against the finite signed
measure F''. These statements hold for arbitrary real X, not only integers.

Removing n=1 gives exactly W. For y>=b=log2, the elementary theta bound

    exp(3y/2)psi(y)<1

pays the removed F term: with z>=4pi>12, use c(w)<=8w^3, the complete label
ratio sum <2, and (16/pi)z^4 exp(-z)<= (16/3)12^4 exp(-12)<1.
Consequently, for w(y)=W(y)/(I0 exp(y/2)),

    |w(y)-1|<=16 exp(-2y), y>=b.                      (4)

Set w(y)=0 below b; (4) remains a valid inequality there. For y>=log19,
the similarly elementary bound
exp(3y/2)|psi'(y)-psi(y)/2|<1 pays the removed G term. It follows that

    |W'/W-1/2|
      <=[34/(3X)+254/(3X^2)]/[1-16/X^2]
      <=20/23<1,                     X>=19.           (5)

For the removed G bound the Gaussian argument is already >1000, and the
polynomial bound 100z^5 exp(-z)<1 suffices. Equations (4)-(5) use no smoothing
of the exact integer knots.

## 2. The complete incoming-W deficit is at most 13/20

Fix y>=3, z=pi exp(2y)>1200, X=exp y>20, r=1/X, q=16/X^2<1/25. Let

    C_y(h)=W(y-h)/W(y) for 0<h<y-b, and zero otherwise.

We claim

    integral_0^infinity kappa(h)[exp(-h/2)-C_y(h)]dh
                                                        <13/20. (6)

The integrand need not be nonnegative; the following is an upper bound.
For h<=r, (5) gives C_y(h)>=exp(-3h/2), so this portion is at most
integral_0^r h/(2sinh h)dh<=r/2<1/40. For h>=r, (4) and C_y>=0 give

    exp(-h/2)-C_y(h)
       <=exp(-h/2) min{1,q(exp(2h)+1)/(1-q)}.

Put u=exp(-h), u0=sqrt(q/(1-2q)). Since
kappa(h)exp(-h/2)dh=-du/(1-u^2), the remaining integral is at most

    atanh(u0)+q/(1-q)[1/u0+2atanh(exp(-r))].            (7)

The four contributions, including h<=r, have the elementary bounds

    atanh(u0)<=sqrt(23)/22<11/50,
    q/[(1-q)u0]<5/24,
    2q atanh(exp(-r))/(1-q)
       <=16log(3X)/(X^2-16)<=log60/24<7/40,
    r/2<1/40.

The sum is 377/600<13/20, proving (6). Monotonicity of
log(3X)/(X^2-16) for X>=20 verifies the uniform third bound.

## 3. Two cross rows and the exact outgoing diagonal

Use the row notation

    A_y(h)=xi(y+h)/xi(y),
    B_y(h)=sqrt[W(y)xi(y+h)/(xi(y)W(y+h))],
    D_y(h)=sqrt[W(y-h)xi(y)/(W(y)xi(y-h))]
                 on h<y-b, and zero otherwise.

Let H=z^(-1/2) and lambda=z-sqrt(z)-4>0. The exact xi logarithmic score
is less than -2z+7 in all arguments used below. From (5),

    B_y(h)<=exp(-lambda h),             h>=0,
    D_y(h)<=exp(-lambda h),             0<h<=H.        (8)

For the second bound, use 1-exp(-2h)>=2h(1-h) and y-H>log19.
For the tail, c(w)>=(11/16)8w^3 for w>=12 and (4) give

    D_y(h)<=3 exp(3h) exp[-z(1-exp(-2h))/2].            (9)

On H<=h<=1/2, kappa(h)<=1/h and 1-exp(-2h)>=h, hence

    integral_H^(1/2) kappa D_y
       <=28 exp(-sqrt(z)/2)/sqrt(z)<1/2000.

On h>=1/2, use kappa<=2exp(-h/2), 1-exp(-2h)>1/2, and h<=y-b.
The remaining integral is at most 3z^2 exp(-z/4)<1/2000 for z>1200.
Thus the total extra cost beyond (8) is <1/1000.

The outgoing diagonal is kept EXACT by its Gaussian ladder:

    integral kappa(h)[1-A_y(h)]dh=y+C0/2-beta_xi(z).   (10)

This avoids separately approximating a divergent Gamma exit row. Grouping
(6),(8)-(10) yields

    V_Gamma(y)>=2 I(lambda)-2y-C0+2beta_xi(z)
                                  -13/10-1/500,      (11)
    I(lambda)=integral kappa(h)
                  [1+exp(-h/2)-2exp(-lambda h)]dh
       =digamma(lambda/2+1/4)
                   -digamma(1/4)/2-digamma(1/2)/2.

## 4. A uniform strictly positive remainder

Use L/W<=y, beta_xi>0, C0=log pi-digamma(1/4), and
 digamma(1/2)=-EulerGamma-2log2. The elementary estimate
 digamma(t)>=log t-1/t follows by bounding its harmonic-limit sum by an
integral. Equations (11) then imply

    V_0(y)>=log pi+EulerGamma+2log(lambda/z)-4/lambda
                                      -13/10-1/500.   (12)

For z>1200,

    1-lambda/z<1/34+1/300=167/5100,
    2log(lambda/z)>-7/100, 4/lambda<1/250.

Finally log pi>11/10 and EulerGamma>1/2. The latter already follows from
EulerGamma>=H_6-log7>1/2; the strict logarithmic inequalities are checked
by elementary exponential estimates. Substitution in (12) gives

    V_0(y)>8/5-7/100-1/250-13/10-1/500
             =28/125>1/5.

This proves (1). None of the discarded terms was a negative square or a
conditional mean correction: only the positive beta term and the inequality
L/W<=y were used. All unproved finite-head and mixed-block signs remain
outside the theorem.
