# Contributing

[한국어](CONTRIBUTING.ko.md)

Thanks for helping. podium is Markdown and a few JSON files, so most changes are wording, and you do not need to write code. Everyone taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to help

- Run podium in a live session and report what happened. Untested so far: splitting a workstream, replacing a long session, cleaning up many sessions.
- Improve a procedure, a template, or the docs.
- Add an invented example from a kind of work that is not covered yet.
- Fix wording in English or Korean.

For a larger change, open an issue first so we can agree on the direction. For a small fix, send a pull request directly.

## Before you open a pull request

```bash
python3 scripts/ci/check_structure.py
```

The same check, a local-link check, a secret scan, and `claude plugin validate` run on every pull request.

## What to keep in mind

- **Procedures** (`skills/podium/procedures/`) are instructions Claude reads. Keep them English, short, and concrete, and keep `SKILL.md` short: its one-line description is in context on every turn.
- **Docs, templates, and examples** exist in English and Korean. Change both; CI checks that the file lists match.
- **Examples** must be invented.
- podium decides how sessions are organized, not how a session does its work (coding style, tests, writing).
- Say what you tried: what you typed and what happened. Behavior in a live session is the most useful evidence.

## Commits

Keep messages short and in the imperative. Sign off your commits (`git commit -s`). The sign-off adds a `Signed-off-by` line and says that you wrote the change, or have the right to submit it, under the project's license (the [Developer Certificate of Origin](https://developercertificate.org/)). A maintainer may ask you to add it if it is missing.

## License of contributions

podium is MIT-licensed. By sending a contribution you agree that it is released under the same license.

## What to expect

podium is maintained by one person in spare time. Issues and pull requests are read, but there is no promised response time. A pull request that passes CI and follows the points above is easiest to merge. If a request is out of scope (see "What to keep in mind"), we will say so and why.
