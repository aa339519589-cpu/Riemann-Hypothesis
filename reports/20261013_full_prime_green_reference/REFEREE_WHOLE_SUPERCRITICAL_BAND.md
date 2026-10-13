# Independent review of the whole supercritical-band comparison

Date: 2026-10-14. Two independent reviews checked [WHOLE_SUPERCRITICAL_BAND.md](WHOLE_SUPERCRITICAL_BAND.md). Both approve the dimension-free form-norm and spectral-count statements under the cited complete source/domain, reference-row and PNT inputs. Neither review infers a unit Green bound or RH.

## Mixed spectral parameters

On the actual finite supercritical band of Lambda=T*T, the correct parameter is the self-adjoint operator D=I-Lambda inverse. The auxiliary reflected-energy operator is 2(I-A), and the complete source equation is

    H0 J = -2 J D + 2 A J D.

Each eigen-source is in the same auxiliary operator domain. Finite-dimensional linear extension therefore legalizes this identity on arbitrary mixtures. It does not give every vector a common scalar eigenvalue. The rearrangement

    B_N J = (Q0+F)J - 2 A J(I-D) - 2 J D

retains the complete forward, reflected, mass and pole terms with their full-line factors. No commutation of D through J, A or a cutoff is used.

## Cutoff and order-preserving inverse

The sharp cutoff acts in the reviewed auxiliary Gamma form domain. With X=J*chi_R J, z=||chi_R J|| and beta=||J||, its nonnegative kinetic part gives

    XD+DX <= z beta eta(R) I.

The reflected error uses ||J(I-D)||<=beta; the other rows and Gamma cross use the same beta. The entire eta(R) is bounded by the published row D_0(R)+E_N(R), including every prime power and every omitted-label Stieltjes tail. Thus the estimate does not acquire a factor equal to the unknown spectral rank.

The one-sided order inequality is sufficient. The positive Lyapunov inverse is the integral of Y mapped to exp(-tD)Y exp(-tD), and sends I to (2D) inverse. Applying it gives X<=(z beta eta(R)/2)D inverse, hence z<=beta eta(R)/(2 delta_gamma). The proof never uses the generally invalid noncommuting inequality XD+DX>=2 delta_gamma X.

Both reviews checked the resulting constant 193 times 2 to the 28th power and the exponent 9R-pi exp(2R). The subsequent weighted Stieltjes step gives 193 times 2 to the 29th power with exponent 11R-pi exp(2R).

## Physical norm and full form domain

The improved physical weight requires the actual complete-row theorem L(x)exp(-x/2) tending to a strictly positive limit. Together with continuity and positivity, this supplies a global positive lower constant. The theta quotient then gives mu squared divided by m squared <=C_W exp(2x), with C_W=256/(c_L pi squared). The earlier one-prime lower row alone would not give this exponent.

Choosing exp(2R) comparable to 1+log(1/delta_gamma) absorbs the delta_gamma inverse-square tail loss. The central contribution has the same logarithmic order. Both reviews checked the stated finite constant C and the factor two for the odd full-line extension. The bound is uniform in spectral-band dimension and excess parameter; C has no decimal enclosure in this report.

Physical L2 membership together with the already established logarithmic source form puts the image in the original odd form domain. The complete source and physical prime pairings agree term by term and in their full convergent tails, with the pole moment zero by centering. This gives the physical form value P-N. It does not assert membership in the original physical operator domain.

## Injectivity, count and limitation

If the physical image is zero, J is zero on that vector, hence N=2<J,(I-A)J> is zero. But N is bounded below by (1+gamma)P on the selected band, proving injectivity there. The image is therefore a negative subspace of the same dimension. Its form Rayleigh quotients are bounded above by minus gamma divided by C(1+log(1/delta_gamma)). Original odd negative spectral discreteness and form minmax give the stated projection-rank inequality; polar decomposition transfers the positive band from T*T to TT*.

The result compares entire spectral counts in one direction. It does not identify individual eigenvalues, identify the two full completions, prove a uniform positive physical depth as gamma tends to zero, or rule out any remaining arbitrarily small Green excess above one.
