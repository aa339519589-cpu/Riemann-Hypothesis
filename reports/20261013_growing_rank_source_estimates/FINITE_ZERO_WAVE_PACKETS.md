# Finite true-zero packets: negative observation and relative far-source clipping

For a finite scalar packet supported on genuine zeros a fixed positive distance from the critical line, the complete even wave packet is controlled by its actual nonground negative spectral projection observed on a slightly larger fixed time interval. The proof keeps both conjugate phases and all true multiplicity terms. Its uniform cost is exp(C_d T^2 log^6(2+T)), with no internal zero-spacing assumption. Consequently a cutoff error supported beyond physical radius L has a relative bound with the additional factor exp(-c exp(2L)).

The construction uses the original complete theta/Gamma/prime operator throughout. It does not compare a transition at bounded physical position, remove the infinite inverse-transform remainder, or establish the signed CORE inequality. Parts I–II provide the full interpolation and spectral arguments used in Part III; their equation numbers are local to each part.

We use the original closed realization and graph core in [the adaptive source report, Sections 1 and 9](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a55c6081bc1509ef9b78829b68add21300a2a207/reports/20261012_adaptive_spectral_tail/REPORT.md). Exact zero division, the complete sesquilinear Weil pairing and its original-domain extension are given in [ZERO_INERTIA.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a55c6081bc1509ef9b78829b68add21300a2a207/reports/20261013_foundation_audit/ZERO_INERTIA.md), including the section “Check of the inherited exact zero-division construction.” Here the argument of Xi is the zeta variable s: Xi(s)=xi(s)=integral Phi(x)exp(-(s-1/2)x)dx. This differs from the height-variable notation Xi(z)=xi(1/2+iz) used in some cited reports. Inner products are conjugate-linear in the first slot.

# I. A global actual-source contour projector

## 1. Definitions

Use the original theta source Phi, m^2=Phi/(2cosh(x/2)), normalized ground e0=2m cosh(x/2), and Xi(s)=integral Phi(x)exp(-(s-1/2)x)dx. Thus Xi(1-s)=Xi(s), 2Xi(0)=1 and ||e0||=1. For even physical u in L2 set B_u(s)=integral m(x)u(x)exp(-(s-1/2)x)dx.

Let Omega be a bounded contour domain stable under conjugation and s->1-s, with no Xi zero on its boundary. S consists of ALL zeros of Xi enclosed by Omega, with their true multiplicities. Put

 R_u(s)=sum_(rho in S) PP_rho[B_u(s)/Xi(s)].

There is no polynomial part in this rational principal-parts sum. Symmetry gives R_u(1-s)=R_u(s), in particular R_u(1)=R_u(0).

Define W_pre and W_S by their source transforms:

 B_(W_pre u)(s)=Xi(s)R_u(s),
 B_(W_S u)(s)=Xi(s)[R_u(s)-R_u(0)].

These definitions have an actual physical realization below. Moreover W_S=(I-Pi_0)W_pre, where Pi_0 is the orthogonal ground projection.

## 2. Actual source contour and domain

Write lambda_z=z-1/2. For x<=0 put

 J_z(x)=integral_(-infinity)^x exp(lambda_z(x-y))Phi(y)dy;

for x>=0 put

 J_z(x)=-integral_x^infinity exp(lambda_z(x-y))Phi(y)dy.

Then the source of W_pre u is

 f_pre(x)=contour_integral_(boundary Omega) [B_u(z)/Xi(z)]J_z(x) dz/(2pi i).

The two half-line expressions fit at zero after contour integration: their discrepancy is contour_integral B_u(z)exp(lambda_z x)dz/(2pi i)=0. They also fit with all derivatives. Although the piecewise J_z alone has Laplace transform [Xi(s)-Xi(z)]/(s-z), the whole contour has transform Xi(s)R_u(s), initially checked with s outside the contour and then continued. One must not omit the piecewise correction if evaluating the contour formula for R_u at an interior point such as zero.

If |Re z-1/2|<=b on the contour, the two half-line theta-integral majorants divided by m are uniformly in L2, with bound depending only on b. Also |B_u(z)|<=C_b||u||. Thus

 ||W_pre u|| <= C_b length(boundary Omega) sup_(boundary Omega)|1/Xi| ||u||.

The ground coefficient is <e0,W_pre u>=R_u(0), since 2Xi(0)=1. Orthogonal ground subtraction consequently preserves the same norm upper bound for W_S, without introducing any distance-to-zero factor.

