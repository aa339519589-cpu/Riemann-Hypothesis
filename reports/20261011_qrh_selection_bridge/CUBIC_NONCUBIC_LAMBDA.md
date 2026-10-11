# Noncubic Gauss twists in all nine primary lambda-ray channels

## Theorem and scope

Let O=Z[omega], lambda=1+2omega, lambda^2=-3, and Q=N(r). Let r be primary, r=1 modulo 3, with (r,3)=1. Let phi be a primitive residue character modulo (r), zero on nonunits, with phi cubed nonprincipal. For T modulo 3 put

\[
 t=T/3,\qquad A_T=T\lambda/27,
 \qquad\alpha_T(c)=\check e(A_T(c-1)),\quad c\equiv1\pmod3.
\]

Here check e(z)=exp(2 pi i Tr(z)). The nine alpha_T are exactly the nine cubic characters of the primary subgroup modulo 9. For

\[
 R_{\phi,T}(s)=\sum_{c\equiv1\ (3)}
       \widetilde g(c)\phi(c)\alpha_T(c)N(c)^{-s},
\]

there is a holomorphic continuation to Re s>1/2. For 0<epsilon<1/2,

\[
 |R_{\phi,T}(\sigma+i\tau)|
 \ll_\epsilon Q^{3/4}(1+|\tau|)^3,
 \qquad\sigma\ge1/2+\epsilon.                         \tag{1}
\]

The constant is independent of r, phi and the nine ray labels. If M is a finite ideal mask, remove its redundant primes at 3r and put M_0=rad(M). For a compact smooth norm test W and X>=1,

\[
 \left|\sum_{c\equiv1(3),\ (c,M)=1}
 \widetilde g(c)\phi(c)\alpha_T(c)W(N(c)/X)\right|
 \ll_{\epsilon,W}Q^{3/4}
       \sum_{d\mid M_0}N(d)^{1/4}X^{1/2+\epsilon}.      \tag{2}
\]

All estimates are unconditional. The explicit mask cost is retained. The hypothesis concerns primitive residue characters at a modulus prime to 3; the nine additional primary ray characters at lambda are now handled explicitly. Other local characters, the full ordered physical pole calculation, the whole probe and RH are outside this theorem.

## Nine characters and the shifted source

Write c=1+a_2 lambda^2+a_3 lambda^3 modulo 9. For T=A+B omega,

\[
 \alpha_T(c)=\omega^{B a_2+(2A-B)a_3}.                   \tag{3}
\]

Thus T=0 gives the trivial label, six unit classes T modulo 3 give 2A-B nonzero, and the two remaining classes have lambda|T but 3 not dividing T. The map in (3) is invertible over F_3. Multiplicativity follows because the cross term (c_1-1)(c_2-1) is in 9O and A_T9O is contained in the trace-dual lambda^(-1)O; alpha_T has order dividing three. Also f^3=1 modulo 9 for primary f.

Use the source support S={mu=lambda^(-3)cf^3: c,f primary, c squarefree}. On it,

\[
 \check e(t\mu)=\zeta_T\alpha_T(c),\qquad
 \zeta_T=\check e(A_T),\quad |\zeta_T|=1.               \tag{4}
\]

Let F_T(v)=bar F_(1,S)((t,v);phi) in the source's periodic-twist convention, and let D_T(s) be its coefficient Dirichlet series. Direct substitution of the source coefficients on S gives

\[
 D_T(s)=\zeta_T3^{5/2+3s}\phi(\lambda)
    R_{\phi,T}(s)L_{(3r)}(3s-1/2,\phi^3),\quad\Re s>1. \tag{5}
\]

This is the general multiplicative factorization, retaining phi cubed; the source's cubic-only Lemma 5.4 is not substituted for it. The T=0 case, including its growth estimate, is the preceding [noncubic continuation](CUBIC_NONCUBIC_TWIST.md) and [quantitative bound](CUBIC_NONCUBIC_GROWTH.md). Below T is nonzero modulo 3.

## Primal finite twist and reduced cusp matrices

Primitive finite Fourier support gives hat phi(d)=0 off units and |hat phi(d)|=sqrt(Q) on units. Fourier inversion and the source's S projection give the exact finite formula

\[
 F_T(v)=\frac1{3Q}\sum_{d\in(O/r)^\times}\widehat\phi(d)
   \sum_{j=0}^2\omega^j\overline\theta
       \left(t-\frac{9d}{r}+\eta_j,v\right),
 \qquad(\eta_0,\eta_1,\eta_2)=(0,\omega,-\omega).       \tag{6}
\]

