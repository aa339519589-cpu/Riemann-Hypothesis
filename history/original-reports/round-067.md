## Round 67 — audit of the “Overdetermined Weil Systems” preprint

I audited Yifan Zhou's [*Overdetermined Weil Systems and the Riemann
Hypothesis*](https://zenodo.org/records/21218854), including the attached
[PDF](https://zenodo.org/records/21218854/files/RH%20%282%29.pdf?download=1).
The advertised contradiction is not obtained. There are several independent
breaks before the claimed linear-independence argument can be used.

### I. The stated Fourier regularization has the wrong limit

The manuscript defines
\(h_n^{\mathrm{even}}(z)=\tfrac12[\cos(z\log n)/(z\log z)+
\cos(z\log n)/((-z)\log(-z))]\). It then sets
\(\widehat h_{n,\delta}(t)=\widehat h_n^{\mathrm{even}}(t)\varphi_\delta(t)\)
with \(\varphi_\delta(t)=\delta^{-1}\varphi(t/\delta)\), where \(\varphi\) is
supported in \([-1,1]\).

This factor is a concentrating approximate identity, not a multiplier
converging to \(1\). With the manuscript's own asserted regular local
formula for \(\widehat h_n^{\mathrm{even}}\), its inverse transform satisfies
\[
h_{n,\delta}(z)=\int_{-1}^{1}\widehat h_n^{\mathrm{even}}(\delta u)
\varphi(u)e^{2\pi i\delta uz}\,du
\longrightarrow \widehat h_n^{\mathrm{even}}(0)\int_{-1}^{1}\varphi(u)\,du.
\tag{67.1}
\]

The displayed limit is independent of \(z\), not \(h_n^{\mathrm{even}}(z)\).
If the value at zero is instead treated distributionally, the claimed
pointwise convergence is even less justified. Normalizing the bump at zero
does not repair the wrong \(\delta^{-1}\varphi(t/\delta)\) scaling.

Thus the passage from the admissible \(h_{n,\delta}\) to the singular
function used in the constraint is not established. The reality constraint
\(\operatorname{Im}\sum_\rho h_n^{\mathrm{even}}(\rho)=0\) therefore does not
follow from the cited regularization.

### II. The proposed limiting test function is not analytic in the Weil strip

With the principal logarithm, the first term has a cut on
\((-\infty,0]\), while the second has a cut on \([0,\infty)\). The even sum
does not cancel these cuts. Also, near \(z=1\),
\[
\frac{\cos(z\log n)}{z\log z}
=\frac{\cos(\log n)}{z-1}+O(1),
\tag{67.2}
\]
and the second summand is finite there. Hence the proposed test has a genuine
real-axis pole at \(z=1\), with a reflected pole at \(z=-1\).

A principal-value Fourier transform of a singular function is not
automatically an admissible analytic test function for the Weil formula.
A separate extension theorem would have to specify the singular test space,
the zero-side evaluation, and continuity of the complete explicit-formula
functional. The manuscript supplies none of these. The zero terms also retain
the \(\cosh(\gamma\log n)\) growth, so they generally do not tend to zero as
\(|\gamma|\) tends to infinity; the claimed symmetric zero sum is not defined
by the stated argument.

### III. The finite linear-independence step uses a false accumulation claim

For finite \(M\), the manuscript sets \(t=\log n\) and argues that an
exponential polynomial vanishing on
\(\{\log n:n=2,3,\ldots\}\) vanishes identically because this set has
\(+\infty\) as an accumulation point. It does not: it is a discrete subset of
the real line and has no finite accumulation point. An analytic function can
vanish on an unbounded discrete set without being identically zero.

A valid replacement would require a separate theorem proving linear
independence of the particular generalized powers \(n^{\lambda_j}\), including
all exponent collisions and real-part ties. No such theorem is proved in the
paper.

For \(M=\infty\), the failure is stronger. From
\(\sum_{k=1}^{\infty}f_k(n)=0\) one cannot apply the one-pair argument to an
arbitrary summand. An infinite convergent sum can vanish through cancellation
among infinitely many terms, and no decomposition that permits removing all
other pairs is supplied. The paper's Case 3 therefore does not follow even if
the finite-\(M\) lemma were repaired.

### IV. The auxiliary spectral paragraph does not encode the zero real parts

The appendix assigns the real numbers \(E_n=\tfrac14+\gamma_n^2\) to a
self-adjoint Sturm--Liouville model. These numbers contain only the imaginary
ordinates. Self-adjointness of an operator whose spectrum has been prescribed
this way cannot force the omitted \(\operatorname{Re}\rho\) values to equal
\(1/2\). The manuscript gives no characteristic determinant or spectral
transform identifying the full complex zero set with that operator, and the
asserted \(J\)-symmetry-to-RH implication is an unsupported extra claim.

**Established:** the proposed \(f_k\)-system would be useful if an admissible
test family and a justified zero sum were first constructed.

**Failure / error:** the Fourier regularization does not converge to the
claimed test function; the limiting function is not analytic in the required
strip; the finite independence proof misuses accumulation at infinity; and
the infinite case illegally isolates one summand.

**Remaining load-bearing statement:** construct a valid Weil-admissible family
whose constraints are rigorously defined for the complete zero set, then prove
a finite and infinite-system theorem strong enough to exclude all
off-critical pairs. The preprint does not provide either statement.

**RH status:** no unconditional proof has been produced.