The first x derivative of the source costs only an additional factor 1+max|z|; f_pre and its ground-subtracted source have double-theta tails and belong to H1. The complete physical prime term is bounded, so W_S u lies in the actual D(H). This assertion keeps every original prime and both wings.

## 3. Jets and idempotence

At rho in S of multiplicity j, B_(W_Su)-B_u vanishes to order at least j. At every zero outside S, B_(W_Su) vanishes to its full multiplicity. Ground moments at s=0,1 vanish. Subtracting R_u(0) changes no principal part, and taking principal parts a second time reproduces R_u. Hence

 W_S^2=W_S.

This is a physical source interpolation projection. Its range retains all selected Laurent/division jets, including the null directions supplied by multiple zeros, and is not identified with the negative spectral subspace.

## 4. A bound independent of internal zero separation

For T>=2 choose T' in [T,T+1] at distance at least c/log(2+T) from every nearby zero ordinate. Riemann--von Mangoldt gives O(log T) zeros in a fixed-length ordinate band, so this choice is possible. Use the rectangle with vertical sides Re s=-1,2 and horizontal sides Im s=+-T'.

The vertical sides are controlled by the Euler product at Re s=2, reflection and Stirling. On the horizontal sides, normalize Xi by exp(pi T'/4) in fixed-radius disks centered at 2+-iT'. The center has a polynomial lower bound and the disk boundary has a polynomial upper bound. Jensen, removal of O(log T) Blaschke factors and Harnack give a polynomial zero-free-factor lower bound; each removed factor on the target horizontal segment is at least c'/log T. Therefore

 sup_(boundary Omega)|1/Xi| <= exp(pi T/4+C log^2(2+T)).

Absorbing the contour length and the fixed-width physical majorant,

 ||W_S|| <= exp(pi T/4+C log^2(2+T)),

and its original graph norm has the same relaxed exp(C T+C log^2 T) bound. No constant depends on the spacing of zeros inside the rectangle, and multiplicities are retained.

## 5. Exact remaining scope

The bound controls interpolation of analytic evaluation data arising from an actual physical L2 source. It is not a uniformly bounded inverse for arbitrary node values, a uniform bound for separately normalized cardinal division vectors, or a lower bound for the negative projection of a complete zero-mode combination. Such a relative clipped-probe estimate does not follow from Part I alone. The finite-packet statement is proved in Part III; the complete observable and its infinite inverse-transform remainder still require separate estimates.


# II. Negative projection on one polarized cluster

## 1. Original setting and selected contours

Use the original even self-adjoint H, its normalized ground e0 of eigenvalue -1/2, and P_- its entire nonground negative spectral projection. Let P_0 project onto ker H and P_+ onto the strictly positive spectral space. All projections are physical L2 projections. Put B_u(s)=integral m(x)u(x)exp(-(s-1/2)x)dx and Xi=B_(e0).

Fix d>0 and T>=2. Choose d_T in [d/2,d] so the vertical line Re s=1/2+d_T is at distance at least c_d/(T log(2+T)) in real part from every Xi zero with |Im s|<=T+2. The zero count is O(T log T), so such a choice exists. Choose T' in [T,T+1] whose distance to every nearby zero ordinate is at least c/log(2+T).

Use the upper-right rectangle 1/2+d_T<Re s<2, 0<Im s<T', its image under s->1-s, and their conjugates. Xi has no real zero because Phi is positive and Xi(s) is its bilateral Laplace transform. These four disjoint contours enclose ALL zeros in their interiors, with true multiplicities. Denote their union by S.

Assign phase +i on the upper-right rectangle and its reflected lower-left rectangle, and -i on their conjugates. Thus

 phase(1-s)=phase(s),
 phase(bar s)=overline{phase(s)},
 phase(s)=overline{phase(1-bar s)}.

## 2. The actual phase operator

Define

 R_A,u(s)=sum_(rho in S) phase(rho) PP_rho[B_u/Xi](s),
 B_(Au)(s)=Xi(s)[R_A,u(s)-R_A,u(0)].

The global-contour construction in Part I realizes A as an actual real even finite-rank physical operator from L2 to D(H), retaining all original primes and both wings. Its source has double-theta tails. If W is the unphased projector on these same contours, then A^2=-W, A^3=-A and Ae0=0. Rank r is at most C T log(2+T), counting all multiplicities.

The rectangle reciprocal estimate, now using the real-part avoidance above on the inner vertical sides, gives

 ||A|| <= M_T := exp(C_d T+C_d log^2(2+T)).                         (1)

A sharper coefficient pi/4 in the leading exponential is available but not needed here. There is no dependence on internal zero separation.

## 3. Original H symmetry and the eigenvectors

With the Hilbert inner product conjugate-linear in the first slot, the complete original sesquilinear zero formula on nonground sources is

 h(u,v)=sum_(all rho) j_rho overline{B_u(1-bar rho)} B_v(rho).

If either slot is A applied to a core vector, the external-zero terms vanish and only the finite S sum remains; the pole contribution vanishes because the A slot has both ground moments zero. The identity phase(rho)=overline{phase(1-bar rho)} therefore gives h(u,Av)=h(Au,v). The physical graph bound for A and core density yield

 H A=A* H on D(H).                                               (2)

For a basic zero probe psi_rho=m cosh((rho-1/2)x), the jet interpolation implies A*psi_rho=+i psi_rho or -i psi_rho, with the sign determined by the first-slot convention. Genuine division gives psi_rho in Ran H; in particular it is orthogonal to ker H. Since Ae0=0, every nonzero-phase eigenvector of A* is also orthogonal to e0.

Let V_i denote the span of the basic psi_rho carrying ONE fixed adjoint eigenvalue i. The other phase has an identical argument. This statement does not include their sum.

## 4. A finite-rank real-spectrum compression

Work on (ker H) perpendicular. Since A preserves ker H, C=A* preserves its orthogonal complement. From (2), C maps Ran H to Ran H and

 H^(-1) C=C* H^(-1)

on Ran H, with the adjoint understood on this reduced space. The image C(Ran H) is a linear subspace of the finite-dimensional Ran C and is dense there; hence it equals Ran C. Consequently Ran C is contained in D(H^(-1)). This is a finite-rank domain statement and uses no bounded inverse for H.

Set B=P_+ C P_+ on the positive spectral space. Its range is contained in D(H^(-1)), rank is at most r and ||B||<=M_T. Every nonzero eigenvector w of B belongs to that domain. The symmetry identity gives

 lambda <w,H^(-1)w> real,

while <w,H^(-1)w> is strictly positive. Therefore every nonzero eigenvalue of B is real. No quantitative positive spectral gap or negative depth is required.

Let S_B=Ran B. In the orthogonal decomposition S_B plus its perpendicular, B has the finite block B_S and an upper-right block of norm at most M_T. Since all eigenvalues of B_S are real,

 |det(iI-B_S)|>=1,
 ||iI-B_S||<=1+M_T.

The product-of-singular-values bound gives ||(iI-B_S)^(-1)||<=(1+M_T)^(r-1), with the trivial r=0 case treated separately. The complete block inverse therefore satisfies the convenient bound

 ||(iI-B)^(-1)||<=2(1+M_T)^r.                                    (3)

## 5. The polarized negative-projection lower bound

For v in V_i, write v=v_++v_- using the positive and nonground negative spectral projections; there is no ground or kernel component. From Cv=iv,

 (iI-B)v_+=P_+ C P_- v.

Equations (1)--(3) imply

 ||v_+|| <= 2M_T(1+M_T)^r ||v_-||,

and hence

 ||P_-v|| >= [1+2M_T(1+M_T)^r]^(-1)||v||
            >= exp(-C_d T^2 log^3(2+T)) ||v||.                    (4)

The deliberately relaxed last exponent is uniform across arbitrary internal collisions and true multiplicities of the selected basic modes. It is an all-rank estimate for this single polarized span, rather than a separate-point division bound.

## 6. Scope of the remaining work

The estimate does not cover V_i+V_(-i): its full division form has both signs. The additional time-frequency separation argument needed for a finite real pole packet is supplied in Part III. Nor does (4) automatically cover parameter derivatives of psi at multiple zeros; such probes can have components in ker H. The actual inverse Mellin packet contains those lower Laurent terms, so they cannot be silently discarded.

Finally, a source cutoff requires its own relative physical tail bound and its exact L or L-A buffer. Merely comparing the exponent in (4) to a nominal double-theta tail does not yet pay the forward/mixed terminal budget. No complete clipped-probe comparison or signed CORE margin is asserted.


# III. Complete finite packets and relative far-source clipping

## 1. Statement and actual packet

Use the original m, H and entire nonground negative projection P_-. When a cutoff is not even, P_- means the orthogonal projection on full physical L2 onto this even negative space. Write D_c=partial/partial c, not the original Fourier multiplier convention. Fix d>0. Let S be any finite conjugation-stable collection of actual right-hand zeta zeros rho, with Re rho-1/2>=d and |Im rho|<=T. Each occurs with no more than its true multiplicity j_rho. Write lambda_rho=rho-1/2 and take any scalar exponential polynomial

 p(c)=sum_(rho in S) exp(lambda_rho c) p_rho(c),
 deg p_rho<j_rho.

Define the original even physical wave packet

 V(c,x)=m(x)[p(c+x)+p(c-x)]/2,
 Y(c)=P_- V(c).

This is the complete scalar form of a finite pole packet: derivatives of its numerator at multiple zeros are all retained in the even-translation formula. The coefficients of p are unrestricted complex scalars. For each fixed c, the physical vector V(c) is in the original D(H): its source mV is a finite exponential polynomial times m^2, hence has H1 regularity and double-theta decay, while the complete physical prime term is bounded. Let I=[c0-1,c0+1] and I+=[c0-2,c0+2]. There are constants C_d,c>0 and an absolute finite power q (q=6 is a safe relaxation below) such that

 integral_I ||V(c)||^2 dc
 <= exp(C_d T^2 log^q(2+T)) integral_(I+) ||Y(c)||^2 dc.             (1)

For any bounded scalar cutoff whose difference from one is supported in x<-L (or in |x|>L),

 integral_I ||P_-[(phi_L-1)V(c)]||^2 dc
 <= C exp(C_d T^2 log^q(2+T)-c exp(2L))
       integral_(I+) ||Y(c)||^2 dc.                              (2)

The same bound (2) holds with V inside its left-hand cutoff expression replaced by V_one(c,x)=m(x)p(c-x). Indeed P_-V_one=Y, and the proof reconstructs the two translation legs separately. For a non-even cutoff one must not identify P_-(phi_L V_one) with P_-(phi_L V).

Constants are independent of internal zero spacing, coefficients, center c0 and all true multiplicities. They may depend on d and the bounded size of the cutoff. No assertion concerns a transition at finite x, a complete infinite contour remainder, or the signed CORE energy.

## 2. A quantitative basic-probe lower bound

The polarized-cluster argument in Part II supplies, for every selected rho,

 ||P_- psi_rho|| >= epsilon_T ||psi_rho||,
 epsilon_T=exp(-C_d T^2 log^3(2+T)),
 psi_rho(x)=m(x)cosh(lambda_rho x).

Moreover ||psi_rho|| has a uniform positive lower bound on the fixed real-part strip. Indeed |cosh((a+it)x)|^2=sinh^2(ax)+cos^2(tx), and the integral of cos^2(tx) on a fixed interval with m bounded below is uniformly positive. All fixed lambda derivatives of psi have norms uniformly bounded on a fixed real-part strip, independently of Im lambda.

## 3. Uniform observation for a finite exponential-polynomial ODE

Let y be Hilbert-space valued and solve a monic constant-coefficient ODE of order n, all characteristic roots of modulus <=T+1. Its coefficient sum is A<=(C(1+T))^n. The state Y_y=(y,y',...,y^(n-1)) obeys the companion equation Y_y'=JY_y, with ||J||<=CA.

The first n terms of the Taylor series around c have polynomial L2 norm on an interval of length delta bounded below by

 exp(-C n log(2+n)) delta^(n-1/2)||Y_y(c)||/(n-1)!.

This is the finite monomial Gram bound, valid also for Hilbert coefficients. The first row of J^n is the coefficient row of the original ODE; it is not bounded by the unnecessarily large ||J||^n. Consequently the remainder L2 norm is at most

 C A exp(CA delta) delta^(n+1/2)||Y_y(c)||/n!.

Choose delta=exp(-C' n log(2+n))/(CA). The remainder is absorbed, giving

 ||Y_y(c)|| <= exp(C n^2 log(n(T+2))) ||y||_(L2(I+))              (3)

for every c in I. At an endpoint use the inward interval; the fixed gap between I and I+ makes all intervals legal. No propagation by exp(||J||) is used.

A Riesz projector of this companion matrix separating any selected root groups on contours at distance delta_0 from all roots has norm bounded by a contour-length factor times

 (C(A+T+1))^(n-1) delta_0^(-n).

This follows directly from the determinant and adjugate. For delta_0>=c/log(2+T), it remains exp(C n^2 log(n(T+2))). Repeated roots are included.

## 4. Separate bounded-height boxes without internal spacing

Riemann--von Mangoldt gives O(log T) zeros in each fixed-length height interval, counting multiplicity. Choose horizontal cuts in successive bounded intervals avoiding all zero ordinates by c/log(2+T). This partitions S into O(T) boxes, each of bounded height and containing k<=C log(2+T) roots with multiplicity. Vertical boundaries may be chosen a fixed distance from the selected strip.

The full packet Y solves its global ODE of total order n<=CT log(2+T). Apply the global companion Riesz projector for a box. It extracts exactly Y_b=P_-V_b, including every polynomial factor. Equation (3), the projector bound and the powers needed for up to k centered derivatives control the scalar or Hilbert state of Y_b by

 exp(C T^2 log^3(2+T)) ||Y||_(L2(I+)).                            (4)

Every operation acts in the observation variable c and commutes with the fixed physical projection P_-. No positivity or individual separation within the box is assumed.

## 5. A genuine negative scalar evaluator for each box

For the distinct roots in one box, the vectors P_-psi_rho have norms at least c epsilon_T. A unit vector w_b in their finite-dimensional span can be chosen so that

 |<w_b,psi_rho>| >= epsilon_T/(C k^(3/2))=:m0

at every distinct root. A complex or real finite-dimensional sphere argument and a union bound give this deliberately relaxed estimate. In particular w_b belongs to the actual negative spectral space.

Put b_b(lambda)=<w_b,m cosh(lambda x)>. This is entire, and its first derivative is bounded uniformly on the fixed real-part strip. Around every box root take disks of radius delta<=m0/(Ck). On their union, b_b stays bounded below by m0/2. On the union boundary every root is at distance at least delta and some root is at distance delta; a harmless contour perturbation handles touching circles. The total boundary length is at most Ck delta.

Center the box in imaginary height. Its local companion J_b has bounded characteristic roots and ||J_b||<=C^k. Holomorphic functional calculus on the disk-union contour gives

 ||b_b(i gamma_b+J_b)^(-1)||
 <= exp(C k^2 log(2+k)) epsilon_T^(-Ck).                         (5)

This is a determinant/resolvent estimate; it includes confluent roots and needs no internal spacing.

If h_b(c)=<w_b,Y_b(c)>, then the exact scalar packet identity is

 h_b=b_b(D_c)p_b.

The same identity applies to the full centered state, so (5) recovers the scalar state of p_b from the observed state of h_b. Combining (4)--(5) costs at most exp(C_d T^2 log^q(2+T)) with q=6 a safe common relaxation.

## 6. Complete physical reconstruction and its theta tail

Do not use exp(||J_b|| |x|). On a fixed-radius circle outside all centered roots, the resolvent of J_b costs only exp(Ck^2). Functional calculus therefore gives

 ||exp(+-x J_b)|| <= exp(Ck^2) exp(C|x|).

The imaginary box center contributes only unit-modulus scalar factors. Thus the complete physical packet m[p_b(c+x)+p_b(c-x)]/2 has L2_x norm at most exp(Ck^2) times the recovered centered state. Its part with |x|>L has norm at most

 C exp(Ck^2-c exp(2L)) times that state,

using the original double-theta tail of m. Summing O(T) boxes only changes the relaxed exponent. Equation (1) follows, and projection contraction gives (2). All source derivatives caused by true multiplicities were included in the scalar p_b and its state; no separate jet Gram was used.

## 7. Boundary of the conclusion

The same argument is invariant under translating the center c0 and permits fixed comparable observation windows, with changed constants. It yields a relative estimate only for the indicated finite actual-zero wave packet. A complete observable still requires a paid contour remainder and a choice of T relative to the terminal scale.

In particular, the forward-prime cutoff parameter tau=log j-L reaches tau near zero. That transition lacks the exp(-c exp(2L)) tail factor in (2), so (1)--(2) do not by themselves bound that contribution by o(U) times the true activity energy. Nor may an additional physical window radius A be subtracted from L without replacing the tail exponent by its actual exp(2(L-A)). These remaining comparisons are not part of this lemma.
