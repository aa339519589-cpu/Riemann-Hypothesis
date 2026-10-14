# Coercivity of the complete original source head without auxiliary loads

## 1. The theorem and its exact scope

Let b=log 2, alpha_n=Lambda(n)/sqrt(n), and let the positive-wing original
source form on sources supported in (0,b) be

    q0[f]=2<f,a(D)_odd f>
         +2alpha_2 integral_0^b conjugate(f(x))f(b-x)dx
         +2alpha_3 integral_(log(3/2))^b
                                conjugate(f(x))f(log3-x)dx
         -8|integral_0^b sinh(x/2)f(x)dx|^2,
    a(t)=Re digamma(1/4+it/2)-log pi.                    (1)

The compressed reflected pairings are real on the diagonal. The domain is
the closure of finite sine spans in the restricted original odd Gamma-form
norm. In particular it includes the head restrictions of the proved actual
fixed-depth sources, whose odd zero extensions belong to H^sigma for some
0<sigma<1/2. The theorem is

    q0[f] >= 10^(-10) ||f||_L2(0,b)^2.                  (2)

No pole or neutral load is added to the left side of (2). Both internal
prime reflections, the full Gamma multiplier, and the full pole are retained.
The theorem is about this ORIGINAL source restriction. It does not prove
positivity of the original full-line form or of its mixed tail Schur
complement. It does not assert separate original P/N membership for an
arbitrary nonzero-trace source; the actual original-P use also retains the
weighted potential domain.

This improves the previous repaired head theorem by a different estimate,
not by deleting its two positive loads. The complete high columns are
first grouped as signed endpoint data. A structured low-rank tail bound
preserves that cancellation, which a scalar norm tail bound loses.

## 2. Complete sine matrix and infinite high-block lower comparison

Let e_j=sqrt(2/b)sin(omega_j x), omega_j=j*pi/b and lambda_r=2r+1/2.
The exact matrix identity is proved in
[the original sine Gram](GAMMA_SINE_GRAM.md):

    qGamma_ij=2a(omega_j)delta_ij-E_ij,
    E_ij=(4/b)omega_i omega_j(-1)^(i+j)
       sum_(r>=0)(1-exp(-2lambda_r b))
                /[(lambda_r^2+omega_i^2)(lambda_r^2+omega_j^2)],
    E>=0,   |E_ij|<=1/(i+j)+4b/(pi^2 i j).             (3)

The prime-two reflection is diagonal with entries
2alpha_2(-1)^(j+1). The prime-three reflection is compressed to
(log(3/2),b), and the pole is the exact rank-one matrix -8ell ell^T,
where

    ell_j=-sqrt(2/b)omega_j(-1)^j sinh(b/2)/(omega_j^2+1/4).

For every high source h supported on modes j>N, the Hilbert-kernel estimate
and the full reflection/pole operator norms give

    q0[h]>=sum_(j>N)[2a(omega_j)-C_N]|h_j|^2,
    C_N=pi+4b/(pi^2 N)+2(alpha_2+alpha_3)+4(sinh b-b).  (4)

Set tau=10^(-10), N=64, M=4096, and

    d_j=2a(omega_j)-C_N-tau.

The function a is increasing on positive arguments. The complete interval
evaluation gives d_65>2.0732853777616627 and d_(4097)>10.3605323529835.
Consequently all high diagonals are strictly positive. It is enough to
prove the finite Schur inequality

    q0_LL-tau I-sum_(j>N)q_Lj q_jL/d_j >=0.            (5)

There is no neutral-load tail loss in d_j or (5), and no finite cutoff is
substituted for the sum in (5).

## 3. Preserve the exact endpoint cancellation before taking absolute values

The independently derived grouped expansion is
[the complete high-column remainder theorem](GROUPED_HIGH_TAIL.md).
Here is its interface with (5). Put c=log(3/2), sigma_i=(-1)^i and

    S(A)=sum_(r>=0)(1-exp(-2b lambda_r))/(lambda_r^2+A^2),
    A_i=sigma_i omega_i,
    B_i=A_i S(omega_i)+alpha_3 sin(omega_i c),
    theta_j=sigma_j omega_j S(omega_j)+alpha_3 sin(omega_j c),
    c_s=sqrt(2/b)sinh(b/2).

For i!=j, the entire original matrix entry is exactly

    q_ij=(4/b)[A_i theta_j-sigma_j omega_j B_i]
                        /(omega_j^2-omega_i^2)-8ell_i ell_j. (6)

