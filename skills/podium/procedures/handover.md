# handover: replace a long session with a fresh one

Optional. Use when a session's context auto-summary has already run, the conversation has become very long, or the topic has shifted a lot (for example research moved to rollout). The new session starts from files, not from the old conversation.

This is not splitting a task and not summarizing in place. Same work, same name, fresh context.

## 1. Check it is worth it
- Is the session mid-task in a way files cannot capture (a half-finished edit, an open database transaction, a running job)? If so, finish or note that first; do not hand over blindly.
- If the work is nearly done, say so and suggest finishing instead.

## 2. Show the plan and get a yes
Before asking anything of the old session, tell the user in a few lines: which session will be replaced, that it will first update its workstream file, that a new session with the same name will start from that file, and that the old one will be archived last. Ask: **Proceed / Adjust / Keep the old session.** Do nothing until the answer is yes.

## 3. Ask the old session to bring its file up to date
Message it (or do it yourself if you are in it): update the workstream file's "Current state", "Next", "Open items", and "Decisions" so someone who reads only that file can continue. For a risky next step (a deploy, a data change), write the exact order, the checks, and how to undo it. Tell it: do not start new work, and report in one line when finished. For a database or similar session, it must say whether a transaction is still open. For a manager, tell it which sub-sessions to keep untouched.

## 4. Verify, then start the new session
- Read the workstream file. If it is not enough to continue, ask for more before going on.
- Show the brief you will give the new session (the file path, the current step, what is undecided, the reporting rule). The yes from step 2 covers the replacement itself; ask again only if the file update changed the plan.
- With session tools, open the new session with the **same name as the old one**, with no "(replaced)" tag. If the old session was a lead or manager, open the new one the way `new.md` does (detached, in the workstream's section). If the old session was a task session, open it from its lead session. Without session tools, print the brief and ask the user to open it.
- Ask the new session to say in one line that it has taken over and what comes next, then wait for the user.

## 5. Retire the old session
- Only after the new session has confirmed it took over, and the user agrees.
- Default is archive. Delete only if the user says delete. If the old session had sub-sessions you want to keep, detach them first: archiving a parent also archives its finished sub-sessions. Re-list sessions afterward to check.
- The main session updates the ledger: move the old row to "Closed or replaced" with the reason and the file that holds the result, and add the new session to "Active".

## Report
Two lines: which session replaced which, and which file holds the state.
