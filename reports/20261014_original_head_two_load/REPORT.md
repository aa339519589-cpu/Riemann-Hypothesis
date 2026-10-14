# Original-source head coercivity after two lawful loads

## 1. Statement and scope

Let b=log 2, alpha_n=Lambda(n)/sqrt(n), and s1=psi''-psi/4, where

    psi(x)=exp(x/2)sum_(m>=1)c(pi m^2 exp(2x))exp[-pi m^2 exp(2x)],
    c(z)=8z^3-30z^2+15z.

This is the usual odd theta derivative psi=-Phi'. The complete original odd-source form restricted to (0,b) is

    q0[f]=2<f,a(D)_odd f>
         +2alpha_2 integral_0^b f(x)f(b-x)dx
         +2alpha_3 integral_(log3-b)^b f(x)f(log3-x)dx
         -8|integral_0^b sinh(x/2)f(x)dx|^2,
    a(t)=Re digamma(1/4+it/2)-log pi.                 (1)

The prime reflections and pole are not dropped. The domain in this note is
the closure of finite sine spans in the restricted Gamma-form norm. It
includes the head restrictions of the actual fixed-depth sources: those
belong to H^sigma after zero extension for some 0<sigma<1/2, which is
stronger than the logarithmic Fourier regularity required here. A half-source
with nonzero origin trace is interpreted in the direct signed source form;
this does not assert separate original P and N membership.

Define the two bounded head loads

    U(f)=integral_0^b exp(x/2)f(x)dx,
    V(f)=(5/787)N(f,s1)=(5/787)integral_0^b n(x)f(x)dx,
    n(x)=2[(L(x)/psi(x))s1(x)-(F_r s1)(x)],
    L(x)=sum_(d>=2)alpha_d psi(log d-x),
    (F_r s1)(x)=sum_(d>=2)alpha_d s1(log d-x).         (2)

All prime powers occur in (2). The origin quotient is analytically continued.
The normalization 5/787 is an exact rational choice, not an estimate of a
norm. The result is

    q0[f]+2|U(f)|^2+2|V(f)|^2 >= (1/100)||f||_2^2.   (3)

The computer-assisted part uses interval enclosures of whole infinite sums,
exact integer matrix products, a rigorous infinite high-mode estimate, and
interval LDL elimination. No finite sampled matrix is used as a positivity
proof. This theorem does not prove positivity of q0 without the two loads,
or positivity of the full original mixed head/tail residual.

## 2. Exact infinite-dimensional Gamma and high-mode bound

Use e_j=sqrt(2/b)sin(omega_j x), omega_j=j*pi/b. The exact boundary Gram and
its proof are in [GAMMA_SINE_GRAM.md](GAMMA_SINE_GRAM.md):

    qGamma_ij=2a(omega_j)delta_ij-E_ij,
    E_ij=(4/b)omega_i omega_j(-1)^(i+j)
       sum_(r>=0) [1-exp(-2lambda_r b)]
          /[(lambda_r^2+omega_i^2)(lambda_r^2+omega_j^2)],
    lambda_r=2r+1/2,
    0<=E,  |E_ij|<=1/(i+j)+4b/(pi^2 i j).            (4)

On sine modes j>N the Hilbert-kernel Schur estimate gives

    q0[h]>=sum_(j>N)[2a(omega_j)-C_N]|h_j|^2,
    C_N=pi+4b/(pi^2 N)+2(alpha_2+alpha_3)+4(sinh b-b). (5)

This retains the operator norms of both complete internal prime reflections
and the complete pole. The multiplier a is increasing on positive arguments.

The U coefficients are exactly

    u_j=sqrt(2/b)omega_j[1-sqrt(2)(-1)^j]/(omega_j^2+1/4),
    |u_j|<=1/j,  sum_(j>N)|u_j|^2<=1/N.              (6)

