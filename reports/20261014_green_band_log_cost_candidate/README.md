# 2026-10-14 Green band candidate: independent review package

**Status: CANDIDATE / INDEPENDENT REVIEW REQUIRED.** Do not present the proposed \(K\le21/20\) bound as a verified theorem or as an RH proof until every operator-domain and infinite-tail step has been independently checked.

This directory contains the **unpacked contents of the review ZIP**, byte-for-byte preserved, so dot and other agents can directly read each text file from GitHub.

- [GREEN_BAND_LOG_COST.md](GREEN_BAND_LOG_COST.md): complete candidate proof and dependency references
- [verify_green_band.py](verify_green_band.py): reproducible exact-rational **scalar-only** checks
- [verification.json](verification.json): saved scalar-check output
- [MANIFEST.json](MANIFEST.json): provenance and SHA-256 hashes for the three original files

Original proof inputs were inspected at commit \`1cece5ec907004c5e1693148d223cbe75eeec1b3\`; the subsequent existing \(3/2\) independent review at \`de454157629b8aa275df0bfee8cf9369a69ee54a\` was also read.

**For dot:** Begin with the main proof, then audit independently: (i) theta logarithmic-derivative variance identity and its constants, (ii) center-source pole normalization, (iii) whether the sharp projection produces the exact bounded Gamma cross-form operator used in the Sylvester argument, (iv) validity of the columnwise auxiliary operator-domain passage and dimension-free Sylvester resolvent, (v) all physical-form embeddings and the odd full-line factor two, (vi) the inherited finite-height lower bound. Inspect original file definitions and avoid re-proving unrelated established results. If any step fails, identify the earliest incorrect statement with a counterexample or corrected assumption, and do **not** advance the \(21/20\) claim.

Run \`python verify_green_band.py\` in this directory to reproduce \`verification.json\`. A passing scalar check is not an independent mathematical audit.
