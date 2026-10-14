# A positive de-Gaussianized factorization of the complete first-label repair

The original psi-squared adjoint is not replaced by a positive one. Instead,
the SAME actual first-label error has sufficiently strong Gaussian tails to
belong to a larger, explicitly specified metric in which its exact killed
operator is coercive. The complete signed prime/continuous mismatch and
centered refresh forcing remain on the right. Their Gaussian row gains pay
the change of metric without worsening the already certified constants.
This is a positive factorization of the correction equation, not a proof
of the original Q_delta comparison or a new independently spendable budget.

## 1. Same-source equation and exact change of variables

Use the full-band current field w of
[../20261014_first_label_current_approximation/CURRENT_FIELD.md](../20261014_first_label_current_approximation/CURRENT_FIELD.md)
and the proved first-refresh equation in
[KILLED_EQUATION.md](KILLED_EQUATION.md).
Write

    u=r-c_infinity, e=w_1-u, S1=psi p_1=eta s, s=psi/Phi,
    beta=K/psi, a_1=beta_1-(G_eta s)/s, K=3Phi+Theta/2,
    f=D u+R_a, D=G_prime,psi-G_extra, R_a=T[a(w-u)].             (1)

The operator G_extra has rate
[p_1(y)/p_1(x)-1]kappa(y-x)psi(y)/psi(x), which is NONNEGATIVE.
It enters D with a MINUS sign. Every true prime power and every refresh
label remain. The exact equation is

    (G1+beta)e=f,
    G1 h=int_0^infinity kappa(v) S1(x+v)/S1(x)
                                      [h(x)-h(x+v)]dv.        (2)

Now put z=pi exp(2x), B0(x)=exp(x/2)exp(-z), and

    q(z)=S1(x)/B0(x)=(4z^2-6z)s(x),
    g(z)=q(z)e(x), lambda(z)=a_1(x)+beta(x).                   (3)

The exact Gaussian-ground identity for D0 is

    D0(B0 F)=B0 G_B F,
    G_B F(z)=(1/2)int_0^infinity exp(-v)
                                      [F(z)-F(z+v)]dv/v.     (4)

Also D0 S1=-a_1 S1. This follows from D0 eta=-beta_1 eta and the eta
product rule; label one has no divisor jumps. Therefore G_B q=-a_1 q and

    q(G1+beta)e=(G_B+lambda)g=q f.                            (5)

Both a_1 and beta are strictly positive. The two coordinates in (2) and
(4) are different: v in (2) is a logarithmic increment, whereas v in (4)
is an ADDITIVE physical-z increment. The exact Jacobian in (4) is essential.

## 2. Genuine half-line Gamma accretivity, with its boundary retained

On z>=pi, let G_B be the positive generator in (4). Its Markov process is
the increasing Gamma subordinator. For smooth compact g, extended by zero
below pi, grouping at a common small-jump cutoff gives

    D_B[g]:=Re int_pi^infinity conjugate(g)G_B g dz
      =(1/4)int_pi^infinity dz int_0^infinity exp(-v)/v
                                      |g(z+v)-g(z)|^2 dv
       +(1/4)int_pi^infinity E1(z-pi)|g(z)|^2 dz >=0,          (6)
    E1(t)=int_t^infinity exp(-v)dv/v.

Indeed 2Re[conjugate(g(z))(g(z)-g(z+v))] is the difference square
plus |g(z)|^2-|g(z+v)|^2. Integration over z leaves precisely
int_pi^(pi+v)|g(z)|^2 dz, giving the second term of (6).
This term is a genuine half-line boundary term. It has not been dropped or
identified with the original polar form. The associated closed sectorial
form and the killed semigroup of G_B+lambda are obtained by monotone
positive-potential approximation; lambda may diverge at pi.

## 3. Actual domain in the larger metric

The global same-field estimate gives

    |e(x)|^2<=epsilon(x)V(x)<=C exp(-6z),
    epsilon=(1-p_1)/p_1.                                    (7)

