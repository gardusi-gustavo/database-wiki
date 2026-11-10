#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors = []
index = json.loads((ROOT / "data/index.json").read_text())
pages = {}
for entry in index.get("pages", []):
    path = ROOT / "data" / entry["path"]
    if not path.is_file():
        errors.append(f"missing page: {entry['path']}")
        continue
    page = json.loads(path.read_text())
    for key in ("id", "title", "slug", "tags", "body", "updated"):
        if key not in page:
            errors.append(f"{entry['path']}: missing {key}")
    if page.get("id") != entry.get("id"):
        errors.append(f"{entry['path']}: id mismatch")
    if page.get("slug") not in {entry["id"], page.get("id")}:
        errors.append(f"{entry['path']}: slug should match id")
    pages[page.get("id")] = page
if len(pages) != len(index.get("pages", [])):
    errors.append("duplicate page ids")
for error in errors:
    print(f"ERROR: {error}", file=sys.stderr)
if errors:
    raise SystemExit(1)
print(f"wiki ok: {len(pages)} pages")
