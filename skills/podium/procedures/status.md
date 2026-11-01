# status: where things stand

Goal: one or two lines per workstream, from files and live session state, without reading every conversation.

## Steps
1. Read the ledger, `progress.md`, and `activeContext.md`. Read each active workstream file's "Current state", "Next", and "Open items" only.
2. With session tools: list sessions, keep only this project's folder, and compare with the ledger. A ledger row with session ID "(not created)" is pending, not a mismatch. Flag differences: a session in the ledger that is gone or archived, a running session not in the ledger, a pull request or task that finished while the ledger still says in progress.
3. Report per workstream, in this shape, with the labels in the user's language (for example Korean: state, next, needs you):
   `<ID> <name>: <state in one line>. Next: <one line>. Needs you: <decision, or none>.`
   The workstream file's section names follow the template's language (for example "Current state" is "현재 상태" in the Korean template).
4. After the list, add at most three lines: what needs the user's decision first, anything blocked, and mismatches between the ledger and the live state.

## Tidy hint (one line, only when it applies)
After the report, if you have session tools, count in this project's folder: sessions whose workstream is marked done or closed in the files but are not archived, and sessions with no activity for `idleDays` days that are not running, pinned, or tied to an open pull request. If the count is more than zero, add one line: how many, and that the user can say "clean up sessions" to review them. Do not list them, do not archive anything, and do not repeat the hint if the user ignored it earlier in this conversation.

## Rules
- Say which facts you checked in a file and which come only from a report ("as reported"). Do not present a report as verified.
- If `activeContext.md` still holds its placeholders, say it has not been filled in. Do not treat that as a problem to fix.
- Do not edit the ledger or `activeContext.md` unless the user asks. Offer to fix mismatches.
- Do not start follow-up work because a status shows something to do.
