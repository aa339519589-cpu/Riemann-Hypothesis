# Complete primitive-column cancellation of a physical square-resonant family

For the actual half-damped observation, retain exactly c=s with s squarefree and n=r^2, including all original masks and unit conventions. Summing the complete primitive m column FIRST gives decay faster than any prescribed power of the ambient Z, uniformly in the auxiliary modulus and every Gaussian scale 0<T<=Z. The bound survives the original finite compensation, both original/core nonflat markings and the published Gaussian-only restoring operation. It uses no Q hypothesis.

This is a bound for a precisely specified signed physical contribution. It permits subtracting that contribution before a second-moment decomposition. It does not permit deleting its individual positive Kummer-class energies, and supplies no estimate for the remaining physical family, the whole low side or RH.

## Relation to the actual observation

The original coefficient contains BOTH chi_A(m), with A=cn^3, and the primitive auxiliary xi(m). The first factor retains every genuine A-m common-prime zero. The cancellation below uses their exact product with the original s-Gauss sum; an auxiliary character alone cannot replace chi_A(m). Any later Kummer-class decomposition keeps this original coefficient. No claim about a finite pairwise kernel is needed as an input to the theorem below.

The actual new half-damped observation is defined in [HALF_DAMPED_PROBE.md](HALF_DAMPED_PROBE.md). The auxiliary family and common holes are in [POLYNOMIAL_AUXILIARY_ENSEMBLE.md](POLYNOMIAL_AUXILIARY_ENSEMBLE.md). The exact Gaussian-only operator and normalization used in Section 5 are [RESTORED_AUXILIARY_COMPARISON.md, Part A](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a887d3fa25950f58310a65eab4ae9f53d7d95f24/reports/20261011_qrh_selection_bridge/RESTORED_AUXILIARY_COMPARISON.md). The conditional high theorem in that earlier report has additional hypotheses; none is imported into the primitive-column estimate here. Independent source and proof verification is in [REFEREE_PHYSICAL_SQUARE_RESONANCE.md](REFEREE_PHYSICAL_SQUARE_RESONANCE.md).

## 1. Actual subfamily and statement

Use the original eta=1 physical probe with its half-damped n weight, fixed base data S0,b0,xi0, and any admissible enlarged primitive auxiliary xi modulo b*=b0 b. All original unit masks remain. Let B=N(b*). In each actual finite compensation summand retain exactly the tuples

                 c=s with s squarefree,  n=r^2.             (1)

The original primary representatives and all their fixed unit/ray phases are retained. In particular the completed index is A=s r^6, so A/s is a literal sixth power. Conversely, on the squarefree-s subfamily, the valuation condition A/s in K^(times 6) forces c and s to have the same ideal and n to be a square ideal; the original unit convention must still be retained when identifying literal tuples. We prove the estimate for the unambiguous subfamily (1), not an enlarged family with discarded unit factors.

Freeze the original ambient Z, all slot windows and b. For a finite compensation subset of length d_slot, the scales satisfy, up to fixed compact slot ratios,

 X'=Z^(17/48-d_slot), Y'=Z^(23/48-d_slot),
 T_eff=T N(p_(J^c)) << Z^(7/6-d_slot),
 0<T<=Z, 0<=d_slot<=1/6.                                 (2)

The Gaussian scale T varies in the same family; it does not change b, X',Y', the slots or their coefficients. Denote by I_res,b(T) the contribution of (1) to the entire finite compensated observation, with either original/core nonflat marking. Then for every fixed A0>0,

                   |I_res,b(T)| <<_(A0) Z^(-A0)           (3)

uniformly for all 0<T<=Z and all admissible auxiliary moduli and characters. This estimate requires no Q. Its constants depend on the original fixed smooth profiles and slot system, not on B.

For the reviewed polylogarithmic auxiliary ensemble, the normalized Gaussian-restored contribution A_b[I_res,b/c_Sb](Z), and its finite normalized average, also satisfy (3). The ambient slot normalizer A_T(Z) costs only a fixed logarithmic power and may likewise be included by adjusting A0.

## 2. Exact character cancellation, with every zero mask

The original corrected completed row contains the factor chi_A(m). It must be present: it is part of Psi_(m,s,eta)(A), not part of the auxiliary phase alone. For squarefree s the character chi_s modulo s is primitive. With the original positive additive convention,

 g_(chi_s)(s,-m)/sqrt(Ns)
       =gamma_1(s) conjugate(chi_s(-m)).                   (4)

On (1), chi_(s r^6)(m)=chi_s(m) when m is prime to sr, and it is zero otherwise. Multiplication in (4) consequently gives exactly

 chi_(s r^6)(m) g_(chi_s)(s,-m)/sqrt(Ns)
     =gamma_1(s) conjugate(chi_s(-1)) 1_((m,sr)=1).        (5)

This includes primes shared by s and r. No coprimality (s,r)=1 is imposed. All the remaining phases in the original physical coefficient are independent of m and have modulus at most one on their original support. In particular the genuine full-modulus auxiliary Gauss root is not split into local roots or removed inside a signed average: it is a fixed unit scalar for the complete m sum considered here.

Thus the remaining m column is the complete primitive auxiliary character xi(m), with exactly the original additional sr-unit mask and the original radial window. Put

 M=B (Ns) X', D=rad(sr),
 C_xi(M;D)=M^(-1/2) sum_(m in O) xi(m) 1_((m,D)=1) W0(Nm/M).

Here (D,b*)=1 by the genuine physical masks. The zero extension of xi already handles the bad primes.

