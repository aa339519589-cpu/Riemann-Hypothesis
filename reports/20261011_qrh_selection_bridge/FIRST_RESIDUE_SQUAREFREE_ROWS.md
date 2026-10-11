# Squarefree frequency sums in the genuine first-residue row

## Exact scope

This note proves a character-sum input for a previously uncontrolled first-residue frequency type. It does not bound its complete physical sector, the full low probe, or the high comparison. The field is K=Q(sqrt(-3)), the original bad set S is fixed, and all ideals below are prime to S. Norms are denoted q. We invoke Q only in its already verified finite-order Hecke zero-free form Re z>7/8.

The exact first m-Poisson identity at physical n=1 is equation (2.3) of QUADRATIC_DUAL_N1.md Part I, with pinned original source fd4aeeb2. For s=gt, c=gc1 with g,t,c1 pairwise coprime, its frequency coefficient contains

    c_g(H/g) chi_t(H) conjugate(chi_c1(H)) conjugate(xi(H)).       (1)

The auxiliary xi is the primitive residue character fixed in paper.tex lines 3349--3375. In particular its component at the prime over 2 is nonprincipal of order three. Good-symbol conductors are supported at their good numerator/denominator primes and at the fixed prime over 3, and cannot cancel that component over 2. The character values and their nonunit zeros in (1) are retained.

## A genuine ideal character

Consider H=epsilon v a^6 with v good squarefree and nonunit. Fix t,c1,a and the original unit epsilon. Because all three characters in (1) have order dividing six, their a^6 factors are one on the surviving support. Their dependence on the primary generator of v is exactly

    theta(v)=conjugate(xi(v)) chi_t(v) conjugate(chi_c1(v)).       (2)

Any original zero at a prime of tc1 is a fixed deleted-prime condition. It is not discarded from a signed sum. Reciprocity/fixed-ray pieces can be separated before using (2); the pure theta character statement is for the pieces having precisely (2), and no arbitrary additional moving coefficient is included.

Every good ideal has a unique generator congruent to 1 modulo 3: the unit group maps bijectively onto (O/3O)^*, and the class number is one. These normalized generators multiply. Thus (2) defines a finite-order Hecke character on the good ideal group, through a finite ray modulus containing 3b*tc1. Its primitive conductor norm satisfies

    q_f(theta) <= C q_t q_c1,                                    (3)

with C depending only on fixed S and the original presentation. For t having powers, only the relevant radical/conductor is needed; the weaker bound (3) remains valid. The two symbol factors have no conductor at 2. To see that normalization cannot make the xi factor principal, use CRT to choose a primary generator congruent to 1 modulo 3 and modulo all the other ray factors, and with any prescribed nonzero residue at the prime over 2. Its ideal is good. Since xi is nonprincipal at that prime, theta is nonprincipal. The same CRT argument survives every further fixed good-prime exclusion.

The original physical probe uses the radial m-weight W0(q_m/(q_b q_s X)); its two-dimensional Fourier transform is radial as well. For a common radial frequency piece its finite unit factor is therefore exactly sum_epsilon conjugate(xi(epsilon)) chi_t(epsilon) conjugate(chi_c1(epsilon)), which is either zero or six. Keep that factor until the fixed columns are chosen. Equation (2) on normalized generators does not require the raw generator character to be trivial on the six units. For a nonradial test one must instead retain the separate unit weights; the estimate below does not address additional angular characters.

## Exact squarefree Dirichlet series and Q consequence

Let M be any actual common deleted-prime ideal, including the zero masks in (1). For Re z>1,

    F_theta,M(z)=sum_(v squarefree,(v,M)=1) theta(v) q_v^(-z)
      = L^S(z,theta)/L^S(2z,theta^2)
        product_(p|M,p notin S) (1+theta(p) q_p^(-z))^(-1).       (4)

This is an Euler identity for an actual arithmetic sum, and is unrelated to the unproved assertion that a spectral source belongs to an ordinary Dirichlet class. At a prime ramified in theta the theta(p)=0 convention gives local factor one on both sides. If theta is imprimitive, use its actual finite deleted Euler factors in both L-functions.

