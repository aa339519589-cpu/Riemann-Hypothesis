# Independent audit of the fifth-round even zero/inertia correspondence

The exact distinct-quartet count below is already stated in
[Round 5, §7, Theorem 7.1](../../rounds/05/REPORT-pages-06-10.txt). This note
checks that inherited result against the original even form and gives an
alternative compact-source proof of its lower bound. It also spells out the
tail and form-domain steps in the report's exact zero-division construction.
The audit passes under the cited original-form and explicit-formula inputs;
it supplies no zero exclusion.

Let
\[
 \widehat f(z)=F_f(z):=\int_{\mathbb R} f(x)e^{izx}\,dx
\]
denote the entire Fourier transform with the convention used in the
[original form foundation](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md)
and the [even pole-free Weil criterion](EVEN_WEIL_CRITERION.md). Consider the
real source class
\[
 \mathscr D_{e,0}=\left\{f\in C_c^\infty(\mathbb R;\mathbb R):
 f(-x)=f(x),\quad \widehat f(i/2)=\widehat f(-i/2)=0\right\}.
\]
Let \(\mathcal H_e=L^2(\mathbb R)_{\rm even}\), \(H_e=H|_{\mathcal H_e}\),
and let \(e_0\) be the normalized even ground state, \(H_e e_0=-e_0/2\).
Write \(\mathcal O_{\rm off}\) for the set of distinct off-critical zero
quartets of \(\Xi\), with a representative \(z=\gamma-i\beta\),
\(\gamma,\beta>0\), for each orbit under \(z\mapsto-z\) and conjugation.
The zeros lie in \(|\operatorname{Im}z|<1/2\), and the theta integral gives
\(\Xi(iy)>0\) for \(|y|<1/2\), so an off-critical zero has both coordinates
nonzero and admits such a representative.
Let \(j_z\) be the common multiplicity of the four zeros in that quartet,
and set \(N_{\rm off}=\#\mathcal O_{\rm off}\), counting distinct quartets
once, regardless of \(j_z\).

**Audited statement (Round 5 Theorem 7.1).** The negative index of the
compact pole-free Weil form and of the completed original even
ground-perpendicular form is exactly
\[
 \boxed{\quad
 \operatorname{ind}_-(Q_W|_{\mathscr D_{e,0}})
 =\operatorname{ind}_-\!\left(
   \mathfrak h_{H_e}\big|_{\mathcal D(\mathfrak h_{H_e})\cap e_0^\perp}
   \right)
 =\dim\operatorname{Ran}\mathbf1_{(-\infty,0)}
   (H_e|_{e_0^\perp})
 =N_{\rm off}.\quad}
\]
The form index is the supremum of dimensions of strictly negative
subspaces. The spectral dimension is over the complex Hilbert space; it
equals the real form index since \(H_e\) has real coefficients. Thus one
off-critical quartet gives one negative eigenvalue multiplicity, not
infinitely many. A zero multiplicity \(j_z\) scales that quartet's
coefficient but does not add directions. On the full even space
\(\mathcal H_e\), the ground line adds one negative direction, so the
negative index is \(1+N_{\rm off}\).

Under the unitary source map in the [original form foundation](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md), the energy operator is
\(U L_+U^{-1}=H_e+\tfrac12\). Thus the spectral count in this statement is
exactly the total multiplicity of \(L_+\)-eigenvalues in \((0,\tfrac12)\)
from Round 5 Theorem 7.1; the zero eigenvalue of \(L_+\) is the removed
ground line.

## The quartet signature

For real even \(f\), the transform satisfies
\(\widehat f(-z)=\widehat f(z)\) and
\(\widehat f(\bar z)=\overline{\widehat f(z)}\). The audited compact-source
identity is
\[
 Q_W(f)=\sum_{w\in Z_\Xi}j_w\widehat f(w)^2,\qquad
 Q_W(f)=\mathfrak h_{H_e}[f/m]\quad(f\in\mathscr D_{e,0}),
\]
with an absolutely convergent sum over all zeros and their actual
multiplicities. Grouping the critical pairs and off-critical quartets gives
\[
 Q_W(f)=2\sum_{\substack{\gamma>0\\\Xi(\gamma)=0}}
       j_\gamma\widehat f(\gamma)^2
       +4\sum_{z=\gamma-i\beta\in\mathcal O_{\rm off}}
       j_z\operatorname{Re}\bigl(\widehat f(z)^2\bigr)
\]
\[
 \phantom{Q_W(f)}
 =2\sum_{\gamma>0}j_\gamma\widehat f(\gamma)^2
  +4\sum_{z=\gamma-i\beta\in\mathcal O_{\rm off}}
       j_z\left((\operatorname{Re}\widehat f(z))^2
                    -(\operatorname{Im}\widehat f(z))^2\right).
\]
Each distinct off-critical quartet has one negative real evaluation
coordinate, \(\operatorname{Im}\widehat f(z)\), and one positive coordinate.
Repeating the same evaluation \(j_z\) times changes the weight, not the
dimension of its negative coordinate.

If \(M=\#\mathcal O_{\rm off}<\infty\), the map
\[
 f\longmapsto\left(\operatorname{Im}\widehat f(z)\right)_
      {z\in\mathcal O_{\rm off}}\in\mathbb R^M
\]
has a nonzero kernel on every subspace of dimension greater than \(M\).
Every summand in the grouped expression is nonnegative on that kernel.
Therefore the compact-source negative index is at most \(M\).

## Simultaneous negative directions and the full zero tail

For the matching lower bound, fix any finite set
\(S=\{z_1,\ldots,z_d\}\) of distinct off-critical quartets. The interpolation
lemma in the [even pole-free criterion](EVEN_WEIL_CRITERION.md) gives a real
even \(f_0\in C_c^\infty(\mathbb R)\) such that
\[
 \widehat f_0(z_r)=\widehat f_0(\bar z_r)=1\quad(1\le r\le d),\qquad
 \widehat f_0(i/2)=\widehat f_0(-i/2)=0.
\]
On the zero strip, \(\widehat f_0\) decays faster than every power as
\(|\operatorname{Re}w|\to\infty\). Since the zeros are discrete, only
finitely many zero classes modulo sign, other than the selected quartets,
have \(|\widehat f_0(w)|\ge1/2\). Call these the exceptional classes.

For each \(r\), interpolate a real even compact-smooth function \(k_r\),
with transform \(K_r\), to satisfy
\[
 K_r(z_r)=i,\qquad K_r(\bar z_r)=-i,
\]
and to vanish at both poles, every other selected quartet, and every
exceptional zero class. These data respect conjugation and evenness. For
\(N\ge1\), set \(f_{r,N}=f_0^{*N}*k_r\); then
\(\widehat f_{r,N}=\widehat f_0^{\,N}K_r\) and
\(f_{r,N}\in\mathscr D_{e,0}\). The selected quartet \(r\) contributes
\(-4j_{z_r}\), while every other selected quartet contributes zero.

The rest of the zero sum is controlled in full. Rapid strip decay of \(K_r\)
and the zero-counting bound with multiplicity imply
\[
 C_r:=\sum_{w\in Z_\Xi}j_w|K_r(w)|^2<\infty.
\]
At every remaining zero either \(K_r(w)=0\), or
\(|\widehat f_0(w)|<1/2\). Thus
\[
 \left|\sum_{w\notin\text{target quartet }r}
       j_w\widehat f_{r,N}(w)^2\right|
 \le4^{-N}C_r .
\]
Let \(T\) be the union of the \(d\) selected quartets. The interpolation data
make every selected-quartet cross term vanish, except for the matching
diagonal target. For the polarized form, the remaining off-target cross
term for \(r,s\) is bounded by
\[
 4^{-N}\sum_{w\in Z_\Xi\setminus T}j_w|K_r(w)K_s(w)|,
\]
which is finite by Cauchy--Schwarz. Hence the Weil-form matrix on
\(\{f_{r,N}\}_{r=1}^d\) is
\[
 \left(Q_W(f_{r,N},f_{s,N})\right)_{r,s=1}^d
 =\operatorname{diag}(-4j_{z_1},\ldots,-4j_{z_d})+R_N,
 \qquad \|R_N\|\longrightarrow0.
\]
It is negative definite for sufficiently large \(N\). Therefore any \(d\)
distinct off-critical quartets produce a \(d\)-dimensional negative subspace
of the compact pole-free source class. This proves the lower bound for every
finite \(d\); together with the upper bound when \(N_{\rm off}\) is finite,
it gives the stated exact compact-source index.

## Check of the inherited exact zero-division construction

Round 5 also gives a different lower-bound witness that annihilates the
entire unselected zero set exactly. For a finite selection
\(w_i=\gamma_i+i\delta_i\), \(\gamma_i,\delta_i>0\), with multiplicity
\(m_i\), it sets
\[
 P_i(z)=\bigl[(z^2-w_i^2)(z^2-\bar w_i^{\,2})\bigr]^{m_i},
 \qquad E_i(z)=\Xi(z)/P_i(z).
\]
The quotient is entire, real and even, and has nonzero value at \(w_i\).
Since \(\operatorname{Im}(w_i^2)=2\gamma_i\delta_i\ne0\), real
\(a_i,b_i\) can be chosen so that
\[
 F_i(z)=E_i(z)(z^2+1/4)(a_i+b_i z^2),\qquad F_i(w_i)=i.
\]
Here \(E_i(w_i)(w_i^2+1/4)\ne0\): the selected zero has nonzero
\(\operatorname{Im}(w_i^2)\), and \(\Xi(\pm i/2)=\xi(0)=\xi(1)=1/2\).
The factor \(z^2+1/4\) kills both pole evaluations. \(F_i\) vanishes at
every zero outside the selected quartet, and at every other selected
quartet's zeros. Hence the zero-side form on these sources is exactly
\(Q_W(f_i)=-4m_i\) and \(Q_W(f_i,f_j)=0\) for \(i\ne j\), provided the
inverse transforms belong to the original form domain and the full Weil
identity passes to them.

Let \(f_i\) denote the inverse Fourier transform of \(F_i\). The quotient
has no real poles, and \(\Xi\) is Schwartz on the real axis, so \(F_i\) is
Schwartz there. The following division argument gives the stronger
double-exponential tail needed for the weighted original form domain.

The needed inverse-transform operation is division by one linear zero. If
\(\widehat f(w)=0\), define
\[
 g(x)=i e^{-iwx}\int_x^\infty e^{iwu}f(u)\,du
     =-i e^{-iwx}\int_{-\infty}^x e^{iwu}f(u)\,du .
\]
The equality uses the zero condition. Direct differentiation gives
\(ig'-wg=f\), so Fourier transformation yields
\(\widehat g(z)=\widehat f(z)/(z-w)\), first on the real axis and then
everywhere by analytic continuation. The two integral representations are
important: the first controls the positive tail and the second the negative
tail.

For each fixed derivative order and each \(\kappa<\pi\), the theta series
gives bounds of the form
\[
 |\Phi^{(r)}(x)|\le C_{r,\kappa}e^{A_{r,\kappa}|x|}
                       e^{-\kappa e^{2|x|}}.
\]
If \(f\) has such bounds and \(|\operatorname{Im}w|<1/2\), the factors
\(e^{-iwx}\) add only ordinary exponential growth. Estimating the relevant
half-line integral at each endpoint therefore preserves every fixed
\(\kappa<\pi\); the equation \(g'=-i(f+wg)\) gives the same conclusion for
all fixed derivatives. Repeating this operation finitely many times divides
by all roots of \(P_i\), with their full multiplicities. Multiplication by
\((z^2+1/4)(a_i+b_i z^2)\) differentiates the source only finitely many
times and preserves the same tail bounds. Because the final transform
\(F_i\) is real even, Fourier uniqueness makes its inverse source real even
as well.

Choose \(\pi/2<\kappa<\pi\). For large \(|x|\), the theta lower bound
\(\Phi(x)\ge c e^{9|x|/2}e^{-\pi e^{2|x|}}\) implies
\[
 \|q_i\|_{L^2(\nu)}^2
 =\int_{\mathbb R}|f_i(x)|^2\frac{2h(x)}{\Phi(x)}\,dx<\infty,
\]
since the leading double-exponential factor is
\(e^{-(2\kappa-\pi)e^{2|x|}}\). The pole zeros give
\(\nu(f_i/\Phi)=0\).

To place \(q_i=f_i/\Phi\) in the closed original energy domain, take smooth
even cutoffs \(f_{i,R}=\chi_R f_i\) and \(q_{i,R}=f_{i,R}/\Phi\). They are
compact-smooth and even. The tail bounds give \(v_{i,R}=f_{i,R}/m\to v_i=f_i/m\) in physical \(L^2\), and \(f_{i,R}\to f_i\) in \(H^1\). Since \(b(t)\le C(1+t^2)\),
\[
 q_b[f_{i,R}-f_{i,S}]\le C\|f_{i,R}-f_{i,S}\|_{H^1}^2\longrightarrow0.
\]
The complete physical prime perturbation \(V\) is bounded, so
\[
 |\langle v_{i,R}-v_{i,S},V(v_{i,R}-v_{i,S})\rangle|
 \le\|V\|\,\|v_{i,R}-v_{i,S}\|_2^2\longrightarrow0.
\]
Thus the cutoff sequence is Cauchy in the original shifted form norm. The closed form places \(v_i\) in its actual domain, and the unitary map places \(q_i=f_i/\Phi\) in the maximal energy domain. This proves the compressed form-domain step of the inherited zero-division argument directly from the Gamma form and the complete bounded prime perturbation.

Finally, the same bounds hold uniformly for all fixed derivatives of
\(f_{i,R}\), including cutoff terms. Integration by parts therefore gives,
for every \(N\), a uniform bound
\[
 |\widehat f_{i,R}(t+i\eta)|\le C_N(1+|t|)^{-N},
 \qquad |\eta|\le1/2.
\]
The zero-counting estimate with multiplicity,
\(\#\{w:|\operatorname{Re}w|\le T\}=O(T\log(2+T))\), makes
\(\sum_w j_w(1+|\operatorname{Re}w|)^{-2N}\) finite for \(N>1\), by
dyadic summation.
Dominated convergence thus passes the complete Weil zero sum through these
cutoffs. The exact-zeroing argument is valid on the original completion;
it does not rely on a finite zero truncation or on a formal quotient alone.

## Completion and negative spectrum

For \(f\in\mathscr D_{e,0}\), the source vector \(v=f/m\) is compact smooth,
belongs to \(e_0^\perp\), and satisfies \(Q_W(f)=\mathfrak h_{H_e}[v]\).
The even pole-free criterion proves that these vectors are form-dense in the
entire original even ground-perpendicular form domain. Finite-dimensional
strict negativity is preserved under form-norm approximation, so passage to
the completion does not change the index.

The [negative-spectrum audit](NEGATIVE_SPECTRUM.md) proves that
\(\mathbf1_{[-1/2,-\kappa]}(H_e|_{e_0^\perp})\) has finite rank for each
\(\kappa>0\), all negative spectrum is pure point with finite multiplicity
away from zero, and \((-H_e)_+\) is compact. The spectral theorem identifies
the negative form index with the total multiplicity of the negative
spectrum, proving the remaining equality in the theorem.

If \(N_{\rm off}=\infty\), the negative index is infinite despite finite
rank at every fixed negative depth. To see the compatibility directly, fix
\(\kappa>0\) and take a \(d\)-dimensional negative subspace with
\(d>\operatorname{rank}\mathbf1_{[-1/2,-\kappa]}(H_e|_{e_0^\perp})\). It
contains a nonzero vector \(v\) orthogonal to that spectral band. Its
spectral support lies in \((-\kappa,\infty)\), since the operator is bounded
below by \(-1/2\). Therefore its Rayleigh quotient is strictly greater than
\(-\kappa\). The subspace is strictly negative, so the quotient is also
strictly less than zero. This constructs negative Rayleigh quotients in
\((-\kappa,0)\) for every \(\kappa>0\), as expected for a compact negative
part with infinitely many negative eigenvalue multiplicities accumulating
only at zero.

If \(N_{\rm off}=M<\infty\), the ground-perpendicular space has exactly
\(M\) negative eigenvalue multiplicities, separated from zero. In particular,
one off-critical quartet forces a negative direction but does not by itself
force infinitely many. Infinitude of the ground-perpendicular negative index
is equivalent to infinitude of distinct off-critical quartets.

The [signed zero-pairing report](../20261013_supercritical_source_tails/SIGNED_ZERO_PAIRING.md)
groups an odd generalized-source identity into the same critical pairs and
off-critical quartets, with coefficient
\(-4j_z\operatorname{Re}(G(z)^2)\). The even form here has coefficient
\(+4j_z\operatorname{Re}(\widehat f(z)^2)\), so the negative coordinate is
the imaginary evaluation in the even case and the real evaluation in that
odd identity. This checks the orbit signatures while keeping the two
operators and parities distinct.

This theorem is conditional on the actual zero set and proves no zero
exclusion. \(N_{\rm off}=0\) is equivalent to RH and, by the pole-free Weil
criterion, to nonnegativity of the original even ground-perpendicular form.
The theorem does not determine whether \(N_{\rm off}\) is zero, finite, or
infinite.

The two independent checks of the orbit signs, full-tail interpolation and original-domain passage are recorded in [the joint inertia review](INERTIA_REFEREE.md). The odd and Green total-count interface is proved in [ODD_GREEN_INERTIA.md](ODD_GREEN_INERTIA.md).
