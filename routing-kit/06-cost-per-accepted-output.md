# 06. Cost per Accepted Output

Token price is not the price of a result. A cheap model that is rejected often can cost more than an expensive one that is accepted first time, because every rejected attempt still costs someone's review time.

## Formula

```
attempt_cost         = input_tokens / 1,000,000 * input_price
                     + output_tokens / 1,000,000 * output_price
cost_per_accepted    = (attempt_cost + review_cost) / acceptance_rate
```

- Thinking tokens are usually billed as output tokens. Count them in output.
- `review_cost` is the money value of the human time spent reading one attempt, accepted or not.
- `acceptance_rate` is the share of attempts you accept (0 to 1). Measure it with your test set and Decision Log.

## Worked example (all numbers are assumptions)

Per attempt: 80,000 input tokens and 15,000 output tokens in total across the agent loop, review cost $10, caching ignored. List prices as of 2026-11-07.

| Tier (example model) | Model cost per attempt | Hard task: assumed acceptance | Hard task: cost per accepted | Easy task: assumed acceptance | Easy task: cost per accepted |
|---|---|---|---|---|---|
| Fast (Haiku 5.5) | $0.0155 | 30% | $33.38 | 90% | $11.13 |
| Balanced (Sonnet 5.5) | $0.31 | 60% | $17.18 | 95% | $10.85 |
| Strong (Opus 5.5) | $0.62 | 80% | $13.27 | 95% | $11.18 |

What to take from it: when review time dominates, a low acceptance rate is the real cost. On easy tasks the tiers are nearly equal, so choose on speed. The acceptance rates are invented to show the mechanism. Replace them with yours.

## Run it yourself

```
python3 scripts/cost_calculator.py --demo

python3 scripts/cost_calculator.py \
  --input-tokens 80000 --output-tokens 15000 \
  --input-price 2 --output-price 10 \
  --acceptance 0.6 --review-cost 10

# with cached input and machine-readable output
python3 scripts/cost_calculator.py \
  --input-tokens 80000 --cached-tokens 50000 --cached-price 0.2 \
  --output-tokens 15000 --input-price 2 --output-price 10 \
  --acceptance 0.6 --review-cost 10 --json
```

## Things this simple model leaves out

- Caching: cached input is cheaper on most vendors. Add it if your agent re-reads the same context.
- Long-context surcharges: some price pages charge more above a token threshold per request. Read the current pricing page for your model.
- Batch or flex pricing: cheaper for work that can wait.
- Price changes: for example, Gemini 4 Argon was reported to carry an introductory price that changes on 2026-12-01. Re-check before you plan a budget.
