# Scope

**What you are learning here.** A project scope says who the system is for, which machine it must run on, what the first version will do, and what is intentionally left for later. Writing this down keeps the laptop fast and the assistant accurate.

The original brief is [PROJECT.md](../PROJECT.md). This file is the boundary we build inside.

## Who it is for

The person using the laptop is a normal user. They speak or type ordinary sentences. They do not manage a terminal, pick models, or read logs to get through the day.

You, the builder, are also part of the project. The work is arranged so that each phase teaches one layer: the base system, then measurement, then skills, then voice, then training, then updates. The guide is the textbook. The laptop is the lab.

## The laptop it must fit

The test machine is an everyday Lenovo ThinkPad.

| Spec | Target |
|---|---|
| RAM | 8GB |
| Storage | 256GB SSD |
| Graphics | Integrated only, no discrete GPU |
| CPU | Ordinary Intel or AMD, x86_64 |
| Network | Optional. Needed for updates and for online pages such as YouTube |

If a feature is too heavy for this machine, it is out of scope until it can be made light enough. The Mac is where the notes and code are written. The ThinkPad is where speed and memory are judged.

## What version 1 includes

- A small Debian desktop that leaves most of the RAM for the person’s own apps.
- An offline assistant. Speech, understanding, and replies run on the laptop. No cloud model API.
- A fixed set of skills that do everyday tasks reliably. The model chooses a skill and fills in the details. The skill does the work.
- A local memory of this person’s routines, including what is on screen, so the next time is easier.
- English speech and text. The data and voice setup keep a language tag so Sinhala can be added later.
- Safe updates, with a way back if an update breaks the assistant.
- A simple screen: a normal desktop, a small assistant card, and a page that shows what has been learned.

## Everyday tasks in the first skill set

These are the first skills, from the brief:

- Play something on YouTube.
- Open an app.
- Set, raise, lower, or mute the volume.
- Set the screen brightness.
- Find a file from a description, and open a file.
- Search the web.
- Set a reminder.
- Take a screenshot.
- Turn Wi-Fi on or off.

Later the set can grow toward the 30–50 tasks people ask for most often. New skills are added one at a time, after the current ones work.

## What waits

These are real parts of the idea. They are not in the first build.

- Sinhala speech models, a Sinhala voice, and Sinhala training sentences. The hooks exist first. The weights and the labeled sentences come after English is solid.
- A search that understands the meaning inside every file. Version 1 matches names, folders, and dates. Memory can remember which folder was right last time.
- Guessing where to click from a screenshot. Skills do the action. Screen reading is for learning what the person is looking at, not for inventing mouse clicks.
- A second browser-automation stack on the installed system. YouTube opens in Chromium at the video page.
- A discrete GPU, CUDA, or any cloud inference.
- The assistant inventing shell commands. If there is no skill, it says so.
- Final wallpaper and boot artwork. Those belong to the polish phase. The name is already Hearthlen.
- Rewriting the always-on program in Rust or Go. Python is the prototype. A rewrite happens only if the memory numbers require it.

## Memory budget

On an 8GB laptop the assistant has to stay small so the person can still browse, watch video, and edit documents.

| Piece | Budget |
|---|---|
| Base system and desktop, sitting idle | about 400–600MB |
| Always on: wake word and the small understanding model | about 150–250MB |
| Loaded only while a request is in progress: speech-to-text, the small fallback model, spoken reply | about 1.5–2GB, then released |
| Left for the person | 5GB or more |

Heavy pieces load for one step, then unload. Wake word and the tiny understanding model are the pieces that stay resident. These numbers are gates. Each phase records the real figure on the ThinkPad. A feature that breaks the gate waits or shrinks.

## What “good” means

Version 1 is good when all of these are true:

- The ThinkPad still feels quick with the assistant installed.
- The first skills do the thing the person asked, in English, by voice or by typing.
- After repeated use, vague requests get easier: the usual song, the usual folder, the brightness they already prefer at night.
- The person can see what was learned, delete a habit, or pause learning.
- Risky actions ask first, and actions can be traced.
- Boot time, idle RAM, response time, and accuracy are written down for the release.

## Name

The system and the assistant are both called Hearthlen. The wake phrase is “hey Hearthlen”. Wallpaper and the boot screen come in the polish phase. The domain to hold is hearthlen.com.
