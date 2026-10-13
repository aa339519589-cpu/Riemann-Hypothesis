# Dimension-free near-threshold physical comparison for an entire Green band

Date: 2026-10-14. This addresses all mixtures in a fixed supercritical band, not just separate eigenvectors. The coefficient-one sign is not proved.

## Statement

Let T:K_P→K_N be the actual bounded gradient map, Λ=T*T on the P-gradient Hilbert space, and K=TT*. For γ>0 set Eγ=1_[1+γ,infinity)(Λ), δγ=γ/(1+γ), and Aγ=log(1/δγ). The compact-positive-excess theorem makes Eγ finite dimensional. The construction below gives a linear injective map Fγ from Eγ into the ORIGINAL odd physical form domain such that, with a single fixed finite C independent of γ and dim Eγ,

    ||Fγ ξ||² <= C(1+Aγ)||ξ||_P²,
    h_o[Fγ ξ] = ||ξ||_P² - <ξ,Λξ>_P <= -γ||ξ||_P².

Consequently, with aγ=γ/[C(1+Aγ)],

    rank 1_[1+γ,infinity)(K) <= rank 1_(-infinity,-aγ](H_o).

Both sides refer to actual complete operators. This is a one-sided minmax comparison of counts; no individual eigenvalue pairing or bounded global map between the completions is asserted. At a single eigenvalue 1+γ it gives an actual odd negative eigenvalue of depth at least cγ/(1+log(1/γ)) for 0<γ<=1. The estimate tends to zero at the endpoint.

## Exact auxiliary objects and uniform source embedding

All objects are those of the [actual source and domain theorem](../20261013_supercritical_source_tails/REPORT.md) and the [complete three-halves comparison](THREE_HALVES_BOUND.md). The source reference and row constants used here are independent of that comparison's finite-height exclusion step. On the positive wing let ψ=-Φ', L(x)=Σ_(d_n>x) α_n ψ(d_n-x), μ²=ψ/L, e_N=μ sinh(x/2). Every ratio is centered by ∫ψ sinh(x/2)r=0. For ξ in the P completion write its actual centered representative r_ξ and

    Jξ=v_ξ=√(ψL) r_ξ,   g_ξ=μ Jξ=ψ r_ξ.

The independent reference estimate gives ||J||²<=193 on the whole P completion. All inner products below are conjugate-linear in their first slot. On L²((0,infinity),dx) put

    (A v)(x)=Σ_(d_n>x) α_n μ(x)μ(d_n-x)v(d_n-x),
    Q0=2 C0 M_(μ²)+8|e_N><e_N|,
    (F v)(x)=2Σ_n α_n [μ(x)μ(x+d_n)v(x+d_n)
                    +1_(x>d_n)μ(x)μ(x-d_n)v(x-d_n)].

A is the unitary conjugate of the reflected Markov operator on L²(2ψL dx); it is self-adjoint and ||A||<=1. Its entire series and F's entire series are also controlled by the published weighted coefficient sums. In particular

    N(r_ξ,r_ζ)=2<Jξ,(I-A)Jζ>.

Let B_N be the associated nonnegative operator of q_b[(μv)_odd] on its published auxiliary form domain. The complete pole-inclusive source operator in these coordinates is

    H0=B_N-Q0-F+2A,   D(H0)=D(B_N).

This includes the full-line mass and pole factors. Its form is P-N, not the original physical form until physical L² membership has been paid.

## One operator parameter for the entire mixed band

Work on Eγ and define D=I-Λ^-1 there. Then δγ I<=D<I and 0<I-D<=I. No scalar eigenvalue is assigned to a mixed vector. For a genuine Λ-eigenvector the actual source equation and auxiliary-domain theorem give

    H0 Jξ=-2JDξ+2AJDξ.

Eγ is finite dimensional and spanned by these genuine eigenvectors, so this extends linearly as an identity in auxiliary L² on every vector in Eγ. In particular J(Eγ)⊂D(B_N). Equivalently,

    B_N J=(Q0+F)J-2AJ(I-D)-2JD.                  (1)

