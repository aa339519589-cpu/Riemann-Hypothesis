# Odd pole-inclusive inertia and the off-critical zero count

## Result and relation to existing reports

Let \(Z_\Xi\) be the set of distinct zeros of
\(\Xi(z)=\xi(\tfrac12+iz)\), with actual multiplicity \(j_z\) attached, and
let \(N_{\rm off}\) be the number of distinct off-critical quartets
\(\{\pm z,\pm\bar z\}\), counted once regardless of common multiplicity
\(j_z\). Define the odd physical restriction
\[
 H_o=H|_{L^2(\mathbb R)_{\rm odd}},\qquad
 s(x)=m(x)\sinh(x/2),\qquad
 \mathcal A_o=H_o-2|s\rangle\langle s|.
\]
The rank-one subtraction is the pole-inclusive odd form in the
[Green-interface report](../20261013_green_spectral_interfaces/REPORT.md)
and the [signed zero-pairing report](../20261013_supercritical_source_tails/SIGNED_ZERO_PAIRING.md).
Let \(K=TT^*\) be the bounded Green operator of the Green-interface report.
Then
\[
 \boxed{\quad
 \operatorname{ind}_-(\mathfrak a_o|_{C_c^\infty(\mathbb R)_{\rm odd},\,\mathbb R})
 =\operatorname{ind}_-(\mathcal A_o)
 =\operatorname{rank}\mathbf1_{(-\infty,0)}(H_o)
 =N_{\rm off}.\quad}
\]
Combining this with the established even ground-perpendicular count and
Green transfer gives
\[
 \boxed{\quad
 \operatorname{rank}\mathbf1_{(1,\infty)}(K)
 =\operatorname{ind}_-(q_{PN})
 =\operatorname{ind}_-(\mathfrak a_o)
 =\operatorname{ind}_-(\mathcal A_o)
 =\operatorname{rank}\mathbf1_{(-\infty,0)}(H_o)
 =\operatorname{ind}_-(H_e|_{e_0^\perp})
 =N_{\rm off}.\quad}
\]
The spectral ranks count eigenvalue multiplicity, whereas \(N_{\rm off}\) counts distinct quartets without repetition. The equalities hold with finite or infinite value.
Here \(H_e=H|_{L^2(\mathbb R)_{\rm even}}\) and \(e_0\) is its normalized ground vector; \(q_{PN}\) is the \(P-N\) form on the P-gradient completion. The
count is one direction per distinct quartet. Zero multiplicity scales its
form contribution but does not add independent directions.

The [independent review](INERTIA_REFEREE.md) checks this count interface. The Green report already proves the total inertia transfer
\(\operatorname{rank}\mathbf1_{(1,\infty)}(K)
=\operatorname{ind}_-(q_{PN})
=\operatorname{ind}_-(\mathcal A_o)\) in equation (25), and Round 5
Theorem 7.1 gives the even count \(N_{\rm off}\). The odd compact-source
count below supplies the zero-indexed interface between these results.
This is equality of total negative multiplicities, not an eigenvalue
correspondence or a bounded similarity between completions.

## Odd zero-orbit signature

Use the source transform
\[
 \widehat f(z)=\int_{\mathbb R}f(x)e^{izx}\,dx.
\]
For a real odd compact-smooth source,
\[
 \widehat f(-z)=-\widehat f(z),\qquad
 \widehat f(\bar z)=-\overline{\widehat f(z)}.
\]
The additive Weil identity for the pole-inclusive odd source form is
\[
 \mathfrak a_o[f/m]
 =\sum_{w\in Z_\Xi}j_w\widehat f(w)
                          \overline{\widehat f(\bar w)}
 =-\sum_{w\in Z_\Xi}j_w\widehat f(w)^2.                 \tag{1}
\]
The first equality and its convergence for compact odd sources are in the
[signed zero-pairing report](../20261013_supercritical_source_tails/SIGNED_ZERO_PAIRING.md);
the second uses real-odd symmetry. The pole term
\(-2|\int_{\mathbb R}f(x)\sinh(x/2)\,dx|^2\) is already included in
\(\mathfrak a_o\).

