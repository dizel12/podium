---
name: podium
description: Use when the user asks to make something a workstream or start a new one ("make this a workstream", "새 업무로 만들어 줘"), set podium up, update podium or its project rules ("podium 업데이트해 줘"), sort or clean up sessions, check status across workstreams, find where something was decided, set up an independent verification of finished work, close a workstream, open a task session for part of a workstream, have a separate session verify finished work, or replace a long session with a fresh one.
---

# podium

Run many sessions without losing track: one sidebar section per workstream, one session per task, context kept in files.
Read only the procedure that matches the situation. Do not read the others.

| Situation | Read |
|---|---|
| First use in a project (no `memory-bank/` yet), or many existing sessions to sort into workstreams for the first time | procedures/init.md |
| User asks to update podium or refresh an existing project's podium rules; checking only is also allowed | procedures/update.md |
| User asks to make a piece of work a workstream or to start a new one, in any field (not only code), or accepts your offer to | procedures/new.md |
| User asks what is going on across workstreams | procedures/status.md |
| A workstream grows and needs sub-sessions | procedures/promote.md |
| A workstream is finished | procedures/close.md |
| podium is already set up and finished or unneeded sessions pile up, or the user asks to clear them in one pass. If there is no `memory-bank/` yet, use init.md first | procedures/tidy.md |
| User asks where or when something was decided, or what happened with something earlier | procedures/find.md |
| Finished work should be checked by a session other than the one that built it | procedures/verify.md |
| A long session should be replaced by a fresh one | procedures/handover.md |

## Rules for every procedure

- A request that combines two procedures (for example "set up and clean up") runs them in order, and each stops at its own confirmation. If `memory-bank/` already exists, skip `init` and say so; an update request uses `update`, not a reinstall of the templates.

- Talk to the user in the language they use. Keep file names, paths, and commands as they are.
- When a decision is needed, ask one question with a few options and a recommended first option. Use the choice-question tool if your tools have one; otherwise list the options in plain text. Do not decide for the user, and wait for the answer.
- Never create or move sessions, edit the user's `CLAUDE.md`, or archive anything before showing the plan and getting a yes.
- Read settings from `memory-bank/.podium.json` (`idPrefix`, `ledgerPath`, `maxWorkSessions`, `idleDays`). If the file is missing, use `W`, `memory-bank/sessions.md`, `4`, `14`.
- Templates live in this plugin: `<skill directory>/../../templates/` (English) and `.../templates/ko/` (Korean). The skill directory is shown when the skill loads; do not rely on `CLAUDE_PLUGIN_ROOT`, it may be unset. Use the one that matches the user's language. Initial setup never overwrites an existing file. Updating existing project rules requires the narrow, approved patch in `update.md`; it never resets the memory-bank from templates.
- The ledger may be a file of its own (`sessions.md`) or a table inside another file (for example a "session registry" section of `CLAUDE.md`, when `ledgerPath` points there). Read the existing table's header first and write rows in that layout: map your fields to its columns by meaning, never add, drop, or reorder columns, and edit only that table. If a field has no column, put it in the closest text column. The ledger belongs to the main session: if you are not it, say what to change instead of editing.
- Never write secrets (passwords, keys, tokens) into any file.

## Placement is a precondition

- Treat working directory, app project membership, sidebar section, and parent-child nesting as separate properties. A shared working directory does not authorize putting every workstream in the current app project.
- Before creating any session, determine the intended destination and check whether the available tools can achieve it. Separate workstreams must be independently grouped; never silently inherit the current app project. If the user asks for independent projects, sidebar sections or projectless chats are not equivalent.
- If the required project cannot be created or selected, or the required detach/move operation is unavailable, stop before creating the session. Explain the missing capability and give the prepared brief and the minimal manual setup step. Do not create a misplaced session as a fallback.
- After creation, read back actual project membership, section, and nesting where supported. Report setup complete only for properties actually verified. Missing evidence means unverified, not success.
- Use the host's actual tool schema. Tool names, fields, nesting, and detach behavior described in procedures may be host-specific; do not assume another app implements them.

## Full rules
The project's `CLAUDE.md` holds only a short pointer. The full rules (roles, when to split, who edits which file, opening order, reporting, approval, replacing a session) are in `<skill directory>/../../docs/rules.md` (Korean: `docs/rules.ko.md`). Read them when a procedure depends on them or you are unsure; do not read them for every request.

## Session tools (desktop app only)

If your tool list has session management tools (list sessions, start session, detach, move to a sidebar section, archive), use them where a procedure says so. If it does not, you are in a plain terminal: print the brief the procedure produces, tell the user to open the session themselves, and record it in the ledger by hand.

Limits seen in the app:
- A session can open a new session only when the user typed a request in that very session. A message from another session, an automated event, or a task another session handed you does not count. Check this before you try: if this turn did not start from the user's own words, do not call the start tool; give the brief and the manual steps instead.
- The session list covers every folder, and sidebar sections are shared across projects. Decide what belongs to this project by each session's working folder, not by its section.
- A session nests under the session that opened it, and moves with it. Only the opener can detach it. If a detach or move is refused, say so and give the manual steps (sidebar, right-click, detach to top level, drag to the section).
- Never archive a session that is open on screen or pinned without telling the user; delete only when the user says delete.
