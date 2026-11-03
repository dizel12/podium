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

## Test A: set up and clean up in a folder that already has sessions (2026-11-01)

Setup: a session in the scratch folder was asked "set up podium and clean up sessions". The folder already held a memory-bank from an earlier test, so this exercised routing, not a clean first install. Source: the subject's report and the start of its transcript.

- Routed correctly: it saw the existing memory-bank, skipped init, and followed tidy; it kept to this project's folder by working folder, listed the folder's three test sessions, left out sessions of other folders, and stopped at the confirmation question without acting.
- It read init and status before tidy, which cost tokens; the table row and the combined request made the choice unclear.
- Gaps fixed: what to do when memory-bank exists and the user also asked to clean up; folder scoping by working folder, not sidebar section; no evidence rule for offering delete; the "recent activity" window was loose (now 48 hours); a combined request runs the procedures in order.
- Not covered: a truly clean init in a folder with many sessions.

## Test B: find, verify, promote, handover up to their confirmation questions (2026-11-01)

Setup: a session in a folder holding the fictional memory-bank, five prompts in one brief, stopping before anything that would create, open, move, archive, or edit. The memory-bank was compared with the fixture afterwards: unchanged. Source: the full transcript of the test session.

- find: answered a decision question from the workstream file with its date and basis, and did not search sessions when the file was enough. For a term absent from the files it searched sessions across folders, including archived ones, and found two earlier test sessions; it said the answer came from conversation snippets and was not confirmed in any file.
- verify: noticed the workstream had a goal but no acceptance criteria, and stopped at proposing criteria to confirm, as intended.
- promote: noticed the workstream was already at the task-session limit (a finished one still counted) and moved to offering to archive or merge first. Gap fixed: what to do when the request reaches a session that is not the lead, and that finished sessions count until archived.
- handover: stopped before asking the old session to edit its file, because the procedure asked the user only after that. Fixed: the plan and the yes now come first.
- Not tested: opening the sessions themselves (needs the user's own typed request), tidy's archive and delete step, a truly empty folder's first init.
- During this test the working tree held uncommitted edits to `SKILL.md`, `new.md`, the rules docs, and the templates that were not made by the test sessions or the author of the commits above; the subject read them. They are about placement of new sessions. They are not part of any commit here.

## Test C: clean init, new workstream, and tidy with real archiving (2026-11-02)

Setup: a session in an empty folder and the earlier test-A session. The author delegated the whole test to the orchestrating session, which relayed the requests and answers as messages, each labelled as relayed. The author typed one answer ("go ahead") in the empty-folder session. Source: the sessions' transcripts, the files on disk, and the app's session list read afterwards.

- Clean init: in an empty folder it showed a plan, asked for a yes, and after the yes created six memory-bank files and a `CLAUDE.md`. The six files and the `CLAUDE.md` match the Korean templates exactly.
- New workstream: it asked two questions first (where the app code is, and whether a small task should be a workstream), showed a draft plan with the placement note, and noticed that a request relayed by another session cannot open a session. After the answers it created the progress entry, the workstream file, and a ledger row marked "(not created)", printed the lead session's brief, and listed what it had and had not verified. It did not create a sidebar section, as intended.
- Gap fixed: the ledger kept template placeholders and a made-up main session name; `new` now fills known fields and deletes lines it cannot fill.
- Tidy: it chose tidy over init (the memory-bank existed, and it checked instead of trusting the relayed text that said otherwise), scoped to the working folder, wrote a candidate table with reasons, and stopped at the question. After the choice "archive two, keep the one active within 48 hours" it archived exactly those two; the app's list afterwards shows the two archived and every other session unchanged. It left the ledger alone because the ledger belongs to the main session.
- Observation: `new` asks up to three things before creating anything (the small-task check, an app-location question when the folder is empty, and a placement confirmation at open time). Worth watching for friction.
- Still not tested: opening sessions from a request the user typed in that very session (lead session, task session, verifier, replacement session), and a replacement actually archiving its predecessor.

## Test D: opening a lead session from a turn the user typed (2026-11-03)

The author asked the orchestrating session, in that session itself, to run the open step. The skill was not loaded there, so the orchestrating session ran the `new` procedure's open step by hand; this tests the app's side, not the skill's wording.

- Start was accepted this time (the previous refusals were all in turns started by another session or an automated event). The lead session was opened with the brief, detached from the opener, filed into a newly created sidebar section, and read back from the app: detached, in the section, working folder correct.
- The lead session read its workstream file, announced "taking over, next: …" in one line, created nothing, and waited, as the brief said.
- The ledger in the scratch folder was updated by the orchestrating session (main role): session name, ID, section, and a note that detachment was verified in the app.
- Still not tested: opening task, verification, and replacement sessions from inside that lead session (they must be typed by the user there so the new sessions nest under the lead).

## Test E: split, verify, and replace, each typed by the user inside the sessions (2026-11-03)

The author typed the requests in the lead session and in the research session. Source: the full transcripts of the lead and research sessions, the app's session list, and the files on disk.

- Worked: the lead opened a research task session on request; it started from the user's typed turn, nested under the lead, and sat in the lead's section. The research session saved its result to the shared notes folder and made no project files. The lead refused to open a verifier while there was nothing to verify, then, after the app blocked a start made in a notification turn and turned it into a start card, the author started the card: the verifier opened under the lead, read the result file only, and returned a verdict with specific gaps. The lead then asked the author the open questions as choices. A user-typed "replace this session" in the research session produced a working successor that read the result note and the workstream file and waited.
- Did not fire: the podium skill. None of the three sessions called it. They acted from the short pointer in `CLAUDE.md` alone. The result was close to intended, but skipped the skill's own safeguards: no limit check or plan question before opening the task session, the workstream file's session table was not updated (results stayed in the notes folder), the replacement got a reworded title with a "(replaced)" tag, and the research session opened its own successor, so the tree is now lead, research, research-2 (four layers; archiving the old research session would archive its finished child too).
- Fixes made: the description now names opening a task session and having a separate session verify; `handover` says a task session never opens its own replacement and the replacement keeps the exact title; the CLAUDE.md pointer asks to record opened sessions and results in the workstream file and says a task session asks the lead to replace it.
- Not retested after these fixes.

## Not yet checked

- Headless `claude -p` here is not logged in, so tests run in a desktop-app session.