The complete-load certificate proves |v_j|<3/j, hence its squared high tail
is at most 9/N, and encloses v_1,...,v_48. Its proof and reproducible checker
are [NEUTRAL_LOAD.md](NEUTRAL_LOAD.md)
and [certify_head_neutral_load.py](certify_head_neutral_load.py).
These bounds retain the endpoint values of n in integration by parts.

Write f=p+h with p in the first N=48 sine modes. For either scalar load,

    2|x+y|^2 >= |x|^2-2|y|^2.                       (7)

Consequently the left side of (3), minus ||f||^2/100, is bounded below by

    <p,A p> +2 Re sum_(i<=N<j) conjugate(p_i)q0_ij h_j
                    +sum_(j>N)d_j|h_j|^2,
    A=q0_LL+u_L u_L^*+v_L v_L^*-(1/100)I,
    d_j=2a(omega_j)-C_N-20/N-1/100.                  (8)

The complete positive high diagonal satisfies d_49>1.0800209029378.
Thus it suffices to prove the finite Schur matrix inequality

    A-sum_(j>N) q0_Lj q0_jL/d_j >=0.                (9)

The loss 20/N was spent exactly once in (8); no high-load cross term remains
silently omitted.

## 3. Enclosure of the complete matrix entries

For different i,j, put

    S(omega)=sum_(r>=0)1/(lambda_r^2+omega^2)
            =Im digamma(1/4+i omega/2)/(2omega).

The unweighted sum in (4) is
[S(omega_i)-S(omega_j)]/(omega_j^2-omega_i^2). For a diagonal entry, sum the
first 1000 rational terms 1/(lambda_r^2+omega^2)^2 and enclose the rest by
one half of the decreasing integral, with at most its first omitted term
added. The required antiderivative tail is

    integral_t^infinity du/(u^2+omega^2)^2
       =atan(omega/t)/(2omega^3)-t/[2omega^2(t^2+omega^2)]. (10)

The exponential correction to (4) is summed through r=11. Every omitted
matrix entry has absolute value less than 10^(-16), by
omega/(lambda^2+omega^2)<=1/(2lambda) and the geometric factor exp(-4b).
The checker verifies this bound at lambda_12=24.5.

