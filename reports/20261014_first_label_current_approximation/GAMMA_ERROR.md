# A same-source first-label Gamma error bound with the full posterior debit

Let w(x,n) be the current-adapted full-band eta lift of the SAME actual
plateau ratio u, as constructed in
[CURRENT_FIELD.md](CURRENT_FIELD.md).
Write

    p_n(x)=n^(-1/2)eta(x+log n)/Phi(x),
    u(x)=sum_n p_n(x)w(x,n),
    V(x)=sum_n p_n(x)|w(x,n)-u(x)|^2,
    e(x)=w(x,1)-u(x), K(x)=3Phi(x)+Theta(x)/2.

The result controls the entire forward Gamma energy of e, not merely its
pointwise size. Every moving-posterior term is retained. All estimates also
hold as inequalities of nonnegative extended integrals; separate finiteness
of a hidden energy is not inferred just from a pointwise variance bound.

Use the ONE-ORIENTATION forward forms

    F_Gamma[e]=int_(0<x<y) psi(x)psi(y)kappa(y-x)|e(y)-e(x)|^2 dxdy,
    E_Gamma[w]=int_(0<x<y) psi(x)psi(y)kappa(y-x)
                    sum_n p_n(y)|w(y,n)-w(x,n)|^2 dxdy,
    R_0[w]=int_0^infinity psi(x)K(x)V(x)dx.

The hidden Gamma conductance really is the displayed p_n(y), by the exact
full-band intertwining. It is not replaced by p_n(x).

**Theorem.** For every t>0,

    F_Gamma[e] <= (1+t) E_Gamma[w]/400
                       +(1+1/t) R_0[w]/50.                     (1)

The same constants apply to complex sources and finite vector-valued sources
in a Hilbert space. This does not by itself bound the prime error, the full
signed form, or a separately divergent hidden wall field.

## 1. Exact edge decomposition

For a forward edge x<y put p=p(x), q=p(y), Delta_n=w(y,n)-w(x,n),
and h_n=w(x,n)-u(x). Then EXACTLY

    e(y)-e(x)=A-B,
    A=Delta_1-sum_n q_n Delta_n,
    B=sum_n(q_n-p_n)h_n.                                      (2)

Weighted Cauchy--Schwarz gives

    |A|^2 <= eps(y) sum_n q_n|Delta_n|^2,
    |B|^2 <= chi2(q||p) V(x),
    eps(x)=(1-p_1(x))/p_1(x),
    chi2(q||p)=sum_n (q_n-p_n)^2/p_n.                          (3)

The first coefficient is exact: sum_n (1_(n=1)-q_n)^2/q_n=eps(y).
Using |A-B|^2<=(1+t)|A|^2+(1+1/t)|B|^2 proves (1) once we establish

    sup_(x>=0) eps(x)<1/400,
    R_chi(x):=int_x^infinity kappa(y-x)psi(y)
                               chi2(p(y)||p(x))dy <=K(x)/50.  (4)

These bounds include the genuine origin, where the second integral is
finite; they do not require a pointwise derivative of the actual source.

## 2. The complete eta posterior is monotone in each tail label

Put z=pi exp(2x)>=pi and

    a(q)=(4q^2-6q)exp(-q), A(z)=sum_(n>=1)a(n^2 z).

Then p_n=a(n^2 z)/A(z). For n>=2 let

    rho_n(z)=a(n^2 z)/a(z)
       =n^2(2n^2z-3)/(2z-3) exp(-(n^2-1)z),
    eps(z)=sum_(n>=2)rho_n(z).

For z>=pi>3,

    n^4 exp(-(n^2-1)z) < rho_n(z)
                         <2n^4 exp(-(n^2-1)z).                 (5)

Set b_n(z)=-partial_z log a(n^2z). Direct differentiation gives

    b_n=n^2-1/z-1/(z-3/(2n^2)),
    b_n-b_1=n^2-1+1/(z-3/2)-1/(z-3/(2n^2)).                  (6)

Thus b_n-b_1<n^2 and b_n-b_1>3 for every n>=2. Moreover

    E_p b-b_1 <=sum_(n>=2)p_n n^2
              <2 sum_(n>=2)n^6 exp(-(n^2-1)z)<1.               (7)

