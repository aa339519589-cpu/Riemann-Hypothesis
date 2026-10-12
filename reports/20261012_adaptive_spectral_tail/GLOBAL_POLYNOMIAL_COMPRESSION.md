# Global even-polynomial compression for the exact high-frequency base

Status: independently reviewed mathematical supplement with independently rerun interval parameter budgets. This does not change the positive base, the prime cutoff, or the rigorous norm interpretation of the accompanying main theorem.

The exact changed positive base A, signed prime multiplier C_N, true source resolvent, complete norm-error formula and original operator-domain proof are those of [POLYNOMIAL_ACCURACY_TAIL.md](POLYNOMIAL_ACCURACY_TAIL.md), referred to below as the main theorem. The actual 3/8 bound in [CERTIFIED_GAP.md](CERTIFIED_GAP.md) uses a separate comparison and does not certify the matrix below.

Let Q=rho(D) have frequency support in [−2T,2T], let J be the actual source map for the exact positive base A, and suppose ||J||<=M. Let R=R0+d be as in the main theorem. For an integer r>=1, let Pi_r be orthogonal projection onto the even polynomials of degree at most 2r−2 on [−R,R], extended by zero outside that interval. This space has dimension r. One possible normalized basis is the even Legendre polynomials on [−R,R].

Then

    ||(P_R−Pi_r) QJ|| <= beta_r M,
    beta_r=(2TR)^(2r)/(2r)!.                              (1)

To prove this, g=QJu is even and band limited, so its odd derivatives at zero vanish. The Taylor polynomial at zero through order 2r−1 is therefore an admissible even polynomial of degree at most 2r−2. On [0,R] its integral remainder is convolution with x^(2r−1)/(2r−1)! on [0,R]. Its L1 norm is R^(2r)/(2r)!. Young's inequality, even reflection, and ||g^(2r)||_2<=(2T)^(2r)||g||_2 give (1). Orthogonal projection has no larger error than this particular comparison polynomial.

In equations (7)–(8) of the main theorem replace the local-cell error by beta_r M and rank n(p+1) by r. Thus

    ||K−F* C_N F||
      <=2c_N M [m_tail(R0)/sqrt(e)+ell_k(Td)M+beta_r M],
    F=Pi_r QJ.                                           (2)

Keeping the same first two budget conditions, it suffices that

    beta_r<=eta/(6 c_N M^2).                              (3)

This criterion uses a literal factorial and is convenient for rigorous numerical parameter selection. The elementary factorial inequality q!>=(q/e)^q also shows that

    2r>=max{4eTR, log_2[6c_N M^2/eta]}

is a sufficient explicit choice (here e inside 4eTR denotes Euler's number, not the positive spectral depth e=epsilon−delta_N). Consequently the rank can be chosen O(TR+log_+(c_N M^2/eta)), instead of the earlier product of a cell count and a logarithmic polynomial degree. The joint epsilon asymptotic remains subpolynomial for eta=c epsilon^a.

The resolvent Gram and signed finite matrix remain exactly those in the main theorem, now in the global even-polynomial basis. This is a change in approximation space only; no source domain, Gamma term, prime translation, or true resolvent is replaced.

## Reproducible parameter budgets

The companion script [certify_global_polynomial_budgets.py](certify_global_polynomial_budgets.py) uses mpmath.iv at 45 decimal digits. The full Gamma lower bound is rigorously sharpened for numerical parameter selection by retaining 32 exact positive terms and bounding the remaining decreasing sum from below by its integral:

 b(t)>=sum_(j=0)^31 (t/2)^2/[(j+1/4)((j+1/4)^2+(t/2)^2)]
              +(1/2)log[1+(t/(2(32+1/4)))^2].             (4)

It verifies the strict interval inequalities (1) and (9) of the main theorem, with (3) here replacing the cell-degree choice. The M^2 upper bound is rounded UP to an integer; the spatial radii are exact rational numbers. The factorial in (3) is evaluated as exp(2r log(2TR)−logGamma(2r+1)) with outward interval arithmetic. The script also recomputes the total bound (2) and checks it is below eta.

Run `python certify_global_polynomial_budgets.py` with Python 3 and mpmath (the independent integration rerun used version 1.3.0). The selected exact budgets in [global_polynomial_budgets.json](global_polynomial_budgets.json) are:

- epsilon=1/8, eta=1/32: N=3, sigma=1/100, T=65, k=14, R0=109/100, M^2<=15, r=373. Total tail <0.01085<eta.
- epsilon=1/64, eta=1/256: N=3, sigma=1/100, T=84, k=21, R0=124/100, M^2<=167, r=517. Total tail <0.001551<eta.
- epsilon=1/1024, eta=1/4096: N=4, sigma=1/100, T=132, k=27, R0=137/100, M^2<=1000, r=858. Total tail <0.00009273<eta.
- epsilon=1/1048576, eta=1/4194304: N=7, sigma=1/100, T=2489, k=40, R0=156/100, M^2<=4000, r=17332. Total tail <0.00000009567<eta.

The displayed decimal inequalities are intentionally slack summaries of the directed interval comparisons in the code, not printed endpoints being treated as exact rational bounds. No Gram entry or eigenvalue is evaluated by this script. For example, the first budget needs 69751 independent entries of a dense real symmetric Gram, rather than the 33296880 entries in the conservative piecewise-cell budget. At the fourth depth it still needs 150207778 entries, and dense interval evaluation remains substantial. The Gram is not certified simply because a dimension and a tail budget have been certified.
