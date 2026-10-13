# Independent review of the complete centered boundary coupling

Date: 2026-10-14 (UTC+8). The complete proof in [CENTERED_BOUNDARY_COUPLING.md](CENTERED_BOUNDARY_COUPLING.md) passes independent mathematical review under its stated original-form and unconditional zero-count inputs. The reviewed clean proof has SHA-256 `19dacde690242ed4a827535d08ead78af45253f94fc5793015e10608405cb155`. This review covers the full mathematical text, rather than an unprovided attachment.

## Result and actual increment

The complete centered-kernel, weighted boundary, closed-form convergence, and averaged-cut arguments pass this independent check. The constants below are coarse analytic upper bounds. The independent 15-comparison Fraction/Taylor check in [check_centered_boundary_constants.py](check_centered_boundary_constants.py) was executed and its output reproduced; it is not the original draft's unprovided 19-comparison script.

Compared with the earlier complete-kernel and hard-cut estimates, the substantive increment is the exact retention of

    ell(T) <F_low, F_high>,  F_low=m v_low, F_high=m v_high, ell(t)=log(2+t).

After subtracting this source Gram term, the cross kernel has no height logarithm. Consequently the residual boundary budget has one logarithmic sampling weight, rather than the two logarithms in the previous absolute full-kernel boundary estimate. This is not merely the earlier separated-band inequality with renamed constants. In addition, the Q(a) assumption proves unconditional convergence in the original closed form norm for all subseries; it does not require graph-absolute convergence.

The displayed source Gram uses the ordinary conjugate-first inner product of the two source vectors. It is not the physical Gram.

## Explicit analytic checks

Let w=m^2, f_z=w cos(zx), gamma_z>=0 and |Im z|<=1/2. The positive-real-part convention is needed also for the nonzero-specific two-mode extension: without it, z=-zeta would invalidate a bound involving |gamma_z-gamma_zeta|. All genuine nodes in the actual theorem have positive real part.

1. In |Im x|<=1/2, cos(2 Im x)>1/2. The theta coefficient bound 4 pi^2+6 pi<59, the ratio bound 16 exp(-9/2)<1/4 and the nonzero cosh denominator give

       |w(x+iy)| <= 100 exp(4|x|-(3/2)exp(2|x|)).

   Negative x follows from the analytic even theta identity. No complex square root of w or strip analyticity of an actual infinite eigen-expansion is used.

2. The elementary inequality (9/2)r<=(3/4)exp(2r)+2 and exp(2r)>=2r pay the shifted L1 integral by 1200. Hence

       |fhat_z(t)| <= 600 [exp(-|t-gamma_z|/2)+exp(-|t+gamma_z|/2)].

3. For each prime-power label and either shift d=+/-log n, the outside complex-frequency factor costs at most sqrt(n). The contour shift by +/-i/2 gains exp(-|Delta gamma|/2). The remaining product of complete theta envelopes is bounded by

       (8/3) 10^4 exp(4) exp(-3n/4).

   The factor sqrt(n) is canceled by alpha_n=Lambda(n)/sqrt(n). Both shift directions give the stated coefficient (16/3)10^4 exp(4). Using exp(4)<81 and sum_(n>=2) n exp(-3n/4)<2 gives 8,640,000<2^24. Thus no prime tail, imaginary-frequency cost, or direction is omitted. The exchanges are after a summable positive majorant is available.

4. Decreasing-integrand comparison for the complete Gamma series yields

       .5 log(1+4t^2) <= b(t) <= 4+.5 log(1+4t^2),
       |b(t)-log(2+|t|)| <= 5.

   With C0<8 and gamma<=T<=gamma', choose a=+/-gamma, c=+/-gamma', d=|a-c|. Then ||t|-T|<=|t-a|+d. The centered integral is bounded by

       (136+8d) exp(-d/4) <= 200 exp(-d/8).

   The Plancherel factor gives 600^2*4*200/(2 pi)<2^26. Addition of the complete-prime bound gives the claimed centered kernel constant 2^27.

5. Unit-height counting with true multiplicities gives the exponential row bound 2^12 C_Z ell(gamma). Weighted Young with |p_z|^2/j_z and the opposite j_zeta factor gives the bilinear Schur bound. Splitting the cross-cut distance exactly in two gives

       |D_T| <= C sqrt(E_<(T) E_>=(T)), C=2^39 C_Z.

   Both boundary factors have exponent -distance/8 after squaring the coefficients weighted by exp(-distance/16).

6. The physical Gram in the form-domain argument involves imaginary offsets up to 1, rather than the 1/2 in the displayed single-source Fourier estimate. Its constant C1 was left unspecified. The same theta envelope with 5r<=(3/4)exp(2r)+2 pays this larger offset directly. The positive Gamma Gram is bounded by C ell(min(gamma,gamma')) exp(-|Delta gamma|/8). Weighted Young therefore gives physical norm <=C J(a)^2 and kinetic form <=C Q(a)^2. The closed form domain then supplies an unconditional Cauchy net, all subseries, and the full-prime form limit.

7. Integration of exp(-|T-gamma|/8) over any real interval is at most 16. Thus averaging sqrt(E_< E_>=)<=(E_<+E_>=)/2 gives the stated 8 C J(a)^2/L cut. This is an absolute coefficient-budget estimate.

## Exact interface with the actual lowest negative state

For the actual real u=l+v, Hu=-kappa u, define

    Q_kappa= h+kappa <.,.>,
    K_T(a,b)=kappa<a,b>+ell(T)<ma,mb>.

Each genuine cut is in the original ground complement, and the lowest-state property gives the already paid identity

    Q_kappa(l,v)=-Q_kappa[v]=-Q_kappa[l] <=0.

The new centered residual D_T=h(l,v)-ell(T)<ml,mv> therefore gives the exact sharpened relation

    K_T(l,v)=-Q_kappa[v]-D_T,
    |K_T(l,v)+Q_kappa[v]| <= (4C/kappa^2) sqrt(S_<(T)S_>=(T)).

All quantities are real for this actual real cut. Equivalently, if R_T[v]=h[v]-ell(T)||mv||^2, then

    K_T(u,v)+R_T[v]=-D_T.

This displays the remaining issue precisely. K_T is a positive inner product on individual vectors, but its mixed pairing K_T(l,v) need not be positive. Its exact sign is tied to the unresolved residual D_T; only Q_kappa(l,v) is known nonpositive. The two renormalized diagonal quantities R_T[l], R_T[v] have not been proved nonnegative. Keeping the exact source main term removes the height logarithm from the error, but does not create a favorable sign for those diagonals or bound the residual relative to them. The actual factor kappa^(-2) and Hermitian sampling squares remain.

No coefficient-one comparison, exclusion of a negative actual state, unit Green bound, or RH conclusion follows from this estimate alone.
