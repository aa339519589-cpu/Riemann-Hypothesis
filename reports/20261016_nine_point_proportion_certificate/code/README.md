# Reproducing the nine-point local certificate

This directory contains independently authored verifier/build code and explicit
mathematical data. It does not execute the cited author's Lean program or trust
its numerical acceptance results. The compressed partition and anchor hints are
untrusted inputs: coverage and every local inequality are checked anew.

## Requirements

- Python 3 without `-O` or `PYTHONOPTIMIZE` and the official `python-flint==0.9.0` distribution (FLINT 3.6.0 in the
  tested environment).
- A C++17 compiler supporting signed `__int128`; g++ 14.2.0 was tested.
- No network connection is required after obtaining those ordinary dependencies.

Use an existing Python environment with python-flint, or create one with the
official PyPI package. From this directory run:

```
PYTHON=python3 CXX=g++ bash reproduce.sh
```

The script unpacks mathematical hints, independently proves their binary cover,
checks the exact constants, regenerates all 1,048,576 scalar and jet cells, checks
all upper-curvature cells and analytic side conditions, compares the scientific
byte hashes, compiles our verifier, and performs the complete search without a
node limit. Only its final PASS after both stacks empty is acceptance. A failed
command aborts the script; LIMIT or UNRESOLVED is not a certificate.

For an additional runtime arithmetic check, compile the same frozen C++ source
with `-O2 -fsanitize=undefined,signed-integer-overflow
-fno-sanitize-recover=all`, then invoke it with the same two generated tables
and reward 867000. The integer proof and fixed-data bounds are in the report;
sanitizers are an additional implementation check.

The generation outputs and binary executable are not included as opaque proof
inputs. They are reproducible from the small source/data package. The source
manifest identifies all shipped bytes. Mathematical proof details and exact
conclusions are in the accompanying report. Do not interpret this package as a
Lean-kernel proof or as proof of RH.

Attribution and the exact upstream provenance of the mathematical hints are in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The source contains no upstream
Lean program and imports none of its proof axioms.
