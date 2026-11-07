# 04. Phase Prompt Templates

Every template has the same six parts: Phase, Goal, Context, Constraints, Output, Done when. A fixed shape makes prompts comparable across models, which is what you need for fair tests.

Replace everything in angle brackets. Keep the "Done when" line concrete and checkable.

## Brainstorm (Strong tier)

```
Phase: Brainstorm
Goal: Explore approaches for <problem>.
Context: <users, constraints, existing system, what has been tried>.
Constraints: <time, budget, stack, things we will not change>.
Output: 4 distinct approaches. For each: how it works, who it suits, main risk, cheapest way to test it. Then ask me up to 5 questions that would change your ranking.
Done when: the approaches differ in kind, not in wording, and every risk is specific.
```

## PRD and requirements (Balanced tier, ask first)

```
Phase: PRD
Goal: Turn <idea> into requirements we can build and test.
Context: <background, users, links to notes>.
Constraints: <scope limits, non-goals>.
Output: First, list every question you need answered before writing. Do not write the PRD yet. After I answer, produce: problem, users, scope, non-goals, acceptance criteria as testable statements, open risks.
Done when: each acceptance criterion can be turned into a test without further questions.
```

## Architecture and ADR (Strong tier, human gate)

```
Phase: Architecture review
Goal: Decide <decision>.
Context: AGENTS.md attached. <current architecture, scale, team size>.
Constraints: <no new infrastructure, budget, compliance>.
Output: 3 options with trade-offs, one recommendation, and open questions. Then write an ADR: context, decision, consequences, alternatives rejected.
Done when: every option names its main failure mode and how we would detect it.
```

## Spec and task breakdown (Balanced tier)

```
Phase: Spec
Goal: Break <feature> into tasks an agent can implement independently.
Context: PRD and ADR attached.
Constraints: each task touches at most <n> files and can be verified alone.
Output: ordered task list. For each task: scope, files likely touched, acceptance criteria, the command that proves it works.
Done when: no task depends on an unstated assumption, and each has a runnable check.
```

## Implement (Balanced tier, Fast for boilerplate)

```
Phase: Implement
Goal: Implement task <id> from the spec.
Context: AGENTS.md, spec section <x>, relevant files <paths>.
Constraints: change only what the task needs. Do not refactor unrelated code. Do not add dependencies without asking.
Output: the change, plus the exact commands you ran and their output.
Done when: the task's acceptance criteria pass, tests pass, and you have shown the output of running the code.
```

## Code review (Strong tier, different model or fresh context)

```
Phase: Review
Goal: Review this diff against the spec. You did not write it.
Context: spec <link or text>, diff <paste>, test output <paste>.
Constraints: report only real problems. Separate must-fix from nice-to-have.
Output: findings with file and line, why it matters, and a suggested fix. Then list anything in the spec the diff does not cover.
Done when: every acceptance criterion is marked covered, not covered, or unclear.
```

## Security review (Strong tier, human gate)

```
Phase: Security review
Goal: Find security problems in this change.
Context: diff, threat model notes, data classification.
Constraints: assume an attacker controls all external input. Do not suggest fixes that need new infrastructure.
Output: findings ranked by severity, each with an exploit scenario and a fix. List what you could not assess.
Done when: authentication, authorization, input handling, secrets, and logging have each been addressed or marked not applicable.
```

## Debug (Fast for triage, then escalate)

```
Phase: Debug
Goal: Find the cause of <symptom>.
Context: logs <paste>, recent changes <list>, how to reproduce <steps>.
Constraints: do not change code yet.
Output: 3 ranked hypotheses, the evidence for and against each, and one cheap experiment per hypothesis.
Done when: I can run the experiments without further explanation.
```

## Docs and changelog (Fast tier)

```
Phase: Docs
Goal: Update docs for <change>.
Context: diff, existing docs <paste>.
Constraints: do not invent behavior. If something is unclear, list it as a question.
Output: updated text and a changelog entry in the existing format.
Done when: every statement in the docs is traceable to the diff or to a question you listed.
```
