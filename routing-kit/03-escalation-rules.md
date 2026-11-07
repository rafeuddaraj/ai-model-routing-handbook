# 03. Escalation Rules

Defaults to copy into `AGENTS.md` or your team handbook. The numbers are starting points. Tune them with your Decision Log (`05-decision-log.md`).

## Climb rules

1. Two failed attempts on the same task at the same tier: stop re-prompting. Improve the context first (add the failing test output, the relevant file, the constraint you forgot), then move up one tier.
2. The model invents something that does not exist in the codebase (a function, a config key, a flag): escalate immediately and add a correction to the context. Do not wait for a second failure.
3. The model breaks a written rule from AGENTS.md twice: tighten the rule so it can be checked, then retry once. If it still breaks it, move up one tier.
4. The task touches authentication, payments, data deletion, or permissions: start at Strong, and require a human gate before merge.
5. The model says "done" without showing the command it ran and its output: reject the result and ask for the evidence.
6. Context grows past what you can summarize in one handoff packet (`07-handoff-packet.md`): start a fresh session with the packet. Do not keep stacking turns.
7. Climbing twice in one task: stop and ask whether the spec is the real problem. A stronger model cannot fix an ambiguous requirement.

## Descend rules

8. A higher tier passed three similar tasks in a row on the first attempt: test one tier down on the next similar task, and record the result.
9. A task type runs often (dozens of times a day): measure Cost per Accepted Output at two tiers before you pick one (`06-cost-per-accepted-output.md`).

## Human takeover rules

10. You are already at the Strong tier and the second attempt failed: a person takes over, or rewrites the spec and starts again. Log what the model could not do.

## Do not do this

- Do not escalate silently. Every climb gets a one-line Decision Log entry.
- Do not use "try again, but think harder" as a strategy. Change the context, the tier, or the effort, and write down which one you changed.
