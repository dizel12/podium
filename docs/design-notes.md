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

## Second live test, typed by the user (2026-10-30)

The user typed the requests in a clean session in the scratch folder. Read from that session's transcript and checked against the app's session list and the files on disk.

- Confirmed: the skill fired on a typed new-task request, read only `new.md`, showed a plan, and waited for the user's real answer before creating anything.
- Confirmed: with the user's typed answer, the app allowed the lead session to be opened, detached from the opener, and filed into a new sidebar section (read back: detached, parent was the test session, section matched).
- Confirmed: status reported per workstream and noticed the ledger still showed the workstream active after the lead had finished it.
- Confirmed: close read the files itself before asking to archive, asked before archiving or removing the section, and offered archive, not delete.
- Gaps fixed: IDs were planned as `W1` then written `W-01` (format now stated); with no `memory-bank/`, new skipped installing the rules, so the lead session ran without them in `CLAUDE.md` (new now includes the install steps); new reported the session as placed before reading it back (now reads it back).
- Still untested: promote and handover, a project that already has many sessions (init with a real session list), and a second workstream.

## Fire test with five ordinary phrasings (2026-11-01)

Setup: one session in the scratch folder was given five prompts in one brief and asked to report whether the skill fired. Weak evidence: the subject knew it was a podium test, all prompts came in one message, and the folder had no podium files. Only the first skill call is visible in the transcript; the other decisions are the subject's own report.

- Fired as intended: "too many sessions" (tidy), "refactoring is done, let's wrap up" (close).
- Did not fire: a new feature request ("build a sign-up screen by next month"), a non-code planning request ("plan a trip, help me get organized"), and an unrelated explanation request (correct).
- Findings: the description did not signal that non-code or multi-session work counts, so the trip request was treated as unrelated; the sign-up request was borderline; "wrap up" could mean finishing code; "too many sessions" fits both init and tidy.
- Changes made, not yet retested: description now says work spanning several sessions or steps, code or not; `new` skips small one-conversation tasks; `close` first checks what "wrap up" means; init vs tidy told apart in the skill table.

## Not yet checked

- Headless `claude -p` here is not logged in, so tests run in a desktop-app session.
