#!/usr/bin/env bash
# This script checks a small core-Lean file, never RH.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$HERE"
if ! command -v lean >/dev/null 2>&1; then
  echo 'NOT_RUN: lean is unavailable on PATH.' >&2; exit 127
fi
if grep -nE '\b(sorry|admit|axiom|sorryAx|unsafe)\b' Smoke.lean; then
  echo 'Rejected placeholder or custom-axiom marker in Smoke.lean.' >&2; exit 2
fi
mkdir -p .build
lean --version | tee .build/version.log
if ! grep -Eq 'version 4\.34\.1([, )]|$)' .build/version.log; then
  echo 'Wrong Lean version: expected the pinned stable 4.34.1.' >&2; exit 5
fi
lean -DwarningAsError=true -o .build/Smoke.olean Smoke.lean 2>&1 | tee .build/smoke.log
if grep -E 'sorryAx|depends on axioms:' .build/smoke.log; then
  echo 'Unexpected axiom dependency; inspect the log.' >&2; exit 3
fi
[[ "$(grep -c 'does not depend on any axioms' .build/smoke.log)" -eq 2 ]] || {
  echo 'Both explicit dependency reports are required.' >&2; exit 4;
}
echo 'PASS: both tiny smoke declarations were compiled and report no axioms. This is not an RH proof.'
