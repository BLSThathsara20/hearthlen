---
title: "An 8GB Laptop Has to Run YouTube and a Local AI Assistant"
subtitle: "The RAM budget behind an offline assistant: what stays loaded, and what has to leave."
slug: local-ai-assistant-8gb-ram
seo_title: "Run a Local LLM Assistant on 8GB RAM"
seo_description: "Savindu Thathsara's RAM budget for an offline AI assistant on 8GB: a tiny always-on model, then whisper, llama.cpp, and a voice that exit when the reply is done."
series: "Hearthlen"
devto_tags: ai, linux, machinelearning, tutorial
hashnode_tags:
  - local-llm
  - llama-cpp
  - edge-ai
  - linux
  - machine-learning
  - privacy
keywords:
  - local LLM
  - llama.cpp
  - small language model
  - edge AI
  - faster-whisper
  - 8GB RAM
  - on-device AI assistant
  - Savindu Thathsara
canonical_url: ""
published: false
author: Savindu Thathsara
website: https://savithathsara.me
email: savindu@savithathsara.me
---

# An 8GB Laptop Has to Run YouTube and a Local AI Assistant

Eight gigabytes sounds like enough until a browser and a language model want it at the same time. The test machine for this project is a ThinkPad with 8GB of RAM and no discrete GPU. YouTube still has to play. The assistant still has to answer. Whatever the assistant borrows, it has to give back.

I'm Savindu Thathsara, and this is the third note in the Hearthlen series. The project is a lightweight Linux system with a local AI assistant and no cloud model API. The habit loop is in the previous post, [a local assistant that learns your habits](02-assistant-that-learns-your-habits.md). This one is only about fitting.

## The split

I am treating RAM as four piles.

| Piece | Budget |
|---|---|
| Debian desktop, sitting idle | about 400–600MB |
| Always on: wake word and a tiny understanding model | about 150–250MB |
| Borrowed while one request is in progress | about 1.5–2GB, then released |
| Left for the person, including the browser | 5GB or more |

The always-on pile is allowed to be boring. A wake word, a small intent model in the MiniLM or DistilBERT size, exported to ONNX, plus a short local log of habits. That pile should answer “play this song” in milliseconds once it has been trained.

The borrowed pile is where the heavy pieces live, and only one of them at a time.

## What loads, then leaves

Speech-to-text is faster-whisper, English, int8, starting at the `base` size. It transcribes the utterance and the process exits.

If the tiny model is confident, the skill runs. If it is not, a 1–2B model at 4-bit starts through llama.cpp. The candidates I will measure are Qwen3 1.7B and Llama 3.2 1B. It may return a skill name and the fields that skill expects. It may not return a shell command. When the reply is done, that process exits too.

The spoken reply is Piper. Same rule: speak, then leave.

Loading whisper, a local LLM, and a voice at the same moment would spend the 2GB twice. The pipeline is a queue, not a group photo.

## Skills stay ordinary code

The model picks from a fixed list: YouTube, open an app, volume, brightness, find a file, open a file, web search, reminder, screenshot, Wi-Fi. Finding a file in the first version means names, folders, and dates. A search over the meaning of every document is a later feature, because an index of the whole disk is another way to spend the RAM I just promised the browser.

YouTube opens in Chromium at the video page, with hardware decode on the integrated GPU, so the CPU is not decoding 1080p while a model is trying to unload. I am not putting a second browser-automation stack on the machine.

## What I will not claim yet

These numbers are the gates, not the measurements. Phase 0 is a clean Debian install and a stopwatch. Phase 1 is llama.cpp and faster-whisper on that ThinkPad, CPU only, with the peak written down after the processes have exited. If the peak stays high, the model gets smaller before any assistant is built around it.

I will publish the figures that miss the gate as well as the ones that pass. A local LLM that only looks fast in a README is not a result.

English is the first language of the models. Every model entry has a language tag, so a later Sinhala voice is another row in the same list, not a rewrite. The English weights do not become that voice by renaming the file.

Next in the series: the roadmap I want to be graded against, before the installer runs. [I wrote the map before installing the OS](04-build-in-public-roadmap.md).

---

Savindu Thathsara builds practical AI and automation in London. This series is the public log of an offline AI operating system he is writing and learning at the same time.

- Site: [https://savithathsara.me](https://savithathsara.me)
- Email: savindu@savithathsara.me
- DEV: [https://dev.to/savinduthathsara](https://dev.to/savinduthathsara)
