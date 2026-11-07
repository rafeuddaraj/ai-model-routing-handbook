# 10. Verification Gates

"Looks correct" is not evidence. Models write plausible text, so you need checks the model cannot talk its way past.

## The ladder (cheapest first)

| Gate | What it proves | What it does not prove |
|---|---|---|
| Linter or type check | Syntax and some types are valid | The code works |
| Unit tests | Specific behaviors you wrote tests for | Behaviors nobody tested |
| Run it for real | It starts, accepts input, produces output | It is correct in every case |
| Integration or end-to-end check | The parts work together | Security, load, and unusual input |
| Independent review (different model or person) | A second pair of eyes found nothing blocking | There are no defects |
| Human gate | A person accepts the risk | Nothing about correctness by itself |

Pass the gates in order. Do not skip to the end because an earlier gate was green.

## Definition of done (copy into every spec)

1. Acceptance criteria are met, each mapped to a test or a manual check.
2. The author shows the command and the real output of the tests.
3. The author ran the changed code for real and shows what happened.
4. A reviewer who did not write the code checked the diff against the spec.
5. Anything not verified is listed.

## Evidence format for pull requests

```
Command: <exact command>
Result: <pass or fail>
Output (key lines): <paste>
Run for real: <what you did, what you saw>
Not verified: <list>
```

## Traps

- A manifest, config, or query that passes a linter but fails when deployed.
- A test that was changed to match the bug.
- A function or flag that does not exist (the model invented it).
- "Done" reported without a command or output.
- Reviewing with the model that wrote the code, in the same context.

## When a gate fails

Log it in the Decision Log, improve the context, and apply the Escalation Rules (`03-escalation-rules.md`). Do not argue with the model. Change the input or the tier.
