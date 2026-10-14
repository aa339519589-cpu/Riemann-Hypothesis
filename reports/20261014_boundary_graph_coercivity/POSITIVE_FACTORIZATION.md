# Exact positive factorization of the full boundary graph

Use the definitions, complete row certificates and domains of
[REPORT.md](REPORT.md). This is an exact decomposition of
B_delta=H+(1-delta)N-P. It is not a factorization of Q_delta=2F_G-B_delta.

Put beta=1-delta, 2/3<=beta<=1, R=7/10, C=(0,R), T=(R,infinity),

    v=u-c_C(u), h_C=2kappa(2R)int_C psi,
    k_beta=2beta/(2beta-1), 2<=k_beta<=4.

Let H_out denote the original Gamma-wall double integral over the complement
of C x C, and let N_CC,N_TT retain exactly the original reflected prime
edges with both endpoints in C or both in T. Define

    H_res[v]=int_(C x C)[kappa(x+y)-kappa(2R)]
                         psi(x)psi(y)|v(x)-v(y)|^2 dxdy,

    J_CT[v]=int_T psi(x)sum_(0<d_n-x<R)alpha_n psi(d_n-x)
                                |v(x)-k_beta v(d_n-x)|^2 dx.

Every sum is over ALL genuine prime powers. The cross integral is oriented
once, with x in T; no second copy is included in J_CT.

Then the complete identity is

    B_delta[u]
      =int_C psi[h_C-s-k_beta L_T]|v|^2
       +int_T psi[L_C-s]|v|^2
       +H_res[v]+H_out[v]
       +beta N_CC[v]+beta N_TT[v]
       +(2beta-1)J_CT[v]+8|int s psi v|^2.             (1)

All terms on the right are nonnegative. The certified central coefficient
is >9/50, and the tail coefficient is >1/4. In particular (1) displays the
coercive comparison as a full sum of positive terms, not as an inference
from positive diagonal rows. Its single global centering c_C is retained.

To verify (1), the central wall integral splits into h_C int_C psi|v|^2
plus H_res because int_C psi v=0. The pole contributes
-int s psi|v|^2+8|int s psi v|^2. For every complex a,b the exact identity

    2beta|a-b|^2
       =|a|^2-k_beta|b|^2+(2beta-1)|a-k_beta b|^2      (2)

follows by expanding all squares. Applying (2) to the two-oriented original
cross-reflection energy gives the two displayed diagonal rows and the
single-oriented J_CT with coefficient 2beta-1. This proves every factor
and all mixed terms in (1).

## A lawful positive boundary norm and its neutral quotient

At delta=0, the graph B_0 defines a genuine Hilbert seminorm modulo constant
ratios on its finite-energy completion. Coercivity implies that its null
space contains only constants and that a mean-zero representative is
controlled in L2(psi dx). This conclusion does not require that the original
signed source form q be positive.

The other positive form in the original exact identity is

    F[u]=2 int psi^2 Gamma_psi[u],  q[psi u]=F[u]-B_0[u]. (3)

Let S be any finite common theta-neutral source span, written in ratios,
with q(s,f)=0 for every legal f. Then

    F(s,f)=B_0(s,f), s in S.                          (4)

Thus S has the SAME Gram matrix and the SAME mixed loads in these two
positive metrics. Its finite orthogonal projections coincide, and exactly

    q[psi u]=F[u-Pi_S u]-B_0[u-Pi_S u].              (5)

Increasing neutral spans gives the common abstract neutral completion and
the corresponding two quotient norms. One must distinguish this abstract
completion from a claim that its projected representative has any additional
pointwise theta tail or lies in a specified physical source class.

The same projection statement is NOT valid with B_delta in place of B_0
without its delta N correction: the neutral Gram changes by -delta N.
Likewise (1) does not compare the two positive quotient norms in (5). That
coefficient-one comparison remains the full signed problem. The gain here
is an explicit coercive positive boundary metric, with every reflected,
Gamma-wall and polar component accounted for, in which finite bridge
covariances and their neutral Schur complements are lawful.
