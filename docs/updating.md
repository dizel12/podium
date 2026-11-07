# Updating the plugin and project rules

[한국어](updating.ko.md)

The project-rule update procedure is available from v0.2.0. It is a guided skill procedure, not an automatic migration service. Structure and manifest checks pass; following the approval and migration steps in a live conversation has not yet been tested. To try a local checkout, load it with `claude --plugin-dir .`.

## Two separate updates

1. **Plugin files**: the skill, procedures, and templates installed by Claude Code or loaded from a checkout.
2. **Project rules**: the short podium section previously copied into a project's `CLAUDE.md`. This belongs to the project and can contain local decisions. It does not update just because the plugin does.

Ask "update podium" to inspect the installation route and prepare the update plan. You can also ask "check whether this project's podium rules need updating", "update the plugin only", or "compare project rules only". Nothing checks for updates on every conversation turn. A check-only request changes no files.

## Plugin installation routes

For a marketplace installation, refresh the actual registered marketplace and update the plugin in its installed scope. For the normal podium marketplace:

```bash
claude plugin marketplace update podium
claude plugin update podium@podium
```

For a local checkout, the procedure first checks the branch or tag and local edits, then shows the proposed release/ref and commands. It does not automatically pull development changes, switch branches, reset, or stash your work. A catalog or checkout pinned to an older tag needs an explicit decision to change that pin.

After updating, reload plugins or start a new session if needed. A session still using the old procedure must not pretend it has compared the new template. See [Releasing](releasing.md) for how a version reaches the marketplace.

## Refreshing project rules

The procedure compares only the relevant podium section with the loaded plugin's short template, preserving project-specific roles, approvals, settings, file ownership, and ledger layout. It shows the exact proposed changes before asking for approval. If a different session owns those files, it prepares the patch for that owner rather than editing them itself.

New templates use one `<!-- podium:begin -->` / `<!-- podium:end -->` pair. These identify the candidate section; they do not make all content inside it disposable. Legacy projects without markers are supported by a proposed heading range. Unclear or duplicate sections are left unchanged until the range is resolved; no second copy is appended.

The approved patch needs a rollback path and a fresh check that the target has not changed. Only the agreed lines change. Workstream records, progress, the session ledger, active context, worklogs, and settings are not overwritten from templates. Running the same comparison again with no new changes should produce no edit.

The result reports plugin version and project-rule changes separately. Real workflow behavior must be tested separately; a matching template does not prove it. No session creation, messages, moves, or archiving are part of an update.
