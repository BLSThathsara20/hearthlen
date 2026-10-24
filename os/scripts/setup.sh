#!/usr/bin/env bash
# Idempotent Phase 0 setup for Debian 13 on the ThinkPad.
# Safe to run more than once. Does not install AI models.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "Run this on the ThinkPad after Debian is installed, not on the Mac." >&2
  exit 1
fi

if [[ ! -r /etc/os-release ]] || ! grep -q '^ID=debian$' /etc/os-release; then
  echo "This script is for Debian." >&2
  exit 1
fi

if [[ "$(id -u)" -ne 0 ]]; then
  exec sudo -- "$0" "$@"
fi

ensure_firmware_component() {
  local file="/etc/apt/sources.list.d/debian.sources"
  [[ -f "$file" ]] || return 0
  if grep -q '^Components:' "$file" && ! grep -q 'non-free-firmware' "$file"; then
    sed -i 's/^Components: \(.*\)$/Components: \1 non-free-firmware/' "$file"
  fi
}

install_packages() {
  local package
  local -a packages=()
  while IFS= read -r package; do
    [[ -z "$package" || "$package" == \#* ]] && continue
    packages+=("$package")
  done <"$ROOT/packages.list"
  export DEBIAN_FRONTEND=noninteractive
  apt-get update
  apt-get install -y "${packages[@]}"
}

install_file() {
  local source="$1"
  local target="$2"
  local mode="$3"
  install -d -m 755 "$(dirname "$target")"
  if [[ -f "$target" ]] && cmp -s "$source" "$target"; then
    return 0
  fi
  install -m "$mode" "$source" "$target"
}

ensure_firmware_component
install_packages
install_file "$ROOT/config/zramswap" /etc/default/zramswap 644
install_file "$ROOT/config/chromium-vaapi" /etc/chromium.d/vaapi 644

systemctl enable zramswap.service
systemctl restart zramswap.service
systemctl enable sddm.service
systemctl set-default graphical.target

echo "Phase 0 packages are installed. Reboot, then run: os/scripts/baseline.sh"
