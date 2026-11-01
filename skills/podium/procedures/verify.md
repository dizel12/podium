# verify: independent verification of finished work

Goal: have a separate session check the result against the workstream's own acceptance criteria. The session that built something tends to confirm its own assumptions, so it must not verify its own work, and the verifier starts from files, not from the builder's conversation.

## 1. Gather what to verify
Read the workstream file: the goal, the done criteria, and where the result lives (paths, branch, commit). If there are no clear criteria, propose two to five checkable ones and ask the user to confirm them before going on.

## 2. Write the verifier's brief
Files and facts only, no builder conversation. Include:
- what was built and where it is (paths, branch, commit),
- the acceptance criteria, one per line,
- how to check each (commands to run, files to inspect, behavior to try),
- the rules: read-only on the implementation, do not fix anything, record each criterion as pass or fail with the evidence,
- where to write the result (a "Verification" section in the workstream file, or a worklog note) and the reporting rule: tell the lead only when done, blocked, or a decision is needed.
A cheaper model is fine for read-only checks.

## 3. Confirm and open
Show the brief and ask: **Proceed / Adjust / Skip.** It counts toward `maxWorkSessions`.
With session tools, and only when the user typed the request in this session (see the skill's session limits), open the verifier from the lead session so it nests under it. Otherwise print the brief and the manual steps.

## 4. After it reports
- Read what it wrote; do not rely on its one-line report.
- Record the outcome in the workstream file: which criteria passed, which failed, and the evidence.
- If something failed, tell the user plainly and do not fix it from the verifier. Fixing belongs to the lead or a task session.
- The verifier is one-shot: once its result is in a file, offer to archive it.
