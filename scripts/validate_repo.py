#!/usr/bin/env python3
"""Repository checks used by CI and contributors.

Checks
  1. Relative links in Markdown files point to files that exist.
  2. CSV files parse and every row has the header's number of columns.
  3. JSON, TOML, and SVG (XML) files parse.

Run from the repository root:  python3 scripts/validate_repo.py
"""

import csv
import json
import re
import sys
import tomllib
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "__pycache__", "node_modules"}
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"```.*?```", re.S)
INLINE = re.compile(r"`[^`\n]*`")


def files(suffix):
    for p in ROOT.rglob(f"*{suffix}"):
        if not (set(p.relative_to(ROOT).parts) & SKIP_DIRS):
            yield p


def check_markdown_links():
    errors = []
    for p in files(".md"):
        text = INLINE.sub("", FENCE.sub("", p.read_text(encoding="utf-8")))
        for target in LINK.findall(text):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            if not path:
                continue
            if not (p.parent / path).resolve().exists():
                errors.append(f"{p.relative_to(ROOT)}: broken link -> {target}")
    return errors


def check_csv():
    errors = []
    for p in files(".csv"):
        with open(p, newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f))
        if not rows:
            errors.append(f"{p.relative_to(ROOT)}: empty file")
            continue
        n = len(rows[0])
        for i, r in enumerate(rows[1:], start=2):
            if r and len(r) != n:
                errors.append(f"{p.relative_to(ROOT)}: line {i} has {len(r)} columns, expected {n}")
    return errors


def check_structured():
    errors = []
    for p in files(".json"):
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except ValueError as e:
            errors.append(f"{p.relative_to(ROOT)}: invalid JSON ({e})")
    for p in files(".toml"):
        try:
            tomllib.loads(p.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as e:
            errors.append(f"{p.relative_to(ROOT)}: invalid TOML ({e})")
    for p in files(".svg"):
        try:
            ET.parse(p)
        except ET.ParseError as e:
            errors.append(f"{p.relative_to(ROOT)}: invalid SVG/XML ({e})")
    return errors


def main():
    errors = check_markdown_links() + check_csv() + check_structured()
    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s) found.")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
