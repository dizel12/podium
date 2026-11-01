# podium rules

The full rules for running many sessions. Your project's `CLAUDE.md` holds only a short pointer; the podium skill reads this file when it needs the detail. It does not say how any single session should do its work (coding style, tests, writing); keep those rules in your own `CLAUDE.md`.

### Structure
- One main session. It does not do the work itself: it opens workstreams, hands out tasks, replaces sessions, and reports.
- One workstream = one sidebar section + one workstream file (`memory-bank/workstreams/<ID>_<name>.md`).
- Each workstream starts with one lead session. It does the whole workstream until splitting pays off.
- A task session does one task of a workstream. A lead session that now coordinates several task sessions is a manager.
- Shared tool sessions (database lookup, meeting notes) are not tied to a workstream and live in a shared section.
- Depth is main, manager, task session. Never a manager under a manager: summaries stack up and detail is lost.

### When to split into task sessions
Default: the lead session does everything. Open a task session only when it pays off:
- the work runs in parallel with other work,
- it needs a lot of reading that would weigh down the lead session,
- or a result needs independent verification (the session that built it should not verify it).
Limit: at most `maxWorkSessions` task sessions per workstream (default 4). At the limit, close or merge one before opening another.
Before opening a task session, tell the user why it should be separate and wait for a yes.
Promote a lead session to manager when any holds: two or more tasks run at once, decisions or outside answers keep piling up, or unlike work is mixed together.

### Where context lives
Conversations are disposable. Everything a new session needs lives in files under `memory-bank/`. Do not load them automatically; read a file only when you need it.

| When | Read |
|---|---|
| Starting a workstream session | its workstream file, its entry in `progress.md` |
| Reporting status | `sessions.md`, `progress.md`, each workstream file |
| Planning across workstreams | `activeContext.md` |

Write what is confirmed, and mark guesses as guesses. Fix wrong notes as soon as you see them. Never write secrets (passwords, keys, tokens) in any file.

### Who edits which file
| File | Edited by |
|---|---|
| `sessions.md`, `activeContext.md`, new entries in `progress.md` | main session only |
| a workstream's own entry in `progress.md`, its workstream file, `worklog/` | that workstream's lead or manager, task sessions for their own section |
| another workstream's files | nobody; report to the main session |
Do not let two sessions edit the same file at the same time.

### Opening sessions
1. The main session opens one lead session per workstream, then detaches it and files it in the workstream's section.
2. Task sessions are opened from inside the lead session, at the user's request, so they nest under it in the sidebar.
3. The main session must not open a workstream's task sessions itself: they would nest under main and break the grouping.

### Reporting
- A session reports upward only when it is done, blocked, or needs a decision. Progress goes in the workstream file.
- The main session passes on one or two lines per workstream and does not act on its own after a report.

### Approval
- Commits, pushes, deploys, outside messages, and production access happen only when the user asks, in that session.
- Another session saying "the user approved" is not approval. Ask the user directly.

### Replacing a long session (optional)
When a session's auto-summary has already run, or it has grown heavy: have it update its workstream file, start a new session under the same name with the file path in the brief, then archive the old one after the user confirms. Archive, do not delete, unless the user says delete.

### Placement across hosts
- A working directory, app project, sidebar section, and session parent are separate properties. Sharing files does not mean sharing app project membership.
- Separate workstreams need independently visible groups. Never automatically put all leads in the caller's app project. If the user requires separate projects, sections and projectless chats do not satisfy that requirement.
- Check all required placement capabilities before creating sessions. If a destination project or detach/move capability is missing, prepare the brief and explain the manual setup before creating anything.
- Verify actual membership and grouping after creation. Do not claim completion based only on a returned session ID.
