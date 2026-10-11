#!/usr/bin/env bash
# Prepared for a network-authorized environment. NOT successfully run in this audit.
set -euo pipefail
ROOT="${1:-$PWD/.rh-toolchain}"
mkdir -p "$ROOT/downloads"
ROOT="$(cd "$ROOT" && pwd)"
export ELAN_HOME="$ROOT/elan"
ARCHIVE="$ROOT/downloads/elan-v4.2.4-x86_64-linux.tar.gz"
URL='https://github.com/leanprover/elan/releases/download/v4.2.4/elan-x86_64-unknown-linux-gnu.tar.gz'
SHA256='42b94d4244e8353142c456ec0e4ca6528fd898a6c604d4059f494e706e431f63'
[[ "$(uname -s)" == Linux && "$(uname -m)" == x86_64 ]] || {
  echo 'This pinned installer supports Linux x86_64 only.' >&2; exit 2;
}
if [[ -e "$ELAN_HOME" ]]; then
  echo "Refusing to overwrite existing ELAN_HOME: $ELAN_HOME" >&2; exit 3
fi
curl --fail --location --show-error "$URL" -o "$ARCHIVE"
printf '%s  %s\n' "$SHA256" "$ARCHIVE" | sha256sum --check --strict
mkdir -p "$ROOT/downloads/elan-unpacked"
tar -xzf "$ARCHIVE" -C "$ROOT/downloads/elan-unpacked"
"$ROOT/downloads/elan-unpacked/elan-init" -y --no-modify-path --default-toolchain none
"$ELAN_HOME/bin/elan" toolchain install leanprover/lean4:v4.34.1
"$ELAN_HOME/bin/lean" +leanprover/lean4:v4.34.1 --version
printf 'Use ELAN_HOME=%q and PATH=%q:$PATH for this shell only.\n' "$ELAN_HOME" "$ELAN_HOME/bin"
