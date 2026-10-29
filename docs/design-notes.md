# Design notes

Findings from implementation-time checks. Dates are when checked.

## Skill loading (2026-10-29)

- Confirmed: loading the folder with `--plugin-dir` registers the skill as `podium:podium` (Claude Code 2.1.309).
- Confirmed (official docs): `SKILL.md` can point to other files in its folder, and those files load only when read. Keep `SKILL.md` short and list each procedure with when to read it.
- Confirmed (official docs): `description` plus `when_to_use` is truncated at 1,536 characters in the skill listing.
- Confirmed (official docs): `disable-model-invocation: true` in frontmatter keeps the description out of context.
- Not usable for plugin skills: the `skillOverrides` setting does not apply to plugin skills (official docs). So an `invocation` option in `.podium.json` cannot switch auto/manual by itself. Manual mode means editing the frontmatter line, or shipping a second skill variant. Decision pending.

## First live test (2026-10-30)

Setup: installed at local scope into a scratch folder; a fresh desktop-app session (Claude Sonnet 5.5) was started there and given four prompts. Its own report is the source; the files it created and its report were read, its full transcript was not.

- Installed cost: about 52 tokens always on, about 610 when the skill is invoked (`claude plugin details`).
- Skill fired on "set up podium", on a new task, and on "how are things"; it did not fire on an unrelated programming question. Each time it read only the matching procedure file.
- It did not read non-matching procedures.
- Session start was refused in the new-task test: the test session was started by another session, so the app does not count its turn as the user's own words. That is a limit of how the test was run, not proof about real use; a run where the user types the request in that session is still untested.
- Gaps found in the procedures and fixed in 0.1.0 (commit "fix: procedures after first live test"): session list covers every folder; no check for the start-session limit before trying; an empty section was left behind when the session could not open; ambiguity about "install only" scope, placeholders, the ID of the first workstream, templates location, priority, file-name slug, localized section names.
- Not fixed, noted: the test answered its own confirmation questions because the brief told it to, so waiting for a real answer is untested.

## Not yet checked

- Whether session start, detach, and move to section work when the user typed the request in that session (the sidebar section creation worked).
- Whether the skill waits for a real answer at each confirmation.
- Headless `claude -p` here is not logged in, so tests run in a desktop-app session.
