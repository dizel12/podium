# promote: split a workstream into task sessions, or promote the lead to manager

Run this from inside the workstream's lead session, when the user asks to split work or the lead is getting heavy. The main session does not open a workstream's task sessions: they would nest under main and break the grouping.

Goal: split only when it pays off, keep the count small, and keep the workstream file the single source of truth.

## 1. Check whether splitting is worth it
Read the workstream file and its `progress.md` entry. A split is justified only if at least one holds:
- the work runs in parallel with other work (for example building while a policy check runs),
- it needs a lot of reading that would weigh down the lead session,
- a result needs independent verification (the session that built it must not verify it).
If none holds, say so and recommend staying in one session. The user decides.

Check the limit: count the workstream's active task sessions in the ledger. At `maxWorkSessions` or more, do not open another. Offer to close a finished one or merge two tasks first.

## 2. Check whether the lead should become a manager
Promote when any holds: two or more tasks run at the same time, decisions or outside answers keep piling up, or unlike kinds of work are mixed (for example paperwork and building).
Do not promote for a single task. Never put a manager under a manager: the depth stops at main, manager, task session.

## 3. Propose the split
Show, for each proposed task session:
- the task in one line and why it should be separate (one of the three reasons above),
- what it reads and which part of the workstream file it will write to,
- how it reports (to the lead or manager only, when done, blocked, or a decision is needed).
Ask: **Proceed / Adjust / Stay in one session.** Ask once for the whole set, not per session.

## 4. On a yes
1. If promoting: add a "Session operation" section to the workstream file (table: session name, ID, role, state). The manager now owns this file.
2. For each task session, write a brief: the workstream file path, the single task, what is already known, what to write and where, and the reporting rule. Do not paste the conversation.
3. With session tools: open the task sessions from this session, so they nest under it and land in the same section. This works only when the user asked for it in this session, which the "Proceed" answer is. If a session cannot be opened, print the brief and give the manual step.
4. Without session tools: print each brief and ask the user to open the sessions and paste them.
5. Report each new session to the user and ask them to tell the main session, or send one line to the main session if you can: workstream ID, session names, roles. The main session updates the ledger; you do not edit it.

## 5. Afterwards
Update the workstream file's "Session operation" table when sessions open, finish, or are replaced. Collect task results into "Current state" and "Decisions" yourself; task sessions write only their own sections.
