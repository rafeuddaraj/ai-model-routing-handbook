#!/usr/bin/env python3
"""Cost per Accepted Output calculator.

Token price is not the price of a result. A cheap model that is rejected often
can cost more than an expensive one that is accepted first time, because every
rejected attempt also costs review and rework time.

Formulas
    attempt_cost = (input_tokens - cached_tokens) / 1e6 * input_price
                 + cached_tokens / 1e6 * cached_price
                 + output_tokens / 1e6 * output_price      (thinking tokens count as output)
    cost_per_accepted = (attempt_cost + review_cost) / acceptance_rate

Examples
    python3 scripts/cost_calculator.py --demo
    python3 scripts/cost_calculator.py --input-tokens 80000 --output-tokens 15000 \
        --input-price 2 --output-price 10 --acceptance 0.6 --review-cost 10
    python3 scripts/cost_calculator.py --input-tokens 80000 --cached-tokens 50000 \
        --cached-price 0.2 --output-tokens 15000 --input-price 2 --output-price 10 \
        --acceptance 0.6 --review-cost 10 --json

Every number you pass in is your own assumption or measurement. Prices are USD
per 1 million tokens. Confirm prices on each vendor's official page.
"""

import argparse
import json


def attempt_cost(input_tokens, output_tokens, input_price, output_price,
                 cached_tokens=0, cached_price=None):
    """Model cost of one attempt, in USD."""
    if min(input_tokens, output_tokens, input_price, output_price, cached_tokens) < 0:
        raise ValueError("tokens and prices must not be negative")
    if cached_tokens > input_tokens:
        raise ValueError("cached_tokens cannot exceed input_tokens")
    if cached_price is None:
        cached_price = input_price
    fresh = input_tokens - cached_tokens
    return (fresh / 1_000_000 * input_price
            + cached_tokens / 1_000_000 * cached_price
            + output_tokens / 1_000_000 * output_price)


def cost_per_accepted(model_cost, review_cost, acceptance):
    """Expected total cost to obtain one accepted result."""
    if not 0 < acceptance <= 1:
        raise ValueError("acceptance must be greater than 0 and at most 1")
    if model_cost < 0 or review_cost < 0:
        raise ValueError("costs must not be negative")
    return (model_cost + review_cost) / acceptance


# Illustrative snapshot. List prices as of 2026-11-07 (see SOURCES.md).
# Acceptance rates are ASSUMPTIONS used to demonstrate the method, not measurements.
DEMO_MODELS = [
    # name, input $/M, output $/M, acceptance on a hard task, acceptance on an easy task
    ("Fast tier (Haiku 5.5 list price)", 0.10, 0.50, 0.30, 0.90),
    ("Balanced tier (Sonnet 5.5 list price)", 2.00, 10.00, 0.60, 0.95),
    ("Strong tier (Opus 5.5 list price)", 4.00, 20.00, 0.80, 0.95),
]
DEMO_INPUT_TOKENS = 80_000
DEMO_OUTPUT_TOKENS = 15_000
DEMO_REVIEW_COST = 10.0  # USD of human time per attempt (assumption)


def demo_rows():
    rows = []
    for name, p_in, p_out, hard, easy in DEMO_MODELS:
        m = attempt_cost(DEMO_INPUT_TOKENS, DEMO_OUTPUT_TOKENS, p_in, p_out)
        rows.append({
            "name": name,
            "model_cost": m,
            "hard": cost_per_accepted(m, DEMO_REVIEW_COST, hard),
            "easy": cost_per_accepted(m, DEMO_REVIEW_COST, easy),
            "hard_rate": hard,
            "easy_rate": easy,
        })
    return rows


def run_demo():
    print("Demo (ASSUMED numbers, replace with your own measurements)")
    print(f"Per attempt: {DEMO_INPUT_TOKENS:,} input + {DEMO_OUTPUT_TOKENS:,} output tokens, "
          f"review cost ${DEMO_REVIEW_COST:.2f} per attempt\n")
    header = f"{'Tier':40} {'Model $':>8} {'Hard $/acc':>11} {'Easy $/acc':>11}"
    print(header)
    print("-" * len(header))
    for r in demo_rows():
        print(f"{r['name']:40} {r['model_cost']:>8.4f} {r['hard']:>11.2f} {r['easy']:>11.2f}")


def build_parser():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--demo", action="store_true", help="print the worked example from the handbook")
    ap.add_argument("--input-tokens", type=float, help="total input tokens per attempt")
    ap.add_argument("--cached-tokens", type=float, default=0.0,
                    help="part of the input served from cache (default 0)")
    ap.add_argument("--output-tokens", type=float, help="output tokens per attempt, including thinking")
    ap.add_argument("--input-price", type=float, help="USD per 1M input tokens")
    ap.add_argument("--cached-price", type=float, default=None,
                    help="USD per 1M cached input tokens (default: same as input price)")
    ap.add_argument("--output-price", type=float, help="USD per 1M output tokens")
    ap.add_argument("--acceptance", type=float, help="share of attempts you accept, above 0 up to 1")
    ap.add_argument("--review-cost", type=float, default=0.0, help="USD of human time per attempt")
    ap.add_argument("--json", action="store_true", help="print machine-readable output")
    return ap


def main(argv=None):
    ap = build_parser()
    a = ap.parse_args(argv)
    if a.demo:
        run_demo()
        return 0
    needed = {"--input-tokens": a.input_tokens, "--output-tokens": a.output_tokens,
              "--input-price": a.input_price, "--output-price": a.output_price,
              "--acceptance": a.acceptance}
    missing = [k for k, v in needed.items() if v is None]
    if missing:
        ap.error("missing: " + ", ".join(missing) + " (or use --demo)")
    try:
        m = attempt_cost(a.input_tokens, a.output_tokens, a.input_price, a.output_price,
                         a.cached_tokens, a.cached_price)
        total = cost_per_accepted(m, a.review_cost, a.acceptance)
    except ValueError as e:
        ap.error(str(e))
    result = {
        "model_cost_per_attempt_usd": round(m, 6),
        "expected_attempts": round(1 / a.acceptance, 4),
        "cost_per_accepted_output_usd": round(total, 4),
    }
    if a.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Model cost per attempt:     ${m:.4f}")
        print(f"Expected attempts:          {1 / a.acceptance:.2f}")
        print(f"Cost per accepted output:   ${total:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
