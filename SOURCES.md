# Sources and verification status

Read this before you quote a number from the handbook.

**How these were checked.** On 2026-11-07 the author searched the web and read excerpts of each page listed below. The pages were not each opened in full, and no model was benchmarked by the author. "Vendor" means the company that makes the product. "Secondary" means a third party reporting vendor information. Before you rely on any price, model ID, or flag, confirm it on the vendor's official page.

## Prices, context windows, model names

| Claim | Where it came from | Type | Status |
|---|---|---|---|
| Claude Haiku 5.5 is $0.10 / $0.50 per 1M tokens, 1M context, 128K max output | platform.claude.com/docs/en/models/haiku-5-5/overview | Vendor docs | Read from excerpt |
| Claude Sonnet 5.5 is $2 / $10, 1M context | platform.claude.com/docs/en/models/sonnet-5-5/overview | Vendor docs | Read from excerpt |
| Claude Opus 5.5 is $4 / $20 and Fable 5.1 is $10 / $50 | Comparison table on the Haiku 5.5 overview page above | Vendor docs | Read from excerpt |
| GPT-6 Astra $10 / $50, GPT-6.1 Sol and GPT-6 Sol $2 / $10, GPT-6.1 Terra $1 / $5, GPT-6 Luna $0.10 / $0.50, all listing 1,050,000 context | benchlm.ai/blog/posts/gpt-6-models-compared | Secondary (cites OpenAI pricing page) | Not checked against OpenAI directly |
| GPT-6.1 Terra reached ChatGPT Work and Codex on 2026-10-26; GPT-6 Sol and Luna shipped 2026-09-22 | benchlm.ai (above) and yottalabs.ai post on Sol and Luna | Secondary | Not checked against OpenAI directly |
| An earlier source said GPT-6 had no Terra tier, then Terra shipped | emergent.sh explainer vs benchlm.ai | Secondary, conflicting over time | Used as an example of naming churn |
| Gemini 4 Argon: ID `gemini-4-argon`, $2 / $10 introductory, $4 / $20 from 2026-12-01, 1,048,576 context, thinking levels low, medium, high | computingforgeeks.com/gemini-4-argon-released-features-benchmarks/ | Secondary (independent review of Google's pricing page and API) | Not checked against Google directly |
| Argon at `high` spent about three thinking tokens per visible token in one reviewer test | Same review | Secondary, one test | Single observation, not a general rule |
| Vals Index scores in Google's model card: Argon 68.9%, Opus 5.5 67.0%, Fable 5.1 65.8%, Astra 63.1%, with Google comparing only three other models and Argon run at its highest thinking setting | Same review | Secondary, vendor-reported numbers | Vendor claim |
| Haiku 5.5 price multiplier above 100K tokens per request | implicator.ai | Secondary | Not verified. Check Anthropic's pricing page |

## Tool behavior

| Claim | Where it came from | Type | Status |
|---|---|---|---|
| Claude Code aliases, `opusplan` (Opus in plan mode, Sonnet for execution), `/effort`, plan mode | code.claude.com/docs/en/model-config | Vendor docs | Read from excerpt. Docs also say aliases move to newer versions over time |
| `/advisor` pairs a faster main model with a stronger advisor, typically cheaper than running the stronger model throughout | code.claude.com/docs/en/advisor | Vendor docs | Read from excerpt |
| Fable 5.1 advisor added 1.7 points to Opus 5.5 at 2.1 times the cost, in Anthropic-internal tests | developersdigest.tech summary | Secondary, summarizing vendor-internal results | Cannot be reproduced by outsiders |
| Codex `config.toml`, `model_reasoning_effort`, `[profiles.<name>]`, `codex --profile`, `plan_mode_reasoning_effort`, `project_doc_max_bytes` default 32768 | developers.openai.com/codex/local-config and /codex/config-sample | Vendor docs | Read from excerpt. A third-party post suggests profile storage changed in newer versions |
| Antigravity Agent Manager, model dropdown, Planning vs Fast mode, plan artifacts with comments | blog.openreplay.com/google-antigravity-ide-guide/ and related guides | Secondary, written around the product's first release | May be outdated. Check antigravity.google |
| `AGENTS.md` is read by Codex and many other agents; Claude Code reads `CLAUDE.md`; import with `@AGENTS.md`; Gemini and Antigravity read `GEMINI.md` with an import | docs.crewai.com guide and other third-party explainers | Secondary | Sources disagree on whether Claude Code now reads `AGENTS.md` natively. The import line is safe either way |

## Research papers

| Claim | Paper | Status |
|---|---|---|
| LLM evaluators favor their own outputs, and the bias correlates with self-recognition | Panickssery, Bowman, Feng. NeurIPS 2024. arXiv:2404.13076 | Tested GPT-4, GPT-3.5, Llama 2. Newer models not covered |
| Tokenization length for the same text differs by up to 15 times across languages | Petrov, La Malfa, Torr, Bibi. NeurIPS 2023. arXiv:2305.15425 | 2023 tokenizers. Current ratios must be measured (see `routing-kit/08-token-tax-experiment.md`) |
| Model performance becomes less reliable as input length grows | Hong, Troynikov, Huber. Chroma technical report, July 2025. research.trychroma.com/context-rot | 18 models of that time. Newer models may behave differently |

## Illustrative content (not evidence)

- The cost example in `routing-kit/06-cost-per-accepted-output.md` and `scripts/cost_calculator.py --demo` use assumed acceptance rates and an assumed review cost.
- `templates/decision-log.example.csv` contains illustrative rows, not real results.
- The diagrams in `docs/diagrams/` are illustrations of the method, not measurements.
- The Kubernetes anecdote is one reviewer's small test of 12 generated manifests, not a verdict on any model.