In particular the Gamma, compressed reflection and pole must not be
bounded separately before the following grouping. For r=0,1,2 define

    v_(r,i)=-(4/b)omega_i^(2r)B_i+8ell_i c_s(-1/4)^r,
    w_(r,i)=(4/b)omega_i^(2r)A_i.

Then, for i<=N and j>M,

    q_ij=sum_(r=0)^2 [sigma_j v_(r,i)/omega_j^(2r+1)
                       +theta_j w_(r,i)/omega_j^(2r+2)]+R_ij. (7)

All these vectors are explicit exact analytic data; none is defined by a
sampled near-null eigenvector. In fact v_0 is proportional to the COMPLETE
original endpoint load of e_i at b. This is the cancellation retained by
the certificate.

One has |theta_j|<3/2. The code uses the exact geometric remainder bounds

    |R_ij|<=r_(7,i)/omega_j^7+r_(8,i)/omega_j^8,
    r_(7,i)=(4/b)omega_i^6|B_i|/(1-rho^2)+8|ell_i|c_s/64,
    r_(8,i)=(6/b)omega_i^7/(1-rho^2), rho=N/(M+1).       (8)

A separate simple rational check also gives |R_ij|<(5/2)i^6/j^7 for these
N,M. Both estimates include the full pole remainder. No arithmetic or
Gamma row has been replaced by an asymptotic value.

Define, using d_*=d_(M+1),

    I_p=(b/pi)^(2p)/[(2p-1)M^(2p-1)d_*], p=1,...,8,
    epsilon_R=2||r_7||^2 I_7+2||r_8||^2 I_8.

The factor-seven square inequality applied to the six terms in (7) and
its one remainder proves the COMPLETE ordered tail bound

    sum_(j>M)q_Lj q_jL/d_j <= T,
    T=7 sum_(r=0)^2 [I_(2r+1)v_r v_r^T
                         +(9/4)I_(2r+2)w_r w_r^T]
                                      +7epsilon_R I.  (9)

Here sum_(j>M)omega_j^(-2p)/d_j<=I_p by monotonicity and the integral test.
The scalar remainder in the actual run is below 3.330e-26. The six rank
matrices are retained; they are NOT replaced by their scalar operator norm.

## 4. Sharper enclosures of the complete kernel, not new numerical assumptions

The generator is
[certify_unrepaired_head_kernel.py](certify_unrepaired_head_kernel.py).
It uses outward interval arithmetic and the same exact complete matrix
formulas as (3). Two analytically bounded improvements are essential at
the small scale in (2).

First, apply the Binet formula at w=z+128, z=1/4+i omega/2. The same
three-step denominator expansion used in the preceding source-head proof
is

    digamma(w)=log w-1/(2w)-1/(12w^2)
                            +1/(120w^4)-1/(252w^6)+R,
    |R|<=1/[480 Re(w) Im(w)|w|^6].                     (10)

Use the exact recurrence digamma(z)=digamma(w)-sum_(r=0)^127 1/(z+r).
For completeness, the denominator remainder in Binet is bounded with
|w^2+t^2|>=2Re(w)Im(w) and
integral_0^infinity t^7/(exp(2pi t)-1)dt=1/480. Thus increasing the
recurrence shift changes no asymptotic assumption or unproved truncation.

Second, the diagonal rational series in (3) is summed through r=999.
For f(t)=(t^2+omega^2)^(-2), at t=2000+1/2 the remaining spacing-two sum
has the enclosure

    sum_(k>=0)f(t+2k)
       in (1/2)integral_t^infinity f+f(t)/2-f'(t)/6
                                         +[-E,E],
    E=-f'''(t)/90.                                    (11)

The derivative formulas are

    f'''(t)=-24t(5t^2-3omega^2)/(t^2+omega^2)^5,
    f''''(t)=24(35t^4-42omega^2t^2+3omega^4)
                                           /(t^2+omega^2)^6.

For every low mode omega<=omega_64, t>2omega, so f'''' is positive on the
whole remaining ray and f''' tends to zero. Euler--Maclaurin through B2,
with spacing two, has coefficients 1/2,1/2,-1/6. Its B4 remainder has
absolute bound (2^3/4!)(1/30)integral|f''''|=-f'''(t)/90, proving (11).
The integral is elementary and evaluated outward. This is not a sampled
derivative-sign test.

