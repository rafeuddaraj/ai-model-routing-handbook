# 05. Decision Log

A short entry after each meaningful model decision. After a month, this log is the evidence for your Routing Card.

## Template

```
Date:
Task:
Phase: (brainstorm, prd, architecture, spec, implement, review, debug, docs)
Harness and model: (include effort or thinking level)
Why this choice: (matrix quadrant, routing card row, or "experiment")
Result: accepted | accepted with rework | rejected
Rework minutes:
Escalated? yes/no, and why:
Cost (if known):
What I will do differently next time:
```

## Example (illustrative)

```
Date: 2026-11-07
Task: Invitation token expiry logic
Phase: implement
Harness and model: Balanced tier, medium effort
Why this choice: Matrix quadrant "clear spec, high cost of error"
Result: accepted with rework
Rework minutes: 20
Escalated? no
Cost (if known): not tracked
What I will do differently next time: have a different model review any time-related logic
```

A CSV version for spreadsheets is in `templates/decision-log.csv`, and `templates/decision-log.example.csv` shows what filled rows look like (illustrative data only).

To summarize a log by phase and tier:

```
python3 scripts/summarize_decision_log.py my-log.csv
python3 scripts/summarize_decision_log.py my-log.csv --markdown
```

The script reads the columns `phase`, `tier`, `result` (`accepted`, `accepted_with_rework`, or `rejected`), `rework_minutes`, and `escalated` (`yes` or `no`).

## How to use it

- Review the log monthly. Count how often each tier was accepted first time, per task type.
- Update the Routing Card rows where the log disagrees with your assumptions.
- Keep failed experiments. They are the most valuable entries.
