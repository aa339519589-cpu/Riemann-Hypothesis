# Exact Gamma boundary Gram and analytic high-mode bound on the original head

This note concerns the ORIGINAL odd-source form restricted to sources supported
in (0,b), b=log2. It is not the safe latent xi metric. It does not assert a sign
for the finite low-mode block or for the mixed source head/tail Schur complement.

## 1. Exact original head, including pole and reflected primes

Extend a real half-source f supported in (0,b) oddly to the full line. Let

    a(t)=Re digamma(1/4+it/2)-log pi,
    alpha_n=Lambda(n)/sqrt(n), ell(f)=integral_0^b sinh(x/2)f(x)dx.

The complete original source form on this support is

    q_0[f]=2<f,a(D)_odd f>
          +2alpha_2 integral_0^b f(x)f(b-x)dx
          +2alpha_3 integral_(log3-b)^b f(x)f(log3-x)dx
          -8ell(f)^2.                                  (1)

Every forward prime overlap vanishes. The only nonzero internal reflected
prime overlaps are n=2,3; n=4 touches only the zero-measure endpoints.
All larger prime powers miss this support. Equation (1) is the direct signed
source form, not a separate P/N completion for nonzero-trace half-sources.

Use the orthonormal sine basis

    e_j(x)=sqrt(2/b)sin(omega_j x), omega_j=j*pi/b, j>=1.

## 2. Exact positive boundary Gram

Put lambda_r=2r+1/2. The complete Gamma matrix is

    2<e_i,a(D)_odd e_j>=2a(omega_j)delta_ij-E_ij,
    E_ij=(4/b)omega_i omega_j(-1)^(i+j)
       sum_(r>=0) [1-exp(-2lambda_r b)]
                /[(lambda_r^2+omega_i^2)(lambda_r^2+omega_j^2)]. (2)

In particular E is positive semidefinite: each r contributes one positive
rank-one Gram matrix, despite the alternating sine signs.

To prove (2), expand the exact multiplier as

    a(t)=-C0+2 sum_(r>=0)t^2/[lambda_r(lambda_r^2+t^2)],
    C0=log pi-digamma(1/4).

For an unnormalized sine, the Dirichlet half-line exponential kernel has

    integral_0^b [exp(-lambda|x-y|)-exp(-lambda(x+y))]
                       sin(omega_j y)dy
       =[2lambda/(lambda^2+omega_j^2)]sin(omega_j x)
        -[2omega_j(-1)^j/(lambda^2+omega_j^2)]
                                      exp(-lambda b)sinh(lambda x). (3)

This follows either by two elementary integrations or by solving the second-
order inhomogeneous equation with u(0)=0 and u'(b)=-lambda u(b). Finally

    integral_0^b sin(omega_i x)exp(-lambda b)sinh(lambda x)dx
       =-omega_i(-1)^i[1-exp(-2lambda b)]
                                      /[2(lambda^2+omega_i^2)].

Substitution gives (2), including the factor 4/b. All sums in the boundary
Gram are absolutely convergent on finite sine spans. The full Gamma operator
is not replaced by its large-frequency logarithmic approximation.

## 3. Uniform operator control, including infinitely many high modes

For fixed positive A,B the function
1/[(lambda^2+A^2)(lambda^2+B^2)] decreases in lambda. Therefore

    sum_(r>=0)1/[(lambda_r^2+A^2)(lambda_r^2+B^2)]
       <=1/(A^2B^2)+(1/2)integral_0^infinity
                                      d lambda/[(lambda^2+A^2)(lambda^2+B^2)]
       =1/(A^2B^2)+pi/[4AB(A+B)].

Dropping the factor 1-exp(-2lambda_r b) only increases the sum. Thus

    |E_ij|<=1/(i+j)+4b/(pi^2 i j).                     (4)

The Hilbert kernel 1/(i+j) has norm at most pi by the Schur weights i^(-1/2):
the required positive sum is bounded by the integral of the decreasing
function x^(-1/2)/(i+x), whose value is pi/sqrt(i). Consequently on the
sine subspace j>N,

    0<=E<= [pi+4b/(pi^2 N)] I.                        (5)

The rank-one remainder uses sum_(j>N)j^(-2)<=1/N. This is an infinite-
dimensional bound, not a truncation justified by numerical decay.

Both partial reflection operators in (1) have norm at most one before
multiplication by alpha_n. Also

    8||sinh(x/2)||_(L2(0,b))^2=4(sinh b-b).

Hence for every field in the closed restricted Gamma-form domain that is
orthogonal to e_1,...,e_N (equivalently, first on finite sine spans and then
by that form closure),

    q_0[f]>=sum_(j>N) [2a(omega_j)-C_N]|<f,e_j>|^2,
    C_N=pi+4b/(pi^2 N)+2(alpha_2+alpha_3)+4(sinh b-b).  (6)

The multiplier a(t) is increasing for t>=0 by its positive series, so a single
explicit lower bound for a(omega_(N+1)) gives a uniform high-mode gap.
Equation (6) also remains valid after adding any nonnegative finite-rank
penalty for exact lawful source functionals. A low/high Schur proof must
still retain their actual off-diagonal loads.

The un-repaired complete Schur certificate is proved in [REPORT.md](REPORT.md).
