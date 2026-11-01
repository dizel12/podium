# tidy: clean up finished or unneeded sessions

Goal: survey the sessions, find the ones that are finished and whose results are safe in files, and retire them in one pass after the user picks. Nothing is archived or deleted before the user has chosen.

## 1. Scope
- Default: sessions in this project's folder. The session list covers every folder; include other folders only if the user says so.
- Never include the main session or shared tool sessions, and never the session you are running in.

## 2. Survey
With session tools, list the sessions: title, folder, section, running or not, pinned, pull request number and state, last activity, who opened it, whether it has a parent. If podium files exist, read the ledger, `progress.md`, and the workstream files. Judge from this metadata and the files; do not read whole transcripts unless something is unclear, and then read only the end.

## 3. Sort each session
**Keep, do not offer:**
- running, pinned, or open on screen
- an open pull request
- the ledger or `progress.md` says the workstream is still active
- a manager with active sub-sessions
- recent activity (within the last 48 hours)
- you can see unfinished work: uncommitted or unpushed changes in its folder (read-only git commands), an open transaction mentioned in its workstream file

**Candidate:** finished and the result lives outside the conversation: a merged or closed pull request, a workstream marked done with its worklog written, a ledger row already closed, or no activity for `idleDays` days (default 14) with nothing open.
Write one line per candidate: why it is finished, and where the result lives (file, pull request, branch). If the result exists only in the conversation, it is not a candidate: offer to write it into the workstream file first.

**Unclear:** say what is missing and ask. Do not guess.

## 4. Parents and children
Archiving a parent also archives its finished sub-sessions. If a child should live on, it must be detached first, and only the session that opened it can detach it. List these cases in the plan; if you cannot detach, say so and leave the parent out.

## 5. Show the plan and ask
Show a table: session, why it is a candidate, where the result lives, and the action proposed. Then ask: **Archive the selected (can be undone) / Delete the selected permanently / Choose one by one / Cancel.** Let the user remove items from the list and follow their exclusions exactly.
- Archive is the default and the recommended option. An archived session keeps its conversation, and the session search can include archived sessions, so what was decided there stays findable. Recommend archive for any session that did real work.
- Offer delete only for sessions with nothing worth keeping, and only when the evidence says so: the user called it a test or throwaway, its workstream file or ledger note says so, or it never got past the first turn. Say that delete also destroys the conversation. When unsure, recommend archive.
- Delete only if the user asks for delete in this exchange or picks it. Say that delete cannot be undone, and expect the app to ask for approval again.
- If the user says only "close" or "clean up", treat it as archive and say you did.

## 6. Do it
- Run the action on the chosen sessions. Skip any that fail and keep going. Sessions open on screen or pinned cannot be removed: list them and ask the user to close them.
- Afterwards list the sessions again and compare. A child may have been archived with its parent, or a session may be missing that you did not expect; tell the user.

## 7. Record and report
- Move the matching ledger rows to "Closed or replaced". In the reason column write one line that works as an index for the archived session: what the work was, what was decided or produced, and where the result lives (file, pull request, branch). The ledger belongs to the main session: edit it if you are the main session, otherwise tell the user what to change. Remove an empty sidebar section only after asking.
- Report: how many archived, how many deleted, what was kept and why, what failed, and what is now gone for good.
