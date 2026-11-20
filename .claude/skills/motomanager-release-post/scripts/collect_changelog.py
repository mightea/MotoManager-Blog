#!/usr/bin/env python3
"""Collect one month's release-please entries for the web app and the iOS app.

Usage:
    python3 collect_changelog.py 2026-12            # month to collect
    python3 collect_changelog.py 2026-12 --root /path/to/MotoManager-Project

Prints, per component, every release in that month (newest first) with its
date, the GitHub compare URL for the "All changes" link, and its entries
grouped by section. Commit hashes and links are stripped so the output is
easy to rewrite. Sections that never belong in a rider-facing post
(chores, CI, docs, tests, refactors, styles) are listed separately under
"skipped" so you can still tell when a release had nothing visible.

The API (MotoManagerApi) is deliberately not collected: the blog is for
riders, and API changes show up through the web app and iOS app anyway.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

COMPONENTS = {
    # label: (repo folder, GitHub repo, tag prefix)
    "Web app": ("MotoManager", "mightea/MotoManager", ""),
    "iOS app": ("MotoManagerApp", "mightea/MotoManager-App", "v"),
}

SKIP_SECTIONS = ("chore", "continuous integration", "documentation", "tests", "refactor", "styles", "build")

HEADER = re.compile(r"^## \[(?P<version>[^\]]+)\]\((?P<url>[^)]*)\) \((?P<date>\d{4}-\d{2}-\d{2})\)")
SECTION = re.compile(r"^### (?P<name>.+)")
ENTRY = re.compile(r"^\* (?P<text>.+)")


def clean(text: str) -> str:
    text = re.sub(r" \(\[[0-9a-f]{7,}\]\([^)]*\)\)", "", text)  # (hash link)
    text = re.sub(r", closes \[#\d+\]\([^)]*\)", "", text)        # closes #N
    text = re.sub(r"\*\*([^*]+):\*\* ", r"[\1] ", text)            # **scope:**
    return text.strip()


def parse(path: Path):
    releases, current, section = [], None, None
    for line in path.read_text().splitlines():
        if m := HEADER.match(line):
            current = {**m.groupdict(), "sections": {}}
            releases.append(current)
            section = None
        elif current and (m := SECTION.match(line)):
            section = re.sub(r"^[^\w]+", "", m["name"]).strip()  # drop emoji
            current["sections"].setdefault(section, [])
        elif current and section and (m := ENTRY.match(line)):
            current["sections"][section].append(clean(m["text"]))
    return releases


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("month", help="YYYY-MM")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[5],
                    help="MotoManager-Project folder (default: inferred from this script's location)")
    args = ap.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}", args.month):
        print("month must look like 2026-12", file=sys.stderr)
        return 2

    for label, (folder, repo, prefix) in COMPONENTS.items():
        changelog = args.root / folder / "CHANGELOG.md"
        if not changelog.exists():
            print(f"!! {changelog} not found — pull the repo or pass --root", file=sys.stderr)
            continue
        releases = parse(changelog)
        month = [r for r in releases if r["date"].startswith(args.month)]
        print(f"\n=============== {label} ({repo}) ===============")
        if not month:
            print("(no releases this month)")
            continue
        for r in month:
            idx = releases.index(r)
            prev = releases[idx + 1]["version"] if idx + 1 < len(releases) else None
            d = date.fromisoformat(r["date"])
            compare = (f"https://github.com/{repo}/compare/{prefix}{prev}...{prefix}{r['version']}"
                       if prev else r["url"])
            print(f"\n### {r['version']} – {d.strftime('%B')} {d.day}")
            print(f"compare: {compare}")
            skipped = []
            for name, entries in r["sections"].items():
                if any(s in name.lower() for s in SKIP_SECTIONS):
                    skipped += entries
                    continue
                for e in entries:
                    kind = "Fix: " if "fix" in name.lower() else ("Revert: " if "revert" in name.lower() else "")
                    print(f"- {kind}{e}")
            if skipped:
                print(f"  (skipped: {'; '.join(skipped)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
