# What we will do

**What you are learning here.** A build has an order. The base system is measured before models are added. Skills work from typed text before a microphone is attached. The understanding model is trained after there is something real for it to call. Updates come last, when there is a thing worth updating.

[PROJECT.md](../PROJECT.md) describes the product. [07-roadmap.md](07-roadmap.md) is the checklist with a “done” test for each phase. This file is the story of the work.

## The two machines

You write on the Mac, in this repo. The ThinkPad is the test laptop. It is the machine whose boot time and RAM count.

```mermaid
flowchart LR
  mac[Mac: notes and code]
  git[GitHub]
  actions[GitHub Actions on x86_64]
  thinkpad[ThinkPad: install and daily use]
  mac --> git
  git --> actions
  actions --> thinkpad
```

The Mac may be Apple Silicon. Disc images and installable packages for the ThinkPad are built on x86_64 runners in GitHub Actions, so the Mac’s chip does not decide the build. Model weights are downloaded onto the machine that runs them. They are never committed to git.

While the project is still one ThinkPad, that laptop can pull the stable branch when it is online and idle. Later, real installs take signed Debian packages from an APT repository. Both stages are in Phase 5. The early phases can be copied onto the ThinkPad by hand.

## The path

### 1. A fast, empty desktop

Install a minimal Debian 13 system and a small LXQt desktop on the ThinkPad. Add networking, audio, Chromium with hardware video decode, compressed RAM (zram), and nothing extra. Write down boot time, idle RAM, and how hard the CPU works during YouTube. This is the baseline. Every later feature is compared with it.

You practice: what a package is, what runs at boot, how to read memory use, and how to make a setup script safe to run more than once.

### 2. Prove the models fit

On the ThinkPad’s CPU, run one small language model and one speech-to-text model. Measure speed and the RAM peak when they run one after another, then unload. If they do not fit the budget in [01-scope.md](01-scope.md), the model gets smaller before any assistant is built around it.

You practice: quantization (smaller numbers, less RAM, some loss of quality), process memory, and why a model must exit when the sentence is finished.

### 3. Typed commands and the first memory

A background program accepts typed sentences. It maps them to the first skills. Each skill is ordinary code with a known shape: a name and a few fields, such as `play_youtube` with a query. Risky skills ask first. Every action is logged.

The same phase starts the habit store. Repeated commands, files, settings, and what was on screen begin to form local habits. Typed use is enough to test that loop before the microphone exists.

You practice: a long-running service, a skill as a function with inputs, logs, and a small local database.

### 4. Voice

Add a wake word, speech-to-text, and a spoken reply, all offline, English first. The language tag on each call selects the model and the voice. A future Sinhala entry can point at other files without a new pipeline.

You practice: audio devices, a wake phrase, speech-to-text, and text-to-speech, and why those models load only for the utterance.

### 5. Train the fast understanding model

Collect everyday English sentences, including messy ones (“I can’t hear anything”). Label each with a skill, the details, and `lang`. Keep a test set that is never used for training. Fine-tune a tiny model, export it so it runs quickly, and write down accuracy per skill. The larger model is only the fallback when the tiny one is unsure, and it unloads afterward.

You practice: a dataset, a held-out test, fine-tuning, and the difference between a classifier and a generative model.

### 6. Updates that can undo themselves

The ThinkPad checks for a stable update when it is online, downloads it in the background, and applies it when idle. If the assistant fails its health check, the previous version returns. After that path works, GitHub Actions builds signed packages and a bootable installer image.

You practice: git branches, a systemd timer, package signing, and rollback.

### 7. Make it feel finished

Choose the name, wallpaper, and boot screen. If the always-on process is still too heavy, rewrite that process in Rust or Go. On the same ThinkPad, compare boot, idle RAM, YouTube, and wake-to-action against a fresh Windows install and a standard Ubuntu install.

You practice: reading a benchmark honestly, and branding as a thin layer on a system that already works.

## What we will not do along the way

- Call a cloud model to understand speech or decide an action.
- Let the fallback model emit a shell command.
- Install the heavy models into the always-on memory budget.
- Turn one accidental click into a habit.
- Hide the memory from the person using the laptop.

## How a session should start

Open [07-roadmap.md](07-roadmap.md), find the first phase whose exit check is still open, and do that phase. Leave the later phases alone until the exit check is met. Record numbers in `docs/benchmarks/` when a phase asks for them. Those notes do not exist yet. Phase 0 creates them.
