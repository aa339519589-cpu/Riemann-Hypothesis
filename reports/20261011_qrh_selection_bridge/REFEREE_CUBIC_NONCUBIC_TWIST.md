# Referee check: quadratic norm twist and the first pole

## Verdict

**Accept the bounded no-pole lemma, with the stated level restriction and an explicit definition of the Hecke (L)-factor.** Dunn–Radziwiłł, arXiv:2109.07463v3, Proposition 5.1 applies to the general periodic twist in §5.3/5.4 once its Fourier transform is supported on units. A primitive finite multiplicative character modulo a primary (r\equiv1\pmod3), ((r,3)=1), has that support. The finite transform at zero is then an ordinary character sum, and it vanishes if \(\phi^3\) is nonprincipal. The direct coefficient factorization in the draft is also correct in \(\Re s>1\), and the second factor is nonzero at the candidate pole. Thus the normalized series is holomorphic at (5/6); the corresponding unnormalized series is holomorphic at (4/3).

This proves the pure norm twist \(\psi=\chi_4\circ N\) modulo \((4)\), and its product with a fixed cubic character of conductor prime to (6) (using the exact product conductor). It also proves the product with a cubic character modulo (4), provided it is treated as a multiplicative character on units modulo (4). It does **not** prove cancellation for any row whose actual combined twist contains a character at \(\lambda\mid3\), nor a full ordered residue after other masks are summed.

## Source/hypothesis check

- Proposition 5.1 assumes a periodic sequence \(\psi\pmod r\) whose finite Fourier transform is supported on classes coprime to (r); it gives a unique possible simple pole of \(\mathcal D(s,\overline{F_1};\psi)_S\) at (5/6), with residue proportional to \(\widetilde\psi(0)\). Equations (5.49)–(5.52) show the only non-entire term is the displayed multiple of \(\widetilde\psi(0)/(s-5/6)\). Lemma 5.3's gamma factor is finite and nonzero at (5/6).
- In (5.21), \(\widehat\phi(d)=\sum_{x\bmod r}\phi(x)\check e(dx/r)\). For units (d), substitution (y=dx) gives \(\widehat\phi(d)=\overline{\phi(d)}\widehat\phi(1)\). For primitive \(\phi\), the transform vanishes on nonunits; this is the standard primitive finite Gauss-sum support statement, using the perfect trace pairing since \((r,3)=1\). Thus the general-character specialization meets Corollary 5.1 and Proposition 5.1. No cubic-only hypothesis is being imported from Lemma 5.4.
- Use the **general transform (5.42)** (equivalently, definitions (5.22)–(5.23)), not the later cubic-only specialization (5.69). At \(u=0\), (5.42) imposes \(ad\equiv\lambda^{-8}\pmod r\), and its cubic factor is \((\lambda^4a/r)_3=(\lambda^{-4}d^{-1}/r)_3\). Thus, with \(\rho_r(x)=(x/r)_3\),
  \[
  \widetilde\phi(0)=\Big(\frac{\lambda^{-4}}r\Big)_3\widehat\phi(1)
       \sum_{d\in(\mathcal O/r)^\times}\overline{(\phi\rho_r)(d)}.
  \]
  The scalar is nonzero because \((r,3)=1\). The sum is zero unless \(\phi\rho_r\) is principal; that would imply \(\phi^3=1\). The conjugate convention variant gives \(\phi\bar\rho_r\) and the same implication. Equation (5.69) is only the later cubic-character specialization and is not the source for this general-twist step.
- In the source's \(\mathcal D\)-series, on \(S\) a nonzero coefficient has \(\mu=\lambda^{-3}ef^3\) and \(\overline{\tau(\mu)}=3^{5/2}\widetilde g(e)|f|\) by (5.7), (5.17), and (5.24). Therefore \(N(\mu)=N(e)N(f)^3/27\), \(\lambda^4\mu=\lambda ef^3\), and
  \[
  \mathcal D(s,\overline{F_1};\phi)_S
  =3^{5/2+3s}\phi(\lambda)R_\phi(s)\,L_{(3r)}(3s-\tfrac12,\phi^3).
  \]
  Here \(L_{(3r)}\) means the Euler product over primary prime generators away from \(3r\), with \(\phi^3\) evaluated on the unique primary generator. The (e)-sum is (R_\phi(s)), since \(\widetilde g(e)=0\) off squarefree (e); the (f)-sum is exactly this Hecke (L)-series. At (s=5/6), its argument is (2), so it is absolutely convergent and nonzero. Also \(\phi(\lambda)\ne0\) when \((r,3)=1\). Hence holomorphy of \(\mathcal D\) gives holomorphy of \(R_\phi\).

## Specialization to \(\chi_4\circ N\)

For \(r=4\), (4\equiv1\pmod3), \((4,3)=1\), and \((4)=(2)^2\) with (2) inert. The norm character is periodic modulo (4), unit-invariant because every Eisenstein unit has norm (1), and primitive: on the kernel of \((\mathcal O/4)^\times\to(\mathcal O/2)^\times\), it takes value (-1) at \(\lambda=1+2\omega\), since \(\lambda\equiv1\pmod2\) and \(N\lambda=3\). Its cube is itself and is nonprincipal. In particular \(\phi(\lambda)=-1\).

