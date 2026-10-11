# Core Lean smoke check: NOT RUN

Status on 2026-10-11: **BLOCKED_NETWORK_ALLOWLIST**. Lean is not installed in the checked cloud environment, and `Smoke.lean` has not been compiled.

This directory contains a pinned toolchain selection, an isolated-install preparation script, a small candidate proof file using only `Init`, and a strict validation script. Shell syntax validation passed; Lean validation did not run. No Mathlib installation is required for this test.

Read `../LEAN_TOOLCHAIN_AUDIT.md` for exact scope, missing repository sources, network evidence, versions, and limitations. The original command output is in `../evidence/`.

When access to the official release host is legitimately available:

```bash
bash scripts/install-lean-isolated.sh /workspace/shared/rh-toolchains-20261011
export ELAN_HOME=/workspace/shared/rh-toolchains-20261011/elan
export PATH="$ELAN_HOME/bin:$PATH"
bash scripts/check-smoke.sh
```

A future passing smoke check would establish only that two tiny core-Lean declarations compile with empty axiom dependencies. It would not verify any Riemann Hypothesis claim or the absent Lean files cited by the repository's prose.
