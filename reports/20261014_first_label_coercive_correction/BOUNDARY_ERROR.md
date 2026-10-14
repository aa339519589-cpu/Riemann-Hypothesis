# The complete signed boundary error of the actual first-label current

Let u, w, V and e=w_1-u be the SAME actual current-adapted fields of the
first-label Gamma and divisor estimates. Put

    eps(x)=(1-p_1(x))/p_1(x), K=3Phi+Theta/2,
    R_v=int_0^infinity psi(x)K(x)V(x)dx.

The exact posterior variance estimate is |e|^2<=eps V. We use it to control
not just an individual prime row but the COMPLETE signed boundary graph

    B_delta[e]=H[e]+(1-delta)N[e]-P_pole[e], 0<=delta<=1/3.

The independently proved graph coercivity gives B_delta[e]>=0. In the
ordered-edge conventions of that theorem, the stronger upper bound is

    0<=B_delta[e]<=(2/125)R_v<=R_v/50.                                    (1)

Every reflected prime power and the full pole variance remain in the form.
The upper estimate uses P_pole>=0, rather than claiming that its square is
zero. It spends the SAME reset-variance row R_v already appearing in the
first-label energy comparison and must be accounted for jointly with it.
No positivity of the complete Q_delta follows solely from (1).

## 1. Exact complete-row reduction

Set

    Hpsi(x)=int_0^infinity kappa(x+y)psi(y)dy,
    L(x)=sum_(log n>x)alpha_n psi(log n-x).

Symmetry and |a-b|^2<=2|a|^2+2|b|^2 give exactly

    H[e]+N[e]<=4 int psi(x)[Hpsi(x)+L(x)]|e(x)|^2 dx.

Thus it suffices to prove the uniform coefficient bounds

    eps Hpsi/K<3/1000,
    eps L/K<1/1000.                                         (2)

They imply B_delta[e]<=4(4/1000)R_v=(2/125)R_v<=R_v/50.
The final comparison is strict when R_v>0; no nonzero-variance assertion
is required.

## 2. The complete Gamma-wall row

For x,y>=0, kappa(x+y)<=exp(-x/2)kappa(y). The exact origin row gives
Hpsi(0)<=K(0)<3. The elementary last upper bound can be checked directly:
writing z=pi,

    K(0)=sum_(n>=1)[12(n^2z)^2-18n^2z+1/2]exp(-n^2z),

the n=1 term is below 14/5, and the n>=2 sum is below 1/10. For the first,
the function (12z^2-18z+1/2)exp(-z) decreases for z>=157/50 and
exp(157/50)>(27/10)^3[1+7/50+(7/50)^2/2]. For the second use pi^2<10,
pi>3, a successive-term ratio below1/2, and the upper bound
3840/(27/10)^12<1/10.

Use the complete eta posterior estimate eps<28exp(-3z), z=pi exp(2x),
and K(x)>=6exp(x/2)z^2exp(-z). Then

    eps Hpsi/K <14 exp(-x)exp(-2z)/z^2
       <=14/{(157/50)^2 (27/10)^6[1+7/25+(7/25)^2/2]}
       <3/1000.                                             (3)

All comparisons in (3) are rational after the displayed positive-series
lower bound for exp(157/25).

## 3. Every reflected prime power, including the moving tail

Put a=exp(x)>=1, z=pi a^2, and use the ORIGINAL theta source theta_c. Then

    L(x)=a^(-1/2)sum_(n>a)Lambda(n)theta_c(pi n^2/a^2).

For q>=pi,

    0<=theta_c(q)<=8q^3 sum_(m>=1)m^6 exp(-m^2q).

Keeping the entire reflected row and only enlarging its positive weights
by Lambda(n)<=log n gives

    eps L/K
      <=(112pi/3)a^(-11)
           sum_(n>a,m>=1)log(n)(mn)^6
              exp[-2pi a^2-pi(mn)^2/a^2].                    (4)

Group l=mn only AFTER retaining all prime powers. Since
sum_(n|l,n>a)log n<=l log l, a>=1, and
2pi a^2+pi l^2/a^2>=2pi sqrt(2)l, formula (4) gives

    eps L/K
      <=(112pi/3)sum_(l>=2)l^7 log l exp(-2pi sqrt(2)l)
      <(352/3)sum_(l>=2)l^8 exp(-44l/5).                      (5)

Here pi<22/7, log l<=l, and 2pi sqrt(2)>44/5 are elementary strict bounds.
For the last series the successive ratio is at most
(3/2)^8 exp(-44/5)<26/5000<1/100. Therefore

    eps L/K
      <(352/3)(100/99)256 /
               {(27/10)^17[1+3/5+(3/5)^2/2]}
      <1/1000.                                               (6)

The denominator is a positive-series lower bound for exp(88/5). To verify
the preceding exp(44/5)>5000, use
(27/10)^8[1+4/5+(4/5)^2/2]>5000. This proves (2) without a prime cutoff,
a compact interval grid, or an unproved prime-counting remainder.

## 4. Source-level scope

The actual V is bounded by the same current variance, so all displayed
boundary integrals are finite; the theta weights also pay the complete
reflected row. The argument itself only needs finite R_v and the displayed
nonnegative integrals. No random original-P source is introduced.

The result can be used with the already proved forward error estimate
F[e]<=13E_current/400 and the exact stationarity
Q_delta[psi w_1]=Q_delta[psi e]. The identity remains

    Q_delta[psi e]=2F[e]-B_delta[e].                           (7)

Here E_current denotes the full positive bracket of this SAME actual
current-adapted eta field, not a safe-xi seed norm.

Thus (1) is an explicit small debit for the ENTIRE signed boundary error,
not an assertion that the error direction or the actual source has a new
favorable sign. The full actual transport row and neutral costs remain.

## 5. The lawful common-neutral cost is also small

The separate reflected row in (2) gives

    N[e]<=(1/250)R_v.                                        (8)

For the actual source at POSITIVE depth 0<delta<=1/3, and any lawful
completed common-neutral subspace S, the actual source is
N-orthogonal to S: Q_delta(u,s)=delta N(u,s)=0 and delta>0. This
argument is not asserted for arbitrary q-null sources at delta=0.
Therefore its first-label error has exactly the same
neutral projection as w_1, and

    N[Pi_S w_1]=N[Pi_S e]<=N[e]<=(1/250)R_v.                  (9)

All notation here refers to ratio gradients, or equivalently to sources
psi times those ratios. The exact compensated value is

    Q_delta[psi w_1]-delta N[Pi_S w_1]
       =Q_delta[psi e]-delta N[Pi_S e],                       (10)

with the retained debit bounded by R_v/750 for delta<=1/3. Orthogonal
projection is used only on the already legal N vectors; no convolution
domain is inferred for arbitrary neutral representatives. The coefficients
and inequalities also hold as finite Gram-matrix inequalities for a finite
family of actual states at the same delta, by linearity of the SAME current
map and quadratic polarization. Polynomial neutral infinite currents are
not substituted for these actual current fields.
