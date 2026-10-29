# Design notes

Findings from implementation-time checks. Dates are when checked.

## Skill loading (2026-10-29)

- Confirmed: loading the folder with `--plugin-dir` registers the skill as `podium:podium` (Claude Code 2.1.309).
- Confirmed (official docs): `SKILL.md` can point to other files in its folder, and those files load only when read. Keep `SKILL.md` short and list each procedure with when to read it.
- Confirmed (official docs): `description` plus `when_to_use` is truncated at 1,536 characters in the skill listing.
- Confirmed (official docs): `disable-model-invocation: true` in frontmatter keeps the description out of context.
- Not usable for plugin skills: the `skillOverrides` setting does not apply to plugin skills (official docs). So an `invocation` option in `.podium.json` cannot switch auto/manual by itself. Manual mode means editing the frontmatter line, or shipping a second skill variant. Decision pending.

## Not yet checked

- Whether the skill, in a real model session, reads only the matching procedure file.
- Whether a one-line description fires on new-workstream requests and stays quiet on small questions.
- Whether the skill can call the desktop app's session tools (start session, detach, move to section).
- These need a logged-in interactive session. Headless `claude -p` here is not logged in.
