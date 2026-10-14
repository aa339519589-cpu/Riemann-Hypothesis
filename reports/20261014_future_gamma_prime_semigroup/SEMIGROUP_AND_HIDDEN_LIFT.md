# An explicit positive semigroup for the complete future Gamma-plus-prime generator

This is a constructive full future identity. It preserves the complete Gamma
and Mangoldt contributions in one positive transition kernel, rather than
assuming a Gamma-only joint divisibility coupling. It does not remove odd
reflection, the eta/Phi differential ladder, or the finite pole correction.
Those are separate requirements before any original signed-form conclusion.

## 1. Definitions

For z>0 put

    theta(z)=sum_(n>=1)exp(-n^2 z),
    (T w)(z)=theta(z)^(-1)sum_(n>=1)exp(-n^2 z)w(n^2 z).

The operator T is a Markov conditional average on bounded measurable w.
For t>0, a=t/2, define the complete arithmetic coefficients

    J_t(k)=sum_(d|k)mu(d)d^(-t)
          =product_(p|k)(1-p^(-t)),   J_t(1)=1.

Thus J_t(k)>=0. Two exact finite-divisor identities are

    sum_(d|n)d^(-t)J_t(n/d)=1,                         (1)
    sum_(d|n)d^(-t)J_s(d)J_t(n/d)=J_(s+t)(n).          (2)

They follow by checking prime powers and multiplying over distinct primes.
In particular d/dt J_t(k)|_(t=0+)=Lambda(k) for k>=2; labels having two or
more distinct prime factors have zero first derivative, not zero finite-t
coefficient.

Define a positive kernel by

    (P_t f)(z) = 1/[Gamma(t/2)theta(z)]
        sum_(k>=1) J_t(k) integral_0^infinity
           v^(t/2-1) theta(k^2 z+v) f(k^2 z+v) dv.     (3)

No signed Mobius sum appears in (3). We set P_0=I.

## 2. Exact stochastic normalization and semigroup law

For f=1, expand theta in (3) and integrate the positive exponentials:

    P_t1(z)=theta(z)^(-1)
       sum_(k,j>=1)J_t(k)j^(-t)exp(-(kj)^2 z)=1,

where the last equality is (1). All exchanges are justified by Tonelli.
Thus (3) defines a Markov contraction on bounded measurable functions.
For bounded signed or complex f, every exchange below is absolutely bounded
by the same positive expression for ||f||_infinity.

To compose P_t and P_s, let a=t/2,b=s/2. Their theta factors cancel. In
the resulting double integral replace the first integration variable u by
w=l^2 u. With n=kl the coefficient becomes

    sum_(l|n) l^(-t)J_s(l)J_t(n/l).

The beta convolution in w,v turns w^(a-1)v^(b-1)/(Gamma(a)Gamma(b)) into
q^(a+b-1)/Gamma(a+b). Equation (2) therefore gives exactly

    P_t P_s=P_(t+s).                                  (4)

This proves the semigroup directly. It does not rely on a critical-line
inverse-zeta multiplier, an unproved inverse domain, or cancellation of an
infinite signed double sum.

For every z_0>0 this is a strongly continuous positive contraction semigroup
on C_0([z_0,infinity)). It preserves C_0 because its transition support is
contained in [z,infinity). For strong continuity, the k=1 mass tends to one
uniformly for z>=z_0, by

    1-theta(z)^(-1)sum_j j^(-t)exp(-j^2z)
       <=t theta(z)^(-1)sum_j(log j)exp(-j^2z)<=C_(z0)t.

Within this k=1 term the first moment of v is at most t/2. Uniform continuity
of a C_0 function, followed by Markov's inequality for this first moment,
pays the remaining displacement. The terms k>=2 have total mass O_(z0)(t).
Continuity for fixed t follows from the same normally convergent positive
series and integral on compact z-intervals.

## 3. The complete generator

Write P_t=exp(-t L_theta). On C_c^1([z_0,infinity)), with the right derivative
at z_0, the generator is

    L_theta f(z)
      = (1/2)integral_0^infinity theta(z+v)/theta(z)
                   [f(z)-f(z+v)] dv/v
        +sum_(k>=2)Lambda(k)theta(k^2z)/theta(z)
                   [f(z)-f(k^2z)].                    (5)

