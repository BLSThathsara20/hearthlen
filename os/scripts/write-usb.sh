#!/usr/bin/env bash
# Write the Debian installer to one external USB disk.
# Refuses the internal disk, the Windows installer stick, and the dashcam stick.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ISO="$ROOT/build/debian-13.7.0-amd64-netinst.iso"
EXPECTED="a7ef94ac2fb9a7fec454552abd629b7cc9d5155c886165a45649f5ce6167e355"
DISK="${1:-}"

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "Run this on the Mac." >&2
  exit 1
fi

if [[ -z "$DISK" ]]; then
  echo "Usage: os/scripts/write-usb.sh diskN" >&2
  echo "External disks right now:" >&2
  diskutil list external physical
  exit 1
fi

DISK="${DISK#/dev/}"
NODE="/dev/$DISK"

if [[ ! -e "$NODE" ]]; then
  echo "No such disk: $NODE" >&2
  exit 1
fi

info="$(diskutil info "$DISK")"
echo "$info" | grep -q "Device Location:.*External" || {
  echo "Refusing $DISK because it is not an external disk." >&2
  exit 1
}
echo "$info" | grep -q "Protocol:.*USB" || {
  echo "Refusing $DISK because it is not USB." >&2
  exit 1
}
echo "$info" | grep -q "Removable Media:.*Removable" || {
  echo "Refusing $DISK because it is not removable." >&2
  exit 1
}

if mount | grep -q "WIN11"; then
  win_disk="$(diskutil info WIN11 2>/dev/null | awk -F': *' '/Part of Whole/{print $2; exit}')"
  if [[ "$win_disk" == "$DISK" ]]; then
    echo "Refusing $DISK because it is the Windows 11 installer." >&2
    exit 1
  fi
fi

for volume in /Volumes/*; do
  [[ -d "$volume" ]] || continue
  dev="$(diskutil info "$volume" 2>/dev/null | awk -F': *' '/Part of Whole/{print $2; exit}')"
  [[ "$dev" == "$DISK" ]] || continue
  if [[ -f "$volume/DEVICE.XML" && -d "$volume/Emergency" ]]; then
    echo "Refusing $DISK because it looks like a dashcam card (Emergency/Photo)." >&2
    exit 1
  fi
  if [[ -f "$volume/bootmgr" || -f "$volume/setup.exe" ]]; then
    echo "Refusing $DISK because it already holds a Windows installer." >&2
    exit 1
  fi
done

if [[ ! -f "$ISO" ]]; then
  echo "Missing $ISO. Download it before writing." >&2
  exit 1
fi

actual="$(shasum -a 256 "$ISO" | awk '{print $1}')"
if [[ "$actual" != "$EXPECTED" ]]; then
  echo "Checksum mismatch. Not writing the USB." >&2
  echo "Expected $EXPECTED" >&2
  echo "Actual   $actual" >&2
  exit 1
fi

echo "About to erase $NODE and write the Debian 13.7 installer."
echo "This destroys everything on that stick."
diskutil info "$DISK" | awk -F': *' '/Device Node|Media Name|Disk Size|Volume Name|Device Location/{print}'
read -r -p "Type the disk name ($DISK) to continue: " answer
if [[ "$answer" != "$DISK" ]]; then
  echo "Stopped."
  exit 1
fi

diskutil unmountDisk "$NODE"
sudo dd if="$ISO" of="/dev/r$DISK" bs=4m status=progress
sync
diskutil eject "$NODE" || true
echo "The stick is bootable. On the ThinkPad, use the boot menu and install Debian."
