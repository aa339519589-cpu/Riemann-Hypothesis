# Exact first-pole vanishing in the three negative cubic units

## Result and decomposition

Retain the physical probe and the finite-physical-e-first decomposition of [QUADRATIC_DUAL_N1, Part XXIV](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e62ca4aed10b99ed791e1b22aef791f35f61afe9/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md). Set eta=1 and

\[
 H=\varepsilon v_1^2v_2^4a^6,
 \quad\varepsilon\in\{-1,-\omega,-\omega^2\},
 \quad v_1,v_2\text{ coprime good squarefree},\quad v_1v_2\ne1.
\]

For each fixed admissible physical fiber, the specified first Gauss-series residue is zero at normalized s=5/6, equivalently at original norm-Mellin coordinate z=1/3. Thus the specified first-polar-then-second-remainder functional is identically zero for these three units. This retains all physical n,a,g,h, the actual finite e cutoff, both original and core marks, both exact first-flat operations, and the original finite compensation.

The proof applies the generic nine-channel theorem [CUBIC_NONCUBIC_LAMBDA](CUBIC_NONCUBIC_LAMBDA.md) to the exact moving character. It is unconditional and uses no Q input. Together with the existing three square-unit proof, the specified secondary term has the published bound Z^(-19/480+epsilon) for all six units. The whole first nonpolar remainder is still unestimated by this argument. Its definition is the original sector minus this zero polar functional, so the argument does not assert that the original negative-unit sector is zero.

## The actual bad Fourier vector and its convention

The original self-dual additive character is

\[
 e_o(z)=\exp(2\pi i\operatorname{Tr}(z/\lambda)),
 \qquad\lambda=1+2\omega.
\]

Let psi_4(c)=chi_4(Nc), primitive modulo (4), and keep the complete fixed bad vector A_epsilon on its genuine period M. Its 2-part is exactly (4); the primary selection, lambda data and bad masks are already inside this vector. Put

\[
 \widehat A_\varepsilon(h)=
    \sum_{b\bmod M}A_\varepsilon(b)e_o(hb/M).
\]

Write tau_epsilon(c)=chi_c(epsilon)=psi_4(c)tau_+(c), where chi_c here is the original sextic symbol and tau_+ is its cubic supplementary factor. For the good CUBIC character chi=theta_(v_1) conjugate(theta_(v_2)), whose actual good conductor is q=v_1v_2, the retained CRT/Poisson factors are exactly those of the physical source:

\[
 \frac{S}{q_M\sqrt{q_q}}\,
 \tau_\varepsilon(q)\chi(M\lambda)\gamma_D(\chi)
 \sum_h\widehat A_\varepsilon(h)\overline{\chi(h)}
       \widehat F\!\left(\frac{\sqrt S h}{Mq}\right).     \tag{1}
\]

The selector is included once. The factors chi(M) and chi(lambda) respectively come from Gauss CRT and gamma_o(chi)=chi(lambda)gamma_D(chi). No extra primary average or additive-conversion factor is appended. The Fourier vector may be kept intact rather than presumed to be one primitive lambda Gauss sum.

In the original additive convention,

\[
 \sum_{b\bmod4}\psi_4(b)e_o(hb/4)=4\psi_4(h),            \tag{2}
\]

with its zero extension on nonunits. In the literal trace convention of the theta source the scalar is -4. The change is accounted for by psi_4(lambda)=-1. In either convention the primal 2-divisible branch vanishes, and the dual h is a unit at 2. These finite identities are checked in [check_cubic_noncubic_twist.py](check_cubic_noncubic_twist.py).

## Moving character on each physical fiber

In the intact-bad-vector organization (1), the free source numerator is

\[
                    Z_0=\kappa j f^2c_2h.               \tag{3}
\]

The alternative expanded-bad-mask organization replaces A_epsilon by its mask-free vector and sums the original squarefree d with mu(d). Its substitution s=dv contributes tau_epsilon(d)chi(d), changes the actual scale to S/q_d, and hence contributes the original q_d^(-1) in the Poisson prefactor. Cubic covariance then gives Z_d=kappa d^2 j f^2 c_2 h. Use either this organization or (1), once; the d^2 factor is not appended to a vector that still contains that mask. Zero branches, including a 2-divisible d, retain their genuine zero extension.

Keep the f^2 phase, its genuine Fourier scale, the a mask, and the fixed v_2 factor. At a fixed physical n=n_0 r_phys^2 layer, split v_1=n_+g_+rho. Gauss CRT and the character covariance change the fixed factors into scalars and cubic residue factors on rho. The negative-unit norm character leaves the genuine free psi_4(rho), multiplied by the fixed psi_4(n_+g_+). It is not frozen by treating the old free s-column as a fixed t-column.

At the norm-four prime pi=(2), with the original orientation j_pi=1 or 2,

