# Contributing

Models, prices, and flags change often, so the most useful contribution is a correction: a wrong or outdated price, model name, flag, or claim.

Open an issue with the Correction form, or a pull request. Include a link to the official page and the date you checked it. If you add or change a number, add its source to `SOURCES.md` and a dated line to `CHANGELOG.md`.

Two rules:

- Do not add benchmark scores you did not run or cannot link to.
- Say whether a number is measured, quoted from a source, or assumed.

Before you open a pull request:

```
python3 -m unittest discover -s tests
python3 scripts/validate_repo.py
```
