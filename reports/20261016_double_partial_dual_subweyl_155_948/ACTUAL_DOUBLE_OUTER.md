# Actual order-thirteen phase and the eleven common-length rows

Status: actual-phase and outer assembly have passed independent internal review. The complete global theorem additionally uses the local lemma and the original-sum assembly in REPORT.md.

Let M,N>=2,c>0,F=2sqrt(cMN),s=10^(-30), and assume

(32+s)(8+s)MN/(4c)<=10^(-80).                                    (1)

Use the exact first-dual logarithmic phase

phi(x,y)=xy/2-2c[asinh sqrt(xy/(4c))
                  +sqrt(xy/(4c))sqrt(1+xy/(4c))].

Take one positive x difference and two positive y differences, with each total coordinate shift at most s times its scale. Their threefold difference f has scale

F3=F d1d2d3/(MN^2).

On [M/16,32M]x[N/4,8N], its leading model is

(F3/8)(x/M)^(-1/2)(y/N)^(-3/2).

Indeed the exact convergent series is

phi=xy/2-2sqrt(cxy) sum_(k>=0) a_k(xy/(4c))^k,
a_k=binom(1/2,k)/(2k+1), |a_k|<=1.

The bilinear term vanishes under these three differences. The model mixed derivative is (sqrt(c)/4)x^(-1/2)y^(-3/2). Differentiating the shift average through total order10 uses the underlying series through order13. Each nonzero falling factorial of1/2 through this order has absolute value at least1/4. The differentiated relative series error is bounded by

32*15^13*10^(-80),

because the majorant ratio is at most(16/15)^13*10^(-80)<1/2. The finite shift-average relative error is below500s: the smallest normalized coordinates are1/16 and1/4, and the sum of the relevant differentiated exponents is at most13. These bounds imply the entire relative C10 box of radius10^(-25), including signs. The checker verifies both endpoint inequalities exactly.

Any real added separable phase u(x)+v(y) is annihilated identically before this comparison. This is what licenses the arbitrary Fourier frequencies of the ORIGINAL curved cutoff. It does not replace either bounded-frequency cutoff inside the later two partial transforms.

Put

kappa=(M^14 N^23/F^7)^(1/89),
kappa>=2, 2kappa^4<=s min(M,N).                                 (2)

Take the same outer lengths H,H^2,H^4, H=floor kappa, with the first difference in x and the next two in y. The total y shift is at mostH^2+H^4<=2kappa^4. The inclusive-lattice recurrence gives

a0<=22H^(-1/2)+12(average a3)^(1/8).                             (3)

Every terminal scale F3 is at most F, so its logarithm is at most L=log(2+FMN). If F3<1, the trivial terminal count is covered by the local row MN/sqrt(F3); the local theorem is not used outside its phase-scale domain.

For each of the eleven local rows F3^k M^l N^m, normalization by MN and the common lengths gives the output

F^K M^J N^Z,
K=k/8-(7k/8)(7/89),
J=(7+l-k)/8+(7k/8)(14/89),
Z=(7+m-2k)/8+(7k/8)(23/89).                                    (4)

For k>=0 use average(d1d2d3)^k<=H^(7k). For the only negative exponent k=-1/2, retain average(d1d2d3)^(-1/2)<=8 H^(-7/2), followed by H>=kappa/2. Thus all rows use the SAME H; none is optimized independently. The diagonal22H^(-1/2) has exactly the powers of the first output row.

The full subrectangle bound is10^16 sqrt(L) times the sum of these eleven output rows:

name          K          J           Z
main          7/178      82/89       155/178
bx           15/356     163/178     2441/2848
by           15/356    2519/2848    1265/1424
inverse2      4/89     2503/2848    2491/2848
cap          35/712    2479/2848    4865/5696
short         0           1          15/16
constant      0           1           7/8
derivative2  25/534    1261/1424    3653/4272
log2          5/178    1255/1424    1229/1424
inverse1     -5/178    1415/1424    1441/1424
derivative1   5/267     715/712      463/534.                      (5)

The coefficient follows directly from12(10^100)^(1/8), the factor8^(1/8)2^(7/16) on the inverse row, and22sqrt2 on the main row. All are less than10^16. The exponent1/2 on L is the fourth power in the local lemma raised to1/8.

The exact-rational checker certify_double_outer.py verifies the actual derivative margin, every power in(4)--(5), and these constants. The original-scale complements and complete zeta sum are separate obligations, retained in REPORT.md rather than inferred from this local calculation.
