#!/usr/bin/env bash
# Record boot time and idle RAM on the ThinkPad. Run after a fresh reboot, before AI is installed.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUT="$ROOT/docs/benchmarks/phase0.txt"
mkdir -p "$(dirname "$OUT")"

{
  echo "# Phase 0 baseline"
  echo
  echo "Recorded: $(date -Is)"
  echo "Kernel: $(uname -sr)"
  echo
  echo "## Boot"
  systemd-analyze || true
  echo
  echo "## Top boot costs"
  systemd-analyze blame | head -n 30 || true
  echo
  echo "## Memory"
  free -h
  echo
  echo "## Video decode"
  vainfo 2>&1 | head -n 40 || true
} | tee "$OUT"

echo "Wrote $OUT"
echo "Play a YouTube video, then note the CPU use from: top"
