# new: start a workstream

Goal: turn a task the user describes into a workstream with a section, a workstream file, and one lead session. Analyze first, show the split, and only then create anything.

## 0. Is podium installed here?
If `memory-bank/` does not exist, this is a first use. Say so in the plan and include the init install steps (copy the templates, append the session rules to `CLAUDE.md`) in what you will create, so the lead session works under the rules. Do not skip the rules just because the user only described a task.

## 1. Understand the task
- Read what the user wrote and any files they point to. Check `progress.md` for an existing workstream that already covers it; if one does, say so and offer to continue it instead.
- Ask only what would change the split, at most three questions (scope, deadline, what "done" looks like, who else is involved). Skip questions whose answers are already in the material. Do not ask about priority: use "normal" and say so in the plan, so the user can change it.

## 2. Draft the split
Default: **one lead session** that does the whole workstream. Name task sessions only for work that is parallel, reading-heavy, or needs independent verification (see the split criteria in the session rules). Do not propose more than `maxWorkSessions`.

Show:
- Section name (the workstream's title) and workstream ID: the next number after the highest real entry in `progress.md`, written `<idPrefix>-NN` with two digits (`W-01`, `W-02`), the same way the templates write it. Ignore the placeholder block from the template (the one with `<...>` fields); the first real entry replaces it.
- Lead session: what it will do first.
- Candidate task sessions for later, each with the reason it would be separate. These are not opened now.
- Whether a manager will likely be needed, and the trigger that would promote the lead.
- Anything you are unsure of, marked as such.

Ask: **Proceed / Adjust / Start small (lead session only).** "Start small" is the recommended first option when the task is vague.

## 3. On a yes, create in this order
1. Add the entry to `progress.md` (status: in progress, priority from the user, goal, related files).
2. Create `memory-bank/workstreams/<ID>_<name>.md`, where `<name>` is a short ASCII kebab-case slug of the title, from the template: goal, key documents, current state (what you learned in step 1), next steps, open items.
3. Write the lead session's brief. Do not paste the conversation; give: the workstream file path, the goal, the current step, what is undecided, and the reporting rule: **report to the main session only when done, blocked, or a decision is needed; keep progress in the workstream file.** Add the project's own working rules only by pointing to `CLAUDE.md`.
4. With session tools, first check that this turn started from the user's own words (see the skill's session limits). If it did not, skip to step 5. Otherwise open the lead session: brief to `prompt`; the goal, decisions so far and constraints to `background` (at least 80 characters, the tool refuses less); `cwd` this project's folder; same folder, no separate worktree, unless the project already uses worktrees. Then detach it from the main session and put it in the workstream's sidebar section. Create the section only together with the session. Afterwards read the session back (get its details) and confirm it exists, is detached, and is in the section; report what you confirmed, not what you asked for. If opening is refused, do not work around it and do not leave an empty section: go to step 5 and include creating the section in the manual steps.
5. Without session tools: print the brief in one block and ask the user to open a session and paste it.
6. Record the session in the ledger (active table, section list). If no session exists yet, write the row with the session ID "(not created)" and a note, so status shows it as pending.

## 4. Tell the user
In two or three lines: where the workstream is, which session is the lead, and that task sessions are opened from inside the lead session when it is worth it. Do not start work on the task yourself in the main session.
