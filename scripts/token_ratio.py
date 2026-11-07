#!/usr/bin/env python3
"""Summarize a Token Tax experiment (see routing-kit/08-token-tax-experiment.md).

Input: a CSV with the columns  passage,english_tokens,other_tokens
Each row is the same passage written in English and in another language, with
the input token count read from the model's API usage field.

Usage:
    python3 scripts/token_ratio.py templates/token-tax.csv
    python3 scripts/token_ratio.py my-results.csv --markdown
"""

import argparse
import csv
import statistics


def load_rows(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for i, r in enumerate(csv.DictReader(f), start=2):
            if not any((v or "").strip() for v in r.values()):
                continue
            try:
                en = float(r["english_tokens"])
                other = float(r["other_tokens"])
            except (KeyError, TypeError, ValueError):
                continue  # skip unfilled template rows
            if en <= 0 or other <= 0:
                raise ValueError(f"line {i}: token counts must be positive")
            rows.append({"passage": r.get("passage", str(i - 1)), "en": en, "other": other, "ratio": other / en})
    return rows


def summarize(rows):
    if not rows:
        raise ValueError("no completed rows found")
    ratios = [r["ratio"] for r in rows]
    return {
        "n": len(rows),
        "mean": statistics.mean(ratios),
        "median": statistics.median(ratios),
        "min": min(ratios),
        "max": max(ratios),
        "total_ratio": sum(r["other"] for r in rows) / sum(r["en"] for r in rows),
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_path")
    ap.add_argument("--markdown", action="store_true", help="print a Markdown table")
    a = ap.parse_args(argv)
    try:
        rows = load_rows(a.csv_path)
        s = summarize(rows)
    except (OSError, ValueError) as e:
        ap.error(str(e))
    if a.markdown:
        print("| Passage | English tokens | Other tokens | Ratio |")
        print("|---|---|---|---|")
        for r in rows:
            print(f"| {r['passage']} | {r['en']:.0f} | {r['other']:.0f} | {r['ratio']:.2f} |")
        print(f"| **Mean ratio** | | | **{s['mean']:.2f}** |")
    else:
        for r in rows:
            print(f"{r['passage']:>12}  en={r['en']:.0f}  other={r['other']:.0f}  ratio={r['ratio']:.2f}")
        print("-" * 44)
        print(f"passages={s['n']}  mean={s['mean']:.2f}  median={s['median']:.2f}  "
              f"min={s['min']:.2f}  max={s['max']:.2f}  total={s['total_ratio']:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
