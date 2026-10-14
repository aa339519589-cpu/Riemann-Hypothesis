# Independent mathematical review: safe-xi Gamma–divisor coercivity

This review verifies the complete assembled proof in [REPORT.md](REPORT.md),
SHA-256 `3f7837ef7d9791e01e19c7ef2edd9cf65f8fcb36ec986bab533e2625925c9da9`.

## Result and exact scope

The complete proof supports

    G_tail[a] - D_div[a]
      >= 8*10^(-6) inf_c integral_(log2,infinity) W(y)xi(y)|a(y)-c|^2 dy.

This is a global comparison of the stated hidden component, including its
constant null mode and full mixed head/tail block. It applies first on the
stated core plus constants and then on the actual weighted-Sobolev
common-seed class, including finite polynomial theta-jet modifications.
It is not a proof of the full reflected original form or of RH.

## Independent complete-certificate reproduction

The compact checker was independently executed with a fresh outward W cache,
not a precomputed cache. All 999 interval boxes passed, with minimum lower bound
0.00023180687892906165. The head checker then used this freshly generated
cache; all 66 leaves passed, with minimum lower bound
0.12433724636438578. The head JSON agrees byte for byte with its stated
certificate. The cap, head-gap theta and complete analytic-tail constant
checkers were also independently executed successfully.

The checkers are interval proofs, not samples. The review checked:

* outward conversion of stored endpoints and coverage by all intersected
  cache cells, including the extra cells at range-query boundaries;
* exact prime-power factorization in log(n)-Lambda(n), one-sided W
  derivative bounds at integer knots, and the inactive zero branch;
* complete n>=9 theta tails rather than a finite theta approximation;
* preservation of the grouped h=0 cancellation by score ratios and an
  explicit omitted-row allowance;
* complete negative outgoing square-root tails, with positive omitted
  pieces discarded only in a lower bound;
* multiplication of rho by the genuine scalar lower bound, not by an
  artificial quadrature upper endpoint;
* coverage of the capped initial collar, the full head complement, the
  compact bulk and the analytic far tail without gaps.

## Arithmetic star reduction and coefficient budget

The conditional-variance identity retains its mean:

    D_star-D_div = 2 integral W_Lambda psi |R-a|^2 >= 0.

Collecting proper factors d*n=k with d,n>=2 gives L-W_Lambda, not L.
This row vanishes identically below log4. The exact W dilation and both
Schur rows give a residual norm less than 2*10^(-6), with forward,
incoming and outgoing-diagonal bounds respectively 24/20^6, 36/20^6 and
256/20^12. Its absolute bound is applied once, after the same global
constant subtraction used in the Gamma comparison. No prime budget or
conditional mean is spent twice.

## Capped ground and global constant projection

The auxiliary comparison is h=1+10^(-6)k, where k=min(m^(-1/2),1000) on
the first head and k=m^(-1/2) afterwards, m=W xi. Its cap is confined to
s<10^(-4) and contains s<=5*10^(-7). On the entire head,
1<=h<=1001/1000. The complete cap row is greater than -10^(-6) after
scaling. Outside the cap, reducing only the left comparison values
increases the positive-generator row, giving L_Gamma h/h>=rho V_Gamma.

The selected constant satisfies integral_head m(a-c)/h=0. Consequently
v=(a-c)/h has zero mean for exactly the m-weight used by the head gap.
The head estimate is 3/4000, not a normalized-mass or half-line variant.
The transformed positive kernel contains h(y)h(t)>=1. Keeping only its
head edges therefore gives 3/[4000(1001/1000)^2] times the head norm of
a-c; all discarded mixed edges are nonnegative.

The scalar potential is at least -10^(-4) on the head and 10^(-5) outside.
After the single 2*10^(-6) star error the remaining coefficients are

    3/[4000(1001/1000)^2] - 102/10^6 > 8*10^(-6),
    8*10^(-6) on the tail.

Both original forms are invariant under this one global constant.
No separate head and tail constants or deleted mixed block are used.

## All-domain passage

The auxiliary h is not an original-P trial source. Its pointwise rows
exist absolutely: the cap removes the left singularity, local Lipschitz
bounds pay the diagonal, and sqrt(xi/W) pays the remote future.
The absolute row integral of |1-h(t)/h(y)| is bounded on the capped
origin collar, locally bounded across the integer knots, and O(1+y) at
infinity. Splitting the separation at 1/z gives the last bound, with
log z=O(y). This supplies a uniform majorant for the separation-cutoff
potential, not merely convergence of its signed value.

