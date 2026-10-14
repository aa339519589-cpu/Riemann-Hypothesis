# An exact coercive correction equation for the actual first-label current

## Result and scope

The actual first-label error admits an exact positive factorization in a
larger, explicitly paid metric. The complete second-label refresh term
becomes positive killing, and all remaining labels stay in a controlled
signed forcing. An exponential conjugation supplies a genuine uniformly
coercive Gamma operator with its half-line boundary retained.

This is an extension of
[the original first-label approximation theorem](../20261014_first_label_current_approximation/REPORT.md),
not a proof of RH, K<=1, or positivity of the complete original source form.
The source, posterior, complete current, prime powers and original pole
are unchanged. In particular no generic inverse estimate in the original
psi-squared metric is assumed.

## 1. Same actual fields and the signed equation

Let u be the bounded plateau-zero ratio of an actual scalar source, and
let w(x,n) be the full-band eta conditional mean of its complete original
current. Put

    T w=u, H_n=w_n-u, V=T H^2, e=w_1-u,
    p_n=n^(-1/2)eta(x+log n)/Phi(x), s=psi/Phi,
    S1=psi p_1=eta s, beta=(3Phi+Theta/2)/psi,
    a_n=beta_n-(A_eta s)_n/s>0, T a=beta.

The published first-label theorem proves that psi e is in the ORIGINAL P
domain and gives F[e]<=13E_current/400. Here F is the one-orientation full
Gamma/prime forward energy, while E_current is the SAME integrated hidden
current bracket, including all divisors and both refresh-square components.
It is not a safe-xi common-seed norm.

[KILLED_EQUATION.md](KILLED_EQUATION.md) proves the exact first-refresh equation

    (G1+beta)e=D u+T(aH),
    D=G_prime,psi-G_extra,
    G1 f=int kappa(h)S1(x+h)/S1(x)[f(x)-f(x+h)]dh.

The extra continuous measure is positive but enters D with a MINUS sign.
The honest operational origin, its holding current and competing refresh
hazard remain. [GLOBAL_LABEL_CONTROL.md](GLOBAL_LABEL_CONTROL.md) proves
all-label logarithmic control and the Gaussian actual variance/error tails
used in the changed-metric domain proof.

## 2. Positive second-label killing and the full residual

[SECOND_LABEL_COMPLETION.md](SECOND_LABEL_COMPLETION.md) proves, with every
true divisor and full theta tail retained,

    kappa2=p_1(a_2-a_1)>828/401>2,
    T(aH)=-kappa2 e+R3,
    R3=sum_(n>=3)p_n(a_n-a_2)H_n,
    |R3|^2/beta<=B3(z)T(a|H|^2),
    B3(z)=(324+5832z)exp(-8z)+1680z exp(-15z)<1/200000,
    z=pi exp(2x).

Consequently (G1+beta+kappa2)e=f2 with f2=D u+R3. This is an exact signed
completion, not a bound obtained by deleting the label2 contribution.
[RESET_FORCING.md](RESET_FORCING.md) and [DRIFT_MISMATCH.md](DRIFT_MISMATCH.md)
retain the original full forcing and the stronger pointwise exponential
envelopes needed when its metric changes.

## 3. Exact uniformly coercive factorization

Set a=1/4 and

    q(z)=(4z^2-6z)s(x),
    g_a(z)=exp[a(z-pi)]q(z)e(x),
    Lambda_a=a_1+beta+kappa2+(1/2)log(1+a),
    G_a f=(1/2)int_0^infinity exp[-(1+a)v]
                                         [f(z)-f(z+v)]dv/v,
    m_a=psi^2 p_1^2 sqrt(z/pi)exp[(5/2)(z-pi)].

[COERCIVE_INVERSE.md](COERCIVE_INVERSE.md) proves the exact equation

    (G_a+Lambda_a)g_a=exp[a(z-pi)]q f2

on the genuine half-line L2 domain. The potential exceeds
828/401+(1/2)log(5/4). The Gamma real quadratic form is the sum of its
nonnegative future-difference square and the positive boundary term
E1((5/4)(z-pi))/4. With c0=1/(2pi exp(2pi)), the full identity is

    int m_a |f2|^2/Lambda_a
      =int m_a Lambda_a|e|^2
          +2c0 Re<g_a,G_a g_a>
          +int m_a |f2-Lambda_a e|^2/Lambda_a.

Every term on the right is nonnegative. Variable Lambda_a introduces no
missing derivative: the weighted-square cross term is exactly
2c0 Re<g_a,G_a g_a>. The original e is not forced to vanish at the wall;
its positive gauge q vanishes there, and the original entrance equation
is retained before conjugation.

Most importantly the enlarged metric is paid by the SAME original source
energies. Put R_a=int psi^2 T(a|H|^2). Then

    int m_a |f2|^2/Lambda_a
      <=[sqrt((3/80){F_prime[u]+F_Gamma[u]/400})
                                     +sqrt(R_a/200000)]^2.

The exponential envelope, not an unweighted bound, is multiplied by the
new metric before taking its supremum. This estimate and the previous
13/400 theorem are alternative uses of overlapping energy resources, not
independent gains to be added.

## 4. Original boundary, pole and P-error remain explicit

[BOUNDARY_ERROR.md](BOUNDARY_ERROR.md) proves for the same e and
R_v=int psi K V that

    0<=B_delta[e]<=2R_v/125, N[e]<=R_v/250,
    B_delta=H+(1-delta)N-P_pole, 0<=delta<=1/3.

[ORIGINAL_P_ERROR.md](ORIGINAL_P_ERROR.md) retains the complete pole variance
and proves

    P_pole[e]<=R_v/70000,
    P_original[psi e]<=4551E_current/70000.

At positive depth the lawful common-neutral projection has N cost at most
R_v/250 and delta-weighted cost at most R_v/750. These are the same error
and reset budgets; they do not create extra variance spending.

The full original comparison still contains

    Q_delta[psi u]=2F[u]-B_delta[u],
    F[u]=E_current+int bV,
    b=psi[sinh(x/2)/2+2K-2x psi-H_kappa psi-F_r psi].

The density b changes sign. None of the above replaces its signed pairing
by a favorable one or removes the full boundary graph. Obtaining the
necessary joint original-form comparison remains open.

## 5. Reproduction and dependencies

Run `python check_correction_coefficients.py` for the exact rational
coefficient, envelope-monotonicity and pole-error checks used here. The
script is supplementary; the analytic operator/domain proofs are complete
in the linked files. No numerical point sampling or finite-prime surrogate
is used to assert a full tail.

The package depends on the published first-label/current construction,
[the Gaussian future intertwining](../20261014_future_gamma_prime_semigroup/FOUNDATIONAL_INTERTWINING.md),
[the complete forward rays](../20261014_positive_reflected_storage/FORWARD_RAYS.md),
[their operational entrance](../20261014_coherent_prime_ray_bridges/COHERENT_OPERATIONAL_RAY_CURRENTS.md),
and [the signed boundary graph](../20261014_boundary_graph_coercivity/REPORT.md).
