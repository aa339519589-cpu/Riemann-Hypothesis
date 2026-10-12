# Independent review: effective Gamma tails of the original nonpositive states

The complete [mathematical proof](EFFECTIVE_GAMMA_EIGENSTATE_TAIL.md) has been independently reviewed. Part A gives an explicit cutoff for each normalized actual eigenvector of H with lambda<=0, uniform in its eigenvalue depth. Part B gives a qualitative norm limit on the entire genuine nonpositive spectral subspace. The stronger domain of the qualitative statement does not transfer the effective rate to arbitrary spectral superpositions. Neither theorem controls the remaining prime-edge defect or excludes a zeta zero.

The original form realization retains the user's attribution. The user's necessary Gamma-depth theorem for a selected-space comparator is a separate result; this proof gives a sufficient cutoff only for the stated Gamma-energy approximation.

## Part A. Constructive estimate

### Actual scalar inputs

The upper and lower theta envelopes give M=2 and the displayed m_tail and mu on their stated outer and inner regions, since 4x-pi exp(2x) decreases for x>=0. The finite-prime norm bound and complete tail make C an explicit bound for ||V||. The estimate c_N<=C0+4sqrt(N)log N follows by the elementary sum of n^(-1/2). No omitted prime is changed in the actual operator.

The exact jump kernel has moment constants M1=(1/2)sum(j+1/4)^(-2)<9 and M2=(1/2)sum(j+1/4)^(-3)<36. Their factors agree with the original digamma symbol and the 1/2 in the jump form. The decreasing-series integral yields b(T)>=0.5log(1+4T^2).

### Original-domain localization

The Lipschitz commutator is an L2-bounded integral operator with norm at most M1 times the Lipschitz constant. The exact IMS-type identity (7), including its plus sign and factor 1/2, follows by expanding the two jump differences. Multiplication by the cutoff preserves the original source form domain; convergence from finite kernels is controlled by the second moment. The argument never assumes that the global unweighted b(D)f is L2.

On the support of a nonzero cutoff difference, one endpoint lies outside radius R. Thus m(x)m(x+y)<=M m_tail(R). Young's inequality applied to the original normalized v yields precisely 72 M m_tail(R)/s^2. This is stronger than discarding the true theta factors. Testing the actual eigenvalue equation against chi^2 v is legitimate in the original form domain, and the term lambda||chi v||^2 has the claimed favorable sign. The outer V contribution is at most M m_tail(R)c_N+delta_N. These verify (8)-(9) for a true eigenvector.

The local distributional eigen-equation gives b(D)f=(Vv+lambda v)/m on compact intervals. The positive lower bound mu(R+s), together with the bounded commutator, makes b(D)(theta f) globally L2. The maximal Fourier multiplier domain therefore genuinely contains the compact interior source g. Its bounds in (11) have the correct factors 2C and 18M/s.

### Gamma-tail split and explicit budget

On |t|<=T, beta_J is bounded by beta_J(T); on the complement, beta_J<=b<=b^2/b(T). Combining this with f=g+chi f gives (12) with both factors 2. The decreasing series tail gives beta_J(T)<=3T^2/(8J^2).

For the specified y,R,s,N, c_N<=8y^2. Since M=2 and m_tail(R)=7y exp(-pi y/2), the outer main term is at most 1120y^3 exp(-pi y/2). The complete prime tail is at most one further copy: the ratio is decreasing for y>=2 and already below one at y=2. Hence the relaxed constant 1200 is valid. The displayed exponential choice of y pays 2h<eta/3; the elementary inequality 7200*47^3<10^9<2^40<exp(40) supplies strict separation without numerical sampling.

With T=exp(6L_*^2/eta+1), the full digamma lower bound pays 2L_*^2/b(T)<eta/3. With J=ceil(4T/sqrt eta), the low-frequency remainder is at most 3eta/16. All three parts sum to less than eta, proving (18) uniformly in the depth of the eigenvalue.

For the growth order, exp(2/y)<=1+4/y gives the stated mu inverse bound. Squaring (11) by the two-term inequality and using y^4<=exp(pi y) yields exactly K in (19). The substitution exp(pi y)=exp(80)eta^(-2)(ell+2)^6 and y>=(2/pi)(ell+2) gives the L_* bound. The final rounding J<=5T/sqrt eta proves (20) with the displayed C_Gamma. Every constant is explicit.

### Scope

This is a genuine effective Gamma approximation bound for actual nonpositive eigenvectors, including any one eigenspace. The proof uses the eigenvalue identity after localization; it does not extend that sign step to arbitrary superpositions of distinct eigenvalues or to a general energy cone. The separate qualitative spectral-subspace compactness result has a different scope.

Choosing eta smaller than a target depth is now possible without knowing the eigenvector or a rate for an unknown spectral projection. The remaining full-prime edge defect, its shorted complementary block, and the critical sign are untouched. The estimate is not a successful all-epsilon comparison certificate and does not contradict the user's necessary Gamma-depth bound for a different corrected comparator. No new zeta-zero exclusion is claimed.

## Part B. Compactness on the genuine spectral subspace

Since H>=-||V||, its restriction to this spectral subspace is bounded. Hence P maps boundedly to D(H)=D(B), HP and BP are bounded, and the form inequality (2) is valid on its whole range. This is a spectral-subspace assertion, not an inference about an arbitrary expectation-energy cone.

The complete source frequency tail and the Hilbert--Schmidt operator Q_T m prove mP compact. Every finite-prime V_NP factors through mP with a bounded left factor. The established full-prime operator-norm tail then makes VP compact. Compression PVP is nonnegative on this subspace and dominates the positive compression PBP. The manuscript's finite-rank compression estimate proves compact domination directly. Consequently the genuine source Gamma-energy map T=sqrt(b)(D)m has TP compact because its Gram PBP is compact.

The measurable multipliers sqrt(beta_J/b), with zero assigned at t=0, are contractions and converge pointwise to zero. They converge strongly on source L2, and their composition with the compact TP converges in norm. This gives the asserted uniform tail for all normalized vectors of the genuine nonpositive spectral subspace. The explicit fixed-frequency series bound (5) is correct but alone does not furnish a global effective rate.

Removing the ground from P still leaves the known infinite-dimensional kernel; the desired exclusion concerns only its strictly negative spectral part. The independent full-prime edge form is not controlled by this Gamma-tail conclusion. These limitations are essential and retained.
