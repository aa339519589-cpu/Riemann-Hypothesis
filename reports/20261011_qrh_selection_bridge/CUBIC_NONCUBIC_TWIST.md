# Primitive noncubic twists of the cubic Gauss series

## Result and scope

For the normalized cubic Gauss Dirichlet series

\[
R_\phi(s)=\sum_{c\equiv1\ (3)}\frac{\widetilde g(c)\phi(c)}{N(c)^s},
\]
Assume \(r\in\mathbb Z[\omega]\) is primary, \(r\equiv1\pmod3\), and \((r,3)=1\), and let \(\phi\) be a **primitive residue (Dirichlet) character modulo the ideal \((r)\)**, extended by zero on nonunits. If \(\phi^3\) is nonprincipal as a residue character, then the candidate pole at \(s=5/6\) is absent. More is true: \(R_\phi(s)\) continues holomorphically to the full half-plane \(\Re s>1/2\), and the unnormalized series continues holomorphically to \(\Re s>1\). This follows from Dunn–Radziwiłł, arXiv:2109.07463v3, Proposition 5.1, by evaluating its finite transform \(\widetilde\phi(0)\), together with a direct coefficient factorization of their \(\mathcal D\)-series. The cancellation is an explicit finite-character orthogonality calculation, not an inference from \(\phi^3\ne1\) alone. Here “primitive” refers only to the residue character modulo \((r)\); we do not identify its associated character on primary generators with an ideal Hecke character of conductor \((r)\), since primary normalization can introduce \(\lambda\)-power ramification.

In particular, this proves the absence of the \(5/6\) pole for the pure norm-character twist \(\phi=\psi_{-1}=\chi_4\circ N\) modulo \(r=4\), and also for its product with fixed cubic residue characters whose exact moduli are good (prime to 6). The cubic factor \(\theta_w(4)=(w/4)_3^2=\overline{(w/4)_3}\), when present as a fixed residue character modulo 4, is covered as well. The finite-hole extension below covers fixed common masks coprime to \(3r\). Since \(g(c)=|c|\widetilde g(c)\), the corresponding unnormalized series has no pole at \(s=4/3\).

This does **not** by itself settle any actual row whose combined multiplier contains a cubic ray character at the ramified prime \(\lambda\mid3\). Dunn–Radziwiłł's Proposition 5.1 assumes a modulus \(r\equiv1\pmod3\), hence \((r,3)=1\); that local-at-3 component needs a separate treatment or cancellation in the exact row bookkeeping. Nor does this result evaluate a full ordered two-residue expression after summing other masks.

## Fixed input and conventions

Let phi be a primitive multiplicative residue character modulo rO, extended by zero outside its unit group, with the primary generator r congruent to 1 modulo 3. Primitivity refers to this residue presentation; it does not assert that the induced character on primary ideals has primitive Hecke conductor r. The partial L-function below omits primes dividing 3r.

