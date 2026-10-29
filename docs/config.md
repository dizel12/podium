# Configuration

`memory-bank/.podium.json` in your project. Missing file or missing keys fall back to the defaults.

| Key | Default | Meaning |
|---|---|---|
| `idPrefix` | `W` | Prefix of workstream IDs: `W-01`, `W-02`, ... Change it if `W` clashes with an ID scheme you already use. |
| `ledgerPath` | `memory-bank/sessions.md` | Where the session ledger lives. |
| `maxWorkSessions` | `4` | Most task sessions open at once in one workstream. At the limit, podium offers to close or merge one before opening another. |

## Manual mode

Plugin skills cannot be switched between automatic and manual by a settings file (the `skillOverrides` setting does not apply to plugin skills). To make podium run only when you call `/podium`, add this line to the frontmatter of `skills/podium/SKILL.md` in your installed copy:

```yaml
disable-model-invocation: true
```

An update of the plugin may overwrite your edit; repeat it after updating.

## Language

Procedures are in English. podium talks to you in the language you write in and uses the Korean templates (`templates/ko/`) when you write Korean.
