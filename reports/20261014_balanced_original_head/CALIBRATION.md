# Two exact head loads balanced against the hidden endpoint and constant

This construction uses the actual source's global neutral orthogonalities,
not extra conditions imposed on its head. It gives two independent head
functionals whose tail pullbacks vanish at the degenerate safe-ray endpoint
and annihilate the hidden constant. It does not by itself prove an original
head gap or control the full head/tail remainder.

## 1. Fix the neutral convention and actual gauge

Put b=log 2 and use precisely

    t_j=psi^(2j)-4^(-j)psi, j=1,2,3.

These are centered original neutral sources: h(t_j,z)=0 for every legal
common source z. For j>=2 they are NOT the individual powers
(partial^2-1/4)^j psi, though the two finite families span the same space.

Define the complete global neutral load

    n_j(x)=2{L(x)t_j(x)/psi(x)-F_r t_j(x)},
    F_r u(x)=sum_(log d>x)alpha_d u(log d-x).            (1)

Thus N(f,t_j)=integral_0^infinity conjugate(f)n_j. The equality is used on
the common actual/theta source class, with all original prime powers.
On the head 0<=x<=b, both sides extend continuously to the endpoints. Since
Wpsi=0, the constant theta subtraction cancels exactly:

    psi n_j=2{L psi^(2j)-psi F_r psi^(2j)}.             (2)

Let g=psi r be an actual centered positive-depth top source. Use the
PLATEAU representative

    f=g-c_infinity psi, c_infinity=U_g/U_psi,
    U_u=integral_0^infinity exp(x/2)u(x)dx.

Then U_f=0, N(f,t_j)=0, and Q_delta(f,.)=0. The equality defining
c_infinity is the proved actual pointwise plateau identity. This is not the
r(0) anchor in general. Its changed pole remains in the original form, and
no two-zero-moment prime-origin law is transferred to it.

## 2. Exact endpoint and tail-constant calibration

Write

    u(x)=exp(x/2), beta_j=integral_b^infinity psi n_j,
    beta_U=integral_b^infinity psi u,
    A=[[n_2(b), n_3(b)],[beta_2,beta_3]].

The accompanying interval certificate proves

    det A in [4773295124.153197,4773295124.153244]>0.    (3)

Define the coefficients EXACTLY by

    (a_2,a_3)^T=-A^(-1)(sqrt(2),beta_U)^T,
    (c_2,c_3)^T=-A^(-1)(n_1(b),beta_1)^T,              (4)

and the two full load functions by

    l_U=u+a_2 n_2+a_3 n_3,
    l_1=n_1+c_2 n_2+c_3 n_3,
    l_V=(5/787)l_1.                                   (5)

Rounded coefficients do not define the loads; (4) does. The rigorous
coefficient intervals are in the certificate. For orientation only,

    (a_2,a_3) approximately (-4.15372e-6,1.11842e-7),
    (c_2,c_3) approximately (-.00426227,3.14921e-5).

Both calibration conditions hold exactly for either load:

    l_U(b)=l_V(b)=0,
    integral_b^infinity psi l_U
      =integral_b^infinity psi l_V=0.                 (6)

For the actual plateau source f, the global constraints in Section 1 give

    integral_0^b l_i f=-integral_b^infinity l_i f,
                                        i=U,V.        (7)

The head loads in (7) are not individually set to zero.

## 3. Why the two calibrated head functions are independent

On the head, the four functions u,n_1,n_2,n_3 are linearly independent. Here
is an analytic argument, not a determinant inferred from sampled values.
The complete head rows in (1) have the fixed-tail analytic continuation to
all real x<b; the ratio psi^(2j)/psi is removable at x=0 by oddness, and
psi has no other real zero. This is continuation of the fixed all-prime
row on this interval, NOT continuation through the changing positive-wing
cutoffs beyond b.

Let x tend to minus infinity and Z=pi exp(-2x). The first true prime row
d=2 dominates all later rows exponentially. The theta polynomial ladder
and evenness of psi^(2j)/psi give

    psi^(2j)(x)/psi(x)=4^j Z^(2j)(1+O(1/Z)),
    psi^(2j)(b-x)/psi(b-x)=4^j 16^j Z^(2j)(1+O(1/Z)).

Consequently

    n_j(x)=2alpha_2 psi(b-x)4^j(1-16^j)Z^(2j)
                                               (1+O(1/Z)). (8)

