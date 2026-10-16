# Retaining the cross pole: uniform tail-window L2 of the selected ratio

Date: 2026-10-16.

This separately labeled addendum strengthens the moving-window conclusion
of the [selected-pair report](REPORT.md), without changing that report.
For the same selected pair, the ratio p=e/h itself has uniformly bounded
L2 mass on every sufficiently far unit window, including when the source
ratio e/psi has zero plateau. The proof retains the positive cross pole
in the already justified complete comparison. It uses no division by
e/psi, no signed feasible ground direction, and no new derivative passage.
The resulting bound has no explicit delta^(-1) loss.

We also prove a complete shifted-seed remainder limit. That limit has no
asserted rate and does not bound the square of the original current.

## 1. Hypotheses and the retained complete rows

Keep all hypotheses, conventions and objects of the report. In particular,

    e=psi a, Q0 e=-2delta W_psi e, 0<delta<1,
    ell(f)=integral_0^infinity sinh(x/2)f(x)dx,
    U(f)=integral_0^infinity exp(x/2)f(x)dx,
    ell(h)=1, p=e/h, q=e^2/h.

The source ratio a is bounded, globally Holder and has a finite plateau.
Ratios are zero on the common-zero set {h=e=0}; e=0 a.e. on {h=0}.
The ground h is the lawful one-sided minimum specified in the report.
In particular U(q)<infinity and integral s psi p^2<infinity, where
s=sinh(x/2). Every reflected or forward sum below includes every prime
power with alpha_n=Lambda(n)/sqrt(n).

Let v be an admissible positive neutral seed from report Section 2,
rescaled so that ell(v)=1. Its complete fixed-v reciprocal estimate,
retained-square differentiation and old actual first-slot pairing have
already been proved in report Sections 2--5. Define

    A_v=integral q Rv,
    B_v=integral v p^2 Rh,
    C_v=integral e R(vp),
    D_v=integral q V_psi v,
    J_v=ell(vp^2), m_v=ell(vp).                    (1)

All these quantities are finite, C_v is absolute, and the complete rows
are

    0<=B_v<=A_v, |C_v|<=sqrt(A_v B_v), D_v>=0,
    P_cross,v=2(A_v+B_v)-4(1-delta)C_v-4delta D_v. (2)

P_cross,v is the sum of the positive Gamma, forward-prime and pole cross
energies with edge

    (h_x v_y+v_x h_y)(p_x-p_y)^2.

Thus its pole block, with both normalized grounds retained, is exactly

    P_cross,v,pole
       =8[J_v+ell(q)-2ell(e)m_v].                  (3)

This formula also holds on common-zero sets: h p=e, h p^2=q, and no
cross term is deleted merely because one ground endpoint is zero.

## 2. A seed-uniform ratio-square bound

Dropping only nonnegative terms from the complete positive cross energy,
and using the upper bound in (2), gives

    8[J_v+ell(q)-2ell(e)m_v]
       <=P_cross,v
       <=2(A_v+B_v)+4(1-delta)sqrt(A_v B_v)
       <=4(2-delta)A_v.                            (4)

The middle inequality uses D_v>=0 and 0<delta<1, without imposing a
sign on C_v. Weighted Cauchy gives

    |m_v|<=sqrt(J_v), ell(e)^2<=ell(q),             (5)

because ell(v)=ell(h)=1. Consequently

    (sqrt(J_v)-|ell(e)|)^2
       <=(1-delta/2)A_v-ell(q)+ell(e)^2,            (6)

and in particular

    sqrt(J_v)<=|ell(e)|+sqrt((1-delta/2)A_v)
              <=|ell(e)|+sqrt(A_v).               (7)

The normalization of the seeds is essential in (3), (5), and (7).
No uniform bound on the earlier seed-by-seed proof constants is needed:
that proof establishes finiteness and (2) for each fixed seed, after which
(7) is uniform whenever A_v is uniform.

Use the report's normalized shifted-Phi seeds

    v_z(x)=2[Phi(x-z)-Phi(x+z)]/sinh(z/2).          (8)

The complete Chebyshev estimate already proved there is

    Rv_z(x)<=C exp(x/2), z>=1, x>0.                (9)

Hence A_z<=C U(q). For a sufficiently large fixed z0>1, the same
positive shifted-Phi window estimate gives

    s(x)v_z(x)>=c0>0 whenever z>=z0, |x-z|<=1.     (10)

Indeed v_z>=c exp(-z/2) there, while s(x)>=c exp(z/2).
Equations (7)--(10) prove

    sup_(z>=z0) integral_(z-1)^(z+1) |e/h|^2
       <=C (|ell(e)|+sqrt(U(q)))^2<infinity.       (11)

