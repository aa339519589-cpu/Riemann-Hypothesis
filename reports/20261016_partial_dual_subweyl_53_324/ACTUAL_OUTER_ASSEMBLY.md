# Actual order-eleven comparison and the complete outer mixed-A ledger

Status: complete local assembly with independent internal review. The full original zeta sum is assembled in REPORT.md; this appendix alone is not a global theorem.

Let M,N>=2, c>0, F=2sqrt(cMN), s=10^(-16), and assume

(3+s)(4+s)MN/(4c)<=10^(-40).                                    (1)

Use the exact first-dual logarithmic phase

phi(x,y)=xy/2-2c[asinh sqrt(xy/(4c))
                     +sqrt(xy/(4c))sqrt(1+xy/(4c))].

For one positive x-shift and two positive y-shifts with each total coordinate shift at most s times its scale, let f be their threefold forward difference. Then f satisfies the partial-dual lemma's C8 hypothesis on[M,3M]x[N/2,4N], with scale

F3=F d1 d2 d3/(MN²).

Indeed the exact series is

phi=xy/2-2sqrt(cxy) sum_(k>=0) a_k (xy/(4c))^k,
a_k=binom(1/2,k)/(2k+1), |a_k|<=1.

The linear/bilinear term vanishes. The leading mixed derivative is

partial_x partial_y² phi0=(sqrt(c)/4)x^(-1/2)y^(-3/2),

so averaging over the three shifts gives the model (F3/8)X^(-1/2)Y^(-3/2). To differentiate this average through total order8 requires underlying derivatives through order11. The denominator falling factorials of1/2 are each at least1/4 in absolute value. For every such derivative, the relative series tail is at most

32*12^11*10^(-40),

because the successive majorant ratio is at most(13/12)^11*10^(-40)<1/2. The positive model shift averages differ from the unshifted derivative by at most24s relatively on X>=1,Y>=1/2. Thus the full relative error is below10^(-12), including every sign required in the C8 hypothesis. The same conclusion holds after adding ANY real separable phase u(x)+v(y) to phi: the terminal mixed difference annihilates it identically before the partial Poisson transform is applied.

## Common lengths and all five propagated rows

Put kappa=(M^4 N^7/F²)^(1/30), and assume

kappa>=2, 2kappa^4<=s min(M,N).                                 (2)

Use H=floor kappa and three outer lengths H,H²,H⁴, with the first shift in x and the two subsequent shifts in y. The full normalized inclusive-lattice A recurrence from the accepted mixed-coordinate appendix gives

a0<=22H^(-1/2)+12(average a3)^(1/8).

All three diagonal terms and the terminal coefficient are retained. The total y-shift is at most H²+H⁴<=2kappa⁴, so(2) applies to every phase, not just an average shift.

Write L=log(2+FMN), C=10^40. If F3>=1 the partial-dual lemma, divided by MN, gives

a3<=C L² [F3^(1/2)M^(-1/2)N^(-3/4)
                  +N^(-1/2)+F3^(-1/2)+F3^(1/3)/N+1/N].

We used F3<=F. If F3<1 the same right side dominates the trivial lattice count<=9/4, so no small-F3 omission occurs. Averaging the three lengths gives respectively

H^(-4), N^(-1/2),
8 F^(-1/2)M^(1/2)N H^(-7/2),
F^(1/3)M^(-1/3)N^(-5/3)H^(7/3), N^(-1).

For the inverse row use Q^(-1)sum_(d<Q)d^(-1/2)<=2Q^(-1/2) independently at all three levels. The leading row follows from kappa^(15/2)=M N^(7/4)F^(-1/2). All positive power averages are bounded by their maximum; no term is optimized using a different H.

Taking the eighth root subadditively and using kappa/2<=H<=kappa proves, uniformly over every subrectangle and every separable added phase,

|sum e(phi+u+v)|<=10^7 L^(1/4) sum_j F^(k_j)M^(l_j)N^(m_j),       (3)

with the complete five rows

j        k_j       l_j       m_j
main     1/30      14/15     53/60
boundary 0         1        15/16
endpoint -1/30     241/240   491/480
derivative 1/45    359/360   619/720
constant 0         1        7/8.

The endpoint and derivative rows use the SAME kappa as the main row. The finite certificate checks their exact rational exponents and the outward coefficient10^7. In particular the M sqrt(N) boundary row of the partial-dual lemma survives as M N^(15/16); it is not removed by an invented inverse-range restriction.

The original first-dual curved boundaries can now use the already proved arbitrary-frequency Fejer lemma: the three outer mixed differences kill its full separable twist before any new partial B operation. This is different from the bounded-frequency inner cutoff, whose complete extra debit is already present in the partial-dual lemma.
