## Round 135 — correction of the compact-support sign diagnostic

The Round 134 computation has one bookkeeping correction.  If \(F\) is
supported in \([-4,4]\), then \(C_F(a)=0\) for \(a\ge8\), but the numerator
in the second integral of Definition 3.2 is still \(-C_F(0)\) there.  The
analytic tail omitted from the first diagnostic run is
\[
 2C_F(0)\int_8^\infty\frac{da}{e^{2a}-1}
 =-C_F(0)\log(1-e^{-16}),
\]
which enters \(D_\infty(F)\) with a positive sign.  For the stated test,
\(C_F(0)\approx0.4747148449468\), so this correction is only
\(5.3422121024\times10^{-8}\).

After including that tail, the independently refined compact correlation
calculation gives
\[
\begin{array}{c|c}
\text{grid spacing }h & \text{corrected computed }D_\infty(F)\\
\hline
0.004 & -0.249968062666\\
0.002 & -0.249968062704\\
0.001 & -0.249968062706\\
0.0005& -0.249968062707
\end{array}
\]
Thus the sign and the high margin are unchanged.  This correction is why the
Round 134 table is treated as a numerical diagnostic rather than a finished
interval certificate; any formal refutation of Proposition 6.1 must include
this analytic tail and bound all remaining quadrature errors.

**Established:** the support-outside tail has been identified exactly, and
including it leaves the compact-test sign stably negative in the diagnostic.

**Remaining load-bearing statement:** turn the corrected calculation into a
rigorous interval enclosure, or identify a stated hypothesis in Proposition
6.1 that excludes the test.  Until then this is strong evidence of a finite
proposition failure, not itself the final formal counterexample.

**RH status:** no unconditional proof has been produced.