The omitted complete prime/theta rows have strictly stronger Gaussian
exponents. In a linear relation involving u and the n_j, the u term must
first vanish because it has only exponential decay in x, while all n_j
have the common double-exponential scale in (8). The largest remaining j
then has a nonzero highest polynomial degree in Z and cannot cancel. Thus
all coefficients vanish. Real analytic uniqueness transfers this conclusion
to every open head subinterval.

Now l_U has u coefficient one and l_V has n_1 coefficient 5/787, so their
independence follows. There is also an exact useful distinction:

    integral_0^b psi l_U=U_psi>0,
    integral_0^b psi l_V=0.                           (9)

Indeed N(psi,t_j)=0 globally, and the tail integrals vanish by (6). The
second load is a nonzero function despite its zero psi pairing. This proves
independence only; it does not prove that the resulting two penalties give
a numerical gap for the original head operator.

## 4. Exact tail pullback interface

On the safe ray let phi=Mf, a=phi/xi, so f=C(xi a), and define

    A_l(y)=sum_(k<=exp(y-b))k^(-1/2)l(y-log k), y>=b.

For the actual theta-decaying source, absolute future regrouping gives

    integral_b^infinity l(x)f(x)dx
        =integral_b^infinity xi(y)a(y)A_l(y)dy.       (10)

Equation (6) gives both

    A_l(y)=O(y-b) near b,
    integral_b^infinity xi A_l=0.                    (11)

The first uses local Lipschitz continuity of the complete n_j at b; each
new prime summand enters with zero source value. The second follows by
putting a=1, since Cxi=psi. Thus (10) is unchanged if a is replaced by a-c
for ANY constant c. This is the missing constant-null cancellation, not
only the endpoint cancellation.

If the complete dual norm

    C_l^2=integral_b^infinity [xi(y)/W(y)]|A_l(y)|^2dy

is bounded, then the exact Cauchy--Schwarz interface is

    |integral_0^b l f|^2
        <=C_l^2 inf_c integral_b^infinity W xi |a-c|^2. (12)

The endpoint in (12) is integrable because W~(psi'(0)/sqrt(2))(y-b) and
A_l=O(y-b). At infinity the complete prime row bound and theta polynomial
ladder give at most exponential growth of A_l, paid by xi/W. Quantitative
complete dual bounds and a head Schur certificate for these particular
balanced loads are separate steps. No separated U-tail or n_1-tail bound
is substituted for their calibrated combination.

## 5. Independent replay of the calibration

The proof data are in
the generated balanced_head_load_certificate.json,
generated by [certify_balanced_head_loads.py](certify_balanced_head_loads.py).
All arithmetic uses mpmath.iv at 50 digits and outward nextafter conversion.

The complete prime row on the head is evaluated by the exact identity

    L=exp(-x/2)sum_(k>=2)(log k)P0(pi k^2 exp(-2x))
                                              exp[-pi k^2 exp(-2x)],

and F_r psi^(j) uses P_j in that same row, with
P_(j+1)=2zP_j'+(1/2-2z)P_j and P0=8z^3-30z^2+15z.
The Gaussian derivative bounds use
M0=53, M_(j+1)=(2j+17/2)M_j. Ordinary labels beyond 16 contribute less than
10^(-220) through order 14; mirrored labels beyond 32 contribute less than
10^(-260). The checker verifies all complete tail inequalities and geometric
ratios rather than assuming a numerical cutoff.

Since N(psi,t_j)=0, beta_j=-integral_0^b psi n_j. Formula (2) makes these
smooth integrands free of an origin quotient. On each of 256 intervals,
the degree-seven midpoint Taylor integral uses derivatives 0,2,4,6 and the
whole-interval eighth-derivative error

    sup |F^(8)| * length^9/[2^8*9!].

The largest summed remainder, for j=3, is less than 5.482e-10. The endpoint
n_j(b) is evaluated by its nonsingular direct formula.

Finally the U-tail is an exact elementary theta endpoint sum:

    beta_U=2 sum_(m>=1)w_m(4w_m-5)exp(-w_m),
    w_m=4pi m^2.                                    (13)

To verify (13), integrate each xi term after w=pi m^2 exp(2x). The erfc
terms cancel in 8Gamma(7/2,w)-30Gamma(5/2,w)+15Gamma(3/2,w), leaving
2w^(3/2)(4w-5)exp(-w). The omitted m>=9 tail is less than 10^(-300), checked
by the same positive decreasing Gaussian bound. Hence (3)-(6) are rigorous
complete-row identities with outward coefficient enclosures.
