# An all-integer Euler bound for positive first-label child transport

This is a positive all-prime Gamma/divisor transport estimate, with every
prime power retained. It uses the normalized killed inverse, rather than
spending its full outgoing row in scalar Cauchy. The resulting arithmetic
majorant is exactly multiplicative and sums to less than7/5. It concerns
one honest positive component of the actual current construction; the
complete common forcing and first-label reference correction are not
silently identified with this component.

## 1. The normalized potential input and the exact child geometry

Use the full eta-score hidden lift and the notation of
[the exact triangular current theorem](TRIANGULAR_CURRENT_CONTRAST.md). Put

    nu_n(x)=psi(x)exp(x/2)p_n(x),
    L_n(x)=sum_(d|n,d>=2)lambda_d(x),
    lambda_d=Lambda(d)s(x+log d)/s(x),
    R_n=(G_n+beta+L_n)^(-1), n>=2.

The [normalized-potential theorem](NORMALIZED_BOUNDARY_TRANSFER.md) proves

    ||R_n L_n||_(L2(nu_n)->L2(nu_n))<=4/3.           (1)

Only this precise operator theorem is used below. In particular an energy
estimate with an unnormalized Ln forcing would NOT be a substitute for
(1). All quantities have the original operational entrance meaning.

For y=x+log d and n=dm, a direct cancellation of the true theta factors
is EXACT:

    nu_n(x)lambda_d(x)dx=[Lambda(d)/d]nu_m(y)dy.      (2)

The complete source score inequality s'-2s>3 gives
s(x+log d)/s(x)>d^2. Consequently, with the arithmetic number

    A_n=sum_(d|n,d>=2)Lambda(d)d^2>0,

one has L_n(x)>=A_n, and (2) yields

    nu_n(x)[lambda_d(x)/L_n(x)]dx
                <=[Lambda(d)/(d A_n)]nu_m(y)dy.      (3)

The lower cutoff y>=log d remains in the actual pushforward; enlarging it
to y>=0 is used only for a nonnegative upper norm bound. No reciprocal
prime sum replaces (3).

## 2. The honest positive homogeneous extension

For bounded initial first-label data v define

    Y_1 v=v,
    Y_n v=R_n L_n{sum_(d|n,d>=2)
                         [lambda_d/L_n]E_(log d)Y_(n/d)v}.   (4)

This is a finite triangular recursion for each n. Probabilistically it is
the genuine hidden continuous/divisor process killed at its first reset
candidate, with terminal value v at its first arrival at label1. Thus Y_n
is positive and sub-Markov. In particular |Y_n v|<=||v||infinity. No reset
re-birth is deleted from the actual full current: (4) is explicitly the
first-reset-killed component only.

Write E_n=||Y_n v||_(L2(nu_n))^2, c=(4/3)^2=16/9. Combining (1), Jensen
for the true divisor probabilities, and (3) gives

    E_n<= (c/A_n)sum_(d|n,d>=2)[Lambda(d)/d]E_(n/d).           (5)

Every prime-power divisor participates in this sum. Bounded v in L2(nu_1)
can be approximated by compact data; positivity and (5) extend the
operators and the theorem to arbitrary L2(nu_1) data.

Define C_1=1 and the exact scalar majorant recursively by equality in

    C_n=(c/A_n)sum_(d|n,d>=2)[Lambda(d)/d]C_(n/d).             (6)

Induction proves E_n<=C_n E_1. These are majorant constants, not a claim
that every step of the operator estimate is simultaneously sharp.

## 3. The complete arithmetic recursion is multiplicative

Put D_n=n^3 C_n. Equation (6) becomes

    D_n=(c/A_n)sum_(d|n,d>=2)Lambda(d)d^2 D_(n/d).             (7)

Since Lambda is supported on prime powers,
A_n=sum_(p^v||n)(log p)sum_(j=1)^v p^(2j). For a prime p define

    D_(p^0)=1,
    D_(p^v)=c [sum_(j=1)^v p^(2j)D_(p^(v-j))]
                                      /[sum_(j=1)^v p^(2j)]. (8)

Then D_n=product_(p^v||n)D_(p^v) solves (7): for each active p, its
prime-power sum in (8) contributes exactly its summand in A_n times the
full product. Summing p and dividing by A_n proves (7). Triangular
uniqueness therefore gives the claimed multiplicativity for ALL n.

This calculation is the full Lambda divisor algebra. It is not a
factorization obtained by discarding composite labels or by bounding
each prime independently before accounting for the shared denominator.
In particular

    sum_(n>=1)C_n=product_p[sum_(v>=0)D_(p^v)p^(-3v)]         (9)

once convergence is proved below. Positive monotone finite-prime products
justify (9); no bilateral or conditionally convergent interchange occurs.

## 4. A complete exact bound less than7/5

Set r=p^(-2), T_v=sum_(k=0)^(v-1)r^k, and write D_v=D_(p^v).
The recurrence gives D_1=c and

    D_(v+1)/D_v=1+(c-1)r^v/T_(v+1), v>=1.

Thus, using T_(v+1)>=1+r,

    D_v<=c exp[(c-1)r/(1-r^2)].                    (10)

For p=2 the exponent is28/135; the elementary exponential bound
exp(28/135)<99/80 gives D_v<11/5. For p>=3 it is at most7/80, and
exp(7/80)<9/8 gives D_v<2. Retaining D_1=c separately, the p=2 factor is

    U2<=1+c/8+(11/5)sum_(v>=2)2^(-3v)
       =1+2/9+11/280.                              (11)

For every p>=3 its factor is at most
1+c/p^3+2/[p^6(1-p^(-3))]. Use log(1+t)<=t and enlarge the odd primes to
ALL odd integers>=3 only in this positive upper bound. The complete sums
obey

    S3:=sum_(odd n>=3)n^(-3)
           <=1/27+1/125+1/100,
    S6:=sum_(odd n>=3)n^(-6)
           <=1/729+1/15625+1/31250.

The tails come from half the integral on[5,infinity); they are not finite
numerical cutoffs. Since2/(1-p^(-3))<=27/13,

    product_p sum_v D_(p^v)p^(-3v)
      <=[1+2/9+11/280]exp[c S3+(27/13)S6]<7/5.       (12)

The accompanying fractions-only checker proves both exponential bounds
and the final strict rational inequality with a positive Taylor remainder.
It is not a test over finitely many integer labels.

Consequently the complete positive extension satisfies

    sum_(n>=2)||Y_n v||_(L2(nu_n))^2
                         <=(2/5)||v||_(L2(nu_1))^2. (13)

This gives a genuine all-integer contraction from first-label input to
its entire first-reset-killed child field, with squared norm below2/5.

## 5. The full actual current forcing remains separate

The actual current W_n v is NOT Y_n v. Its exact equations are

    W_n v=R_n{sum_(d|n)lambda_d E_(log d)W_(n/d)v
                                      +(G_1+beta)v}, n>=2,  (14)

with W_1v=v. The common forcing in (14) follows from the n1 equation;
it includes the complete signed first-label drift and reset contribution.
Equivalently, in contrast coordinates it is the already proved
R_n L_n[child v-P_n v], which annihilates constants. For arbitrary bounded
v the latter is the valid kernel construction; (14) is asserted only on
the actual extended/common generator domain.

The remaining first-label reference forcing may not be dropped, declared
positive, or charged to the homogeneous bound (13) for free. Nor does
(13) identify the resulting norm with E_current, the safe-xi component,
or the original signed B_delta graph. It is a new positive transport
component that retains the exact complete divisor geometry needed for
that remaining joint comparison.
