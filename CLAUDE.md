# podium

If the user asks what this repository is, answer in two or three plain sentences in their language, then tell them how to start:

- What it is: a Claude Code plugin that turns each task into a workstream (one sidebar section, one file holding its state, one lead session) so many sessions do not pile up in one list.
- Who it is for: people who run several pieces of work at once in Claude Code, not only code.
- How to start: install it (see README.md, section Install), then say "Set up podium and sort my sessions" in a project, or just describe a new task.
- Read the current version from `.claude-plugin/plugin.json`. Describe the tested scope and remaining gaps from README.md and docs/design-notes.md; do not claim that every procedure is verified in live sessions.

## Working on this repository

- Procedures in `skills/podium/procedures/` are English only. User-facing docs, templates, and examples exist in English and Korean; keep both in step.
- Keep `SKILL.md` short: the one-line description is in context on every turn.
- Examples must be invented.
- Do not push, open pull requests, or create a public repository unless the owner asks.
- Commits: no AI co-author trailer; keep any `Signed-off-by`.
