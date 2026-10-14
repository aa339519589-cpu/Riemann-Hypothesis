# A strict signed square for the complete source/profile arithmetic block

This package proves a strict, coefficient-one positive factor for a
specific COMPLETE source/profile block: its Gamma and all-prime source
cross, true conditional-variance principal, and ORIGINAL signed adjoint
storage are kept together. The exact full original-boundary remainder
is unchanged and remains unsigned.

**The full original coefficient-one comparison, K<=1, and RH remain
unproved.** The strict square itself does not assume Q_delta>=0. Its
boundary-aligned corollary uses the stated actual mixed stationarity,
without claiming that a transformed current is again an actual null source.

## 1. Original conventions and necessary published inputs

Let z=pi exp(2x), eta=exp(x/2)(4z^2-6z)exp(-z), Phi=C eta,
psi=-Phi'>0 on x>0, and

 p_n(x)=n^(-1/2)eta(x+log n)/Phi(x), T f=sum_n p_n f_n,
 kappa(t)=exp(-t/2)/(1-exp(-2t)), alpha_d=Lambda(d)/sqrt(d),
 G f=int_0^infinity kappa(t)psi(x+t)/psi(x)[f(x)-f(x+t)]dt
      +sum_d r_d(x)[f(x)-f(x+log d)],
 r_d(x)=alpha_d psi(x+log d)/psi(x).

All displayed generators use the positive convention. Every arithmetic
sum over d includes every true prime power. Write G=G_cont+G_prime,
lambda_prime=sum_d r_d, and

 F[u]=int_(0<x<y)psi(x)psi(y)kappa(y-x)|u(x)-u(y)|^2dxdy
       +sum_d alpha_d int psi(x)psi(x+log d)|u(x)-u(x+log d)|^2dx.

This is ONE forward orientation. The original form is
Q_delta[psi u]=2F[u]-B_delta[u], where
B_delta=H+(1-delta)N-P_pole keeps the complete Gamma-wall, reflected-prime
and original negative pole. Its normalization is the published
[boundary graph](../20261014_boundary_graph_coercivity/REPORT.md).
The actual positive-depth setup has 0<delta<=1/3.

The SAME actual current-adapted field w satisfies T w=u and
A_hidden w=G u in its extended current domain. We use the published
[full hidden lift and current field](../20261014_first_label_current_approximation/REPORT.md),
[global label control](../20261014_first_label_coercive_correction/GLOBAL_LABEL_CONTROL.md),
[bounded-mask original domains](../20261014_centered_mobius_profile/BOUNDED_MASK_DOMAIN.md),
and [centered projection and its complete residual cross](../20261014_centered_mobius_profile/REPORT.md).
The actual plateau-zero ratio is not replaced by a canonical Mobius seed.
The operational holding current at the origin is retained.

The genuine refresh scores are called c_n here, to distinguish them from
the arithmetic mask. They satisfy beta=T c=(3Phi+Theta/2)/psi. The hidden
energy E_full is int psi^2 T Gamma_hidden, and E_sp is its continuous-plus-
divisor part. Thus E_sp(Uu,Uu)=F[u]; the hidden bilinear is obtained by
polarization with this normalization. [RESET_FACTS.md](RESET_FACTS.md)
records the exact finite-mask reset facts and the needed source domain.

## 2. Arithmetic projection and true variance metric

Take a(n)=1-mu_ar(n), or a_N(n)=1-mu_ar(n)1_(n<=N), N>=3. Put

 m=T a, sigma^2=Var_p(a), H=w-u=A(a-m)+Z,
 T Z=T(aZ)=0, h=sigma^2 A,
 kappa_a=T[c(a-m)^2]/sigma^2,
 lambda_0=beta+kappa_a+23/200.

[FINITE_PROJECTION.md](FINITE_PROJECTION.md) proves the exact principal

 P_a h=G_cont h+lambda_prime h+kappa_a h
             +sum_(p prime)r_p theta_p(x+log p)h(x+log p),
 0<=theta_p<=1.

The PLUS prime sign remains. Every higher prime power has zero off-site
covariance, but remains on the complete diagonal and in the source
forcing. Finite square-collision and cutoff-union terms are kept exactly.
The actual equation is

 P_a h=-S_a(u)+r+I_Z,
 S_a(u)=-Gamma_cont(m,u)
          +sum_d r_d[T_y a(dm)-m(x)][u(x)-u(y)], y=x+log d,
 r=-T[c(a-m)Z], I_Z=sum_d r_d T_y[a(dm)Z_m(y)].

