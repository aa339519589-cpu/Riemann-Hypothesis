# Exact two-scale prime-energy Gram limit and its positive Fourier spectrum

Date: 2026-10-12. Objective remains a complete unconditional RH proof. This is a **real full-theta, full-von-Mangoldt bilinear theorem**, building on the rigorously controlled *actual* prime-energy moments in PRIME_ENERGY_MELLIN_MOMENTS.md. It exposes the limiting whole-kernel arithmetic correlation between different genuine critical equality vectors, rather than looking only at single-vector moments.

**NO NEW UNCONDITIONAL RH THEOREM PROVED.** The positivity proved below concerns an explicit limiting Gram family of already-known equality vectors, not arbitrary test vectors of the original Weil form.

## 1. Original source and fully polarized prime energy

Use the original positive even theta source \(\Phi\), \(h=\cosh(x/2)\), \(m^2=\Phi/(2h)\), \(a_*=\frac12\log2\), and the exact true-critical family
\[
f_\delta(x)=\Phi(x+a_*-\delta)+\Phi(x-a_*+\delta)
-2\cosh((a_*-\delta)/2)\Phi(x),\quad
v_\delta=f_\delta/m,\quad q_\delta=f_\delta/\Phi.
\tag{1}
\]
For each real \(\delta\in(0,a_*/2)\), \(v_\delta\in\ker H\), where H is the original fully weighted theta/Gamma/all-prime selfadjoint operator; equivalently \(Lq_\delta=q_\delta/2\). Its exact squared norm satisfies
\[
\|v_\delta\|_2^2\sim(3/128)\delta^{-5/2}\qquad(\delta\downarrow0).
\tag{2}
\]
The arithmetic theorem itself uses only the explicit functions (1) and literal prime edge integrals.

For any real s, define the **complete polarized** prime form
\[
E_{P,s}(q_\delta,q_\epsilon)=
\sum_{n\ge2}\frac{\Lambda(n)n^s}{\sqrt n}
\int_{\mathbb R}\Phi(x)\Phi(x+\log n)
[q_\delta(x+\log n)-q_\delta(x)]
[q_\epsilon(x+\log n)-q_\epsilon(x)]dx .
\tag{3}
\]
All sums converge absolutely for each fixed positive \(\delta,\epsilon\). This is a bilinear form; off-diagonal values need not be positive. No prime or prime-power summand is deleted.

Let the complete weighted prime-rate and signed source shifts be
\[
\lambda_s(x)=\frac1{2h(x)}\sum_{n\ge2}\Lambda(n)n^{s-1/2}
[\Phi(x-\log n)+\Phi(x+\log n)],
\]
\[
S_sf(x)=\sum_{n\ge2}\Lambda(n)n^{s-1/2}[f(x-\log n)+f(x+\log n)].
\]
Expanding the two prime differences and translating integrals gives the exact polarized identity
\[
\boxed{E_{P,s}(q_\delta,q_\epsilon)=
\int_{\mathbb R}v_\delta(x)v_\epsilon(x)\lambda_s(x)dx
-\langle f_\delta,S_sf_\epsilon\rangle.}
\tag{4}
\]
Uniform double-exponential source tails and an exponentially weighted L² correlation estimate show
\[
|\langle f_\delta,S_sf_\epsilon\rangle|\le C_s
\tag{5}
\]
uniformly for \(0\le\delta,\epsilon\le a_*/2\). The full proof is the same valid absolute-series estimate as Lemma 2 of PRIME_ENERGY_MELLIN_MOMENTS.md, now with two distinct source inputs. The actual full prime-rate satisfies
\[
\boxed{\lambda_s(x)\sim\xi(1+s)e^{s|x|}
\quad(|x|\to\infty),\qquad
0<\lambda_s(x)\le C_s e^{s|x|}.}\tag{6}
\]
This is the all-real-s PNT/theta result, not a conjectural Euler-product continuation.

## 2. The two-scale theorem

For \(\theta>0\), let \(\epsilon=\theta\delta\). Define
\[
\mathscr B_s(\delta,\theta)=
\frac{(\delta\epsilon)^{s/4}}
{\|v_\delta\|_2\|v_\epsilon\|_2}
E_{P,s}(q_\delta,q_\epsilon).
\tag{7}
\]

