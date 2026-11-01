# podium

[한국어](README.ko.md)

**Status: written and tested in live sessions for set-up, new workstream, status, and close; splitting, replacing a long session, and cleaning up are not yet tested. Version 0.1.0, not published.**

## What is this?

podium is a Claude Code plugin that keeps many sessions from piling up in one flat list.
You tell Claude a task in plain words. podium turns each task into its own workstream: one sidebar section, one file that holds what is going on, and one lead session. When a workstream gets big, the lead session can take on task sessions; when it is small, it stays one session.
Because the state lives in files and not in the chat, you can close any session and a new one picks up where it stopped.

## Who is it for?

- You use Claude Code, mostly in the desktop app, for more than one piece of work at a time, and your sidebar has become a long list of similar titles.
- Your work is not only code. The examples include a non-coding one (planning a move).
- You want to steer: podium asks before it creates or moves anything.

It is not for you if you run one task at a time, or if you want agents to run on their own without you. Tools like that exist; podium is the opposite: a person runs it.

## Your first 5 minutes

1. Install it (below).
2. In a project, say: "Set up podium and sort my sessions." podium reads your sessions and docs, shows how it would group them, and asks: proceed, adjust, or only install the files and rules.
3. When you have a piece of work that will take more than one session, tell Claude to make it a workstream, for example: "Make this a workstream: add reminders to my to-do app." If you forget, Claude offers once when it sees a big piece of work. podium reads what you point it to, asks up to three questions, shows a plan (section name, lead session, task sessions it might add later) and asks: proceed, adjust, or start small. Small tasks stay in a normal conversation; you do not need podium for them.
4. Open the lead session it made and work there. Ask for task sessions from inside the lead session only when splitting pays off.
5. When the work is done, say so. podium checks the files before it archives the sessions.

## Install

Not published yet. To try it from a local copy, in a terminal:

```bash
claude plugin marketplace add ./podium
claude plugin install podium@podium
```

or load it for one session only: `claude --plugin-dir ./podium`.
After it is published the first command will take a GitHub `owner/repo` instead of a path. In the desktop app, use the **+** button next to the prompt box and choose **Add plugins** once the marketplace is added.

## What you get

- One skill, `podium`, and nine procedures it picks from: set up a project, start a workstream, status, split or promote, close, clean up finished sessions in one pass, find where something was decided, verify finished work with a separate session, and replace a long session. There are no commands to memorize; you ask in plain sentences such as "make this a workstream", "how are things", "close this workstream", "clean up finished sessions", "where did we decide the caching approach?".
- Templates for the files that keep context (`memory-bank/`) and a short rules section for your `CLAUDE.md` (about 370 words, roles, splitting, file ownership, reporting, approval) so every session in the project knows podium exists, in English and Korean. The full rules are in [docs/rules.md](docs/rules.md).
- A template for shared tool sessions such as a read-only data lookup (`templates/tool-session.md`).
- Two fictional examples under `examples/`: a software feature and a move.

## How it keeps cost low

Only the skill's one-line description is in context on every turn. The procedures and templates are read only when needed. If even that line bothers you, turn on manual mode: in `skills/podium/SKILL.md`, add `disable-model-invocation: true` to the frontmatter, then call it with `/podium` when you want it.

## Settings

`memory-bank/.podium.json`: `idPrefix` (default `W`), `ledgerPath` (default `memory-bank/sessions.md`), `maxWorkSessions` (default 4). See [docs/config.md](docs/config.md).

## Limits

- Creating sessions and filing them into sidebar sections uses the desktop app's session tools. In a plain terminal, podium still sets up the files and rules and gives you briefs to paste, but you open sessions yourself.
- A session can open new sessions only when you typed a request in that session, and only the session that opened another can detach it. podium works around this by opening each workstream's lead session first and having you split from inside it.
- podium does not say how a session should do its work (coding style, tests, writing). Keep that in your own `CLAUDE.md`.
- Verified in live sessions (see [docs/design-notes.md](docs/design-notes.md)): the skill reads only the matching procedure, stays quiet on small questions, waits for your answer, and can open and file a lead session when you typed the request. Not yet verified: splitting, replacing a long session, cleaning up, a project with many existing sessions.

## Similar projects

Gas Town and CCPM coordinate coding agents automatically; claude-workstream-kit keeps workstream state in files for one project. podium is for a person running many sessions across kinds of work. Details and sources: [docs/design-notes.md](docs/design-notes.md).

## License

MIT