Normalization note: with the literal transform (5.21), direct enumeration gives \(\widehat\psi(1)=\sum_{x\bmod4}\chi_4(Nx)\check e(x/4)=-4\), so \(\widehat\psi(h)=-4\psi(h)\) for units (h), and zero for nonunits. If one uses the equally valid \(\lambda\)-scaled additive character \(\check e(\lambda h x/4)\), the scalar is (+4\psi(h)\), because \(\psi(\lambda)=-1\). This is only a Fourier normalization scalar; support and the vanishing argument are unchanged.

For a cubic character \(\rho\) modulo (4), \(\rho^3=1\), so \((\psi\rho)^3=\psi\). Also \(\rho\) factors through reduction modulo (2), whereas \(\psi\) is nontrivial on the kernel modulo (2); hence \(\psi\rho\) is still primitive of conductor (4). If the cubic character has conductor prime to (6), coprimality of conductors gives the primitive exact product conductor (r=4q\), whose unique primary generator satisfies (r\equiv1\pmod3\). In either case the proposition applies.

## Primary source

Dunn–Radziwiłł, [*Bias in cubic Gauss sums: Patterson’s conjecture*, arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3), especially §5.3–5.4, equations (5.7), (5.17), (5.19)–(5.24), **(5.42)**, (5.44), (5.46)–(5.52). Equation (5.69) is cubic-only and is not used for the general character argument.

## Follow-up corollary: larger holomorphy half-plane

**The half-plane corollary is valid:** for the same primitive twists \(\phi\), \(R_\phi(s)\) continues holomorphically throughout \(\Re s>1/2\), and the unnormalized series \(\sum_c g(c)\phi(c)/N(c)^u=R_\phi(u-1/2)\) is holomorphic for \(\Re u>1\). This is an unconditional continuation region; it makes no claim on or to the left of the boundary.

The reason is global, not just local at the candidate pole. Proposition 5.1 says the completed series \(\Lambda(s,\overline{F_1};\phi)_S\) has no possible singularity except a simple pole at (5/6). Since \(\widetilde\psi(0)=0\), the displayed residue is zero and that pole is removable, so \(\Lambda\) is entire. For \(\ell=0\), Lemma 5.3 gives
\[
\Lambda(s,\overline{F_1};\phi)_S=\tfrac14(2\pi)^{-2s}\Gamma(s-\tfrac16)\Gamma(s+\tfrac16)\mathcal D(s,\overline{F_1};\phi)_S.
\]
Equivalently, \(\mathcal D=4(2\pi)^{2s}\Gamma(s-\tfrac16)^{-1}\Gamma(s+\tfrac16)^{-1}\Lambda\). Reciprocal gamma is entire, hence \(\mathcal D\) is entire. There is no extra independent \(\psi(0)\) term in this Dirichlet series: (5.24) and (5.44) define the (S)-supported series as a sum over its nonzero Fourier indices. The constant term in the transformed automorphic form is exactly the \(\widetilde\psi(0)\)-term already isolated in (5.51)–(5.52).

The coefficient factorization is initially valid for \(\Re s>1\). There, and hence by continuation wherever the quotient is defined,
\[
R_\phi(s)=\frac{\mathcal D(s,\overline{F_1};\phi)_S}{3^{5/2+3s}\phi(\lambda)L_{(3r)}(3s-\tfrac12,\phi^3)}.
\]
For \(\Re s>1/2\), the Hecke (L)-function argument has real part (>1), so its Euler product converges absolutely and is nonzero; \(3^{5/2+3s}\phi(\lambda)\) is entire and nonzero. The quotient is therefore holomorphic on that full half-plane. Replacing (s) by (u-1/2) gives the unnormalized region \(\Re u>1\). The same ((r,3)=1) condition remains essential; no (\lambda\)-ray twist or full-row cancellation follows.

## Definition precision and finite common-hole corollary

The theorem's hypothesis is a **primitive residue character modulo the finite ideal \( (r) \)**, extended by zero on nonunits, with \(r\equiv1\pmod3\) and \((r,3)=1\). “Primitive” here means primitive as a character of \( (\mathcal O/r)^\times \); it does not assert that the induced character on ideals, defined by evaluating the character at the unique primary generator, has exact Hecke conductor \( (r) \). The primary-generator choice can introduce a local \(\lambda\)-power in the Hecke conductor. The factor \(L_{(3r)}\) in the coefficient identity is the partial Euler product of those primary-generator values away from (3r), which is all the proof uses.

