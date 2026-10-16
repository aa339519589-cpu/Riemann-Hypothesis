# Littlewood denominator 19.875 from the unsplit finite sub-Weyl table

Status: complete proof, directed certificate and independent internal review completed.

## Theorem

For every real t with |t|>=3, zeta(s) has no zero in
\[
 \Re s>1-\frac{\log\log|t|}{19.875\log|t|}.                 \tag{1}
\]

This conclusion uses only the independently proved finite-height
[unsplit Patel–Yang table](../20261016_unsplit_py_subweyl_table/REPORT.md),
not the separate proposed global coefficient61. No critical-line proportion
or percentage of zeros is asserted.

## 1. Retained complete local inequality

We use the complete detector inequality proved and source-checked in the
[finite-strip19.95 report](../20261016_finite_strip_littlewood_1995/REPORT.md),
Sections1–5. The primary source is A. Yang,
[arXiv:2301.03165v2](https://arxiv.org/html/2301.03165v2), Lemmas4.1–4.8,
identity(4.65), and the complete derivation of(4.125). No isolated-zero,
reflected-zero, pole, right-integral or zero-count contribution is removed
when changing the critical-line input here.

In detail, D=46, b0=1, b1<=1.747088, b=sum(j=1..46)bj<=3.574410, and bj>=0.
Put L1=log(46t+1), L2=log L1 and V=L1-3.377. The source detector gives
\[
 b^{-1}\sum_{j=1}^{46}b_j\log(jt)\le V.                  \tag{2}
\]
Under the actual zero-free rectangle
\[
 1-\lambda<\Re s\le1,\quad t-1\le\Im s\le46t+1,
\]
and 0<lambda<=1-beta<=eta/2, lambda(R+1)<=eta, R>=100, the full inequality is
\[
 .17996-.20523\left(\frac{1-\beta}{\lambda}-1\right)
 \le\lambda\left\{\frac{.087\pi^2b_1(1-\beta)}{\eta^2}
                 +\frac B{2\eta}+c(R)\lambda T\right\},   \tag{3}
\]
where c(R)<=1+10.05/R. For 2/7<=eta<=1/2,
\[
 T=b[(.891+.6079\nu)V+(.7813+.58\nu)L_2+7.329+3.898\nu]+1.8,
 \quad\nu=(\eta^{-2}+(1-\eta)^{-2})/2.                    \tag{4}
\]
Only B is altered. The right integrals retain log zeta(1+eta), and the
source's discarded count coefficient remains negative for this eta range.
The finite program rechecks the fixed detector theta bracket and c(R)
coefficient, not a newly optimized detector.

## 2. Finite-strip input over the complete integrals

Use the same harmonic barrier proof as the19.95 report, now for
63<=x=log t<=215. For every harmonic center tau=jt,1<=j<=46, consider
1/2<=sigma<=5/7, |y-tau|<=1000. The uniform Euler bound
\[
 |\zeta(\sigma+iy)|\le6(1+|y|)
\]
holds throughout the strip for all real y. Since log6+log(1+46e215+1000)<223,
the barrier
\[
 H=\sqrt2\,223\,
 \frac{\cos((7\pi/3)(\sigma-17/28))\cosh((7\pi/3)(y-\tau))}
      {\cosh(1000(7\pi/3))}
\]
pays both horizontal sides and is nonnegative on both vertical sides.
Its central value |y-tau|<=32 is below10^-1000. All tau±1000 exceed exp60
because exp63-1000>exp60. The maximum logarithmic displacement is now
\[
 \epsilon_{\log}=-\log(1-1000e^{-63})<10^{-22}.            \tag{5}
\]
The same subharmonic maximum principle is therefore valid on every rectangle.
No global vertical estimate is inferred from a finite table.

On a closed certificate cell [l,r] contained in[63,215], choose the least
j with r+log46+10^-20<65+5j, require j<32, and use the new table coefficient
A_j. The coefficients are strictly increasing, as the verifier checks.
Consequently this ONE coefficient bounds all finite table intervals touched
by all46 rectangles throughout the cell. Put
\[
 G(v)=\frac{27}{164}v+\log A_j,
 \qquad F(v)=v/14+\log v+\log1.546,
 \qquad \alpha=(14\eta-4)/3.
\]
On v>=60 these functions are positive, increasing and concave, and their
derivatives are at most1. The harmonic barrier and(5) therefore bound the
central part of
\[
 I_\eta(\tau)=\frac12\int_{\mathbb R}
 \log|\zeta(1-\eta+i\tau+2\eta iu/\pi)|\,\operatorname{sech}^2u\,du
\]
by alpha*G(log tau)+(1-alpha)*F(log tau)+epsilon_log+10^-1000.
The central upper bound is positive, so its kernel mass may be enlarged to1.
For |u|>100 the whole-strip Euler estimate gives the envelope223+|u|;
both infinite tails together are at most
\[
 4\int_{100}^{\infty}e^{-2u}(223+u)du
 =2e^{-200}(323.5)<10^{-80}.
\]
The checker verifies that the sum of all three debits is below10^-20.
Using the SAME G for every harmonic, (2) and Jensen give
\[
 B\le b[\alpha G(V)+(1-\alpha)F(V)+10^{-20}]
       +\log\zeta(1+\eta).                               \tag{6}
\]
This is the only new local witness. All finite-table transitions and the
upper log-height220 are retained explicitly.

## 3. Unchanged unbounded-height witnesses

Outside the finite-strip range the verifier uses only the original
integer-k witnesses, k=4,...,14, eta=k/(2^k-2), from Yang's complete proof:
\[
 B=b[V/(2^k-2)+L_2+\log1.546]+\log\zeta(1+\eta),
\]
\[
 T=b\left[(23.99/\sqrt\eta-40.051)V+1.2031L_2-38.58
       +(2.0373L_2-.5322\log\eta)/\eta^2\right]+1.8.        \tag{7}
\]
Their entire half-line integral hypotheses and all contributions were
verified in the preceding20.4/20.1/19.95 chain. No global interpolation from
the new finite table is used. The program checks the multiplied main and
tail brackets are positive before replacing b by its outward upper bound.

## 4. Genuine minimizing zero and the height splices

The independently established [classical4.79 theorem](../20261016_littlewood_feedback_479/REPORT.md)
pays the low heights because
\[
 4.79\log63<19.875.
\]
The published MTY Vinogradov–Korobov denominator55.241 pays the high tail:
\[
 10^6/(\log10^6)^4>(55.241/19.875)^3,
\]
and x/(log x)^4 is increasing for x>=10^6. The primary source is
[MTY Theorem1.1](https://link.springer.com/article/10.1007/s40993-023-00498-y),
version-pinned [arXiv:2212.06867v1](https://arxiv.org/abs/2212.06867v1).

If(1) fails, the positive global infimum M of
(1-beta)log t/log log t over zeros with t>=exp63 is less than1/19.875.
It is attained in the remaining compact range, by the existing positive
zero-free seed and the MTY tail. At a minimizing zero take
\[
 1-\beta=M\log x/x,\qquad \lambda=M L_2/L_1.
\]
Global minimality supplies the complete local rectangle in Section1. The
possible lower sliver t-1<exp63 is paid by the strict classical splice.
This does not assume the proposed improved region as its own rectangle.

The directed verifier substitutes the worst allowed M=1/19.875, retaining
the inherited relative slack10^-20. Both sides are treated in exactly the
monotonic directions proved in the base report. Every cell checks all domain
conditions, R>=100, both bracket signs and strict positivity of the complete
margin of(3). Floating arithmetic proposes a candidate witness only; Arb
interval arithmetic alone accepts a real closed cell.

The terminal certificate has996 accepted closed cells after1976 evaluations,
no unresolved interval, and minimum directed margin greater than
5.6144572076530e-7. Exact rational endpoints cover[63,10^6] without a gap.
Together with the two splices and conjugation this proves(1).

## Reproduction and scope

Run `python certify_transfer.py` with python-flint0.9.0 / FLINT3.6.0.
The program uses160-bit Arb arithmetic and writes the scientific summary
and full rational witness JSON. It requires no unproved global61 input.
The finite critical-line table is a proved dependency with its own complete
32-row checker. No finite-height bound is extended across an unbounded
integral without the Euler-tail payment above.