\[
 \theta_{v_1}(4)=\xi_\pi(v_1)^{j_\pi},
 \qquad\overline{\theta_{v_1}(\kappa)}\big|_\pi
                     =\xi_\pi(v_1).
\]

Hence the exact local multiplier on the free variable is

\[
            \psi_4(\rho)\xi_\pi(\rho)^{j_\pi+1}.        \tag{4}
\]

The cubic factor is conjugate(xi_pi) for j_pi=1 and principal for j_pi=2. The primitive quadratic factor survives both orientations. The character xi_pi factors through modulo (2), so its order divides three; it cannot cancel psi_4's conductor (4).

Reduce the remaining fixed residue symbols to their exact primitive cubic character chi_R, with R prime to 6, and choose R's primary generator, so 4R is primary. Remove principal components from its conductor while retaining their original zero masks. The free first-source coefficient then has the form

\[
 \frac{\gamma_D(\rho)}{\sqrt{N\rho}}\,
       \phi(\rho)\alpha_{k,\ell}(\rho),
 \quad\phi=\psi_4\xi_\pi^{j_\pi+1}\chi_R\pmod{(4R)},    \tag{5}
\]

up to fixed scalars, the exact finite holes and the original separated norm tests. The other physical moving phases are cubic. For instance the odd-prime factor containing rho^2 has the extra multiplier chi_p(rho)^(-6)=1 on either odd branch. Thus no physical square layer introduces an inverse psi_4 factor.

The residue character phi is primitive modulo (4R), and

\[
                  \left.\phi^3\right|_{(4)}=\psi_4\ne1. \tag{6}
\]

A concrete witness is y=lambda modulo 4 and y=1 modulo R. Its quadratic value is -1, while every other factor has cube one. Since y=1 modulo (2), it also witnesses that the primitive quadratic conductor at 2 remains (4).

## The exact nine-label match

On primary rho=1+a_2 lambda^2+a_3 lambda^3 modulo 9, the actual supplementary symbols give

\[
 \alpha_{k,\ell}(\rho)=\omega^{-ka_2+\ell a_3},
 \qquad k,\ell\in\mathbb F_3.
\]

In the notation of CUBIC_NONCUBIC_LAMBDA,

\[
 T=A+B\omega,\quad B=-k,\quad A=2(\ell-k)\pmod3,
 \qquad\alpha_{k,\ell}=\alpha_T.                         \tag{7}
\]

This is an invertible label map. The moving primary character is cubic and has period 9; higher lambda powers in M reside in the fixed Fourier vector in (1) or its fixed scalars. The actual free row has no angular character. Norm-Mellin phases are retained as vertical shifts of the same Dirichlet series.

Equations (5)--(7) match every hypothesis of the unconditional nine-channel theorem. Finite holes outside 3(4R) are its exact inclusion--exclusion case. A fixed good divisor forced into rho contributes only Gauss-CRT cubic factors and a scalar psi_4 of that divisor; after extraction the remaining character still has the restriction (6). A branch forced into a genuine character zero is zero before the residue. Both conjugated-Gauss orientations are covered by the correctly conjugated theorem.

The normalized Gauss series is therefore holomorphic at s=5/6, and its first residue vanishes. The original factor 1/sqrt(Nrho) shifts that coordinate to z=1/3. Smooth common norm separation does not restore a pole: the theorem supplies holomorphy on the whole open half-plane and polynomial vertical growth for each fixed modulus and mask.

## Order of the physical operations

The whole physical e-column is restricted first, before Poisson and the two specified extractions. The actual cutoff is

\[
                  q_{n_-}q_gq_j^2q_e\le C_1Y.
\]

It is a scalar on each fixed physical fiber and is common to the finite bad-vector calculation; it does not freeze psi_4 on the free column. All shared divisors, mixed-core numerators, actual nonunit zero extensions, and compact original tests remain. Original/core priority assignments add fixed good divisors or holes; they preserve (6).

For each first-flat scale, apply the same residue definition to its inner sector. The scale preserves epsilon,v_1,v_2 and contributes its original scalar and good cubic factors. Each of its polar summands is zero. This does not regroup unestimated first-remainder integrals or assert an infinite-family contour shift. The original compensation is a finite sum of the same zero functionals.

This proves the stated fiberwise and specified-secondary zero. The first remainder remains the original probe sector minus that zero functional. The distinct q=x+y=1 coupled-wall residue and its complementary surface are not identified with this ordered decomposition.

The exact physical source and its CRT matching are [QUADRATIC_DUAL_N1, Parts XXIV V--VII](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/e62ca4aed10b99ed791e1b22aef791f35f61afe9/reports/20261011_qrh_selection_bridge/QUADRATIC_DUAL_N1.md), using the [pinned September 30 probe](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex). The independent row audit is [REFEREE_NEGATIVE_CUBIC_FIRST_POLE](REFEREE_NEGATIVE_CUBIC_FIRST_POLE.md). No RH or complete first-remainder estimate is asserted.
