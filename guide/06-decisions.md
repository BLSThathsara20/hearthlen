# Decisions

**What you are learning here.** A decision log is the reason a choice was made, so a later session does not relitigate it by accident. [PROJECT.md](../PROJECT.md) remains the brief. Where this file goes further, the guide is the newer record. Change a row here before changing the build.

## Locked

### Product

- **Audience.** A non-technical person on an 8GB laptop. The builder learns by constructing it, phase by phase.
- **Offline assistant.** Understanding, speech, and replies run on the machine. No cloud model API. YouTube and other websites may use the network. The choice of what to open is local.
- **English first.** Version 1 understands and speaks English. Every utterance, manifest entry, and string file carries a `lang` tag. `en` is the only filled-in language. `si` is a later set of weights and labeled sentences on the same manifest.
- **Accuracy over range.** Ship a small skill list that works, then grow it. Missing a skill is an honest “I can’t do that yet”.
- **Habits.** The assistant remembers routines and what is on screen, on the laptop, and uses that to make the next time easier. Details are in [03-assistant-that-learns.md](03-assistant-that-learns.md).

### Memory and screen

- **Screen context** comes from the Linux accessibility tree: application, window title, and visible control names. Samples happen on focus changes and occasionally while the person is active.
- **A habit is stored after the pattern repeats.** One event stays a note.
- **Left out of the store:** keystrokes, password fields, chat transcripts, document bodies, screenshots, and screen video. A focused password field skips the sample.
- **Visible and pausable.** The What I’ve learned page lists habits as sentences. Delete removes one. Pause stops new records and stops screen reading. The panel shows a mark while screen reading is on.
- **Local only.** The database stays on the laptop and out of git.

### Safety

- The model may return a skill name and slots. The skill registry is the only code that runs.
- The model does not generate shell commands.
- Delete, send, pay, and turning the network off always ask, including when a habit matches.
- Volume and brightness apply immediately and are logged.
- Actions are logged so they can be audited and, as skills gain undo, reversed.

### System

- **Debian 13**, minimal, x86_64, CPU only. No CUDA and no discrete-GPU requirement.
- **LXQt** core. Revisit Xfce only if a stripped idle session stays above 600MB.
- **Chromium** with VA-API for video. YouTube opens at a resolved watch URL.
- **Playwright** stays off the installed system.
- **File search** in version 1 uses names, folders, and dates. Habit memory may remember the right folder. A semantic index waits.
- **zram** on. Unused services off.
- **Python** for the prototype daemon, skills, and training. A Rust or Go rewrite of the always-on process is Phase 6, and only if RAM requires it.
- **One heavy model at a time**, then unload. Always on: wake word, Tier 1, screen sampler, habit writer.
- **Tier 2** is a 1–2B model at 4-bit through llama.cpp, only when Tier 1 is unsure.
- **Voice tools:** openWakeWord, faster-whisper int8, Piper. English models first.
- **Weights never go in git.**

### Build and updates

- The Mac is for editing, training, and tests that do not need the ThinkPad.
- Packages and ISO images build in GitHub Actions on x86_64.
- Two branches: `dev` for experiments, `stable` for the device.
- Stage 1 updater: timer, about every 10–15 minutes when online, apply when idle, roll back if the assistant health check fails.
- Stage 2 updater: signed `.deb` packages, an APT repository, unattended upgrades. Devices trust the signing key.
- An update does not apply mid-task.

### Name

- The setting is `ASSISTANT_NAME` until a real name is chosen.
- The name is required before wake-word training, because the phrase is “hey” plus that name.

## Open

| Decision | When it closes |
|---|---|
| The assistant’s name, wallpaper, and boot screen | Before wake-word training for the name. Artwork in Phase 6. |
| Qwen3 1.7B or Llama 3.2 1B, or a smaller model if neither fits | Phase 1, from ThinkPad measurements |
| faster-whisper `base` or `small` | Phase 1, from speed and RAM on short English clips. Start the measurement at `base` int8. |
| When Sinhala sentences and voices start | After English test-set accuracy is recorded |
| Xfce instead of LXQt | Only if Phase 0 idle RAM stays above 600MB |

## How to change a locked row

Write the new choice in this file, say why, and point at the guide page that must change with it. Then change that page. Do not leave the code ahead of the guide.