On a critical pair \(\{\pm\gamma\}\), \(\widehat f(\gamma)\) is purely
imaginary, so (1) contributes \(2j_\gamma|\widehat f(\gamma)|^2\ge0\).
On an off-critical quartet represented by \(z=\gamma-i\beta\), the four
terms give
\[
 -4j_z\operatorname{Re}(\widehat f(z)^2)
 =-4j_z\left((\operatorname{Re}\widehat f(z))^2
                    -(\operatorname{Im}\widehat f(z))^2\right).       \tag{2}
\]
Each distinct off-critical quartet therefore has one negative real
coordinate, \(\operatorname{Re}\widehat f(z)\), and one positive
coordinate. The even pole-free form has the opposite sign on this
two-coordinate block, with its negative coordinate imaginary.

If there are finitely many, say \(M\), off-critical quartets, the real-linear
map
\[
 f\longmapsto
 \bigl(\operatorname{Re}\widehat f(z)\bigr)_{z\in\mathcal O_{\rm off}}
 \in\mathbb R^M
\]
has a nonzero kernel on every subspace of dimension greater than \(M\).
On that kernel all terms in (2) are nonnegative, as are the critical-pair
terms. Hence the compact odd negative index is at most \(M\).

## Odd interpolation and simultaneous lower bound

Finite interpolation by compact odd tests follows from independence of the
sine kernels. Fix distinct nonzero nodes modulo \(z\sim-z\),
\(z_1,\ldots,z_r\). For a complex odd test \(g\),
\[
 \widehat g(z)=2i\int_0^\infty g(x)\sin(zx)\,dx.
\]
If a linear combination of the evaluation functionals vanished on every
compact smooth odd test, then
\(\sum_{k=1}^r c_k\sin(z_kx)=0\) for \(x>0\). Its odd derivatives at zero
of orders \(1,3,\ldots,2r-1\) give
\[
 \sum_{k=1}^r c_k z_k(z_k^2)^\ell=0,\qquad 0\le\ell<r.
\]
This is a Vandermonde system in the distinct \(z_k^2\), multiplied by
nonzero \(z_k\), so it is invertible. The complex evaluation map is onto.
For real odd sources, compatible data satisfy
\(a_{\bar z}=-\overline{a_z}\). Replacing a complex interpolant \(g\) by
\((g+\bar g)/2\) preserves such values, since
\(\widehat{\bar g}(z)=-\overline{\widehat g(\bar z)}\). On a real node the
compatible values are purely imaginary; zero is admissible. At a purely imaginary node the values are real and opposite under sign reversal. In particular the pole values at \(\pm i/2\) need not vanish: their contribution is already included in \(\mathfrak a_o\).

Fix any finite set \(S=\{z_1,\ldots,z_d\}\) of distinct off-critical
quartets. By the even interpolation lemma in the
[even pole-free criterion](../20261013_foundation_audit/EVEN_WEIL_CRITERION.md),
choose real even \(f_0\in C_c^\infty\) with
\[
 \widehat f_0(z_r)=\widehat f_0(\bar z_r)=1,\qquad 1\le r\le d.
\]
Its transform decays rapidly on the zero strip. Discreteness of the zeros
implies that only finitely many other zero classes modulo sign have
\(|\widehat f_0(w)|\ge1/2\); call these exceptional. The theta integral
gives \(\Xi(iy)>0\) for \(|y|<1/2\), so there are no zero nodes on the
imaginary axis or at zero.

For each selected \(r\), odd interpolation gives a real odd
\(k_r\in C_c^\infty\), with transform \(K_r\), satisfying
\[
 K_r(z_r)=1,\qquad K_r(\bar z_r)=-1,
\]
and vanishing at every other selected quartet and at every exceptional zero
class. These values obey \(K_r(\bar z)=-\overline{K_r(z)}\); assigning zero
on real critical classes is compatible. This is finite interpolation.

For \(N\ge1\), set \(f_{r,N}=f_0^{*N}*k_r\). Since an even function
convolved with an odd one is odd, \(f_{r,N}\) is real odd compact smooth,
and
\[
 \widehat f_{r,N}=\widehat f_0^{\,N}K_r.
\]
The target quartet has values \(1,-1,-1,1\), up to ordering. Their squares
are all \(1\), so (1) contributes exactly \(-4j_{z_r}\). Every other
selected quartet contributes zero.

