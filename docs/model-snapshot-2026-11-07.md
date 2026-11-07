# Model snapshot, 2026-11-07

A dated snapshot of the models this handbook uses as examples. It will go stale. When you update it, copy this file to a new date, and add a line to `CHANGELOG.md`. Confirm every row on the vendor's official page before you rely on it. How each row was checked is in `SOURCES.md`.

## Prices and context (USD per 1 million tokens)

| Model | Input | Output | Context window | Source type |
|---|---|---|---|---|
| Claude Haiku 5.5 | $0.10 | $0.50 | 1M | Vendor docs |
| Claude Sonnet 5.5 | $2 | $10 | 1M | Vendor docs |
| Claude Opus 5.5 | $4 | $20 | 1M | Vendor docs |
| Claude Fable 5.1 | $10 | $50 | 1M | Vendor docs |
| GPT-6 Luna | $0.10 | $0.50 | 1.05M | Secondary |
| GPT-6.1 Terra | $1 | $5 | 1.05M | Secondary |
| GPT-6.1 Sol | $2 | $10 | 1.05M | Secondary |
| GPT-6 Astra | $10 | $50 | 1.05M | Secondary |
| Gemini 4 Argon | $2 (introductory) | $10 (introductory) | 1,048,576 | Secondary |

Watch for:

- Gemini 4 Argon: the $2 / $10 price was reported as introductory, with $4 / $20 from 2026-12-01.
- Thinking tokens are usually billed as output, so the effort level can change the bill more than the tier does.
- Some pricing pages add surcharges above a per-request token threshold, and discounts for cached input or batch work. Read the current page.

## Suggested tier mapping (a starting point, verify with your own tests)

| Tier | Claude | OpenAI | Google |
|---|---|---|---|
| Strong | Opus 5.5, Fable 5.1 | GPT-6 Astra | Gemini 4 Argon, thinking `high` |
| Balanced | Sonnet 5.5 | GPT-6.1 Sol (or Terra for lighter work) | Gemini 4 Argon, thinking `medium` |
| Fast | Haiku 5.5 | GPT-6 Luna | Argon with `low`, or a smaller Gemini model |

## What changed the tiers' meaning

Flagship context windows are now all around 1 million tokens, so context size no longer separates the tiers. Price, reasoning depth, effort controls, speed, and behavior do.

## Tool controls, as documented on this date

- Claude Code: aliases (`opus`, `sonnet`, `haiku`), `opusplan`, `/effort`, `/advisor`, plan mode.
- Codex: `config.toml`, `model_reasoning_effort`, `plan_mode_reasoning_effort`, named profiles with `codex --profile`.
- Antigravity: model dropdown in Agent Manager, Planning and Fast modes, plan artifacts with comments.

Flags and layouts change between versions. Check the official docs for your version.
