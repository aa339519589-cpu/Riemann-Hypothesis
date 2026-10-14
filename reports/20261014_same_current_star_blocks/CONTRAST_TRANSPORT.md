# The same conditional-variance transport and its signed contrast block

This note keeps the exact current variance V in the original adjoint
pairing. Subtracting the legal first-label field inside the genuine hidden
current produces a finite cross block containing ALL prime/Gamma mismatch
channels. Its original-metric Cauchy bound is constructive but has a stated
direction: it is not an upper estimate for E_current by F and not a proof
of the full original signed form.

## 1. Same fields and finite energies

Let u, w, V and v=w_1 be the actual fields in the published first-label
current theorem. Put

    e=v-u, Delta_n=w_n-v, H_n=w_n-u,
    T Delta=-e, T Delta^2=V+e^2,
    F[f]=int psi^2 Gamma_G[f],
    E_Delta=int psi^2 T Gamma_A[Delta],
    R_a=int psi^2 T[a H^2], R_v=int psi K V.

All fields are real for simplicity; real polarization gives the complex
version. The hidden lift of a label-independent field v has exactly
T Gamma_A[v]=Gamma_G[v]. Therefore E_Delta is finite, bounded by
2E_current+2F[v], and includes the COMPLETE true-divisor squares. Its refresh
part is exactly R_a+R_v, since subtracting the same v from every label does
not change any refresh difference.

Use the exact original adjoint density

    b=G^*(psi^2)
      =psi[sinh(x/2)/2+2K-2x psi-H_kappa psi-F_r psi].          (1)

It has its genuine signed value, with int |b|(V+e^2) finite by the proved
bounded current/ratio estimates and complete theta rows.

## 2. A finite full mismatch covariance

Let G_n be the continuous label-n generator, L_n its full divisor rate,
and qdiff_n=q_1-q_n. The exact mass identity and true-divisor bound are

    M_n=int qdiff_n=L_n-a_n+a_1, 0<M_n<L_n,
    L_n<=4a_n/3, n>=2.                                      (2)

Define a finite-kernel source contrast

    F_n^0(x)=sum_(d|n)r_d(x)[v(x+log d)-v(x)]
                    -int qdiff_n(x,dy)[v(y)-v(x)],
    F_1^0=0.                                                (3)

Both channel measures in (3) are positive, but their RELATIVE MINUS sign
is retained. They are not an absolute prime norm surrogate. Put

    C=-int psi^2 sum_(n>=2)p_n H_n F_n^0.                    (4)

On a smooth localized core (4) is precisely
int psi^2 Cov_p(Delta,A v), because
(A v)_n-(A v)_1=-F_n^0 and T H=0. Formula (4), not a separately divergent
G_n v drift, defines it for the actual current field.

The entire mismatch square is bounded in the SAME source energy:

    |C|^2 <= (8/3)R_a {F_prime[v]+F_extra[v]},
    F_extra[v]<=F_Gamma[v]/400.                              (5)

To prove it, Cauchy on the UNION of the two measures in (3) gives

    |F_n^0|^2/a_n
      <=(L_n+M_n)/a_n
           {sum_(d|n)r_d |v(x+log d)-v(x)|^2
                         +int qdiff_n |v(y)-v(x)|^2}
      <=(8/3){the same complete positive bracket}.

Averaging uses the exact full identities

    T[true-divisor bracket]=Gamma_prime,psi[v],
    sum_n p_n qdiff_n=q_1-sum_n p_n q_n=q_extra.

The last measure is the original extra first-label Gamma measure, with
p_1(y)/p_1(x)-1<=1/400. A second weighted Cauchy in labels and x, using
R_a, proves (5) and absolute integrability of (4). No fixed-label original-P
claim is made for n>=2.

## 3. Exact signed transport block

The complete current drift is A w=G u, independent of the label. Thus

    T[Delta A Delta]=e G e-Cov_p(Delta,A v).

The hidden product identity, intertwining and (1) give EXACTLY

    E_Delta=F[e]-int b V-2C.                                 (6)

Here is a safe form-level interpretation. First replace v by bounded-ratio
original-P core approximations and use finite Gamma/label cutoffs jointly.
The common-current equation is applied in its full extended martingale
sense; it is not replaced by a false vanishing cutoff source equation.
The mismatch covariance is passed through its finite representation (4)
and the bound (5). The hidden cross energies converge by Cauchy using
E_current and F[v]; the label-independent squares converge in the original
P form. The bounded-ratio/theta cutoffs pay b(V+e^2). This identifies the
limiting integrated product identity without separating a backward-prime
row or assuming a classical G_1 v drift.

For comparison, polarization gives the equally exact identity

    E_hidden(v,Delta)=-F(v,e)+C.

Together with E_hidden[w]=F[u]-int bV, this verifies every factor in (6).
It is the SAME V as the current field and the initial-star covariance,
not a surrogate edgewise variance.

## 4. A signed Schur estimate and its precise direction

Let F_mis=F_prime[v]+F_extra[v]. Equation (5) gives the genuine positive
2-by-2 Schur block, or equivalently for every t>0,

    2|C|<=t R_a+(8/(3t))F_mis.                              (7)

Since E_Delta contains its entire refresh part R_a+R_v, (6)-(7) imply

    int bV <=F[e]+(8/3)F_mis-R_v,                            (8)

by taking t=1. Thus the complete signed transport has an upper bound which
retains a negative R_v term. It does not assert int bV>=0 or int bV<=0.
In particular (8) gives

    F[u]<=E_current-R_v+F[e]+(8/3)F_mis,

which is a LOWER-control direction for E_current, not the sought upper
comparison E_current<=constant*F[u]. Claiming the opposite direction would
be a sign error. The reset channel in (7) is the same R_a already present in
E_current, and cannot be spent independently again.

The full signed kernel F_n^0 remains the comparison target beyond (8).
Positivity of the individual current or reset operators does not imply a
favorable completion. The original boundary graph, pole, and any common-neutral
forcing remain outside this component estimate.
