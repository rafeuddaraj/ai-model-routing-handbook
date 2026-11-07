#!/usr/bin/env python3
"""Summarize a Decision Log CSV by phase and tier (see routing-kit/05-decision-log.md).

Columns used: phase, tier, result, rework_minutes, escalated
`result` is one of: accepted, accepted_with_rework, rejected
`escalated` is yes or no.

Usage:
    python3 scripts/summarize_decision_log.py templates/decision-log.example.csv
    python3 scripts/summarize_decision_log.py my-log.csv --markdown
"""

import argparse
import csv
from collections import defaultdict

RESULTS = ("accepted", "accepted_with_rework", "rejected")


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())]
    return rows


def summarize(rows):
    groups = defaultdict(lambda: {"n": 0, "accepted": 0, "accepted_with_rework": 0, "rejected": 0,
                                  "rework": 0.0, "rework_n": 0, "escalated": 0})
    for r in rows:
        key = ((r.get("phase") or "").strip().lower(), (r.get("tier") or "").strip().lower())
        g = groups[key]
        g["n"] += 1
        res = (r.get("result") or "").strip().lower()
        if res in RESULTS:
            g[res] += 1
        try:
            g["rework"] += float(r.get("rework_minutes") or 0)
            g["rework_n"] += 1
        except ValueError:
            pass
        if (r.get("escalated") or "").strip().lower() in ("yes", "y", "true"):
            g["escalated"] += 1
    out = []
    for (phase, tier), g in sorted(groups.items()):
        out.append({
            "phase": phase, "tier": tier, "n": g["n"],
            "first_time_rate": g["accepted"] / g["n"],
            "accepted_with_rework": g["accepted_with_rework"],
            "rejected": g["rejected"],
            "avg_rework_min": (g["rework"] / g["rework_n"]) if g["rework_n"] else 0.0,
            "escalations": g["escalated"],
        })
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_path")
    ap.add_argument("--markdown", action="store_true")
    a = ap.parse_args(argv)
    try:
        rows = load(a.csv_path)
    except OSError as e:
        ap.error(str(e))
    if not rows:
        ap.error("no entries found")
    summary = summarize(rows)
    head = ["Phase", "Tier", "Entries", "Accepted first time", "With rework", "Rejected", "Avg rework min", "Escalations"]
    lines = [[s["phase"], s["tier"], str(s["n"]), f"{s['first_time_rate']:.0%}", str(s["accepted_with_rework"]),
              str(s["rejected"]), f"{s['avg_rework_min']:.1f}", str(s["escalations"])] for s in summary]
    if a.markdown:
        print("| " + " | ".join(head) + " |")
        print("|" + "---|" * len(head))
        for l in lines:
            print("| " + " | ".join(l) + " |")
    else:
        widths = [max(len(h), *(len(l[i]) for l in lines)) for i, h in enumerate(head)]
        print("  ".join(h.ljust(widths[i]) for i, h in enumerate(head)))
        for l in lines:
            print("  ".join(c.ljust(widths[i]) for i, c in enumerate(l)))
    print(f"\nEntries: {len(rows)}. Small samples are noise. Look for patterns over a month, not single results.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