**Theorem 1 (all real s>-5, all fixed positive scale ratios).** For every \(s>-5\) and every \(\theta>0\),
\[
\boxed{\begin{aligned}
\lim_{\delta\downarrow0}\mathscr B_s(\delta,\theta)
&=C_s^{\mathrm{arith}}
\left(\frac{2\sqrt\theta}{1+\theta}\right)^{(s+5)/2},\\
C_s^{\mathrm{arith}}
&=\frac{\xi(1+s)}{(2\pi)^{s/2}}
\frac{\Gamma((s+5)/2)}{\Gamma(5/2)}>0.
\end{aligned}}\tag{8}
\]
The limit is locally uniform in \(\theta\in(0,\infty)\). For \(\theta=1\), it is exactly the **actual moment convergence** of PRIME_ENERGY_MELLIN_MOMENTS.md; this theorem additionally handles all true bilinear cross terms at two different escape scales.

### Proof

Put \(c_\delta=\pi(e^{-2(a_*-\delta)}-\frac12)\sim\pi\delta\). Uniformly as \(x\to+\infty\) and the two scales approach zero in a fixed ratio,
\[
v_\delta(x)v_\epsilon(x)
=4\pi^2 e^{5x-\frac92(2a_*-\delta-\epsilon)}
e^{-(c_\delta+c_\epsilon)e^{2x}}\,[1+o(1)].
\tag{9}
\]
The product is even. For each \(s>-5\), double the positive x-axis, put \(u=e^{2x}\), and apply the complete first-mode theta majorants:
\[
\boxed{
\int_{\mathbb R}v_\delta(x)v_\epsilon(x)e^{s|x|}dx
\sim4\pi^2\,2^{-9/2}\,
\Gamma((s+5)/2)(c_\delta+c_\epsilon)^{-(s+5)/2}.}\tag{10}
\]
The integral diverges for s>-5, so any fixed spatial compact contributes a negligible O(1). By (6) the same integral with \(e^{s|x|}\) replaced by \(\lambda_s(x)\) is asymptotic to \(\xi(1+s)\) times (10). The uniformly bounded exact source cross term (5) is lower order after applying the normalization in (7):
\[
\frac{(\delta\epsilon)^{s/4}}
{\|v_\delta\|\|v_\epsilon\|}\,O_s(1)
=O_{s,\theta}(\delta^{(s+5)/2})=o(1).
\]
Using \(\|v_\delta\|\|v_\epsilon\|\sim(3/128)(\delta\epsilon)^{-5/4}\), \(c_\delta+c_\epsilon\sim\pi(\delta+\epsilon)\), and the s=0 normalization identity in (2), the ratio becomes (8) by exact algebra. All estimates are uniform when \(\theta\) belongs to a compact subset of \((0,\infty)\). □

## 3. Positive-definite continuum Gram kernel with explicit spectral density

Introduce a log-scale coordinate \(u=\log\delta\). If \(\theta=e^\ell\), the **normalized universal ratio kernel** in (8) is
\[
\boxed{K_s(\ell)=
\left[\operatorname{sech}\left(\frac\ell2\right)\right]^{(s+5)/2},
\qquad s>-5.}\tag{11}
\]
It is positive definite on all real log scales, and its Fourier transform is **strictly positive at every real frequency**:
\[
\boxed{
\int_{\mathbb R}K_s(\ell)e^{i\omega\ell}d\ell
=\frac{2^\beta}{\Gamma(\beta)}
\left|\Gamma\left(\frac\beta2+i\omega\right)\right|^2>0,
\qquad \beta=\frac{s+5}{2}>0.}\tag{12}
\]
Proof: for \(z=e^\ell>0\), \(\operatorname{sech}(\ell/2)=2\sqrt z/(1+z)\) and \(d\ell=dz/z\). Therefore the Fourier transform is the absolutely convergent beta integral
\[
2^\beta\int_0^\infty\frac{z^{\beta/2+i\omega-1}}{(1+z)^\beta}dz
=2^\beta B(\beta/2+i\omega,\beta/2-i\omega).
\]
The Gamma product is a positive real number for all real \(\omega\). Thus (12) is an *exact diagonalization of the limiting true-prime critical Gram on logarithmic escape scales*, not a claim about the sign of the true operator on its orthogonal complement.

At s=0, \(K_0(\ell)=\operatorname{sech}^{5/2}(\ell/2)\), precisely the known **unweighted** normalized Hilbert Gram geometry used by the theta boundary-frame/Riesz construction. The new result is that the *entire actual weighted-prime energy family* carries this same kernel with a continuously varying exponent \((s+5)/2\), and has the strictly positive spectral density (12). No Riesz bound on a continuous non-discrete frame is inferred from Fourier positivity alone.

