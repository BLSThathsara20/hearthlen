# Roadmap

**What you are learning here.** A roadmap is a sequence of exit checks. A phase is finished when its check is true on the ThinkPad, not when the code merely exists. Do the phases in order. The guide you are reading is already the step before Phase 0.

Numbers go in `docs/benchmarks/` inside the repo, created in Phase 0. Model weights stay off git. RAM gates are the ones in [01-scope.md](01-scope.md).

## Phase 0 — Foundation

**You learn:** a minimal Debian install, packages, the boot process, LXQt, zram, and how to tell whether video is decoded on the GPU.

**Work.** On the ThinkPad, install Debian 13 with standard system utilities only, then LXQt core, NetworkManager, PipeWire, Chromium, zram, and the VA-API driver that matches the CPU. Put the package list and idempotent setup scripts under `os/`. Idempotent means running the script twice leaves the machine in the same state as running it once.

**RAM gate.** Idle desktop about 400–600MB before any assistant is installed. If it stays above 600MB after a real cleanup, compare a stripped Xfce session and record the result in [06-decisions.md](06-decisions.md).

**Exit.** Boot time, idle RAM, and YouTube CPU use are written down. YouTube plays with hardware decode. The setup scripts can be run again without duplicating configuration.

## Phase 1 — Feasibility

**You learn:** llama.cpp, 4-bit quantization, faster-whisper, and how to measure a process that must exit.

**Work.** On the ThinkPad CPU, measure one 1–2B model at 4-bit and faster-whisper `base` int8 on short English clips. Measure them one after another, then unloaded. Record tokens per second, transcription delay, and peak RAM.

**RAM gate.** The on-demand peak stays around 1.5–2GB, and the memory comes back after the processes exit.

**Exit.** A short note names the model that fits, or says which one must shrink. Tier 2 is allowed into the product only if a short reply returns in a few seconds without leftover RAM growth.

## Phase 2 — Text pipeline and first memory

**You learn:** a user service, a skill registry, confirmation, an action log, and a local habit database.

**Work.** A daemon accepts typed commands. Tier 1 can be a small rule or embedding matcher until Phase 4, as long as it emits a skill name and slots. Implement the skills in [05-architecture.md](05-architecture.md). Risky ones confirm. Every call is logged. Start the habit store and the accessibility-tree sampler under the rules in [03-assistant-that-learns.md](03-assistant-that-learns.md). The panel text box and the assistant card from [04-ui.md](04-ui.md) are enough UI for this phase. The microphone column can wait.

**RAM gate.** Peak RAM during a typed command is recorded and stays inside the on-demand budget. The sampler’s idle cost is recorded and counts toward the always-on budget.

**Exit.** Typed “play Shape of You on YouTube” plays the video in Chromium. The other first skills pass a manual script on the ThinkPad. A repeated action can appear as a sentence on What I’ve learned, and Delete and Pause work. Pause stops screen reading.

## Phase 3 — Voice

**You learn:** wake words, speech-to-text, Piper, and a language manifest.

**Work.** Train the wake phrase “hey Hearthlen”. Add openWakeWord, faster-whisper, and Piper behind the daemon. English models only, selected by the `en` manifest entry. Speech-to-text and Piper start per utterance and exit. The card and the spoken line say the same sentence.

**RAM gate.** Always-on RAM, including the wake word, stays around 150–250MB. The speech models are absent from that figure because they have exited.

**Exit.** “Hey Hearthlen, play Shape of You on YouTube” completes. The assistant path is offline. YouTube itself may use the network. Wake-to-action time is logged. A second manifest entry can point at future Sinhala files without a pipeline change.

## Phase 4 — Training

**You learn:** labeling, a held-out test, fine-tuning, ONNX export, and per-skill accuracy.

**Work.** Build an English command set the way people actually talk, including messy phrasing. Label skill, slots, and `lang`. Split a test set and never train on it. Fine-tune a MiniLM or DistilBERT-size model, export ONNX, and compare accuracy per skill with the untrained Phase 2 matcher. Leave an empty `si` split in the eval report. Connect Tier 2 as the low-confidence fallback, then unload it. Vague phrases may take a slot from the habit store.

**RAM gate.** Tier 1 fits the always-on budget. Tier 2 is not resident after the reply.

**Exit.** Test-set accuracy is recorded per skill. Common commands are handled by Tier 1 in milliseconds. The eval script already groups by `lang`.

## Phase 5 — Updates

**You learn:** systemd timers, a health check, rollback, Debian packages, signing, and live-build images.

**Work.** Stage 1: a timer on the ThinkPad checks `stable` every 10–15 minutes when online, downloads in the background, and applies when idle. A failed assistant health check restores the previous revision. Stage 2: GitHub Actions builds signed `.deb` packages and a Debian live-build ISO, and publishes an APT repository. Devices use unattended upgrades. `dev` is not installed on devices.

**Exit.** A bad `stable` update returns to the previous version without a reinstall. An ISO from GitHub Releases installs on the ThinkPad.

## Phase 6 — Polish

**You learn:** how to compare operating systems with the same tasks on the same hardware.

**Work.** Apply the name, wallpaper, and boot screen. If the always-on process is over budget, rewrite that process in Rust or Go and measure again. Benchmark this system, a fresh Windows install, and standard Ubuntu on the same ThinkPad: boot, idle RAM, YouTube, and wake-to-action.

**Exit.** The metrics from section 10 of [PROJECT.md](../PROJECT.md) are filled in for all three systems, and a release note can be written from those numbers.

## Order

```mermaid
flowchart LR
  guide[Guide]
  p0[Phase 0 baseline]
  p1[Phase 1 models]
  p2[Phase 2 text and memory]
  p3[Phase 3 voice]
  p4[Phase 4 training]
  p5[Phase 5 updates]
  p6[Phase 6 polish]
  guide --> p0
  p0 --> p1
  p1 --> p2
  p2 --> p3
  p3 --> p4
  p4 --> p5
  p5 --> p6
```

Start a phase when the previous exit check is met. Phase 0 is the next build step when you decide to leave the guide and touch the ThinkPad.
