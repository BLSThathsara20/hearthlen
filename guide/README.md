# Guide

This folder is the map for the project. [PROJECT.md](../PROJECT.md) is the original brief. These notes explain that brief, add the personal assistant that learns, and say what to build in which order.

Read them before writing the operating system. When a later session starts a phase, it follows [07-roadmap.md](07-roadmap.md). Packages, model weights, and install scripts stay out of the repo until that phase starts.

## Two kinds of learning

You are learning how to build a small Linux system and a local assistant. Each file starts with what that file is teaching.

The assistant, once it is running on the laptop, learns how you use that laptop. It keeps that memory on the machine. [03-assistant-that-learns.md](03-assistant-that-learns.md) describes that loop. Your study notes and the assistant’s memory are different things.

## Read in this order

1. [01-scope.md](01-scope.md) — who it is for, the laptop, what version 1 includes, and the memory limits.
2. [02-what-we-will-do.md](02-what-we-will-do.md) — the path from this repo to a laptop that listens, acts, and remembers.
3. [03-assistant-that-learns.md](03-assistant-that-learns.md) — how habits form from commands and from what is on screen.
4. [04-ui.md](04-ui.md) — what the person sees and hears.
5. [05-architecture.md](05-architecture.md) — the pieces and how a request moves through them.
6. [06-decisions.md](06-decisions.md) — choices already made, and the few still open.
7. [07-roadmap.md](07-roadmap.md) — Phases 0–6. This is the checklist after the guide.

## How to use a file

Read the learning note at the top. Then read the rules. If a later change disagrees with [PROJECT.md](../PROJECT.md), record it in [06-decisions.md](06-decisions.md) and keep the brief and the guide pointing at each other.

The guide is written in English. The product’s user-facing words will also live in string files, with a language tag, so Sinhala can be added later without rewriting the skills.

Public writing is separate. A major result becomes a post under [blog/](../blog/) using [blog/WRITING.md](../blog/WRITING.md), then `python3 blog/publish.py`. The first two sentences of that post are a hook, not a table of contents.

## Where we are

The guide is the current work. Phase 0 has not started. The ThinkPad does not get Debian from these notes alone. The next build step is Phase 0 in [07-roadmap.md](07-roadmap.md), when you choose to start it.