For each summand the cusp is a_0/c_0, with

\[
       a_0=rT+3r\eta_j-27d,\qquad c_0=3r.             \tag{7}
\]

At a prime of r, a_0 is a unit because d is a unit and 27 is coprime to r. If T is a unit modulo 3, (a_0,c_0)=1. Choose the unique global unit kappa making a=kappa a_0 primary and put c=kappa c_0. The value of kappa is independent of d and j, since a_0=T modulo 3. Then N(c)=9Q.

If lambda|T but 3 does not divide T, divide both entries in (7) by lambda. Their lambda valuations show that the resulting numerator and denominator are coprime. Choose a global unit kappa making a=kappa a_0/lambda primary and put c=kappa c_0/lambda=-kappa lambda r. Now N(c)=3Q. The primary normalization may depend on j, but not on d: 27d/lambda has lambda valuation five, hence vanishes modulo 3.

In either case (a,3c)=1. Choose D satisfying aD=1 modulo 3c and set b=(aD-1)/c. This constructs

\[
 \gamma=\begin{pmatrix}a&b\\c&D\end{pmatrix},
 \quad\det\gamma=1,\quad a,D=1\ (3),\quad b=0\ (3).     \tag{8}
\]

For unit T, c=0 modulo 3 as well, so gamma lies in the FULL principal group Gamma_1(3). For the two lambda-divisible classes, c is plus or minus lambda modulo 3; hence gamma is congruent to L(plus or minus lambda), where L(u)=[[1,0],[u,1]]. The distinction between these two cases is retained.

The hyperbolic action has the exact vertical-line identity

\[
 \gamma^{-1}(a/c,v)=(-D/c,1/(N(c)v)).                   \tag{9}
\]

There is no v-dependent horizontal error. Within each T case the same N(c) is used by all summands in (6).

## Six unit classes: finite orthogonality at the cusp

For unit T, the conjugated theta function transforms by the multiplier bar chi(gamma)=conjugate((c/a)_3). To compute chi itself, factor c=-lambda^2 r kappa. Its lambda and unit factors depend only on the primary denominator a modulo 9. By (7),

\[
 a=\kappa r(T+3\eta_j)\pmod9,
 \qquad a=-27\kappa d\pmod r.                          \tag{10}
\]

The first residue is independent of d. Primary cubic reciprocity gives (r/a)_3=(a/r)_3; the factor -27 is a cube. Therefore

\[
 \chi(\gamma)=C_{T,j,r}\rho_r(d),
 \quad\rho_r(d)=(d/r)_3,\quad |C_{T,j,r}|=1,            \tag{11}
\]

with C independent of d. The only possible leading cusp term of each unprojected theta is sigma (N(c)v)^(-2/3), multiplied by the conjugate of (11), where sigma=3^(5/2)/2. For each j its complete finite coefficient is proportional to

\[
 \sum_{d\in(O/r)^\times}\widehat\phi(d)\overline{\rho_r(d)}
 =\widehat\phi(1)\sum_d\overline{(\phi\rho_r)(d)}=0.    \tag{12}
\]

Indeed rho_r cubed is principal, whereas phi cubed is nonprincipal. Every nonconstant Fourier mode at the transformed infinity decays exponentially. Equation (12) cancels the full cusp constant separately for each theta translate.

## Two lambda-divisible classes: zero-constant cosets

For these classes (8) is congruent modulo 3 to L(lambda) or L(-lambda). Congruence modulo 3 preserves its left Gamma_2 coset because Gamma_1(3) is contained in Gamma_2. The source representatives are gamma_10=L(omega) and gamma_19=L(omega^2). Explicitly,

\[
 L(\lambda)=L(2+3\omega)L(\omega^2),
 \qquad L(-\lambda)=L(-1-3\omega)L(\omega).             \tag{13}
\]

Both first factors belong to Gamma_2: they are products of an integral rational lower translation and a principal-level-three lower translation. Thus the two cosets are those of gamma_19 and gamma_10. The source gives no constant term for F_19 or F_10. Consequently every summand has zero leading cusp term individually; no assumption about phi at lambda or an untwisted bad-prime matrix is made.

## Entire completion, functional equation and quantitative bound

Using (9) and the theta/coset transformation laws term by term in (6), define a finite transformed combination H_T with

\[
 F_T(v)=H_T(1/(L_Tv)),\qquad
 L_T=9Q\text{ for unit T},\quad L_T=3Q\text{ otherwise}. \tag{14}
\]

