---
name: podium
description: Use when the user asks to start a new workstream or task area, restructure many sessions, clean up finished sessions or the user says sessions are piling up, check status across workstreams, close a workstream, or hand a long session over to a new one.
---

# podium

Run many sessions without losing track: one sidebar section per workstream, one session per task, context kept in files.
Read only the procedure that matches the situation. Do not read the others.

| Situation | Read |
|---|---|
| First use in a project, or many existing sessions to sort | procedures/init.md |
| User gives a new workstream or task area | procedures/new.md |
| User asks what is going on across workstreams | procedures/status.md |
| A workstream grows and needs sub-sessions | procedures/promote.md |
| A workstream is finished | procedures/close.md |
| Finished or unneeded sessions pile up, the user says there are too many, or asks to clear them in one pass | procedures/tidy.md |
| A long session should be replaced by a fresh one | procedures/handover.md |

## Rules for every procedure

- Talk to the user in the language they use. Keep file names, paths, and commands as they are.
- When a decision is needed, ask one question with a few options and a recommended first option. Use the choice-question tool if your tools have one; otherwise list the options in plain text. Do not decide for the user, and wait for the answer.
- Never create or move sessions, edit the user's `CLAUDE.md`, or archive anything before showing the plan and getting a yes.
- Read settings from `memory-bank/.podium.json` (`idPrefix`, `ledgerPath`, `maxWorkSessions`, `idleDays`). If the file is missing, use `W`, `memory-bank/sessions.md`, `4`, `14`.
- Templates live in this plugin: `<skill directory>/../../templates/` (English) and `.../templates/ko/` (Korean). The skill directory is shown when the skill loads; do not rely on `CLAUDE_PLUGIN_ROOT`, it may be unset. Use the one that matches the user's language. Never overwrite a file that already exists.
- Never write secrets (passwords, keys, tokens) into any file.

## Full rules
The project's `CLAUDE.md` holds only a short pointer. The full rules (roles, when to split, who edits which file, opening order, reporting, approval, replacing a session) are in `<skill directory>/../../docs/rules.md` (Korean: `docs/rules.ko.md`). Read them when a procedure depends on them or you are unsure; do not read them for every request.

## Session tools (desktop app only)

If your tool list has session management tools (list sessions, start session, detach, move to a sidebar section, archive), use them where a procedure says so. If it does not, you are in a plain terminal: print the brief the procedure produces, tell the user to open the session themselves, and record it in the ledger by hand.

Limits seen in the app:
- A session can open a new session only when the user typed a request in that very session. A message from another session, an automated event, or a task another session handed you does not count. Check this before you try: if this turn did not start from the user's own words, do not call the start tool; give the brief and the manual steps instead.
- The session list covers every folder. Keep only sessions whose folder is this project's folder.
- A session nests under the session that opened it, and moves with it. Only the opener can detach it. If a detach or move is refused, say so and give the manual steps (sidebar, right-click, detach to top level, drag to the section).
- Never archive a session that is open on screen or pinned without telling the user; delete only when the user says delete.
