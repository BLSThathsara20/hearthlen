# Install on the ThinkPad

The Mac builds nothing that can boot an Intel or AMD laptop by itself. This folder downloads the official Debian 13.7 installer for x86_64, checks it, and can write it to a blank USB stick. After Debian is on the ThinkPad, the laptop installs our desktop from GitHub.

## On the Mac

The installer image is:

`os/build/debian-13.7.0-amd64-netinst.iso`

Checksum `a7ef94ac2fb9a7fec454552abd629b7cc9d5155c886165a45649f5ce6167e355`.

Plug in a blank USB stick. Leave the stick named WIN11 alone, and leave the stick that contains Photo, Emergency, and Parking alone. Then:

```bash
os/scripts/write-usb.sh
os/scripts/write-usb.sh diskN
```

The first command lists external disks. The second writes only if you type that disk name back, and only if the disk is a removable USB drive.

## On the ThinkPad

1. Boot from the USB stick. On a ThinkPad that menu is usually F12.
2. Install Debian 13. Create your user. When the installer asks which software to install, leave the desktop boxes unchecked and keep standard system utilities.
3. Connect to the network, then:

```bash
git clone https://github.com/BLSThathsara20/ai-os.git
cd ai-os
./os/scripts/setup.sh
sudo reboot
```

4. After the reboot, from the project folder:

```bash
./os/scripts/baseline.sh
```

That writes boot time and idle RAM to `docs/benchmarks/phase0.txt`. Play a YouTube video and note whether the CPU stays low. Hardware decode is the point of the Chromium flag.

## Later updates

On the ThinkPad, inside the clone:

```bash
./os/scripts/update.sh
```

That pulls the GitHub `main` branch and runs the setup again. The script is safe to repeat. Model weights are not in git.