We use the unconditional periodic-transform construction, Proposition 5.1, and Lemma 5.3 of [Dunn–Radziwill, Section 5](https://arxiv.org/html/2109.07463v3). The finite transform is their general definition (5.22)–(5.23), equivalently (5.42). The coefficient identities needed below are (5.7), (5.17), and (5.24). Their cubic-only Lemma 5.4 is not applied to a noncubic character: the direct factorization retains the factor phi cubed.

## Exact coefficient factorization for a general multiplicative twist

Let \(\phi\) be multiplicative modulo \(r\), with \((r,3)=1\), and extend it by zero on nonunits. For \(\Re s>1\), insert \(\mu=\lambda^{-3}ef^3\) into the source's \(\mathcal D\)-series. Since \(N(\lambda)=3\), \(N(\mu)=N(e)N(f)^3/27\), and \(\lambda^4\mu=\lambda ef^3\), multiplicativity gives

\[
\begin{aligned}
\mathcal D(s,\overline F_1;\phi)_S
&=\sum_{e,f\equiv1(3)}
 \frac{3^{5/2}\widetilde g(e)|f|\,\phi(\lambda ef^3)}
      {(N(e)N(f)^3/27)^s}\\
&=3^{5/2+3s}\phi(\lambda)
 \left(\sum_{e\equiv1(3)}\frac{\widetilde g(e)\phi(e)}{N(e)^s}\right)
 \left(\sum_{f\equiv1(3)}\frac{\phi(f)^3}{N(f)^{3s-1/2}}\right)\\
&=3^{5/2+3s}\phi(\lambda) R_\phi(s)
 L_{(3r)}(3s-\tfrac12,\phi^3).
\end{aligned}
\]

Equivalently,
\[
\boxed{\ \mathcal D(s,\overline F_1;\phi)_S
 =3^{5/2+3s}\phi(\lambda)R_\phi(s)L_{(3r)}(3s-\tfrac12,\phi^3).\ }
\]
The \(e\)-sum may be over all primary \(e\) because \(\widetilde g(e)=0\) off squarefree moduli. The \(f\)-sum is the partial Hecke \(L\)-series \(L_{(3r)}(t,\phi^3)\): primary generators omit the factor at \(\lambda\mid3\), and the zero extension of \(\phi\) omits primes dividing \(r\). Its Euler product is holomorphic and nonzero for \(\Re t>1\), so \(L_{(3r)}(3s-\tfrac12,\phi^3)\) is holomorphic and nonzero throughout \(\Re s>1/2\). Also \(\phi(\lambda)\ne0\) because \((r,3)=1\). This is a statement about the partial Hecke \(L\)-series attached to the values of the residue character on primary generators; no conductor identification at \(\lambda\) is needed. For the pure norm character,
\[
\psi_{-1}(\lambda)=\chi_4(N\lambda)=\chi_4(3)=-1,
\]
so the explicit scalar is nonzero. Since \(\mathcal D\) is entire and the remaining factors have no zeros or poles for \(\Re s>1/2\),
\[
R_\phi(s)=\frac{\mathcal D(s,\overline F_1;\phi)_S}
 {3^{5/2+3s}\phi(\lambda)L_{(3r)}(3s-\tfrac12,\phi^3)}
\]
is holomorphic throughout \(\Re s>1/2\). It agrees with the original Dirichlet series on \(\Re s>1\), where the factorization was derived, so this is its analytic continuation.

## The finite-transform residue vanishes

Write \(\rho_r(d)=(d/r)_3\), a character of order dividing 3 on \((\mathcal O/r)^\times\). From the general transform (5.22)–(5.23), equivalently (5.42), for \(u=0\) and \(ad\equiv\overline{\lambda^8}\pmod r\),

\[
\widetilde\phi(0)
=C_{r,\lambda}\sum_{d\in(\mathcal O/r)^\times}
  \widehat\phi(d)\,\overline{\rho_r(d)},
\qquad C_{r,\lambda}=\Big(\frac{\lambda^{-4}}r\Big)_3\ne0.
\]

For a primitive multiplicative character, substitution \(y=dx\) in (5.21) gives
\(\widehat\phi(d)=\overline{\phi(d)}\widehat\phi(1)\) for every unit \(d\), with \(\widehat\phi(1)\ne0\); primitivity gives support only on units. Consequently

\[
\widetilde\phi(0)=C_{r,\lambda}\widehat\phi(1)
 \sum_{d\in(\mathcal O/r)^\times}\overline{(\phi\rho_r)(d)}.
\]

The last sum is zero unless \(\phi\rho_r\) is principal. But \(\rho_r^3=1\), so \(\phi\rho_r=1\) would imply \(\phi^3=1\). Therefore, when \(\phi^3\) is nonprincipal, \(\widetilde\phi(0)=0\). This is the precise finite orthogonality responsible for the pole cancellation. 

Proposition 5.1 leaves only the possible simple pole at \(5/6\) in the completed series \(\Lambda(s,\overline F_1;\phi)_S\); its residue is a constant times \(\widetilde\phi(0)\). The vanishing just proved makes that pole removable, so \(\Lambda\) is entire. Lemma 5.3 gives
\[
 \mathcal D(s,\overline F_1;\phi)_S
 =4(2\pi)^{2s}
   \frac{\Lambda(s,\overline F_1;\phi)_S}
        {\Gamma(s-1/6)\Gamma(s+1/6)}.
\]
The reciprocal Gamma functions are entire. Thus \(\mathcal D\) is entire, which supplies the numerator used in the half-plane quotient above. The series is supported on the nonzero Fourier indices in \(S\); there is no additional independent constant-term pole.

For \(\phi=\psi_{-1}\), the residue-character conductor is exactly \((4)\): it is nontrivial on the principal-unit kernel modulo 2 (for instance, \(1+2\omega\equiv1\pmod2\) but \(\psi_{-1}(1+2\omega)=-1\)). It is also nonprincipal on primary generators: CRT gives \(c=1-6\omega\equiv1\pmod3\), \(c\equiv\lambda\pmod4\), and \(\psi_{-1}(c)=\chi_4(43)=-1\). The fixed cubic factor \((\cdot/4)_3\) has cube 1; its product with \(\psi_{-1}\) is still primitive modulo 4, since an order-two character on the mod-2 principal-unit kernel cannot be canceled by a character with values in the cube roots of unity. It also leaves the cube nonprincipal.

## Fixed finite common holes

Let \(M\) be a fixed ideal coprime to \((3r)\), and define
\[
R_{\phi,M}(s)=\sum_{\substack{c\equiv1\ (3)\\(c,M)=1}}
 \frac{\widetilde g(c)\phi(c)}{N(c)^s}.
\]
Let \(M_0=\operatorname{rad}(M)\), and choose primary generators for its squarefree ideal divisors \(d\mid M_0\). Put \(\chi_d(c)=(c/d)_3\), extended by zero when \((c,d)>1\); \(\chi_1=1\). The exact inclusion–exclusion and CRT identity are
\[
\boxed{\quad
R_{\phi,M}(s)=\sum_{d\mid M_0}\mu(d)\,
 \widetilde g(d)\phi(d)N(d)^{-s}
 R_{\phi\overline{\chi_d}}(s).
\quad}
\]
Indeed, \(\widetilde g(c)=0\) unless \(c\) is squarefree. On the term \(d\mid c\), write \(c=dc_0\), where \((d,c_0)=1\) and both factors are primary. Dunn–Radziwiłł (2.3), followed by cubic reciprocity (1.4), gives
\[
\widetilde g(dc_0)
=\overline{\Big(\frac d{c_0}\Big)_3}\widetilde g(d)\widetilde g(c_0)
=\overline{\Big(\frac {c_0}d\Big)_3}\widetilde g(d)\widetilde g(c_0).
\]
The zero extension of \(\chi_d\) sets the inner terms with \((c_0,d)>1\) to zero, so the inner sum is exactly \(R_{\phi\bar\chi_d}(s)\), with no extra coprimality condition to impose.

For squarefree \(d\), \(\chi_d\) is a primitive residue character modulo \((d)\): each prime factor \(\mathfrak p\nmid3\) contributes the nontrivial cubic character of \((\mathcal O/\mathfrak p)^\times\), whose order-three part exists because \(N\mathfrak p\equiv1\pmod3\). Since \((d,r)=1\), the product \(\phi\bar\chi_d\) is primitive as a residue character modulo \((rd)\), with \(rd\equiv1\pmod3\). On the unit group modulo \((rd)\), its cube is the inflation of \(\phi^3\); with zero extensions, it is \(\phi^3\) times the principal zero-extended character modulo \((d)\). In either convention it is nonprincipal, because its restriction to the \((r)\)-component is \(\phi^3\ne1\):
\[
 (\phi\bar\chi_d)^3\ne1.
\]
The main theorem above therefore applies termwise and proves \(R_{\phi,M}(s)\) holomorphic for \(\Re s>1/2\). For the conjugated coefficient define \(R^{\mathrm{conj}}_\phi(s)=\sum_c\overline{\widetilde g(c)}\phi(c)N(c)^{-s}=\overline{R_{\bar\phi}(\bar s)}\). It is holomorphic in the same half-plane. Its finite-hole formula has coefficient \(\mu(d)\overline{\widetilde g(d)}\phi(d)N(d)^{-s}\) and residual series \(R^{\mathrm{conj}}_{\phi\chi_d}(s)\). The residual residue character is likewise primitive modulo \((rd)\), and its cube is nonprincipal by the same restriction argument. The sum over \(d\mid M_0\) is finite. No bound uniform in \(M\), height, or the varying modulus \((rd)\) follows from this argument.

If a finite mask includes primes dividing \((3r)\), those factors can be removed from \(M_0\): divisors of \(r\) are already excluded by the zero extension of \(\phi\), and primary \(c\equiv1\pmod3\) are already coprime to \(\lambda\mid3\).

## Pole-location conversion

Since \(g(c)=|c|\widetilde g(c)=N(c)^{1/2}\widetilde g(c)\),
\[
\sum_c\frac{g(c)\phi(c)}{N(c)^s}=R_\phi(s-\tfrac12).
\]
Thus the normalized candidate at \(5/6\) corresponds to the unnormalized candidate at \(4/3\). More strongly, the continuation of \(R_\phi\) to \(\Re s>1/2\) gives a holomorphic continuation of the unnormalized series to \(\Re s>1\), hence removes its \(4/3\) candidate for the stated moduli/twists.

## Exact limitation for the row

The modulus in this proof is prime to 3. It covers the primitive quadratic norm residue character modulo 4 and products with fixed cubic residue characters of good modulus. It does not cover an additional \(\lambda\)-power ray dependence on primary \(c\) that cannot be represented by a residue character modulo some \((r)\) coprime to 3; such a component requires a separate level-at-3 calculation or an exact cancellation in the CRT bookkeeping. In particular, apply the conclusion to the actual \(\varepsilon=-1\) first-polar row only after verifying that its **combined** multiplier, including \(\theta_w(4)\), \(\overline{\theta_w(\kappa)}\), the additive-character conversion, and zero extensions, is represented by a primitive residue character modulo a good \((r)\). The continuation is qualitative and gives no height- or conductor-uniform bounds by itself. This result says nothing about the other polar term or the RH conclusion.


## Unit-minus local interface

The frequency unit epsilon=-1 introduces the finite character psi(t)=chi_t(-1)=chi_4(Nt) on the good primary s-column. Its primitive residue modulus is (4)=(2)^2, of ideal norm 16. For u=a+b omega its zero extension is zero for even a^2-ab+b^2, +1 for norm 1 modulo 4, and -1 for norm 3 modulo 4. It is primitive because 1+2 omega is congruent to 1 modulo 2 but has character value -1.

With the original additive character e(z)=exp(2 pi i [omega]z), the exact transform is

    sum_(u mod 4) psi(u) e(hu/4) = 4 psi(h).

For the literal trace character check_e of Dunn–Radziwill, the corresponding value is -4 psi(h), since check_e(z)=e(lambda z) and psi(lambda)=-1. Both transforms vanish exactly at the four nonunit residue classes and have primitive support at the remaining twelve classes. The companion [check_cubic_noncubic_twist.py](check_cubic_noncubic_twist.py) verifies these identities and the cubic finite projections with exact integer arithmetic.

For good primary squarefree w with (w,6)=1, theta_w=chi_w^2, define gamma_o(w)=q_w^(-1/2) sum_(x mod w) theta_w(x)e(x/w). The CRT formula in the original convention is

    G_(psi theta_w)(4w,h)
      =4 sqrt(q_w) gamma_o(w) psi(h) psi(w) theta_w(4) conjugate(theta_w(h))

when h is a unit modulo 4w, and zero otherwise. Thus the primal mask branch divisible by (2) is redundant because psi vanishes there, while the dual (2)-valuation must be zero. The row factors psi(w) and theta_w(4) remain; neither is discarded from the signed residue calculation.

If xi_pi^2=theta_pi^j at the norm-four prime, j=1 or 2, the new cubic CRT factor theta_w(4)=xi_pi(w)^j combines with the pre-existing xi_pi(w) to give xi_pi(w)^(j+1). This is conjugate(xi_pi(w)) for j=1 and 1 for j=2. The quadratic factor psi(w) still remains in both cases.

The general theorem applies to this noncubic factor and any fixed cubic residue factor representable modulo a modulus prime to 3, including the modulo-4 factor just displayed and fixed common holes. It does not remove additional lambda-ray factors or justify reusing the unit-one bad-prime matrix for every frequency unit. A full unit-minus polar assertion still requires that remaining local-at-3 interface and the full coupled column bookkeeping.

The independent mathematical review is [REFEREE_CUBIC_NONCUBIC_TWIST.md](REFEREE_CUBIC_NONCUBIC_TWIST.md). The original first-Poisson conventions and restricted unit-one two-polar theorem remain those of [QUADRATIC_DUAL_N1, Parts I and XXI](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/92d2d98d4a24d1f2885e72ad0b2d258b93540495/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md). No full-probe estimate or RH conclusion is asserted here.
