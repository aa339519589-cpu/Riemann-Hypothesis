# The projected Mobius principal is a full signed storage factor

The exact conditional-variance principal has a direct interpretation in
the original source pairing: it is one half of the projected hidden
energy plus its COMPLETE signed adjoint storage. This is not positivity
of a separately truncated backward row, and no original-boundary term
is omitted. The finite mask boundary is included throughout.

Dependencies: [the true variance metric](TRUE_VARIANCE_METRIC.md),
[the exact centered cross](../20261014_centered_mobius_profile/RESIDUAL_CROSS.md),
[the finite Mobius reset theorem](RESET_FACTS.md),
and [the exact finite prime-cancellation theorem](FINITE_PROJECTION.md).
The arithmetic projection is restated here to fix its operator
normalization; the companion theorem additionally retains its full
square-collision and cutoff-union incidence.

## 1. Project the genuine hidden generator, not only its mean

Use the finite or full profile a=1-mu_N, with a(1)=0, a(2)=2,
mu_N(n)=mu_ar(n)1_(n<=N), or mu_N=mu_ar. Let

    m=T a, sigma^2=T(a-m)^2, beta=T c,
    kappa=T[c(a-m)^2]/sigma^2,
    D_n=A(x)[a(n)-m(x)], h=sigma^2 A.

The full hidden generator is A_hidden=A_sp+A_reset, with refresh rates
p_j c_j and the complete genuine Gamma/divisor dynamics. Write

    A_d(y)=T_y a(dm),
    gamma_d(y)=-Cov_y(a(dm),a(m)), y=x+log d.

Then the exact projected generator identity is

 T_x[(a-m)A_hidden D]
      =G_cont h+lambda_prime h+kappa h
                       +sum_d r_d(x)gamma_d(y)A(y)
      =:P_a h.                                    (1)

The term lambda_prime=sum_d r_d retains EVERY prime power. There is
no assertion that this projected operator is Markov.

To verify (1), the continuous cross at the future endpoint is
-T_y[(a-m_x)(a-m_y)]A_y=-sigma_y^2 A_y. The true divisor cross is
-T_y[(a(dm)-m_x)(a(m)-m_y)]A_y=gamma_d A_y.
For the local diagonal, use

    G_cont p_n=p_n[L_n+beta-c_n-lambda_prime],
    G_cont(m^2)=2m G_cont m-Gamma_cont[m].

Expanding the two centered moments cancels every L_n and posterior
Gamma-cooling row. The spatial remainder is (kappa-beta)h; refresh
adds exactly beta h. This gives (1). As in the earlier matrix proof,
the infinite Gamma diagonal is never separated before this cancellation.

## 2. Complete arithmetic attenuation, including the finite boundary

Put A_mu=T mu_N=1-m. For d=p^j with j>=2, mu_N(dm)=0 for every m,
so a(dm)=1 and

    gamma_(p^j)=0.                                 (2)

For a prime p, define E_(p,N)={m<=N/p: p does not divide m}, omitting
the cutoff for the full mask. The exact product mu_N(pm)=-mu_N(m)
1_(E_(p,N)) yields

 gamma_p=sum_(m in E_(p,N))p_m mu_N(m)[mu_N(m)-A_mu],
 sigma^2=sum_m p_m mu_N(m)[mu_N(m)-A_mu].            (3)

Since 0<A_mu<1 and mu_N takes only -1,0,1, EVERY summand in (3) is
nonnegative. Consequently

    0<=theta_p:=gamma_p/sigma^2<=1.                 (4)

The finite complement {m<=N: p divides m OR m>N/p} is counted as one
union, not counted twice. For p>N the sum in (3) is empty. In particular
higher powers do not vanish from lambda_prime or the source forcing;
only their off-site projected covariance vanishes exactly.

Combining (1)-(4), with the same q_psi=psi/B as before,

 q_psi P_a h
    =[G_B+beta+kappa+K_theta](q_psi h),
 K_theta g=sum_(p prime)log p exp[-(p^2-1)z]
                                theta_p(p^2z)g(p^2z).        (5)

The sign in (5) is PLUS. This is the exact antiferro prime covariance,
not the Liouville operator. All finite prime-cutoff boundary information
is inside theta_p and the residual described below.

## 3. Its exact true-metric coercivity

Use the isometry F=psi*h/[sqrt(2z)sigma] and the complete ratio
R(z)=exp(3z)sigma(z)^2 from the true-variance theorem. Equation (5)
conjugates to

    G_(3/2)+beta+kappa+(1/2)log(3/2)-J_R+K_(theta,R).  (6)

The coefficient of the p-th future dilation in K_(theta,R) is

 log p sqrt(p) exp[-3(p^2-1)z/2]
            sqrt[R(p^2z)/R(z)] theta_p(p^2z).

By (4) its L2 norm is bounded by the SAME complete series <1/120000.
The true-variance theorem already gives ||J_R||<=1/12, with exact
D_(3/2) and its E_1/4 half-line boundary. Therefore

 int psi^2 A P_a h
   =D_(3/2)[F]+int[beta+kappa+(1/2)log(3/2)]F^2
                   -Re<F,J_R F>+Re<F,K_(theta,R)F>
   >=D_(3/2)[F]+int(2beta+21/10)F^2.                (7)

