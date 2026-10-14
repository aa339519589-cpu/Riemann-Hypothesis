# A normalized all-divisor contraction in the true boundary-weighted space

This result removes the unbounded incoming sum Lambda(d)/d without dropping
any prime. The normalization is inside the genuine killed contrast potential,
not an estimate of its unnormalized forcing. Its exact score cancellation
also removes the origin singularity in the conjugating weight. The result
constructs a closed all-label transfer in L2(psi exp(x/2)dx), with the SAME
actual variance and explicit constants. The final signed Q comparison is
not inferred from boundedness of that transfer.

## 1. Exact normalized contrast and boundary metric

Use the frozen triangular contrast theorem, the complete score inequalities,
and the actual global current bounds from the preceding notes. Put

    mu(x)=psi(x)exp(x/2), nu_n=mu p_n, n>=2,
    X=direct_sum_(n>=2)L2(nu_n dx), Delta_1=0,
    T_n=(G_n+beta+L_n)^(-1)L_n.

The inverse is the genuine positive killed potential; pointwise
T_n1<=1. With v=w_1, the SAME actual contrast equation is

    Delta_n=T_n[(K Delta)_n+J_n v],
    (K Delta)_n=sum_(d|n)lambda_d Delta_(n/d)(x+log d)/L_n,
    J_n v=sum_(d|n)lambda_d v(x+log d)/L_n-P_n v(x).        (1)

All prime-power divisors and the full P_n probability remain. The symbol
J_n in (1) denotes the source-input operator only, not the finite Gamma
correction below.

## 2. The normalized killed potential has norm at most4/3

Set z=pi exp(2x), q_n=sP(n^2z), P(t)=4t^2-6t and

    B_n(z)=sum_(d|n,d>=2)Lambda(d)s(d^2z),
    L_n=B_n/s,
    A_n(z)=z^(1/4)sqrt(q_n L_n)
          =z^(1/4)sqrt(P(n^2z)B_n(z)).                    (2)

Here s is viewed as a function of physical z. The factor s cancels EXACTLY
from the last expression in (2). Since every true divisor d>=2, B_n is
positive and smooth even at z=pi.

The complete score bounds give, for t>=4pi>12,

    s(t)>=3t/2, s_t(t)<=9/4.

Indeed s>=k(t)=2t-9/2-6/(2t-3)>=3t/2, and the full posterior derivative
bound is s_t<=17/8+12/(2t-3)^2<9/4. Therefore

    B_n'/B_n<=3/(2z),
    P(n^2z)'/P(n^2z)<=15/(7z),
    A_n'/A_n<=29/(14z)<3/z.                               (3)

Consider the normalized metric m_n=nu_n/L_n. Its exact conjugation is

    h_n=z^(-1/4)sqrt(q_n/L_n)exp(-n^2z/2)Delta_n,
    m_n|Delta_n|^2dx=|h_n|^2dz/(2sqrt(pi)).                 (4)

As in the signed-weight inverse, the transformed equation is

    [G_[n^2/2]-E_n+a_n+beta+log n-(log2)/2]h_n
                        =t_n L_n f_n,
    t_n=z^(-1/4)sqrt(q_n/L_n)exp(-n^2z/2),                 (5)
    E_n h(z)=(1/2)int_0^infinity exp(-n^2v/2)
                    [A_n(z+v)/A_n(z)-1]h(z+v)dv/v.

By (3), A_n(z+v)/A_n(z)<=(1+v/z)^3. Both ordinary Lebesgue Schur rows
of E_n are therefore bounded by

    j*= (1/2)[3/(2*3)+3/(2^2*3^2)+2/(2^3*3^3)]=8/27.     (6)

For the column use z>=pi>3 before integrating v; no origin singularity
is hidden. Thus G_[n^2/2]+j*I-E_n has a nonnegative form, with its EXACT
Gamma difference, E1 half-line boundary, finite-kernel difference and
row/column remainder squares. Its residual potential is

    lambda_n=a_n+beta+log n-(log2)/2-j*>=a_n+beta>=3L_n/4, (7)

using log2>69/100 and L_n<=4a_n/3. The positive square completion is the
same ordinary Schur identity as in the critical inverse.

For bounded compact forcing f_n, the weak equation and (7) give

    (3/4)int nu_n|Delta_n|^2
       <=Re int nu_n conjugate(Delta_n)f_n,
    ||T_n f_n||_(L2(nu_n))<=(4/3)||f_n||_(L2(nu_n)).        (8)

All form-domain steps are lawful: h_n=O(z-pi) at the origin, since
q_n/L_n=s^2P(n^2z)/B_n, and its actual tail is Gaussian. For general L2
forcing, the positive closed form and its weighted dual yield the unique
weak solution, and bounded compact approximation extends (8). On bounded
forcing the positive killed formula identifies this solution: its normalized
forcing is bounded, T_n1<=1, and the surviving actual terminal is killed
at rate beta+L_n>=4log2. Hence the extension is the SAME T_n, not a new
boundary condition or generic original-P operator.

The exact lossless square from (5), including all its Gamma/origin/kernel
terms, remains valid. Estimate (8) is only the norm consequence needed
below; it does not spend an outgoing L_n on the forcing.

## 3. The true normalized child map contracts by the complete n^-3 sum

For every genuine divisor d|n, m=n/d, put y=x+log d. The exact density
identity is

    nu_n(x)lambda_d(x)=nu_m(y)Lambda(d)/d.