For complete digamma enclosures, start from the Binet integral, valid for
Re z>0 ([NIST DLMF 5.9.15](https://dlmf.nist.gov/5.9.E15)):

    digamma(z)=log z-1/(2z)
               -2 integral_0^infinity t/[(t^2+z^2)(exp(2pi t)-1)]dt.

For w=z+8 with z=1/4+i omega/2, expand the denominator three times. Since
|t^2+w^2|>=2 Re(w)Im(w) and integral t^7/(exp(2pi t)-1)dt=1/480,

    digamma(w)=log w-1/(2w)-1/(12w^2)+1/(120w^4)-1/(252w^6)+R,
    |R|<=1/[480 Re(w)Im(w)|w|^6].                   (11)

The recurrence digamma(z)=digamma(z+8)-sum_(r=0)^7 1/(z+r) then encloses
both real and imaginary parts, with no unproved asymptotic remainder.

The n=2 reflection is diagonal, with entry -(-1)^j. For n=3, let
l=log3-b and c=2b-log3. Its exact normalized matrix is, when i differs from j,

    R3_ij=(2/b)[omega_i(-1)^i sin(omega_j l)
                -omega_j(-1)^j sin(omega_i l)]/(omega_j^2-omega_i^2),
    R3_ii=[sin(omega_i c)/omega_i-c cos(omega_i log3)]/b. (12)

The pole coefficients are exactly

    ell_j=-sqrt(2/b)omega_j(-1)^j sinh(b/2)/(omega_j^2+1/4). (13)

Equations (4), (10)-(13) enclose q0_ij, including every sign and factor.
The generator [certify_original_head_kernel.py](certify_original_head_kernel.py)
uses outward mpmath.iv operations at 35 digits. Its serialized float endpoints
are checked against their exact dyadic rational values before use.

## 4. Complete high Schur tail, beyond the explicitly enclosed columns

Let M=4096. For i<=N and j>M, equations (4), (12), (13) imply

    |q0_ij| <= C_i/j,
    C_i=1+4alpha_3/[pi(1-N/(M+1))]+6b/(pi^2 i).      (14)

Indeed |R3_ij|<=2/[pi(j-i)], |ell_i|<=sqrt(b)/(2pi i), and the n=2
reflection is diagonal. Since d_j is increasing,

    sum_(j>M)q0_Lj q0_jL/d_j <= delta_tail I,
    delta_tail=(sum_(i<=N)C_i^2)/(M d_(M+1))
               <0.004070923469.                    (15)

This is a full infinite-dimensional operator bound, not a claim that the
uncomputed matrix entries are negligible or zero.

## 5. Exact dyadic Schur assembly and positive interval elimination

The checker [certify_original_head_schur.py](certify_original_head_schur.py)
reads the coefficient intervals, never their midpoints alone. Put Q=2^48.
For each enclosed cross column q_j, choose integer vectors c_j,r_j such that

    |q_j-c_j/Q|<=r_j/Q componentwise,
    w_j=ceil(Q/(lower endpoint of d_j)).

The integer matrix sum_j w_j c_j c_j^* /Q^3 dominates the central-column
Schur sum. Its missing interval uncertainty is bounded in operator norm by

    epsilon I,
    epsilon=Q^(-3)sum_j w_j
           [2||c_j||_1||r_j||_1+||r_j||_1^2]
            <2.531*10^(-10).                       (16)

Every entry of the large sum is computed with exact Python integers. The
inequality follows by the triangle inequality for the two rank-one cross
errors and their square; replacing Euclidean norms by l1 norms only enlarges
the bound. Using w_j/Q>=1/d_j enlarges the central rank-one sum in the
positive-semidefinite order.

The 48 by 48 interval matrix

    q0_LL+u_Lu_L^*+v_Lv_L^*-(1/100+delta_tail+epsilon)I
                           -Q^(-3)sum_j w_j c_j c_j^*

has all interval LDL pivots strictly positive. A fresh run gives minimum
pivot lower bound greater than 0.37956. This pivot bound is not asserted to
be its least eigenvalue; positivity alone is used. Every arithmetic step
of LDL is enclosed at 45 digits, including the independent uncertainty of
the complete neutral-load coefficients. It follows that (9), hence (3),
holds on finite sine spans. The form closure gives the stated domain.

## 6. Reproduction and exact remaining original-source problem

Run, in order:

    python certify_head_neutral_load.py
    python certify_original_head_kernel.py
    python certify_original_head_schur.py

The JSON files are regenerated coefficient enclosures, not mathematical
point samples. The proof is supplied by the analytic tail bounds and the
successful interval/exact-integer assertions in these scripts.

For an actual top source g at depth delta>0, choose the plateau representative
f=g-c_infinity psi, with c_infinity=U(g)/U(psi). Then U(f)=0 and N(f,s1)=0,
and the actual stationarity Q_delta(f,z)=0 is unchanged. This is not the
origin anchor g-r0 psi unless c_infinity=r0. Split f=f_H+f_T at b; both
pieces are original P vectors. Actual stationarity gives exactly

    Q_delta[f_H]=Q_delta[f_T],
    (1/100)||f_H||_2^2
       <=Q_delta[f_T]+2|U(f_T)|^2+2|(5/787)N(f_T,s1)|^2. (17)

Indeed Q_delta[f_H]=q0[f_H]+delta N[f_H]>=q0[f_H], while the global load
identities give U(f_H)=-U(f_T) and N(f_H,s1)=-N(f_T,s1). The full changed
pole remains in q0. Thus (17) retains explicit genuine tail-load debits,
not vanishing head loads. It requires the actual source hypotheses and
does not extend to arbitrary fields satisfying only finitely many moments.
The full original mixed head/tail form and actual stationarity must still
be retained. In particular this estimate cannot be added to the
hidden xi comparison as an independent positive budget without proving the
same-source block identity and paying all cross terms. No positivity of the
remaining original residual and no RH conclusion is claimed.
