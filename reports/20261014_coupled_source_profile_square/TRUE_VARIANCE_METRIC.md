# The actual Mobius covariance principal in its true conditional-variance metric

The exact actual Mobius current equation has a coercive principal not only
in a de-Gaussianized auxiliary norm, but in the precise metric needed to
pair its residual with the same orthogonal projection amplitude. This
retains every prime-power diagonal and source term, the finite Mobius boundary, and
the exact half-line Gamma term. It does not sign its source-gradient,
collision or original-boundary forcing.

Use [the finite arithmetic projection](FINITE_PROJECTION.md),
[the reset facts](RESET_FACTS.md), and the published
[same-current centered profile/domain](../20261014_centered_mobius_profile/CENTERED_PROFILE.md)
and [exact residual cross](../20261014_centered_mobius_profile/RESIDUAL_CROSS.md).

## 1. Exact metric and finite-mask scope

Let a(n)=1-mu_ar(n), or for any N>=2 let a(n)=1-mu_ar(n)1_(n<=N).
In either case a(1)=0, a(2)=2 and 0<=a<=2. Put

    m=T a, M=T a^2, sigma^2=M-m^2,
    h=T[a(w-u)]=sigma^2 A,
    kappa_a=T[c(a-m)^2]/sigma^2.

Here c_n is the genuine positive refresh score, beta=T c. The SAME
actual projected current equation is

    P_a h=f=-S_a(u)+r+I_Z,
    P_a h=G_cont h+lambda_prime h+kappa_a h
                 +sum_(p prime)r_p theta_p(y)h(y),
    0<=theta_p=gamma_p/sigma^2<=1, y=x+log p,
    r=-T[c(a-m)Z],
    w-u=A(a-m)+Z, T Z=T(aZ)=0.                     (1)

The finite arithmetic theorem retains the complete cutoff union in theta_p
and I_Z. Every prime power remains in lambda_prime and S_a(u); only the
projected off-site covariance and residual of higher powers vanish.
All identities below retain this entire f. The metric is

    ||h||_var^2=int_0^infinity psi(x)^2 |h(x)|^2/sigma(x)^2 dx
                =int psi^2 sigma^2 |A|^2.          (2)

Thus its mixed forcing pairing is exactly int psi^2 A f, including the
same int psi^2 A r that occurs in the residual cross theorem. There is
no replacement of the current conditional variance by a canonical seed.

## 2. A complete-theta logarithmic bound for the metric

Write z=pi exp(2x), P(z)=4z^2-6z and

    r_n=p_n/p_1
        =n^2(n^2 z-3/2)/(z-3/2) exp[-(n^2-1)z], n>=2,
    k_n=(3/2)(n^2-1)/[(z-3/2)(n^2 z-3/2)].

Then -d_z log r_n=n^2-1+k_n, and for z>=pi>3,

    k_2=9/[2(z-3/2)(4z-3/2)]>9/(8z^2),
    k_2<=k_n<1/3,
    sum_(n>=3)(r_n/r_2)(n^2-4)<1/1000.             (3)

For the final complete tail use
r_n/r_2<=n^4 exp[-(n^2-4)z]/14. Its first n=3 term is at most
(405/14)exp(-15), and each successive ratio is at most8exp(-21)<1/2.
Since exp3>20, their total is less than 1/1000. This proof applies to
both the a and a^2 tilted weights because their n=2 weight is maximal,
and every other profile coefficient is at most that maximal weight.
In particular their tilted N^2 means are less than5.

Let R(z)=exp(3z)sigma(z)^2. We prove the uniform, full-mask bounds

    0<-d_z log R(z)<1/2.                            (4)

Here are all correction terms. Set A_j=sum_(n>=2)r_n a(n)^j,
T_2=exp(3z)A_2 and v=m^2/M. Then

    R=T_2 p_1(1-v), v<=q_tail<1/401,
    k_2<=-d_z log T_2<1/3+1/1000.                  (5)

The complete posterior bound q_tail<=28exp(-3z) gives

    0<d_z log p_1<130exp(-3z).                     (6)

