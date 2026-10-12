# Independent review: exact-order complete-prime edge correction

The complete [mathematical proof](EXACT_PRIME_EDGE_CORRECTION.md) has been independently reviewed, including its explicit even trial columns, global operator order, complete-prime error and computable rational Gram inversion. It gives no successful central inertia test, critical positivity certificate or zero exclusion.

## Actual domains and an effective Gram inverse

The source-cell reconstruction proved in Section 1 of this report, including its error rho<epsilon/20, has been independently reviewed. This manuscript correctly uses only ||v||<=1 and B[v]<=41 there.

The sharp cell source has Fourier transform bounded by min(sqrt(h),2/(sqrt(h)|t|)). The complete digamma symbol grows logarithmically, so b(t)^2|phihat(t)|^2 is integrable. Thus each single cell belongs to the full-line D(b(D)). Its normalized reflected even combination phi_j^+ belongs to that domain in the original even space. The column psi_j=phi_j^+/m is original even L2 with compact support and belongs to D(B) by the associated-form criterion, with Bpsi_j=m b(D)phi_j^+. This is a genuine original-domain column, not a formal unweighted inverse.

For u supported in [-R,R], translation by Klog2 with Klog2>2R has disjoint support. Telescoping and Cauchy give 2||u||^2<=K^2||tau_log2 u-u||^2. On the difference support both theta factors are at least mu(R+log2), and alpha_2>1/4. Combined with ||Psi c||>=||c||/M, this proves the stated g_R lower bound for every finite Gram G_Q, Q>=2, and the full Gram. It is explicit, although extremely small.

## Exact global order and residual

For C_Q=E_QPsi and G_Q=Psi*E_QPsi, the factor sqrt(E_Q)Psi G_Q^(-1)Psi*sqrt(E_Q) is the orthogonal projection onto its finite-dimensional range. Hence F_Q=C_QG_Q^(-1)C_Q* satisfies 0<=F_Q<=E_Q<=E. The variational identity (9) follows from the same projection or direct completion of squares.

In E-F_Q=(E-E_Q)+(E_Q-F_Q), the first term is paid on the original v by the complete-prime tail 2delta_bar(Q)||v||^2. The variational second term is at most e[v-Zv]. This explains why the omitted-prime price in (10) has no artificial mu(R)^(-2) multiplier. The selected cutoff gives (11).

## Computable columns and rational order preservation

Formula (12) is the full expansion of E_Qpsi_j, including both shift directions and the diagonal. It has compact support within [-R-log Q,R+log Q]. Its finitely many discontinuities are known cell endpoints or their translates; away from them the theta factors and their derivatives are computable with explicit convergent tails. Certified integration of every Gram entry is therefore available without a spectral oracle.

The complete-prime column and Gram errors (13) are the actual operator-norm tail times ||Psi|| or its square, with constants 2delta_bar(Q)/mu and 2delta_bar(Q)/mu^2. They do not disappear merely because the columns are finite in number.

If ||G_tilde-G_Q||<=delta, G_plus=G_tilde+delta I is above G_Q>=g_R I. Inversion reverses the positive order, hence C_QG_plus^(-1)C_Q*<=F_Q. The rational approximation is performed directly on the L-dimensional even coefficient space; entrywise error delta/L and Hermitian symmetry give the required norm error. The inverse difference is at most 2delta/g_R^2; ||C_Q||<=18/mu then gives 648delta/(mu^2g_R^2), at most epsilon/4 with (14). The exact computable column functions are retained. Replacing them by floating approximations without an additional order proof would not retain (15), and the manuscript correctly does not do that.

## Global comparison and exact limitation

The combined residual is positive and below epsilon on the entire class ||v||<=1, B[v]<=41. Max-normalization gives the full-domain relative bound, including a separate zero-vector case. The comparison Lhat=B-C0m^2-p+Fhat is therefore genuinely below H on Q(B), with unchanged Gamma coefficient, no scalar penalty, and the same operator domain D(B). Its low-state compression has the asserted error.

The final limitation is mathematically necessary. On the infinite-dimensional intersection ker(H) intersect ker(Fhat), Lhat[v]=-e[v]. Already the prime-two edge has trivial kernel on original L2: its zero form forces log2-periodicity almost everywhere, impossible for a nonzero L2 function. Thus every such fixed finite-rank comparison has infinite negative index, including in the ground-perpendicular space. Exact order does not turn it into a critical finite certificate. Positive-depth or central applications still require a separate verified sign or inertia argument. No zero exclusion follows.
