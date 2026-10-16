# Independent internal mathematical and computational review

This review concerns the following frozen files:

- REPORT.md: SHA256 6c0008dc653457eb28846840427f8c5268d31c74de6f1f59070115a7d5e1edec
- frontier8192_certificate.json: SHA256 db89bd57816bce9041b9f6f3d3157e41107723c1685455e503a0732f77cfa773
- verify_block_certificate.py: SHA256 d4650f5efcc35185472cac9a5709fb970feddd6a1302759dbe917328ee45fe80

The complete written proof and verifier were read. The exact rational ordering, endpoint convention, nonzero signs, sign alternation, independent total multiplicity counts, and the logical exhaustion argument were checked. Shared nonzero sample endpoints do not compromise disjointness of the open sign-change intervals. Equality of their number with the total multiplicity-count difference proves simplicity as well as critical-line location.

A separate complete replay used 160-bit Arb arithmetic and four workers. It recomputed all 8,193 signs using the Gamma/absolute-Gamma phase, rather than the generating log-Gamma phase. Every sign was nonzero and matched the certificate. The two exact counts were 12,363,153,437,138 and 12,363,153,445,330. The replay returned PASS for all 8,192 intervals in 481.38 seconds. The replayed verifier and the staged verifier differ only in the latter's default sibling certificate path; no mathematical calculation differs.

The cited Platt--Trudgian endpoint and the version-pinned FLINT count contract were inspected. The latter counts all nontrivial zeros with multiplicity, not only located critical-line zeros. The computation retains the documented FLINT/Arb and hardware trust boundary and does not claim a Lean-kernel or integer-only proof.

The exact new upper endpoint is 1,536,089,771,373,645/512. The interval includes the earlier 32-zero certificate, so its additional coverage beyond that certificate is 8,160 zeros. The report correctly claims a finite extension, not a proportion theorem, an exhaustive world-record assertion, or RH.

This is independent internal review, not external peer review or an institutional endorsement. No correction is requested for these pinned files.