The fixed finite-hole extension in the author draft is valid. For a fixed ideal \(M\) coprime to \((3r)\), put \(M_0=\operatorname{rad}(M)\), and let \(d\mid M_0\) be represented by its primary generator. Inclusion–exclusion gives
\[
R_{\phi,M}(s)=\sum_{d\mid M_0}\mu(d)\,\widetilde g(d)\phi(d)N(d)^{-s}R_{\phi\overline{\chi_d}}(s),\qquad \chi_d(x)=(x/d)_3.
\]
Indeed, only squarefree \(c\) contribute. If \(d\mid c\), write \(c=dc_0\); squarefreeness forces \((d,c_0)=1\), and \(c_0\) is primary. Dunn–Radziwiłł (2.3) and (1.4) give
\[
\widetilde g(dc_0)=\overline{(d/c_0)_3}\widetilde g(d)\widetilde g(c_0)
=\overline{(c_0/d)_3}\widetilde g(d)\widetilde g(c_0).
\]
The zero extension of \(\chi_d\) then inserts exactly the needed coprimality on \(c_0\). There is no missing extra Möbius or cubic-symbol factor.

For squarefree (d) away from \(3\), every prime ideal \(\mathfrak p\mid(d)\) has \(N\mathfrak p\equiv1\pmod3\) (split primes have norm \(p\equiv1\pmod3\); inert primes have norm \(p^2\equiv1\pmod3\)). Its finite-field cubic residue character is nontrivial of order 3. The product \(\chi_d\) is therefore primitive as a residue character modulo \((d)\). Since ((d,r)=1), CRT makes \(\phi\overline{\chi_d}\) primitive modulo \((rd)\), with primary \(rd\equiv1\pmod3\), and its cube is nonprincipal: on the (r)-component it restricts to \(\phi^3\), which is nonprincipal. Thus each term has the already-proved holomorphy for \(\Re s>1/2\); the finite sum is holomorphic there. Conjugating the Gauss coefficient conjugates the reciprocity factor and replaces \(\overline{\chi_d}\) by \(\chi_d\), which remains primitive and has the same cube.

The mask may first be reduced to primes outside \(3r\): divisors of \(r\) are already zero under the extension of \(\phi\), and primary \(c\equiv1\pmod3\) are automatically coprime to \(\lambda\mid3\). The conclusion is qualitative for each fixed \(M\); it gives no bound uniform in \(M\), \(d\), height, or conductor.

## Final publication audit: draft and exact script

**Verdict:** the main general-twist argument and the stated qualitative scope are sound after the local-factor and script-reference corrections below. In particular, the new entire-completion step checks out: Proposition 5.1 says the completed (S)-series has only the possible simple pole at (5/6); the zero transform removes it, so \(\Lambda\) is entire. Lemma 5.3 for \(\ell=0\) gives \(\mathcal D=4(2\pi)^{2s}\Gamma(s-1/6)^{-1}\Gamma(s+1/6)^{-1}\Lambda\), and both reciprocal gamma factors are entire. Equation (5.44) defines the relevant \(S\)-series directly over \(\mu\in S\); the constant term of the automorphic form is already the \(\widetilde\phi(0)\)-term isolated in the residue calculation, not another independent term in this Dirichlet series. Hence \(\mathcal D\) is entire. The Euler-product denominator in the coefficient identity is holomorphic and nonzero on \(\Re s>1/2\), giving the asserted fixed-twist continuation there. This remains a qualitative result for each fixed modulus, not a uniform estimate or a claim below the half-plane boundary.

The conjugated finite-hole orientation is correct. Since
\[
\overline{\widetilde g(dc_0)}=\chi_d(c_0)\overline{\widetilde g(d)}\,\overline{\widetilde g(c_0)},
\]
the inner character is \(\phi\chi_d\); thus the residual series is \(R^{\mathrm{conj}}_{\phi\chi_d}\), with coefficient \(\mu(d)\overline{\widetilde g(d)}\phi(d)N(d)^{-s}\). This is not a bar-orientation typo.

The appended \(\varepsilon=-1\) finite transform is exactly checked by the requested script. The independent audit ran the companion `check_cubic_noncubic_twist.py`; it passed all 16 classes, unit support, both additive-character conventions, and all three cubic finite-character projections. The script does **not** verify the CRT formula modulo \((4w)\); that identity follows algebraically by CRT from the modulo-4 transform and the primitive cubic Gauss sum modulo \(w\). For this formula, state explicitly that \( (w,4)=1\), \(w\) is squarefree and good, and \(h\) is a unit; the zero claim for nonunit \(h\) also uses primitivity of the local characters. It would help to define \(\gamma_o(w)=q_w^{-1/2}\sum_{v\bmod w}\theta_w(v)e(v/w)\) in the draft or cite the convention at first use.

The published introduction uses the corrected cubic orientation: with theta_w=chi_w^2, theta_w(4)=(w/4)_3^2=conjugate((w/4)_3). The local CRT section explicitly assumes (w,6)=1 and defines gamma_o at first use. These presentation corrections leave the general no-pole and fixed-hole conclusions unchanged. The companion script is published under `check_cubic_noncubic_twist.py`.

The epsilon=-1 section stops short of cancellation for the actual ordered row. Additional lambda-ray dependence and coupled columns still require separate treatment. The result gives no uniform conductor/height bound, complete ordered-pole assertion, or RH conclusion.
