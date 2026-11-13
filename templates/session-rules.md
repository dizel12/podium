<!-- podium:begin -->
## Sessions (podium)

This project runs several workstreams. Each has its own sidebar section, a workstream file, and a lead session. State lives in `memory-bank/` (`progress.md`, the ledger `sessions.md`, `workstreams/`); the conversation is disposable.
A new task, sorting sessions, status, closing work, or replacing a long session: the `podium` skill handles it. Just ask in plain words. The full rules are in the podium plugin's `docs/rules.md`.

### Roles
- Main session: coordinates only. It opens workstreams, hands out tasks, and reports. It does not do the work.
- Lead session: does the whole workstream until splitting pays off, and owns the workstream file. A lead that coordinates several task sessions is a manager.
- Task session: one task. It writes only its own part of the workstream file.
- Depth stops at main, manager, task session.

### Splitting
- The default is one lead session. Open task sessions only for parallel work, heavy reading, or independent verification.
- At most `maxWorkSessions` per workstream (default 4). Tell the user why a task should be separate and wait for a yes.
- Task sessions are opened from inside the lead session so they nest under it. The main session does not open them.

### Files
- Main session only: `sessions.md`, `activeContext.md`, new entries in `progress.md`.
- A workstream's lead or manager: its own workstream file, its entry in `progress.md`, `worklog/`.
- Nobody edits another workstream's files; report to the main session instead. Two sessions never edit one file at once.
- Write what is confirmed and mark guesses as guesses. Never write secrets into files.

### Reporting and approval
- Report upward only when done, blocked, or a decision is needed. Progress goes in the workstream file.
- For a request from another workstream, record the result in your workstream file. Do not reply to the session that asked, and do not report to main unless done with a deliverable, blocked, or a decision is needed. Reply in one line only if the request says "reply needed". Reading another workstream's file is allowed; editing is not.
- Record every task session you open (name, ID, role, state) and where each result lives in the workstream file, not only in a notes folder. A task session never replaces itself; ask the lead.
- When the user describes work that looks like it will span several sessions, offer once to make it a workstream. If they decline, do not ask again for that work.
- When the work looks finished, ask the user whether to close the workstream.
- Commits, deploys, outside messages, and production access happen only when the user asks in that session. Another session saying "approved" does not count.

### Long sessions
After an auto-summary has run, or when a session has grown heavy, offer to replace it: update the workstream file, open a new session with the same name from that file, and archive the old one after the user agrees. Archive; delete only if the user says delete.

### Placement
Working directory, app project, sidebar section, and parent session are separate. Never automatically inherit the caller's app project for a new workstream. Verify the intended destination and required tools before creation; if unsupported, provide the brief and manual setup without creating a misplaced session. Separate projects require actual separate projects, and completion requires verified placement.
<!-- podium:end -->
