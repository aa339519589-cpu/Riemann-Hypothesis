# A strict signed square for the complete source/profile Gamma-prime block

This combines the complete source operator with the TRUE projected
conditional-variance metric and its original signed adjoint storage.
The resulting coefficient-one block has a positive factor without using
actual Q_delta positivity. It is not yet the full original boundary
comparison, and the exact original-boundary remainder is displayed.

Dependencies: [the complete source contraction](SOURCE_CONTRACTION.md),
[the true variance metric](TRUE_VARIANCE_METRIC.md),
[the projected signed storage](STORAGE.md),
and [the complete finite projected arithmetic](FINITE_PROJECTION.md).

## 1. Same fields, all source channels, and the exact principal

Use the full arithmetic profile a(n)=1-mu_ar(n), or its genuine finite
mask a_N(n)=1-mu_ar(n)1_(n<=N), N>=3. Write

    m=T a, sigma^2=Var_p(a), beta=T c,
    kappa=T[c(a-m)^2]/sigma^2,
    D_n=A(x)[a(n)-m(x)], h=sigma^2 A,
    lambda_0=beta+kappa+23/200.

A is a scalar amplitude; for the actual current it is precisely
T[a(w-u)]/sigma^2. No canonical seed is substituted. For a scalar source
ratio u, let S_a(u) be its COMPLETE projected mismatch

 S_a(u)=-Gamma_cont(m,u)
          +sum_d r_d(x)[T_y a(dm)-m(x)][u(x)-u(y)],
    y=x+log d.

Every true prime power, including those beyond a finite mask, remains
in this expression. Let P_a be the exact projected hidden principal,
whose off-site terms after projection are the attenuated primes, while
its original diagonal keeps every prime power. Define

    I[A]=int psi^2 A P_a(sigma^2 A),
    D_0=int psi^2 sigma^2 A^2,
    D_lambda=int psi^2 lambda_0 sigma^2 A^2,
    F_A(z)=psi(x)sigma(x)A(x)/sqrt(2z), z=pi exp(2x).

For compact smooth amplitudes and for the separately proved actual
amplitude domain, I is the displayed operator pairing. For a generic
amplitude in the closed transformed form domain, I denotes its closed
sectorial-form extension. Finite Gamma FORM energy alone is not asserted
to imply the logarithmic GENERATOR domain.

The previously proved exact identity is

 I[A]=D_(3/2)[F_A]+int[beta+kappa+c_*]|F_A|^2
                   -Re<F_A,J_R F_A>+Re<F_A,K_(theta,R)F_A>,
    c_*=(1/2)log(3/2).                              (1)

The complete bounds are ||J_R||<=1/12 and ||K_(theta,R)||<1/120000.
Because c_*>1/5,

 I[A]-D_lambda
   >=D_(3/2)[F_A]+(199/120000)D_0.                 (2)

Indeed 1/5-1/12-1/120000-23/200=199/120000.
The positive E_1/4 half-line boundary is inside D_(3/2) throughout.

## 2. The remaining source cross is genuinely the hidden spatial cross

Full intertwining and the product rule, using T D=0, give

 T Gamma_hidden(Uu,D)
   =u T(A_hidden D)+T[D A_sp Uu]-G(u T D)
   =A S_a(u).

Refresh contributes zero because Uu is label-independent. Therefore

    E_sp(Uu,D)=int psi^2 A S_a(u).                  (3)

This is the full continuous-plus-divisor bilinear, not a selected prime
row. In particular the opposite signs of its continuous/profile and
prime parts have not been erased.

## 3. Exact completion, followed by the strict source inequality

Let F[u]=F_Gamma[u]+F_prime[u] be the complete original one-orientation
forward form. The source contraction theorem proves

    ||S_a(u)||_*^2:=int psi^2 |S_a(u)|^2/(lambda_0 sigma^2)
                               <=(124633/125000)F[u].       (4)

Its Gamma/prime 2 routing and complete higher-prime forcing use disjoint
source expenditures, including their full mixed cross. It does not
assume a false complete-prime/Gamma domination.

Define the signed coupled block

    C[u,A]=F[u]+2E_sp(Uu,D)+I[A].                   (5)

The square completion is EXACT:

 C[u,A]
   =F[u]-||S_a(u)||_*^2+[I[A]-D_lambda]
       +int psi^2 lambda_0 sigma^2
                  [A+S_a(u)/(lambda_0 sigma^2)]^2.           (6)

Combining (2),(4),(6) gives the strict positive factor

 C[u,A]
   >=(367/125000)F[u]+D_(3/2)[F_A]+(199/120000)D_0
       +int psi^2 lambda_0 sigma^2
                  [A+S_a(u)/(lambda_0 sigma^2)]^2.           (7)

Every term on the right is nonnegative. No actual-source extremal
property or Q_delta>=0 assumption is used in (7). The complete arithmetic
principal, source gradient, finite boundaries and Gamma half-line
boundary remain in their exact definitions.

