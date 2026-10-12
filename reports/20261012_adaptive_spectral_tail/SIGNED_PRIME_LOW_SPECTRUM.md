# Complete signed-prime exterior cancellation and effective localization of negative eigenstates

For the original even operator H=B-V, let P*=1_(-infinity,0](H)-|e0><e0| remove only its known normalized ground. This theorem proves the genuine signed operator tail

    ||1_(|x|>=R) V P*||=o(t(R)exp(R/2)),
    t(R)=7exp(2R-(pi/2)exp(2R)).

The complete prime sum is taken before its norm. Its leading translated moment cancels by the original ground orthogonality; compactness upgrades ordinary PNT convergence to uniform convergence on the true spectral source set.

A second, explicit bound does not need a convergence rate for that unknown projection:

    ||1_(|x|>=R)V||<=D(R)=10000t(R)exp(R/2).

For any normalized actual eigenvector Hv=-kappa v perpendicular to e0, 0<kappa<=1/2, this bound and a legal sharp-cutoff Gamma identity give an explicitly searchable finite radius R(kappa,eta) and a compactly supported original form-domain witness v_c satisfying

    H[v_c]+(1/2)|<v_c,e0>|^2<=-kappa/2,  0<eta<=1/16.

This localizes a hypothetical negative state, with its true ground term paid. It does not prove positivity of the central block, a successful Schur criterion, or absence of that state. The original certified gap 511/1024 is unchanged; no zeta zero is excluded.

## Original inputs and scope

The closed original realization, theta normalization and complete-prime conventions are the user's [ORIGINAL_FORM_FOUNDATION.md](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/78077e787ffc447b0cb173f6c130be903c34e465/reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md). Work on complex even L2(dx), with Fourier transform fhat(t)=integral f(x)exp(-itx)dx and Plancherel measure dt/(2pi). Use

    Phi(x)=sum_(n>=1)[4pi^2 n^4 exp(9x/2)-6pi n^2 exp(5x/2)]
                              exp[-pi n^2 exp(2x)]  (x>=0),
    m^2=Phi/(2cosh(x/2)),
    C0=EulerGamma+pi/2+3log 2+log pi,
    Astar=4pi^2(125/121)<49.

Phi is extended by its genuine evenness. The normalization is integral 2Phi cosh(x/2)dx=1. The associated form defines B; its domain does not assume global unweighted b(D)(mv) in L2. The theta bounds and complete-prime norm convergence are proved in [REPORT.md, Sections 1.1–1.2](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/78077e787ffc447b0cb173f6c130be903c34e465/reports/20261012_adaptive_spectral_tail/REPORT.md):

    9 exp(4|x|-pi exp(2|x|))<=m(x)^2
         <=Astar exp(4|x|-pi exp(2|x|)),
    ||V-V_N||<=(20Astar/9)(N+1)^2 exp[-pi(N+1)].

For clarity, the two weighted scalar estimates used below also follow directly. With u=exp(2x),

    ||m exp(|x|/2)||_2^2
    <=Astar integral_1^infinity u^(3/2)exp(-pi u)du
    <=Astar exp(-pi)(1/pi+2/pi^2+2/pi^3)
    <(500/121)(1/20)(22/7+2+2/3)
    =3050/2541<36/25.

Here u^(3/2)<=u^2, 3<pi<22/7 and exp(pi)>20 suffice. Also exp(2x)m(x)^2<=Astar exp(6x-pi exp(2x)) decreases for x>=0, so ||exp(|x|)m||_infinity^2<=Astar exp(-pi)<49/20<4. These supply the constants 6/5 and 2 with the full theta series retained.

The user's [matching narrow theta-tail bounds](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/78077e787ffc447b0cb173f6c130be903c34e465/reports/20261012_narrow_theta_tail/REPORT.md) concern one specified odd source and its cutoff family. They are a separate result, retain their user attribution, and are not substituted for the even-space operator-norm and actual-eigenstate assertions proved here.

