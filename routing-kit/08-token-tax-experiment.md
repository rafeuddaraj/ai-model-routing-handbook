# 08. Token Tax Experiment (Bangla, or any language)

The same content costs a different number of tokens in different languages. A NeurIPS 2023 paper (Petrov et al., arXiv:2305.15425) reported differences of up to 15 times between languages for the same translated text, using tokenizers available at the time. It does not tell you the ratio for the current Claude, GPT-6 or Gemini 4 tokenizers. This experiment measures it for your model and your content.

## Steps

1. Pick 5 passages of about 150 words each from your real work: a spec paragraph, an error explanation, a user story, a code comment, a customer message.
2. Write each passage in English and in your language, with the same meaning. Translate carefully. Do not shorten one version.
3. Send each version to the model you use, with a trivial instruction such as "Reply with the single word OK."
4. Read the input token count from the API response `usage` field (or the harness usage display). Use the same model and the same instruction every time, so the instruction cancels out.
5. Record the numbers.

## Record

| Passage | English input tokens | Your language input tokens | Ratio (yours / English) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| Average | | | |

## Compute the ratio

Copy `templates/token-tax.csv`, fill in the two token columns, then run:

```
python3 scripts/token_ratio.py my-token-tax.csv
python3 scripts/token_ratio.py my-token-tax.csv --markdown
```

## What to do with the ratio

- A ratio near 1 means the language barely changes cost on this model. Write in whichever language your team reads best.
- A large ratio means long instruction files, specs and system prompts cost more and fill the context window faster. Consider keeping agent-facing instructions in English and user-facing text in your language.
- Cost is not quality. Run your hardest task in both languages and compare the results before you decide. This experiment does not measure quality.
- Repeat when you change models. Tokenizers change between model families and generations.
