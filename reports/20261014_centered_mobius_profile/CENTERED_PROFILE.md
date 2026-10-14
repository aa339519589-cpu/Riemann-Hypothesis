# A complete positive spatial factor for the centered Mobius current profile

This pays the moving-centering defect of the genuine Mobius profile, not
only its uncentered diagonal. The comparison keeps the whole Gamma kernel,
every prime power and every square collision. It is a strict positive block
on the SAME actual current's conditional Mobius projection. The residual
current component and its mixed original boundary are not discarded.

## 1. Exact field and normalization

Use the genuine Mobius profile in
[the uncentered profile theorem](UNCENTERED_PROFILE.md):

    a(n)=1-mu_ar(n) in {0,1,2}, a(1)=0,
    m=T a, M=T a^2, sigma^2=M-m^2,
    V_1=T[(a_score-beta)a], V_2=T[(a_score-beta)a^2],
    beta=T a_score, q=sum_(n>=2)p_n.

Here a_score is the reset score, not the fixed arithmetic profile a.
Every tail score satisfies a_score,n-beta>3log2. Therefore

    0<V_1<=V_2, V_2>3log2 M,
    m<=2q<2/401, m^2<=qM.                             (1)

Let A(x) be a real amplitude and consider the CENTERED label field

    D_n(x)=A(x)[a(n)-m(x)].                           (2)

Its mean is zero and its variance is sigma^2 A^2. The SAME star law
provides a coherent random source-coordinate field D(x)=D_(N_x)(x).
Its covariance is exactly

    E[D(x)D(y)]=A(x)A(y)[M(max(x,y))-m(x)m(y)].         (3)

Let F_star[D] be its full original forward energy, and E_sp[D] the genuine
hidden continuous-plus-true-divisor energy. Refresh is not added to either
side. The theorem is

    E_sp[D] >= F_star[D]+(9/5)int psi^2 M A^2.        (4)

The SAME current amplitude A_*=T[a(w-u)]/sigma^2 is permitted by the
uncentered profile theorem's averaged form-domain proof. No assertion
that unweighted individual higher-label sources are original-P is used.

## 2. The complete centered quadratic kernel

Put y=x+log d and K_d(x)=alpha_d psi(x)psi(y). Define

    A_d(y)=sum_m p_m(y)a(dm),
    C_d(y)=M(y)-sum_m p_m(y)a(m)a(dm)>=0.

The last nonnegativity is the exact Mobius incidence law: a new prime
against mu_ar(m)=-1 contributes4, and a square collision contributes2.
Every other case contributes0. In particular 0<=C_d<=M.

Direct expansion of the centered squared differences gives EXACTLY

 E_sp[D]-F_star[D]
   =int psi^2 [V_2-2mV_1]A^2
    -2int_(x<y) psi(x)psi(y)kappa(y-x)
                          m(y)[m(x)-m(y)]A(x)A(y)dxdy
    +2sum_d int K_d(x)
           {C_d(y)+m(y)[A_d(y)-m(x)]}A(x)A(y)dx.      (5)

Here m decreases because it is a fixed nonnegative combination of the
strictly decreasing tail probabilities. Formula (5) is not an absolute
Cauchy estimate for the centering debit; it retains the signed kernels.

To check its diagonal, the uncentered comparison gives V_2. Subtracting
the mean b=mA adds the diagonal -2mV_1, since the complete spatial/profile
intertwining gives

    T[A_sp a]-Gm = T[a_score a]-beta m=V_1.

For the continuous cross, hidden same-label transport has p_n(y), while
the star covariance is M(y)-m(x)m(y); their difference is exactly
-m(y)[m(x)-m(y)]. For a divisor edge the true prelabel is dm and the child
is m. Its centered cross gives C_d+m(y)[A_d-m(x)]. This proves (5) with
both original edge orientations and every divisor crossing retained.

## 3. Complete Gamma Schur bound, without spending derivative energy

Set B(x)=psi(x)sqrt(M(x))A(x). The absolute normalized Gamma kernel for
x<y is

    J(x,y)=kappa(y-x) m(y)[m(x)-m(y)]/sqrt(M(x)M(y)).

The elementary inequality m^2<=qM yields

    J(x,y)<=kappa(h)sqrt(q(x)q(y))[1-m(y)/m(x)], h=y-x. (6)

We prove the complete logarithmic derivative bound

    0<=-d_x log m(x)<14z, z=pi exp(2x).               (7)

Indeed the profile-tilted distribution is supported at n>=2, with its
n=2 weight exactly2p_2. Since a(n)<=2,

 E_(a p/m) N^2
   <=4+sum_(n>=3)(p_n/p_2)(n^2-4)<5.

The full tail inequality here follows from the complete series proved in
[the SAME-star boundary Schur theorem](../20261014_same_current_star_blocks/BOUNDARY_SCHUR.md), Section3:
sum_(n>=3)(p_n/p_2)(3/8)^2(n^2-4)^2<1/384^2:
its displayed first-power sum is at most64/(45*384^2)<1.
The complete posterior moment is E_p N^2<17/16. Differentiating
P(n^2z)e^(-n^2z), P(t)=4t^2-6t, gives

 d_z log m=-E_(a p/m)N^2+E_p N^2
       +E_(a p/m)[2N^2/(2N^2z-3)]-E_p[2N^2/(2N^2z-3)].

