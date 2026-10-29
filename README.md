# podium

[한국어](README.ko.md)

**Status: designed and written, not yet tested in live sessions. Version 0.1.0, not published.**

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
3. Next time you have a task, say it as you normally would, for example: "I need to add reminders to my to-do app." podium reads what you point it to, asks up to three questions, shows a plan (section name, lead session, task sessions it might add later) and asks: proceed, adjust, or start small.
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

- One skill, `podium`, and six procedures it picks from: set up a project, start a workstream, status, split or promote, close, and replace a long session. You do not memorize commands.
- Templates for the files that keep context (`memory-bank/`) and a rules section for your `CLAUDE.md`, in English and Korean.
- Two fictional examples under `examples/`: a software feature and a move.

## How it keeps cost low

Only the skill's one-line description is in context on every turn. The procedures and templates are read only when needed. If even that line bothers you, turn on manual mode: in `skills/podium/SKILL.md`, add `disable-model-invocation: true` to the frontmatter, then call it with `/podium` when you want it.

## Settings

`memory-bank/.podium.json`: `idPrefix` (default `W`), `ledgerPath` (default `memory-bank/sessions.md`), `maxWorkSessions` (default 4). See [docs/config.md](docs/config.md).

## Limits

- Creating sessions and filing them into sidebar sections uses the desktop app's session tools. In a plain terminal, podium still sets up the files and rules and gives you briefs to paste, but you open sessions yourself.
- A session can open new sessions only when you typed a request in that session, and only the session that opened another can detach it. podium works around this by opening each workstream's lead session first and having you split from inside it.
- podium does not say how a session should do its work (coding style, tests, writing). Keep that in your own `CLAUDE.md`.
- Not yet verified in live sessions: that the skill reads only the matching procedure, stays quiet on small questions, and can call the app's session tools. See [docs/design-notes.md](docs/design-notes.md).

## Similar projects

Gas Town and CCPM coordinate coding agents automatically; claude-workstream-kit keeps workstream state in files for one project. podium is for a person running many sessions across kinds of work. Details and sources: [docs/design-notes.md](docs/design-notes.md).

## License

MIT
