## Round 96 — finite-interval self-adjointness does not identify the zeta spectrum

I checked Suzuki's August 2026 operator paper [*Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096). It gives a useful unconditional finite-interval construction: the localized Weil form has a self-adjoint Friedrichs operator \(A_a\). That fact alone is not the Hilbert--Pólya conclusion. The paper explicitly formulates as a conjecture the limiting identity
\[
 c_a\,\widehat v_a(z)\longrightarrow \xi\!\left(\tfrac12+iz\right)
 \qquad(a\to\infty),
\tag{96.1}
\]
where \(v_a\) is a lowest-eigenvalue eigenfunction of the finite-interval operator. Without locally uniform convergence, control of normalization and zeros, and an exact identification of the limiting spectrum, self-adjointness of every \(A_a\) does not imply that the zeros of \(\xi\) are real.

There is an independent circularity in the same framework. The associated continuous kernel is stated to be a screw function if and only if RH holds. Thus proving the needed global positivity of that kernel would already be an RH proof; the finite-\(a\) Friedrichs-extension theorem does not provide it. The paper also notes that the arithmetic terms must be analyzed to control the limiting eigenvalue and that this control lies beyond its unconditional finite-interval arguments.

**Established:** a rigorous self-adjoint finite-interval realization of the localized Weil form exists without assuming RH.

**Failure / missing step:** the global limit/spectral-identification statement (96.1), or an equivalent unconditional positivity theorem, is not proved.

**Route decision:** keep this as a reformulation of the same RH-bearing limit problem, not as a completed proof.

**RH status:** no unconditional proof has been produced.
