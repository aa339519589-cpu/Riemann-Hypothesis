# Unconditional original-form positivity of every centered star field

The rapidly cooling SAME star law supplies enough genuine Gamma noise to
sign its complete ORIGINAL source covariance form. This is an independent
form theorem. It does NOT invoke hypothetical actual Q_delta positivity,
replace the observed source by its current, or assert positivity for
arbitrary deterministic sources. The Gamma wall, every forward and reflected
prime power, and the full negative pole are retained.

## 1. The same posterior law and statement

Use the complete eta posterior

 p_n(x)=P(n^2z)exp(-n^2z)/sum_m P(m^2z)exp(-m^2z),
 P(t)=4t^2-6t, z=pi exp(2x), x>0.

The [coherent star initial-label field](../20261014_same_current_star_blocks/CURRENT_STAR_FIELD.md)
satisfies, for x<y,

 P(N_x=N_y=n)=p_n(y), n>=2;
 P(N_x=n,N_y=1)=p_n(x)-p_n(y), n>=2;
 P(N_x=N_y=1)=p_1(x).                                 (1)

Let H(x,n) be any scalar or Hilbert-valued field with T_x H(x)=0.
Put V(x)=T_x|H(x)|^2 and G(x)=psi(x)H(x,N_x). Assume the expected original
odd Gamma form is finite and int psi^2 V<infinity. The theorem is

             E q0[G] >=(1/10)int_0^infinity psi^2 V.   (2)

The full prime and pole expectations are absolutely finite under these
hypotheses, as proved below. The inequality also has its extended-form
interpretation if the positive Gamma energy is infinite. In particular
(2) applies to the proved actual centered current field, its genuine
centered Mobius projection, and its same-star orthogonal residual.
It is NOT necessary to assume Q_delta>=0 for any of these applications.

The original positive-wing source form is

 q0[g]=2<g,a(D)_odd g>
       -4 Re sum_n alpha_n int_0^infinity conj(g(x))g(x+d_n)dx
       +2 sum_n alpha_n int_0^(d_n) conj(g(x))g(d_n-x)dx
       -8|int_0^infinity sinh(x/2)g(x)dx|^2,            (3)

 a(t)=Re digamma(1/4+it/2)-log pi,
 alpha_n=Lambda(n)/sqrt(n), d_n=log n.

Every sum in (3) includes EVERY prime power. Reflected pairings on the
diagonal are real. Formula (3) agrees with the original odd-source
normalization, not a separately modified generator or positive repair.

## 2. Uniform exponential decorrelation in the physical theta coordinate

Two proved COMPLETE posterior bounds are

 q=1-p_1<1/401, E_p N^2<17/16.

The first bound follows from the complete
[posterior tail theorem](../20261014_first_label_current_approximation/GAMMA_ERROR.md),
and the second is the explicit all-integer estimate(7) in the
[same-star rate comparison](../20261014_same_current_star_blocks/BOUNDARY_SCHUR.md).
No finite posterior replaces p. For completeness,
the required consequence follows directly from their exact derivatives.
Since

 d_z log[P(n^2z)exp(-n^2z)]
      =-n^2+1/z+1/(z-3/(2n^2)),

one has

 -d_z log p_2
   >=4-E_pN^2-q/(z-3/8)
   >47/16-8/8421>14/5.                                (4)

Here the root logarithmic derivative is no smaller than the label2
one, while every tail derivative is at least1/z before its -n^2 term.
Also p_n/p_2 decreases for every n>=2, since

 d_z log(p_n/p_2)
 =-(n^2-4)+1/(z-3/(2n^2))-1/(z-3/8)<=0.

Consequently, with t=p_2(y)/p_2(x), every tail survival probability
p_n(y)/p_n(x) is at most t. The conditional star channel in (1) is exactly

                  P_xy=(1-t)J_1+t Q_xy,              (5)

where J_1 sends every label to1 and Q_xy is a genuine Markov kernel.
The mixture coin is independent of the starting label. For centered
endpoint fields X and Y, conditional variance gives

 |E(X conjugate(Y))|^2 <=t E|X|^2 E|Y|^2.            (6)