The exponentially damped Gamma correction is summed through r=19. Using
omega/(lambda^2+omega^2)<=1/(2lambda), its COMPLETE omitted matrix entries
are below

    exp(-2b lambda_20)/[b lambda_20^2(1-exp(-4b))]<10^(-25).

The analogous omitted scalar damped S sum is smaller still. Real and
imaginary Binet errors, recurrence, rational diagonals, all trigonometric
reflection factors and the complete pole are propagated as intervals.
Serialized binary float endpoints are checked outward by their exact dyadic
values; their central values are not used as uncertified coefficients.

## 5. Exact finite sum and verified positive interval elimination

The assembly is
[certify_unrepaired_head_schur.py](certify_unrepaired_head_schur.py).
For each N<j<=M, enclose the cross column as Q^(-1)(c_j+e_j),
Q=2^60, with integer center c_j and |e_(j,i)|<=r_(j,i).
Use the exact integer weight w_j=ceil(Q/d_j,lower). Then

    sum_(N<j<=M)q_Lj q_jL/d_j
       <=Q^(-3)sum_j w_j c_j c_j^T+epsilon_cross I,
    epsilon_cross=Q^(-3)sum_j w_j
                [2||c_j||_1||r_j||_1+||r_j||_1^2].     (12)

All large matrix products and sums in (12) use Python integers, with no
floating matrix multiplication or spectral estimate. In a fresh full run,
epsilon_cross<8.594e-15. The finite comparison matrix is

    A=q0_LL-tau I-Q^(-3)sum_j w_j c_j c_j^T
                                      -epsilon_cross I-T.  (13)

The symmetric input intervals are intersected, and every operation in (13)
and its LDL elimination is outward. All 64 pivot intervals have positive
lower endpoints; the minimum lower endpoint is greater than
0.000907339663. This number is an LDL pivot, not a claimed least eigenvalue.
Together with (4), (9), (12), and the positive d_j, this proves (5), hence
(2), first on finite sine spans and then on the stated closed form domain.

Reproduction needs no saved cache or numerical-log evidence:

    python certify_unrepaired_head_kernel.py
    python certify_unrepaired_head_schur.py

The first command rebuilds all outward kernel intervals. The second checks
the finite integer sum, complete analytic high tail and interval LDL. The
separate standard-library grouped-remainder checker tests the coarse
rational bound, not the sign of a finite matrix.

## 6. Immediate original-source consequence and the remaining sign gap

For every delta>=0 and every head in the genuine weighted original domain,

    Q_delta[f]=q0[f]+delta N[f/psi]>=10^(-10)||f||^2.    (14)

Thus at the log2 cut the actual head inverse now has the EXPLICIT L2 bound
10^10; no actual-depth compactness argument or auxiliary head load is needed
for this assertion. For an actual stationary source and any fixed constant
psi representative e=e_H+e_T, full stationarity still gives

    e_H=-A_(delta,b)^(-1)L_T,
    Q_delta[e_H]=Q_delta[e_T].                         (15)

The complete mixed Gamma/prime/pole functional L_T remains in (15).
Equation (2) does not set it to zero. In particular the full tail original
form and its signed Schur subtraction are not assigned a favorable sign.
The globally infinite neutral theta space and all changed pole/gauge terms
remain relevant outside this restricted head theorem. No RH conclusion is
claimed from (2) or (15).

## 7. Effective actual-source consequence at the same endpoint

The separate [actual endpoint consequence](ACTUAL_ENDPOINT.md) combines
the unpenalized sign (2), [complete mixed forcing](MIXED_FORCING.md), and
the [complete reflected potential tail](POTENTIAL_TAIL.md). For a genuine
actual source at fixed depth delta, with its TRUE common seed a and the
SAME hidden head-weighted mean c_a, it gives

    P[g/psi]<=[(1-delta)(8000/(delta gamma_H)+8C_V)
                                      C_amp(delta)]^2 M,
    gamma_H=10^(-10), M=integral Wxi|a-c_a|^2.

There is no unknown head spectral gap and no omitted global U scalar in
this implication. C_V and C_amp(delta) are the proved analytic tail and
actual-regularity constants; no numerical value for their product or
uniformity as delta decreases to zero is claimed. This observes the
original actual source in the same hidden norm, but does not lower-bound
the remaining original signed Schur residual or exclude an actual state.

The reproducible scripts require Python 3 and mpmath. They do not require
a numerical eigensolver. Generated JSON and run logs are reproducible
outputs, not frozen proof prerequisites.
