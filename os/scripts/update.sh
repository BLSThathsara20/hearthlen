#!/usr/bin/env bash
# Pull the latest project from GitHub and re-apply the setup. Safe to run more than once.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

if [[ ! -d .git ]]; then
  echo "This folder is not a git checkout. Clone the GitHub repository first." >&2
  exit 1
fi

git pull --ff-only
exec "$ROOT/os/scripts/setup.sh"