Indeed only the Q branch contributes to the covariance; after subtracting
its own endpoint mean, Cauchy gives t^2 Var(X)Var_Q(Y), while the total
endpoint variance is at least t Var_Q(Y). This proves (6), without
assuming independence of the two endpoint fields.

Set a=7pi/5. Equations (4)-(6) imply the COMPLETE covariance envelope

 |E[G(x)conj(G(y))]| <=f(x)f(y)R(x,y),
 f(x)=psi(x)sqrt(V(x)),
 R(x,y)=exp[-a|exp(2x)-exp(2y)|].                     (7)

For Hilbert fields the same statement applies to the scalar inner-product
covariance by Cauchy or finite-coordinate approximation. No arithmetic
projection or special profile coefficient is needed in (7).

Absolute Fubini uses a separate consequence of the SAME mixture, not
merely the absolute value of its covariance. For centered endpoint
fields X,Y, the Q branch obeys

 t E_Q|X||Y|<=sqrt(t)sqrt(V_x V_y),

because E_Q|Y|^2<=V_y/t. Centeredness also gives
p_1(y)|Y_1|^2<=q(y)V_y, and q(y)<=t q(x). The J_1 branch is therefore
at most sqrt(t)sqrt[q(x)/p_1(y)]sqrt(V_x V_y), which is less than the
first bound. Consequently

 E[|G(x)||G(y)|] <=2 R(x,y)f(x)f(y).                 (7a)

The factor2 in (7a) is used ONLY to prove absolute convergence. The
sharper centered covariance bound(7) supplies all sign constants below.


## 3. Exact odd Gamma energy and the independent positive noise

Write kappa(h)=exp(-h/2)/(1-exp(-2h)) and
C0=log pi-digamma(1/4). The exact odd restriction gives

 <g,a(D)_odd g>
 =-C0||g||^2
  +int_(x<y) kappa(y-x)|g(x)-g(y)|^2 dxdy
  +int |g(x)|^2 int_x^infinity kappa(h)dh dx
  +int int kappa(x+y)conj(g(x))g(y)dxdy.               (8)

The last term is POSITIVE, since kappa(x+y) is the sum of the positive
rank-one kernels exp[-(2j+1/2)(x+y)]. It remains positive after taking
expectation; dropping it is therefore lawful without a covariance sign
assumption. By (7), the expected edge square in (8) is at least
(1-R(x,y))[f(x)^2+f(y)^2]. Thus

 E< G,a(D)_odd G> >=int W(x)f(x)^2 dx,                (9)

 W(x)=-C0+int_x^infinity kappa(h)dh
  +int_0^infinity kappa(h)[1-exp(-lambda(e^(2h)-1))]dh
  +int_0^x kappa(h)[1-exp(-lambda(1-e^(-2h)))]dh,
 lambda=a exp(2x).

All terms defining W are finite for x>0. Near h=0 the differences remain
grouped, so no infinite Gamma diagonal has been introduced.
We prove the uniform bounds

 W(x)>=1/2, 0<x<=3/10;
 W(x)>=43/50, x>=3/10.                               (10)

### 3.1 Complete compact-band bound

Use e^(2h)-1>=2h. For0<h<x, use
lambda(1-e^(-2h))>=2a h. The positive kappa expansion then gives

 W(x)>= [digamma(1/4+a e^(2x))+digamma(1/4+a)]/2-log pi
             +sum_(j>=0) exp[-(2a+2j+1/2)x]/(2a+2j+1/2).      (11)

The elementary Binet bound, valid for every w>0, is

 digamma(w)>=log w-1/(2w)-1/(12w^2)=:B(w).            (12)

It follows by bounding (t^2+w^2)^(-1)<=w^(-2) in Binet's positive
integral and using int_0^infinity t/(exp(2pi t)-1)dt=1/24.
B is increasing. Retain the FIRST20 positive terms in (11), not a
truncated equality. On each cell [l,r] of the1000 equal cells in[0,3/10],
evaluate B(1/4+a exp(2l)) at the left endpoint and these decreasing
exponentials at the right endpoint. The accompanying55-digit directed
interval checker proves every lower endpoint exceeds1/2; the smallest
certified lower bound is greater than0.50998. Thus the omitted entire
Gamma tail is positive, and no source sampling is used in (10).

