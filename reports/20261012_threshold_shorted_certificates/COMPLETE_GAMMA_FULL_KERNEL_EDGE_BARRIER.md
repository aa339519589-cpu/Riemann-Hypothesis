# Complete Gamma and whole-kernel prime-edge shorting: a multi-evaluation obstruction

For the original even operator H and its complete positive prime-edge form e, let Z be any complex-linear subspace of the entire actual ker H. The lower comparison

    L_Z[v]=H[v]-inf_(z in Z)e[v-z]

has infinitely many negative directions on the ground-perpendicular domain, even when Z is the whole true kernel and the complete Gamma form is retained. On the height-G division-source span, the proof constructs at least N(G)-O(G log log G) such directions, where N(G) is the number of simple positive critical-line zeros up to G. Every constructed nonzero vector has strictly positive ORIGINAL H energy.

The new ingredient is a common O(G log log G)-dimensional approximation to the actual two-prime current columns, with a superpolynomially small error paid in their true weighted Hilbert norm. The count N(G) is of order G log G. Keeping the required square-root-of-N column-error factor then produces a small-current coefficient subspace. This is compatible with the nonvanishing individual evaluation costs in the earlier theorem.

The conclusion concerns this particular lower comparison and exact kernel-only edge restoration. It neither constructs a negative H vector nor rules out corrections using nonkernel directions, positive-depth certificates, or the exact signed-prime formulation. The original spectral gap and all zero-exclusion questions are unchanged.

## Original normalization and complete dependencies

Use the user's [original closed-form foundation](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a99fbcda6b496eb36811ed80f3bfe5b18b7e2585/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md), on complex even L2(R,dx). In the Fourier convention fhat(t)=integral f(x)exp(-itx)dx with Plancherel measure dt/(2pi),

    b(t)=Re psi(1/4+it/2)-psi(1/4),
    B is the operator of the closed form b[mv],
    V=C0 m^2+sum_(n>=2) alpha_n m(tau_(log n)+tau_(-log n))m,
    C0=-psi(1/4)+log pi,  H=B-V,  D(H)=D(B).

The actual theta multiplier, full prime-edge form and original ground are specified in Section 1. Section 2 gives precise fixed public proof locations for the genuine division-source vectors, all-kernel evaluation identity, and the actual two-prime currents. Sections 3–6 prove the new common approximation and complex-coefficient transfer without assuming a classification of ker H. Section 7 also gives the finite-rank correction requirement. The [independent review](REFEREE_COMPLETE_GAMMA_FULL_KERNEL_EDGE_BARRIER.md) checks the complete proof and original-domain dependencies.

## 1. Objects and conclusion

Work in the unchanged original even L2(dx) space. Let H=B-V be the original selfadjoint operator, with its complete Gamma form B and bounded complete prime operator V. Retain

 m(x)=sqrt(Phi(x)/(2cosh(x/2))),
 g0(x)=2cosh(x/2)m(x),
 F_v(gamma)=integral m(x)v(x)cos(gamma x)dx.

The original positive ground vector satisfies H g0=-g0/2. The exact bounded complete prime-edge form is

 e[v]=sum_(n>=2)alpha_n integral m(x)m(x+log n)
                                  |v(x+log n)-v(x)|^2 dx,
 alpha_n=Lambda(n)/sqrt(n).

Write E for its positive bounded operator, with 0<=E<=18I. No truncation of E occurs in the comparison below. The two summands e_2 and e_3 are used only to construct upper bounds on dual evaluation costs; e_2+e_3<=e.

Let Z be any complex-linear subspace of the actual ker H, including Z=ker H. Define

 r_Z[v]=inf_(z in Z)e[v-z],
 L_Z[v]=H[v]-r_Z[v],                  v in D(B^(1/2)).       (1)

If Z is not closed, this infimum has the same value after closing E^(1/2)Z in the energy image. More explicitly, if Pi_Z is the orthogonal projection onto that closed image,

 r_Z[v]=|| (I-Pi_Z) E^(1/2)v ||^2.

Thus r_Z is a bounded positive quadratic form, and L_Z is the closed semibounded form obtained by subtracting a bounded positive operator from H. This is exactly the complete-Gamma diagonal comparison H-E after exact prime-edge shorting on Z, with no scalar penalty.

