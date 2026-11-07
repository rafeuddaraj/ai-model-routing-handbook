# 01. Model Routing Card

A Routing Card answers one question per task type: which tier first, what is the fallback, when do we climb, and who decides. Copy it per team or per project, fill it from your own tests (see `02-model-test-template.md`), and keep it in the repo.

Use tiers in the card, not model names. Map tiers to real models in one place (the table below), so a new model changes one row instead of the whole card.

## Step 1. Map tiers to the models you use this month

| Tier | Meaning | Claude | OpenAI | Google | Your pick |
|---|---|---|---|---|---|
| Strong | Hard reasoning, high cost of error | Opus 5.5, Fable 5.1 | GPT-6 Astra | Gemini 4 Argon, thinking `high` | |
| Balanced | Daily workhorse | Sonnet 5.5 | GPT-6.1 Sol | Gemini 4 Argon, thinking `medium` | |
| Fast | Cheap, quick, well-defined work | Haiku 5.5 | GPT-6 Luna | (fill in) | |

Names and prices are a 2026-11-07 snapshot (see `../docs/model-snapshot-2026-11-07.md`).

## Step 2. Fill the card

| Task type | First choice (tier, effort) | Fallback | Escalate when | Human gate | Data rule |
|---|---|---|---|---|---|
| Brainstorm | | | | | |
| PRD and requirements | | | | | |
| Architecture and ADR | | | | | |
| Spec and task breakdown | | | | | |
| Implement | | | | | |
| Code review | | | | | |
| Security review | | | | | |
| Debug | | | | | |
| Docs and changelog | | | | | |

## Example (not a recommendation for your team)

| Task type | First choice | Fallback | Escalate when | Human gate | Data rule |
|---|---|---|---|---|---|
| Brainstorm | Strong, high effort | Balanced | Answers stay generic after 2 rounds | Scope | No secrets |
| Spec and tasks | Balanced | Strong | Acceptance criteria are vague | None | No secrets |
| Implement | Balanced, Fast for boilerplate | Strong | 2 failed attempts | None | No customer data |
| Review | Strong, a different model | Strong, fresh context | Security-sensitive diff | Merge | No secrets |
| Debug | Fast for log triage | Balanced, then Strong | Root cause not found in 2 tries | None | No production data |
| Docs | Fast | Balanced | Facts are uncertain | None | No secrets |

## Rules for keeping the card honest

1. Every row must trace back to a test or a Decision Log entry, or be marked "assumption".
2. Review the card monthly and whenever a new model ships (`09-new-model-checklist.md`).
3. The Data rule column is policy, not preference. Ask your security lead before you fill it.
4. A spreadsheet version lives in `templates/routing-card.csv`.