For the last very coarse bound, use z>3, exp(1)>2: the n=2 term is
64 exp(-9)<1/8, while the n>=3 sum is at most twice its first term
729 exp(-24)<1/10000. The successive-term ratio on that tail is below
(4/3)^6 exp(-21)<1/2. Multiplication by 2 still leaves (7) below 1.
Consequently

    partial_z log p_n=E_p b-b_n<0, n>=2,
    partial_z p_1>0.                                         (8)

All label series and their differentiations converge normally on z>=pi.

For p=p(z), q=p(t), t>=z, write D=q_1-p_1>=0. Since every tail coordinate
has decreased,

    chi2(q||p)
       =D^2/p_1+sum_(n>=2)(p_n-q_n)^2/p_n
       <=D^2/p_1+D<=D/p_1
       =[eps(z)-eps(t)]/[1+eps(t)]
       <=eps(z)-eps(t).                                      (9)

This is the full chi-square debit, not an unproved estimate on a scalar
normalization factor.

## 3. A uniform derivative and theta-integral payment

Differentiating rho_n gives

    -partial_z log rho_n
      =(n^2-1){1+6/[(2n^2z-3)(2z-3)]}
      <=(10/9)(n^2-1).                                      (10)

In particular the n=2 contribution to -eps'/eps is at most 10/3. From
(5), eps>=rho_2>=16 exp(-3z), so the remaining contribution is bounded by

    (5/36) sum_(n>=3)n^6 exp(-3(n^2-4))<1/100.                 (11)

Indeed this last sum is at most twice 729 exp(-15), since its successive
ratio is below 1/2; exp(15)>2^15 already proves (11). Therefore

    0<=-eps'(z)<=4 eps(z),
    eps(z)-eps(t)<=4(t-z)eps(z).                             (12)

Define the ORIGINAL positive theta source and the reset coefficient by

    theta_c(t)=sum_(n>=1)c(n^2t)exp(-n^2t),
    c(q)=8q^3-30q^2+15q,
    k(z)=exp(-x/2)K(x)
        =sum_(n>=1)k_0(n^2z)exp(-n^2z),
    k_0(q)=12q^2-18q+1/2.

Only theta_c(t)>=0 for t>=pi is used; individual c(n^2t) are never assigned
probabilities. Direct integration of the COMPLETE theta series gives

    I(z):=int_z^infinity theta_c(t)dt
       =sum_(n>=1)n^(-2)d(n^2z)exp(-n^2z),
    d(q)=8q^3-6q^2+3q+3.                                    (13)

For q>=3,

    d(q)<(6/5)q k_0(q).                                      (14)

The difference has numerator 32q^3-78q^2-12q-15, which is positive at 3
and has positive increasing derivative thereafter. Termwise summation gives

    I(z)<(6/5)z k(z).                                        (15)

The exact logarithmic change of variables in (4) is

    R_chi(x)/K(x)
       =[1/(2k(z))]int_z^infinity theta_c(t)/(t-z)
                                chi2(p(t)||p(z))dt.

Combining (9), (12), and (15) yields the complete row payment

    R_chi(x)/K(x)<(12/5)z eps(z).                             (16)

No prime term is hidden inside this Gamma payment; K is precisely the
already available SAME reset-variance row.

## 4. Explicit rational constants

For z>=pi>157/50, the n=2 prefactor in rho_2 is

    4(8z-3)/(2z-3)=16+36/(2z-3)<27.

The remaining series, after dividing by exp(-3z), is bounded by

    2 sum_(n>=3)n^4 exp(-3(n^2-4))<1

using its first term and the same ratio bound. Thus

    eps(z)<28 exp(-3z).                                     (17)

Both exp(-3z) and z exp(-3z) decrease on z>=157/50. Finally, from the
positive exponential series and exp(1)>27/10,

    exp(471/50)>(27/10)^9 [1+21/50+(21/50)^2/2]
       =57504630634286967/5000000000000
       >11200.                                              (18)

Equations (17)-(18) imply eps<1/400. They also imply

    (12/5)z eps(z)
       < (336/5)(157/50) / (57504630634286967/5000000000000)
       <1/50,                                               (19)

by integer cross multiplication. This proves both assertions in (4).

The proof of (1) now consists solely of (2)-(4) and Tonelli on the positive
hidden energy and variance measures. It preserves the complete actual
posterior, every Gamma jump, and the exact mixed posterior/source debit.
It may be combined with a SEPARATELY proved full-prime error estimate using
the same reset row, provided that row is not spent twice beyond its stated
coefficient.