Both differences are retained. The Gamma integral is finite at zero by the
C^1 assumption and at infinity by the theta tail; the complete prime sum is
absolutely convergent locally uniformly in z>=z_0.

Here is the exact diagonal balance in differentiating (3). For a decaying
C^1 function H,

    d/da [Gamma(a)^(-1)integral_0^infinity
                  v^(a-1)H(z+v)dv]_(a=0+)
       =integral_0^infinity[H(z+v)-exp(-v)H(z)]dv/v.

Taking H=theta f, the k=1 derivative supplies this integral with coefficient
1/2; the k>=2 derivatives supply the full Lambda sum. The terms proportional
to f(z) combine by the identity

    (1/2)integral_0^infinity
         [theta(z+v)/theta(z)-exp(-v)]dv/v
       =-theta(z)^(-1)sum_n(log n)exp(-n^2z)
       =-sum_(k>=2)Lambda(k)theta(k^2z)/theta(z).        (6)

The second equality is precisely log n=sum_(k|n)Lambda(k). Equation (6)
produces (5), with no divergent prime diagonal separated from its row.
For a direct uniform justification of differentiation, J_t(k)<=t log k
for k>=2 and 0<t<=1, since J_t(k)<=1-p^(-t)<=t log p<=t log k
for any prime p dividing k. This estimate and
the Gaussian-in-k tail dominate the k>=2 derivative series. The k=1
Gamma limit is uniform on compact z-intervals; outside the support of f,
both the semigroup and generator vanish because transitions move forward.

## 4. Positive intertwining with an ordinary gamma subordinator

Let

    (G_t w)(z)=1/Gamma(t/2) integral_0^infinity
                    u^(t/2-1)exp(-u)w(z+u)du.

This is the usual additive gamma-subordinator semigroup of shape t/2 and
rate one. Directly from (3), expand T inside P_t T, set u=n^2 v, and group
the integer product r=kn. Identity (1) gives

    P_t T=T G_t                                         (7)

for every bounded measurable w. The proof is positive for w>=0 and absolutely
convergent for bounded w. It avoids asserting that the inverse of T is a
bounded map on any Hardy or original-source Hilbert space.

Its generator is

    L_B w(z)=(1/2)integral_0^infinity
                     exp(-u)[w(z)-w(z+u)]du/u.

Consequently L_theta T=T L_B on the corresponding controlled generator core.
All identities also hold for fixed polynomial-growth w, by positive theta
and gamma moment domination, with locally uniform convergence.

## 5. Exact return to the physical future generator

Put z=pi exp(2x), B(x)=exp(x/2)exp(-pi exp(2x)) and
Theta(x)=sum_n n^(-1/2)B(x+log n)=exp(x/2)theta(z).
Then (5) becomes

    L_Theta f(x)
      =integral_0^infinity kappa(h)Theta(x+h)/Theta(x)
                    [f(x)-f(x+h)]dh
        +sum_(n>=2)alpha_n Theta(x+log n)/Theta(x)
                    [f(x)-f(x+log n)],                (8)

where kappa(h)=exp(-h/2)/(1-exp(-2h)) and alpha_n=Lambda(n)/sqrt(n).
Indeed v=z(exp(2h)-1) makes the continuous kernel in (5) exactly the first
kernel in (8). For the Gaussian B, the same substitution u=z(exp(2h)-1)
reduces its Doob future Gamma kernel to exp(-u)du/(2u), explaining the
ordinary gamma subordinator in (7).

Thus (3) is the honest Markov semigroup for the full future Gamma-plus-prime
operator proposed by the Gaussian arithmetic intertwining, with all prime
powers preserved.

## 6. A hidden integer-death and gamma-process realization

The construction admits a direct positive arithmetic path model. Conditional
on Z_0=z choose N_0 with probability exp(-n^2z)/theta(z), and set Y_0=N_0^2z.
Conditional on this initial state, use mutually independent gamma increments
and integer death clocks, independent also of the initial sampling. Let
Y_t-Y_0 be the additive gamma subordinator of shape t/2 and rate one, and
let N_t be the integer pure-death chain with transitions

    n -> n/k at rate Lambda(k), for each prime power k dividing n.