The seed constants C and c0 are universal fixed-theta constants; the
right side has no explicit delta^(-1) factor. No window in (11) reaches
the wall. There is no assumption that a's plateau is nonzero, and no
division by a near its zeros. Since q/psi=a p,

    sup_(z>=z0) integral_(z-1)^(z+1) |q/psi|^2
       <=||a||_infinity^2 sup_(z>=z0)
                        integral_(z-1)^(z+1)|p|^2. (12)

If a(x)->0, the window integrals in (12) tend to zero. This improves the
report's earlier statement about what its L1 estimate alone could imply;
the improvement uses the additional retained cross pole, not a division
of that L1 estimate by a.

## 3. The full shifted-seed remainder

Write w=W_psi e=W_psi g. The original actual-ratio and complete PNT
conclusions give

    |w(x)|<=C exp(x/2),
    exp(-x/2)w(x)->0 as x->infinity.               (13)

For completeness, the second limit uses the actual plateau equation
lim a=U(e)/U(psi), together with
Rpsi/exp(x/2)->U(psi) and Re/exp(x/2)->U(e).
These are the full prime-power statements, not a prime-only replacement.
The original actual current is bounded on every compact wall collar.

Symmetry of the complete R pairing in (1) gives the exact absolute row

    C_z-D_z=-integral v_z p w.                    (14)

We now show its limit is zero, without a rate. By (11) and Cauchy, the
L1 masses of |p| in unit intervals contained in [1,infinity) are uniformly
bounded. The finitely many remaining intervals before the far-tail
threshold are paid by integral s psi p^2, since s psi is bounded below
on every compact away from zero.

Set k(t)=exp(t/2)Phi(t). Its unit-bin suprema are summable over all
integers, by the two theta tails. Positivity and monotonicity of Phi
in (8) give, uniformly for z>=1 and x>0,

    exp(x/2)v_z(x)<=C k(x-z).                     (15)

Indeed Phi(x+z)<=Phi(x-z), and 1/sinh(z/2)<=C exp(-z/2).
The translation-bounded L1 mass of |p| and the summable bin envelope
therefore imply

    sup_(z>=1) integral_1^infinity |p(x)|k(x-z)dx
       <infinity.                                (16)

Put epsilon(x)=exp(-x/2)w(x). For x>=M, (13), (15), and (16) bound the
absolute tail in (14) by C sup_(x>=M)|epsilon(x)|. On each fixed interval
[1,M], the kernel in (15) tends uniformly to zero as z->infinity, and
p is integrable there.

The wall must be treated separately; ordinary wall L1 of p is not used.
Since s(x)psi(x) is comparable to x^2 near zero, the already paid
reciprocal budget implies integral_0^1 x|p(x)|dx<infinity. Smooth oddness
of (8) and the theta tails give

    sup_(0<x<=1) v_z(x)/x ->0.

Together with bounded w on that collar, this pays the wall part of (14).
Taking first z->infinity on the compact pieces and then M->infinity
proves

    C_z-D_z->0.                                   (17)

This proof uses only the selected-ratio budget and the already known
normalized little-o in (13). It supplies no improved decay rate for w.

## 4. Exact tail consequences and limitations

The full smooth-seed PNT gives, for each fixed x>0,

    Rv_z(x)->2 exp(x/2).                           (18)

To check the normalization, put y=x+z in the first branch of (8).
Then

    exp(-y/2) sum_(d_n>x) alpha_n Phi(d_n-y)
       ->integral_R exp(t/2)Phi(t)dt=1/2.

The factor 2/sinh(z/2) is asymptotic to 4 exp(-z/2).
The second shifted-Phi branch tends to zero by the complete Chebyshev
bound and the theta tail. The sum includes all proper powers throughout.
By (9), U(q)<infinity and dominated convergence,

    A_z->2U(q).                                   (19)

Rewriting (2), without discarding its remainder, gives

    0<=P_cross,z
       =2(A_z+B_z)-4D_z-4(1-delta)(C_z-D_z).

Using B_z<=A_z, (17), and (19), we obtain

    limsup_(z->infinity) D_z<=2U(q).               (20)

If the source plateau is zero, then also D_z->0 and C_z->0. Indeed
D_z=integral L v_z a p, L<=C exp(x/2), and (15)--(16) pay its tail with
the extra factor sup_(x>=M)|a(x)|->0. On a fixed compact, including the
wall, write D_z=integral q L(v_z/psi): q is integrable, L is bounded,
and v_z/psi tends uniformly to zero there. Finally use (17).

The new result is a far-tail L2 bound for the selected changed-ground
ratio, including the zero-source-plateau case. It does not give ordinary
wall L2 of e/h, a pointwise lower bound for h, a feasible negative ground
variation, a reverse signed IMS estimate, or an all-epsilon bound on the
original current W_psi g. In particular (17) and (20) are limits of
complete linear pairings, not estimates of integral exp(-epsilon x)|w|^2.
The original RH comparison remains open.
