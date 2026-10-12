# Independent review of the user's full-Gamma omitted-tail correction

Review completed 2026-10-12 09:00 UTC, Approved for the stated 373-column certificate at epsilon=1/8.

The user supplied this correction in commit e4326b0a16552c2de3024754d25721cea8ffbddf. Authorship of the patch remains the user's. The user-authored mathematical source is [FULL_GAMMA_TINY_TAIL.md](FULL_GAMMA_TINY_TAIL.md), SHA-256 197e7f9dca0cfc4583318d64071a352cb5812203d8dc2d7a2d36dff5af136b78. Its accompanying review has hash ee93ea62932ea6492e8dde08aa93d8dd142cf7fce8f4f7e4d496736c57bfa2dd, and the rational checker has hash 32e95cee0289b826757b55b7069fc8ed4f4f80775047855c82589b1235edbf8c. The checker was independently executed and passed. This execution verifies its constant comparisons, not by itself the analytic proof.

## What was missing

The original continuous code had already charged generic tiny remainders, but the original proof had not explicitly bounded three required objects: the omitted computed cross lattice, the input-period difference on |x|>20, and the Q^2 C_N nonzero-image output on |x|>24. They are genuine required proof components. In particular the computed cross lattice contains the exact periodized input row; the whole-line unperiodized Bessel bound cannot silently replace it.

I independently reread the actual code certify_continuous_residual_components.py, SHA-256 f113960822cf08b1dc5a27f9b010450f6fbda3cd95b413f9200a71bff18c4ca1, and matched these terms to its inputPeriod, q2Period, crossError and residual allocations. The immutable actual dyadic input was opened independently: its shape is 1274 by 373, denominator 2^42, maximum absolute numerator 118174228126, strictly below 2^37.

## Analytic verification

The full theta envelope gives the stated continuous and right-Riemann lattice tails, with the samples at +/-4 retained. The squared-tail integration has exactly the factor Astar exp(-pi E)(E/pi+1/pi^2). The stronger pointwise bound m_env(4)<2^-3733 follows from the positive exponential series; no truncated numerical theta sum is used.

The exact periodic input has fewer than 2^12 supported frequencies. The normalized input L1 bound, its 1/(2L) Fourier normalization, and the actual dimension give a global row bound below 2^13. The independently bounded midpoint coefficient row sum below 10^6 also safely yields cross-tail bound 2^-3698. This pays the computed periodic cross lattice, rather than a different input.

The whole-line input row bound below 7 and periodic row bound give the remote input error below 2^-361 after multiplication by m. For Q^2 C_N, the previously proved absolute periodized K*K bound below 4T, the actual signed finite translation L1 norm c_N<8, and ||mY||_L1 <= S0 ||m||_1 give the remote-output error below 2^-348. The source convolution tail, central images, separate local C_N images and numerical coefficient errors remain distinct previously charged terms. The unweighted Gaussian trial tail remains its explicit much larger separate term.

Thus the missing pieces total less than 2^-347 < 10^-100, including charging both the continuous cross integral and omitted cross lattice if desired. The code already contains sufficient separate allowances. No matrix, interval result, inertia bound or numerical threshold changes.

## Conclusion and precise correction scope

The published original even mean-zero gap L>=3/8 remains justified with this explicit supplement. The original report and corresponding review should directly link the user's FULL_GAMMA_TINY_TAIL.md and acknowledge the missing explicit ledger. This is a proof correction/expansion, not a new spectral bound. The lemma does not establish an all-epsilon result or any new zeta-zero exclusion.

The 127-column certificate uses different inputs and a nonperiodized hard-band integral. It is not covered by this lemma. A separate direct audit is recorded in [REFEREE_MULTIBAND_TINY_TAIL.md](REFEREE_MULTIBAND_TINY_TAIL.md).