### 3.2 Analytic entire-wing reduction to one positive series

For any lambda the last integral in (9) plus its boundary tail is at
least the SAME integrand integrated over all h>0. Both resulting full
integrals increase in lambda. Since pi>157/50 and exp(3/5)>91/50,

        lambda>= (7/5)(157/50)(91/50)>8

when x>=3/10. The future integral is at least
[digamma(33/4)-digamma(1/4)]/2. In the past integral, the exact positive
Poisson expansion gives

 int_0^infinity kappa(h)[1-exp(-8(1-exp(-2h)))]dh
  =(1/2)exp(-8)sum_(k>=1)8^k/k! sum_(j=0)^(k-1)1/(j+1/4).    (13)

Using (12) at33/4, retaining k<=60 in this POSITIVE series, and the exact
identity digamma(1/4)=-EulerGamma-pi/2-3log2 gives a directed lower bound
larger than0.86488>43/50. This proves the entire wing of (10), rather than
stopping a numerical scan.

## 4. Every prime power in all three source branches

Taking absolute values only AFTER retaining the genuine covariance (7),
the forward and reflected terms in (3) have combined lower bound

       -2 int [J_+(x)+J_-(x)+J_R(x)] f(x)^2 dx,       (14)

 J_+=sum_(n>=2)alpha_n R(x,x+log n),
 J_-=sum_(2<=n<exp x)alpha_n R(x,x-log n),
 J_R=sum_(n>exp x)alpha_n R(x,log n-x).

We prove

 J_++J_-+J_R<1/8, 0<x<=3/10;
 J_++J_-+J_R<3/4, x>0.                              (15)

In the following upper bounds, allowing ALL integers n>=2 only enlarges
the original prime-power sums. Put T=exp(2x)>=1. One has
alpha_n<=log(n)/sqrt(n)<=2/exp(1)<14/19, and also alpha_n<=n.

For J_+, its n-th envelope is n exp[-aT(n^2-1)]. The first term is at most
2/20^4, and each consecutive ratio is less than(3/2)/20^7, since
exp3>20 and a>21/5. Hence J_+<1/1000.

J_- is empty for T<=4. For T>4 its at most sqrt(T) labels each have
exponent at least3aT/4. Thus

 J_- <=(14/19)sqrt(T)exp(-3aT/4)
      <=(28/19)/20^4<1/1000.                         (16)

For reflection,

 J_R<=sum_(n>=2) (log n)/sqrt n
                            exp[-a|n^2-T^2|/T].     (17)

On n>=T/2 the exponent is at least(3a/2)|n-T|. The COMPLETE integer
lattice exponential sum is at most coth(3a/4)<401/399. Its contribution
is therefore at most(14/19)(401/399). If2<=n<T/2, necessarily T>4;
there are fewer than T/2 labels and the exponent is at least3aT/4.
This remaining entire piece is at most(28/19)/20^4. Consequently

 J_R <(14/19)(401/399)+(28/19)/20^4
       =32080399/43320000<149/200.                    (18)

Combining (16)-(18) proves the global second bound in (15).

On the compact band T<=exp(3/5)<11/6, the n=2 term in (17) is less than
(1/2)exp(-161/110)<3/25. For n>=3, use
n^2/T-T>=(6/11)n^2-11/6. The first exponent exceeds1421/110>12,
and the complete consecutive ratio is less than1/2. Its entire
contribution is less than6/20^4. Therefore

 J_R<3/25+6/20^4,
 J_++J_-+J_R<3/25+6/20^4+2/1000<1/8.

The elementary exponential comparisons and all final rational bounds
are included in the checker. There is no last-prime or largest-label
cutoff in (14)-(18).

## 5. The full negative pole in the SAME covariance

Let s(x)=sinh(x/2). The expected pole magnitude is at most the quadratic
form with kernel8s(x)s(y)R(x,y). Apply weighted Schur with the strictly
positive weight s(x), x>0. Its row ratio is

 8int_0^infinity s(y)^2 exp[-a|exp(2y)-T|]dy
 =int_1^infinity [v^(-1/2)+v^(-3/2)-2/v]exp[-a|v-T|]dv.