The final difference has absolute value at most1/3 for z>=pi>3.
Thus |d_z log m|<5+17/16+1/3<7, proving (7).
The total tail q<1/401 and q<=28e^(-3z) are complete theta bounds.
Consequently, for z_y>=z_x>=pi>3,

 sqrt(q(x)q(y))<1/401,
 z_y sqrt(q(x)q(y))
   <=28z_y exp[-3(z_x+z_y)/2]
   <=84exp(-9)<21/2000.                              (8)

The middle expression is maximized by first decreasing z_y to z_x,
then decreasing z_x to3. The last rational bound uses exp3>20.
Equations (6)-(8) give the uniform envelope

    J(x,y)<=kappa(h)min(1/401,(147/1000)h).           (9)

The continuous half-line kernel has

 int_0^1 h kappa(h)dh <=exp(1/2)-1<2/3,
 int_1^infinity kappa(h)dh<2.

For the first, kappa(h)=exp(h/2)/(2sinh h). For the second, use
1-exp(-2h)>3/4 and exp(-1/2)<2/3 for h>=1. The symmetric Schur row of
J is therefore strictly less than

    c_Gamma=2[(147/1000)(2/3)+2/401]
             =49/250+4/401.                         (10)

It follows that the entire continuous cross line of (5) is bounded in
absolute value by c_Gamma||B||_2^2. No Gamma derivative square, current
reset energy or original hub budget was used for this debit.

## 4. Complete prime Schur bound and the resulting gap

For every true prime power d, a(d)>=1. Therefore
A_d(y)>=p_1(y)>400/401>m(x). Using a<=2 and m<=M gives

    0<=C_d(y)+m(y)[A_d(y)-m(x)]<=3M(y).              (11)

The uncentered profile's complete endpoint estimate is

    M(x+log d)/M(x)<2exp[-3(d^2-1)z].

Hence the ENTIRE prime cross line of (5) is bounded in absolute value by

  6sqrt2 sum_(d>=2)alpha_d exp[-(3pi/2)(d^2-1)] ||B||_2^2
                      <(1/20000)||B||_2^2.         (12)

This is three times its already proved all-integer series majorant. It
retains the exact true-prime expression in (5); non-prime-power integers
appear only in the safe upper bound.

Finally (1) gives the diagonal lower bound

    V_2-2mV_1 >=(1-2m)V_2
                   >(397/401)3log2 M.

Using log2>69/100 and (10),(12), its net coefficient is greater than

 (397/401)(207/100)-(49/250+4/401)-1/20000
        =14783479/8020000 >9/5.                     (13)

Equations (5)-(13) prove (4). The smallness is in the exact original
source-coordinate two-endpoint kernels, not a false bound on a generic
inverse in psi^2. All complete Gamma and prime cross terms have been paid.

## 5. Same-current domain and the full original boundary

For a compact smooth amplitude, (5) follows with common spatial, label
and Gamma cutoffs. The infinite Mobius incidence must be imposed only
after the square-collision tails are paid, exactly as in the uncentered
profile theorem. The bounds (9),(12) extend its cross terms continuously
in L2(psi^2 M dx). The diagonal is locally integrable with the proved
operational 1/x score, while psi^2=O(x^2).

For the actual projection A_*, the uncentered theorem proves boundedness,
finite averaged spatial energy and potential, and approximation by compact
amplitudes in the weighted logarithmic form. Its mean b=mA_* has a lawful
original-P source psi*b: it is the mean of the integrable original-P star field
Y=A_*a. Jensen in the original positive forward form pays F[b]. Thus D=Y-b
has finite genuine spatial and star forward energy as well, by the
quadratic triangle bound. All cutoff limits in (5) are therefore justified;
no amplitude-to-Gamma-domain inference is used.

Let B_D be the COMPLETE original Gamma-wall/reflected-prime/pole form
of the centered covariance (3). All its positive component integrals
are finite under the bounded actual amplitudes and original theta rows.
The actual PSD hypothesis gives Q_D=2F_star[D]-B_D>=0. The resulting
strict full-boundary block is

    2E_sp[D]-B_D
       =Q_D+2(E_sp[D]-F_star[D])
       >=(18/5)int psi^2 M A_*^2.                  (14)

One may retain a fixed common-neutral projection inside Q_D exactly as
in the dominant feature theorem; its leakage is not silently discarded.
Formula (14) is a SAME-current centered arithmetic block, not the complete
hidden current comparison. In H=A_*(a-m)+Z, the residual satisfies
T Z=T(aZ)=0, but its spatial and full-boundary cross terms with D generally
remain. They must be kept before any sign for the full original Q_delta
or K<=1 can be inferred. No such total sign is claimed here.