The sign of the last exact prime pairing is not assumed favorable for
sign-changing F. Its whole bounded-operator debit has been paid. This
proof uses no actual Q_delta positivity hypothesis.

## 4. The complete original signed adjoint storage

Let b=G^*(psi^2) be the original signed current density, namely

 b=psi[sinh(x/2)/2+2K-2x psi-H_kappa psi-L],
 K=3Phi+Theta/2.

Its positive and negative parts have the published
[complete adjoint bounds](../20261014_uniform_same_current_energy_bridge/REPORT.md), namely b_+<=2psi K and b_-<=2psi exp(x/2). In particular it is NOT
pointwise positive. The hidden product rule and full intertwining give

 T Gamma_hidden[D]
    =2A T[(a-m)A_hidden D]-G(sigma^2 A^2).

Pairing against psi^2 and keeping the common adjoint cutoff therefore gives

    E_full[D]+int b sigma^2 A^2
                         =2int psi^2 A P_a h.      (8)

Every true-prime backward contribution is contained in b in (8). No
backward theta row is split or asserted to converge by itself.
Equations (7)-(8) prove the strict signed storage factor

 E_full[D]+int b sigma^2 A^2
   >=2D_(3/2)[F]+int psi^2(4beta+21/5)sigma^2 A^2.  (9)

This is the projected conditional variance in the ORIGINAL source
coordinate. It is stronger information than an unweighted Gamma
resolvent norm, but it is still only the projected block, not the full
original Q_delta or the whole current covariance.

## 5. Actual source and residual alignment

For the actual current H=w-u=D+Z, T Z=T(aZ)=0. Define

    S_a(u)=T[(a-m)A_sp Uu],
    r=-T[c(a-m)Z],
    I_Z=sum_d r_d T_y[a(dm)Z_m(y)].

Direct projection of A_hidden w=G u gives EXACTLY

    P_a h=-S_a(u)+r+I_Z.                            (10)

To check the residual projection, its continuous future term vanishes
because T_y Z(y)=T_y[a Z(y)]=0. The full local outgoing/posterior row
is -r, and the true divisor future row is -I_Z. Thus
T[(a-m)A_hidden Z]=-r-I_Z, with no omitted moving Gamma term.
Equations (8),(10) identify the full signed forcing:

 E_full[D]+int b sigma^2 A^2
    =-2int psi^2 A S_a(u)+2int psi^2 A(r+I_Z).        (11)

The source-gradient term is

 S_a(u)=-Gamma_cont(m,u)
              +sum_d r_d[A_d(y)-m(x)][u(x)-u(y)].    (12)

It contains every prime power even though (2) eliminates their off-site
projected covariance. For the full Mobius profile the residual satisfies
I_Z,p=-r_p T_y[mu_ar(m)1_(p|m)Z_m], and I_Z,p^j=0 for j>=2.
Finite masks additionally retain the single union m<=N with
p|m OR m>N/p. Orthogonality can remove the first two child labels by
subtracting their affine interpolant, but no such boundary is discarded
from (10)-(11).

## 6. Form domains and the original boundary still to be paid

For bounded compact smooth amplitudes, (1),(8) follow by common label,
spatial and Gamma cutoffs, followed by the complete posterior identities.
The actual amplitude has finite hidden and star forms by the centered
profile theorem. Its full refresh form is finite as well, because
A is bounded and T[c(a-m)^2]<=C beta, with int psi^2 beta finite.
The absolute signed storage is paid by

    |b| sigma^2 A^2 <=C[psi exp(x/2)+psi K]q_tail,

which is integrable at both the origin and infinity. Thus its adjoint
passage does not rely on separating any growing prime prefix.

The exact variance-metric theorem proves F belongs to the half-line
Gamma generator domain and has finite potential pairing. That proof applies directly to (6), including its bounded attenuated-prime
perturbation and the theta-paid full forcing in (10).
Smooth compact approximation in the weighted logarithmic form proves
(7). For (8), approximate D by the same cut amplitudes in its two finite
positive energies, and use the displayed absolute b bound. Both sides
then converge in their closed scalar/hidden forms. Equivalently the weak
product rule can be paired with the smooth psi^2 using its finite Gamma
commutator before removing the cutoff. No classical pointwise drift for
each unweighted higher label is presumed.

The full original boundary of the centered field is B_D, with Gamma wall,
all reflected primes and the original negative pole retained. Its exact
relation to (8) is

 2E_sp[D]-B_D
   =[E_full[D]+int b sigma^2 A^2]
       +[E_sp[D]-E_reset[D]-int b sigma^2 A^2-B_D].   (13)

The second bracket is NOT declared positive. The earlier strict centered
boundary factor already compares this same E_sp[D] with B_D; it cannot
be added to (9) as an independent gain. Likewise (11) still contains the
signed source-gradient and orthogonal residual. The paired cross theorem
retains their complete cooling/divisor and boundary terms. No full-form
contraction, elimination of the actual source, or K<=1 conclusion is
asserted by the projected storage identity.
