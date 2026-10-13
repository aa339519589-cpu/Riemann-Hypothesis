# Exact-Q Green load at subprincipal order

Mathematical derivation, 2026-10-13; independently reviewed. This uses the
[projected frame](PROJECTED_FRAME.md), the [full-tail trial](../20261013_growing_theta_trial/LAGUERRE_SCHUR_TRIAL.md), and the
[complete collar reconstruction](../20261013_collar_subprincipal/SUBPRINCIPAL_FORM.md). No Schur-sign or RH claim is made.

Fix d and the exact old spaces E_k,Q_k of [PROJECTED_FRAME.md](PROJECTED_FRAME.md). Let M_k be the closed restriction
of the actual old odd source form to Q_k, Y_k=Q_k B_k the true
collar-to-Q block, and D_k the true new-collar diagonal. For M_k>=0 set

    G_k(y)=sup_v in Dom(M_k form)
               [2 Re<v,Y_k y>-M_k[v]] in [0,infinity].

Here Q_k is the orthogonal complement of E_k in the whole old odd window,
and the new space is the entire odd collar. The restriction M_k is a closed
form on Q_k; its domain is the intersection of Q_k with the old form domain.
The off-diagonal Y_k is the bounded old/new source block followed by Q_k.
These are the actual blocks of the polar-inclusive source form, with the
sharp domain split supplied by [SHARP_WINDOW_DOMAIN.md](../20261012_localized_odd_schur/SHARP_WINDOW_DOMAIN.md).

This is the squared positive-form Green dual norm, with infinity when
appropriate; it does not impose an L2 norm cap on v. Its signed short is
D_k[y]-G_k(y). Define explicitly the baseline quotient, for L=log k,

    eta_k^Q = sup_(0!=y in Dom(D_k form)) G_k(y)/(L||y||²).

Thus for each such nonzero y,

    eta_k^Q >= G_k(y)/(L||y||²).                       (1)

Any larger joint quotient whose beta=0 slice contains all these y is at
least eta_k^Q. The theorem below concerns eta_k^Q itself and needs no
unpublished definition of the larger joint quotient.

## A Q-admissible trial and exact quadratic comparison

Take any fixed nonzero complex W in C_c^infinity(0,pi) and the actual
collar vector y_k=f0(x)W(pi exp(2x)-pi k)/sigma_k with odd reflection.
Use the exact-Q projected growing frame with m=floor((log k)^(1/4)).
Its profile approximates the Laguerre polynomial P_m on the entire tail
with the same weighted H1 error k^-1 exp(C_(d,A)m²log(m+2)), and its
pointwise envelope has subpower growth. Thus every Gamma, full signed
prime-power and polar estimate of the full-tail trial applies unchanged.
With the mandatory scale G_source,k=F_k/sigma_k, the resulting vector
v_k=chi_k G_source,k belongs to Q_k exactly and obeys

    q_(A_(k+1))[v_k+y_k]=epsilon_k(W), epsilon_k(W)->0. (2)

For clarity, with the realized profile Pcal_k, the exact residual profile
has the decomposition

    eta_cut,k Pcal_k-W0
        =eta_cut,k(Pcal_k-P_m)+(eta_cut,k P_m-W0).

The rescaled cutoff has derivative O(1), and W0 vanishes on its transition.
Consequently the weighted H1_24 profile errors are
O(m^-r+k^(-1+o(1))) in value and
O(m^(1-r)+k^(-1+o(1))) in derivative for every fixed r>2.
In particular L times the squared value error tends to zero. The pointwise
polynomial envelope is absorbed in exp(C_d m²log(m+2))=k^o(1), so every
prime-power and polar contribution also tends to zero as in the full trial.

This part needs no old positivity: it is an actual finite source-null
trial identity. It uses only finite combinations for each k and the
proved growing-dimensional estimates, not a fixed-degree limit.

By the exact block form and v_k in Q_k,

    q_(A_(k+1))[v_k+y_k]
       =M_k[v_k]+2 Re<v_k,Y_k y_k>+D_k[y_k].

The dual supremum can be tested at -v_k. Hence, whenever M_k>=0,

    G_k(y_k)>=-2 Re<v_k,Y_k y_k>-M_k[v_k]
             =D_k[y_k]-epsilon_k(W).                 (3)

