# A complete shared-prime subrow of the natural Möbius collar

The non-delta triangle-minus-past terms whose mask label shares a prime
with the prime-power label admit an absolute O(log^2(2N)) bound. The
entire prime-2 non-delta row admits an O(log(2N)) bound, including the
terms where the common factor comes only from the fixed outer mask.
Both orientations and every prime power are retained.

This is a bound for a specified complete subrow, not for the full
arithmetic collar. The odd-prime coprime terms and every delta term
remain. No nonnegative sign for the remaining collar, critical inverse
bound, exclusion of the actual source, or proof of RH is asserted.

## 1. Normalizations, dependencies and uniform inputs

Write mu for the Möbius function and Lambda for the von Mangoldt
function. A prime-power sum below includes n=p^k for every prime p and
every integer k>=1, with Lambda(p^k)=log p.

The original actual source is g(x)=psi(x)r_log(x), x>0. It is the same
source as in the [physical range theorem](../20261015_old_actual_physical_range/REPORT.md),
not a state in a different mass space. The original theta ground is

    B(x)=exp(x/2-pi exp(2x)),
    xi(x)=-(partial_x^3-partial_x/4)B(x),
    psi(x)=sum_(n>=1)n^(-1/2)xi(x+log n).

Use physical coordinates t=exp(x), and put

    q_0(t)=t^(-1/2)psi(log t),
    r(t)=r_log(log t), v(t)=q_0(t)r(t), t>=1.

Here q_0 denotes the physical ground, not the original quadratic form
q0. When needed, q_0 and v are zero-extended below1; no value of r below1
is used. The [actual ratio theorem](../20261014_actual_ratio_multipliers/REPORT.md)
provides ||r||_infinity<infinity. All constants may depend on this actual
source and its fixed positive depth; none is claimed uniform as that
depth tends to zero.

The ground has a polynomial-Gaussian tail. Indeed, with z=pi t^2,

    xi(log t)=sqrt(t)(8z^3-30z^2+15z)exp(-z),
    q_0(t)=sum_(n>=1)
       [8(pi n^2t^2)^3-30(pi n^2t^2)^2+15pi n^2t^2]
                                        exp(-pi n^2t^2).

Consequently |q_0(t)|<=C(1+t)^6 exp(-pi t^2) for t>=1, after increasing
C. In particular both ||q_0(t)t^s||_2 and ||q_0(t)t^(-s)||_2 over t>=1
are finite for every fixed s.

Let H be the real even physical field of the range theorem. Thus
H=Fourier(H), H is constant on the unit head, and

    H in X_s=L2(R,|u|^(2s)du), every 1/2<s<1.

For physical future dilations D_d f(u)=f(du), retain the SAME finite mask

    B0=I-5D_4+4D_16,
    M_N=sum_(m<=N)mu(m)D_m,
    P_N=B0 M_N=sum_d a_(N,d)D_d,
    F_N=P_N H,
    e_N=C F_N, C=sum_(j>=1)D_j.

Equivalently,

    a_(N,d)=mu(d)1_(d<=N)
       -5 mu(d/4)1_(4|d, d/4<=N)
       +4 mu(d/16)1_(16|d, d/16<=N).

It is useful to keep its three branches d=bm separately, with
b in {1,4,16} and (c_1,c_4,c_16)=(1,-5,4). Repeated total labels are
added linearly. This is not a fictitious two-label mask at prime2.

The positive-wing bound needed below follows directly from the range
theorem. Since ||D_d||_(X_s)=d^(-s-1/2), both C and each M_N are bounded
on X_s uniformly in N. More explicitly,

    sup_N ||e_N||_(X_s)
      <=zeta(s+1/2)^2
          [1+5*4^(-s-1/2)+4*16^(-s-1/2)]||H||_(X_s).

Thus, with the positive-half-line notation

    ||e_N||_s^2=int_1^infinity t^(2s)|e_N(t)|^2dt,

one has sup_N||e_N||_s<infinity. No ordinary unweighted critical Euler
bound, pointwise estimate of e_N, theta-relative square, or estimate for
its reciprocal field is used. The same e_N retains the FULL N mask in
every sum below; it is never replaced by a smaller-cutoff field.

