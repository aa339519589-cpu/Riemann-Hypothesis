# The original signed edge measure in the coalescing physical coordinates

This note records an exact, cutoff-compatible comparison target for the
coherent all-prime pair flow. It does not assign a sign to the pair-adjoint
or to the original source form.

## 1. All original edge measures, with one normalization

Put z=pi exp(2x), theta(z)=theta_c(z), and v(z)=u(x). Work on the ordered
pair space pi<z<w and write d_v(z,w)=v(z)-v(w). The complete original form
is the integral of d_v^2 against the following signed edge measure:

    h[psi u]=int d_v^2 (mu_Gamma+mu_F+mu_P-mu_H-mu_N).   (1)

Every measure on the right is nonnegative. They are

    mu_Gamma(dz,dw)
      =theta(z)theta(w) dz dw/[2 sqrt(pi z)(w-z)],

    mu_F: sum_(n>=2) Lambda(n) theta(z)theta(n^2z)
                              dz/sqrt(pi z), at w=n^2z,

    mu_P(dz,dw)
      =theta(z)theta(w)[sqrt(z/pi)-1][sqrt(w/pi)-1]
                                                   dz dw/(2zw),

    mu_H(dz,dw)=theta(z)theta(w) dz dw/[2(zw-pi^2)],

    mu_N: sum_(n>=2) Lambda(n) theta(z)theta(pi^2 n^2/z)
                          dz/z, at w=pi^2 n^2/z,
                                      pi<z<pi n.       (2)

The n=1 contributions vanish because Lambda(1)=0. All prime powers remain.
The coefficients in (2) include ordering: the original symmetric wall and
pole double integrals are doubled on z<w, and the reflected-prime interval
is likewise halved and doubled. The positive future terms were already
ordered. For example

    kappa(x+y)psi(x)psi(y) dx dy
                   =theta(z)theta(w) dz dw/[4(zw-pi^2)]

before ordering. The reflected-line identity uses
`zw=pi^2 n^2`, so `alpha_n psi(x)psi(y)=Lambda(n)theta(z)theta(w)`.

For the actual supercritical Q_delta, replace -mu_N by -(1-delta)mu_N.
Equation (1) has not replaced the true source by an independent Gaussian
seed and has not omitted the polar rank-one correction: mu_P is precisely
its original psi-ground difference-square form.

## 2. The killed continuous pair dynamics

Let L^(2) be the Markov generator, the negative of the positive pair
operator. For z<w, its continuous off-diagonal transitions are

    (z,w) -> (t,w), z<t<w,
                        rate theta(t)dt/[2(t-z)],
    (z,w) -> (z,t), w<t,
                        rate theta(t)(w-z)dt/[2(t-w)(t-z)],
    (z,w) -> diagonal (t,t), w<t,
                        rate theta(t)dt/[2(t-z)].        (3)

The third line is absorption for difference functions. These are the
exclusive lower-only, upper-only, and common accepted arrow regions of
the same Poisson field. Their sum is the exact continuous coupled generator,
not a different process fitted to the signed edge measures.

For compact smooth test functions F away from the diagonal, set F=0 on the
diagonal. The weak adjoint on a density

    rho(z,w)=theta(z)theta(w) k(z,w)

is the following grouped expression:

    (L_cont^(2))*rho(z,w)=theta(z)theta(w)/2 times
      { int_pi^z theta(a) k(a,w)/(z-a) da
       +int_z^w theta(b) k(z,b)(b-z)/[(w-b)(w-z)] db
       -k(z,w)[int_z^w theta(a)/(a-z) da
                        +int_w^infinity theta(a)/(a-w) da] }.         (4)

The near-z and near-w terms in (4) MUST be grouped with common small-distance
cutoffs before removal. Each isolated integral need not exist. This is a
weak paired identity; it does not assert that arbitrary k belongs to the
strong adjoint domain. It follows directly by pushing forward each of the
three channels in (3). In particular the diagonal absorption contributes
to the displayed loss; it has not been discarded.

## 3. Exact Cauchy-kernel reduction of the Gamma wall

Set c=pi^2 and k(z,w)=1/(zw-c). Define the grouped one-dimensional row

    R_theta(z)=PV {int_pi^z theta(a)/(z-a) da
                           -int_z^infinity theta(a)/(a-z) da}.

Then (4) becomes

    (L_cont^(2))*[theta(z)theta(w)/(zw-c)]
      =theta(z)theta(w)/[2(zw-c)]
                          [R_theta(z)+R_theta(w)+E_c(z,w)],          (5)

where the finite additional term is

    E_c(z,w)
      =int_w^infinity theta(a)/(a-z) da
       -int_pi^z theta(a)/(w-a) da
       +w int_pi^z theta(a)/(aw-c) da
       -(z^2-c)/(w-z) int_z^w theta(a)/(za-c) da.        (6)

Here z>w is not used; throughout pi<z<w. Each integral in (6) is finite.
The two algebraic identities behind (5) are

    1/[(aw-c)(z-a)]
        =[w/(aw-c)+1/(z-a)]/(zw-c),

    (b-z)/[(zb-c)(w-b)(w-z)]
        =[1/(w-b)-(z^2-c)/((w-z)(zb-c))]/(zw-c).

Thus the simple wall Cauchy kernel closes to two genuine one-state rows
plus the explicit cross term E_c, not merely to a diagonal multiple.
No sign of E_c or of their complete sum has been established.

## 4. The reflected-prime measure generates genuine incoming diffuse rows

On ordered pairs, the continuous incoming density from mu_N is

    theta(z)theta(w)/(2w)
       sum_(n: pi<=a_n<z) Lambda(n)theta(a_n)/(z-a_n),
                    a_n=pi^2 n^2/w,

    plus theta(z)theta(w)/(2z)
       sum_(n: z<b_n<w) Lambda(n)theta(b_n)(b_n-z)
                                      /[(w-b_n)(w-z)],
                    b_n=pi^2 n^2/z.                   (7)

Its loss remains supported on the original reflected curves and includes
the coalescence channel. Formula (7) is read first with the same jump
cutoffs as (4), and away from its curve-endpoint singularities. It follows
by parameterizing each original reflected curve by its unchanged coordinate.
Thus the actual pair adjoint does not preserve the reflected-prime curve
family under continuous jumps. Those diffuse incoming rows must be retained
in any all-prime comparison.

Prime transitions, by contrast, send a reflected label n to nk under a
single accepted k jump and to nk^2 under a common accepted k jump. The exact
rates are the same minimum and residual theta acceptance rates as in the
coherent current construction. Both order reversal and diagonal absorption
are retained by pushing these positive channels forward on ordered pairs.
No coprimality or prime-only restriction on k is imposed.

## 5. The remaining exact comparison

The proven coalescence theorem makes every fixed-pair current difference
an honest finite pre-coalescence integral. Its squared expectation can be
integrated against each finite wall, pole, and reflected-prime measure in
(2). The complete original identity nevertheless retains its signed storage
and covariance correction. Equations (4)-(7) display a concrete next target:
a comparison of the JOINT pair transport of mu_P-mu_H-mu_N with the positive
future edge incidence, with the one-state source rows and every diffuse
incoming prime term kept together.

A pointwise bound on the one-state distance drift, or positivity of the
current covariance as a matrix, does not imply that comparison. No strong
adjoint passage, invariance of the original signed measure, or coefficient-one
source-form contraction is asserted here.