The complete mismatch row and centered refresh bounds show, on every
sufficiently large z wing,

    |f(x)|<=C (1+z)^M exp(-3z)                               (8)

for some fixed finite M. For D this follows from the complete prime and
extra-Gamma row bounds and bounded u. For R_a use T(w-u)=0 to write
R_a=T[(a-a_1)(w-u)], use the logarithmic label bound for w, and the complete
polynomial-Gaussian tails of p_n a_n for n>=2. No absolute Mobius estimate
or unproved analytic regularity is used.

At the origin q(z)=O(z-pi), lambda(z)=O((z-pi)^(-1)), and q f is bounded.
These statements follow from the honest operational first-refresh equation:
the physical forcing has at most its paid 1/x entrance singularity. The
error e is continuous and bounded, not required to vanish at zero. Thus

    q f belongs to L2(dz),
    int |q f|^2/lambda dz<infinity,
    g=O(z-pi) at pi and has a polynomial-Gaussian tail.        (9)

One can justify the energy passage without assuming it from pointwise
decay. For eps>0 use the L2 resolvent of G_B+lambda+eps on q f. Its form
identity gives uniform bounds for D_B and the lambda-weighted norm. The
positive killed kernels are dominated by the un-killed Gamma potential.
For any c>0,

    G_B exp(-cz)=(1/2)log(1+c)exp(-cz),

so that potential maps polynomial-Gaussian majorants to integrable
polynomial-Gaussian majorants. Monotone kernel convergence, applied to the
positive and negative parts, identifies the eps-downarrow-zero limit with
the positive killed potential of q f in L2. By (5), its finite-interval
Feynman--Kac formula equals the SAME actual g; the surviving terminal vanishes
by (7). The form lower bound and the limiting weak equation therefore place
g in the Gamma form domain with int lambda|g|^2 finite. Finally (5) gives
G_B g=q f-lambda g in the lambda-inverse weighted space. This proves all
pairings below, rather than asserting a pointwise-tail-to-form implication.

For the exact operator pairing, use also a_1<=beta, since every tail
reset rate exceeds a_1 and T a=beta. Thus lambda<=2beta. The actual
bounds g=O(z-pi), beta=O((z-pi)^(-1)) at the wall, and beta=O(1/z)
at infinity show lambda g belongs to L2(dz). Since q f is L2, the weak
equation puts g in D(G_B). The operator pairing therefore agrees with
the closed form, and the equality below is not merely a lower-semicontinuity
inequality.

The unbounded lambda near pi does not impose e(0)=0: only g=q e vanishes
there. The real original entrance and forcing have already entered (2).

## 4. Exact lossless positive factorization

Set

    c0=1/[2pi exp(2pi)],
    A(x)=p_1(x)^2 sqrt(z/pi)exp[2(z-pi)],
    m(x)=A(x)psi(x)^2.

The Jacobian dz=2z dx gives EXACTLY

    m(x)dx=c0 q(z)^2 dz.                                     (10)

Take the weighted square of (5) and expand its mixed term. With
D_gamma=c0 D_B[g], the result is the exact identity

    int m |f|^2/lambda
       =int m lambda |e|^2+2D_gamma
                       +int m |f-lambda e|^2/lambda.          (11)

All three terms on the right are nonnegative. In particular the killed
inverse has norm at most one from L2(m/lambda) to L2(m lambda), and (11)
retains the positive Gamma difference and half-line boundary squares in
(6). This is NOT an accretivity assertion in the original psi^2 metric.
The extra factor A grows exponentially in physical z, and (7)-(9) are why
the actual error, unlike a generic source, is lawful in this metric.

## 5. Complete arithmetic forcing pays the larger metric at the old constants

The following are the pointwise envelopes proved with complete tails in
[the Gamma error note](../20261014_first_label_current_approximation/GAMMA_ERROR.md),
[the centered reset note](RESET_FORCING.md),
and [the drift mismatch note](DRIFT_MISMATCH.md):

    epsilon(z)<28 exp(-3z),
    r_extra/beta <=(12/5)z epsilon(z),
    r_prime/beta <60z exp(-3z),
    T_tail a/beta <=epsilon(z)+r_prime/beta.                   (12)