**Theorem.** For every such Z, the form L_Z has infinite negative index, even on the ground-perpendicular space. More precisely, for sufficiently large G, let N(G) be the number of distinct simple critical-line zeros with positive height at most G. There is an original-domain subspace of dimension

 N(G)-O(G log log G)

on which H is strictly positive and L_Z is strictly negative. The estimate is uniform in the choice of Z inside ker H.

The argument uses many evaluations together. It does not assert that an individual pure-edge evaluation norm tends to zero; that assertion is false for the previously established family. An almost-dependent collection of dual current columns supplies the new ingredient.

## 2. Established source and current inputs

We state the exact prior inputs and their proof locations so that the new finite-rank argument does not depend on a classification of ker H.

First, the genuine division-source construction for every simple positive real zero gamma of Xi gives an even w_gamma in D(H) with

 <g0,w_gamma>=0,
 H w_gamma=2m cos(gamma x),
 F_(w_gamma)(gamma')=1 if gamma'=gamma and 0 at every other
                    distinct simple positive real zero gamma'.       (2)

Consequently, for any finite selection gamma_1,...,gamma_N,

 <w_(gamma_i),H w_(gamma_j)>=2 delta_ij.                       (3)

Selfadjointness also gives, for every vector z in the full actual ker H,

 F_z(gamma_j)=0.                                              (4)

These are the original-domain statements proved in Appendices C and D of [Fixed finite-Gamma full-kernel barrier](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a5cc93ac213383d36980fe258fe251a3b67370cc/reports/20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md). That construction controls division-source tails, puts w_gamma in the original operator domain, and evaluates the complete explicit formula. It requires simplicity only at the selected gamma_j. It assumes neither that all zeros lie on the critical line nor that known theta vectors exhaust ker H.

Second, retain the actual prime-2 and prime-3 currents from [Pure prime-edge evaluations](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/44001ff94f5dd298acd132a00a173f3b143d6cc5/reports/20261012_adaptive_spectral_tail/PURE_PRIME_EDGE_EVALUATIONS.md). The following formulas and bounds from that proof will be used.

Put d=log 2, a=log 3 and

 c_gamma=(integral m(x)cos(gamma x)dx)/(integral g0(x)dx),
 q_gamma(x)=m(x)cos(gamma x)-c_gamma g0(x),
 B_gamma=18(exp(|gamma|/6)+1),
 Q(t)=14exp(5t/2)exp[-(pi/2)exp(2t)],
 mu(t)=3exp(2t-(pi/2)exp(2t)).

Then |c_gamma|<=1/2, integral q_gamma=0, m<=2, and

 |q_gamma(x)|<=Q(|x|),
 m(x)>=mu(S) for |x|<=S.                                  (5)

The periodization h_gamma(s)=sum_(k in Z)q_gamma(s+kd) has mean zero. The real periodic solution

 j_gamma(s-a)-j_gamma(s)=h_gamma(s),
 (j_gamma)_0=0

has Fourier coefficients satisfying

 |(j_gamma)_k|<=(B_gamma/2)exp(-|k|/4),   k!=0.              (6)

This estimate follows from the proved zero-free theta strip of width 1/6 and the elementary log 2/log 3 small-divisor bound. There is no unproved Diophantine assumption.

Set

 J_(3,gamma)(x)=j_gamma(x)1_[0,d)(x),
 q_(3,gamma)(x)=J_(3,gamma)(x-a)-J_(3,gamma)(x),
 r_gamma=q_gamma-q_(3,gamma).

The d-periodization of r_gamma vanishes and the original prime-2 current is

 J_(2,gamma)(x)=sum_(k>=1)r_gamma(x+kd)
              =-sum_(k<=0)r_gamma(x+kd).                  (7)

The pointwise current divergence is q_gamma. Weighted integration by parts gives, for every original even v in L2,

 F_v(gamma)-c_gamma<g0,v>
   =sum_(n=2,3) integral J_(n,gamma)(x)
                               [v(x+log n)-v(x)]dx.       (8)

All currents in (8) are real vectors in the following complex Hilbert space:

 Y=L2(dx/[alpha_2 m(x)m(x+d)])
                         direct_sum L2(dx/[alpha_3 m(x)m(x+a)]).       (9)

For J=(J2,J3), Cauchy--Schwarz in (8) bounds the square of the functional by ||J||_Y^2 e[v]. This also applies to any finite complex linear combination of the actual currents. The original form e is retained on the right.

## 3. A split lift with separate uniform real tails

Define a linear split lift on the sources in question by

 (S q)(x)=sum_(k>=1)q(x+kd),       x>=0,
 (S q)(x)=-sum_(k<=0)q(x+kd),      x<0.                    (10)

The branch switch is intentional. Every source argument moves toward the corresponding real tail. We do not assume that S q is analytic across zero. Since r_gamma has zero periodization, both expressions in (7) agree, and hence the exact current can be written

 J_gamma=(S q_gamma,0)+A j_gamma,
 A j=(-S q3,J3),
 J3=j 1_[0,d), q3=J3(.-a)-J3.                            (11)

Each term on the right belongs separately to Y. Indeed, for x<0 all arguments in S q3 are negative, whereas q3 is supported in [0,d] union [a,a+d]. For x>=a all forward arguments exceed a+d. Thus S q3 is supported in [0,a]. A one-sided sum contains at most two nonzero terms, so

 ||A j||_Y<=6 ||j||_infinity/mu(2).                       (12)

For detail, the first component has support length below 2, pointwise size at most 2||j||_infinity, alpha_2>1/4, and both weighted endpoints lie in [0,2]. Its squared norm is at most 32||j||_infinity^2/mu(2)^2. The second has support length below 1, alpha_3>1/2 and endpoints in [0,2], giving at most 2||j||_infinity^2/mu(2)^2. The sum is below the square of the right side of (12).

For S q_gamma the far-tail estimates from (5), the geometric ratio Q(t+d)/Q(t)<1/2 for t>=d, and the real lower bound on m give, uniformly in real gamma,

 |S q_gamma(x)|^2/[alpha_2 m(x)m(x+d)]
   <=2800 exp(x) exp[-(9/2)exp(2x)],             x>=3,
   <=1400 exp(-x) exp[-(9/8)exp(-2x)],           x<=-3.    (13)

These are the same paid real-tail estimates as in the current construction. Integration yields, for R>=3,

 ||1_(|x|>R) S q_gamma||_(Y_2)^2
                 <=5000 exp[-exp(2R)].                   (14)

In particular the exponentially growing upper bound B_gamma from the complex-strip proof does not enter this real spatial truncation. The possibly large low Fourier coefficients of j_gamma are kept as independent finite-rank features below, not multiplied by a spatial tail error.

## 4. A common low-dimensional approximation to all currents up to height G

Fix G>=exp(4), and choose

 R=log log G+3, Y0=R+3,
 K=ceil(4G), M=ceil(8G Y0),
 D_R=sqrt(8R)/mu(R+d), A_Y=2Y0/d+2.                      (15)

Let j_(gamma,K) retain the Fourier modes 1<=|k|<=K of j_gamma. By (6), for 0<=gamma<=G,

 ||j_gamma-j_(gamma,K)||_infinity
  <=4 B_gamma exp(-K/4)
  <=144 exp(-5G/6).                                      (16)

The collection A j_(gamma,K) lies in one complex subspace of Y of dimension at most 2K. Its mode amplitudes may be arbitrarily large; the approximation retains them exactly.

On the source side, let P_M(t) be the degree-M Taylor polynomial of cos t at zero, including zero odd coefficients. For real |t|<=G Y0, the integral Taylor remainder and (M+1)!>=((M+1)/e)^(M+1) give

 |cos t-P_M(t)|<=[e GY0/(M+1)]^(M+1)
                                 <=2^(-(M+1)).           (17)

Here M+1>=8GY0 and e<3. Keeping the scalar ground correction exact, put

 p_gamma(y)=m(y)P_M(gamma y)-c_gamma g0(y).

Define S_(Y0) by the same half-axis formulas as S, but retaining only terms whose source argument y satisfies |y|<=Y0. This is a finite sum at every x. Set

 J_tilde_gamma=(1_[-R,R] S_(Y0)p_gamma,0)
                                      +A j_(gamma,K).    (18)

This is an actual vector in Y; every polynomial-source term is supported in the compact x interval [-R,R]. The common feature space in (18) is spanned by

 (1_[-R,R]S_(Y0)[m(y)y^l],0),        0<=l<=M,
 (1_[-R,R]S_(Y0)g0,0),
 A cos(2pi k x/d), A sin(2pi k x/d), 1<=k<=K.

Its dimension D(G) is therefore at most

 D(G)<=M+2+2K=O(G log log G).                             (19)

There is no analyticity assumption at the branch switch x=0: the Taylor approximation is in the source factor cos(gamma y), and S_(Y0) is applied afterward as a fixed linear map. All branch and support discontinuities are retained in the feature vectors.

We now pay the approximation error in the true weighted Hilbert norm. On [-R,R], both endpoints x,x+d lie in [-R-d,R+d], and alpha_2>1/4. Hence

 ||u||_(Y_2)<=D_R ||u||_infinity
                  for u supported in [-R,R].            (20)

The omitted source arguments in S-S_(Y0) lie beyond Y0 on one real half-axis. The Q-ratio used in (13) therefore gives

 ||(S-S_(Y0))q_gamma||_(L_infinity[-R,R])<=2Q(Y0).         (21)

There are at most A_Y retained arguments. Since m<=2 and the ground term was retained exactly, (17) gives

 ||S_(Y0)(q_gamma-p_gamma)||_(L_infinity[-R,R])
                              <=2 A_Y 2^(-(M+1)).        (22)

Combining (12), (14), (16), and (20)-(22), one has the explicit uniform estimate

 sup_(0<=gamma<=G)||J_gamma-J_tilde_gamma||_Y<=delta(G),
 delta(G)=sqrt(5000) exp[-exp(2R)/2]
          +2D_R Q(Y0)
          +2D_R A_Y 2^(-(M+1))
          +(864/mu(2)) exp(-5G/6).                        (23)

Every object in this finite-rank approximation is built from the original theta source, actual two-prime weights, and the established circle solution. It does not involve P, a choice of basis in an unknown spectral space, or a kernel classification.

For later use, (15) and (23) imply, for every fixed p>0,

 delta(G)=o(G^(-p)).                                      (24)

Here is the complete growth check. Write L=log G. Then exp(2R)=exp(6)L^2, exp(2Y0)=exp(12)L^2, and exp(2(R+d))=4exp(6)L^2. Thus the first term of (23) is exp[-c_1 L^2]. Also

 log D_R=(pi/2)exp(2(R+d))+O(R+log R),
 log Q(Y0)=-(pi/2)exp(2Y0)+O(Y0).

Since exp(12)>4exp(6), their product in the second term has logarithm -c_2 L^2+O(log L), with c_2>0. For the third term, log(D_R A_Y)=O(L^2), whereas (M+1)log 2 is of order G log log G and dominates L^2. The last term is exponentially small in G. These four facts prove (24), without interchanging G-dependent spatial, Fourier, or coefficient limits.

## 5. Many simple critical zeros force a small-current coefficient space

Let gamma_1,...,gamma_N be all distinct simple positive critical-line zeros with gamma_j<=G. We use only the unconditional quantitative statements

 c G log G<=N=N(G)<=C G log G                            (25)

for all sufficiently large G, with some positive constants c,C. Both inputs may be read in J. B. Conrey, “More than two fifths of the zeros of the Riemann zeta function are on the critical line,” Journal fuer die reine und angewandte Mathematik 399 (1989), 1–26 ([primary paper PDF](https://aimath.org/~kaur/publications/24.pdf)). Page 3, equation (8), states the total zero count; equation (11) defines N_0^* as the simple critical-line zero count; page 4, Theorem 1, gives its lower asymptotic proportion at least 0.401. These statements imply (25). No claim that these zeros exhaust all zeros is used.

Define complex-linear maps from C^N to Y,

 T_G c=sum_(j=1)^N c_j J_(gamma_j),
 T_tilde_G c=sum_(j=1)^N c_j J_tilde_(gamma_j).

The second map has rank at most D(G). Set C_G=ker T_tilde_G. Then

 dim C_G>=N-D(G),
 ||T_G c||_Y<=sqrt(N)delta(G)||c||_2,     c in C_G.         (26)

This is precisely where the number of columns enters: sum|c_j|<=sqrt(N)||c||_2. It is not enough to bound the error of each column by a fixed small number.

By (19), (24), and (25),

 D(G)=o(N(G)), epsilon_G:=N(G)delta(G)^2 ->0.              (27)

Thus for all sufficiently large G, epsilon_G<1/4, N-D(G) tends to infinity, and on the whole coefficient subspace C_G,

 ||T_G c||_Y^2<=epsilon_G ||c||_2^2.                      (28)

This gives a small Gram form only on the kernel of the approximating column map. We do not invert the full dual Gram matrix, assert orthogonality of its columns, or infer decay of the individual diagonal entries.

## 6. Transfer to genuine original-domain negative subspaces of the comparison

For c in C_G define

 w_c=sum_(j=1)^N c_j w_(gamma_j).

Equations (2)-(3) show that w_c belongs to D(H), is ground-perpendicular, and

 H[w_c]=2||c||_2^2,
 F_(w_c)(gamma_j)=c_j.                                   (29)

In particular the map c -> w_c is injective. For any z in Z, selfadjointness gives <g0,z>=0, because z is in ker H while g0 has eigenvalue -1/2. Equation (4) gives F_z(gamma_j)=0. Therefore the linear combination of the exact current identities (8) satisfies

 sum_j conjugate(c_j) [F_(w_c-z)(gamma_j)
                         -c_(gamma_j)<g0,w_c-z>]=||c||_2^2.

The current in this test is sum_j conjugate(c_j)J_(gamma_j).
The actual current columns are real, so this vector is the complex conjugate of T_G c and has the same Y norm. Thus the bound in (28) applies to arbitrary complex c, without any conjugation-invariance assumption on Z. Cauchy--Schwarz in the actual current Hilbert space, followed by e_2+e_3<=e, yields

 ||c||_2^4<=||T_G c||_Y^2 e[w_c-z]
             <=epsilon_G ||c||_2^2 e[w_c-z].             (30)

For c!=0, take the infimum over z to obtain

 r_Z[w_c]>=||c||_2^2/epsilon_G.

If epsilon_G happens to vanish, (30) would contradict nonzero c; thus a nontrivial C_G automatically has epsilon_G>0 for this argument. In the explicit formula (23), delta(G)>0 in any event. Finally,

 L_Z[w_c]<= (2-1/epsilon_G)||c||_2^2<0,
                       0!=c in C_G, G sufficiently large.          (31)

The resulting complex subspace has dimension at least N-D(G) and is negative definite by (31). As this dimension tends to infinity, the theorem follows. Neither a quantitative lower bound for Xi'(gamma_j) nor a bound on ||w_gamma_j|| is required: each finite collection consists of genuine original-domain vectors, and the exact Gram identity (3) is the only normalization used.

## 7. Scope

This establishes an obstruction for the lower comparison obtained by dropping the complete prime-edge form and restoring it by exact shorting on any part of the true kernel, even the whole true kernel. It is stronger than the earlier fixed finite-Gamma obstruction because no Gamma truncation remains. It also explains why the nondecay of single-evaluation pure-edge constants was not the end of the multi-evaluation question.

Every negative subspace constructed above has strictly positive original H form by (29). Its negativity belongs to L_Z, so the result supplies no negative vector for H and no counterexample to RH. It does not exclude another lower comparison, a correction using nonkernel directions, a positive-depth certificate, or an argument retaining enough of the complete edge residual. The original critical sign problem remains open.

As a direct quantitative corollary, suppose a bounded finite-rank selfadjoint correction F is added to L_Z and the result is required to be nonnegative on the height-G division-source span used above. Necessarily

 rank F>=N(G)-D(G).

Otherwise its kernel intersects the negative subspace in (31) nontrivially, and the correction vanishes on that intersection. In particular, even after exact whole-kernel shorting, an extra correction of rank o(G log G) cannot make all those height-G tests nonnegative. A fixed finite-rank correction leaves infinite negative index. This is a rank requirement for that specified lower comparison, not a restriction on unrelated methods for the original H.
