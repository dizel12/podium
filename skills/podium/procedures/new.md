# new: start a workstream

Goal: turn a task the user describes into a workstream with a section, a workstream file, and one lead session. Analyze first, show the split, and only then create anything.

## 1. Understand the task
- Read what the user wrote and any files they point to. Check `progress.md` for an existing workstream that already covers it; if one does, say so and offer to continue it instead.
- Ask only what would change the split, at most three questions (scope, deadline, what "done" looks like, who else is involved). Skip questions whose answers are already in the material.

## 2. Draft the split
Default: **one lead session** that does the whole workstream. Name task sessions only for work that is parallel, reading-heavy, or needs independent verification (see the split criteria in the session rules). Do not propose more than `maxWorkSessions`.

Show:
- Section name and workstream ID (next number after the highest in `progress.md`, with `idPrefix`).
- Lead session: what it will do first.
- Candidate task sessions for later, each with the reason it would be separate. These are not opened now.
- Whether a manager will likely be needed, and the trigger that would promote the lead.
- Anything you are unsure of, marked as such.

Ask: **Proceed / Adjust / Start small (lead session only).** "Start small" is the recommended first option when the task is vague.

## 3. On a yes, create in this order
1. Add the entry to `progress.md` (status: in progress, priority from the user, goal, related files).
2. Create `memory-bank/workstreams/<ID>_<name>.md` from the template: goal, key documents, current state (what you learned in step 1), next steps, open items.
3. Write the lead session's brief. Do not paste the conversation; give: the workstream file path, the goal, the current step, what is undecided, and the reporting rule: **report to the main session only when done, blocked, or a decision is needed; keep progress in the workstream file.** Add the project's own working rules only by pointing to `CLAUDE.md`.
4. With session tools: open the lead session with that brief, detach it from the main session, and put it in the workstream's sidebar section (create the section if needed). If a step is refused, give the user the manual steps.
5. Without session tools: print the brief in one block and ask the user to open a session and paste it.
6. Record the session in the ledger (active table, section list).

## 4. Tell the user
In two or three lines: where the workstream is, which session is the lead, and that task sessions are opened from inside the lead session when it is worth it. Do not start work on the task yourself in the main session.
