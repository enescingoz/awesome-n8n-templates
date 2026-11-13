#!/usr/bin/env python3
"""Every template in this repo must be exactly one JSON value with a nodes array.

n8n's import dialog parses the file as a single JSON document. A file that is a
valid workflow followed by a stray title, or by a second complete workflow,
looks fine in an editor and is rejected on import. This check catches that at
review time instead of at download time.
"""
import io
import json
import os
import sys

SKIP_DIRS = {".git", ".github"}
# 0 bytes in the repo for a long time; not a workflow and not something this
# check should delete.
ALLOW_EMPTY = {"Other/ALL_unique_nodes.json"}


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dec = json.JSONDecoder()
    bad = []
    checked = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            if not name.lower().endswith(".json"):
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            checked += 1
            raw = io.open(full, encoding="utf-8").read()
            if not raw.strip():
                if rel not in ALLOW_EMPTY:
                    bad.append((rel, "empty file"))
                continue
            try:
                obj, end = dec.raw_decode(raw)
            except json.JSONDecodeError as exc:
                bad.append((rel, "not JSON: %s" % exc))
                continue
            trailing = raw[end:].strip()
            if trailing:
                bad.append((rel, "%d characters of trailing text after the first JSON value" % len(trailing)))
                continue
            if not isinstance(obj, dict) or not isinstance(obj.get("nodes"), list):
                bad.append((rel, "no nodes array"))
    print("%d JSON files checked, %d problem(s)" % (checked, len(bad)))
    for rel, why in bad:
        print("  %s: %s" % (rel, why))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
