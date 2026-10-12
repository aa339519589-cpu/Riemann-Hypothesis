# Independent review: executed rank-one threshold shorting

The complete [RANK_ONE_SHORTING.md](RANK_ONE_SHORTING.md) argument and both [interval programs](rank_one_certificate) were independently reviewed and executed. The 40,000-cell output is byte-identical to the author's output. The scope is the original complete even form-domain gap 7/16 through the user's exact rank-one repair, which is weaker than the separately certified 511/1024 result. The actual interval assertions and original operator, rather than exploratory eigenvalue signs, are the proof inputs.


## Original comparison and the user's correction

For each actual Gamma summand, its constant minus multiplier is the Fourier transform of exp(-(2j+1/2)|x|), without an omitted normalization. The six-term bound and the complete prime tail give K<=H+1/16 on the entire original form domain. The included prime powers are 2,3,4,5; Lambda(6)=0. The diagonal prime estimate and omitted-prime delta keep every original prime power in the comparison.

The true threshold vector w=(Phi''-Phi/4)/m belongs to D(B), and Hw=0 follows by differentiating the actual source identity twice and subtracting one quarter of it. The original theta tails make w square-integrable. Thus b_col=-Aw and g=<w,b_col> are exactly the user's defect column and defect Gram. The independently approved user theorem (commit 1d739d99) gives F=b_col b_col*/g<=H-A and (K+F)w=epsilon w. This review does not reattribute that shorting theorem.

The user d50c8734 original-form foundation has also been independently approved. It gives a self-contained unconditional realization of the original complete maximal even form, its source form, and the known normalized ground. The use of the comparison is through these closed forms, not an operator-inner-product assertion for every form-domain vector.

## Folded signed Hilbert--Schmidt criterion

The unitary even-to-half-line map supplies sqrt(2) in z and the two exponentials in the folded positive T kernel. No extra factor belongs in T. The real multiplication by d^(1/2) is boundedly invertible, since d is bounded and the global verified lower bound is 1/50; it preserves negative inertia. K+F is therefore congruent to I-(T-zz*/g).

T is positive compact Hilbert--Schmidt; the finite-rank subtraction may be signed. With tau=||z||^2 and A1=<z,Tz>, expansion gives exactly
Tr(T_c^2)-(A1/tau-tau/g)^2=Tr(T^2)-(A1/tau)^2.
A positive and a negative Rayleigh direction force separate spectral branches. If there were two eigenvalues above one, the largest positive square, the second square above one, and the negative extreme square would exceed the certified total squared trace. The probes need not be orthogonal. This establishes the strict signed two-Rayleigh sufficient test without assuming positivity of T_c.

The known H ground has value -1/2, so at epsilon=1/16 it consumes the single allowed negative direction of H+epsilon. The orthogonal original mean-zero form is therefore at least 7/16.

## Theta ranges, full-line tails, and interval arithmetic

The polynomials for Phi, Phi', f=Phi''-Phi/4, and f' were checked. The omitted n>=5 theta terms have geometrically dominated consecutive ratios and the stated polynomial bounds. The midpoint-plus-first-derivative range is intersected with the independently valid direct positive m^2 range; this does not replace a range by point sampling. Interval endpoints are represented with higher mp precision than their interval precision, so the midpoint/radius operations used here do not silently lower the enclosure precision.

The actual bound E(x)=exp(13x/2-3 exp(2x)/2) controls m,f,w and the derived columns. The f and w estimates retain the true original denominator m. The global bound for |d-epsilon| and the folded kernel bound 12 imply every displayed column envelope. The convolution input constants are at most 5*10^9; all scalar-product constants are covered by 10^22 E^2, including the full-line factor two in g. The exterior script directly verifies the derivatives of the exponent at R0=5/2, the global exterior d lower bound, and the stated tails. The actual convolution-tail bound is about 3.25e-82 and scalar tails about 6.41e-161, each below the symmetric 1e-45 allowances used in the mesh program.

Signed convolution uses independent prefix/suffix intervals and a genuine same-cell kernel range. The positive squared trace uses factor 8 on the two distinct-cell triangles and factor 4 on a whole same-cell square, with multiplicity two for unequal lambda pairs. The full exterior square is bounded using the exact integrated theta envelope for a^2. Hence neither diagonals nor the exterior line is omitted.

The mesh script uses directed mpmath intervals at 35 decimal digits and higher-precision exact endpoint handling. All comparisons that matter are strict against explicit rational thresholds. It checks d_min>1/50, 64<g<66, Qplus>389/100, Qminus<-47/100, and the signed squared-trace remainder<99/100. The independently reproduced last enclosing interval is approximately [0.75378410430, 0.97100456413]; these decimals are informational, while the proof uses the rational assertion.

## Scope

Approved: an unconditional whole-original-domain certificate at epsilon=1/16, giving E(q)>=7 Var_nu(q)/16 for every original even form-domain q, with the user rank-one shorting applied exactly. It neither establishes all epsilon, exhausts the threshold space, improves the currently known 511/1024 gap, nor proves RH. No higher-rank candidate or exploratory floating eigensolver is a dependency.
