# Mathematical review: first-jet arithmetic rigidity

Reviewed theorem: [First-jet rigidity for all polynomial-growth coupled arithmetic perturbations](REPORT.md).

Reviewed version, SHA-256:

`285996da0d890cd4e9f5f1f83342e2d74422c3280dad39e7c0f421aa4815e3a7`

Date: 2026-10-14.

## Disposition and exact scope

The theorem and its completed-domain positivity corollary pass this independent mathematical read-through. No sign, normalization, convergence, or domain error was found in the reviewed version. This is not formal verification, an external peer-review endorsement, a literature-priority claim, or a proof of RH.

The theorem fixes the genuine theta source, the complete Gamma and pole components, integer shifts `log n`, and the coupling of each forward and reflected coefficient. It allows real or complex perturbations bounded by a fixed polynomial in n. It assumes mixed nullity of the first actual theta jet against every compact ratio-core test, and concludes that every coefficient perturbation vanishes. It does not make this conclusion from one quadratic equality alone.

## Mixed-form reduction and domains

Expanding the forward square gives the two same-wing divergences with coefficient two. Reflection of the negative square gives the opposite-wing divergence with coefficient minus two. Extending psi oddly and the first ratio jet evenly therefore gives exactly

    Delta_b(r_0,r) = 2 integral_0^infinity psi r [h''-(psi''/psi)h].

The signs and the factor two in this formula are correct. When a shifted r_0 appears, its accompanying psi converts it to the rapidly decreasing source f_0. Polynomial growth of b_n is consequently absorbed by the theta tails, uniformly with every fixed derivative on compact x intervals. This validates the exchanges of sums, differentiation, and compact-test integration.

The potential psi''/psi has a smooth even extension at zero because psi is smooth odd with a simple zero. Both h and psi are odd and vanish there. Ordinary initial-value uniqueness therefore gives h=c psi. No singular-endpoint uniqueness theorem is being assumed.

## Integer theta transform

The proof correctly avoids taking a Fourier transform of the log-prime measure, which can have exponential growth in its logarithmic coordinate.

The exact scaling is

    Phi_k(x+log n) = sqrt(n) Phi_kn(x),

so regrouping yields the divisor coefficient a_m=sum_{n|m,n>=2}sqrt(n)b_n and a_1=0. The double series is locally absolutely convergent by its Gaussian factor in n²k².

Direct differentiation confirms the seed identity

    (partial_x²-1/4)[e^{x/2}e^{-pi m²e^{2x}}] = Phi_m(x).

The integration constant in F(x)+F(-x)=c Phi(x)+C_0 is retained. After removing c Phi/2 and undoing the differential seed, the even homogeneous solution and the constant particular solution give exactly

    Theta_A(t)+t^{-1/2}Theta_A(1/t) = -8C_0 t^{-1/4}.

Thus the factor minus eight and the exponent minus one quarter are correct.

## Homogeneous-error elimination

The polynomial-growth integer coefficients define a genuine even tempered distribution supported on the integers, with delta atoms and no delta derivatives. The Gaussian pairing of |x|^{-1/2} is exactly

    pi^{-1/4} Gamma(1/4) t^{-1/4}.

The supplied Gaussian uniqueness lemma is valid. Differentiation in the parameter occurs in the Schwartz topology. Evenness supplies the odd moments, and the Gaussian-weighted Fourier pairing is entire. Vanishing of all its derivatives makes that pairing zero; Fourier uniqueness followed by local division by a nonvanishing Gaussian proves the distribution vanishes.

The resulting equation mu+hat(mu)=kappa|x|^{-1/2} therefore follows. Integer delta support makes hat(mu) one-periodic and makes multiplication of mu by e^{2pi ix}-1 equal to zero. After this multiplication, the left side is periodic. For nonzero kappa the right side is not periodic, as seen by comparing x and x+1 on any open subinterval of (0,1). This argument is legitimate distributionally because those compared functions are smooth there. Hence the homogeneous error vanishes.

Anti-selfduality then makes mu itself periodic. Its integer atom coefficients must all be equal. Pairing the Gaussian at t=1 forces that constant comb coefficient to be zero. Finally a_1=0 eliminates c, and the triangular divisor relation eliminates all b_n. No critical-strip zero-location assumption occurs.

## Positivity and a saturated first jet

The corollary correctly uses a nonnegative absolute control form, rather than subtracting potentially infinite energies. For polynomial-growth candidate coefficients, the reflected row is bounded by C exp((A+1)x), and the sum of forward and backward rows by C(1+exp((A+1)x)). The ordinary exponential growth of r_0 is therefore paid by the double-exponential theta tail. These row bounds prove absolute arithmetic-energy finiteness and cutoff convergence for r_0.

The Gamma cutoff difference splits into the original r_0 difference and a cutoff-difference term. The latter is controlled by the integrability of the jump kernel times min(1,|x-y|²), while the theta-weighted r_0 square is integrable. The pole convergence is its weighted L² convergence. Thus the cutoff sequence reaches r_0 in the stated absolute-energy completion, and its signed quadratic value is the actual integral value.

Positivity on the compact core extends continuously to this completion. If the completed value at r_0 is zero, the positive-semidefinite Cauchy–Schwarz inequality forces mixed nullity against every core test. Subtracting the genuine mixed identity now meets the theorem's exact hypothesis. This validates the corollary.

## Limitations

The result is rigidity, not existence or positivity. It does not construct a positive candidate form, establish the coefficient-one Green comparison, or exclude an off-critical zero. The corollary's candidate existence is equivalent to the genuine positivity problem, not an easier problem already solved.

The fixed source, fixed Gamma/pole terms, paired shifts, integer arithmetic, polynomial growth, and full mixed-null hypothesis are substantive restrictions. The proof does not establish comparable uniqueness for arbitrary shifts, independently perturbed forward/reflected coefficients, a changed theta source, or uncontrolled coefficient growth.
