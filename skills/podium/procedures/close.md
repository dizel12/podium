# close: finish a workstream

Goal: make sure the result is in files, then retire the sessions. Do not trust a "done" report until the files show it.

## Steps
1. Ask the lead (or manager) session to finalize: write `worklog/<date>_<topic>.md`, set its `progress.md` entry to done with the finish date, and bring its workstream file up to date. Tell it not to start new work, and to report in one line when finished. With a manager, tell it to leave any sub-session you want to keep alone.
2. When it reports, read the files yourself: the worklog exists, the `progress.md` entry says done, the workstream file's "Current state" matches the outcome. If something is missing, say what and ask the session to fix it.
3. Check that nothing is left open: unmerged branches, open pull requests, an unfinished database transaction, pending approvals. List them for the user; do not act on them.
4. Show the user the sessions to retire (lead, task sessions) and ask. Default is **archive**, which can be undone. Delete only if the user says delete. Sessions open on screen or pinned cannot be removed; ask the user to close them.
5. After the user confirms: archive, then move the ledger rows from "Active" to "Closed or replaced" with the period and where the result lives. Remove the workstream's section if it is empty.
6. Re-list sessions afterwards. A sub-session you meant to keep may have been archived with its parent; if so, tell the user and offer to restore it.

## Report
Two lines: what was closed, and where the result lives (files, branch, link).
