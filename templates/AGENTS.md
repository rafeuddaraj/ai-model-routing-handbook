# AGENTS.md

Instructions for AI coding agents working in this repository. Humans should start with `README.md`.

Keep this file short, specific, and checkable. When an agent repeats the same mistake, add one precise rule here. When a rule is never used, delete it.

## Project

<One or two sentences: what this project does and who uses it.>

- Language and runtime: <for example, TypeScript 5 on Node.js 22>
- Main frameworks and services: <for example, Next.js, PostgreSQL 16, Redis>
- Package manager: <for example, pnpm 9>

## Setup and commands

Run these exactly as written. Prefer the narrowest command that proves your change (one test file, one package) before running the full suite.

| Purpose | Command |
|---|---|
| Install dependencies | `<pnpm install>` |
| Run the app locally | `<pnpm dev>` |
| Run one test file | `<pnpm test path/to/file.test.ts>` |
| Run all tests (before every commit) | `<pnpm test>` |
| Lint and format | `<pnpm lint>` |
| Type check | `<pnpm typecheck>` |
| Build | `<pnpm build>` |

## Repository map

- `<src/>`: application code
- `<tests/>`: tests, mirroring `src/`
- `<docs/>`: documentation and ADRs (`docs/adr/`)
- `<scripts/>`: tooling. Do not change without asking.

## Code style

- Follow the existing style in the file you edit. Match naming, error handling, and import order.
- <Specific rule, for example: use named exports, no default exports.>
- <Specific rule, for example: validate all external input with the schema library, never by hand.>
- Prefer small, focused functions. Add a doc comment to every new public function.

Example of the expected style:

```
<paste 5 to 10 lines of real code from this repo that show the preferred pattern>
```

## Testing

- Every behavior change needs a test that fails without the change.
- Test names say what is expected: `returns 404 when the invitation has expired`.
- Do not skip, delete, or loosen a test to make it pass. If a test is wrong, say so and explain.
- Do not mock what you can run for real in under a second.

## Git and pull requests

- One task per branch and per pull request. Keep diffs small.
- Commit message format: `<type>(<scope>): <summary>` (for example, `fix(auth): reject expired invitations`).
- Pull request description: what changed, why, how you verified it, and anything you could not verify.
- Never force-push to a shared branch.

## Boundaries

Always:
- Run the test command and show its real output before you say a task is done.
- Keep changes limited to what the task asks for.
- Follow the acceptance criteria in the task or spec.

Ask first:
- Adding, removing, or upgrading a dependency.
- Changing the database schema, a public API, CI configuration, or infrastructure.
- Changing anything under `<generated, vendored, or legacy paths>`.

Never:
- Commit secrets, tokens, private keys, or customer data.
- Invent a function, flag, endpoint, or config key. If you cannot find it in the repository or its documentation, say so.
- Edit lockfiles by hand, or edit generated files.
- Disable security checks, linters, or tests to get a green result.

## Security and data

- Treat all external input as untrusted.
- Do not log secrets or personal data.
- Do not send code or data outside this machine unless the task explicitly requires it and the data rules in `<link to your policy>` allow it.

## Definition of done

A task is done only when all of these are true:

1. The acceptance criteria are met.
2. Tests pass, and you have pasted the command and the relevant output.
3. You ran the changed code at least once for real (started the service, ran the command, called the endpoint) and reported what happened.
4. Anything you could not verify is listed explicitly.

"Looks correct" and "the linter passes" are not evidence by themselves.

## When to stop and ask

Stop and report instead of guessing when:

- The spec is ambiguous, or it contradicts the code.
- The same approach has failed twice. Describe what you tried and what you saw.
- The task touches authentication, payments, permissions, or data deletion.
- You would need more than <N> files changed to finish a task described as small.

## Handoff note

When you finish or stop, write a short note: goal, decisions and reasons, files touched, commands run and results, open questions, next step. The format is in `<docs/handoff-packet.md>` (see `routing-kit/07-handoff-packet.md` in the handbook).

## Nested instructions

In a monorepo, a more specific `AGENTS.md` inside a package refines this file for that package. Many tools apply the closest file first. Confirm how your tools resolve nested files before you rely on it.
