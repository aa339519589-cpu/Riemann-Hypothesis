# Exact centered-profile residual cross: the reset forcing and the same star law

This identity aligns the complete spatial/current cross with the actual
Mobius-mask equation. It is not a sign estimate. In particular the mixed
reset forcing is counted exactly once in the spatial form and once in
refresh, rather than replaced by independent error budgets.

Dependencies: [the same-star matrix](../20261014_same_current_star_blocks/JOINT_STAR_MATRIX.md),
[the centered Mobius block](CENTERED_PROFILE.md),
[the posterior current domain](BOUNDED_MASK_DOMAIN.md).

## 1. Conventions and the exact single-label balance

Write mu_0=psi^2, T_x f=sum_n p_n(x)f_n, c_n for the positive refresh
score, beta=T c, and L_n for the complete true-divisor exit rate of label n.
The original positive future generator is G, and its prime rate is
r_d(x)=alpha_d psi(x+log d)/psi(x). Write lambda_prime=sum_d r_d.
The continuous rate at label n is q_n(x,dy), with

    p_n(x)q_n(x,dy)=p_n(y)q_Gamma(x,dy),
    q_Gamma(x,dy)=kappa(y-x)psi(y)/psi(x), y>x.

The complete pointwise posterior balance is

    G_cont p_n=p_n[L_n+beta-c_n-lambda_prime].       (1)

Indeed apply T A=G T to the fixed label-n indicator. Its genuine divisor
outflow is p_n L_n, its inflow is sum_d r_d p_n(y), and the refresh
mean is beta p_n-p_n c_n. The latter prime inflow cancels the same
term in G_prime p_n, giving (1). No finite prime truncation is inserted
in this exact identity. Equivalently it follows from L_n-M_n=c_n-c_1
and the label1 balance. Gamma differences in (1) have finite local
moments; the separately infinite Gamma diagonal is never introduced.

All bilinear energies below are polarized from the one-orientation
squared-difference energies. Put

    K_Gamma(x,y)=psi(x)psi(y)kappa(y-x), x<y,
    K_d(x)=alpha_d psi(x)psi(y), y=x+log d.

The notation int_forward K f denotes the Gamma double integral plus the
sum of prime integrals, with exactly these one-orientation weights.

## 2. General centered-field identity

Let H_n(x),J_n(x) be real fields satisfying T_x H(x)=T_x J(x)=0.
In particular they need not be mutually orthogonal. Use the SAME coherent
star law: for x<y a tail label n survives with probability p_n(y), and
its lost mass p_n(x)-p_n(y) moves to label1. Define

    U_H(x,y)=T_y H(x), U_J(x,y)=T_y J(x).

The exact cross endpoint expectation is

    E[H(x)J(y)]
       =T_y[H(x)J(y)]-J_1(y)U_H(x,y).              (2)

The root transfer term in (2) follows from T_x H(x)=0. It is present even
though both one-point means vanish. The reverse ordered expectation has
the corresponding H_1(y)U_J(x,y) correction.

Let E_sp be the genuine hidden continuous-plus-divisor form, and F_star
the complete original forward form of this same random field. Then

 E_sp(H,J)-F_star(H,J)
   =int mu_0 T[(c-beta)HJ]
    -int_forward K [J_1(y)U_H(x,y)+H_1(y)U_J(x,y)]
    -sum_d int K_d T_y{
          [H_(dm)(x)-H_m(x)]J_m(y)
         +[J_(dm)(x)-J_m(x)]H_m(y)}.                (3)

The subscript m is summed by T_y in the last line. In particular all
child-to-root crossings m=1 and every higher prime-power incidence are
retained; no tail-only replacement is made.

### Proof

For one Gamma edge, subtracting the star cross-square from the true
same-label cross-square gives

 T_y[H(x)J(x)]-T_x[H(x)J(x)]
              -J_1(y)U_H-H_1(y)U_J.

For a true divisor edge, the corresponding difference is

 T_y[H_(dm)(x)J_(dm)(x)]-T_x[H(x)J(x)]
 -T_y{[H_(dm)(x)-H_m(x)]J_m(y)
                +[J_(dm)(x)-J_m(x)]H_m(y)}
              -J_1(y)U_H-H_1(y)U_J.

On summing the first, purely outgoing row of these two expressions, the
coefficient of H_n(x)J_n(x) is

    -G_cont p_n+p_n L_n-lambda_prime p_n
                          =p_n(c_n-beta)

by (1). This proves (3). This combination must be made at a common
Gamma cutoff before removing it. In particular (3) is not obtained by
separating the divergent continuous outgoing diagonal.

