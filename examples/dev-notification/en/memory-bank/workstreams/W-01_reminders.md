# Reminders

- ID: W-01 / name: reminders
- Goal: users can set a reminder on a task and get a notification at the right time, on phone and desktop.
- Deadline / schedule: beta cut 2026-10-30, behind a feature flag
- Key documents: docs/reminders-spec.md (invented path for this example)

## Current state
- Research (s-0004) is finished: push services compared; the team will use the platform's own push service for phone and web push for desktop. Details in "Decisions".
- Build (s-0005) has the reminder model and scheduler working in the dev environment; delivery to phone is next.
- Policy check (s-0006) found two open questions on quiet hours and snoozing (see Open items).
- Screens (s-0007) is waiting for the design files; nothing to review yet.

## Next
- build: finish phone delivery, then desktop.
- policy: write the quiet-hours rule once the user decides the snooze limit.
- screens: start when design files arrive.

## Open items
- How long should a snoozed reminder live before it is dropped? Options: 24 hours (recommended: keeps lists clean), 7 days, never.
- Should quiet hours be per user or per device? (policy recommends per user.)

## Decisions
- 2026-10-14: split into research, build, policy, screens. Reason: build and policy run in parallel; research reads a lot; screens need a separate design review.
- 2026-10-15: use platform push for phone and web push for desktop (basis: research summary, s-0004).
- 2026-10-17: replaced the manager session after its auto-summary ran; this file is the handover.

## Session operation
| Session name | Session ID | Role | State |
|---|---|---|---|
| reminders-research | s-0004 | task | finished |
| reminders-build | s-0005 | task | working |
| reminders-policy | s-0006 | task | working |
| reminders-screens | s-0007 | task | waiting on design |
