# The exact dominant/tail covariance matrix of the same star current field

The dominant Brownian covariance is not an arbitrary replacement for the
actual hidden variance. It is exactly the dominant projection of the
already constructed star initial-label field. This note identifies its
joint higher-label covariance, retains the triangular cross term, and
cancels the continuous Gamma cooling against true-divisor outgoing rows.
The remaining defect is a genuine arithmetic label-incidence form. No
favorable total sign or extra independent energy resource is asserted.

## 1. One field throughout

Use the actual current field and the audited star coupling in
[CURRENT_STAR_FIELD.md](CURRENT_STAR_FIELD.md).
For x<=y its initial labels have probabilities

    P(N_x=N_y=n)=p_n(y), n>=2;
    P(N_x=N_y=1)=p_1(x);
    P(N_x=n,N_y=1)=p_n(x)-p_n(y), n>=2.

Future genuine hidden Poisson drivers are independent of the whole initial
label field. Thus W(x)=w(x,N_x) is the conditional mean of the SAME
complete current at x. Write

    u=T w, v=w_1, e=v-u, q=1-p_1, epsilon=q/p_1,
    v_tail=q^(-1)sum_(n>=2)p_n w_n,
    Z_1=0, Z_n=w_n-v_tail (n>=2),
    D_1=e, D_n=-e/epsilon (n>=2),
    Y_1=0, Y_n=e/q (n>=2).

Then, as arbitrary-label identities,

    w=u+D+Z, D=e-Y, T D=T Z=0,
    T D^2=e^2/epsilon, T Z^2=R_high,
    T(DZ)=0.                                           (1)

Define random source-coordinate fields D(x)=D_(N_x)(x) and
Z(x)=Z_(N_x)(x), with the same labels as W. These random fields are not
independent. The argument below does not replace the true hidden dynamics
by a hypothetical tail-posterior process.

## 2. Exact joint covariance, including its nonzero triangular part

For x<=y put A(x,y)=sum_(n>=2)p_n(y)Z_n(x). Directly summing the three
star channels gives

 E[D(x)D(y)]=e(x)e(y)/epsilon(x),
 E[D(x)Z(y)]=0,
 E[Z(x)D(y)]=-e(y)A(x,y)/q(y),
 E[Z(x)Z(y)]=sum_(n>=2)p_n(y)Z_n(x)Z_n(y).             (2)

For example T_y Z(y)=0 kills the second line, whereas
sum p_n(x)Z_n(x)=0 turns the upper-label absorption channel in the third
line into the displayed expression. The first line follows from
p_1(x)-q(x)/epsilon(x)=0 and
q(y)[1+1/epsilon(y)]=1.

Consequently the dominant kernel is exactly

    K_D(x,y)=e(x)e(y)omega(min(x,y)), omega=1/epsilon, (3)

the independently audited nested-cutoff/Brownian kernel. Its higher-label
partner K_Z in (2) is positive semidefinite, and the WHOLE two-by-two
matrix-valued covariance is positive semidefinite because it is the
covariance of this one joint random field. Its off-diagonal block is not
zero. Merely adding two separate PSD kernels would lose that block.

The diagonal identity is the SAME actual variance

    V=e^2/epsilon+R_high.                              (4)

For x<y define the mixed increment

    M(x,y)=E[(D(y)-D(x))(Z(y)-Z(x))]
           =e(y)A(x,y)/q(y).                         (5)

It need not have a pointwise sign. Since A(x,x)=0, its continuous Gamma
pairing has the correct diagonal cancellation already grouped.

## 3. Actual source domains and the complete original boundary

Let F be the one-orientation original forward Gamma/prime form. The full
star field W has finite expected original P energy by its previously
proved cutoff-feature representation. The dominant covariance (3) gives

    F_D:=E F[D]=F_m[e]+int C_omega e^2<infinity,
    m=psi^2/epsilon,                                  (6)

