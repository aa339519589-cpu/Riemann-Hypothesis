# Strict positivity of the exact two-load common-seed dual Gram

Keep the exact neutral convention, calibrated coefficients and full global
loads l_U,l_V of [the balanced-load theorem](CALIBRATION.md).
The two complete Riesz vectors in the common-seed tail metric are

    k_i(y)=A_(l_i)(y)/W(y),
    A_l(y)=sum_(n<=exp(y-b))n^(-1/2)l(y-log n),
    G_ij=integral_b^infinity [xi(y)/W(y)]A_(l_i)(y)A_(l_j)(y)dy.

Their finiteness follows from the exact endpoint and tail-constant balances
and the complete dual theorem. We prove the two by two matrix G is positive
definite. This is not a numerical lower bound on its smallest eigenvalue.

On the open interval (b,log3), the original prime-reflection row is the fixed
tail starting at label3. The same fixed-tail analytic argument used on the
head applies, but with 3 in place of 2. For x tending to minus infinity,
Z=pi exp(-2x), the continuation of the neutral loads obeys

    n_j(x)=2alpha_3 psi(log3-x)4^j(1-3^(4j))Z^(2j)
                                            (1+O(1/Z)).

The real ratio psi^(2j)/psi has its removable value at zero. All later
prime/theta rows have stronger Gaussian exponents, uniformly on compact
analytic-continuation intervals. Hence u=exp(x/2),n_1,n_2,n_3 are linearly
independent on (b,log3): the exponential u term cannot cancel the common
double-exponential scale, and the highest remaining polynomial degree in Z
cannot cancel its predecessors. This continues the FIXED tail with first
label3, not the changing piecewise row through other positive prime knots.

The exact calibrated l_U has u coefficient1 and l_V has n_1 coefficient5/787,
so these two loads are linearly independent on this interval. Moreover

    b<y<log3<2b  implies  A_l(y)=l(y),

because exp(y-b)<2 and only the prefix label n=1 is present. If a real
vector c satisfied c^T Gc=0, the strict positivity of xi/W for y>b would
force c_U A_(l_U)+c_V A_(l_V)=0 almost everywhere. Continuity on (b,log3)
would give c_U l_U+c_V l_V=0 there, contradicting the just-proved independence
unless c=0. Thus G>0.

In particular the exact joint dual estimate for an actual plateau source is
an ordinary inverse-Gram inequality, not just a pseudoinverse statement:

    h^T G^(-1)h <= inf_c integral_b^infinity W xi |a-c|^2,
    h_i=integral_0^b l_i f=-integral_b^infinity l_i f.

The full mixed original Q_delta tail form is still not bounded here. Neither
this strict dual Gram nor the two-load head certificate supplies that missing
signed remainder comparison by itself.
