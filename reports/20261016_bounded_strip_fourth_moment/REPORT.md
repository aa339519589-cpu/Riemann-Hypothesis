# Local zero-count moments control bounded-strip packet fourth moments

This is a derived proof-support lemma from established zero-count moment inputs.
No claim of novelty is made, and this is not a simple-zero proportion estimate. The
constant depends on a fixed normalized imaginary-height cutoff. No control
uniform in that cutoff is claimed.

## 1. Inputs and normalization

Let T tend to infinity, delta=2 pi/log T, and count all zeta zeros with
T<gamma<=2T, including multiplicity. Put

    x_rho=(gamma-T)/delta,
    y_rho=(beta-1/2)/delta,
    z_rho=x_rho+i y_rho.

Fix A<infinity and retain only zeros with |y_rho|<=A. This retains conjugate
partners under beta -> 1-beta. Let f be a fixed nonnegative bounded function
supported on [-lambda/2,lambda/2], of integral one. Define

    F_z(u)=sqrt(f(u)) exp(-2 pi i u z),
    B_T=sum_z |F_z><F_z|,
    A_T=F J F*,

where the synthesis map F includes each retained zero with its multiplicity,
and J pairs z with conjugate(z), fixing real z. Thus A_T is Hermitian and
B_T=FF* is positive.

The conclusion is

    tr(A_T^4)<=tr(B_T^4)<<_(A,f,lambda) T log T.

In particular, for this fixed-strip operator, the normalized cubic spectral
tails are uniformly integrable:

    (T log T)^(-1) sum_(|xi|>R) |xi|^3 <<_(A,f,lambda) 1/R.

The sum here is over operator eigenvalues, not zero multiplicities.

The only zeta input needed below is the fixed sixth short-interval moment

    integral_T^(2T) |S(t+h)-S(t)|^6 dt << T
    for h=4 pi/log T.

It follows from K.-M. Tsang, *Some Omega-theorems for the Riemann zeta-function*, Acta Arith.
46 (1986), no. 4, 369–395, Theorem 4, as stated in Theorem 2 of Simonic,
Trudgian, and Turnage-Butterbaugh, arXiv:2010.10675. The order is fixed at
k=3, so no moving-moment threshold is used. Riemann--von Mangoldt then
gives the same bound with S(t+h)-S(t) replaced by N(t+h)-N(t), because
the deterministic main increment is bounded on this range.

Primary accessible statement: [Simonic, Trudgian, and Turnage-Butterbaugh,
arXiv:2010.10675v1, Theorem 2](https://arxiv.org/pdf/2010.10675v1).

## 2. From continuous short intervals to discrete occupancies

Let c_j count all zeros, including multiplicity, in the half-open physical
bin [T+j delta,T+(j+1)delta), restricted to (T,2T]. The half-open convention
only avoids double counting and has no effect on the integral argument.

For almost every t in [T+(j-1)delta,T+j delta],

    N(t+2delta)-N(t)>=c_j.

These preceding bins are disjoint. Hence

    delta sum_j c_j^6
       <= integral_(T-delta)^(2T) [N(t+2delta)-N(t)]^6 dt
       << T.

The small lower-end extension is paid by the same fixed sixth-moment input
on [T/2,T]; h log(T/2) remains bounded. Consequently

    sum_j c_j^6 << T log T,
    sum_j c_j^5 << T log T.

This includes both multiplicities and clusters of distinct ordinates.
The retained fixed-strip occupancies are no larger than c_j.

## 3. Elementary uniform Bessel bound for one packet per separated bin

Consider any finite list z_l=x_l+i y_l with |y_l|<=A and real parts separated
by at least one. On the support of f,

    f(u)<=||f||_infinity exp(pi lambda^2/4) exp(-pi u^2).

The Gaussian majorant has complex-packet Gram entries

    integral_R exp(-pi u^2)
       exp(-2 pi i u [(x_k-x_l)+i(y_k+y_l)]) du
      = exp(-pi [(x_k-x_l)+i(y_k+y_l)]^2).

Their absolute values are at most

    exp(4 pi A^2) exp(-pi (x_k-x_l)^2).

Separation implies a uniform row sum bounded by

    1+2 sum_(n>=1) exp(-pi n^2).

Schur's inequality therefore bounds the synthesis norm squared, and equally
the norm of the positive packet sum, by the finite constant

    C_A = ||f||_infinity exp(pi lambda^2/4+4 pi A^2)
          [1+2 sum_(n>=1) exp(-pi n^2)].

No real-axis assumption is used here beyond real-part separation.

For at most M packets in each unit bin of normalized real parts, split into
M layers with at most one point per bin, and then split each layer into even
and odd bins. Within each parity class real parts are separated by at least
one. Summing the positive operators gives the bound 2 M C_A.

## 4. Occupancy levels and the Schatten estimate

For r>=0, let B_r contain the retained packets whose full occupancy bin
satisfies 2^r<=c_j<2^(r+1). Then

    ||B_r||_op <= 2^(r+2) C_A,
    tr B_r <= exp(2 pi lambda A) sum_(level r) c_j.

For positive finite-rank B_r,

    ||B_r||_4^4 = tr(B_r^4)
       <= ||B_r||_op^3 tr B_r
       <= C_(A,f,lambda) 2^(3r) sum_(level r) c_j
       <= C_(A,f,lambda) 2^(-r) sum_(level r) c_j^5.

Writing M5=sum_j c_j^5, the triangle inequality in Schatten class 4 yields

    ||B_T||_4 <= sum_r ||B_r||_4
       <= C_(A,f,lambda) M5^(1/4) sum_(r>=0) 2^(-r/4).

The geometric sum converges. Section 2 proves tr(B_T^4)<<T log T.

Finally, Schatten Holder applied to F J F* gives

    ||A_T||_4 <= ||F||_8 ||J||_op ||F*||_8
               = ||FF*||_4 = ||B_T||_4.

Since A_T is Hermitian, its fourth trace is its fourth Schatten norm. The
cubic-tail assertion follows from |xi|^3 1_(|xi|>R)<=|xi|^4/R.

## 5. What this does and does not settle

This excludes a bounded-strip cubic spectral escape caused solely by
uncontrolled multiplicities or close real ordinates, using an actual
short-interval zero-count input. In particular it applies to the critical-line
packet suboperator without assuming RH.

The full zero operator includes normalized imaginary parts growing with log T.
The displayed Gaussian constant grows with A, and this proof does not establish
an estimate uniform as A tends to infinity, nor a small fourth-norm remainder
outside the fixed strip. Ordinary zero density and exponential packet growth
must be compared with their actual constants before any such passage. No full
operator fourth-moment bound, simple-zero improvement, or contradiction to an
off-critical zero follows here.