Let \(T\) be the union of the selected quartets. For each \(r\),
\[
 C_r=\sum_{w\in Z_\Xi}j_w|K_r(w)|^2<\infty,
\]
by rapid strip decay and the zero count with actual multiplicities. Outside
\(T\), a nonzero \(K_r(w)\) can occur only where
\(|\widehat f_0(w)|<1/2\), so the full quadratic remainder is bounded by
\(4^{-N}C_r\). For the polarized off-target terms,
\[
 |R_{rs,N}|
 \le4^{-N}\sum_{w\in Z_\Xi\setminus T}j_w|K_r(w)K_s(w)|,
\]
and this sum is finite by Cauchy--Schwarz. All selected cross terms vanish
exactly. Thus
\[
 \bigl(\mathfrak a_o[f_{r,N}/m,f_{s,N}/m]\bigr)_{r,s=1}^d
 =-\operatorname{diag}(4j_{z_1},\ldots,4j_{z_d})+R_N,
 \qquad \|R_N\|\longrightarrow0.
\]
For sufficiently large \(N\) this matrix is negative definite. Every
finite set of \(d\) distinct off-critical quartets therefore gives \(d\)
negative directions in the compact odd source class. Arbitrary finite
subsets prove the lower bound, including when \(N_{\rm off}\) is infinite.
Together with the finite upper bound, the compact odd index is exactly
\(N_{\rm off}\).

## Passage to the physical and Green forms

For compact odd \(f\), the vector \(v=f/m\) is compact smooth odd. The exact
odd source identity in the
[Green-interface report](../20261013_green_spectral_interfaces/REPORT.md)
identifies \(\mathfrak a_o[v]\) with the \(P-N\) form on the common compact
smooth ratio core. The odd physical form core is compact smooth odd tests;
\(\mathcal A_o\) differs from \(H_o\) by a bounded rank-one operator, so
it has the same form domain and core. Finite-dimensional strict negativity
is stable under approximation in either form norm. The compact odd count
therefore equals the completed \(\mathcal A_o\) index, while the established
common-core theorem gives
\[
 \operatorname{ind}_-(q_{PN})=\operatorname{ind}_-(\mathfrak a_o).
\]
This uses equality of negative indices on a common dense core. It does not
identify the P-gradient completion with the physical Hilbert space or assume
a bounded similarity between their operators.

The rank-one splitting in the Green-interface report gives
\[
 \mathfrak h_o[v]=\tfrac18|a|^2+\mathfrak h_o[z],\qquad
 \mathfrak a_o[v]=\mathfrak h_o[z],\qquad
 v=a u_*+z,\quad z\perp s,
\]
and hence \(\operatorname{ind}_-(H_o)=\operatorname{ind}_-(\mathcal A_o)\).
Equation (25) of that report, using the polar decomposition of \(T\), then
yields
\[
 \operatorname{rank}\mathbf1_{(1,\infty)}(K)
 =\operatorname{ind}_-(q_{PN})
 =\operatorname{ind}_-(\mathfrak a_o)
 =\operatorname{rank}\mathbf1_{(-\infty,0)}(H_o)
 =N_{\rm off}.
\]
The even equality
\(\operatorname{ind}_-(H_e|_{e_0^\perp})=N_{\rm off}\) is Round 5
Theorem 7.1, with its original-form bridge audited in [the companion even note](ZERO_INERTIA.md). This supplies the cross-parity count equality. No step matches an
individual Green eigenvalue \(\lambda>1\) to an individual negative
eigenvalue of \(H_o\) or \(H_e\).

If \(N_{\rm off}=\infty\), all total counts above are infinite. This is
compatible with finite rank of every fixed negative band of \(H_o\) and
finite rank of every fixed supercritical band of \(K\): negative eigenvalues
may accumulate at zero, while Green eigenvalues above one may accumulate at
one. If \(N_{\rm off}<\infty\), each displayed total count equals that finite
number. These identities do not decide whether \(N_{\rm off}\) is zero,
finite nonzero, or infinite.