The same identity also follows from (P-N)(ξ,ζ)+N(Dξ,ζ)=0 against the common ratio core. No unbounded similarity is used. Every bound below uses ||J|| and ||I-D||, not a sum over an eigenbasis.

## Uniform sharp-cutoff tail including all cross terms

For R>=7/5 let χ_R=1_(x>R), X=J*χ_RJ on Eγ, z=||χ_RJ||, and β=||J|Eγ||<=√193. Thus X>=0 and ||X||=z². The published BV/core-closure argument makes χ_R legal on the auxiliary Gamma form domain. Its full odd Gamma cross estimate is

    q_b[(μχ_RJξ)_odd]
       =Re<χ_RJξ,B_NJξ>+C_R(ξ),
    |C_R(ξ)|<=E_N(R)||χ_RJξ|| ||Jξ||,
    E_N(R)=4π||μ||_infinity μ_R, μ_R=sup_(x>R)μ(x).

Insert (1). The left side is nonnegative, and the mass term is exactly

    2Re<χ_RJξ,JDξ>=<ξ,(XD+DX)ξ>_P.

For unit ξ in Eγ, all remaining terms are bounded above by zβ η(R), where

    η(R)=||χ_R(Q0+F)||+2||χ_RA||+E_N(R).

For the reflected term, one uses ||J(I-D)ξ||<=β, rather than commuting D through J, χ_R, or A. The constant/forward/pole rows are bounded in the same way. Consequently the exact operator order statement is

    XD+DX <= zβ η(R) I on Eγ.                    (2)

The complete row proof of [THREE_HALVES_BOUND.md, section 4](THREE_HALVES_BOUND.md) at coefficient 1 gives

    η(R)<=D_0(R)+E_N(R)<=256 e^R M(R),
    M(R)=128 e^(7R/2) exp[-πe^(2R)/2].            (3)

Here D_0 is precisely the full row sum at δ=0: it contains Q0, both forward rows, and 2A. The labels above e^R and e^(2R) are paid by their full Stieltjes tails. No finite-prime or block-diagonal replacement occurs.

The order-preserving Lyapunov inverse is

    L_D^-1(Y)=∫_0^infinity e^(-tD)Y e^(-tD)dt.

Apply it to the ONE-SIDED upper bound (2). It is positive on self-adjoint order, and L_D^-1(I)=(2D)^-1. Thus

    X <= (zβη(R)/2)D^-1 <= zβη(R)/(2δγ) I.

This does not invoke the generally false inequality XD+DX>=2δγX. Since ||X||=z², divide by z if z>0 to obtain

    ||χ_RJ|| <= βη(R)/(2δγ),
    ||χ_RJ||² <=193·2^28 δγ^-2 exp(9R-πe^(2R)).  (4)

The case z=0 is immediate. This is uniform on arbitrary mixtures and has no rank factor.

## Physical weight and logarithmic norm cost

The complete PNT row theorem in [the reflected Markov report](../20261013_reflected_markov_essential_edges/REPORT.md) proves e^(-x/2)L(x)→J0>0. Continuity and positivity on compact intervals imply

    c_L=inf_(x>=0)e^(-x/2)L(x)>0.

The full theta bounds ψ<=256e^(13x/2-πe²x) and Φ>=2π²e^(9x/2-πe²x) then give, with m²=Φ/[2cosh(x/2)],

    μ²/m² <= C_W e^(2x), C_W=256/(c_Lπ²).        (5)

No decimal value of c_L is asserted. The PNT input is unconditional and keeps every Mangoldt label; it does not require a critical-strip zero assertion.

For a unit ξ, set Vξ(R)=∫_R^infinity |Jξ|². From (4), Stieltjes integration gives, for R>=7/5,

    ∫_R^infinity e^(2x)|Jξ(x)|² dx
       =e^(2R)Vξ(R)+2∫_R^infinity e^(2x)Vξ(x)dx
       <=193·2^29 δγ^-2 exp(11R-πe^(2R)).         (6)

Indeed 2πe^(2R)-11>2 there; the elementary derivative bound for exp(11x-πe²x) pays the last integral. The boundary at infinity vanishes by (4).

