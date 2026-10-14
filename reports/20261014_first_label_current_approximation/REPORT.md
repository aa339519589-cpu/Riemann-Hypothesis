# Same-current first-label approximation in the full original forward energy

## Verified result and scope

For the SAME actual scalar source, the first hidden-label conditional mean
of its complete original-psi current is a lawful original-P comparison
source. Its error relative to the actual ratio has at most **13/400** of
the SAME current's integrated hidden bracket energy. The estimate includes
the complete Gamma kernel, every prime-power divisor, the moving posterior,
and both parts of the true refresh energy.

This is not an RH proof or a contraction of the full signed source form.
The exact signed variance transport and the complete reflected/polar graph
remain in the theorem. In particular the bracket energy below is not the
different positive safe-xi component G_tail-D_div.

## 1. Original source, complete current, and fixed conventions

Let g=psi r be an actual fixed-depth scalar source, psi=-Phi' the original
positive odd-theta source on x>0, and 0<delta<=1/3. The existing actual
ratio theorem gives r=c_infinity+u with bounded u in every H^sigma,
1/2<sigma<1, tending to zero. Its exact endpoint identity is
c_infinity=U(g)/U(psi), U(f)=int exp(x/2)f(x)dx. Thus g0=psi u is the
same lawful null representative and lies in ker Q_delta. It need not be
pole-centered; its changed pole moment is always retained.

Use

    kappa(h)=exp(-h/2)/(1-exp(-2h)), alpha_d=Lambda(d)/sqrt(d),
    K=3Phi+Theta/2, m=psi^2,
    G f(x)=int_0^infinity kappa(h)psi(x+h)/psi(x)[f(x)-f(x+h)]dh
              +sum_(d>=2)alpha_d psi(x+log d)/psi(x)
                                      [f(x)-f(x+log d)].

Positive generator means the Markov semigroup is exp(-tG). The genuine
homogeneous process and its finite complete current are established in
[the forward-ray theorem](../20261014_positive_reflected_storage/FORWARD_RAYS.md).
The honest operational entrance, global bounded current variance and its
tail limit are in
[the coherent current theorem](../20261014_coherent_prime_ray_bridges/COHERENT_OPERATIONAL_RAY_CURRENTS.md).
These are not properties of a normalized fixed-time filter.

Write

    I_x=lim int_0^t G u(X_v)dv, E I_x=u(x), Var I_x=J(x),
    F[f]=int m Gamma_G[f]=F_c[f]+F_p[f].

At zero the complete current uses operational time and retains its actual
holding interval. This does not change either the current or its carré
occupation. F has ONE future orientation; the original source form has
coefficient 2 in front of F.

The source remains the actual canonical source: on the positive wing its
honest future Mobius inverse satisfies C M g0=g0. No arbitrary latent seed,
Fourier eigen-seed, new source gauge or inverse-zeta range is substituted.
The current-adapted field below is deliberately NOT identified with the
singular canonical Mobius quotient at the wall.

## 2. The positive hidden lift and its SAME-current field

The full-band posterior is

    eta(x)=exp(x/2)(4z^2-6z)exp(-z), z=pi exp(2x),
    p_n(x)=n^(-1/2)eta(x+log n)/Phi(x), s=psi/Phi,
    T Z=sum_n p_n Z_n.

The positive full-band hidden process, its arbitrary-label intertwining,
nonexplosion and full natural-filtration posterior are proved in
[HIDDEN_LIFT.md](HIDDEN_LIFT.md), with the exact origin extension in
[ENTRANCE.md](ENTRANCE.md). The auxiliary score inequality needed for both
positivity and the divisor estimate is proved independently in
[THETA_SCORE.md](THETA_SCORE.md).

Let A_star be its physical generator. Its channels are

    continuous: kappa(h)eta(x+log n+h)/eta(x+log n) *s(x+h)/s(x),
    divisor d|n: Lambda(d)s(x+log d)/s(x),
    refresh n->j: p_j(x)a_j(x),
    a_n=beta_n-(A_eta s)_n/s>0, T a=beta_psi=K/psi.

Every true divisor death and every refresh is retained. In particular the
current-adapted field generally has NONZERO divisor squares. Put

    w(x,n)=E_(x,n) I_x, H_n=w_n-u, V=T H^2, e=w_1-u.

[CURRENT_FIELD.md](CURRENT_FIELD.md) proves the closed-martingale identity

    T w=u, 0<=V<=J,
    J=V+R_G(T Gamma_(A_star)[w]).                         (1)

Define the four nonnegative integrated components

    E_c=int m T Gamma_cont[w], E_d=int m T Gamma_div[w],
    R_a=int m T(a H^2), R_v=int m beta_psi V,
    E_current=E_c+E_d+R_a+R_v.                            (2)