The proof in Sections 3-5 is also an abstract kernel estimate: it needs
only bounded r, a polynomial-Gaussian q_0, and this uniform weighted
positive-wing L2 bound for e_N. Selfduality is used here only to identify
the actual field supplied by the range theorem, not in that estimate.

## 2. The exact triangle-minus-past contribution

For a mask label d>=1 and prime-power label n>=2, omit its scalar
coefficient a_(N,d)Lambda(n) and define

    J_N(d,n)=int_1^min(d,n)
       q_0(d/t)[r(d/t)-r(n/t)]e_N(n/t)dt/t^2
      -1_(n>d)(1/d)int_d^n
       q_0(t/d)[r(t/d)-r(n/t)]e_N(n/t)dt/t.          (1)

An empty integral is zero. Both endpoints in every ratio difference
are at least1. The first term is the complete non-delta triangle; the
second is its complete past orientation. They are not replaced by an
unsigned diagonal or by just one endpoint ordering.

For completeness, the physical parity field for any positive-wing f is

    j_P f(t)=sum_d a_(N,d)
       [f(dt)-d^(-1)f(t/d)1_(t>d)+t^(-1)f(d/t)1_(t<d)].

The physical reflected-prime operator is

    (R f)(u)=u^(-1)sum_(n>u)Lambda(n)f(n/u).

In the difference R j_P(q_0 r)-r R j_P q_0, the reflected branch of j_P,
paired against e_N and changed by t=n/u, gives the first term of (1).
The past branch gives its second term with the displayed minus sign and
1/d. The future branch is a different complete row, not part of J_N.
This calculation can first be performed with finite prime-power cutoffs
and compact integration ranges. The estimates below give absolute
limits for the subrows asserted in the theorem.

To keep the delta scope explicit, if

    ehat_N=C P_N^*H,

then the corresponding delta triangle in the same normalization is

    delta sum_(d,n) a_(N,d)Lambda(n)
       int_1^min(d,n) q_0(n/t)[r(t)-r(n/t)]
                                      ehat_N(d/t)dt/t^2.              (2)

No part of (2) is estimated in this report. In particular the field
in (2) is not assigned the theta-relative square norm of the ground.
Finite prime-power top terms and the exact delta collar remain in the
complete calculation. Paying the non-delta terms of (1) does not reduce
the coefficient of the original signed load.

## 3. A two-sided kernel estimate, including the small-ratio tail

Fix 1/2<s<1 and put a=s+1/2>1. For Q=n/d, substitution u=d/t in the
triangle and u=t/d in the past integral gives the exact identity

    J_N(d,n)=(1/d)int_(max(1,1/Q))^d
       q_0(u)[r(u)-r(Qu)]e_N(Qu)du
      -1_(Q>1)(1/d)int_1^Q
       q_0(u)[r(u)-r(Q/u)]e_N(Q/u)du/u.             (3)

The bounds on r and e_N will be included in constants. For the first
integral, weighted Cauchy and v=Qu give

    |triangle|<=C d^(-1)Q^(-s-1/2)
        (int_(max(1,1/Q))^infinity
                              |q_0(u)|^2u^(-2s)du)^(1/2).           (4)

For the past term, which exists only when Q>1, put z=Q/u. The squared
norm of the other Cauchy factor is exactly

    int_1^Q |q_0(Q/z)|^2 z^(-2s-2)dz
       =Q^(-2s-1)int_1^Q |q_0(u)|^2u^(2s)du.

Hence

    |past|<=C d^(-1)Q^(-s-1/2)||q_0(u)u^s||_2.      (5)

Define the decreasing Gaussian-tail function

    G(T)=(int_T^infinity |q_0(u)|^2u^(-2s)du)^(1/2), T>=1.

Equations (4)-(5) prove, uniformly in N,d,n,

    |J_N(d,n)|<=(C/d)K(n/d),
    K(Q)=Q^(-a)                         if Q>=1,
    K(Q)=Q^(-a)G(1/Q)                  if 0<Q<1.     (6)