[TRUE_VARIANCE_METRIC.md](TRUE_VARIANCE_METRIC.md) proves, for
F_A(z)=psi(x)sigma(x)A(x)/sqrt(2z),

 I[A]:=int psi^2 A P_a(sigma^2 A)
   >=D_(3/2)[F_A]+int psi^2 lambda_0 sigma^2 A^2
                         +(199/120000)int psi^2 sigma^2 A^2.

The exact transformed Gamma form D_(3/2) includes its positive E_1/4
half-line boundary. The complete theta metric, bounded continuous defect,
all-prime dilation norm and actual logarithmic GENERATOR domain are
proved, including zero extension and the Carleman endpoint argument.
For general form amplitudes I has its closed sectorial-form meaning.

[STORAGE.md](STORAGE.md) identifies this same principal with the original
signed current density b=G^*(psi^2):

 2I[A]=E_full[D]+int b sigma^2 A^2,
 b=psi[sinh(x/2)/2+2(3Phi+Theta/2)-2x psi-H_kappa psi-L].

No positive part is substituted for b, and no separately divergent
backward prime row is split out.

## 3. Complete source contraction and the exact positive square

[SOURCE_CONTRACTION.md](SOURCE_CONTRACTION.md) proves

 ||S_a(u)||_*^2:=int psi^2 |S_a(u)|^2/(lambda_0 sigma^2)
                         <=(124633/125000)F[u].

It uses the genuine [prime 2 Gamma routing](PRIME_TWO_ROUTING.md),
F_2<=11F_Gamma/4, then the complete higher-prime source row. It does NOT
claim the false unrestricted complete-prime/Gamma comparison. The
continuous/profile and prime 2 mixed forcing is paid with one budget.

The product rule gives int psi^2 A S_a(u)=E_sp(Uu,D). Define

 C[u,A]=F[u]+2E_sp(Uu,D)+I[A].

[COUPLED_SQUARE.md](COUPLED_SQUARE.md) proves the exact completion and
therefore the strict factor

 C[u,A] >= (367/125000)F[u]+D_(3/2)[F_A]
          +(199/120000)int psi^2 sigma^2 A^2
          +int psi^2 lambda_0 sigma^2
                        |A+S_a(u)/(lambda_0 sigma^2)|^2.

This is a finite-family quadratic inequality on the stated common
profile/form domain. It includes the ORIGINAL signed storage through
2I=E_full[D]+int b Var(D). It is not an independent second copy of the
previous centered spatial/boundary energy.

## 4. Unchanged original remainder and actual boundary alignment

The full original relation is exactly

 Q_delta[psi u]=2C[u,A]-R_delta[u,A],
 R_delta=B_delta[u]+4E_sp(Uu,D)+E_full[D]+int b sigma^2 A^2.

No sign or upper domination for R_delta is proved. At the actual current,
C=F[u]-I[A]+2int psi^2 A(r+I_Z); the residual is not set to zero.
The complete Z energy, its spatial/boundary cross and all original
reflections and pole remain part of the full comparison.

The lawful mixed stationarity with psi*mA also rewrites the SAME positive
left side as

 F[u]+2F_m(u,A)-B_delta(u,mA)+2J_a(u,A)
                        +(E_full[D]+int b sigma^2 A^2)/2,
 F_m(u,A)=int_forward K m(y)Delta u Delta A,
 J_a(u,A)=sum_d int K_d[T_y a(dm)-m(y)]A(x)Delta u.

Every prime power remains in J_a. This exact mixed original-boundary
alignment does not pay the diagonal B_delta[u] or the whole residual.
No quadratic original-P membership of psi*A is asserted or needed.

## 5. Reproducibility and scope of the certificate

Run with Python3, and mpmath for the directed routing checker:

 python check_finite_projection.py
 python check_true_variance_metric.py
 python check_source_contraction.py
 python check_coupled_square.py
 python check_prime2_gamma_routing.py

The finite arithmetic checker verifies 68,750 exact affine cases and
rational covariance/union identities; the accompanying proof handles all
integers and finite masks. The other short checkers use exact fractions.
The routing checker regenerates 10,000 moment cells and6,000 source cells
with55-digit directed interval arithmetic and complete analytic tails.
It prints the regenerated directed certificate as JSON; generated output is
not part of the publication whitelist.
No sampled eigenvalue or finite-label experiment substitutes for a proof.

Only necessary projected/reset facts are included. Optional sharp
parent-six feedback bounds, different character operators and unrelated
canonical-seed statements are not additional expenditures in this square.
