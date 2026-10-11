## Round 152 — visual correction: the determinant central subtraction is at \(w=0\)

I checked the original page image of the latest v2.4 PDF after text
extraction appeared to show a subtraction at the reflected point
\(\frac12-w\).  The printed Lemma 6.145 (PDF physical page 272, printed
page 271) actually states

\[
 \partial_w\log F_K\!\left(\frac12+w\right)
 -\partial_w\log F_K\!\left(\frac12\right)=G_K(w),
\]

and the preceding Lemma 6.110 (printed page 247) makes the same central-
point subtraction for \(\xi\).  With

\[
 F_K\!\left(\frac12+w\right)
 =e^{a_{EF}+b_{EF}w}\det_2(I+iwK),
 \qquad
 G_K(w)=w\operatorname{Tr}\!\bigl((I+iwK)^{-1}K^2\bigr),
\]

the displayed calculation \(\partial_w\log F_K(\frac12+w)=b_{EF}+G_K(w)\)
and \(G_K(0)=0\) is algebraically correct.  Thus the apparent objection based
on interpreting the second term as a reflected-point logarithmic derivative,
and the resulting proposed odd-trace gap, is withdrawn; it was caused by PDF
text extraction, not by the source page.

This correction does not repair the load-bearing scalar step in Lemma 6.129.
The remaining question is still whether the ordinary scalar coefficient
\(\Psi^{\mathrm{sc}}_{M,\ell;N}\) is actually represented by the finite readout
ledger in a way that justifies the trace contraction.  That question is
independent of the corrected central subtraction.

**Established:** the v2.4 determinant central subtraction is at the central
point, and the local \(K\)-side logarithmic calculation is not rejected on
the proposed evenness ground.

**Remaining load-bearing statement:** define and prove the ordinary scalar
finite-ledger projection/coefficient identity used in Lemma 6.129, then close
the scalar explicit-formula comparison and the global determinant identity.

**RH status:** no unconditional proof has been produced.
