# A grouped six-vector expansion of the original head's complete high columns

This note bounds the omitted ORIGINAL source-head columns while retaining
Gamma/reflection/pole cancellation in each low-mode vector. It supplies a
structured Schur-tail component, not a proof that the full unpenalized head
is positive. All finite-block and high-diagonal certifications remain separate.

The starting exact original matrix is the
[complete sine Gram](GAMMA_SINE_GRAM.md).
Put

    b=log2, c=log(3/2), omega_i=i*pi/b,
    lambda_r=2r+1/2, alpha=log3/sqrt3,
    S(A)=sum_(r>=0)(1-exp(-2b lambda_r))/(lambda_r^2+A^2),
    sigma_i=(-1)^i,
    ell_i=integral_0^b sinh(x/2)sqrt(2/b)sin(omega_i x)dx
          =-sigma_i sqrt(2/b) omega_i sinh(b/2)/(omega_i^2+1/4).

In the formulas below S ALWAYS includes the damped subtraction. Set

    A=omega_i, B=omega_j,
    A_i=sigma_i A,
    B_i=sigma_i A S(A)+alpha sin(Ac),
    theta_j=sigma_j B S(B)+alpha sin(Bc),
    c_s=sqrt(2/b)sinh(b/2).

## 1. Exact combined off-diagonal formula

For i!=j, the entire q_0 matrix entry is

    q_ij=(4/b)[A_i theta_j-sigma_j B B_i]/(B^2-A^2)
                                      -8ell_i ell_j.          (1)

The prime-two reflection is diagonal in the sine basis and contributes no
cross entry. The Gamma boundary Gram has the partial-fraction form

    -E_ij=-(4/b)sigma_i sigma_j A B [S(A)-S(B)]/(B^2-A^2).

For the compressed prime-three reflection, integration of the Wronskian
on [c,b] gives exactly

    (2/b)integral_c^b sin(Ax)sin(B(log3-x))dx
       =(2/b)[sigma_i A sin(Bc)-sigma_j B sin(Ac)]/(B^2-A^2).

Multiplying by 2alpha and adding the Gamma and full pole proves (1).
The sign at each compressed boundary is retained; no separate norm bound
for these three pieces has been taken.

## 2. Six exact low-mode vectors and a controlled remainder

For r=0,1,2, define real low-mode vectors

    v_(r,i)=-(4/b)A^(2r) B_i+8ell_i c_s(-1/4)^r,
    w_(r,i)=(4/b)A^(2r) A_i.                             (2)

Expanding ONLY the two elementary denominators in (1) gives

    q_ij=sum_(r=0)^2 [sigma_j v_(r,i)/B^(2r+1)
                            +theta_j w_(r,i)/B^(2r+2)] + R_ij. (3)

There is no asymptotic replacement of S(B), theta_j or a zeta/prime row.
For a low/high split i<=N<j with rho=N/(M+1)<1 and j>M, the exact geometric
remainders imply

    |R_ij|<=r_(7,i)/B^7+r_(8,i)/B^8,
    r_(7,i)=(4/b)A^6|B_i|/(1-rho^2)+8|ell_i|c_s/64,
    r_(8,i)=(6/b)A^7/(1-rho^2),                         (4)

provided |theta_j|<3/2. In fact the two exact remainder pieces are

    R_geom=(A/B)^6 (4/b)
                   [A_i theta_j-sigma_j B B_i]/(B^2-A^2),
    R_pole=-8ell_i c_s sigma_j/[64 B^7(1+1/(4B^2))].      (5)

The leading vector v_0 is the FULL signed endpoint density:

    v_(0,i)=-sqrt(2/b)l_i(b),
    l_i(b)=-2integral_0^b [kappa(b-x)-kappa(b+x)]e_i(x)dx
               +2alpha e_i(c)-8sinh(b/2)ell_i.           (6)

Thus a near-neutral cancellation of the actual boundary forcing remains
inside v_0 before any positive rank-sum envelope. It is not replaced by
three independent absolute Gamma/reflection/pole rows.

## 3. Elementary bounds sufficient for a tiny uniform residual

The positive sum satisfies

    0<S(A)<=1/A^2+pi/(4A).                               (7)

Indeed discard the exponential subtraction, isolate the first decreasing
summand, and bound the remaining sum by its half-line integral. Also
alpha<2/3: the function (x-1)/sqrt(x)-log x is strictly increasing for x>1
from value zero, since its derivative is
(sqrt(x)-1)^2/(2x^(3/2)). Apply this at x=3.

Using b<3/4, 3<pi<22/7 and A>=pi/b, (7) gives

    |B_i|<pi/4+b/pi+2/3<11/14+1/4+2/3<7/4.             (8)

For j>=8, the same bound gives

    |theta_j|<11/14+1/(3j)+2/3<=11/14+1/24+2/3<3/2.    (9)

Finally sinh(b/2)^2=1/8 exactly, so

    c_s^2=1/(4b),  |ell_i|c_s<=1/(4b A).                (10)

Suppose rho<=1/64. Dividing the two geometric terms in (4) by their
frequency powers and using A/B=i/j yields

    |R_geom| <= [(7+6rho)/(pi(1-rho^2))] i^6/j^7.

The pole remainder is at most

    1/(32b A B^7)=b^7/[32pi^8 i j^7]
                       <i^6/(200000 j^7).              (11)

Here b<1 and 32*3^8=209952>200000. The exact rational inequality

    (7+6/64)/[3(1-1/4096)]+1/200000<5/2

therefore proves the useful uniform bound

    |R_ij|<(5/2)i^6/j^7,
                 i<=N, j>M, M+1>=64N, M>=7.            (12)

## 4. The entire omitted Schur debit, not a sampled tail

Let d_j>=d_*>0 be ANY proved positive diagonal lower comparison for the
infinite high block, j>M. For a low vector x, use the factor-seven square
bound for the six terms in (3) and its one remainder. The residual part
of the resulting Schur debit is bounded by

    7 sum_(j>M) |sum_(i<=N)x_i R_ij|^2/d_j
       <= epsilon_rem ||x||_2^2,
    epsilon_rem = [175/(52 d_*)] sum_(i=1)^N i^12/M^13.  (13)

This follows from Cauchy--Schwarz in the finite i index, (12), and the
complete integral bound sum_(j>M)j^(-14)<=1/(13M^13).
All j>M are included. For N=64,M=4096, the exact value multiplying 1/d_*
is

    140456698917930754513175 /
    148433760041419827630061740822747494183805648896
                         <1/10^24.                     (14)

In particular it is less than 10^(-12) even if the only available
high-diagonal lower bound were d_*=10^(-6). The coefficient in (14) is
already the FACTOR-SEVEN remainder debit, not an unmultiplied row error.

The six leading terms still give their structured positive rank matrices:

    7 sum_(r=0)^2 [v_r v_r^T sum_(j>M)1/(d_j B_j^(4r+2))
                 +w_r w_r^T sum_(j>M)theta_j^2/(d_j B_j^(4r+4))]. (15)

Their interval coefficients and the finite block must be certified before
claiming a head sign. Bounds on (15) must not undo the exact cancellation
inside the v_r vectors. The standard-library checker accompanying this
note verifies only the exact rational estimates (8)-(14); it is not a
checker for the complete original-head Schur certificate.
