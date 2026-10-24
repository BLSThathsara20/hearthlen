---
title: "I'm Building an Offline AI Operating System for an 8GB Laptop"
subtitle: "A local assistant for a normal laptop. No cloud model API."
slug: offline-ai-operating-system-8gb-laptop
seo_title: "Offline AI OS for an 8GB Laptop | Savindu Thathsara"
seo_description: "Savindu Thathsara is building a lightweight Linux OS with a local AI assistant. No cloud model API. It learns your routines and runs on 8GB of RAM."
series: "Offline AI OS"
devto_tags: ai, linux, opensource, machinelearning
hashnode_tags:
  - offline-ai
  - local-llm
  - edge-ai
  - linux
  - privacy
  - open-source
  - build-in-public
keywords:
  - offline AI operating system
  - local LLM
  - on-device AI assistant
  - privacy-first AI
  - lightweight Linux
  - 8GB RAM
  - Savindu Thathsara
canonical_url: ""
published: false
author: Savindu Thathsara
website: https://savithathsara.me
email: savindu@savithathsara.me
---

# I'm Building an Offline AI Operating System for an 8GB Laptop

I'm Savindu Thathsara. I live in London, I build practical AI and automation, and I am about to spend a long stretch of evenings on a strange project: a lightweight Linux operating system with an offline AI assistant for a normal laptop.

The picture I want is simple. You open the machine and say, “Play Shape of You,” or “Open my last document,” or “Find the photos from my graduation.” The assistant does it. The model that understood you is running on that laptop. Your requests are not sent to a cloud API.

This post is the start of a public build log. The guide is written. The first install has not happened yet. I want the plan on the record before the first package goes on the test machine.

## A normal laptop, on purpose

The test computer is a Lenovo ThinkPad with 8GB of RAM, a 256GB SSD, and integrated graphics. No discrete GPU. That is the spec a lot of people actually own, and it is the spec this system has to feel fast on.

If a feature makes that laptop struggle, the feature is wrong. I would rather ship fewer skills that work than a demo that only runs on a workstation.

The person I am building for does not want a terminal. They want the screen a bit brighter, a song, a file, a reminder. I am the person who will learn Linux, local models, and voice along the way, and I am writing it down as I go.

## What “offline AI” means here

Speech recognition, the choice of action, and the spoken reply run on the device. That is the privacy-first part. A local LLM is the fallback for messy sentences, and it is small: a 1–2B model, quantized, through llama.cpp, unloaded when the sentence is finished.

The network still exists. YouTube is online. System updates are online. The decision about what to open is made locally. An on-device AI assistant can play a video without sending the sentence “play this song” to someone else’s server.

## Accuracy before range

A lot of agents try to click whatever is on the screen. That looks flexible and it fails in boring, expensive ways. This assistant gets a fixed list of skills. A small model, trained on everyday phrasing, picks the skill and fills in the details. The skill itself is ordinary, predictable code.

The first list is short:

- Play something on YouTube
- Open an app
- Change the volume or the brightness
- Find a file and open it
- Search the web
- Set a reminder
- Take a screenshot
- Turn Wi-Fi on or off

Delete, send, pay, and turning the network off will always ask first. The model is not allowed to invent shell commands. If there is no skill, the honest answer is that it cannot do that yet.

## It should get easier the longer you use it

The other half of the idea is memory. A typical agent waits for an order and forgets the person. I want this one to notice how this laptop is actually used, keep that on the machine, and make the next day easier. “Play some music” can become the song you usually mean. “Graduation photos” can become the folder that was right last time.

That memory is local. You can read it, delete a habit, or pause learning. The next post in this series is only about that loop, because it is the part I care about most.

## What I am measuring

Every release has to show its cost:

- Boot time
- RAM used while the desktop is idle
- RAM while the assistant is working, then after the heavy models have exited
- Time from wake word to finished action
- Accuracy per skill on a test set that was never used for training

The idle desktop should sit around 400–600MB. The always-on piece, wake word plus a tiny understanding model, should sit around 150–250MB. Speech-to-text, the small fallback model, and the spoken voice share about 1.5–2GB, and only while a request is in progress. The rest of the 8GB stays with the person using the machine.

Those numbers are gates. I will publish the real ThinkPad figures when Phase 0 and Phase 1 produce them, including the ones that miss.

## Where the work stands

English is the first language. The data format keeps a language tag so Sinhala can be added later without rewriting the skills. The desktop target is a minimal Debian with LXQt. The product name is not chosen yet. The series name, until then, is Offline AI OS.

I am building this in the open because I want the constraints visible: ordinary hardware, local models, a short skill list, and a memory the owner can see.

Next: [how the assistant learns a habit without uploading your life](02-assistant-that-learns-your-habits.md).

---

Savindu Thathsara builds practical AI and automation in London. This series is the public log of an offline AI operating system he is writing and learning at the same time.

- Site: [https://savithathsara.me](https://savithathsara.me)
- Email: savindu@savithathsara.me
- DEV: [https://dev.to/savinduthathsara](https://dev.to/savinduthathsara)
