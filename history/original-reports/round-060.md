## Round 60 — \(\Xi\) is not of finite exponential type

The Paley--Wiener invocation in the same manuscript has a separate
hypothesis failure. The paper treats

\[
 \Xi(t)=\xi\!\left(\tfrac12+it\right)
\tag{60.1}
\]

as if its real-axis decay implied that it is an entire function of finite
exponential type. It is not.

Take \(t=-iR\) with \(R\to+\infty\), so
\(s=\tfrac12+it=R+\tfrac12\). From

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\tag{60.2}
\]

and \(\zeta(R+\tfrac12)\to1\), Stirling's formula gives

\[
 \log\left|\Xi(-iR)\right|
 =
 \frac{R}{2}\log R+O(R).
\tag{60.3}
\]

In particular,

\[
 \frac{\log|\Xi(-iR)|}{R}\longrightarrow+\infty,
\tag{60.4}
\]

so no constants \(C,\tau\) can satisfy
\(\lvert\Xi(z)\rvert\leq C e^{\tau|z|}\) on the whole complex plane. The
finite-exponential-type premise required by the Paley--Wiener theorem
invoked in the manuscript is absent. Real-axis decay alone gives no
Gaussian inverse-transform bound.

This is independent of the explicit counterexample in Round 59: even if the
particular theta kernel were separately shown to have Gaussian decay, the
manuscript's universal nonvanishing lemma would remain false.

**Established:** the actual \(\Xi\)-function has superlinear logarithmic
growth along an imaginary direction and is not finite exponential type.

**Failure / error:** the claimed Paley--Wiener upgrade from real-axis decay
to Gaussian decay is unavailable under the function's actual growth.

**RH status:** this candidate is not an unconditional proof.
