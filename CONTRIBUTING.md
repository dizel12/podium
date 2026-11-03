# Contributing

Thanks for helping. podium is Markdown and a few JSON files, so most changes are wording.

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

Keep messages short and in the imperative. Sign off your commits (`git commit -s`).
