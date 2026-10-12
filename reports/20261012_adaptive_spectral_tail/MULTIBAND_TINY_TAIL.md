# Explicit omitted-tail bounds for the unchanged 127-column certificate

Status: independently reviewed analytic bookkeeping clarification; frozen after full source-program and inequality review. This page does not change any trial, program, matrix, budget, or spectral depth. It addresses the fixed tiny remainders in the reviewed epsilon=1/1024 program, not the different epsilon=1/8 periodic-input certificate.

Source program: [certify_hardband_continuous_residual_v4.py](gap_511_over_1024_certificate/certify_hardband_continuous_residual_v4.py), SHA-256 `43e08e869b08f0097bd1b06721ae5e2d76a383de6b9eba026f64e449451e1312`. Line numbers below refer to that immutable file.

## 1. Real envelopes and a common elementary tail estimate

Write M(x)=9 exp(2x-(3/2)exp(2x)) for x>=0. The actual theta bound, Astar<81 and pi>3 imply m(x)<=M(|x|). For x>=4 both M(x) and e^(2x)M(x) have logarithmic derivative less than -1. Indeed the larger derivative is 4-3 exp(2x)<-1.

The positive exponential series gives e>65/24>8/3, so exp(8)>2500, while exp(8)<3^8<2^13. Using e>2,

 M(4)<9*2^13*2^(-3750)<2^(-3733).                 (A)

For any nonnegative envelope W with W(4)=w and log derivative <=-1 on [4,infinity),

 2 integral_4^infinity W(x)^2 dx <= w^2,
 2 integral_4^infinity W(x) dx <=2w.              (B)

For either h=1/128 or 1/256, monotone right-Riemann comparison gives the same respective upper bounds for h sum_(|jh|>4) W(|jh|)^2 and h sum_(|jh|>4) W(|jh|). The endpoint samples at +/-4 are retained. Thus (B) pays omitted whole-line lattice samples as well as continuous tails. In particular ||m 1_(|x|>4)||_2<M(4).

The program proves A0<1000, A1<100000 and S0=sum ||s_b,k||+sum ||s_h,k||<10^8 at line 90. These are vector row Euclidean sums, not individual-column estimates. Therefore, on the real line,

 ||Y(x)||<=1000 exp(-x^2),
 ||s_b(x)+s_h(x)||<=10^8.

There are ten carrier bands. Summing the Taylor coefficient series gives the actual extended input row bound

 ||tilde_phi(x)||<=sqrt(10) exp(2|x|)<4 exp(2|x|). (C)

The complete prime symbol satisfies c_4<16, its positive band width W=67/4<17, and hence c_4 W/pi<128. The previously reviewed real theta bounds ||m||_1<1 and ||m||_2<1 remain in force.

## 2. Omitted residual, cross-Gram and form lattice samples

At line 63, outR=|e0| outY+10^-500. The Gaussian term is separately paid. The remaining row is tilde_F-m(s_b+s_h). By (A)-(C), its omitted continuous or lattice L2 norm is bounded by

 [4 exp(8)+10^8]M(4)<2^28 M(4)<2^(-3705).          (D)

This proves the 10^-500 allocation in that line, including its actual vector dimension.

At line 95, crossErr contains a separate 10^-100. The omitted lattice (or continuous) cross product tilde_F*Y has Frobenius norm at most

 2*4*1000 exp(8) M(4)<2^26 M(4)<2^(-3707).         (E)

We dropped exp(-x^2), making the bound larger; the remaining envelope e^(2x)M(x) is decreasing as required for (B). The comparison is on the actual extended input, not an unperiodized substitute for a periodic input.

At line 96, energyErr contains its own 10^-100, while |e0|outY^2 separately pays the Gaussian-only form term. The remaining omitted m(s_b+s_h)Y product has Frobenius norm at most

 2*10^8*1000 M(4)<2^38 M(4)<2^(-3695).             (F)

The true compact inputs are recovered separately: delta_F from lines 65-72 is added to rho at line 89 and delta_F||Y|| is added to crossErr at line 95. Neither of these actual endpoint corrections is included in (D)-(F) or discarded as tiny.

## 3. The omitted source samples in the complete-symbol Fourier sum

The exact source is f=mY. The source step is 1/128 and the implemented sample range is |x|<=4. Equation (B) gives the vector L1 lattice tail

 M_src=(1/128) sum_(|j/128|>4) ||f(j/128)||
       <2*1000 M(4)<2^(-3722).                   (G)

