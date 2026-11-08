# podium

<p align="center"><b>English</b> | <a href="README.ko.md">한국어</a></p>

![podium: a penguin conductor on a podium raises a baton over a flock of penguins, with small session cards floating above them](docs/assets/banner.png)

**Version 0.2.2, early.** Tested in live sessions: set-up, new workstream, status, close. Not yet fully verified: splitting a workstream, replacing a long session, cleaning up many sessions. The new project-rule update procedure has passed structure and manifest checks but has not been tested in a live conversation. Details: [docs/design-notes.md](docs/design-notes.md).

## What is this?

podium is a Claude Code plugin that keeps many sessions from piling up in one flat list.
You tell Claude a task in plain words. podium turns each task into its own workstream: one sidebar section, one file that holds what is going on, and one lead session. When a workstream gets big, the lead session can take on task sessions; when it is small, it stays one session.
Because the state lives in files and not in the chat, you can close any session and a new one picks up where it stopped.

![Before and after: on the left, scattered penguins with tangled session cards; on the right, the same penguins lined up in three groups under a penguin conductor on a podium](docs/assets/concept.png)

### The few terms you need

| Term | Meaning |
|---|---|
| Workstream | One piece of work that takes more than one session, such as "add reminders to my to-do app". It gets one sidebar section and one file. |
| Lead session | The first session of a workstream. It does the whole job until splitting pays off. |
| Task session | A session that does one task of a workstream. A lead session that coordinates several of them is called a manager. |
| Main session | The one session you talk to first. It does not do the work; it opens workstreams, hands out tasks, and reports. |
| `memory-bank/` | A folder of Markdown files that holds the state: what is done, what is next, what was decided. A new session reads these instead of the old chat. |

### What it looks like

The sidebar gets one section per workstream. The files sit in your project:

```text
Sidebar                      Your project
-------                      ------------
Shared tools                 memory-bank/
  main                         activeContext.md     where things stand across workstreams
Reminders                      progress.md          one line per workstream
  reminders-lead               sessions.md          which sessions are open or replaced
Login bug                      workstreams/
  login-bug                      W-01_reminders.md  goal, status, next steps, decisions
                                 W-02_login-bug.md
                               worklog/             finished work, one file each
```

A complete filled-in version is in [examples/dev-notification](examples/dev-notification/README.md) (a software feature) and [examples/moving-plan](examples/moving-plan/README.md) (a non-coding example).

## Who is it for?

- You use Claude Code, mostly in the desktop app, for more than one piece of work at a time, and your sidebar has become a long list of similar titles.
- Your work is not only code. The examples include a non-coding one (planning a move).
- You want to steer: podium asks before it creates or moves anything.

It is not for you if you run one task at a time, or if you want agents to run on their own without you. Tools like that exist; podium is the opposite: a person runs it.

## Your first 5 minutes

1. Install it (below).
2. In a project, say: "Set up podium and sort my sessions." podium reads your sessions and docs, shows how it would group them, and asks: proceed, adjust, or only install the files and rules.
3. When a piece of work will take more than one session, say: "Make this a workstream: add reminders to my to-do app." If you forget, Claude offers once when it sees a big piece of work. Small tasks stay in a normal conversation.
4. podium reads what you point it to, asks up to three questions, and shows a plan: section name, lead session, task sessions it might add later. You answer: proceed, adjust, or start small.
5. Work in the lead session it made. Ask for task sessions from inside the lead session, only when splitting pays off.
6. When the work is done, say so. podium checks the files before it archives the sessions.

## Requirements

- Claude Code with plugin support (the `claude plugin` commands).
- For the full experience, the Claude desktop app: creating sessions and filing them into sidebar sections uses its session tools. In a plain terminal podium still sets up the files and rules and gives you briefs to paste, but you open sessions yourself.

## Install

In a terminal:

```bash
claude plugin marketplace add stlahxm/podium
claude plugin install podium@podium
```

The marketplace installs the published release pinned by tag and commit, rather than the latest development files on `main`. Creating a GitHub Release alone does not update this pin. See [Releasing](docs/releasing.md) for the release process.