Thus the estimate treats both Q tending to infinity and Q tending to
zero. A comparable Q band has not been made small by Gaussian decay.
The ground norms and the uniform positive-wing norm of e_N are the only
functional inputs. Neither the sign of mu nor a square of ehat_N is used.

## 4. The entire natural shared-prime row

Fix b in {1,4,16}. For a prime p<=N, a natural mask label divisible by p
has d=bpm, m<=N/p. The coefficient is c_b mu(pm); if it is nonzero then
p does not divide m. It is harmless to omit that restriction in an
absolute majorant.

Set A=p^(k-1)/b and M=floor(N/p). In particular A>=1/b. Equation (6)
gives

    sum_(m<=N/p)|J_N(bpm,p^k)|
      <=C/(bp) sum_(m<=M)m^(-1)K(A/m)
      <=(C_b/p)min(1,(bN/p^k)^a).                  (7)

Here is the complete discrete proof of the last inequality. If M<=A,
then K(A/m)=(m/A)^a and

    sum_(m<=M)m^(-1)K(A/m)
       =A^(-a)sum_(m<=M)m^(a-1)<=C_a(M/A)^a.

If M>A, the same calculation pays m<=A. For the remaining terms split
into dyadic blocks 2^j A<m<=2^(j+1)A, j>=0. On each such block,

    K(A/m)<=2^((j+1)a)G(2^j),
    sum_(2^j A<m<=2^(j+1)A)1/m
       <=log2+1/(2^j A)<=log2+b 2^(-j).

The sum of their product over all j is finite because G has a Gaussian
tail. This argument also handles A<1: the bound A>=1/b controls the
first discrete blocks. It requires no quadrature approximation. Finally
M/A<=bN/p^k, which proves (7) in the stated form.

For a fixed p, the complete exponent sum obeys

    sum_(k>=1)min(1,(bN/p^k)^a)
       <=C_a+log(bN)/log p.

Indeed, count p^k<=bN directly; the remaining terms form a geometric
tail with ratio p^(-a). Therefore

    sum_(p<=N)(log p)sum_(k>=1)sum_(m<=N/p)
                                    |J_N(bpm,p^k)|
      <=C_b sum_(p<=N)[(log p)/p+log(bN)/p]
      <=C_b log^2(2N).                             (8)

The last inequality already follows by enlarging the prime sums to all
integers. No prime number theorem, Möbius cancellation, or conjectural
prime correlation is used. Restoring |mu(pm)| only decreases this bound.
Summing the three fixed outer branches with |c_b| preserves it.
Overlapping total labels are harmless because the estimate is branchwise.

## 5. Prime2 and the precise disjoint conclusion

The common factor of d and n can arise solely from the outer labels4 or16.
To cover it without misidentifying the natural two-label pairing, pay the
ENTIRE prime2 non-delta row. With d=bm, A=2^k/b and M=N, the same discrete
estimate gives

    sum_(m<=N)|J_N(bm,2^k)|
       <=C_b min(1,(bN/2^k)^a).

Summing every k>=1 yields

    sum_(k>=1)(log2)sum_(m<=N)|J_N(bm,2^k)|
                                      <=C_b log(2N).                 (9)

For a disjoint decomposition, use (9) for p=2 and use (8) only for odd
p. The fixed b is coprime to every odd p, so p|d is then exactly p|m in
the original natural label d=bm. This proves the asserted complete
absolute bound

    sum_(d) sum_(n=p^k, gcd(d,n)>1)
       |a_(N,d)|Lambda(n)|J_N(d,n)|<=C log^2(2N),    (10)

and, more strongly, (9) pays the whole prime2 row even when d is odd.
Absolute convergence of the complete prime-power subrow follows from
the same proof, uniformly in any prior finite exponent cutoff.

This includes the non-delta common entrance produced by adjacent-prime
pairing; that older entrance estimate is a subset, not a second budget.
The remaining non-delta terms have odd p and gcd(d,p^k)=1. Their ordered
bulk, natural outside strip, and the fixed full-N right field remain.
All of (2), including the reflected/causal right field and any finite
endpoint accounting, remains untouched. Equations (8)-(10) are therefore
a genuine subpower bound for the stated arithmetic subrow and no more.