This is also a finite-family quadratic/Gram inequality, by polarization
on a common profile and common operator domain. A constant source gauge
has zero F and zero S and causes no false strictness claim at zero input.

## 4. The ORIGINAL signed storage is part of the factor

Let b=G^*(psi^2) be the original signed adjoint density. The projected
product-rule identity is

    2I[A]=E_full[D]+int b sigma^2 A^2.              (8)

Thus the left side of (7) is exactly

 F[u]+2E_sp(Uu,D)+(1/2)E_full[D]
                          +(1/2)int b sigma^2 A^2.          (9)

In particular b has not been replaced by its positive part. The full
prime/pole/source row that produced this signed density remains in (9),
including its negative wing. The positive factor (7) therefore does
more than prove an auxiliary Gaussian inverse estimate: it controls a
specific mixed source/current block with its correct original storage.
The earlier positive centered-boundary block uses this same E_sp[D];
it cannot be added as an independent gain without retaining its debit.

## 5. Actual residual and the missing full original comparison

For the actual field w-u=D+Z the exact projected equation is

    P_a h=-S_a(u)+r+I_Z,
    r=-T[c(a-m)Z], T Z=T(aZ)=0.

Therefore (5) can also be written, at this same actual source,

    C[u,A]=F[u]-I[A]+2int psi^2 A(r+I_Z).           (10)

The residual r+I_Z remains grouped and is not set to zero. No quantitative
residual estimate is needed for (6)-(9), and none is spent here. Equation
(10) does not say that the transformed source remains actual Q-null.
There is no iteration of an actual-only current approximation.

The original form is Q_delta[psi*u]=2F[u]-B_delta[u]. Its exact relation
to the newly positive block is

 Q_delta[psi*u]=2C[u,A]-R_delta[u,A],
 R_delta[u,A]=B_delta[u]+4E_sp(Uu,D)
                         +E_full[D]+int b sigma^2 A^2.      (11)

There is also an EXACT full-original-boundary version of the positive
mixed block for the actual source. Set b_A=mA and

 F_m(u,A)=int_forward K m(y)[u(x)-u(y)][A(x)-A(y)],
 J_a(u,A)=sum_d int K_d[A_d(y)-m(y)]A(x)[u(x)-u(y)].

Expanding the full forward bilinear gives directly

 F(u,mA)=F_m(u,A)-int_cont K A(x)[m(y)-m(x)]Delta u
                  +sum_d int K_d A(x)[m(x)-m(y)]Delta u.

Comparing with the exact definition of S_a therefore yields
int psi^2 A S_a(u)=F_m(u,A)-F(u,mA)+J_a(u,A).
The lawful mixed stationarity Q_delta(psi*u,psi*b_A)=0, or
F(u,mA)=B_delta(u,mA)/2, now gives

 E_sp(Uu,D)=F_m(u,A)-(1/2)B_delta(u,b_A)+J_a(u,A).

Therefore the SAME left side of (7) is

 F[u]+2F_m(u,A)-B_delta(u,mA)+2J_a(u,A)
                         +(1/2)[E_full[D]+int b sigma^2 A^2]. (12)

All original Gamma-wall, reflected-prime and negative-pole terms in
B_delta(u,mA) are retained. Every prime power remains in J_a, including
those whose projected off-site covariance vanished. Equation (12) is
an actual-source boundary-aligned corollary of the unconditional square,
not a new expenditure. The lawful source is psi*mA; no quadratic
original-P membership of psi*A is needed for this mixed identity.

No sign or upper domination for R_delta in (11) is asserted. In particular
the DIAGONAL boundary B_delta[u], the projected boundary B_D, and their
full residual cross cannot be inferred from the positive mixed block.
The whole residual field Z and its full boundary/spatial cross, retained
in the joint-star and centered-residual theorems, likewise still have
to be included in any full current comparison. Formula (7) is a genuine
nonlocal signed positive block, not a proof of K<=1 or RH.

## 6. Domain and cutoff passage

For compact smooth source/amplitude cores, all identities follow with
common Gamma, prime, label and origin cutoffs. The infinite profile
identities are imposed only after the exact finite union boundaries
are retained. The completed source estimate (4) extends S from the
original F core to its forward completion modulo constants.

The amplitude domain is the one proved in the projected-storage theorem:
finite hidden/star forms and the exact true-metric Gamma/potential forms,
with absolute signed b storage. It includes the SAME bounded actual
projection. For that actual amplitude the separate Carleman argument
establishes F_A in the Gamma generator domain. For general form-domain
amplitudes use instead the closed sectorial-form interpretation of I
specified above. The isometry, the corresponding operator/form pairing,
and the two bounded complete perturbations justify (1)-(2) in either
case; no generator-domain claim is inferred solely from form finiteness. The square term in (6) is finite by (4) and D_lambda<infinity.
Equation (3) is the continuous bilinear identity on the corresponding
positive hidden forms, followed by the same complete limits. Hence the
signed completion is not a manipulation of separately divergent drifts
or of unproved individual unweighted higher-label source domains.