including ALL incoming prime powers. Its separate boundary edge energies
are finite by the actual theta margin of e. The actual star realization
has exactly these same second moments, so its expected forward and
boundary component energies equal the already audited values, by Tonelli.

For clarity its pointwise amplitudes are also controlled. The global
bound |w_n|<=C(1+log n), together with uniformly bounded conditional-tail
log moments, gives |e|/q<=C. Thus D(x) is bounded. On a realization with
initial tail label n it is the piecewise field -e/epsilon before that
label's finite absorption threshold and e afterward. The finite expected
F_D, bounded ratio and theta boundary rows give original-P closure for
almost every realization. One can first truncate the label and threshold,
then smooth the single threshold; the logarithmic Gamma crossing cost is
finite and converges in the usual cutoff approximation. Hence
Z=W-u-D is likewise a lawful random original-P source with integrable
P energy. No original-P claim for every unweighted w_n is needed.

For each original boundary component H, N and P_pole, let the subscripts
D,Z,DZ denote its expectation on D, on Z, and its polarized mixed value.
All positive component expectations are finite, and

    E B_delta[W]=B_delta[u]+B_D+B_Z+2B_DZ,
    B_delta=H+(1-delta)N-P_pole.                      (7)

Every term in B_DZ is obtained by replacing the squared difference in the
ORIGINAL edge form by M(x,y). In particular its pole coefficient is still
4 in the double integral with sinh(x/2)psi(x)sinh(y/2)psi(y). No rank-one
covariance correction is identified with the original pole.

Under the actual PSD hypothesis, the integrated original Q_delta matrix
of D and Z is PSD. In particular

    Q_D=2F_D-B_D>=0, Q_Z=2F_Z-B_Z>=0,
    |2F_DZ-B_DZ|^2<=Q_D Q_Z.                         (8)

Equation (8) is a conditional common-field Schur inequality, not an
independent proof of Q_delta positivity. It retains the same off-diagonal
block as (2). The strictly positive potential in the dominant spatial
factor can now be combined with the complete B_D from THIS field, rather
than an unrelated realization. It is still the same spatial budget.

## 4. Exact mixed spatial cancellation: only arithmetic incidence remains

Write mu=psi^2 and y=x+log d. Let

    K_d(x)=alpha_d psi(x)psi(y),
    F_tail=sum_(n>=2)p_n a_n Z_n,
    L_n=sum_(d|n,d>=2)Lambda(d)s(x+log d)/s(x),
    lambda_prime=sum_(d>=2)alpha_d psi(x+log d)/psi(x).

Let E_sp denote the genuine integrated hidden spatial energy, including
Gamma and every true divisor death but excluding refresh. Its polarized
version has the same normalization. The exact posterior conductances are

    mu(x)p_n(x) q_Gamma,n(x,dy)
          =psi(x)psi(y)kappa(y-x)p_n(y)dy,
    mu(x)p_(dm)(x)Lambda(d)s(y)/s(x)=K_d(x)p_m(y).       (9)

Define the finite arithmetic mixed term

 T_cross=sum_d int K_d(x) e(y)/q(y)
                   sum_(m>=2)p_m(y)[Z_m(x)-Z_(dm)(x)]dx. (10)

Then the COMPLETE mixed identity is

    E_sp(Y,Z)+F_DZ
       =int mu(e/q)F_tail+T_cross.                   (11)

Proof for the continuous part. By tail centering at y,

 E_Gamma(Y,Z)=int_(x<y)K_Gamma(x,y)
                  [e(x)/q(x)-e(y)/q(y)]A(x,y).

Adding F_Gamma,DZ from (5) leaves
int K_Gamma[e(x)/q(x)]A(x,y). Because sum p_n(x)Z_n(x)=0,
the singular common rate cancels. The exact finite row difference is

    int(q_Gamma,1-q_Gamma,n)=L_n-a_n+a_1.