Here r_extra and r_prime are the ENTIRE positive row masses of the two
oppositely signed components of D. Also a_n>a_1 for n>=2. Consequently

    |R_a|^2<=T[(a-a_1)^2/a] T[a|w-u|^2],
    T[(a-a_1)^2/a]<=T_tail a.                                 (13)

The enlargement in (10) costs no worse rational constant. Since p_1<=1,

    A z exp(-3z)<=z^(3/2)pi^(-1/2)exp(-z-2pi),
    A exp(-3z)<=z^(1/2)pi^(-1/2)exp(-z-2pi).

Both right sides decrease on z>=pi>3. Their maxima are respectively
pi exp(-3pi) and exp(-3pi). Therefore the SAME rational certificates used
in those notes prove

    A epsilon<1/400,
    A r_extra/beta<1/50,
    A r_prime/beta<7/400,
    A T_tail a/beta<1/50.                                    (14)

In particular multiplication by A does not silently use a uniform
unweighted bound inside a growing weight. Its full pointwise envelope is
paid before taking the supremum.

Let

    R_current=int psi^2 T[a|w-u|^2],
    F_prime[u]=int psi^2 Gamma_prime[u],
    F_Gamma[u]=int psi^2 Gamma_cont[u].

Cauchy on the UNION of the two positive mismatch measures, with their
relative minus sign retained, and (14) give

    int psi^2 A |D u|^2/beta
       <=(3/80){F_prime[u]+F_Gamma[u]/400},
    int psi^2 A |R_a|^2/beta<=R_current/50.                   (15)

For the continuous term use additionally
Gamma_extra[u]<=epsilon(x)Gamma_cont[u]<=Gamma_cont[u]/400.
Since lambda>=beta, the left side of (11) is bounded by

    [sqrt((3/80){F_prime[u]+F_Gamma[u]/400})
                         +sqrt(R_current/50)]^2
       <=(23/400){F_prime[u]+F_Gamma[u]/400+R_current}.        (16)

This proves a full coercive correction estimate with the SAME complete
prime/reset energy debit. It is an alternative use of those resources,
not an additive surplus on top of the earlier 13/400 first-label theorem.
The exact square (11), rather than just its scalar upper bound (16), is
available for future signed completion.

## 6. Scope of the sign advance

Equations (11)-(16) sign the actual inhomogeneous first-label correction
operator in a domain that genuinely contains that correction. They resolve
neither the signed transport int b V in
F[u]=E_current+int b V nor the comparison of the complete boundary graph
B_delta[u] with 2F[u]. The full original pole and all actual stationarity or
neutral-forcing terms must still be included in either comparison. No
original-source kernel invariance or unproved RH consequence is asserted.


## 7. A fixed positive tilt gives a uniformly coercive inverse at no larger debit

There is a useful stronger version, requiring no limiting inverse at zero.
Fix the explicit value a=1/4 and set

    g_a(z)=exp[a(z-pi)]q(z)e(x),
    lambda_a=lambda+c_a, c_a=(1/2)log(1+a)>0,
    G_a F(z)=(1/2)int_0^infinity exp[-(1+a)v]
                                      [F(z)-F(z+v)]dv/v.

The exact exponential conjugation is

    exp[a(z-pi)]G_B(exp[-a(z-pi)]F)=G_a F+c_a F,

because the integral of [exp(-v)-exp(-(1+a)v)]/v is log(1+a).
Consequently the SAME source equation becomes

    (G_a+lambda_a)g_a=exp[a(z-pi)]q f.                         (17)