## 4. A quantitative bilinear Gamma/prime cancellation at the actual critical energy

For s=0 the exact original eigen-equations imply the complete polarized identity
\[
E_\Gamma(q_\delta,q_\epsilon)+E_{P,0}(q_\delta,q_\epsilon)
=\tfrac12\langle v_\delta,v_\epsilon\rangle.
\tag{13}
\]
The true unweighted prime-rate has the more precise *inherited* expansion
\[
\lambda_0(x)=\tfrac12-\tfrac12e^{-|x|}+O(e^{-2|x|})
\quad(|x|\to\infty).
\tag{14}
\]
Insert (14) into (4), use (5), and repeat (10) with s=-1. The source cross term contributes only O(1), while the weighted Hilbert integral grows like \((\delta+\epsilon)^{-2}\). This gives, for fixed \(\epsilon=\theta\delta\),
\[
\boxed{
\frac{E_\Gamma(q_\delta,q_\epsilon)}
{\|v_\delta\|\|v_\epsilon\|}
\sim \frac{8\sqrt2}{3}
\frac{\theta^{5/4}}{(1+\theta)^2}\sqrt\delta.}\tag{15}
\]
For \(\theta=1\) the factor reduces to \(2\sqrt2\,\sqrt\delta/3\), exactly matching the previously proved scalar Gamma/prime energy split. Consequently
\[
\boxed{
\frac{E_{P,0}(q_\delta,q_\epsilon)}
{\|v_\delta\|\|v_\epsilon\|}
=\frac12\,\frac{\langle v_\delta,v_\epsilon\rangle}
{\|v_\delta\|\|v_\epsilon\|}
-\frac{8\sqrt2}{3}
\frac{\theta^{5/4}}{(1+\theta)^2}\sqrt\delta+o(\sqrt\delta).}\tag{16}
\]
The first term on the right is deliberately the **actual** normalized Hilbert overlap, not only its limit \(K_0(\log\theta)\). Replacing it by that limit without an appropriate rate would be an unjustified next-order expansion. The formula retains all theta and prime cancellations.

## 5. The sharp Mellin borderline survives two-scale polarization

At s=-5, let \(\epsilon=\theta\delta\) with fixed \(\theta>0\). Use the exact weighted-prime rate \(\lambda_{-5}(x)\sim\xi(5)e^{-5|x|}\) and the product asymptotic (9). The borderline integral is logarithmic:
\[
\int v_\delta(x)v_\epsilon(x)e^{-5|x|}dx
\sim4\pi^2\,2^{-9/2}\log(1/\delta).
\]
The source cross is bounded, and
\((\delta\epsilon)^{-5/4}/(\|v_\delta\|\|v_\epsilon\|)\to128/3\).
Therefore, uniformly in fixed positive scale ratios,
\[
\boxed{
\mathscr B_{-5}(\delta,\theta)
\sim 40\sqrt2\,\zeta(5)\log(1/\delta).}\tag{17}
\]
The leading divergence is independent of \(\theta\). It is the bilinear analogue of the sharp single-vector transition and cannot be inferred by simply setting s=-5 in (8).

## 6. How this enters the full RH problem

The true arithmetic energy **on known equality vectors** has a positive definite log-scale limit for every Mellin weight s>-5, with explicit Gamma-function spectral density and exact second-order continuous-jump balance. This supplies a concrete, two-variable multiscale identity that proposed global spectral positivity arguments must preserve.

It does **not** imply the full original Weil/Poincaré inequality for arbitrary even mean-zero q, does not exclude an actual subcritical eigenstate, and does not prove RH. Only the final complete zero-location statement is the target.

**Acceptance: unconditional two-scale true-prime auxiliary theorem, pending independent audit; NO NEW UNCONDITIONAL RH THEOREM PROVED.**

Provenance: original theta/Weil source and energy in rounds/04–05; true Hilbert translation singularity in REPORT.md; full weighted PNT jump-rate and actual Mellin moment theorem in PRIME_ENERGY_MELLIN_MOMENTS.md; sharp unweighted jump-rate expansion from round 05 §6.2. Gamma/Beta Fourier evaluation is proved explicitly in (12) rather than taken as a black-box positivity theorem. No formal verification or outside peer review claimed.
