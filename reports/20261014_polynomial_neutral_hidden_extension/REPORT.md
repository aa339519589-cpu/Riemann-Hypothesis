# A global hidden extension for polynomial neutral ratios

The individual zero-discount currents of a polynomial neutral ratio need
not exist. This theorem instead retains the exact finite-horizon terminal
and integral together. It constructs a global field of the SAME full eta
lift, with the prescribed posterior mean and label-independent drift.
It does not declare the new source actual-null, and it retains every
neutral forcing, conditional-variance cross and polynomial terminal.

## Scope and published prerequisites

This report proves the weighted inverse and full finite-horizon extension,
including its original weighted form passage. It uses the already
constructed [full eta hidden lift](../20261014_first_label_current_approximation/HIDDEN_LIFT.md),
[operational entrance](../20261014_first_label_current_approximation/ENTRANCE.md),
and [triangular probability/killed kernels](../20261014_same_current_boundary_transfer/TRIANGULAR_CURRENT_CONTRAST.md).
The complete score estimates are in
[the second-label theorem](../20261014_first_label_coercive_correction/SECOND_LABEL_COMPLETION.md).
The original first-label and bounded-mask domains are proved in
[the first-label domain theorem](../20261014_first_label_current_approximation/DOMAIN.md)
and [the arithmetic mask theorem](../20261014_centered_mobius_profile/BOUNDED_MASK_DOMAIN.md).
For the observed escape and operational clock, see
[forward rays](../20261014_positive_reflected_storage/FORWARD_RAYS.md) and
[operational rays](../20261014_coherent_prime_ray_bridges/COHERENT_OPERATIONAL_RAY_CURRENTS.md).
These prerequisites fix the same theta functions, source and all-prime
normalizations throughout; no changed lift is introduced.

The exact rational script [check_polynomial_hidden_extension.py](check_polynomial_hidden_extension.py)
reproduces the complete continuous-barrier constants, the positive Taylor
bound and the full geometric label-tail bound. Run it with Python 3; its
output is generated locally and is not part of the proof package.

## 1. Rates, weights and the exact problem

Use z=pi exp(2x), P(z)=4z^2-6z, s=psi/Phi, p_n the full eta posterior,
and c_n the positive refresh score, with beta=T c=K/psi. The positive
hidden generator A has continuous rates

 q_n(z,dv)=exp(-n^2 v) P(n^2(z+v))/P(n^2z)
                            *s(z+v)/s(z) dv/(2v),

true divisor transitions (z,n)->(d^2z,n/d) at
lambda_d=Lambda(d)s(d^2z)/s(z), and full refresh rates p_m c_m.
Every prime power d|n is included. Its observed generator is G=G_psi,
and the exact posterior link is T A=G T. At the origin use the already
constructed operational clock theta=exp(-x/2)psi, multiplying BOTH
hidden and observed generators by theta.

Put epsilon=1/100 and

 X_epsilon={v continuous on [pi,infinity):
                  ||v||_epsilon=sup_z exp(-epsilon z)|v(z)|<infinity}.

The triangular kernels, already defined including their operational
origin, are

 L_n=sum_(d|n,d>=2)lambda_d,
 P_n=[(c_n-c_1)delta_z+(q_1-q_n)]/L_n,
 R_n=(G_n+beta+L_n)^(-1), n>=2.

P_n is a probability, q_1-q_n is a positive FINITE measure, and all R_n
are genuine positive killed potentials. Define recursively

 W_1 v=v,
 D_n v=R_n{sum_(d|n,d>=2)lambda_d E_d W_(n/d)v-L_n P_n v},
 W_n v=v+D_n v, E_d v(z)=v(d^2z).                   (1)

The theorem first extends these EXACT kernels to X_epsilon. No new
kernel, posterior or current source is chosen.

## 2. Complete exponential barriers, including the wall scale