Therefore the remaining continuous mixed row equals

    int mu(e/q)[F_tail-sum_(n>=2)p_n L_n Z_n].        (12)

For a true divisor d, put B_d(x)=sum_(m>=1)p_m(y)Z_(dm)(x).
Using (9), its hidden mixed edge is

 K_d{[e(x)/q(x)-e(y)/q(y)]B_d
                              +[e(y)/q(y)]p_1(y)Z_d(x)}.

Adding the star mixed edge K_d[e(y)/q(y)]A(x,y) leaves
K_d[e(x)/q(x)]B_d plus the integrand of (10).
The complete first term sums to
int mu(e/q)sum p_n L_n Z_n, canceling (12) EXACTLY.
This proves (11), without a Cauchy estimate or an omitted prime label.

## 5. Exact higher-label spatial cancellation

The same calculation can be done for its quadratic energy. Put

 T_Z=sum_d int K_d(x)sum_(m>=2)p_m(y)Z_m(y)
                                      [Z_(dm)(x)-Z_m(x)]dx.  (13)

Then

    F_Z-E_sp[Z]
      =int mu sum_(n>=2)p_n(beta-a_n)Z_n^2+2T_Z.      (14)

For the Gamma part the star minus same-index hidden square is exactly

    int_(x<y)K_Gamma sum_(n>=2)[p_n(x)-p_n(y)]Z_n(x)^2.

Its complete row coefficient at label n is
L_n-a_n-lambda_prime+beta. This follows from the row difference above and
sum p_n L_n-lambda_prime=0, T a=beta. Equivalently it is
int(q_Gamma,psi-q_Gamma,n), a genuinely nonnegative row for n>=2.
For the prime part, direct expansion gives

    int mu[lambda_prime R_high-sum p_n L_n Z_n^2]+2T_Z.

The two complete outgoing arithmetic rows cancel, leaving (14). The
refresh energy of Z is int mu[T(aZ^2)+beta R_high]; thus a useful
corollary, with the same spatial-plus-refresh normalization, is

    E_full[Z]=F_Z+2int mu T(aZ^2)-2T_Z.               (15)

The last arithmetic incidence term is signed and is not deleted.

## 6. Domain of the row cancellations and the surviving signed target

All identities can first be written with common spatial and small-Gamma
cutoffs. The continuous differences in (12) and (14) cancel the diagonal
before a limit. The derivative bounds for the complete eta posterior,
combined with |Z_n|<=C(1+log n), dominate A(x,y) by O(y-x) on compact
bands with summable Gaussian label coefficients. The genuine spatial
energies are finite by the audited two-group projection theorem and the
star-field construction. This pays their polarized pairings as well.

The displayed arithmetic terms (10),(13) converge absolutely: |e|/q is
bounded, |Z_n| has at most logarithmic label growth, the p_m(y) conditional
moments are uniformly finite, and K_d has the complete theta future tail.
Near zero mu=O(x^2), while L_n,a_n,beta have at most 1/x growth with
polynomial label coefficients; Gaussian posterior moments pay the rows.
At infinity the same theta coefficients pay every resulting polynomial
and logarithm. Thus the grouped row limits use dominated convergence,
not separate infinite Gamma diagonals or a backward-theta row.

The audited remaining higher-tail Schur equation is

 0=E_sp[Z]-2E_sp(Y,Z)+int b R_high
                                +R_high,a-2C_high.

Equations (11),(14) now rewrite it exactly as

 0=F_Z+2F_DZ+int b R_high+2int mu T(aZ^2)
                   -2T_Z-2int mu(e/q)F_tail-2T_cross-2C_high. (16)

This is one common-star higher-label equation with its entire continuous
Gamma cooling already collected. It exposes a genuine all-prime label
incidence target, not a scalar variance surrogate. The original boundary
of the same field is (7); its mixed term has not been set to zero or paid
twice. No sign for the combined right side of (16), and hence no full
coefficient-one source comparison or RH exclusion, is asserted.