For finite Gamma energy and integral (1+y)m|a-c|^2<infinity, dominated
convergence passes the potential pairing while monotone convergence
passes the nonnegative transformed kernel. The star residual is a bounded
L2(m) form and its multiplication row is at most y. These facts justify
the common-cutoff identity and inequality on the stated actual class,
including the noncompact constant introduced by centering. No
infinity-minus-infinity subtraction is licensed outside that class.

## Original-form interface and decisive neutral check

The coefficient-one identity remains

    q[f] = (G_tail-D_div)
           + T_E - H_Gamma^diff + P_pole - N.

The changed pole and every reflected prime edge remain. The future-prime
energy is canceled exactly once. A nonconstant anchored neutral theta jet
has q[f]=0 but strictly positive hidden component by the proved gap, so
the remaining original expression is strictly negative there. It cannot
be separately positive on the full lawful class. An actual-source or
neutral-projected joint comparison is still necessary.


## Pinned mathematical artifacts

The following SHA-256 hashes identify the complete reviewed proof and five
reproducible checkers. Their manifest [SHA256SUMS](SHA256SUMS) has SHA-256
`c7c010be6471a2370780b477b5decf85b7ed38b3e3b41e33045d66a424426987`.
Generated caches and run logs are not proof inputs.

- [BULK_COMPACT.md](BULK_COMPACT.md): `eceb57ff4ab2ead172e317a160502335001d79425c8f37f3406ffc97c408f3a9`.
- [BULK_RHO.md](BULK_RHO.md): `b8ff9fce7a786e3a09a2f996b37491c488ef8d3049be91f8ea0210383a8c51eb`.
- [BULK_TAIL.md](BULK_TAIL.md): `276075b49f202386d159978e0346b818257c6a22488049ef5a6c105580af0a6d`.
- [CAPPED_COMPLETION.md](CAPPED_COMPLETION.md): `191f41854c92a248acaaf4125edbcb87a0280c9bd37ad12abe7a89154c17681c`.
- [DIVISOR_PALM.md](DIVISOR_PALM.md): `855ad8d4e867f73d1fe210844957e370dba06f3fc426d0623fb7d6707c02eaa2`.
- [DIVISOR_STAR.md](DIVISOR_STAR.md): `38e2303369eeb4c3c97886cc69e50ed11b05a2f008db9074607d48cc129dec13`.
- [HEAD_GAP.md](HEAD_GAP.md): `367779d95e1144217fcb9f4d5a5770c6ac62504492c7f850e6228811c4b36e62`.
- [HEAD_SCALAR.md](HEAD_SCALAR.md): `ffe693f657ed6d8ecad25047e9ecda344466897941870cbb92793cfbf9e25688`.
- [ORIGINAL_INTERFACE.md](ORIGINAL_INTERFACE.md): `834a9e66a9e5b8976250b076ad6a681a3f47c2d68ab32e7aff8cac77be7ba507`.
- [REPORT.md](REPORT.md): `3f7837ef7d9791e01e19c7ef2edd9cf65f8fcb36ec986bab533e2625925c9da9`.
- [SAFE_RAY_FORMS.md](SAFE_RAY_FORMS.md): `1fae32e9aace03d616de6842c5b4f83d5c8c540760b8ca31569a489f9d024a2d`.
- [SOURCE_IDENTITY.md](SOURCE_IDENTITY.md): `fae94cc0014c22556ee390ba1ae5c7a3386d9304659f4a464299d05e7b86e956`.
- [certify_xi_bulk_constants.py](certify_xi_bulk_constants.py): `09f2d107439ffe1774c1c8821ae84ca31872ce9e994d3ba67aa434b063822829`.
- [certify_xi_compact_bulk.py](certify_xi_compact_bulk.py): `75e3188fa34d4158680872641827de9ddd764aaa234e517dd02147e6e948d456`.
- [certify_xi_head_theta.py](certify_xi_head_theta.py): `88f0cd114ecee544da1f99243ca854c14dcd4601f42bcb243d605113dbb38978`.
- [certify_xi_lyapunov_cap.py](certify_xi_lyapunov_cap.py): `03859971187e50562784bb87cb118f7d1902e736952ca19ef1f506371e3982df`.
- [certify_xi_lyapunov_head.py](certify_xi_lyapunov_head.py): `0e0c0f6d164f138c3a1c94af57c051020bb7114d846f1a951facb5cac704a67a`.

All package differences from the independently executed proof versions were
checked. They consist of focused exposition, local dependency/import names,
the explicit absolute-row domain argument, and an additional already
certified I0<1 assertion. The complete scalar computations are unchanged.