## 3. Full refresh and exact coefficient two

The full refresh bilinear at one point is

    T Gamma_reset(H,J)
       =beta T(HJ)+T(cHJ)-T H*T(cJ)-T J*T(cH).

For centered fields the last two terms vanish. Therefore, writing E_full
for the hidden spatial PLUS full refresh energy, (3) gives

 E_full(H,J)-F_star(H,J)
   =2int mu_0 T(cHJ)
    -int_forward K[J_1(y)U_H+H_1(y)U_J]
    -sum_d int K_d T_y{
          [H_(dm)(x)-H_m(x)]J_m(y)
         +[J_(dm)(x)-J_m(x)]H_m(y)}.                (4)

The coefficient2 in (4) is exact. One copy of T(cHJ) comes from the
complete spatial posterior balance, the other from refresh. This is a
single identity for the same hidden form, not two independent gains.

## 4. The actual centered Mobius projection

Use a(n)=1-mu_ar(n), m=T a, sigma^2=T a^2-m^2, and the SAME actual field
H_current=w-u. Its orthogonal decomposition is

    H_current=D+Z,
    D_n=A[a(n)-m], A=T(a H_current)/sigma^2,
    T Z=T(aZ)=0.

Let

    h=T(a H_current)=sigma^2 A,
    r=-T[c(a-m)Z],
    Q(x,y)=T_y[a Z(x)], U(x,y)=T_y Z(x), b=mA.

Here r is the exact centered reset covariance of this SAME orthogonal
residual; it is not a new field. Its identity in the local spatial and
refresh terms is proved below, without an inverse or a changed metric. Put

 C_mix=int_forward K[
           A(x)Z_1(y)(m(x)-m(y))+b(y)U(x,y)],

 I_div=sum_d int K_d {
       A(x)T_y[(a(dm)-a(m))Z_m(y)]
        +A(y)T_y[(Z_(dm)(x)-Z_m(x))(a(m)-m(y))]}.

Then (3)-(4) specialize to

    E_sp(D,Z)-F_star(D,Z)=-int mu_0 A r+C_mix-I_div,
    E_reset(D,Z)=-int mu_0 A r,
    E_full(D,Z)-F_star(D,Z)=-2int mu_0 A r+C_mix-I_div.  (5)

To see the local cancellation, T(DZ)=0 pointwise, so
T[(c-beta)DZ]=A T[c(a-m)Z]=-A r. Also
U_D=A(x)(m(y)-m(x)) and D_1(y)=-b(y), giving C_mix.
The last line of (3) is precisely I_div. It includes the root-child
contribution, including the square-collision terms in a(dm).

The SAME-star forward cross itself has the particularly simple exact
form

    F_star(D,Z)=-int_forward K[
          A(x)Z_1(y)(m(x)-m(y))+A(y)Q(x,y)].        (6)

Indeed the one-point cross T(DZ) is zero, and (2) gives the two remaining
ordered endpoint covariances. Formula (6) retains both triangular terms;
neither is silently set to zero by one-point conditional orthogonality.

## 5. Actual domains and the lawful source slot

The centered-profile theorem proves finite genuine spatial and star
forward forms of D. The actual current has finite hidden/current energy
and integrable original-P star energy, so the same is true of Z=H_current-D.
The bounded A and the global bound |w_n(x)|<=C(1+log n) pay every potential
and true-prime term of (3)-(6) absolutely. In particular root-child
arithmetic crossings are included in that assertion.

For the continuous cooling term, centeredness gives
U_H(x,y)=sum_n[p_n(y)-p_n(x)]H_n(x). Complete smooth theta moments and the
logarithmic label bound imply U_H(x,x+h)=O(h) locally uniformly, with a
theta-paid global coefficient. This pays kappa(h)~1/(2h). The same applies
to U_J,Q and m(x)-m(y). Hence C_mix and (6) are individually finite in
the actual fields, although the outgoing row used in deriving (3) is
combined before the common-cutoff limit. No pointwise drift-domain
assertion for each unweighted higher label is needed.

The posterior-mask domain theorem makes the source psi*h, with h=sigma^2 A,
a lawful original-P variation, and actual stationarity gives exactly

    Q_delta(psi*u,psi*h)=0.                        (7)

No quadratic original-P claim for psi*A follows from this note. The
local residual in (5) remains paired in the original weight psi^2; it
is not replaced by a norm in a different Gaussian metric. Equation (7)
alone does not remove C_mix, I_div or the full original
Gamma-wall/reflected-prime/pole mixed boundary. Those remain the joint
signed target. The positive centered arithmetic block proved separately
cannot be spent a second time in (5).
