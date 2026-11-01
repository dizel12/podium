# init: first use in a project

Goal: install the memory-bank and the session rules, and if the project already has many sessions, propose how to group them into workstream sections. Nothing changes until the user says yes.

## 1. Check what exists
- If `memory-bank/progress.md` and the ledger already exist, podium is installed. Tell the user. If they also asked to sort or clean up sessions, continue with `tidy.md`; otherwise run `status.md`. An empty ledger is normal in a new project and does not mean podium is missing.
- Read the project `CLAUDE.md` (if any) and a list of the docs folder. Note existing rules so you do not contradict them.
- If you have session tools, list the sessions and keep only those in this project's folder: title, section, who opened it, whether it is running. Sessions from other folders belong to other projects; leave them alone.

## 2. Pick the case
- No sessions or a brand-new project: plan to install only (files and rules).
- Several existing sessions: plan to also group them.

## 3. Draft the plan (guesses marked as guesses)
Show the user, briefly:
- Workstreams you infer, each with: a name, the sessions that seem to belong to it, and which one could be the lead session.
- Shared tool sessions (database lookup, meeting notes) and the shared section.
- What would be created: `memory-bank/` files, a section in `CLAUDE.md`, sidebar sections, moves.
- What you could not tell from titles alone; ask about those, at most three questions.
Do not invent workstreams the sessions do not support. Prefer fewer sections.

Ask: **Proceed / Adjust / Install rules and folders only.** "Install rules and folders only" means steps 1 and 2 below; steps 3 to 5 are skipped, and the copied files keep their placeholders until a workstream is started.

## 4. On a yes, in this order
1. Copy the templates (from this plugin's `templates/`, see the skill's rules) into `memory-bank/` (skip any file that exists): `activeContext.md`, `progress.md`, the ledger, `workstreams/_template.md`, `worklog/_template.md`, `.podium.json`.
2. Append the short session pointer (`templates/session-rules.md`, or `templates/ko/session-rules.md`) to the end of the project `CLAUDE.md`. It is short on purpose: every session in the project reads it. Do not paste the full rules (`docs/rules.md`) there. Create `CLAUDE.md` if there is none.
3. Write one entry per workstream into `progress.md` with new IDs (`<idPrefix>-01`, `-02`, ...). Create each workstream file from the template with what you actually know; leave the rest as open items.
4. Fill the ledger: sections, active sessions, roles.
5. With session tools: create the sidebar sections and move sessions into them. This changes the user's sidebar, so it is only done after the "Proceed" answer. Sessions nested under another session move with it; detach is possible only for sessions you opened. If a move is refused, list those sessions with the manual steps and carry on with the rest.

## 5. Report
One short list: created, moved, skipped and why. Say what the user must do by hand. Remind them that new work now starts by telling you the task.
