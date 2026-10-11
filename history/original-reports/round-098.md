## Round 98 — the Gram-Jacobi determinant argument fails before the spectral conclusion

I audited Yamaguchi's source manuscript [*Spectral Determinant of a Cutoff-Regularized Hamiltonian and the Riemann Zeta Function*](https://github.com/danalec/riemann), including the TeX source for Theorem II and its RH proof. The proposed Gram-Jacobi matrices are real symmetric at each finite \(N\), but the determinant comparison is not established.

There is an immediate error in Step 2 of the determinant proof. For \(z\notin\mathbb R\), the manuscript sets
\[
h_z(E)=\log(1-E/z)
\]
and claims, using a Weyl bound \(\lambda_k\gg k/\log k\), that
\[
|h_z(\lambda_k)|\le C/k.
\tag{98.1}
\]
This inequality is false: as \(E\to+\infty\),
\[
\log(1-E/z)=\log E-\log(-z)+o(1),
\tag{98.2}
\]
so its magnitude grows like \(\log E\), rather than tending to zero. Convolving with a de la Vallée Poussin kernel of mass one and \(O(E^{-2})\) tails does not turn logarithmic growth into a trace-class function; the convolution still has logarithmic leading growth. Thus the claimed dominated-convergence passage from the Paley--Wiener approximants to the trace of \(h_z(J_\infty)\) is invalid, and the trace formula cannot be extended in the way required for determinant exponentiation.

The later split into \(\log(1-z^2/E^2)\) does not repair this. To obtain the asserted inverse-square trace limit, the proof says that the trace formula applies to a cutoff version of \(1/E^2\), but no admissible approximation is constructed that controls the singularity near \(E=0\), the cutoff-removal term, and the simultaneous \(N\to\infty\) limit. A finite-section Weyl estimate alone does not provide that three-limit interchange.

There is also a circular use of RH in the Hadamard step. The manuscript writes
\[
\xi\!\left(\tfrac12+iz\right)
=\xi\!\left(\tfrac12\right)
\prod_k\left(1-\frac{z^2}{\gamma_k^2}\right),
\tag{98.3}
\]
after saying that the product pairs zeros at \(\tfrac12\pm i\gamma_k\). For a zero \(\rho=\beta+i\gamma\) with \(\beta\ne\tfrac12\), the centered zero of \(z\mapsto\xi(\tfrac12+iz)\) is \(z=\gamma-i(\beta-\tfrac12)\), not the real number \(\gamma\). Pairing it with \(1-\rho\) gives a quadratic factor with complex coefficients, not \(1-z^2/\gamma^2\). Consequently (98.3) is precisely the critical-line assertion the argument is supposed to prove. The definitions of \(\gamma_k\) as a complete zero list and the conclusion that all non-trivial zeros are \(\tfrac12\pm i\gamma_k\) therefore already presuppose RH.

Finally, the stated ratio convergence is only claimed on \(\mathbb C\setminus\mathbb R\) by the preceding resolvent argument. The manuscript then extends it across the real axis by saying that numerator and denominator have the same zeros “since the zero sets coincide in the limit”; that is the desired conclusion, not an established premise. Numerical ratios at finitely many zeros cannot supply the missing normal-family bound or zero multiplicity control.

**Established:** the proposed determinant proof contains a false trace-class domination estimate and uses the real-ordinate Hadamard product before proving that all zeros have real ordinates.

**Route decision:** discard this as a completed RH proof. The active target remains an unconditional exclusion of the Bombieri weighted null-cone alternatives.

**RH status:** no unconditional proof has been produced.
