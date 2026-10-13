# Internal mathematical review of the positive reference inverse

This is an internal independent derivation and proof audit of
[REFERENCE_INVERSE.md](REFERENCE_INVERSE.md), using the finite comparison
in [REPORT.md](REPORT.md). It is not formal verification or an external
referee report. The exact construction passes the checks below; the
critical unit comparison remains unproved.

## Reference normalization

With \(d=\log2\), \(\alpha=d/\sqrt2\), \(w=\psi\sinh(x/2)\), the actual
prime-two forward coefficient is \(c(x)=2\alpha\psi(x)\psi(x+d)\).
Since \(\int w=1/8\), the pole term is
\[
P_{\rm pole}[r]=\int w|r|^2-8\left|\int wr\right|^2.
\]
Thus \(\widehat R=R+8|\int wr|^2=\int w|r|^2+P_{F,2}\) has exactly
the stated coefficients. In the coordinates
\(v_k(t)=\sqrt{D_k(t)}r(t+kd)\), expanding the forward square gives
\(\sum_k|v_k|^2-2\sum_k\beta_k\Re(\overline v_kv_{k+1})\).
This is precisely the Jacobi form in (4), including its factor two.

## Uniform fiber gap

Weighted AM-GM gives \(|\langle v,A_tv\rangle|\le\|v\|^2\), first on
finite sequences and then by density. The displayed tail bound (6)
implies \(\beta_k(t)\to0\) uniformly in \(t\), so each fiber is compact;
the finite truncation error is at most twice the supremum of the discarded
coefficients.

At the exceptional endpoint, with \(a=2\alpha c_\psi\psi(d)\),
\[
D_0(t)=at+O(t^2),\qquad D_1(t)\to w(d)+c(d),\qquad
\beta_0(t)=\sqrt{a/(w(d)+c(d))}\sqrt t+o(\sqrt t).
\]
For \(k\ge1\) the denominators stay positive. Consequently
\(A_0=0\oplus A_d\), and finite-coefficient continuity together with the
uniform tail bound proves operator-norm continuity on \([0,d]\).

For any proposed eigenvector at eigenvalue one, the exact convergent sum is
\[
0=\langle v,(I-A_t)v\rangle
 =\sum_k w_k|r_k|^2+\sum_kc_k|r_k-r_{k+1}|^2.
\]
All \(w_k>0\) for \(0<t\le d\), so the vector is zero. The endpoint
\(t=0\) follows from its block decomposition. Alternating the coordinate
signs conjugates \(A_t\) to \(-A_t\), excluding eigenvalue minus one.
Compactness therefore gives \(\|A_t\|<1\) at each parameter; norm
continuity and compactness of the parameter interval give a uniform
\(\rho<1\).

Only the **fibers** are compact. No compactness of the direct integral is
used. Its norm is at most \(\rho\), which proves the inverse series and
its tail bound in terms of that unevaluated constant. No numerical value
of the gap has been certified.

## Core closure and every current load

The source core is dense in \(L^2(Ddx)\) by removing neighborhoods of zero
and infinity and using smooth approximation where \(D\) is bounded above
and below. The norm equivalence (8) therefore identifies the actual
\(\widehat R\)-closure. The pole mean is continuous because \(w^2/D\le w\)
is integrable. Subtracting a multiple of a fixed core function with nonzero
pole mean makes centered core approximants dense in \(H_D^0\). On that
space \(R=\widehat R\), identifying the quotient completion correctly.

Every \(h\in K_N\) has antisymmetric edge coordinates. The incidence
estimate makes \(W_h\) a legitimate weighted-space limit and implies
absolute convergence of \(\int\psi W_h\), since \(\int\psi L<\infty\).
Edgewise antisymmetry shows that this integral is zero. For the normalized
load \(b_h=2\psi W_h/\sqrt D\),
\[
\|b_h\|_2^2\le4\sup_{x>0}\frac{\psi(x)L(x)}{D(x)}\,\|h\|_N^2.
\]
The supremum is finite. Both numerator and denominator are linear near
zero; away from zero, use \(D\ge\psi\sinh(x/2)\) and the complete-prime
bound \(L\le C_Le^{x/2}\). This verifies the source representation for
all currents, without assuming \(W_h\) lies in unweighted \(L^2\).

The unitary \(\mathcal U\) in (13) is the unweighted fiber-splitting map.
The normalized potential is \(\mathcal U(\sqrt D r)\). Thus the two
multiplication factors and the source in (13) are correct. With the
conjugate-linear-first convention,
\[
\widehat R(u_h^{(0)},r)
 =\langle\mathcal U b_h,\mathcal U(\sqrt D r)\rangle=F_h(r),
\qquad
\Gamma_R[h]=\langle\mathcal U b_h,(I-A)^{-1}\mathcal U b_h\rangle.
\]
The inverse maps into the weighted energy space. It is not claimed to be
a bounded inverse on unweighted potential \(L^2\). The path entries are
nonnegative; odd powers of \(A\) need not individually be positive
semidefinite.

Since \(\int D<\infty\), the constant is in the actual core closure.
Testing it in the Riesz equation gives \(\int wu_h^{(0)}=0\), so this
potential also represents the quotient \(R\)-inverse.

## Full-domain correction identity

A pole-centered \(P\)-Cauchy sequence is \(R\)-Cauchy, hence converges in
\(L^2(Ddx)\). A pointwise convergent subsequence identifies its continuous
edge limits by Fubini and its countably many translated prime-edge limits
by removal of the corresponding null sets. Thus the centered embedding
into the \(R\)-completion is faithful and preserves the components of
\(G=P-R\). The full \(P\)-potential and the reference potential can be
compared in that common space.

Their complex Riesz pairings satisfy
\[
R(u_h^{(0)},u_h)=F_h(u_h)=P[u_h]=\Gamma_P[h]\in\mathbb R.
\]
Expansion of the \(R\)-square therefore proves exactly
\[
\Gamma_R[h]-\Gamma_P[h]=G[u_h]+R[u_h^{(0)}-u_h]\ge0
\quad(h\in K_N).
\]
All remaining forward prime powers are retained in \(G\). This establishes
the correction identity on every current, but gives no lower bound for
that correction sufficient to prove \(\Gamma_P[h]\le\|h\|_N^2\).
The reference gap \(1-\rho\) is internal to \(\widehat R\); it implies
neither contraction of the original \(T\) nor \(P\ge N\). The full
critical sign and RH remain unproved.