The only prime-distribution input for the qualitative cancellation is the ordinary unconditional PNT, in its [Chebyshev form](https://dlmf.nist.gov/25.16#E3). The explicit coarse bound uses only elementary Chebyshev bounds. The [independent review](REFEREE_SIGNED_PRIME_LOW_SPECTRUM.md) covers all six sections, the discontinuous cutoff domain and the relative-depth ledger.

## 1. Original objects

Work on the original even L2(dx) space. Write

 H=B-V, B=M_m b(D)M_m,
 V=C0 m^2+m S m,
 Sf(x)=sum_(n>=2) alpha_n[f(x-log n)+f(x+log n)],
 alpha_n=Lambda(n)/sqrt(n),
 m^2=Phi/(2cosh(x/2)),
 b(t)=Re psi(1/4+it/2)-psi(1/4).

The known ground vector e0=sqrt(2Phi cosh(x/2)) has norm one and He0=-e0/2. Let P=1_(-infinity,0](H) and P*=P-|e0><e0|. The original closed realization has B>=0, V bounded, and D(H)=D(B). The complete weighted prime sum is retained.

We use the already established scalar bounds C0<8 and, for R>=1,

 t(R)=7 exp(2R-(pi/2)exp(2R)),
 sup_(|x|>=R)m(x)<=t(R),
 m(R)>=3 exp(2R-(pi/2)exp(2R)),
 ||m exp(|x|/2)||_2<6/5.

In particular exp(|x|)m(x)<2. The main signed assertion is

 ||1_(|x|>=R)V P*||=o(t(R)exp(R/2)).                    (1)

This is a uniform statement on the actual spectral space, not on arbitrary source coefficients. It uses the original ground moment. It does not give a rate relative to the depth of an unknown eigenvalue.

## 2. Weighted compactness and the canceled moment

For v in range(P),

 0<=b[mv]=H[v]+<v,Vv><=||V||||v||^2.

Thus, for the Fourier projection Q_T,

 ||(1-Q_T)mP||^2<=||V||/b(T).

Q_T m is Hilbert--Schmidt and b(T)->infinity, so mP is compact. For every fixed a>1/2 the map mP*:L2->X_a, where X_a=L2(exp(2a|x|)dx), is also compact: truncate x to a compact interval, then use the operator-norm tail bound sup_(|x|>A)exp(a|x|)m(x)->0.

For f=mP*v, evenness and ground orthogonality give exactly

 M(f):=integral exp(-x/2)f(x)dx
      =integral cosh(x/2)f(x)dx=0,                      (2)

because <e0,P*v>=2M(f). M is continuous on X_a. This is the true pole moment; no new constraint is introduced.

## 3. Complete prime translates converge strongly before compactness is used

For R>=1 set I=[-1,1] and

 T_R f(y)=exp(-(R+y)/2)(Sf)(R+y).

For each a>1/2,

 sup_(R>=1)||T_R||_(X_a->L2(I))<infinity.               (3)

For the minus shift, Minkowski bounds this norm by a fixed multiple of

 exp(-R/2)sum alpha_n exp[-a max(|R-log n|-1,0)].

Partition log n-R into [j,j+1]. The elementary Chebyshev bound psi(X)<=C X bounds the interval mass after normalization by C exp(j/2). The remaining sum is bounded by

 C_a sum_(j in Z)exp(j/2-a max(|j|-2,0))<infinity.

The plus shift is bounded by

 exp(a+1/2)exp(-(a+1/2)R)sum Lambda(n)n^(-a-1/2),

which is finite. These estimates also give absolute L2(I) convergence of both complete prime legs and identify them with the original weighted-operator limits.

For each fixed smooth compact f, partial summation and the unconditional prime number theorem psi(X)~X imply, uniformly on I,

 T_R f(y)->M(f).                                      (4)

Indeed the plus leg tends to zero. For x=R+y the minus leg's continuous main term is exactly

 exp(-x/2)integral_1^infinity u^(-1/2)f(x-log u)du
 =integral_(-infinity)^x exp(-z/2)f(z)dz,

which eventually equals M(f). The PNT error tends to zero uniformly for y in I against this fixed smooth profile. Only ordinary PNT is used, not a short-interval theorem. For normalization see NIST DLMF section 25.16, https://dlmf.nist.gov/25.16 .

By density and (3), (4) extends to strong convergence X_a->L2(I). Compactness from Section 2 then gives

 e(R):=sup_(r>=R)||T_r mP*|| ->0.                       (5)

No uniform C1 or pointwise estimate on the spectral space is assumed.

## 4. Restoring the theta weight on the entire exterior

On I_j=[R+j,R+j+1], (5) gives for each unit input

 integral_(I_j)|m(x)S(mP*v)(x)|^2dx
 <=t(R+j)^2 exp(R+j+1)e(R)^2.

For R>=1,

 sum_(j>=0)exp(j)[t(R+j)/t(R)]^2
 =sum exp(5j-pi exp(2R)(exp(2j)-1))<=2.

This follows from exp(2j)-1>=2j and a geometric sum. Evenness handles the negative exterior. Therefore

 ||1_(|x|>=R)mSmP*||<=2sqrt(e)t(R)exp(R/2)e(R).

The C0m^2 contribution is at most C0t(R)^2, proving (1). This takes the signed prime sum before its norm; replacing the source by its absolute value would lose (2).

We also record a deliberately loose but explicit full-space bound, useful without any unknown projection:

 ||1_(|x|>=R)V||<=D(R),
 D(R)=10000 t(R)exp(R/2), R>=1.                        (6)

Here is an elementary ledger. The binomial inequality psi(2n)-psi(n)<=2n log2 and induction give psi(X)<=4X. With a=1 the minus-leg constant in (3) is at most

 4exp(7/2)sum_j exp(j/2-|j|)
 <=4*81*(10/3)=1080.

We used e<3, exp(1/2)>=3/2 and exp(3/2)>4. The plus leg is at most 12, since sum Lambda(n)n^(-3/2)<=12 by partial summation. Thus ||T_R||_(X_1->L2(I))<1200. Since ||exp(|x|)m||_infinity<2, the preceding exterior calculation is bounded by 4800sqrt(e)t(R)exp(R/2). The remaining C0t(R)^2 is absorbed by the constant 10000. The bound is on the original even space; no P* is used in (6).

## 5. Sharp cutoff and the complete Gamma cross

Let chi_R=1_(|x|>=R), R>=2. This multiplication preserves Q(b), and hence the original Q(B). To verify the discontinuous cutoff rather than assuming it, use

 k(h)=exp(-|h|/2)/(1-exp(-2|h|))
     <=1/(2|h|)+exp(-|h|/2).

Between a central interval and its exterior, the first kernel is a pair of half-line Carleman operators, each bounded by pi/2; the second has full-line L1 norm 4. The cross operator therefore has norm at most pi+4<8. The Carleman constant here follows directly from the weighted Schur identity integral_0^infinity (s+t)^(-1)t^(-1/2)dt=pi s^(-1/2); the singular coefficient is 1/2 at each boundary. The distribution identity for [b(D),chi_R] extends it boundedly on L2. Closedness on D(b), followed by interpolation for b+1, gives form-domain invariance. Equivalently one may first approximate the indicator by monotone smooth cutoffs with the same bounded cross-commutator estimate.

The exact identity, first on a core and then on Q(b), is

 b[chi_R f]=Re b(chi_R f,f)+E_R[f],
 E_R[f]=Re integral_(|x|>=R,|y|<R)
                   k(x-y)f(x)conj(f(y))dxdy.           (7)

The actual theta factors imply

 |E_R[mv]|<=E(R)||v||^2,
 E(R)=10t(R)exp(-R/2).                                 (8)

For |y|<=R/2, |x-y|>=1 and k(x-y)<(6/5)exp(-|x-y|/2). The Hilbert--Schmidt product bound is at most (36/25)t(R)exp(-R/2), using ||m exp(|x|/2)||_2<6/5 and ||1_ext m||_2<=t(R). The latter follows because the logarithmic derivative of t(x)^2 is at most -2 for x>=1. For R/2<|y|<R, the cross-operator bound 8 and the theta suprema give 8t(R)t(R/2); for R>=2, t(R/2)<=exp(-R/2). Adding the two estimates proves (8).

For a unit genuine eigenvector Hv=lambda v, lambda<=0 and v perpendicular to e0, the legal test chi_R v gives

 b[chi_R mv]=Re<chi_R v,Vv>+lambda||chi_R v||^2+E_R[mv]
 <=||chi_R VP*||+E(R)=o(t(R)exp(R/2)).                  (9)

This is only an absolute exterior-energy estimate; no sign for arbitrary localized superpositions of distinct eigenvalues is used.

## 6. The precise relative-depth consequence and the remaining Schur issue

Now suppose Hv=-kappa v, 0<kappa<=1/2, v perpendicular to e0, ||v||=1. Put z=||chi_R v|| and d_*(R)=||chi_R VP*||. Keeping the eigenvalue term, rather than discarding it as in (9), gives

 b[chi_R mv]+kappa z^2<=d_*(R)z+E(R).

Young's inequality yields the useful relative ledger

 b[chi_R mv]+(kappa/2)z^2
 <=d_*(R)^2/(2kappa)+E(R)
 <=D(R)^2/(2kappa)+E(R).                               (10)

For each 0<eta<=1/16 one can choose a finite, explicitly searchable R>=2 satisfying

 D(R)<=kappa sqrt(eta), E(R)<=eta kappa/2.               (11)

The displayed functions decrease to zero and use only fixed original constants. Then the left side of (10) is at most eta kappa. Thus the actual negative-eigenstate tail can be paid relative to its depth, with a radius depending on that depth. No effective knowledge of P* is required for the coarse version (11).

For clarity this can localize a negative witness, but does not prove its absence. Put v_c=(1-chi_R)v and use the critical, ground-corrected form

 Qcal[w]=H[w]+(1/2)|<w,e0>|^2.

The original ground tail obeys ||chi_R e0||^2<=4t(R)^2exp(R). Under (11) this is at most kappa, and D(R)<=kappa. Since

 H[v_c]=-kappa+2kappa z^2+H[chi_R v],
 H[chi_R v]<=b[chi_R mv]+D(R)z^2,
 |<v_c,e0>|<=z||chi_R e0||,

we obtain

 Qcal[v_c]<=-kappa+b[chi_R mv]+(7kappa/2)z^2
           <=-(1-8eta)kappa<=-kappa/2.                 (12)

This is a compactly supported original form-domain witness; standard core approximation preserves its negative sign. The ground/pole term has been paid rather than dropped. Equation (12) does not say that this central block is positive. Proving the required signs for the growing family of central blocks, or a genuine all-depth Schur condition, remains open. Neither (1) nor (10) controls the unbounded operation of dividing by m^2 and convolving with the critical Mobius heat.
