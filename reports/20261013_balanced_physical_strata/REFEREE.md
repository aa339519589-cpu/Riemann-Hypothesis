# Mathematical review of the balanced physical-stratum estimates

The two proofs in [REPORT.md](REPORT.md) are accepted with their original physical definitions, full source activation, complete old restorer, and stated narrow-branch restrictions. The primary review separately verifies the sparse power-free and same-class estimates. A second independent review below covers the full-source and fixed-k refinements contributed during the proof development. No estimate for the remaining large-kernel or full square scalar term is claimed.

## Review A. Sparse power-free strata

## 1. Original branch and both auxiliary roots

The selected branch has the same all-Ec tuple in both columns, n=n'=1, a common squarefree a and fixed varpi, and coprime quotient ideals b,b' of norms comparable to sqrt(Z/P). All original zero masks and fixed bad conventions remain in force. A hole may make this branch empty. No unrestricted sum over other assignments, other free-norm scales or distinct E/a branches is substituted.

In the reviewed mixed-prime identity the gcd is C0=E a varpi and the lcm is C0 b b'. Substitution gives exactly w=q'(b')^2m-qb^2m' and the complete normalized mixed Gauss factor (3), including both original sector and base-character phases. The common-unit conditions imply (w,qq')=1, so w=0 is absent. Its absolute value on its genuine unit support is one. This identity does not replace either original Gauss root by an unnormalized root, identify q with q', or erase the physical h inequality. Subsequent absolute upper bounds permit arbitrary further masks of modulus at most one.

## 2. The norm radius and the true integral fibre

At fixed activation parameters the original m disks have norms bounded by P_aux X exp(-alpha) Ns and its primed counterpart, up to fixed constants. Multiplication by q' (b')^2 or q b^2 and the squared triangle inequality gives

    Nw <= C P_aux^2 Z^(11/6)(exp(-alpha)+exp(-alpha')).

Thus W=P_aux^2 Z^C exp(A), A=|alpha|+|alpha'|, is a valid radius with W>=1 for all parameters. The two coefficients q'(b')^2 and q b^2 are coprime on the common-unit branch. The Eisenstein integral solution set is therefore a translate of the one-parameter lattice with steps q b^2 and q'(b')^2. Counting either physical disk gives the minimum in (5), with its necessary constant term. The arithmetic scales satisfy X Y_s=Z^(5/6) and (Nb)^2,(Nb')^2 comparable to Z/P. The count is at most

    C[1+P Z^(-1/6) min(exp(-alpha),exp(-alpha'))]
      <= C_P exp(A/2).

The final inequality uses min(exp(-alpha),exp(-alpha'))<=exp(A/2); it is valid for every pair of real activation parameters. If a physical disk becomes too small to contain a nonzero element, the actual sum only shrinks. No smooth density approximation or long fibre is assumed.

## 3. The auxiliary power comes from the original radial normalization

I reread the opening raw summand of [the fixed public physical definition](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/8165d030818737dd19838a03c4f8645eb6e86973/reports/20261011_qrh_selection_bridge/UNCONDITIONAL_SINGLE_PRIME_COMPARISON.md). Each column contains M^(-1/2), with M=N(b0q) X exp(-alpha) Ns. Its auxiliary Gauss root is already normalized and has modulus one. The finite s Gauss sum is bounded by Ns before its actual division by sqrt(Ns); the s windows, c values, ordered slot tuples and row multiplicities in this branch have only polynomial Z cost. The scalar normalizer is uniformly bounded in q apart from the already retained fixed logarithmic ambient factor. After bounding the logarithmic Gaussian by its supremum, the only unbounded activation factor in each raw magnitude is exp(alpha/2) from M^(-1/2). The product is therefore at most

    P_aux^(-1) Z^C exp(A/2).

There is no extra P_aux factor of either sign from the normalized tau. No unbounded original variable is silently replaced by a finite label here: the unbounded physical m variables are counted by the exact fibre, the two primes will be averaged with probability weights, and the two source variables are integrated below.

The full old T-only restorer has coefficient series sum_j (Nq)^(-3j), together with numerator shifts of coefficient sizes O((Nq)^(-5/6)) and O((Nq)^(-4)). This follows from the source's D_q=(Nq)^(-5/6) times the T/(Nq) dilation and its (Nq) D_q^6 term. Every shift changes only the Gaussian T scale. Its supremum bound and the absolute coefficient sum are uniform in all source parameters and leave the m disks, w, fibre, original slots and normalizers unchanged. The same raw magnitude bound holds after both complete restorers.

## 4. Sixth-power-free counting, including units and full source

The Eisenstein ring is a PID with finitely many units. Writing each nonzero element w=u v^6, with u sixth-power-free and its actual unit retained, gives only a bounded unit multiplicity. The original fixed and bad prime valuations may be included; dropping the sixth-free restriction on u only enlarges the count. The elementary norm-disk count O(V), valid for V>=1, gives

    # {0<Nw<=W, Nu<=U}
      <= C W^(1/6) sum_(Nu<=min(U,W)) (Nu)^(-1/6)
      <= C W^(1/6) U^(5/6).

The same upper bound holds for the attainable-w set depending on q,q' and for any further mask. It does not require uniformity of a pushforward measure or any character-sum theorem.

Combining the fibre count, the sixth root of W and the two radial normalizers gives the exact factor

    P_aux^(-2/3) U^(5/6) Z^C exp(7A/6).

The source is genuinely f_q=m v with v in the original L2 space. Cauchy--Schwarz bounds its exp(2|alpha|) L1 moment by ||v||_2 ||m exp(2|alpha|)||_2, which is finite by the complete theta decay. Thus both activation integrals converge absolutely against the displayed exp(7A/6). This is a direct full-source proof for the sparse w stratum. It neither invokes nor needs the earlier conditional complete-column tail discussion; no source tail is discarded after a costly raw absolute-m bound.

The remaining selected label sums and any explicitly allowed polynomial row weights cost a fixed power of Z. Each auxiliary law is positive with total mass one, so the independent double mean adds no prime-count factor. The final upper bound is exactly (8). Taking U=P_aux^(4/5-eta) gives exponent -2/3+(5/6)(4/5-eta)=-5eta/6. This is a genuine absolute estimate, including all original phases, full source and restorer, on the specified restricted physical branch. It may also be restricted to large Nw. It is not merely the previous small-Nw bound.

## 5. Fixed higher powers and the remaining square threshold

For each fixed integer k>=3, the same element count is C W^(1/k) U^(1-1/k), with the bounded unit choices retained. The auxiliary exponent is 2/k-1; the source exponent is 1+1/k<2. Hence (10) follows with the same full-source argument. The fixed-k extension and the full-source exponents were checked in the separate second review below. The literal physical cube subset is included by U=1 and has exp(-Z/3) times a polynomial as its upper bound. A physical cube is not thereby identified with a dual cube frequency or the model term in a different Poisson formula.

For k=2 the auxiliary exponent from this argument is zero. The full square stratum and the remaining large power-free kernel are not estimated by a positive auxiliary saving. Nor do these sparse-stratum bounds control the complete coherent Mobius signal, all compensation assignments or the original signed low matrix.

## Review B. Masked same-class subtraction

## 1. Exact same-class parametrization

The definition h=[m/c^2] is the original element class in K*/K*6, not a norm-class replacement. For c=C0 b and c'=C0 b', class equality gives m(b')^2/(m'b^2) a sixth power. The genuine zero extensions imply (m,c)=(m',c')=1. At a prime dividing b, the valuation of m' is therefore congruent to 4 modulo 6; the symmetric assertion holds at b'. At all other good primes the residual valuations of m and m' agree modulo 6. Choosing their common sixth-power-free residual element, with the allowed finite unit convention retained, gives exactly

    m=(b')^4 H u^6,  m'=b^4 H v^6.

Some additional holes on H,u,v are forced by the original support, but dropping them is legitimate for this positive counting upper bound. In particular it does not introduce a spurious phase equality between different ideal directions. The original m variables here are nonzero; zero is absent from the Kummer-class support and from the nontrivial c zero extension.

## 2. Pair counting is uniform at every shifted radial scale

For fixed H, the norm-disk bounds for u and v cost at most C(L1/NH)^(1/6) and C(L2/NH)^(1/6), whenever the corresponding nonzero elements can occur. If an enlarged scale is below the least nonzero norm there are no pairs. The norm counting bound O(V), partial summation and the fixed support constants give

    #pairs <= C(L1 L2)^(1/6) min(L1,L2)^(2/3)
           <= C sqrt(L1 L2).

For example, if L1<=L2, the last comparison is L1^(5/6)L2^(1/6)<=L1^(1/2)L2^(1/2). The same argument remains valid near and below unit scale with the enlarged support constants absorbed in C. Substituting L1=M/(Nb')^4 and L2=M'/(Nb)^4 gives exactly sqrt(MM')/(Nb Nb')^2. This bound is uniform in both auxiliary primes and all real alpha,alpha'; it does not assume that the two radial scales are comparable.

This is an absolute count for every permitted physical pair, before any cancellation or character average. Consequently a bounded mask depending on q,q',m,m',w,sectors or other physical labels can only decrease the absolute sum. The estimate is not an inference that an uncut positive-class theorem survives an arbitrary physical restriction.

## 3. Original radial factors, full s and source, and the whole restorer

The source physical summand has g_(chi_s)(s,-m)/sqrt(Ns), c^(-1/2), and the single radial normalization M^(-1/2). The elementary complete Gauss bound |g|<=Ns gives (4). The full primitive auxiliary tau is normalized and has modulus one; no additional auxiliary half-power is assigned to it. All roots and phases are retained in the contribution being bounded. The fixed bad scalar and ambient A_T inverse have only their established logarithmic costs.

After bounding the actual logarithmic Gaussian by its uniform supremum, the pair count cancels the product M^(-1/2)(M')^(-1/2) exactly. This cancels the auxiliary scale and all activation dependence in that part, rather than trying to estimate an exponentially costly raw-m l1 norm. The complete s windows, including nonsquarefree and powerful s, satisfy

    Y_s^(-2) (sum_(Ns comparable to Y_s) sqrt(Ns))^2 <= C Y_s

by ordinary ideal counting. No squarefree-s support has been invented. Since sqrt(Nc Nc')=NC0 sqrt(Nb Nb'), the remaining denominator is exactly NC0 (Nb Nb')^(5/2), proving (5).

The bound after this cancellation is uniform over alpha,alpha'. The entire source integration is therefore paid by (integral |f_q|)^2. Its finiteness follows from the original f_q=m v representation and Cauchy--Schwarz with the theta weight. Both independent auxiliary measures are positive probability measures. Averaging them does not restore any prime-count factor; restricting or omitting q=q' and cross-prime holes is safe for this absolute upper bound.

I also checked the actual T-only coefficient series. Its geometric weights are (Nq)^(-3j), and its two extra numerator shifts have coefficients bounded by constants times (Nq)^(-5/6) and (Nq)^(-4). These series are absolutely summable uniformly in the auxiliary pool. They change only the Gaussian T scale, whose supremum was already taken; they leave M, physical s, the Kummer class, source variables and selected labels fixed. Thus both complete restorers obey the same upper bound. No source cutoff or unproved projected-tail assertion is needed.

## 4. The common labels and all four exponents

For a fixed-ratio ideal dyad of norm B0, sum_b (Nb)^(-5/2)<=C B0^(-3/2), while sum_a (Na)^(-1)<=C. There are two b sums and only one shared a. The coprimality and squarefree restrictions only reduce these positive upper bounds. The fixed varpi norm is part of the fixed constant. Consequently their total price is B0^(-3), comparable up to fixed P factors to Z^(-3/2).

The common compensation tuple E is essential. Its actual squared slot weights have the diagonal sum sum_E |W_E|^2/NE bounded by Z^epsilon. At each original fixed slot this is the sum of the squared fixed annular weight divided by Np, bounded already by elementary ideal counting (and appearing explicitly in the public source's marked-prime diagonal). The fixed number of slots gives no positive power of their pool sizes. Ordered slot assignments or generator conventions have only bounded multiplicity. Arbitrary different E,E' pairs are not covered by this step, and the manuscript does not claim otherwise.

Combining the prices gives Y_s Z^(-3/2+epsilon)=Z^(-49/48+epsilon). The original outside squared normalization contributes Z^(3/8), leaving exponent -31/48. With exactly one additional common-row weight Na, its fixed dyad costs Z^(1/2), so the raw exponent is -25/48 and the normalized exponent -7/48. These powers include the original logarithmic normalizers. They do not allow an unspecified extra polynomial label multiplicity; the text explicitly excludes such a loss from these stated exponents.

## Result and remaining task

The stated absolute same-class estimate is valid with full source activation, all physical s valuations, both original roots and entire old restorer. It remains valid after any bounded square-w, far-w or other physical mask on this specified common-E/common-a branch. It therefore pays this restricted h=h' subtraction without assuming the masked class kernel is positive semidefinite.

The corresponding scalar two-column term remains a separate estimate. The proof gives no control over all different E/a branches, no whole coherent Mobius bound, and no new low-Schur or zero-exclusion conclusion. The complete same-class theorem is accepted in precisely this scope.

## Review C. Independent full-source and fixed-k verification

The full-source extension is valid. Put A=|alpha|+|alpha'|. The exact fiber lattice has spacing q b^2, of norm Nq (Nb)^2, and similarly in the other coordinate. Its disk count is bounded by

  C[1+P Z^(-1/6) min(exp(-alpha),exp(-alpha'))]
       <= C_P exp(A/2).

Here min(exp(-alpha),exp(-alpha'))=exp(-max(alpha,alpha'))<=exp(A/2); the constant term is covered by exp(A/2)>=1. This remains an upper bound when either actual radial window has scale below one. No auxiliary norm factor enters the lattice count.

The global norm radius W=P_aux^2 Z^C exp(A) has W>=1 and covers the physical w support. The sixth-free count contributes W^(1/6), hence exp(A/6). The two original radial normalizers contribute at most P_aux^(-1) Z^C exp(A/2). All original Gauss roots are normalized units, the remaining finite-label factors are polynomial, and the bounded logarithmic Gaussian and absolutely summable old T-only restorer coefficients are uniform in alpha and alpha'. Thus the three activation costs sum to

                    A/2+A/6+A/2=7A/6<2A.

The original fixed source has integral |f_q(alpha)| exp(2|alpha|) d alpha finite: f_q=m v and Cauchy--Schwarz reduce this to the established theta-weight integral. Applying this in both variables proves the manuscript's full-source bound P_aux^(-2/3) U^(5/6) Z^C. The proof does not need any separate complete-column source-tail theorem or a claim that a raw m absolute tail is cheap.

I independently checked the exponent U=P_aux^(4/5-eta), which gives exp(-5 eta Z/6) Z^C, and the preservation of arbitrary further restrictions by the absolute majorant. The conclusion applies only to the stated balanced all-Ec, n=n'=1 branch and small physical sixth-free part. It supplies no estimate for the remaining large sixth-free part or the complete coherent Mobius signal.

Result: the complete mathematical text and its full-source extension pass this independent review without a requested change.

## Independent fixed-k check

 For each fixed integer k>=3 the same elementary count is W^(1/k) U^(1-1/k). The fiber and pair-normalization exponents remain A/2 each, giving total activation cost (1+1/k)A<2A. The resulting original contribution is bounded by P_aux^(2/k-1) U^(1-1/k) Z^C. In particular a fixed physical cube class has saving exp(-Z/3), and k=2 is precisely the absolute-counting boundary with no auxiliary power saving. These are physical perfect-power strata; none is identified with the raw dual cube-frequency model. The increment passes independent review with the same branch scope.
