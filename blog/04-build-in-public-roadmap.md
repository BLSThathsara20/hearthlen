---
title: "I Wrote the Roadmap Before Installing the Operating System"
subtitle: "Seven phases, what each one has to prove, and the post I will publish when it does."
slug: offline-ai-os-roadmap-build-in-public
seo_title: "Build in Public: Offline AI OS Roadmap"
seo_description: "Savindu Thathsara's build-in-public roadmap for an offline AI OS: baseline the 8GB laptop, measure local models, then skills, voice, training, and safe updates."
series: "Offline AI OS"
devto_tags: ai, linux, opensource, productivity
hashnode_tags:
  - build-in-public
  - linux
  - local-llm
  - open-source
  - edge-ai
  - privacy
keywords:
  - build in public
  - offline AI operating system
  - local LLM
  - lightweight Linux
  - open source
  - edge AI
  - Savindu Thathsara
canonical_url: ""
published: false
author: Savindu Thathsara
website: https://savithathsara.me
email: savindu@savithathsara.me
---

# I Wrote the Roadmap Before Installing the Operating System

The usual build-in-public post shows up after the demo. This one is the map, published first, so the later posts have something to miss. I have not installed the system yet. The ThinkPad is still a test machine on paper. The notes are the part that exists.

I'm Savindu Thathsara. The project is an offline AI operating system for a normal 8GB laptop: local models, a short list of skills, and a memory of your habits that stays on the device. The idea is in [the first post](01-offline-ai-operating-system.md), the memory in [the second](02-assistant-that-learns-your-habits.md), and the RAM budget in [the third](03-local-ai-on-8gb-ram.md).

## Why the order is the product

A model installed on a slow desktop teaches nothing. A voice pipeline wrapped around a skill that does not work yet teaches nothing either. Each phase has to leave a number or a finished action behind before the next one starts.

I am also learning the stack while I build it. The phases are the course: packages and boot, then measurement, then a service, then audio, then a training set, then updates.

## The seven checks

**Phase 0. A fast, empty desktop.** Minimal Debian 13 and LXQt on the ThinkPad. Networking, audio, Chromium with hardware video decode, compressed RAM, and nothing extra. Exit means boot time, idle RAM, and YouTube CPU use are written down, and the setup can be run twice without making a mess.

**Phase 1. The models have to fit.** One 1–2B model at 4-bit, and faster-whisper on short English clips, on the CPU. Exit means a note that names what fits, or what has to shrink. A short reply has to come back in a few seconds, and the memory has to come back with it.

**Phase 2. Typed sentences, real actions, first memory.** “Play Shape of You on YouTube” plays the video. The other first skills pass a manual script. A repeated action shows up as a sentence the person can delete. Pause stops the screen reading.

**Phase 3. Voice.** A wake phrase using the assistant’s name, speech-to-text, and a spoken reply, English only. The card and the voice say the same sentence. The heavy speech models are gone again when the reply is over.

**Phase 4. Train the tiny model.** Everyday English, including messy phrasing, labeled with a skill and the details. A test set that is never used for training. Accuracy per skill, compared with the untrained matcher from Phase 2. The larger model is only the fallback.

**Phase 5. Updates that can undo themselves.** The laptop downloads a stable update while it is online and applies it when idle. If the assistant fails its health check, the previous version comes back. After that works, signed packages and an installer image.

**Phase 6. A fair comparison.** Name, wallpaper, and boot screen. If the always-on process is still too heavy, that process gets a rewrite and another measurement. Then the same ThinkPad, three ways: this system, a fresh Windows install, and standard Ubuntu. Boot, idle RAM, YouTube, and wake-to-action.

## What I will publish at each exit

A major result gets its own post. A passing benchmark, a missed benchmark, a skill that works from a sentence, a rollback that actually rolled back. Not a dependency bump, and not a claim that uses a number I have not measured.

The posts stay in this series, Offline AI OS. The first paragraph will be the result, not a tour of the repository.

## Follow along

The name of the system is still open. English ships first. Sinhala is a later set of weights on the same language tag, which matters to me and is not a promise for version 1.

If you want the constraints in one place: 8GB, no cloud model API, skills instead of guessed clicks, and a habit list you can read and delete.

- Site: [https://savithathsara.me](https://savithathsara.me)
- Email: savindu@savithathsara.me
- DEV: [https://dev.to/savinduthathsara](https://dev.to/savinduthathsara)

---

Savindu Thathsara builds practical AI and automation in London. This series is the public log of an offline AI operating system he is writing and learning at the same time.

- Site: [https://savithathsara.me](https://savithathsara.me)
- Email: savindu@savithathsara.me
- DEV: [https://dev.to/savinduthathsara](https://dev.to/savinduthathsara)