If G_k(y_k) is infinite, (3) and the conclusions below remain valid.
No inverse or positive spectral gap of M_k is needed.

## The actual cell limit supplies the constant term

Use the unitary collar coordinates of [SUBPRINCIPAL_FORM.md](../20261013_collar_subprincipal/SUBPRINCIPAL_FORM.md). With

    a=.5log k, h=.5log(1+1/k),
    g_k(u)=sqrt(2h) y_k(a+hu),
    C=B_cell-(gamma+log pi)I,

the exact theta asymptotic and smooth W give convergence in C1([0,1])

    g_k -> g_W(u)=-sqrt(2pi)exp(-pi u)W(pi u).        (4)

Indeed pi k(exp(2hu)-1)=pi u+O(1/k) in C1, and
sqrt(2h)f0(a+hu)/sigma_k
    =-sqrt(4pi k h)exp(-pi u)(1+O_(C1)(1/k)).
All these profiles are supported in a fixed compact subinterval of
(0,1). In particular n_W=||g_W||²>0.

The [cell operator-domain lemma](../20261013_collar_subprincipal/RESOLVENT_EXPANSION.md) maps C1 profiles continuously to L2
under C. The exact bounded-perturbation reconstruction therefore gives

    D_k[y_k]-L||y_k||² -> <g_W,Cg_W>,
    ||y_k||² -> n_W.                                 (5)

Equations (1),(3),(5) imply, on every unbounded integer sequence with
M_k>=0,

    liminf L(eta_k^Q-1)
          >= <g_W,Cg_W>/||g_W||²                     (6)

for every fixed nonzero W of the specified class. Infinity is understood
in the extended-real sense. No profile degree or W-frequency grows
during this fixed-W limit.

## The right side of (6) is unbounded above

Fix nonzero phi in C_c^infinity(0,1) and phi_N(u)=exp(iNu)phi(u).
For the single positive interval of length one, [SUBPRINCIPAL_FORM.md](../20261013_collar_subprincipal/SUBPRINCIPAL_FORM.md) gives

    q_a[phi_N]=b_cell[phi_N]-(gamma+log(2pi))||phi||²
                    +e_1[phi_N],
    ||e_1||<=2C_rho.

The symbol b(t)=a(t)+C0 is nonnegative and obeys
b(t)>=.5log(1+4t²). The Fourier transform of phi_N is the transform of
phi shifted by N (up to the immaterial sign convention). On the region
whose shifted frequency has modulus at most N/2, |t|>=N/2 and
b(t)>=log N. The missing Fourier mass is O_phi(N^-2) by phi in H1.
Consequently

    q_a[phi_N]>=log N (||phi||²-O_phi(N^-2))-C0||phi||²,
    <phi_N,Cphi_N>/||phi||² >= log N-O_phi(1).        (7)

Each phi_N is g_(W_N) for the fixed smooth compact profile

    W_N(s)=-(2pi)^(-1/2)exp(s)phi(s/pi)exp(iNs/pi).

For any chosen A choose one fixed N making (7)>A, then use the fixed-W_N
limit (6). This order of quantifiers proves

    liminf_(k->infinity, M_k>=0)
           log(k)(eta_k^Q-1)=+infinity,           (8)

whenever the set of qualifying endpoints is unbounded. In particular
eta_k^Q>1 at every sufficiently large qualifying endpoint. This
strengthens the earlier leading-order obstruction liminf eta>=1; it
does not claim eta itself tends to infinity or stays uniformly above
1 by a positive constant.

## Why (8) does not determine the true Schur sign

The denominator in (1) is only L||y||². The actual new diagonal also
contains the generally unbounded cell subprincipal operator C, and
(3) says that the Green load can reproduce that term as well. The
true signed short is D_k[y]-G_k(y), for which this construction gives
only an upper bound epsilon_k(W)->0. It gives no lower bound and can
be compatible with a positive short approaching zero.

The finite-pivot, mixed-row and target changes in the complete joint
Schur problem must still be controlled together. No full-window
positivity, original even weighted spectral gap improvement, new
zero exclusion or RH proof follows from this quotient obstruction.