Indeed d_z log p_1=sum_tail p_n(n^2-1+k_n)<sum_tail p_n n^2.
Its n=2 part is <=112exp(-3z), while the rest is bounded by
2exp(-3z)sum_(n>=3)n^6 exp[-(n^2-4)z]<exp(-3z).
The first term and the same geometric-ratio argument pay the latter
strict inequality. The weaker constant130 in (6) leaves ample margin.

Every tail p_n decreases. The tilted means just bounded, together with
k_n<1/3 and (6), give

    0<-m'/m<7, 0<-M'/M<7,
    |v'|/(1-v)<=21q_tail/(1-q_tail)<590exp(-3z).     (7)

Equations (5)-(7) imply

 d_z log R<=-9/(8z^2)+720exp(-3z)<0,
 -d_z log R<1/3+1/1000+590exp(-3z)<1/2.

For the first inequality use z^2 exp(-3z)<=9exp(-9)<9/8000;
720*9/8000<9/8. For the second use exp(-3z)<1/8000.
Thus every full posterior correction, including the subtraction m^2,
has been retained in (4). No Gaussian approximation of sigma^2 is used.

## 3. Exact operator conjugation

Let B=exp(x/2-z), q_psi=psi/B, g=q_psi h and

    ell(z)=[exp(-2z)/(2 sqrt(pi) sqrt(z) sigma(z)^2)]^(1/2),
    F(z)=ell(z)g(z)=psi(x)h(x)/[sqrt(2z)sigma(x)].

Then ||F||_L2(dz)=||h||_var exactly. The true-prime conjugation is

 q_psi P_a h=(G_B+beta+kappa_a+K_theta)g,
 K_theta g=sum_(p prime)(log p)exp[-(p^2-1)z]
                         theta_p(p^2z)g(p^2z).

Conjugating once more gives the exact equation

    [G_(3/2)+beta+kappa_a+c_* -J_R+K_(theta,R)]F=S,
    S=ell q_psi f, c_*=(1/2)log(3/2),                (8)

where

 G_(3/2)F=(1/2)int_0^infinity exp(-3v/2)[F(z)-F(z+v)]dv/v,
 J_R F=(1/2)int_0^infinity exp(-3v/2)
                         [A(z,v)-1]F(z+v)dv/v,
 A(z,v)=(1+v/z)^(1/4) sqrt[R(z+v)/R(z)],
 K_(theta,R)F=sum_(p prime)(log p)sqrt(p)exp[-3(p^2-1)z/2]
             sqrt[R(p^2z)/R(z)]theta_p(p^2z)F(p^2z).        (9)

Both ratios are genuine complete theta ratios. The PLUS prime sign is
retained: the projected operator is not a Markov generator. At finite N,
only primes p<=N have nonzero theta_p, but no prime-power source or
original diagonal is omitted. Equation (8) is the exact projected
principal, not a substitution of a different arithmetic character.

## 4. All-prime and continuous bounded defects

From (4),

    exp(-v/4)<=A(z,v)<=(1+v/z)^(1/4)<=1+v/(4z).

Since z>3, it follows that |A(z,v)-1|<=v/4. Hence the absolute J_R kernel
is bounded by exp(-3v/2)/8. Both half-line Schur rows are at most 1/12,
so

    ||J_R||_(L2(dz))<=1/12.                         (10)

The monotone R ratio and theta_p are at most 1 in the discrete kernel.
Dilation by d^2 has L2 norm1/d on this half-line; hence the complete
projected prime operator satisfies

 ||K_(theta,R)||<=sum_(d>=2)Lambda(d)/sqrt(d)
                                  exp[-3pi(d^2-1)/2]<1/120000.       (11)

The complete all-integer majorant in the published
[uncentered profile proof](../20261014_centered_mobius_profile/UNCENTERED_PROFILE.md) bounds
2sqrt2 times this sum by1/60000; (11) is its weaker immediate consequence.
No sign of the quadratic prime pairing is inferred from its positive
entries. Absolute values occur only in its certified bounded-operator
estimate. All prime powers remain in the untransformed diagonal and forcing.

