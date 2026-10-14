# A genuine pole-mode witness in the true neutral complement

This note constructs a true-mass neutral-complement vector, in the source
Schur form domain, whose elementary reciprocal-Gaussian pole defect is
nonzero. It is not asserted to be a negative eigenvector. No original
Schur sign or equality of the neutral span with the full kernel is inferred.

Use the weights in [SAFE_SOURCE_ISOMORPHISM.md](SAFE_SOURCE_ISOMORPHISM.md)
and [the closed source Schur form](../20261014_original_seed_schur/CLOSED_OPERATOR.md).
Put B(x)=exp(x/2-pi exp(2x)); the primitive seed is
xi=-(partial_x^3-partial_x/4)B. Thus b=log2, m=W xi on (b,infinity), and

    K=closure_(L2(m dx)) span{1, xi^(2j)/xi-4^(-j): j>=1}.

The reciprocal identity with its elementary defect is independently
recorded in [the complement transform note](RECIPROCAL_IDENTITY.md).

## 1. A self-Fourier function equal to one on a prescribed interval

Fix a physical radius R>2. Let F denote the unitary full-line Fourier
transform with kernel exp(-2pi i uv), and let P_R be restriction to
[-R,R] followed by zero extension. Work on the real even subspace of
L2([-R,R]); there F is a selfadjoint involution before compression. Put

    T=P_R F P_R.

T is compact, selfadjoint, and ||T||<1. Compactness follows from its
bounded kernel on the finite square. For strictness, if ||T||=1,
compactness and selfadjointness give a nonzero u with ||Tu||=||u||.
Equality in the projection contraction then says F u is supported in
[-R,R], while u is also supported there. Since a compactly supported L2
function is L1, its Fourier transform extends to an entire function. Its
vanishing on the open real complement of [-R,R] forces u=0, a
contradiction.

Consequently the following objects are well-defined:

    u=(I+T)^(-1)1_[-R,R],
    H=(I+F)u.                                          (1)

They are real and even, H belongs to L2(R), and F H=H. On (-R,R),
H=u+Tu=1 almost everywhere. The equation u=1-Tu also gives a smooth,
bounded representative on that interval: T maps compactly supported L2
functions to smooth functions with all real derivatives locally bounded.
After zero extension u is bounded and compactly supported. Thus F u is
bounded and tends to zero at infinity. In particular H is bounded on the
whole line and H(v)->0 as |v|->infinity. Values at the two endpoints are
irrelevant to every statement below.

## 2. The true-mass witness and its exact elementary defect

Set

    G(v)=1-H(v),
    f_R(x)=exp(x/2)G(exp x)/W(x), x>b.                 (2)

Here G is even, bounded, zero on (-R,R), and tends to one at infinity.
There is no division at the degenerate endpoint b, since f_R vanishes on
(b,log R). The exact mass change of variables is

    ||f_R||_m^2
      =integral_2^infinity [xi(log v)/W(log v)] |G(v)|^2 dv <infinity. (3)

The finite endpoint gap and the Gaussian tail of xi/W prove (3).
This witness does NOT belong to the ordinary physical L2 range, since
G(v)->1.

For every real t put rho=exp(2t), and define the honest Gaussian pairing

    H_B(t)=integral_b^infinity f_R(x)W(x)B(x+t)dx
          =rho^(1/4) integral_0^infinity G(v)exp(-pi rho v^2)dv.

All derivatives converge by boundedness of G and Gaussian domination.
Since G=1-H,

    H_B(t)=(1/2)exp(-t/2)-J_H(t),
    J_H(t)=rho^(1/4)integral_0^infinity H(v)exp(-pi rho v^2)dv. (4)

The self-Fourier property F H=H and Plancherel give J_H(t)=J_H(-t).
Indeed the full Fourier transform of exp(-pi rho v^2) is
rho^(-1/2)exp(-pi v^2/rho), and the even half-line pairing is half the
full-line pairing. Therefore

    H_B(t)-H_B(-t)=-sinh(t/2),
    H_B'(0)=-1/4.                                    (5)

Thus the reciprocal defect is exactly C=-1. No small-rho continuation or
unproved physical L2 hypothesis has been used.

The seed identity xi=-(partial^3-partial/4)B now yields

    H_xi(t)=integral_b^infinity f_R W xi(x+t)dx
           =-(partial_t^3-partial_t/4)H_B(t).

The operator annihilates exp(-t/2), and maps the even J_H to an odd
function. Hence H_xi is odd and all H_xi^(2j)(0) vanish. These derivatives
are the genuine mass pairings with xi^(2j)/xi. It follows that

    f_R belongs to K-perp.                            (6)

In particular the defect in (5) is a real, nonzero direction of the
actual mass complement, not a merely formal obstruction.

The witness also lies in the closed Schur form domain. To see this,
xi f_R has Gaussian decay and is piecewise smooth, with at most one
bounded jump at x=log R on the safe ray. Derivatives on the smooth wings
have at most polynomial-in-exp(x) growth before the Gaussian factor:
all derivatives of F u are bounded because u has compact support.
Consequently xi f_R belongs to every local H^sigma with sigma<1/2,
and its Gaussian-weighted global norms of those orders are finite.
The complete future sum has only finitely many translated jumps on x>b,
and its remaining derivative tails converge absolutely with Gaussian
margin. Its sharp zero-supported source tail therefore has finite
L2 and logarithmic Gamma norm. This is source-form membership, not
original P membership or an actual eigen-source assertion.

