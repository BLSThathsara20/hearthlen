# How a milestone becomes a post

A major result gets one post in `blog/`, then `python3 blog/publish.py`. The post should be interesting to a developer who does not have this repo open. The working notes in `guide/` stay the textbook. The post is the story.

Author on every post: Savindu Thathsara, [savithathsara.me](https://savithathsara.me), savindu@savithathsara.me.

## Publish one of these

- A phase exit from [guide/07-roadmap.md](../guide/07-roadmap.md), pass or fail
- A skill that works from a real sentence
- A measured number: boot, RAM, tokens per second, wake-to-action, accuracy
- A design change another developer could reuse
- A break that taught something specific

Skip typo fixes, dependency bumps, refactors with no lesson, and any sentence that treats a target as a measurement. "The gate is 600MB" is fine. "Idle RAM is 600MB" waits until `docs/benchmarks/` says so.

## The hook

The first two sentences are a scene, a constraint, or a result. They contain a concrete thing: a laptop, a number, a sentence the user said, a failure.

Write: "Eight gigabytes sounds like enough until a browser and a language model want it at the same time."

Avoid: "In this article I will explore the architecture of our offline AI operating system."

Then say who is writing, in one line, and which part of the series this is. Put the lesson in the middle. End with what is next, as a link to another file in this folder (`02-some-post.md`). The publisher turns that into the live URL.

## SEO

Frontmatter on every file, same shape as [01-offline-ai-operating-system.md](01-offline-ai-operating-system.md).

- `seo_title`: under 60 characters, the phrase a person would search
- `seo_description`: about 140–160 characters, includes Savindu Thathsara once
- `devto_tags`: exactly four, from tags developers already follow: `ai`, `linux`, `opensource`, `machinelearning`, `privacy`, `productivity`, `tutorial`, `python`
- `hashnode_tags`: the specific phrases, such as `local-llm`, `edge-ai`, `build-in-public`
- Series name stays `Offline AI OS`
- Use the keywords in the title and the first paragraph. Do not paste a keyword list at the bottom

Keywords for this project: offline AI operating system, local LLM, on-device AI assistant, small language model, edge AI, privacy-first AI, lightweight Linux, llama.cpp, 8GB RAM, build in public.

## Publish

```bash
python3 blog/publish.py blog/05-your-new-post.md
```

With no arguments, the script publishes every `blog/NN-*.md` file. It creates a post once and updates it after that. State is `blog/published.json`.

Hashnode goes first when `HASHNODE_PUBLICATION_ID` is set in `.env`. Dev.to then uses that URL as the canonical link. Keys live only in `.env`. That file is gitignored.

## Footer

Close with this block, then stop.

```markdown
---

Savindu Thathsara builds practical AI and automation in London. This series is the public log of an offline AI operating system he is writing and learning at the same time.

- Site: [https://savithathsara.me](https://savithathsara.me)
- Email: savindu@savithathsara.me
- DEV: [https://dev.to/savinduthathsara](https://dev.to/savinduthathsara)
```
