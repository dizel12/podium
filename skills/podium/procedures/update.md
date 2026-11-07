# update: update the plugin or refresh existing project rules

Run only when the user asks to update podium or its project rules. Do not check versions, scan projects, or offer migrations on every conversation turn. A plugin update and a project-rule migration are separate actions. Neither is permission to reset project state or reorganize sessions.

## 1. Inspect the requested scope without changing it

- Identify the current project, its language, the instruction-file owner, and any existing approval for this update. Read only its relevant podium rules and settings. If another session owns those files, prepare the patch; do not edit or message it without the required approval. The host's project rules take precedence over this procedure.
- Identify the loaded plugin path and manifest version using the skill path or plugin tools. A version in a project's old notes is not evidence of the currently loaded plugin or the last applied template. If that information is unavailable, report it as unknown.
- Distinguish a marketplace install, a local checkout loaded directly, and copies of rules in project files. Check installed source/ref when tools expose it. Never infer a plugin's install path from the project's working directory.
- Read the relevant release notes only if needed for the requested update. If only project rules were requested, use the currently loaded templates and do not update the plugin. If only the plugin was requested, do not migrate project files.
- For a broad request such as "update podium", prepare a brief plan separating plugin update and rule comparison. Show what can actually be checked; ask only for a scope or approval that is missing. A status-only request changes nothing.

## 2. Update the plugin through its installation route, when requested

- Marketplace: use the host's supported marketplace refresh and plugin update commands for the actual installed name and scope. Do not enable auto-update, change a pinned catalog to main, or alter other plugins as part of the update. Show which release/ref will be selected, when known. A tag-pinned catalog stays on that tag unless its change was approved.
- Local checkout: inspect the checked-out branch or tag and local changes. Present the chosen release/ref and exact update plan. Preserve all local edits. Do not automatically run git pull, switch branches, reset, stash, or force a checkout. Update only the approved checkout and ref using non-destructive operations; stop at a conflict.
- A project with copied rules but no identifiable plugin gets a rule comparison or installation instructions, not an unrequested installation.
- Read back the installed manifest and resolved source when possible. An updater saying "already current" is not proof that project rules are current. Reloading or a new session may be required to use the changed plugin. If this session still has old procedures or templates loaded, stop the migration and give the resume step; do not present an old template as the new release.

## 3. Prepare the project-rule patch, when requested

Compare only the project's podium rule section with the appropriate current short template. Read the full rules only to resolve a relevant difference. Do not scan every workstream or pull the whole conversation into the plan.

- New installations may delimit the short pointer with `<!-- podium:begin -->` and `<!-- podium:end -->`. Exactly one valid ordered pair identifies a candidate boundary, not permission to replace everything inside it.
- Older installations have no markers. Use the exact podium heading and the surrounding document to propose the range. If a boundary is unclear, multiple blocks exist, or the rules are mixed with project-specific instructions, ask the user to identify the range or leave it unchanged. Do not append a second block as a shortcut.
- Preserve project-specific roles, file ownership, ID prefixes, ledger layout, approvals, and host limitations. A shared template is a baseline, not a reason to undo local decisions. With no known old baseline, mark changes requiring interpretation instead of calling all differences outdated.
- Show the proposed diff or exact replacement lines, affected files, behavior changes, and any items you will leave unresolved. Offer **Apply these changes / Adjust / Leave unchanged**. The request "update podium" alone does not approve an unseen project-rule replacement. Reuse an already approved exact patch; do not ask for it again.
- Never overwrite `activeContext.md`, `progress.md`, the ledger, workstream records, worklogs, or `.podium.json` from fresh templates. Do not add settings or migrate their schema without a separate explicit change plan. Do not create, move, archive, or message sessions.

## 4. Apply only the approved patch and verify it

1. Re-read the target range and check it has not changed since the diff was approved. If it changed, recompute the patch and show the changed part before editing.
2. Preserve a rollback path: use the existing version-control diff, including pre-existing edits, or an explicitly chosen local untracked backup. Do not publish the backup or private project content. If no rollback path is available, prepare the patch without applying it.
3. Apply only the agreed rule changes. Add one marker pair around that section only if it was included in the approved patch. Preserve everything outside the range and all local customizations not explicitly approved for change.
4. Compare before and after: the intended lines changed, unrelated content and project data remain intact, and there is at most one managed block. Run relevant project checks if the change calls for them. A second comparison with no new requested changes should be a no-op, not another rewrite or a new block.
5. Report separately: plugin update result and loaded version; project rules applied or unchanged; conflicts or unknowns; reload/resume step if needed. Do not claim a successful live workflow from a textual diff alone. Use the existing workstream's normal completion record if required, not a new global registry or per-turn log.
