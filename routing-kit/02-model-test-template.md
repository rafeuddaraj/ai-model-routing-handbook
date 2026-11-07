# 02. Five-Minute Model Test (and how to grow it to 20 tasks)

Benchmarks tell you which models are worth testing. Your own tasks tell you which one to use. This test takes about five minutes per model for the starter version.

## Starter version: three tasks

Pick three real tasks from your own backlog:

1. Easy: well-defined, low risk (for example, add a unit test for an existing function).
2. Medium: needs reading several files (for example, add a field end to end).
3. Hard: ambiguous or high risk (for example, design a data migration plan).

For each task, write the prompt once and reuse it unchanged for every model. Put the prompt in `prompts/` or in your notes so the test is repeatable.

## Fairness rules

- Same prompt, same repo state (use a clean branch or a fresh clone), same harness version.
- Same effort level where the vendors allow it, and note the effort you used.
- Run each model on each task twice. Outputs vary from run to run.
- Decide the pass or fail check before you run: tests pass, the code runs, a checklist is met. Do not judge by how confident the answer sounds.
- Read token usage from the API response or the harness usage display. Do not estimate.
- Review output blind when you can: hide which model wrote it before you grade.

## Record each run

Use `templates/test-scoring-sheet.csv`, or copy this table.

| Date | Task | Difficulty | Harness | Model | Tier | Effort | Pass (objective check) | Rework minutes | Input tokens | Output tokens (incl. thinking) | Cost USD | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Score the five axes (1 to 5)

After the runs, give each model a score from 1 to 5 on each axis, based on what you saw, not on marketing.

| Axis | What a 5 looks like |
|---|---|
| Reasoning depth | Breaks the hard task down correctly, finds edge cases unprompted |
| Speed | Finishes quickly enough that you do not context-switch while waiting |
| Cost efficiency | Lowest cost per accepted output (see `06-cost-per-accepted-output.md`) |
| Context handling | Stays accurate as you add more files and history |
| Instruction following | Follows every rule in AGENTS.md, does not add unrequested changes |

## Growing to 20 tasks

- Keep 6 easy, 8 medium, 6 hard.
- Add 3 tasks that are traps: a spec with a hidden contradiction, a bug that is not where the stack trace points, a request that should be refused or questioned.
- Re-run the whole set whenever a new model ships or you change the instruction file in a major way.

## What not to conclude

Three tasks cannot rank models for everything. They can tell you where a model clearly fails on your work, and they give you real numbers to put in the Routing Card. Treat small differences as noise until you have repeated the test.
