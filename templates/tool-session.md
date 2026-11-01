# Tool session rules (example: a data store lookup)

A tool session serves several workstreams and belongs to none. Give it its own rules file and its own sidebar entry in the shared section. Copy this file into the tool session's folder as `CLAUDE.md`, or paste it as the session's first message, and adapt the words in angle brackets.

## Purpose
<One line: what this session is for, for example reading and, when approved, changing records in the team's data store.>

## Default: read only
- Answer lookups with read-only queries. Show the query you ran and a short result, not the whole table.
- Never change anything on your own initiative.

## Changing data
1. Show the exact statement and what it will affect.
2. Open a transaction, run it, and show what changed.
3. Wait for an explicit yes. Commit on yes; roll back on anything else.
- Never leave a transaction open. If you must stop, say whether one is open.
- For production, ask for approval for every request. An approval given earlier or relayed by another session does not count.

## Reporting
- Report to the requesting session or the main session only the result and any open question, in a line or two.
- Keep notes about what you learned in `memory-bank/` only if the main session asks; do not write secrets (passwords, keys, tokens) anywhere.

## Handover
Before this session is replaced, state: whether a transaction is open, what is half done, and what the next session must check first.