Crucially L_n>=lambda_d and s(y)/s(x)>d^2, so

    nu_n(x)lambda_d(x)/L_n(x)
                <=nu_m(y)/d^3.                            (9)

Jensen in the true divisor probability, followed by (9), proves

    ||K Delta||_X^2
       <=sum_(d>=2)d^(-3) ||Delta||_X^2
       <=(1/4)||Delta||_X^2.                               (10)

The sum may be enlarged to all integers only for this positive UPPER bound;
all genuine prime-power coefficients remain in the operator itself.
The elementary bound is sum_(d>=2)d^-3<1/8+int_2^infinity t^-3dt=1/4.
Zero label1 input is retained, and the conditions y>=log d are only enlarged
favorably. Consequently, with T=diag(T_n),

    ||T K||_(X->X)<2/3.                                  (11)

This is the closed complete all-label feedback. Replacing T_nL_n by an
unnormalized forcing estimate would instead produce sum Lambda(d)/d and
lose (9); those two estimates must not be interchanged.

## 4. Explicit bounded source input in the SAME boundary weight

For v in L2(mu), let Dv be the first, true-divisor average in Jv, and let
Pv=(P_n v)_(n>=2). Jensen and (9), now allowing every child label including1,
give

    ||D v||_X<=(1/2)||v||_(L2(mu)).                        (12)

Indeed sum_(m>=1)nu_m=mu, so the exact complete posterior is used after the
incoming change of variables.

For P, its stay atom contributes at most
q(x)mu(x)|v(x)|^2, with q=1-p_1<1/401. For its continuous part use
L_n>=4log2 and the exact full posterior identity

    sum_(n>=2)p_n(x)[q_1-q_n](x,dy)
       =kappa(y-x)psi(y)/psi(x)
                              [p_1(y)/p_1(x)-1]dy.         (13)

This is precisely the complete extra-Gamma row, not a sum of independent
label estimates. Relative to mu(y)dy its incoming coefficient is at most

    (1/[4log2])int_0^y
          [epsilon(y-t)-epsilon(y)]/[2sinh t]dt,
    epsilon=(1-p_1)/p_1.                                  (14)

The omitted denominator 1+epsilon(y) only enlarges this upper bound.
The full bounds epsilon<1/400 and -epsilon_z<=4epsilon give

    |epsilon'_x|<=224 z exp(-3z)<1/15.

Split (14) at t0=(1/400)/(1/15)=3/80 and at1. Since 2sinh t>=2t,
and int_1^infinity[2sinh t]^-1dt<1/2, its integral before the factor
1/(4log2) is at most

    (1/800)[2+log(80/3)]<1/150.

Here log(80/3)<10/3, as follows from exp3>20 and exp(1/3)>4/3.
Since log2>2/3, the continuous incoming coefficient is <1/400.
Therefore

    ||P v||_X^2<= (1/401+1/400)||v||_(L2(mu))^2
                         <=(1/200)||v||_(L2(mu))^2,
    ||J v||_X <=(1/2+1/sqrt(200))||v||_(L2(mu)).             (15)

No point-value sampling bound is assumed in (12): its integrated shifted
measure is changed exactly. Every continuous source-input and stay mass in
P is retained through Jensen.

## 5. Closed transfer, actual identification, and the variance it controls

Equations (8),(11),(15) construct the unique solution of (1) in X by
Neumann series, and give

    ||Delta||_X<=C_Delta ||v||_(L2(mu)),
    C_Delta=4(1/2+1/sqrt(200))<23/10.                       (16)

The actual contrasts already belong to X by the global logarithmic label
bound and complete Gaussian posterior. Thus uniqueness identifies this
solution with the SAME actual field. Every operator annihilates constant
input where appropriate, so (16) applies to v-c for any scalar constant.

The posterior mean has e=-sum_tail p_n Delta_n and q<1/401. Hence

    ||e||_(L2(mu))<=C_Delta/sqrt(401)||v-c||_(L2(mu))
                                      <=(23/200)||v-c||_(L2(mu)). (17)

Since u=v-e, this proves a genuine stronger-weight inverse, not merely the
previous sup-norm statement:

    ||v-c||_(L2(mu)) <=(200/177)||u-c||_(L2(mu)).             (18)

It is an L2(mu) current transfer. No bounded operator on the complete
original P source space is inferred. The exact SAME conditional variance
satisfies

    int mu V<=||Delta||_X^2
       <=C_Delta^2(200/177)^2 int mu|u-c|^2.                (19)

One must still retain its exact decomposition
V=|e|^2/epsilon+R_high from the tail-Schur note; (19) is a joint upper
bound, not an independent second expenditure of its two components.

The previously published COMPLETE boundary graph factorization gives
B_delta[u]>= (1/100)int mu|u-c_C|^2: its central margin9/50 pays exp(.35)<2,
its compact-tail margin1/4 through x=6 pays exp3<25, and its analytic
all-prime tail margin is >(291/10000)exp(x/2). Thus (19) is a genuine
finite transfer to an already signed original boundary norm. At an actual
top state B_delta[u]=2F[u] may be used with its full prime and pole terms.

The displayed constants do NOT yet yield the coefficient-one comparison
needed to exclude that state. In particular a large upper constant for
int(-b)_+V is not a favorable sign for Q_delta. The lossless normalized
Gamma/Jensen squares, exact source-input mixed terms, and the higher-tail
Schur structure are retained for the remaining signed completion.
