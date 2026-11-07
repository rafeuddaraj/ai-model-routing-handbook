# 07. Handoff Packet

Use it when you switch models, start a fresh session, or pass work from planner to executor to reviewer. The receiving model starts with no memory of your earlier conversation, so everything it needs must be in the packet.

## Template

```
# Handoff: <task name>

## Goal
<one or two sentences, what done looks like>

## Decisions already made (with reasons)
- <decision>: <why>, <what was rejected>

## Constraints
- <stack, no new dependencies, deadlines, data rules>

## Current state
- <what works, what is half done, what is broken>

## Files touched
- <path>: <what changed>

## Tests and runs
- Command: <command>
- Result: <pass or fail, key lines of output>

## Open questions
- <question>, <who can answer it>

## Next step
<the single next action>

## Do not
- <things the previous session tried that failed, so they are not repeated>
```

## Tips

- Write it in plain, short sentences. The packet is context, so every line should earn its tokens.
- Include failed attempts. They save the next model from repeating them.
- Link to files by path instead of pasting everything. Let the new session read only what it needs.
- Keep the stable rules in `AGENTS.md`. The packet holds only what is specific to this task right now.
