# Independent explicit-tail review for the unchanged 127-column certificate

Review completed 2026-10-12 09:00 UTC, Approved as a correction/expansion of the fixed tiny-remainder ledger, without changing the published single-depth conclusion L>=511/1024.

Reviewed mathematical source: the mathematical text reproduced in [MULTIBAND_TINY_TAIL.md](MULTIBAND_TINY_TAIL.md), SHA-256 82e7a72b2e8bef9c0e90b67ccb338b546d24a6fafff84b203fa9d70bc1f2fe56. The unchanged program is certify_hardband_continuous_residual_v4.py, SHA-256 43e08e869b08f0097bd1b06721ae5e2d76a383de6b9eba026f64e449451e1312. I independently reread its full code and the analytic manuscript's Sections 5–6, with all norms and line references matched. The explicit rational constant comparisons were independently checked and passed; the displayed inequalities in the supplement give their complete mathematical content.

## Actual objects and allocations

The input used in the computed cross lattice is the whole-line extension m(x) tilde_phi(x) of the 127 compact carrier functions. There are ten bands and the vector row satisfies ||tilde_phi(x)|| <= sqrt(10) exp(2|x|). It is not the periodic input of the 373-column program. The hard-band operator is evaluated through actual finite-band Fourier integrals, not a periodized Q^2 C_N kernel.

The genuine compact-input correction EF is separately paid in the residual and cross Gram at lines 89 and 95. The new tail ledger does not absorb or omit it. The unweighted Gaussian contribution is likewise separately paid by outY and |e0|outY^2.

The following envelopes use the program's actual directed assertions A0<1000, A1<100000, synthesis coefficient-row sum S0<10^8. They are row Euclidean bounds, so no uncharged factor of 127 occurs.

## Verified explicit bounds

For M(x)=9 exp(2x-(3/2) exp(2x)), M(4)<2^-3733. Both M and exp(2x)M decrease with logarithmic derivative at most -1 for x>=4. This gives continuous and omitted-lattice L1/L2 bounds for both meshes, retaining the endpoint samples.

1. The non-Gaussian residual tail is below 2^-3705, paying the 10^-500 at line 63.
2. The actual extended-input cross-lattice tail is below 2^-3707, paying the independent 10^-100 at line 95.
3. The m-weighted energy-lattice tail is below 2^-3695, paying the independent 10^-100 at line 96. The Gaussian-only energy is still explicit.
4. The entire source-lattice tail is below 2^-3722. Grouping indices modulo 10240 gives period 80 exactly. The cosine coefficient factor is at most 2/80; 5121 coefficients and |b(t)-C4(t)|<2^23 for t<=128pi yield synthesis error below 2^-3686. This is distinct from the already paid analytic Fourier aliases.
5. The exact positive band weights have total width 67/4. Their absolute C4-weighted mass divided by pi is below 128. This bounds omitted source samples and the true remote hard-band output without assuming exponential decay of a sharp-band kernel. The stored synthesis row is bounded separately, and the global numerical coefficient error remains paid.
6. Every local-prime nonzero source-period image has shift 80j+lambda, |lambda|<=log4. The genuine global operator bound ||m tau_s m|| <= ||m||_infinity M(|s|/2), followed by the full geometric image sum, gives an error below 2^-3713. There is no hidden remote region in this bound. The full b-periodization estimate already applies globally.

All operator-action contributions in items 4–6 fit the 10^-100 at line 88, before its subsequent multiplication by the explicitly bounded trial norm in energyErr. Every displayed tiny sum is below 2^-3600 < 10^-1000. Thus both types of existing tiny allowances are sufficient. The proof previously named these objects but did not expand their fixed constants into this ledger; the supplement now does so.

## Scope and record

No trial, table, numerical output, program, residual threshold, Gram matrix or signed inertia has changed. This is an analytic audit of the omitted tails; it does not pretend to rerun the already independently executed four-program numerical chain. That prior full rerun remains recorded in [REFEREE_CERTIFIED_MULTIBAND_GAP.md](REFEREE_CERTIFIED_MULTIBAND_GAP.md). Together they preserve its single epsilon=1/1024 theorem.

A separate public link from the 127-column report and review to this explicit-tail supplement is appropriate. The user's 373-column lemma must not be cited as if it alone applied to this different implementation. Neither supplement supplies uniform epsilon control, the critical 1/2 inequality, or a new zeta-zero exclusion.

Final status-only snapshot: explicit_127_omitted_tail_audit_reviewed.md, SHA-256 59728707600b0f52fb5d511213792f2036e33fd2cc5ee6ae056bf5d9c7378487. Only the source status changed after review; the mathematical content reproduced in the public supplement is unchanged.
