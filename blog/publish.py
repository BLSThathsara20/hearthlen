#!/usr/bin/env python3
"""Publish blog posts to Hashnode, then Dev.to.

Secrets are read from the repo .env file. They are never printed.
Hashnode runs only when HASHNODE_PUBLICATION_ID is set. Dev.to always runs.
A second pass rewrites links between posts to the live URLs.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = Path(__file__).resolve().parent
STATE = BLOG / "published.json"
ENV_FILE = ROOT / ".env"


def load_env() -> None:
    if not ENV_FILE.exists():
        return
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def parse_post(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise SystemExit(f"{path.name} needs frontmatter")
    _, front, body = text.split("---", 2)
    data: dict = {}
    list_key = None
    for raw in front.splitlines():
        if not raw.strip():
            continue
        if raw.startswith("  - ") and list_key:
            data.setdefault(list_key, []).append(raw.strip()[2:].strip())
            continue
        if ":" not in raw or raw.startswith(" "):
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"')
        if value == "":
            data[key] = []
            list_key = key
        else:
            list_key = None
            data[key] = value
    return data, body.lstrip("\n")


def posts_from_args(argv: list[str]) -> list[Path]:
    if argv:
        return [Path(item).resolve() for item in argv]
    return sorted(BLOG.glob("[0-9][0-9]-*.md"))


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {}


def save_state(state: dict) -> None:
    STATE.write_text(json.dumps(state, indent=2) + "\n")


def devto_request(method: str, url: str, payload: dict | None = None, attempt: int = 0) -> dict:
    data = None if payload is None else json.dumps(payload).encode()
    request = urllib.request.Request(url, data=data, method=method)
    request.add_header("api-key", os.environ["DEV_TO_API_KEY"])
    request.add_header("Content-Type", "application/json")
    request.add_header("Accept", "application/vnd.forem.api-v1+json")
    request.add_header("User-Agent", "ai-os-blog-publish")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read().decode()
    except urllib.error.HTTPError as error:
        detail = error.read().decode(errors="replace")[:500]
        if error.code == 429 and attempt < 6:
            match = re.search(r"(\d+) second", detail)
            wait = int(match.group(1)) + 2 if match else 35
            print(f"Dev.to rate limit, waiting {wait}s")
            time.sleep(wait)
            return devto_request(method, url, payload, attempt + 1)
        raise SystemExit(f"Dev.to {method} failed ({error.code}): {detail}") from error
    return json.loads(raw) if raw else {}


def existing_devto() -> dict[str, dict]:
    found = {}
    for bucket in ("published", "unpublished"):
        page = 1
        while page <= 5:
            rows = devto_request(
                "GET",
                f"https://dev.to/api/articles/me/{bucket}?per_page=100&page={page}",
            )
            if not isinstance(rows, list) or not rows:
                break
            for row in rows:
                found[row.get("title", "")] = row
            if len(rows) < 100:
                break
            page += 1
    return found


def rewrite_links(body: str, urls: dict[str, str]) -> str:
    def replace(match: re.Match) -> str:
        name = match.group(1)
        url = urls.get(name)
        if not url:
            return match.group(0)
        return f"]({url})"

    return re.sub(r"\]\(([0-9]{2}-[^)]+\.md)\)", replace, body)


def hashnode_publish(meta: dict, body: str, canonical: str) -> str | None:
    publication = os.environ.get("HASHNODE_PUBLICATION_ID", "").strip()
    token = os.environ.get("HASHNODE_PAT", "").strip()
    if not publication or not token:
        return None
    command = [
        "npx",
        "--yes",
        "@hashnode/cli",
        "--json",
        "--publication-id",
        publication,
        "post",
        "create",
        "--title",
        meta["title"],
        "--content-file",
        "-",
        "--slug",
        meta["slug"],
        "--meta-title",
        meta["seo_title"],
        "--meta-description",
        meta["seo_description"],
        "--enable-toc",
        "true",
    ]
    if meta.get("subtitle"):
        command.extend(["--subtitle", meta["subtitle"]])
    if canonical:
        command.extend(["--original-article-url", canonical])
    for tag in meta.get("hashnode_tags") or []:
        command.extend(["--tag", tag])
    env = os.environ.copy()
    env["HASHNODE_PAT"] = token
    result = subprocess.run(
        command,
        input=body.encode(),
        capture_output=True,
        env=env,
        check=False,
    )
    stdout = result.stdout.decode(errors="replace")
    stderr = result.stderr.decode(errors="replace")
    if result.returncode != 0:
        print(f"Hashnode skipped for {meta['slug']}: {stderr.strip() or stdout.strip()}")
        return None
    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError:
        payload = {}
    url = (
        payload.get("url")
        or payload.get("post", {}).get("url")
        or ""
    )
    if not url:
        match = re.search(r"https://\S+", stdout)
        url = match.group(0).rstrip(").,") if match else ""
    return url or None


def article_payload(meta: dict, body: str, canonical: str) -> dict:
    tags = [tag.strip() for tag in str(meta.get("devto_tags", "")).split(",") if tag.strip()]
    article = {
        "title": meta["title"],
        "published": True,
        "body_markdown": body,
        "tags": tags[:4],
        "series": meta.get("series") or "Offline AI OS",
        "description": meta.get("seo_description") or "",
    }
    if canonical:
        article["canonical_url"] = canonical
    return {"article": article}


def main() -> None:
    load_env()
    if not os.environ.get("DEV_TO_API_KEY"):
        raise SystemExit("DEV_TO_API_KEY is missing. Put it in .env (see .env.example).")
    paths = posts_from_args(sys.argv[1:])
    if not paths:
        raise SystemExit("No posts found.")
    state = load_state()
    already = existing_devto()
    parsed = []
    for path in paths:
        meta, body = parse_post(path)
        parsed.append((path, meta, body))

    if not os.environ.get("HASHNODE_PUBLICATION_ID", "").strip():
        print("Hashnode account is connected, and it has no publication id yet.")
        print("Create one publication on hashnode.com, put its id in .env, then run this again.")

    urls: dict[str, str] = {}
    for path, meta, body in parsed:
        key = path.name
        entry = state.get(key, {})
        canonical = entry.get("hashnode_url") or ""
        if not canonical:
            canonical = hashnode_publish(meta, body, "") or ""
            if canonical:
                entry["hashnode_url"] = canonical
                print(f"Hashnode {canonical}")
        devto_id = entry.get("devto_id") or (already.get(meta["title"]) or {}).get("id")
        payload = article_payload(meta, body, canonical)
        if devto_id:
            response = devto_request("PUT", f"https://dev.to/api/articles/{devto_id}", payload)
            action = "updated"
        else:
            response = devto_request("POST", "https://dev.to/api/articles", payload)
            action = "published"
            time.sleep(20)
        devto_id = response.get("id") or devto_id
        devto_url = response.get("url") or entry.get("devto_url") or ""
        entry.update({"title": meta["title"], "devto_id": devto_id, "devto_url": devto_url})
        state[key] = entry
        urls[key] = canonical or devto_url
        save_state(state)
        print(f"Dev.to {action} {devto_url}")

    for path, meta, body in parsed:
        key = path.name
        entry = state[key]
        linked = rewrite_links(body, urls)
        if linked == body:
            continue
        canonical = entry.get("hashnode_url") or ""
        devto_request(
            "PUT",
            f"https://dev.to/api/articles/{entry['devto_id']}",
            article_payload(meta, linked, canonical),
        )
        print(f"Dev.to linked {entry['devto_url']}")
        time.sleep(2)

    # A body update clears the series. Set it after the body is final.
    for path, meta, _body in parsed:
        series = meta.get("series")
        entry = state.get(path.name) or {}
        if not series or not entry.get("devto_id"):
            continue
        devto_request(
            "PUT",
            f"https://dev.to/api/articles/{entry['devto_id']}",
            {"article": {"series": series}},
        )
        print(f"Dev.to series {series}")
        time.sleep(2)


if __name__ == "__main__":
    main()