Its terms are F_1 at fixed horizontal arguments in the unit case and F_10 or F_19 in the other case, with genuine modulus-one multipliers. Its constant term vanishes by (12) or (13). H_T has exponentially decaying nonzero Fourier modes at infinity. F_T also decays there, by its original S-supported expansion. Equation (14) gives exponential decay at both ends for both functions. Their completions are therefore entire, with

\[
 \Lambda_T(s)=L_T^{1-2s}\Lambda_{H_T}(1-s).             \tag{15}
\]

At a fixed horizontal coordinate z, insert the phase check e(mu z) in each Fourier coefficient and repeat the termwise Bessel Mellin integral of the source's Lemma 5.3. The phase has absolute value one, so absolute convergence is unchanged and the Gamma completion is the same. In the unit case the aggregate constant has already canceled; equivalently, replace each F_1 term in that aggregate by F_1^star before the integral. Thus both series share the completion, and D_T is entire by the reciprocal Gamma formula. The denominator in (5) is holomorphic and nonzero for Re s>1/2, proving the claimed continuation.

The sum of the absolute values of all coefficients in the finite combination H_T is at most sqrt(Q): (6) has at most Q unit terms, each of size sqrt(Q), three translates and normalization 1/(3Q). The fixed source coefficient series of F_1,F_10,F_19 converge absolutely at 1+delta. Thus for 0<delta<=1/4,

\[
 |D_T(1+\delta+i\tau)|\le C_\delta,
 \qquad |D_{H_T}(1+\delta+i\tau)|\le C_\delta Q^{1/2}.
\]

Dividing (15) by the two completions and applying Stirling on the left edge gives

\[
 |D_T(-\delta+i\tau)|
 \le C_\delta Q^{3/2+2\delta}(1+|\tau|)^{2+4\delta}.    \tag{16}
\]

The completed Mellin integrals give fixed-parameter single-exponential vertical growth after reciprocal Gamma factors. The conductor-balanced strip argument from [CUBIC_NONCUBIC_GROWTH](CUBIC_NONCUBIC_GROWTH.md) therefore applies with exactly the same boundary exponents. It yields Q^(3/4) times height degree three on the required strip when delta=epsilon/4. To the right, use the original R_(phi,T) Dirichlet series, whose coefficients have absolute value at most one and whose norms are at least one; do not extend the D_T right-edge bound beyond its proved strip. The absolutely convergent reciprocal Euler product in (5) completes (1).

For finite holes, alpha_T is multiplicative on primary generators, and exact inclusion--exclusion gives

\[
 R_{\phi,T,M}(s)=\sum_{d\mid M_0}\mu(d)\widetilde g(d)
       \phi(d)\alpha_T(d)N(d)^{-s}
       R_{\phi\overline{\vartheta_d},T}(s),
 \qquad\vartheta_d(c)=(c/d)_3.                         \tag{17}
\]

Each residual residue character is primitive modulo (rd) and retains nonprincipal cube. Applying (1) termwise costs N(d)^(3/4-sigma)<=N(d)^(1/4). Mellin inversion and the polynomial height bound give (2). The conjugated-Gauss version follows by conjugating R_(bar phi,-T) at bar s, or by using the correctly oriented finite-hole identity.

## Sources and limits

The primary analytic input is the unconditional theta and periodic-transform material in [Dunn--Radziwill, Sections 5.1--5.4](https://arxiv.org/html/2109.07463v3): full principal congruence groups and the Kubota multiplier; the S projection; the Fourier twist; the cusp expansions at gamma_10 and gamma_19; and the Gamma completion. The new argument is the explicit primal cusp calculation (7)--(13). The preceding [continuation](CUBIC_NONCUBIC_TWIST.md) and [uniform growth proof](CUBIC_NONCUBIC_GROWTH.md) supply the general coefficient and strip ledgers.

No Q or GRH assumption is used. This theorem removes the nine-channel limitation for the stated noncubic residue twists, but applying it to a complete physical row still requires checking that row's exact combined character, masks and unit factors. The companion rational/integer checker verifies the nine finite labels, the 288 cusp matrices at r=4 and source coset words, not automorphy, the all-r analytic proof or RH.

The independent arithmetic and analytic audits are [REFEREE_CUBIC_NONCUBIC_LAMBDA](REFEREE_CUBIC_NONCUBIC_LAMBDA.md); the finite companion is [check_cubic_noncubic_lambda.py](check_cubic_noncubic_lambda.py).
