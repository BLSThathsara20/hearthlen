---
title: "A Local AI Assistant That Learns Your Habits, and Lets You Delete Them"
subtitle: "On-device memory for an offline assistant. Screen context without a screen recording."
slug: local-ai-assistant-learns-your-habits
seo_title: "Local AI Assistant That Learns Your Habits"
seo_description: "Savindu Thathsara explains an on-device AI assistant that learns routines from use, stores them locally, and lets you read, delete, or pause every habit."
series: "Offline AI OS"
devto_tags: ai, privacy, linux, productivity
hashnode_tags:
  - ai-agents
  - local-llm
  - privacy
  - on-device-ai
  - linux
  - edge-ai
keywords:
  - AI agent with memory
  - local AI assistant
  - on-device AI
  - privacy-first AI
  - offline voice assistant
  - habit learning
  - Savindu Thathsara
canonical_url: ""
published: false
author: Savindu Thathsara
website: https://savithathsara.me
email: savindu@savithathsara.me
---

# A Local AI Assistant That Learns Your Habits, and Lets You Delete Them

Most AI agents are impressive for one prompt. You close the laptop and they forget how you work. I am building an offline AI operating system where the assistant is supposed to do the opposite: learn this person, on this machine, and make the next request shorter.

I am Savindu Thathsara. The project runs the models locally, on an 8GB laptop, with no cloud model API. This post is about the memory. The launch post is [I'm Building an Offline AI Operating System for an 8GB Laptop](01-offline-ai-operating-system.md).

## The loop

A habit is not a single event. The loop I want is small enough to explain on one screen.

1. Notice what just happened.
2. Store a short record on the laptop.
3. Turn it into a habit only after it repeats.
4. Offer the easy version, or just do it when the request is vague and the action is safe.
5. If the person corrects it, update the record.

One accidental click must not become “this is who you are.” Repetition is the gate.

“Play some music,” after enough evenings of the same song, can fill in that song. “Graduation photos” can resolve to the folder that was right the last few times. A brightness level you keep choosing at night can be the level the assistant suggests the next night.

The memory fills in details for a skill that already exists. It does not invent a new program, and it does not write shell commands.

## Learning from what is on screen

Commands are not the whole picture. People also show what they mean by what they leave open. The assistant reads the front window through the Linux accessibility tree. That is the same structure a screen reader uses: application name, window title, and the names of the visible controls.

A sample looks like this:

- Chromium, title “Shape of You - YouTube”
- The file manager, open on a folder named Graduation
- A word processor whose window title is the document name

It samples when the front window changes, and occasionally while you are active. It does not record video, and it does not keep screenshots. A list of names is small. A screen recording would be large, and it would freeze private text into a file.

When a password field is focused, that sample is skipped.

## What the store is allowed to hold

- The sentence you spoke or typed to the assistant
- App name, window title, and visible control names
- A file path, when a file was opened
- Volume, brightness, Wi-Fi, and the time of day
- Which skill ran, and whether you confirmed it, cancelled it, or corrected it

Left out, on purpose:

- Keystrokes
- Password fields
- The body of a document
- Chat and message text
- Screenshots and screen video
- Any copy of the store on a server

Screen context is there so the assistant can tell a YouTube results list from a photo folder. It is not a key logger, and it is not a private copy of your files.

## You can see the whole list

A settings page will show habits as sentences.

- “On weekday evenings you set brightness to 30%.”
- “Graduation photos means Pictures/Graduation.”
- “Play some music means Shape of You on YouTube.”

Each one can be deleted. Learning can be paused. Pause also stops screen reading. While reading is on, the panel shows a mark, so the laptop is never watching quietly.

Risky actions still ask, even when they match an old pattern. Delete, send, pay, and turning Wi-Fi off wait for a yes. Volume and brightness can apply immediately, and they are still logged.

A suggestion is one line, such as “Open your notes?”. Dismissing it is a correction. A stack of popups is a bug.

## Why this stays a small program

The always-on piece writes short rows. It does not keep a vision model loaded to stare at the desktop. The accessibility tree is already there. Reading it is a query, not a camera.

Habits start as counts and recent examples, not as a second large neural net. If a later version ranks habits with a tiny model, that model has to load, answer, and leave, under the same RAM budget as everything else on this 8GB machine.

The database lives on the laptop. It does not go in git, and it does not go to an account.

## What I have not built yet

This is the design I will implement after the base system is measured. The first memory will arrive with typed commands, before the microphone exists, so the loop can be tested without voice in the way. Voice joins the same store later.

If you want the hardware side of the same idea, the next post is how a local LLM, speech-to-text, and a wake word are supposed to share 8GB with a browser.

---

Savindu Thathsara builds practical AI and automation in London. This series is the public log of an offline AI operating system he is writing and learning at the same time.

- Site: [https://savithathsara.me](https://savithathsara.me)
- Email: savindu@savithathsara.me
- DEV: [https://dev.to/savinduthathsara](https://dev.to/savinduthathsara)