The complete posterior and score estimates imply

 s_z<=4, beta>=3/s,
 L_n>69/25+621/(200s), n>=2.                        (2)

For the first assertion use the exact score formula
s=E_p k(n^2z), k(t)=2t-9/2-3/(t-3/2). Differentiating the complete
posterior gives

 s_z=E_p[n^2 k'(n^2z)]-Var_p(k)/(2z)
        <=(10/3)E_p n^2<4.

Indeed E_p n^2-1<=2 sum_(n>=2)n^6 exp[-3(n^2-1)]
<256/8000<1/16: the consecutive tail ratio is less than1/2 and exp3>20.
The beta bound follows from beta=(3+Theta/(2Phi))/s. For L_n choose any
prime factor of n and use the already proved s_x-2s>3. Integrating this
inequality over log d gives
s(d^2z)>=d^2s(z)+(3/2)(d^2-1). Since d>=2 and log2>69/100,
(2) follows. The estimates retain their finite operational limits at s=0.

Let V_n(z)=exp(epsilon n^2z). For n>=2, Y=n^2z>=12 and

 P(Y+t)/P(Y)<=1+(5/28)t+t^2/126,
 s(z+t/n^2)/s(z)<=1+t/s(z).

In the continuous generator substitute t=n^2v. The elementary integrals
of exp(-t)(exp(epsilon t)-1) times polynomials give

 (-G_n V_n)/V_n <1/100+1/(100s), n>=2.              (3)

All bounds in (3) are for the COMPLETE integral, not a finite v cutoff.
For reproducibility, with q=99/100 put

 A(a,b)=[-log q+a(q^(-1)-1)+b(q^(-2)-1)]/2,
 B(a,b)=[q^(-1)-1+a(q^(-2)-1)+2b(q^(-3)-1)]/2.

Use -log q<=1/99. At a=5/28,b=1/126, both A and B are less than1/100,
which proves (3). For n=1 use a=1,b=2/9 and the s ratio1+4v/s.
The same exact rational estimates give

 (-G_1 exp(epsilon z))/exp(epsilon z)<1/50+1/(10s). (4)

Since q_1-q_n is positive and bounded by q_1,

 P_n exp(epsilon z)
  <=exp(epsilon z)[1+(1/50+1/(10s))/L_n]
  <=(31/30)exp(epsilon z)<2V_n(z).                 (5)

Equations (2)-(3) also imply

 (G_n+beta+L_n)V_n >=(L_n/2)V_n,
                  R_n(L_n V_n)<=2V_n.             (6)

The last assertion follows from stopped positive Feynman--Kac and
monotone convergence: the nonnegative terminal is RETAINED in proving
the upper bound, not assumed to vanish. The estimates are unchanged
when multiplied by theta, so (5)-(6) apply to the actual operational
origin kernels as well.

## 3. A complete weighted inverse, with no label truncation

Induction on Omega(n) in (1), using (5)-(6), proves

 |W_n v(z)|<=(6*2^Omega(n)-5)||v||_epsilon V_n(z)
             <=(6n-5)||v||_epsilon V_n(z),
 |D_n v(z)|<=(6n-4)||v||_epsilon V_n(z).            (7)

For the induction the child constant C is replaced by at most2C+5,
starting from C=1. The recursion always goes to a proper divisor, so
this covers every true divisor and does not select a single prime path.

Let K v=sum_(n>=2)p_n D_n v and H=I+K. The complete theta bound
p_n<=2n^4 exp[-(n^2-1)z] yields

 ||K||_(X_epsilon->X_epsilon)
 <=2 sum_(n>=2)n^4(6n-4)exp[-(297/100)(n^2-1)]
 <256/19^3+4536/19^8<1/25.                         (8)

Here exp(297/100)>19, verified by a positive finite Taylor lower sum.
The n=2 term is displayed separately. For n>=3 the first term is
2268/19^8 and the complete consecutive ratio is less than
5/19^7<1/2. Thus (8) includes the entire n>=3 tail, not a finite
numerical check. It follows that

    H^(-1)=sum_(j>=0)(-K)^j                         (9)

converges in X_epsilon and is future-supported. As in the bounded
construction, neither H nor its inverse is asserted positive.

For a prescribed continuous polynomial-growth ratio u, define

    v=H^(-1)u, w_n=W_n v.                          (10)

Then T w=u exactly. Uniform weighted convergence and the Feller
properties of the already constructed killed kernels give continuous
versions on the whole operational state space. At fixed x all moments
used below converge absolutely, since (7) has exponent epsilon n^2z
whereas the posterior has exponent -(n^2-1)z.

More precisely, H_n=w_n-u satisfies

 |H_1(z)|=|v(z)-u(z)|<=C_u exp[-(3-4epsilon)z],
 V_u(z):=T|H|^2<=C_u exp[-(3-8epsilon)z].           (11)

Polynomial factors can be absorbed into C_u after decreasing either
positive exponent slightly; alternatively keep the exact complete
Gaussian sums from (7). Formula (11) follows by factoring the n=2
exponent from sum p_n|D_n v| and sum p_n|D_n v|^2, respectively.
The mean-zero variance can be bounded by sum_(n>=2)p_n|w_n-w_1|^2.
There is no claim that w itself is a bounded field.

## 4. A useful class of prescribed inputs

For the generator and form assertions below assume u is C^2 up to the
wall in z, and u and its first two derivatives have polynomial growth.
This includes every fixed theta-jet ratio needed here, in particular

    nu=s1/psi, s1=psi''-psi/4,
    nu(z)=4z^2+O(z), z->infinity.

At zero, psi and s1 are odd with psi'(0)>0, so their quotient extends
smoothly. At infinity the complete theta series and all its derivatives
are normally convergent, giving the displayed polynomial bounds.
Every psi u in this class has the original forward, reflected and pole
form domains. It is NOT asserted to be an actual Q_delta-null source.

## 5. Extended-generator identification, not a formal H conjugacy

The exact finite-rate relation is

 L_n(v-P_n v)=(G_1-G_n)v.                           (12)

The difference kernel is finite even for locally bounded v. Combining
(1) with (12), initially distributionally on a compact positive spatial
interval, gives

 (A w)_n=G_1v-Sv for every n,
 Sv=sum_(n>=2)p_n c_n D_n v.                        (13)

The complete posterior/score bounds and (7) make Sv locally normally
convergent. Theta*Sv extends continuously through the wall; its tail
has polynomial times exp[-(3-4epsilon)z] decay. The posterior intertwining,
applied at a common spatial/label/jump cutoff and then passed using
these complete envelopes, identifies (13) as

       A w=U G u.                                 (14)

Here U embeds a scalar field as a constant label field. In the weak
passage the small-jump derivative is transferred to a compact smooth
test; its O(h) increment pays the 1/h kernel. Only complete common
cutoffs are removed. The exponential margin 1-2epsilon>0 pays all
future and label tails. Thus (14) does not assume G_1v exists merely
because v is continuous.

For completeness, its first-label domain can be identified explicitly.
Set q1=S1/B, S1=psi p1, B=exp(x/2-z). The exact identity is

 G_B(q1 v)=q1[G_1v-c_1v],
 G_B f=(1/2)int exp(-t)[f(z)-f(z+t)]dt/t.

For any fixed epsilon<a<1, F=exp(-az)q1v belongs to L2 and has zero
trace at z=pi. The distributional equation (13)-(14) becomes

 [G_(1-a)+(1/2)log(1-a)]F
       =exp(-az)q1[Gu+Sv-c_1v],                   (15)

with an L2 right side. The wall factor q1=O(x) pays the complete1/x
forcing; at infinity u is polynomial and (11) pays the correction.
Here the half-line generator is the same closed Gamma generator used in
[the Gaussian inverse theorem](../20261014_first_label_coercive_correction/COERCIVE_INVERSE.md),
with rate exp[-(1-a)t]/(2t). To identify its maximal domain, extend F by
zero below pi. On the negative side its image is a Hankel integral with
kernel bounded by 1/[2(v+t)]; the L2 Carleman inequality bounds this by
(pi/2)||F||_2. The distributional whole-line image is therefore L2 away
from the endpoint. A logarithmic Fourier multiplier maps L2 into every
H^(-eta), eta>0, whereas a nonzero endpoint-supported distribution is
not in H^(-eta) for eta<1/2. There is consequently no missing endpoint
mass, and the whole-line closed multiplier puts F in the maximal domain
of the half-line G_(1-a).
This identifies v in the local extended G_1 domain. Equation (12) then
places it in each G_n domain, and the genuine killed-potential equation
for D_n places every w_n in the full extended hidden domain.

At x=0 use theta A. All spatial small-jump kernels there have a finite
first increment moment, and the operational reset/divisor rows are
finite with uniformly Gaussian label tails. The continuous versions
and the grouped limits above identify (14) through the honest origin
process; no reflecting or absorbing boundary condition is inserted.

## 6. Why the exact finite-horizon terminal cancels lawfully

The following bounds justify finite-horizon Dynkin rather than an
unproved infinite-current integral. Let Y=n^2z. True divisor jumps leave
Y EXACTLY invariant. A continuous jump changes Y to Y+t with its
Gaussian factor exp(-t). For every fixed 0<a<1 the operational generator
of exp(aY) is bounded above by C_a exp(aY): its continuous row follows
from the polynomial P ratio and theta/s=exp(-x/2)Phi; its refresh row
uses the complete Gaussian newborn law and the bounded operational
refresh rate exp(-x/2)K. These estimates also cover the wall. Hence
stopping and Gronwall give finite exponential moments on each finite
operational horizon. On x>=a0>0 the same proof applies in physical time.

In particular the extended Dynkin formula for (14) is legitimate. With
P_T the full hidden semigroup and P_T^G the observed semigroup, define

 w_T=P_T(Uu)+int_0^T P_t(U Gu)dt.                  (16)

At the wall replace both generators and the integrand by their
operational versions. The TWO terms in (16) remain grouped. Dynkin for
w gives exactly

     w_T-w=P_T(Uu-w)=-P_T H.                       (17)

The posterior link extends to |H| by positive truncation and the finite
moment bounds. Therefore, for each fixed x,n,

 p_n(x)|P_T H(x,n)|
  <=T_x P_T|H|=P_T^G(T|H|)(x)
  <=P_T^G(sqrt(V_u))(x)->0.                       (18)

The last limit uses (11), boundedness of sqrt(V_u), and the already
proved escape of the observed increasing process. It applies also to
its operational clock. Consequently

               w_T(x,n)->w(x,n).                 (19)

This proves the finite-horizon interpretation, not just an abstract
weighted inverse. For nu=s1/psi the observed terminal is genuinely
polynomial: nu(Z_T) has leading4 Z_T^2 and does NOT tend to zero.
Accordingly neither P_T(U nu) nor the integral in (16) may be separately
discarded or identified with a convergent zero-discount current.
Their cancellation in (17) is the asserted construction.

## 7. Finite original weighted energies, without a finite individual current

The field in (10) has finite complete hidden spatial and refresh energy
in measure psi^2 p_n, and its variance obeys the exact signed transport
identity

 E_hidden[w]=F[u]-int b(x)V_u(x)dx, b=G^*(psi^2).    (20)

This uses the SAME b as the bounded-current theory. It is not inferred
from positivity of b or from existence of a finite occupation current.
Here are the cutoff details. For finitely many labels and a compact
annulus, (15) and the killed equations give the local logarithmic form
domains, so the polarized jump identity can be tested against a smooth
spatial cutoff times w. The local product formula is

 T Gamma_A(w)=2u Gu-G(T w^2), T w^2=u^2+V_u.

Remove a common small-jump cutoff only after this grouping. The complete
label/divisor/refresh cross terms are dominated by polynomial factors
times exp[-(1-2epsilon)n^2z], using (7) and the complete score bounds.
Label cutoffs commute exactly with the continuous label-preserving
jumps. The O(h) test increment is used for the spatial/posterior weak
derivative passage, not to infer Gamma energy from an amplitude bound.
Thus the remaining label-refresh and finite-divisor cutoff commutators
vanish under the displayed complete Gaussian envelope. Spatial upper tails have the same exponential margin. At
the origin each w_n is bounded and continuous, with the displayed
Gaussian label envelope; the cutoff commutator is bounded by
O(eta^2 log(1/eta)) for Gamma and O(eta^2) for primes, exactly as for
the original bounded-current cutoff. The p_n(y) conductance is retained
in that estimate. These bounds are uniform in the remaining cutoffs.

The positive truncated squared-difference measures are therefore
uniformly bounded by the grouped right side. Monotone convergence gives
their finite full energies, and the same cutoff bounds give equality,
not only lower semicontinuity. Finally
2 int psi^2 u Gu-int b u^2=F[u], proving (20). Its right side is finite:
u is polynomial, b has the already proved complete theta/row envelope,
and (11) gives Gaussian V_u. No finite individual martingale bracket
at infinite time is claimed.

The same proof and Cauchy give finite polarized energies between this
field and the actual bounded-current field. The bounded-mask original-P
argument now applies with T w^2=u^2+V_u in place of a bounded second
moment: every complete row is still integrable because u is polynomial.
The label-tail convergence has the full Gaussian margin from (7).
Consequently psi*T[a(w-u)] is a legal original-P source for every
bounded arithmetic mask a, including every natural finite/full Mobius
profile. The first label psi*w_1 is legal as well. No assertion of
uniform P boundedness on all of X_epsilon is made.

## 8. The lawful neutral gauge and its unavoidable changed forcing

Let w^g be the actual plateau-current field with mean u, and let w^nu
be the field (10) for nu=s1/psi. Then

 u_sharp=u-alpha-beta0 nu,
 w_sharp=w^g-alpha-beta0 w^nu,
 T w_sharp=u_sharp, A w_sharp=U G u_sharp.          (21)

All mixed hidden and original forms in (21) are finite by Section7.
The conditional variance is NOT invariant:

 V_sharp=V_g-2 beta0 Cov_p(w^g,w^nu)+beta0^2 V_nu.  (22)

Its full score, divisor and reflected/pole terms must change coherently.
The scalar source is g_sharp=g-alpha psi-beta0 s1. Since s1 is h-null,
actual Q_delta stationarity gives

 Q_delta[g_sharp]=beta0^2 delta N[s1],
 Q_delta(g_sharp,z)=-beta0 delta N(s1,z)            (23)

for lawful z. The common-neutral-compensated form is unchanged when
its neutral space contains s1, but the displayed forcing is not zero.
Thus a choice killing the normalized origin coefficient C(g_sharp)
can now be made in a genuine global hidden field, while retaining
(16)-(19), (22)-(23) and the full neutral Schur cost. This does NOT prove
that the critical transport source norm is bounded or that its signed
original-boundary remainder is favorable. It supplies the missing lawful
field on which that comparison may be tested.

## 9. Scope of neutral calibration

Only fixed deterministic linear combinations of lawful neutral ratios
are asserted here. A path-dependent random projection is not licensed by
this theorem and must retain its own conditional Gram and cross terms.
Killing one observed origin functional does not automatically kill the
masked source-gradient functional. Neither its sign nor a favorable
full original Q_delta remainder follows from this extension.
