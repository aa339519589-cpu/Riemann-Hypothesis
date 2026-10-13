# Complete-form control of an infinite high-frequency tail

2026-10-13. This extends the [finite-total-rank estimates](REPORT.md) in a different norm: it bounds the complete form of an infinite tail by its absolute coefficient majorant. It retains every internal mixed term and every prime power, with no separation or finite-rank condition. The estimate permits a small negative defect and does not establish the original coefficient-one comparison.

## 1. Exact scope and original domain

Use the original even operator and Fourier convention of the [original form foundation](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md):

w=m^2, F=mv, hat(F)(t)=integral F(x)exp(itx)dx,

h[v]=<F,b(D)F>-C0||F||_2^2-<F,SF>,

(SF)(x)=sum_(n>=2) Lambda(n)n^(-1/2)[F(x+log n)+F(x-log n)].

Here C0=EulerGamma+pi/2+3log 2+log pi, and

 b(t)=sum_(j>=0) 2t^2/[a_j(a_j^2+t^2)],  a_j=2j+1/2.

The complete symbol is nonnegative and b(t)=log|t|+O(1) at infinity. The prime sum is used in its absolutely convergent source quadratic pairing; no bounded unweighted L2 realization of S is assumed. For each fixed delta<pi/4 the complete analytic theta weight satisfies

|w(x+iy)|<=C_delta exp(C_delta|x|-c_delta exp(2|x|)), |y|<=delta.

Let T>=2 and let z range over a countable set with Re z>=T and |Im z|<=1/2. Write

p_T(x)=sum_z a_z exp(izx), q_T(x)=(p_T(x)+p_T(-x))/2=sum_z a_z cos(zx),

v_T=m q_T, F_T=w q_T, M_T=sum_z|a_z|<infinity, A_T=||F_T||_2.

Assume the cosine series converges absolutely in the original operator graph norm. This holds, for example, if sum_z |a_z|log(2+|z|)<infinity: the complete Gamma multiplier and bounded physical prime operator give ||m cos(zx)||+||H(m cos(zx))||<=C log(2+|z|), uniformly in the stated strip. Thus the theorem applies to every subset of the actual negative-eigenstate expansion described in Section 5. Every actual-zero tail remains ground-perpendicular. The estimates below allow arbitrary complex a_z; conjugate-paired actual coefficients make v_T real.

If A_T=0 the assertions are immediate. Otherwise constants below are independent of T, the number or separation of nodes, their multiplicities, and their maximum real part. They depend only on the fixed original weight and one chosen delta in (0,pi/4).

## 2. One-sided analytic continuation needs no exponential coefficient tail

For 0<=y<=delta,

|p_T(x+iy)|<=M_T exp(|x|/2)exp(-Ty).

The positive-frequency series is holomorphic for y>0 and continuous on y=0, by uniform absolute convergence on compact subsets. This does NOT assert that p_T has a lower-half-plane continuation or that q_T has a fixed complex strip. For example, the displayed bound uses only M_T, not sum |a_z|exp(delta Re z).

The theta envelope therefore gives

||w(.+i delta)p_T(.+i delta)||_(L1 and L2)<=C_delta M_T exp(-delta T).       (1)

Vertical contour ends vanish uniformly for 0<=y<=delta. With the +it Fourier convention, shift the positive-frequency source upward and the reflected source downward. For |t|<=T/2 this yields

|hat(F_T)(t)|<=C_delta M_T exp(-delta T/2),

(1/(2pi)) integral_(|t|<=T/2)|hat(F_T)(t)|^2 dt
 <=C_delta T M_T^2 exp(-delta T).                                      (2)

One can first shift finite sums and pass using the same dominated bounds, so no hidden analytic extension of the evenized source is used.

For all sufficiently large T, nonnegativity of the complete b and its full high-frequency lower bound imply

<F_T,b(D)F_T>
 >=(log T-C)A_T^2-C T log(T) M_T^2 exp(-delta T).                       (3)

## 3. Complete prime term: logarithm of the coefficient-to-source ratio

On the real line, |q_T(x)|<=M_T exp(|x|/2). Absorbing fixed exponential factors in the theta envelope gives, for s>=0,

||1_(|x|>=s)F_T||_2<=C M_T exp(-c exp(2s)).                            (4)

For any d>=0, split the correlation integral into |x|>=d/2 and its complement; in the complement |x+d|>=d/2. Cauchy--Schwarz gives

|<F_T,F_T(.+d)>|<=min(A_T^2, 2 A_T ||1_(|x|>=d/2)F_T||_2).

Thus at d=log n,

|<F_T,F_T(.+log n)>|<=min(A_T^2,C A_T M_T exp(-cn)).                    (5)

The other shift is the complex conjugate. Both are retained in S. Let R=M_T/A_T and choose an integer

N=max(2,ceil(K log(2+R)))

with a sufficiently large fixed K. The elementary Chebyshev bound Psi(X)=sum_(n<=X)Lambda(n)<=3X and partial summation give