The operator on the left has L2 accretivity at least c_a, so its killed
L2 inverse is bounded by 1/c_a. Its Gamma form is (6) with exp(-v)
replaced by exp[-(1+a)v], and its half-line boundary is
E1((1+a)(z-pi))/4. All actual functions in (17) have the same paid wall
behavior and stronger-than-needed Gaussian tails. The killed potential
uniqueness can now be justified using the uniform factor exp(-c_a t),
without any zero-discount limit. The same lambda_a g_a and operator-domain
check from Section 3 applies.

Put m_a=m exp[(z-pi)/2] and D_a=c0 Re<g_a,G_a g_a>. The exact identity is

    int m_a |f|^2/lambda_a
       =int m_a lambda_a |e|^2+2D_a
                         +int m_a |f-lambda_a e|^2/lambda_a. (18)

The last residual is precisely G_a g_a divided by its positive gauge;
no extra derivative of the exponential weight has been omitted.

Importantly, (16) remains true with m_a and lambda_a in place of m and
lambda. Indeed

    [A exp((z-pi)/2)] z exp(-3z)
       <=z^(3/2)pi^(-1/2)exp[-z/2-(5/2)pi].

Its derivative has sign 3/(2z)-1/2<0 for z>=pi>3, and its value at z=pi
is exactly pi exp(-3pi). The corresponding degree-1/2 envelope decreases
as well. Hence all four rational bounds (14) survive with the SAME endpoint
constants; lambda_a>=beta is favorable. This gives a uniformly coercive,
fully half-line, same-source correction factorization with no increased
original Gamma/prime/reset energy expenditure. It still does not sign the
unrelated original reflected/pole or bV transport terms.

## 8. Exact dominant-second-label completion in the same positive inverse

The independently checked
[second-label reset completion](SECOND_LABEL_COMPLETION.md),
Sections 1--6, proves

    kappa2=p_1(a_2-a_1)>828/401>2,
    R_a=-kappa2 e+R3,
    R3=sum_(n>=3)p_n(a_n-a_2)(w_n-u),                         (19)
    |R3|^2/beta<=B3(z)T[a|w-u|^2],
    B3(z)=(324+5832z)exp(-8z)+1680z exp(-15z)<1/200000.

In particular (19) is a SIGNED completion of the same centered refresh
forcing, not a second independent variance estimate. It gives exactly

    (G1+beta+kappa2)e=f2, f2=D u+R3.

For a=0 or the fixed a=1/4 of Section 7, define

    lambda_(a,2)=a_1+beta+kappa2+(1/2)log(1+a),
    m_a=m exp[2a(z-pi)],
    g_a=exp[a(z-pi)]q e.

The exact positive identity is now

    int m_a |f2|^2/lambda_(a,2)
      =int m_a lambda_(a,2)|e|^2+2c0 Re<g_a,G_a g_a>
                  +int m_a |f2-lambda_(a,2)e|^2/lambda_(a,2). (20)

The domain proof is unchanged. On the wall kappa2 has at most the same
1/x singularity, and at infinity it tends to3log2. Thus multiplication of
g_a by this additional potential is L2. Uniform coercivity is now at least
828/401+(1/2)log(1+a), including when a=0.

The SAME residual debit remains small in either metric. Every term of
[A exp(2a(z-pi))]B3(z), after p_1^2<=1, is a positive constant times
z^(1/2) or z^(3/2) times an exponential with rate at least 11/2, for a<=1/4.
It decreases on z>=pi. Its endpoint is exactly B3(pi), so the complete
rational1/200000 certificate applies without modification. Consequently

    int m_a |f2|^2/lambda_(a,2)
       <=[sqrt((3/80){F_prime[u]+F_Gamma[u]/400})
                                     +sqrt(R_current/200000)]^2
       <=(7501/200000){F_prime[u]+F_Gamma[u]/400+R_current}.   (21)

No extra original reset square has been created: the n2 part was moved to
the LEFT in (19), while the actual n>=3 residual, including its full rate
and sign, remains on the right. In particular (20), not the sum of (11)
and (20), is the matched stronger use of the same equation. The signed bV
transport and the original full boundary comparison remain outside it.