To update an existing install:

```bash
claude plugin marketplace update podium
claude plugin update podium@podium
```

Updates require a new plugin version. Auto-update is optional and is enabled by the user in `/plugin` → Marketplaces.

Plugin updates do not rewrite rules previously copied into your project. Since v0.2.0, you can ask podium to compare project rules and prepare a patch for your approval. This is a guided procedure, not an automatic migration service. See [Updating project rules](docs/updating.md).

To try it for one session only, clone the repository and run `claude --plugin-dir ./podium`.
In the desktop app, use the **+** button next to the prompt box and choose **Add plugins** once the marketplace is added.

## What you get

- One skill, `podium`, and ten procedures: set up a project, update the plugin or project rules, start a workstream, status, split or promote, close, clean up finished sessions in one pass, find where something was decided, verify finished work with a separate session, and replace a long session. There are no commands to memorize; you ask in plain sentences such as "make this a workstream", "update podium", "how are things", "close this workstream", "clean up finished sessions", "where did we decide the caching approach?".
- Templates for the files that keep context (`memory-bank/`) and a short rules section for your `CLAUDE.md` (about 370 words, roles, splitting, file ownership, reporting, approval) so every session in the project knows podium exists, in English and Korean. The full rules are in [docs/rules.md](docs/rules.md).
- A template for shared tool sessions such as a read-only data lookup (`templates/tool-session.md`).
- Two fictional examples under `examples/`: a software feature and a move.

## How it keeps cost low

Only the skill's one-line description is in context on every turn. The procedures and templates are read only when needed. If even that line bothers you, turn on manual mode: in `skills/podium/SKILL.md`, add `disable-model-invocation: true` to the frontmatter (the settings block at the top of the file), then call it with `/podium` when you want it.

## Settings

`memory-bank/.podium.json`: `idPrefix` (default `W`), `ledgerPath` (default `memory-bank/sessions.md`), `maxWorkSessions` (default 4). See [docs/config.md](docs/config.md).

## Limits

- A session can open new sessions only when you typed a request in that session, and only the session that opened another can detach it (take it out from under its parent in the sidebar). podium works around this by opening each workstream's lead session first and having you split from inside it.
- podium does not say how a session should do its work (coding style, tests, writing). Keep that in your own `CLAUDE.md`.
- Verified in live sessions (see [docs/design-notes.md](docs/design-notes.md)): the skill reads only the matching procedure, stays quiet on small questions, waits for your answer, and can open and file a lead session when you typed the request. Not yet verified: splitting, replacing a long session, cleaning up, a project with many existing sessions.

## Similar projects

- [Gas Town](https://github.com/gastownhall/gastown) and [CCPM](https://github.com/automazeio/ccpm) coordinate coding agents automatically.
- [claude-workstream-kit](https://github.com/ChristopherA/claude-workstream-kit) keeps workstream state in files for one project.
- podium is for a person running many sessions across kinds of work, with the person deciding each step.

Details and sources: [docs/design-notes.md](docs/design-notes.md).

## Contributing

Contributions are welcome, from anyone. Most changes are wording, so you do not need to write code.

Good first contributions:
- Run podium in a live session and tell us what happened (what you typed, what it did). Results for the untested procedures (splitting, replacing a long session, cleaning up) are the most useful.
- Improve a procedure, a template, or the docs. English and Korean files are changed together; [CONTRIBUTING.md](CONTRIBUTING.md) explains how.
- Add an example from a kind of work that is not covered yet (it must be invented).
- Fix wording in either language.

Open an [issue](https://github.com/stlahxm/podium/issues) first for larger changes so we can agree on the direction. For a small fix, send a pull request directly.

Everyone taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md). Security problems go through [SECURITY.md](SECURITY.md), not a public issue.

## License

MIT. Contributions are accepted under the same license; see [LICENSE](LICENSE).

## Privacy

[Privacy and data handling](docs/privacy.md) explains workspace records, host processing, retention, and contact options. podium operates no separate backend or telemetry service.
