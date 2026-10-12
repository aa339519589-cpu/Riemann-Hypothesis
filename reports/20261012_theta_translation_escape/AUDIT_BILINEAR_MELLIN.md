# Proof audit: full prime two-scale Mellin Gram and its Fourier density

Date: 2026-10-12. Reviewed BILINEAR_PRIME_ENERGY_MELLIN.md and its dependencies. This is an internal mathematical audit, not external peer review, a formal proof-assistant check or an RH proof.

## 1. Every original shift is retained, with correct polarization

Each true prime edge is \(\alpha_n\int\Phi(x)\Phi(x+d)[q_1(x+d)-q_1(x)][q_2(x+d)-q_2(x)]dx\). Its two diagonal terms combine after a translation into \(\int v_1v_2\lambda_s\). Its two cross terms equal **one** \(\langle f_1,S_sf_2\rangle\), since S_s has both shifts. There is no residual factor 2, no assumption that bilinear edge energies are individually nonnegative, and no finite-prime cutoff. The true weighted source cross has a uniform absolute bound using exponential L² weights \(a>\max(0,s+1/2)\).

The actual PNT-derived jump rate \(\lambda_s(x)\sim\xi(1+s)e^{s|x|}\) is inherited from the newly proved real-Mellin theorem and is a statement about the genuine theta and von Mangoldt functions. No ζ zero locations are imported into its proof.

## 2. Mixed norm and gamma integral

Let delta,epsilon go to zero at fixed ratio theta=epsilon/delta. On the positive x tail the first mode of v_delta*v_epsilon has exponential factor \(\exp[-(c_\delta+c_\epsilon)e^{2x}]\) with \(c_\delta+c_\epsilon\sim\pi(\delta+\epsilon)\). The complete both-tail weighted integral is
\[
4\pi^2 2^{-9/2}\Gamma((5+s)/2)[\pi(\delta+\epsilon)]^{-(5+s)/2}.
\]
The **product of norms**, not the product of squared norms, is \((3/128)(\delta\epsilon)^{-5/4}\). The Mellin scaling of the prime weight is \((\delta\epsilon)^{s/4}\). Canceling the constants gives
\[
(2\pi)^{-s/2}\frac{\Gamma((5+s)/2)}{\Gamma(5/2)}
\left(\frac{2\sqrt\theta}{1+\theta}\right)^{(5+s)/2}.
\]
The scaled cross source is \(O(\delta^{(s+5)/2})\), which vanishes exactly for s>-5.

When theta=1 this expression reduces to the previously proved scalar actual prime moment. When s=0 it becomes exactly one half times the known normalized Hilbert kernel \((2\sqrt\theta/(1+\theta))^{5/2}\). These are distinct normalization checks and require no floating integration.

## 3. Fourier diagonalization and strictness

For beta=(s+5)/2>0, write \(K_s(\ell)=\operatorname{sech}^\beta(\ell/2)\). The substitution \(u=e^\ell\) gives exactly
\[
\widehat K_s(\omega)=2^\beta B(\beta/2+i\omega,\beta/2-i\omega)
=\frac{2^\beta}{\Gamma(\beta)}|\Gamma(\beta/2+i\omega)|^2 .
\]
The integral is absolutely convergent and the RHS strictly positive for all real omega, since Gamma has no zeros and the two arguments have positive real part. This proves positive definiteness of the limiting log-scale Gram kernel, not positivity of the original H outside the known nullspace.

## 4. Continuous/primes mixed balance

The original threshold identity is polarized:
\(E_\Gamma(q_\delta,q_\epsilon)+E_{P,0}(q_\delta,q_\epsilon)
=\frac12\langle v_\delta,v_\epsilon\rangle\).
The inherited true prime rate satisfies \(\frac12-\lambda_0(x)=\frac12e^{-|x|}+O(e^{-2|x|})\). Multiplying by the first-mode product and inserting s=-1 into the complete gamma integral yields
\[
\frac{E_\Gamma}{\|v_\delta\|\|v_\epsilon\|}
\sim\frac{8\sqrt2}{3}\frac{\theta^{5/4}}{(1+\theta)^2}\sqrt\delta .
\]
In particular at theta=1 this is \(2\sqrt2\,\sqrt\delta/3\), matching the earlier scalar theorem. The prime formula retains the **actual** normalized overlap in the leading term, not just its limiting shape; this avoids an illicit second-order replacement.

At s=-5, the weighted cross source is only O(1) and hence lower order to the logarithm; the squared-norm scaling cancels and the coefficient is \(40\sqrt2\zeta(5)\), independent of a fixed theta>0.

## 5. Numerical/algebraic checks and remaining burden

The source theta and PNT limiting identities are proved in the manuscripts, not delegated to a finite computation. The accompanying small exact SymPy checker confirms the finite constants in the gamma/squared norm ratio and at s=0, s=-1, s=-5; the beta-transform integral is proved analytically. All such checks are auxiliary, no interval certificate of off-critical zeta zero absence is claimed.

**No mean-zero full-space spectral positivity or RH theorem is proved.**