## 5. Exact energy and its coercive consequence

For a real F in the generator domain the exact half-line Gamma identity is

 D_(3/2)[F]=Re<F,G_(3/2)F>
  =(1/4)int_(pi<z<y) exp[-3(y-z)/2]|F(z)-F(y)|^2/(y-z) dzdy
   +(1/4)int_pi^infinity E_1((3/2)(z-pi))|F(z)|^2 dz.          (12)

The E_1 term is positive and is not removed by changing metric. Pairing
(8) with F gives the EXACT original-variable equality

 int psi^2 A f
    =D_(3/2)[F]+int(beta+kappa_a+c_*)|F|^2
                     -Re<F,J_R F>+Re<F,K_(theta,R)F>.             (13)

The finite/full-mask reset theorem gives kappa_a>beta+2. Since
log(3/2)>2/5, (10)-(11) imply the useful uniform lower estimate

 int psi^2 A f
    >=D_(3/2)[F]+int(2beta+21/10)|F|^2.             (14)

The rational margin is 1/5-1/12-1/120000>1/10. Thus the exact forcing
in the TRUE conditional metric is coercive. The complete forcing is still f=-S_a(u)+r+I_Z. Thus (13)-(14) do
not sign the source-gradient or residual separately. Their exact signed
storage and actual alignment are proved in [STORAGE.md](STORAGE.md).
The principal coercivity is one budget, not an independent extra copy of
its hidden spatial or original-boundary energy.

## 6. The actual domain, not amplitude alone

The same-current projection theorem gives bounded A, while
sigma^2<=4q_tail=O(exp(-3z)). Thus h=sigma^2 A has the correct tail,
F=O(poly(z)exp(-5z/2)), and F is bounded and L2(dz). At the origin
q_psi=O(x), sigma(0)>0, and h is bounded/continuous, so F=O(x).
The genuine score and the normally convergent profile-weighted theta
moments give beta+kappa_a=O(1+1/x). Consequently
(beta+kappa_a)F is L2. This last fact is used, not an implication from
pointwise Gaussian decay to the Gamma generator domain.

The complete forcing envelopes recorded in [RESET_FACTS.md](RESET_FACTS.md)
are uniform in the allowed masks. After multiplication by ell q_psi they
are bounded and L2: at infinity the original polynomial exp(-3z) envelope
gains only exp(z/2) times polynomial factors, and at the wall the factor
q_psi=O(x) pays the full 1/x forcing. In particular S in (8) is L2.
The already established local weak current equation transforms by the
smooth positive ell on every compact interior interval. Since J_R,K_(theta,R)
are bounded and the potential times F is L2, (8) implies the distributional
G_(3/2)F belongs to L2. Here is an explicit weak-to-generator argument,
which does not assume an endpoint condition. Extend F by zero to z<pi.
For z=pi-r<pi its full-line Gamma image is the Hankel row

    -(1/2)int_0^infinity exp[-(3/2)(r+t)]F(pi+t)/(r+t)dt.

This is L2-bounded by the Carleman operator norm pi/2. Inside the
half-line the image is the just-proved L2 distribution. The full-line
logarithmic Fourier multiplier maps L2 into H^(-epsilon) for every
epsilon>0. The difference between its image and these two L2 pieces
would be supported only at pi. No nonzero point-supported distribution
belongs to H^(-epsilon) for epsilon<1/2, so this difference is zero.
The full multiplier is consequently L2, placing the zero extension in
its closed full-line generator domain. Restricting the future Gamma
semigroup identifies F in D(G_(3/2)) on the half-line. This semigroup
uses only future values and imposes no origin boundary condition.
Thus (12)-(13) are genuine operator pairings, not merely
lower-semicontinuity inequalities.

All common finite label/divisor boundaries remain in (1) and its forcing.
Taking N to infinity is justified by the same complete Gaussian bounds,
while (4),(10),(11),(14) are uniform. The full original Q_delta and K<=1
remain unproved. This note closes precisely the weighted pairing needed
by the centered profile's exact mixed reset residual.
