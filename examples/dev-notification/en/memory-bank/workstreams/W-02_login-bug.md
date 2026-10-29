# Login bug

- ID: W-02 / name: login-bug
- Goal: fix users being logged out after changing time zone.
- Key documents: none

## Current state
Fixed and merged. The token expiry was compared in local time; it now uses UTC. A regression test covers a time zone change.

## Next
- Close the workstream (worklog written).

## Open items
- None.

## Decisions
- 2026-10-15: one session is enough. Reason: a single small cause, nothing to run in parallel.
