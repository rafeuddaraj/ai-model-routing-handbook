# 09. New Model Checklist (30 minutes)

Run this whenever a model you might use ships, and once a month even if nothing shipped.

## Minutes 0 to 5: facts from official sources only

- [ ] Exact model ID and the date you checked
- [ ] Input and output price, cached input price, any long-context or batch pricing, any introductory price and its end date
- [ ] Context window and maximum output
- [ ] Effort or thinking levels, and whether thinking can be turned off
- [ ] Availability in your harness (Claude Code, Codex, Antigravity) and your plan
- [ ] Anything marked beta, preview, or limited access

Skip third-party summaries for this step. Use them only to find the official page.

## Minutes 5 to 20: run your test set

- [ ] Run the three-task starter test from `02-model-test-template.md` (or your 20-task set if you have it)
- [ ] Record pass or fail, rework minutes, tokens, cost
- [ ] Re-run any task that failed once, to separate noise from a real weakness

## Minutes 20 to 28: update the card

- [ ] Fill or update the tier-to-model table in `01-routing-card.md`
- [ ] Change at most two rows of the card, and only where your test supports it
- [ ] Re-run Cost per Accepted Output for the task types you run most

## Minutes 28 to 30: regression and log

- [ ] Re-test your `AGENTS.md` rules on the new model (does it still follow them?)
- [ ] Add a dated line to `CHANGELOG.md` and a Decision Log entry

## Pinning

Aliases such as `opus` or `sonnet` move to new versions over time. Pin an exact model name in production configs, and change it deliberately after you run this checklist.
