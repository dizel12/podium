# Session ledger

Which session owns which workstream. The app's live session state is the source of truth; this file records who was given what.
Only the main session edits this file.

## Main session
- Name / ID: <main session>

## Sidebar sections
- Shared tools: <main>, <tool sessions such as database lookup or meeting notes>
- <Workstream section name>: <lead session>, <work sessions>

## Active
| Workstream | Session name | Session ID | Role | Started | Notes |
|---|---|---|---|---|---|
| W-01 | <name> | <id> | lead | YYYY-MM-DD | |

## Closed or replaced
| Workstream | Session name | Session ID | Period | Reason (archived or replaced, and where the result lives) |
|---|---|---|---|---|