Since theta is nonprincipal, the numerator in (4) is entire. Input Q makes the reciprocal denominator holomorphic in Re z>7/16. If theta^2 is principal, its pole at 2z=1 produces a zero of the reciprocal, not a pole. No assertion about the boundary line Re z=7/16 is made. Every remaining local factor is nonzero for Re z>0.

Fix 7/16<sigma<1, a smooth compact annular function W0 on positive norms, and a fixed positive buffer in 2sigma-7/8. For all X>=1 and norm modes u, Mellin inversion and a shift to Re z=sigma give

    |sum_(v squarefree,(v,M)=1) theta(v) q_v^(iu) W0(q_v/X)|
      <= C X^sigma q_f(theta)^((1-sigma)/2+epsilon)
          q_M^epsilon (1+|u|)^A.                               (5)

Here ordinary degree-two Hecke convexity bounds the entire numerator. The already verified buffered inverse-L estimate applied at 2sigma bounds the denominator by q_f(theta^2)^epsilon times a height polynomial; q_f(theta^2)<=q_f(theta). Imprimitive factors and the product in (4) cost the actual deleted modulus to an arbitrarily small power. Smooth Mellin decay absorbs the vertical heights and horizontal contour edges. Constants depend on the prescribed buffers and smooth seminorms, not on t,c1,M,X. The unit-ideal term can be subtracted at O(1) when the sector requires v nonunit.

The finite modulus in the inverse bound must contain M, rather than just the primitive conductor. Formula (5) allows compact common norm-Mellin modes only after they have been separated with retained product cutoffs; it supplies no estimate for arbitrary v-dependent weights. A nonzero angular mode on v would twist the denominator by an infinite-order Hecke character, outside the finite-order Q input used here; no such extension is asserted.

## The first-residue shared divisor is different from the quadratic one

For the actual n=1 coefficient in (1), nonzero support forces g=(c,rad H). Write g=g0g1, where g0 contains primes dividing v but not a, and g1 contains the remaining primes dividing a. Since c is squarefree,

    c_p(H/g)=-1 on g0,        c_p(H/g)=q_p-1 on g1.              (6)

Thus mu(g0) times the g0 Ramanujan factor cancels its sign only. The original reciprocal q_g0 survives. In particular one cannot use phi(g)/q_g<=1 as if every g prime had the higher-valuation Ramanujan value. After forcing g0|v, write v=g0v1, with v1 squarefree and (v1,g0)=1; retain theta(g0) and the original zero masks. Applying (5) to v1 at scale X/q_g0 gives, before a conductor-dependent smooth frequency factor, the divisor weight q_g0^(-1-sigma). This converges as an ideal sum. This observation alone does not justify interchanging all c,t,a,g,r/flat sums.

## Remaining mathematical burden

At the original leading annuli, (3) can be as large as q_t q_c1 approximately UY'. The resulting convexity factor in (5) still has a positive conductor power. A complete first-residue sector requires a joint c/t/frequency budget with all original prime slots, shared divisors, physical square layers, Gaussian tails, and exact first-flat coefficients. This note proves none of those missing summations and claims no new full-probe exponent.

Primary fixed sources: original first-completion identity and local scalar table in openai/math fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb; QUADRATIC_DUAL_N1.md Part I equation (2.3); FORMAL_INPUT_Q.md at commit 52ee48d3e2e4c5b0beeb3e4880eca86fb2208ce1. The independent mathematical review is recorded in [REFEREE_FIRST_RESIDUE_SQUAREFREE_ROWS.md](REFEREE_FIRST_RESIDUE_SQUAREFREE_ROWS.md).


Fixed primary links: [original paper](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), [first completion and local scalar identity](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/6257af1e0ee2e5b98c3b3116c1bba2ab93225cf6/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md), and [verified finite-order Q input](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/52ee48d3e2e4c5b0beeb3e4880eca86fb2208ce1/reports/20261011_qrh_selection_bridge/FORMAL_INPUT_Q.md).