The bracket equals w(1-w)^2, w=v^(-1/2), and is at most4/27. Since
the exponential kernel has full-line mass2/a, the whole pole satisfies

 8 E|int s(x)G(x)dx|^2
             <= [8/(27a)]int f^2 <(40/567)int f^2.    (19)

No diagonal pole surrogate has replaced its rank-one square, and no
null gauge or pole-centering hypothesis has been imposed.

## 6. Combine the ORIGINAL form, domains and scope

Equations (9),(14),(19) give directly from (3)

 E q0[G]>=int [2W-2(J_++J_-+J_R)-40/567] f^2.

On0<x<=3/10 the bracket exceeds1-1/4-40/567>1/10.
Onx>=3/10 it exceeds

          43/25-3/2-40/567=4237/28350>1/10.          (20)

This proves (2). The Gamma wall is a positive original kernel and has
only been dropped after its exact inclusion; all prime branches and
the full pole have been paid with their original signs and coefficients.

A common Gamma/spatial cutoff justifies (8)-(9) on smooth finite fields.
The positive Gamma energy and its positive wall kernel pass by closed
form convergence or monotone limits. Equations (14)-(19), with the harmless factor2 from(7a) for absolute
convergence, are bounded forms in int f^2. Thus the COMPLETE prime sums,
pole pairings and their expectations satisfy absolute Fubini. The
positive Gamma terms in(8) can be handled directly by Tonelli, and
(7)-(9) apply directly to the finite expected Gamma form; no unproved
label-truncation convergence in the spatial form is needed. No individual higher-label source or
unbounded generator-row domain is asserted.

For any delta>=0, the same field also obeys

 E Q_delta[G]>= (1/10)int psi^2 V+delta E N[G/psi],    (21)

whenever the original N form is finite. The added term is its ORIGINAL
nonnegative squared-ratio form, not a new comparison norm. In particular
(21) signs the complete covariance of the actual centered current under
the SAME star coupling, including its moving-profile mixed blocks.
It does not sign q0 of its deterministic mean source. The remaining
mean/current spatial-incidence and storage comparison is still needed
before any exclusion of an actual positive-depth state could follow.

## 7. Complete mixed covariance and the deterministic mean

For a finite family of centered same-star fields H_i, apply(2) to every
linear combination. With the conjugate-first convention, their ORIGINAL
Hermitian Gram matrices satisfy

 [E q0(G_i,G_j)] >= (1/10)[int psi^2 T(conj(H_i)H_j)].        (22)

Thus, for the genuine orthogonal split H=D+Z, the entire mixed q0 block
is paid in ONE inequality. Its right side is diagonal because T(DZ)=0;
the original q0(D,Z) entry is generally not zero and is retained by(22).
There is no separate sum of independently spent diagonal bounds.
The additional delta N Gram in(21) is likewise retained as one full
positive matrix, not diagonalized by conditional orthogonality.

For any deterministic mean source psi u for which the mixed forms are
legal, conditional centering gives

 E q0(psi u,psi H)=0,
 E q0[psi(u+H)]=q0[psi u]+E q0[psi H].                (23)

This is a linear ORIGINAL-form statement, not a cancellation of the
genuine hidden spatial pairing E_sp(Uu,H). The latter contains the
complete source-gradient forcing. Equation(23) and positivity of its
covariance term do not determine the sign of the deterministic mean.
The signed adjoint storage and true divisor incidence in the current
transport therefore remain necessary in any full-source comparison.

## 8. Reproducibility and dependencies

Run check_covariance_original_sign.py. It verifies the1000
near-origin Gamma cells, the positive60-term entire-wing Gamma bound,
and every stated final rational/exponential comparison. All omitted
Gamma/prime tails are treated above by positive series or analytic
bounds, not numerical truncation.

The full posterior bounds and coherent law are the linked published
inputs above. Their proofs are only inputs to(4)-(7);
no actual spectral sign, source equation, current forcing contraction,
or original head certificate is an input to theorem(2).