sum_(2<=n<=N)Lambda(n)/sqrt(n)<=C sqrt(N).

For clarity, for each prime power p^k in (m,2m], include one factor p in a product (not a factor p^k). This product divides binomial(2m,m): the valuation formula v_p(binomial(2m,m))=sum_j[floor(2m/p^j)-2floor(m/p^j)] has nonnegative summands, and each such k contributes one. Hence Psi(2m)-Psi(m)<=2m log2. Summing over dyadic m and taking the first power of two at least X gives Psi(X)<4(log2)X<3X. No prime number theorem is needed.

Also, Lambda(n)<=log n implies

sum_(n>N)Lambda(n)n^(-1/2)exp(-cn)<=C exp(-c' N).

Select K so that R exp(-c'N)<=C. Sum (5), including both shifts and every prime power, to obtain

|<F_T,SF_T>|<=C A_T^2 sqrt(log(2+M_T/A_T)).                            (6)

All sums are absolutely bounded in this proof. No finite-prime proxy appears.

## 4. Full original form and optimized negative defect

Combining (3), (6), and the original -C0 source term gives

h[v_T]>= [log T-C-C sqrt(log(2+M_T/A_T))] A_T^2
         -C T log(T) M_T^2 exp(-delta T).                              (7)

This includes every mixed interaction among all nodes in the infinite tail.

Theorem. There are constants c,C,T_* depending only on the fixed original operator such that

h[v_T]>=-C M_T^2 exp(-c (log T)^2), T>=T_*.                           (8)

Indeed put y=log(2+M_T/A_T). For sufficiently large log T, the square bracket in (7) is nonnegative if y<=eta(log T)^2, for a fixed sufficiently small eta>0. On the remaining set y>eta(log T)^2, we have M_T/A_T=exp(y)-2>=exp(y)/2 and

(C+C sqrt(y))A_T^2<=C M_T^2(1+sqrt(y))exp(-2y)
 <=C M_T^2 exp(-eta(log T)^2).

The separate T logT exp(-delta T) defect can be absorbed into the same bound after decreasing c.

## 5. Exact missing comparison

For an actual real even nonground eigenstate H u=-kappa u with kappa>0, put f=m u and B(z)=integral f(x)cos(zx)dx. The [translated full explicit formula](../20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md), Appendix C, gives

 u=-(2/kappa)sum_(Re z>0) j_z B(z)m cos(zx).

The two pole terms vanish by the ground pairing integral cosh(x/2) f(x)dx=0, and the source equation is Lf=-kappa u/m for L=b(D)-C0-S. This gives the displayed normalization without a spectral-synthesis assumption. Here z runs over distinct genuine Xi zeros with positive real part, both members of each nonreal conjugate pair are retained, and j_z is the actual multiplicity. Fixed-order smoothness of the actual source and its complete theta tails make B strip-Schwartz, so this series and every subseries converge absolutely in the original operator graph norm. For the height-T tail the coefficients are a_z=-2j_z B(z)/kappa, and hence

 M_T=(2/kappa)sum_(Re z>=T)j_z|B(z)|.

Bound (8) pays the entire high-tail self-interaction in this absolute, actual coefficient norm. It needs neither finite total rank nor a false fixed analytic strip for B. It does not make the high tail nonnegative, and it does not pay mixed terms between this tail and its complement.

Most importantly, (7)--(8) do not bound M_T/A_T for the actual eigenstate. They therefore do not establish the requested coefficient-one comparison, do not remove the kappa-dependent coefficient cost, and do not prove RH. A genuine eigenstate-specific relative estimate or a signed full coupling identity remains necessary.

## 6. Weighted sampling-square bound for genuine zero tails

For the actual zero family, the absolute l1 coefficient majorant can be replaced by a logarithmically weighted l2 sum. The new input is an upper synthesis estimate from the unconditional local zero count, with actual multiplicities retained. No lower frame bound or separation hypothesis is used.

### 6.1. Assumptions and notation

Let Z_T contain distinct genuine Xi zeros z=gamma_z+i eta_z with gamma_z>=T>=2, including both members of nonreal pairs if present, and |eta_z|<=1/2. Let j_z be their actual multiplicities. The unconditional unit-height count, with multiplicities, is

 sum_(gamma_z in [n,n+1]) j_z <= C log(2+n).

For instance this follows from the full Riemann--von Mangoldt count and its O(log T) remainder, as recorded in E. Hasanalizade, Q. Shen and P.-J. Wong, [Counting zeros of the Riemann zeta function](https://arxiv.org/abs/2107.06506), Corollary 1.2. Taking a difference across an interval of bounded length gives the displayed estimate; endpoints and small heights are absorbed in the fixed constant.

Take the actual coefficient family or another family whose cosine series converges absolutely in the original H graph norm, and assume the following square budget is finite:

 J_T^2=sum_(z in Z_T) (|a_z|^2/j_z) log(2+gamma_z).

Put p_T(x)=sum a_z exp(izx), initially interpreted on the real axis as the local L2 limit justified below, and q_T(x)=(p_T(x)+p_T(-x))/2, v_T=mq_T, F_T=wq_T, A_T=||F_T||_2, with w=m^2 and the full original H of Sections 1–5. In the actual eigenstate expansion a_z=-2j_z B(z)/kappa, so exactly

 J_T^2=(4/kappa^2)sum_(gamma_z>=T) j_z log(2+gamma_z)|B(z)|^2.             (11)

The actual strip-Schwartz bound on B pays finiteness. Unlike the former M_T^2, this is a weighted sum of the actual Hermitian sampling squares, not a square of an l1 sum.

### 6.2. A local upper synthesis bound with no separation hypothesis

Choose a nonnegative smooth compactly supported rho with rho>=1 on [0,1] and support in [-1,2]. For a finite partial sum and any real s,

 integral_s^(s+1)|p_T(x)|^2 dx
 <=integral rho(x-s)|p_T(x)|^2 dx.

The (z,w) Gram entry on the right is

 exp(i(w-conjugate(z))s)
 integral rho(y)exp(i(w-conjugate(z))y)dy.

Since |eta_z+eta_w|<=1, three integrations by parts in y give the uniform absolute bound

 C exp(|s|)(1+|gamma_z-gamma_w|)^(-3).                                (12)

The unit-height zero count gives

 sum_w j_w(1+|gamma_z-gamma_w|)^(-3)<=C log(2+gamma_z).                 (13)

Indeed sum over unit-distance shells and use
log(2+gamma_w)<=log(2+gamma_z)+log(2+|gamma_w-gamma_z|).

Apply

 2|a_z a_w| <= (|a_z|^2/j_z)j_w + (|a_w|^2/j_w)j_z

to the absolutely bounded Gram sum. Equations (12)--(13) yield

 integral_s^(s+1)|p_T(x)|^2 dx <= C exp(|s|)J_T^2.                    (14)

The constant is independent of the number of nodes, their minimum separation, total rank, and maximum height. Tails of the square budget give local L2 convergence and justify passage from finite sums. Reflection and |(p(x)+p(-x))/2|^2<=(|p(x)|^2+|p(-x)|^2)/2 give the corresponding estimate for q_T.

### 6.3. Theta tails and one-sided continuation

Multiplying (14) by the complete real theta envelope and summing unit intervals proves

 ||1_(|x|>=R)F_T||_2 <= C J_T exp(-c exp(2R)), R>=0.                  (15)

For any fixed 0<delta<pi/4, the coefficients of p_T(x+i delta) are a_z exp(-delta z), with magnitudes |a_z|exp(-delta gamma_z). Their square budget is at most exp(-2delta T)J_T^2. Apply (14) to these coefficients, then the complete shifted theta envelope, to obtain

 ||w(.+i delta)p_T(.+i delta)||_(L1 and L2)
 <=C_delta J_T exp(-delta T).                                      (16)

For L1, use Cauchy--Schwarz on each unit interval and sum the theta envelope. This step does not replace the evenized source norm by the positive-frequency norm.

The same separate contours as in Section 2 now yield

 (1/(2pi))integral_(|t|<=T/2)|hat(F_T)(t)|^2dt
 <=C_delta T J_T^2 exp(-delta T).                                  (17)

These contours may be performed on finite sums. The local L2 estimate and the real theta envelope give convergence in source L1 and L2; (16) gives domination after shifting. Thus neither a two-sided analytic strip for q_T nor an exponential coefficient tail has been introduced.

### 6.4. Complete original form and actual interface

Using (15) in the exact shift-correlation split and the elementary Chebyshev estimate proved in Section 3 gives

 |<F_T,SF_T>|<=C A_T^2 sqrt(log(2+J_T/A_T)).                         (18)

As before A_T=0 is interpreted separately. Combining (17), the complete Gamma lower bound, both prime shifts and every prime power gives

 h[v_T] >= [log T-C-C sqrt(log(2+J_T/A_T))]A_T^2
            -C T log(T)J_T^2 exp(-delta T),                         (19)

and therefore, for T>=T_* depending only on the fixed operator,

 h[v_T]>=-C J_T^2 exp(-c(log T)^2).                                (20)

For a real eigenstate write B(z)=b_z-i c_z with real b_z,c_z, consistently with the original full-zero identity. Then B(conjugate(z))=conjugate(B(z)). In the actual real eigenstate, a critical zero contributes j log(2+gamma)|B(gamma)|^2 to the sum in (11), and an off-line conjugate pair contributes 2j log(2+gamma)(b_z^2+c_z^2). Thus (20) retains the true sampling-square structure and every infinite internal mixed term.

The factor kappa^(-2), the additional logarithmic sampling weight, and the tail--low mixed form are still present. In particular the absolute Hermitian sum b_z^2+c_z^2 has not become the signed difference b_z^2-c_z^2. No coefficient-one comparison follows from (11)--(20) alone.