## 3. Primitive Poisson retains the full auxiliary normalization

For the fixed smooth radial test W0 and every L>=0, primitive character Poisson summation gives, uniformly for every U>0,

 |sum_m xi(m) W0(Nm/U)|
                   <<_L sqrt(B) (B/U)^L.                 (6)

For U>=B, the dual zero term is absent because xi is nonprincipal and primitive. Its exact Gauss amplitude U/sqrt(B), followed by the full nonzero Schwartz tail, proves (6). For U<=B, the same complete dual sum is O(sqrt(B)); since (B/U)^L>=1 this also proves (6). The field lattice and additive convention change only fixed constants. No physical m cutoff is introduced and no auxiliary-conductor power is hidden.

Expand the unit mask once:

 C_xi(M;D)=M^(-1/2) sum_(d|D) mu(d)xi(d)
                             sum_l xi(l) W0(Nl/(M/Nd)).

Applying (6), and using Nd<=N(sr), yields the complete bound

 |C_xi(M;D)|
   <<_(L,epsilon) ((Ns)X')^(-1/2)
                    (N(sr))^epsilon (Nr/X')^L.           (7)

Indeed the exact factor for a divisor d is
((Ns)X')^(-1/2) [Nd/((Ns)X')]^L. The full norm B cancels. Formula (7) is valid even if Nr>X'; its right side is then a permitted larger bound. This avoids an artificial long/short split.

## 4. The original Gaussian pays all r and subset ranges

In the half-damped row, the c,n coefficient on (1) has absolute value

                     (Ns)^(-1/2) (Nr)^(-3).

Consequently (7), the exact outer Y'^(-1) W1(Ns/Y'), and the original Gaussian V_G(Ns (Nr)^6/T_eff) give, for L>2,

 |I_res,b,subset(T)|
  << (Y')^(-1)(X')^(-1/2-L)
       sum_(Ns~Y') (Ns)^(-1+epsilon)
       sum_r (Nr)^(L-3+epsilon)
                         V_G(Ns (Nr)^6/T_eff).            (8)

All original row masks and marked divisibility tests may be retained; only this positive upper bound is enlarged. Let R_s=(T_eff/Ns)^(1/6). Ideal counting and the whole log-Gaussian envelope give

 sum_r (Nr)^(L-3+epsilon) V_G((Nr/R_s)^6)
                     <<_(L,epsilon) R_s^(L-2+epsilon)     (9)

for every R_s>0. For R_s<1, keep the original rapid Gaussian tail; (9) remains true. Its constants may grow with the prescribed fixed L, which is chosen after the requested A0 and before taking Z to infinity.

By (2), uniformly in all actual compact slot ratios and all 0<T<=Z,

 X' >> Z^(18/96),  Y' >> Z^(30/96),
 R_s << Z^(11/96).

Substitution in (8)--(9), including the actual annular s count, gives the convenient coarse bound

            |I_res,b,subset(T)|
                       << Z^(-61/96-7L/96+epsilon).       (10)

The strict 7/96 gap is the difference between the smallest X' exponent and the largest possible r scale. It is not inferred from a single unrescaled summand.

For the entire original finite compensation, each coefficient (ND)^(-3/2) has modulus at most one, and the total absolute fixed-slot tuple mass is O(Z^ell)=O(Z^(16/96)); there are only 2^K subset choices. Thus (10) gives

                 |I_res,b(T)|
                       << Z^(-45/96-7L/96+epsilon).       (11)

For any requested A0 choose a fixed L>2 large enough in (11). This proves (3), with all physical r, all actual subset rescalings and the full Gaussian tails included. No order of the Gaussian estimate grows with Z.

## 5. Restoration and the essential ordering restriction

On the uniform norm sup_(0<T<=Z)|I_res,b(T)|, the physical dilation D_p=P^(-5/6) shift(T/P) has norm at most P^(-5/6). The reviewed restoring factor therefore satisfies

 ||A_p|| <= (1-P^-2)
             [1+(1-P^-1)P^-5/6+P^-4]/(1-P^-3)
          <=1+O(P^-5/6).

For the same polylogarithmic pool, product_(p|b)||A_p||=O(1). The factor c_Sb^(-1) costs O(1) as well, because product(1-P^-1)^(-2)=O(1). Hence the restored contribution is still smaller than any prescribed power of Z. The operation changes only T and preserves the support (1), so this is the same physical subfamily at every term of its convergent series.

The proof sums the ENTIRE primitive m column before any positive decomposition by the Kummer class of m/s^2. On one such class xi(m) is constant along its sixth-power direction, and the cancellation in (6) need not hold. Therefore (3) cannot be assigned to each within-class positive energy, nor used to discard positive terms in a previously squared and regrouped formula. It permits subtracting the signed family (1) from the exact physical observation BEFORE that second-moment reduction. The remaining physical family and all its cross-class correlations still require their own estimate.

## Source inputs

The exact physical definition is general-probe and the definition of Psi_(m,s,eta) in [the pinned September 30 source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), lines 3345-3410, including the primitive auxiliary convention, general-probe and Psi definitions. The finite compensation is compensated-probe-definition, lines 6890-6905. The only analytic input in (6) is the original primitive character Poisson identity and Schwartz decay. The Gaussian-restoring operator and its normalization are those already reviewed and published in RESTORED_AUXILIARY_COMPARISON.md at a887d3fa25950f58310a65eab4ae9f53d7d95f24. This note uses none of the corrected moving Gauss-hole formulas and no unproved nonprincipal-row or whole-probe estimate.