Consider the entire-lattice source sum, and group indices modulo 10240, the source period 80. This is exactly the DFT of the periodized source samples. Thus the single difference between that entire-lattice DFT and the implemented finite source sum is the tail (G); no unstated identity between literal and periodized samples is needed.

For every implemented cosine coefficient, the factor is at most 2/80, so its vector error is at most M_src. The number of nonnegative coefficients is 5121<2^13. At their frequencies t<=128pi<512,

 |b(t)-C_4(t)|<=18t^2+c_4<2^23.

Consequently the omitted-source contribution to the entire finite b-C_4 synthesis is bounded uniformly by 2^36 M_src<2^(-3686). Multiplication by m, with ||m||_2<1, preserves this upper bound. This is distinct from the explicit Fourier alias in lines 74-77 and distinct from b periodization in line 73.

## 4. Sharp-band source truncation and remote output

The positive exact quadrature weights on the ten bands sum to W, so their absolute C_4-weighted sum divided by pi is at most c_4 W/pi<128. The difference between the whole-lattice Fourier samples and the |y|<=4 samples therefore contributes less than 128 M_src<2^(-3715), uniformly in the target x. Again multiplication by m costs at most one.

The non-grid source alias is separately paid at line 85. The finite-source Clenshaw-Curtis error on |x|<=4 is separately paid at lines 79-82; its source-weight prerequisite is independently checked at lines 15-16.

Outside |x|<=4, no exponential decay of the sharp-band kernel is assumed. The true hard-band output is bounded in row norm by

 (c_4 W/pi)||f||_1<128*1000<2^17.

The stored hard-band synthesis row is bounded by S0<10^8<2^27. Hence their m-weighted difference outside |x|<=4 has norm less than 2^28 M(4)<2^(-3705). Numerical coefficient error is separately paid globally at line 86; using the stored synthesis bound here does not remove that payment.

There is no Q^2 C_4 periodic-image term in this implementation: its hard-band term is the actual finite-band Fourier integral, and only b-C_4 is periodized. No 373-column periodic input row occurs either.

## 5. Full local-prime image sum

For the local C_4 term, every nonzero period image has shift s=80j+lambda, j nonzero, |lambda|<=log4<2. The true operator bound

 ||M_m tau_s M_m||<=||m||_infinity M(|s|/2)

follows by splitting where |x| or |x+s| is at least |s|/2. Use ||m||_infinity<9 and ||Y||_2<=A0||exp(-x^2)||_2<2A0. Since |s|/2>=40|j|-1>=4+|j|, the logarithmic derivative bound yields M(|s|/2)<=M(4)e^(-|j|). Finally sum_(j>=1)e^(-j)<1. Summing the absolute prime coefficients, including C0, gives the complete nonzero-image norm less than

 2A0 * 9 * c_4 * 2 M(4)<2^20 M(4)<2^(-3713).      (H)

This is global in x. No additional remote-output region is omitted from (H). The complete b-image bound at line 73 is likewise already global.

## 6. Allocation and conclusion

The action tails in sections 3-5 sum to less than 2^(-3680); they fit the 10^-100 term in EA at line 88. The lattice tails (D), (E), (F) fit, separately, their indicated allowances at lines 63, 95, 96. All stated sums are even less than 2^-3600<10^-1000, using 2^10>10^3.

Thus the unchanged 127-column program has enough explicit tiny allowance for these omitted tails. Its published prose already identifies their objects, but had not expanded the fixed constants into (A)-(H). This page supplies that expansion only; it does not independently certify the other numerical components, change the 511/1024 conclusion, or supply an all-epsilon argument.

## Proof-completion context and review

This supplement follows the user's separate [373-column omitted-tail correction](FULL_GAMMA_TINY_TAIL.md), first published in [e4326b0a](https://github.com/aa339519589-cpu/Riemann-Hypothesis/commit/e4326b0a16552c2de3024754d25721cea8ffbddf). Its different periodic-input lemma is not used in place of the actual 127-column estimates above. The original [127-column report](CERTIFIED_MULTIBAND_GAP.md) and [four-program certificate](REFEREE_CERTIFIED_MULTIBAND_GAP.md) should be read together with the [independent review of this supplement](REFEREE_MULTIBAND_TINY_TAIL.md). This supplies previously unexpanded fixed constants; all numerical artifacts and the single-depth 511/1024 conclusion stay unchanged.
