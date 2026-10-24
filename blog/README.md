# Blog posts

Public build log for the offline AI operating system. Each update gets a new markdown file in this folder before it goes anywhere else. [PROJECT.md](../PROJECT.md) and [guide/](../guide/) stay the working notes. These posts are the version for readers.

Author: **Savindu Thathsara**
Site: [https://savithathsara.me](https://savithathsara.me)
Email: savindu@savithathsara.me
DEV profile: [https://dev.to/savinduthathsara](https://dev.to/savinduthathsara)

## Posts

Publish in this order. They are one series: **Offline AI OS**.

| File | SEO title | Dev.to tags (max 4) |
|---|---|---|
| [01-offline-ai-operating-system.md](01-offline-ai-operating-system.md) | Offline AI OS for an 8GB Laptop \| Savindu Thathsara | `ai`, `linux`, `opensource`, `machinelearning` |
| [02-assistant-that-learns-your-habits.md](02-assistant-that-learns-your-habits.md) | Local AI Assistant That Learns Your Habits | `ai`, `privacy`, `linux`, `productivity` |
| [03-local-ai-on-8gb-ram.md](03-local-ai-on-8gb-ram.md) | Run a Local LLM Assistant on 8GB RAM | `ai`, `linux`, `machinelearning`, `tutorial` |
| [04-build-in-public-roadmap.md](04-build-in-public-roadmap.md) | Build in Public: Offline AI OS Roadmap | `ai`, `linux`, `opensource`, `productivity` |

Hashnode can take the extra tags in each file’s frontmatter (`hashnode_tags`). Dev.to allows four tags, so use `devto_tags` there.

## Why this folder exists

These files are the public version of the project. [WRITING.md](WRITING.md) is the rule for the next post: a concrete hook, SEO fields, and the author footer. A Cursor rule in `.cursor/rules/publish-milestones.mdc` tells later sessions to do that when a major result lands.

Keys live in `.env` at the repo root. That file is gitignored. `.env.example` shows the names only.

```bash
python3 blog/publish.py
```

That publishes every numbered post. Pass one file to publish just that post. The script creates a post once and updates it after that. Live URLs are stored in `published.json`.

Dev.to publishes with the API key. Hashnode publishes only after `HASHNODE_PUBLICATION_ID` is set. The Hashnode account `@savindu` is valid, and it does not have a publication yet. The API cannot create one. Create it at [hashnode.com](https://hashnode.com), copy the publication id into `.env`, and run the script again. Hashnode goes out first. Dev.to then uses that URL as the canonical link.

Manual paste still works: copy from the `#` heading down, and fill the title, description, and tags from the frontmatter. Leave the frontmatter out of the body.

## Keywords used across the series

offline AI operating system, local LLM, on-device AI assistant, small language model, edge AI, privacy-first AI, lightweight Linux, Debian, llama.cpp, offline voice assistant, AI agent with memory, open source, 8GB RAM, Savindu Thathsara.

Use them in titles, the first paragraph, and headings. They are already written into the posts. Do not add a raw keyword list at the bottom of a post.
