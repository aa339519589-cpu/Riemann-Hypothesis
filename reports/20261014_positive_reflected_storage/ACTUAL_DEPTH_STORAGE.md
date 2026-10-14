# Positive storage for the actual supercritical comparison

Use exactly the source, reflected-only row L and full current convention in
[CURRENT_FORM.md](CURRENT_FORM.md). There is a uniform strengthened row bound

    Hpsi(x)+(1/2)L(x)-sinh(x/2)/2>1/16, x>=0.             (1)

For the analytic tail, Theorem 10 on printed p.71 of [Rosser--Schoenfeld (1962)](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf#page=8)
has the entry theta_C(X)>.91X for X>=349. Theorem12 gives Psi_C(X)<1.04X.
The same [complete Stieltjes argument and theta constants](ANALYTIC_TAIL.md) J>1, I_plus<2.93
therefore give

    L(x)/exp(x/2)>.91-.13(2.93)=5291/10000,
                                                 exp(x)>=349.

Thus the left side of (1) exceeds

    (291/20000)exp(x/2)+(1/4)exp(-x/2)>1/16

in this range: exp(x/2)>=sqrt(349)>18 and 291(18)/20000>1/16.
This uses the same directly verified primary table, not an extrapolation of
its .84/101 entry.

The new interval checker [certify_half_reflected_storage_row.py](certify_half_reflected_storage_row.py) proves (1)
on all 600 cells of width1/100 covering [0,6]. It uses the already proved
Hpsi>=(3/5)exp(-x/2), only genuine prime powers n<=1024, and the same rigorous
first-xi lower bounds and favorable moving-boundary omissions as the compact
full-L certificate. The [reproducible output](half_reflected_storage_row_certificate.json) gives a minimum interval margin greater than
0.56369057955513. Since log(349)<6, this overlaps the analytic tail.
The old full-L checker and its proof are not altered by this variant.

For 0<=delta<=1/2, put

    R_delta=Hpsi+(1-delta)L-sinh(x/2)/2,
    S_delta[u]=4int psi(K0-x psi)J_u-2delta int psi L J_u.

Because L>=0, equation (1) implies R_delta>1/16. The same exact adjoint
current identity then gives

    S_delta[u]=2int psi^2 Gamma_psi[u]+2int psi R_delta J_u
       >=2int psi^2 Gamma_psi[u]+(1/8)int psi J_u>=0.      (2)

In particular (2) applies throughout the previously proved [three-halves
Green depth](../20261013_full_prime_green_reference/THREE_HALVES_BOUND.md), where lambda<=3/2 and delta=1-1/lambda<=1/3.
No assumption about the sign of K0-x psi or its delta-adjusted pointwise
coefficient is made.

The FULL actual comparison remains

    0=Q_delta[g]=P_ray-H_ray-(1-delta)N_ray+S_delta[u].    (3)

Exactly as in the full-L case, the added product-current variance cost in
P_ray-H_ray-(1-delta)N_ray equals -2int psi R_delta J_u.
It cancels the second, now-positive term of (2) on returning to the original
unlifted forms. The signed storage theorem does not authorize spending this
quantity a second time, deleting the reflected current edge, or asserting
positivity of the entire original form.
