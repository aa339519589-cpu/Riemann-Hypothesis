# The complete parent-six arithmetic residual in the true variance metric

The exact affine label cancellation makes the whole projected arithmetic
residual small in the SAME conditional-variance metric as the principal.
Unlike a generic incoming-row estimate, this proof keeps the child
posterior inside its two-endpoint operator coefficient. It spends only
the existing score energy of the same orthogonal residual.

Dependencies: [the finite prime-cancellation theorem](../20261014_coupled_source_profile_square/FINITE_PROJECTION.md),
[the exact variance metric](../20261014_coupled_source_profile_square/TRUE_VARIANCE_METRIC.md),
and [the projected signed storage](../20261014_coupled_source_profile_square/STORAGE.md).
The finite-mask arithmetic theorem and its full limit are used without
removing any union-boundary branch.

## 1. Same residual and same metric

For the finite or full profile a=1-mu_N, let

    m=T a, sigma^2=Var_p(a),
    w-u=A(a-m)+Z, T Z=T(aZ)=0,
    E_a[Z]=int psi^2 sum_m p_m c_m |Z_m|^2 dx.

The exact projected equation has arithmetic residual

    I_Z(x)=sum_(p prime)r_p(x)sum_(m>=3)p_m(y)j_p(m)Z_m(y),
    y=x+log p,
    j_p(m)=a(pm)-a(p)-[a(2p)-a(p)]a(m)/2.

For every finite mask and for the full mask, j_p(1)=j_p(2)=0 and
|j_p(m)|<=1. At finite N the complete coefficient is zero for p>N;
all other cutoff branches remain inside j_p. The first possible initial
label is pm=6. All prime powers of exponent>=2 have already canceled
EXACTLY in this residual; they remain in the actual diagonal and source
forcing, not in I_Z.

We prove the uniform complete estimate

    int psi^2 |I_Z|^2/(beta sigma^2) dx
                              <=2^(-112) E_a[Z].    (1)

Both bounds are strict for positive E_a; at zero input both sides are
zero. Equivalently, the associated operator norms are strictly bounded
by the displayed constants.

This is not an estimate in an auxiliary unweighted Gaussian norm.
The left side is precisely the dual of the beta-weighted projection
variance D_beta=int psi^2 beta sigma^2 |A|^2.

## 2. Exact original-coordinate operator coefficient

For each m define

    f_m(y)=psi(y)sqrt[p_m(y)c_m(y)] Z_m(y),
    sum_m ||f_m||_L2(dy)^2=E_a[Z].

Since r_p=alpha_p psi(y)/psi(x), the map from f_m to
psi(x)I_Z(x)/(sigma(x)sqrt(beta(x))) has the exact future-shift coefficient

    C_(p,m)(x)=alpha_p j_p(m)sqrt[p_m(y)]
                         /[sigma(x)sqrt(beta(x)c_m(y))].     (2)

There is no Jacobian cost: y=x+log p is a translation in the original
x coordinate. The shift restricted to y>=log p is an L2 contraction.
In particular no backward Chebyshev row has been separated in (2).

The complete theta/score bounds are

 sigma^2(x)>=4p_1(x)p_2(x)>=64(400/401)^2 exp(-3z),
 beta(x)>3/s(x)>24/(17z),
 c_m(y)>3log2>2, m>=3,
 p_m(y)<=2m^4 exp[-(m^2-1)p^2z], z=pi exp(2x)>3.    (3)

The variance lower bound is the single positive label1/label2 pair in
the exact variance sum. All other labels remain; none is used with a
negative sign. Inserting (3) into (2) gives

 |C_(p,m)(x)|
   <=[401/(3200)]m^2(log p)/sqrt(p) sqrt(17z/24)
                    exp[-E_(p,m)z/2],
 E_(p,m)=(m^2-1)p^2-3>=29.                         (4)

The function sqrt(z)exp(-E z/2) decreases for z>=3. Also
sqrt(17/8)<3/2, (401/3200)(3/2)<1/5, and log p<=p.
Consequently the complete coefficient supremum is bounded by

    sup_x |C_(p,m)(x)|
       <(1/5)m^2sqrt(p)exp[-3((m^2-1)p^2-3)/2].     (5)

The actual true-prime expression is unchanged; allowing every integer
p>=2 below is only an upper bound.

## 3. Complete double tail, not a finite computation

At (p,m)=(2,3), the majorant (5) is less than

    3exp(-87/2)<3/20^14,

using exp3>20. Increasing m by1 multiplies its majorant by at most
2exp(-42)<1/2. Increasing p by1 multiplies it by at most
2exp(-60)<1/2. Therefore

    sum_(p>=2,m>=3) sup_x |C_(p,m)(x)|
                            <12/20^14<2^(-56).      (6)

For finite sums, Minkowski and the shift contraction give

 ||psi I_Z/(sigma sqrt(beta))||_2
    <=sum_(p,m) sup|C_(p,m)| ||f_m||_2
    <=[sum_(p,m) sup|C_(p,m)|] sqrt(E_a[Z]).

The absolutely convergent operator series (6) passes the full prime,
label and finite-mask boundary limits. Squaring proves (1). This
argument retains the SAME residual field at both endpoints, rather than
replacing its incoming posterior by an independent scalar row.

## 4. Alignment with the reset residual, with one expenditure

For this combined corollary restrict finite masks to N>=3, as required
by the residual forward theorem; the full infinite mask is also allowed.
The independent estimate (1)-(6) remains valid for every N>=2.
The complete reset residual is r=-T[c(a-m)Z]. The
[complete reset-principal proof](RESET_DUAL.md)
gives its sharp same-metric estimate

    int psi^2 |r|^2/(beta sigma^2)<=E_a[Z]/2800.

Combining it with (1) uses a single Young inequality, not two allocations:

 int psi^2 |r+I_Z|^2/(beta sigma^2)
   <=(101/100)(E_a/2800)+101*2^(-112)E_a
   <=E_a/2750.                                    (7)

The bound (7) is the single grouped reset/prime expenditure used by
[FEEDBACK_SQUARE.md](FEEDBACK_SQUARE.md). No older alternative Young
allocation is added to it. The original source-gradient, Gamma wall,
reflected-prime and pole terms remain in their complete signed identities.
