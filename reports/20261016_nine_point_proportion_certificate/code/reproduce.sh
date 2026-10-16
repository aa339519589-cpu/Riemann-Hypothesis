#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
PYTHON="${PYTHON:-python3}"
CXX="${CXX:-g++}"
"$PYTHON" -c 'if not __debug__: raise RuntimeError("Certificate assertions require Python without -O or PYTHONOPTIMIZE")'
# Dependency: official PyPI python-flint 0.9.0 (FLINT 3.6.0), Python 3.
# No downloaded author code is executed. Hints are untrusted mathematical data.
"$PYTHON" prepare_geometry.py
"$PYTHON" verify_expanded_partition_cover.py
"$PYTHON" verify_constants.py
"$PYTHON" build_am_kernel_table_input.py --input certified_window_data.json --bits 160 --cells 1048576 --out candidate_am_kernel
"$PYTHON" build_am_kernel_jets_input.py --input certified_window_data.json --bits 160 --cells 1048576 --out candidate_am_jets
"$PYTHON" certify_am_curvature_upper.py --input certified_window_data.json --bits 160 --cells 1048576 --table candidate_am_jets.i64le --out candidate_am_upper_curvature.json
"$PYTHON" certify_am_candidate_conditions.py --input certified_window_data.json --table candidate_am_kernel.u32le --out certified_window_side_conditions.json --bits 192
"$PYTHON" verify_generated_hashes.py
"$CXX" -O3 -std=c++17 check_am9_expanded_anchors.cpp -o check_am9_expanded_anchors
./check_am9_expanded_anchors candidate_am_kernel.u32le candidate_am_jets.i64le 867000 | tee replay.log
