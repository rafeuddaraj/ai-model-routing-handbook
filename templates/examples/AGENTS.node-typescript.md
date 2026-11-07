# AGENTS.md (example: Node.js and TypeScript service)

A filled-in example for a fictional project, to show the level of detail that works. See `../AGENTS.md` for the full template.

## Project

REST API for team invitations and memberships, used by the web app.

- Language and runtime: TypeScript 5, Node.js 22
- Frameworks and services: Fastify, PostgreSQL 16 via Prisma, Redis for rate limits
- Package manager: pnpm 9

## Setup and commands

| Purpose | Command |
|---|---|
| Install | `pnpm install` |
| Dev server | `pnpm dev` |
| One test file | `pnpm vitest run src/invitations/create.test.ts` |
| All tests (before every commit) | `pnpm test` |
| Lint and format | `pnpm lint` |
| Type check | `pnpm typecheck` |
| Database migrate (dev) | `pnpm prisma migrate dev` |

## Repository map

- `src/`: application code, one folder per feature
- `src/**/*.test.ts`: tests next to the code
- `prisma/`: schema and migrations (ask before changing)
- `docs/adr/`: architecture decisions

## Code style

- Named exports only. No default exports.
- Validate every request body and query with the zod schema in the route file. Never parse by hand.
- Use the shared `AppError` class for expected failures. Do not throw bare strings.
- Money is integer cents. Dates are UTC `Date` or ISO strings, never local time.

## Boundaries

Always: run `pnpm test` and show the output; keep changes to the task.
Ask first: new dependencies, Prisma schema changes, anything in `.github/` or `infra/`.
Never: commit `.env` files; edit `pnpm-lock.yaml` by hand; edit generated Prisma client files.

## Definition of done

Tests pass with output pasted; you started the dev server and called the changed endpoint once with `curl`, and reported the status code and body; anything unverified is listed.