This E_current is the integrated bracket of the SAME complete current.
It is neither an independent trial norm nor a separately available surplus.

## 3. Main theorem

For the actual u and w above:

1. The odd source z1=psi w_1 belongs to the ORIGINAL completed P domain.
   The same is true of psi e. No such all-label original-domain assertion
   is made for n>=2.

2. All quantities in (2) are finite, and the exact signed transport is

       E_current=int b(J-V)=F[u]-int bV,                 (3)
       b=psi[sinh(x/2)/2+2K-2x psi-H_kappa psi-F_r psi].

   Here F_r psi is the reflected-only row. The adjoint density b changes
   sign; no favorable sign is inferred from V>=0.

3. The complete original forward energy error obeys

       F[w_1-u] <= (13/400) E_current.                  (4)

   Also |w_1-u|^2<=V/400 pointwise.

4. Actual stationarity is genuinely legal:

       Q_delta(g0,z1)=0,
       Q_delta[z1]=Q_delta[psi e]
                   <=(13/200)E_current-B_delta[e].     (5)

   The complete boundary graph B_delta in (5) is defined below. It is not
   deleted or replaced by an unrelated row estimate.

### Proof and coefficient accounting

[DOMAIN.md](DOMAIN.md) proves (3), original-P closure and actual stationarity.
Its key conductance identity is

    m(x)p_n(x) rate_cont((x,n),(y,n))
                =psi(x)psi(y)kappa(y-x)p_n(y).

The uniform floor p_1>.99 therefore controls the original first-label
Gamma norm. Boundedness of w_1 pays all complete prime and polar measures;
origin flattening, theta-tail cutoff and annular logarithmic-form density
prove closure, not only a formal finite energy. The signed adjoint pairing
uses potentials dominated by J and justified cutoff-resolvent limits.

The stronger posterior estimate in [GAMMA_ERROR.md](GAMMA_ERROR.md) gives
p_1>=400/401 and the complete moving-posterior debit. For every t>0,

    F_c[e]<=(1+t)E_c/400+(1+1/t)R_v/50.                 (6)

[DIVISOR_RESET.md](DIVISOR_RESET.md) proves the exact all-prime estimate

    F_p[e]<=3 epsilon_* E_d+4 epsilon_* R_a+R_v/100,
    epsilon_*<2^(-42).                                (7)

Its rate comparison is L_n<=4a_n/3, where
L_n=sum_(d|n)Lambda(d)s(x+log d)/s(x). It follows from the complete theta
score dilation s'-2s>3 and uses every true Mangoldt divisor. The prime
increment decomposition keeps the genuine hidden divisor square as well
as the centered prelabel square; no absolute-value Mobius substitute occurs.

Take t=12 in (6). The coefficients of E_c,E_d,R_a,R_v in (6)-(7) are
13/400, 3*2^(-42), 4*2^(-42), and 19/600, all at most13/400.
This proves (4), with each reset component used exactly once. The exact
rational checks are reproduced by
[check_first_label_coefficients.py](check_first_label_coefficients.py).
Finally (5) is the full source identity and actual stationarity applied to
the now legal pair. This completes the proof.

## 4. Full signed boundary and the remaining comparison

Let sigma(x)=sinh(x/2). The ORIGINAL forms are

    H[f]=int_(x,y>0) kappa(x+y)psi(x)psi(y)|f(x)-f(y)|^2 dxdy,
    N[f]=sum_d alpha_d int_0^log d psi(x)psi(log d-x)
                                      |f(x)-f(log d-x)|^2 dx,
    P[f]=int sigma psi |f|^2-8|int sigma psi f|^2,
    B_delta[f]=H[f]+(1-delta)N[f]-P[f].

The full pole coefficient uses int sigma psi=1/8 exactly. The source identity
is Q_delta[psi f]=2F[f]-B_delta[f], as proved in
[the complete current/source identity](../20261014_positive_reflected_storage/CURRENT_FORM.md).
The recently proved
[boundary-graph coercivity](../20261014_boundary_graph_coercivity/REPORT.md)
signs B_delta itself at the stated depths, but supplies no upper comparison
against F. Thus (5) retains a genuine nonnegative boundary debit; it is not
an RH conclusion.

In particular the tempting replacement E_current<=F[u] is NOT licensed by
(3). Nor does the small full-forward error (4) assert Q_delta[z1]<=c Q_delta[g0],
preserve the original eigen-equation, or give a new independent current
storage budget. A closing estimate must still compare the complete signed
transport and boundary graph for this SAME source. No such favorable total
sign is claimed here.