Choose Y=max(e^(14/5),2(1+Aγ)), Rγ=(log Y)/2. Let C_Y=e^(14/5)+2 and

    H_*=sup_(a>=0) (1+a)^(11/2) exp[-(2π-2)a]<infinity.

Then Y<=C_Y(1+Aγ), and δγ^-2 exp(-πY)<=exp[-2π-(2π-2)Aγ]. Equation (6) is therefore bounded by the fixed constant 193·2^29 C_Y^(11/2)e^(-2π)H_*. On [0,Rγ], (5) and ||J||²<=193 give the upper bound 193 C_W Y. Include the full-line factor two and define

    C=386 C_W [C_Y+2^29 C_Y^(11/2)e^(-2π)H_*].

For Fγξ=(g_ξ)_odd/m, these bounds prove

    ||Fγξ||²<=C(1+Aγ)||ξ||_P².                   (7)

All constants are fixed functions of the already established row and theta bounds. This is an analytic estimate, not a decimal interval certificate for C.

## Original form, injectivity and minmax

Each vector in Eγ is a finite combination of actual supercritical sources. Those sources have q_b[(g_ξ)_odd]<infinity on the established source completion; (7) now gives physical L² membership. Since the original physical form domain is exactly {u∈L²:q_b[m u]<infinity}, Fγξ belongs to its ODD form domain. The complete bounded physical prime sum and the auxiliary source sum have identical finite-label pairings and convergent full tails; the pole moment vanishes by centering. Thus the closed full source identity identifies the original FORM value (no operator-domain assertion for Fγξ is needed):

    h_o[Fγξ]=(P-N)[ξ]=||ξ||_P²-<ξ,Λξ>_P.        (8)

Injectivity is also paid on this band. If Fγξ=0, then Jξ=0 almost everywhere because m and μ are positive for x>0. But N[ξ]=2<Jξ,(I-A)Jξ>=0, while N[ξ]=<ξ,Λξ>_P>=(1+γ)||ξ||_P²; hence ξ=0.

Combining (7)--(8), every nonzero vector in the dim(Eγ)-dimensional physical image has form Rayleigh quotient at most -aγ, where aγ=γ/[C(1+Aγ)]. Original odd negative spectrum is discrete away from zero, by the parity-preserving compact-negative-part theorem. Form minmax therefore gives at least dim(Eγ) actual odd eigenvalues <=-aγ, with multiplicity. Polar decomposition transfers dim(Eγ) to rank 1_[1+γ,infinity)(K), proving the stated count comparison. The count comparison does not match individual eigenvectors.

## Endpoint limitation

For 0<γ<=1, 1+Aγ<=1+log(1/γ)+log2, so aγ>=cγ/(1+log(1/γ)). This tends to zero. The established fixed physical lower bound -10^-5 remains compatible with sufficiently small positive γ. No unit Green bound, odd nonnegativity, or RH conclusion follows. The new point is the dimension-free actual-band comparison including all mixed spectral parameters, rather than an individual-state estimate or a claim that the two full completions are equivalent.

## Sources and independent review

- [Complete Green comparison and gradient completions](REPORT.md), [positive reference inverse](REFERENCE_INVERSE.md), and [three-halves scalar and full-row estimates](THREE_HALVES_BOUND.md).
- [Actual eigen-source equation, auxiliary operator domain and sharp-cutoff closure](../20261013_supercritical_source_tails/REPORT.md).
- [Compactness of the full positive Green excess](../20261013_compact_green_excess/REPORT.md), [reflected Markov representation](../20261013_green_spectral_interfaces/REPORT.md), and [unconditional PNT row asymptotic](../20261013_reflected_markov_essential_edges/REPORT.md).
- [Original physical form domains](../20261013_foundation_audit/CLOSED_FORM.md), [negative-spectrum compactness](../20261013_foundation_audit/NEGATIVE_SPECTRUM.md), and [odd form-domain and parity bridge](../20261013_odd_operator_domains/REPORT.md).
- [Independent whole-band review](REFEREE_WHOLE_SUPERCRITICAL_BAND.md).
