## Round 190 — A/B result: the Nicolas-criterion induction does not prove RH

**Source inspected:** Cheong Siong Chua, *Nicolas Criterion and Riemann
Hypothesis*, v5, record
<https://zenodo.org/records/20790544>, PDF downloaded as
/tmp/chua-nicolas-v5.pdf.

The stated Nicolas inequality uses
\[
 \frac{N_k}{\varphi(N_k)}
 <e^\gamma\log\log N_k+
 \frac{e^\gamma(2+\beta)}{\sqrt{\log N_k}},
 \qquad \beta=2+\gamma-\log(4\pi).
\tag{190.1}
\]
The manuscript's descending step is based on Lemma 4, which in its displayed
normalized form asserts
\[
 \left(1+a_k\right)
 \left(1+O\!\left(e^{-c_1\sqrt{\log p_k}}\right)\right)
 \mathrel{>}1+a_m,
 \qquad
 a_j=\frac{2+\beta}{\sqrt{\log N_j}\,\log\log N_j},
 \quad m=\lfloor k/2\rfloor.
\tag{190.2}
\]

The prime number theorem gives
\[
 \frac{\log N_m}{\log N_k}\longrightarrow\frac12,
 \qquad
 \frac{\log\log N_m}{\log\log N_k}\longrightarrow1.
\tag{190.3}
\]
Consequently
\[
 \frac{a_m}{a_k}\longrightarrow\sqrt2,
 \qquad
 a_m-a_k\sim(\sqrt2-1)a_k.
\tag{190.4}
\]
But
\[
 \frac{e^{-c_1\sqrt{\log p_k}}}{a_k}
 \asymp
 \sqrt{p_k}\,\log p_k\,
 e^{-c_1\sqrt{\log p_k}}
 \longrightarrow\infty.
\tag{190.5}
\]
Thus the unspecified \(O\)-term in (190.2) is asymptotically larger than the
positive gap that must be proved.  An \(O\)-bound has no sign; it cannot imply
the strict inequality in (190.2).  For instance, an error
\(-2e^{-c_1\sqrt{\log p_k}}\) satisfies the stated \(O\)-bound and reverses
the inequality for all sufficiently large \(k\).  The manuscript supplies no
separate signed lower bound for the actual Mertens-product error.

There is also a finite base failure in the manuscript's final paragraph,
which says that the displayed strict inequality is known for all
\(k<k_0=120569\).  A direct high-precision evaluation of the same displayed
formula at \(k=9\) gives
\[
 N_9=223092870,\qquad
 \frac{N_9}{\varphi(N_9)}
 =\frac{676039}{110592}
 =6.1129105179398148\ldots,
\]
whereas the right side of (190.1) is
\[
 6.0962709362222229\ldots.
\]
The difference is \(0.0166395817\ldots>0\), so the asserted “\(<\)” base
statement fails at this index.  This finite computation is used only as
counterexample discovery; it is not used as proof of any positive theorem.

Finally, even a valid implication
\(k\mapsto\lfloor k/2\rfloor\) proved only asymptotically would not yield the
claimed contradiction: repeated halving eventually leaves the asymptotic
range, and the manuscript supplies neither an explicit bound showing the
implication for every step down to \(k_0\) nor a verified base statement below
\(k_0\).

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

No complete unconditional proof of the Nicolas converse or of RH was
obtained.  This step did not produce a new unconditional RH proof progress.