Its total exit rate is sum_(k|n)Lambda(k)=log n. Every path makes at most
floor(log_2 N_0) integer jumps, so this chain is nonexplosive. Its exact
transition probabilities are

    Prob(N_t=d | N_0=n)=d^(-t)J_t(n/d), d dividing n.    (10)

Their sum is one by (1), their composition law is (2), and their right
zero-time derivative is exactly the stated prime-power rate. Thus no
truncation or infinitesimal heuristic is needed to specify the chain.

Set Z_t=Y_t/N_t^2. If N_0=dk and N_t=d, put
u=d^2(z'-k^2z) in the gamma density. The factor d^(-t) in (10) cancels the
Jacobian and power factor d^(2a), since 2a=t. Hence the joint endpoint law
has density

    Prob(Z_t in dz', N_t=d | Z_0=z)/dz'
      = exp(-d^2z')/[Gamma(a)theta(z)]
          sum_(k: k^2z<z')J_t(k)(z'-k^2z)^(a-1).       (11)

Summing (11) over d gives precisely (3). More importantly, its factorization
proves the conditional law

    Prob(N_t=d | Z_t=z')=exp(-d^2z')/theta(z').          (12)

For precision, let H=(N,Y), let Q_t denote the hidden product semigroup,
let pi(H)=Y/N^2, and let Lambda_z be the probability supported on the fiber
{(n,n^2z)} with masses exp(-n^2z)/theta(z). Equation (11) for EVERY starting
z is exactly the kernel identity Lambda Q_t=P_t Lambda on bounded hidden
observables. Moreover Lambda M_(f composed with pi)=M_f Lambda for every
bounded observed function f. Applying these two identities successively
proves by induction the filtering posterior (12) after conditioning on any
finite observed-time cylinder, with the current observed value included.
A monotone-class argument extends from these cylinders to the sigma-field
generated by rational past observation times and the current time. Hidden
and observed paths are cadlag, so this is the entire natural observed
filtration. Thus (12), and the Markov law with semigroup P_t, hold with the
full observed past retained. This is a genuine filtering identity for the
complete process, not the stronger, and generally invalid, Gamma-only
simultaneous-divisibility coupling law.

The two rates can also be checked directly. Conditional on N=d, an additive
gamma jump of Y by u=d^2v induces a Z jump by v with Levy density
exp(-d^2v)dv/(2v). Averaging by (12) gives exactly

    theta(z+v)/theta(z) dv/(2v).

An integer death by a prime-power quotient k sends Z to k^2z, at rate
Lambda(k) times Prob(k divides N | Z=z), namely

    Lambda(k)theta(k^2z)/theta(z).

These are the two complete conductances in (5). The arithmetic matching
therefore follows from the proved joint process; it is not inferred merely
from agreement of a scalar logarithmic transport cost.

## 7. Polynomial ladder and remaining signed interface

The actual even and odd theta seeds are obtained from B using

    q(z)=4z^2-6z,
    c(z)=8z^3-30z^2+15z,
    eta(x)=B(x)q(z),  xi(x)=B(x)c(z).

Their arithmetic averages satisfy

    Phi/Theta=Tq,   psi/Theta=Tc.

The additive gamma generator acts on these polynomials by exact identities

    L_B q=1-4z,
    L_B c=-3q-1/2.                                   (9)

The second polynomial c changes sign in a short interval above z=pi; its
arithmetic average psi vanishes at x=0 and is positive only on the positive
wing. Thus neither the odd seed nor the original reflected problem becomes
a positive marginal merely by applying (7).

Equations (3)-(9) are a full future construction, not a similarity proof of
positivity in the original source metric. The reflection x->-x, the theta
functional-equation boundary terms, the derivative ladder, and the complete
pole contribution must all be retained in a proposed signed comparison.
In particular no forbidden exact Gamma-only joint-divisibility coupling is
claimed by (7).
