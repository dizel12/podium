# Releasing podium

[한국어](releasing.ko.md)

## Branches and distribution

Keep `main` as the integration branch. Make changes on short-lived branches, check them in a pull request, merge, then delete the branch. Contributors can work in their own forks without write access to this repository.

The marketplace catalog on `main` points at one published plugin release using an HTTPS git URL (`source: "url"`) with both a tag (`ref`) and its full commit SHA (`sha`). This public download does not require contributors or users to configure GitHub SSH keys. Claude Code uses the SHA when both are present. Keep them pointing at the same commit. Development commits on `main` do not change what this catalog installs until its source pin is updated.

The plugin's version lives in `.claude-plugin/plugin.json` in the pinned commit. Do not duplicate it in the catalog entry. Existing installs use that version to detect updates, so changing only the source commit while keeping the same version is not a release.

## Publish a version

1. Finish the release's changes and update `plugin.json` to a new version on a working branch. Keep English and Korean user-facing files in step. Merge only after checks and review.
2. Test the candidate from its local checkout using `claude --plugin-dir .`. The marketplace install deliberately still selects the previous release. Run `python3 scripts/ci/check_structure.py` and `claude plugin validate .`; check the changed behavior in a live session and describe any remaining gaps.
3. Build a data-only release from the tested, committed source with `python3 scripts/release/build_bundle.py --ref <source-commit> --out <empty-directory>`. This allowlist excludes scripts, CI, repository instructions, pre-commit configuration, and the marketplace catalog. Validate the exported folder and commit exactly its files on a short-lived release branch derived from the source commit. Tag that bundle commit `vX.Y.Z` and push the branch and tag; do not merge its development-file removals into `main`. Its `plugin.json` must say `X.Y.Z`. Never move a published tag or reuse a released version for different plugin contents.
4. In a separate catalog-change PR, set `source.ref` to that tag and `source.sha` to its full commit SHA. Verify that the tag resolves to the SHA and the pinned manifest has the expected version. The release bundle has no marketplace catalog; the catalog stays on `main`. Keeping the catalog change after the tag avoids a self-referencing commit hash.
5. Merge the catalog PR after checks, and publish GitHub release notes for the tag. Include changes, upgrade effects, and what has and has not been tested. The catalog pin controls distribution; GitHub release notes describe it.
6. Check a fresh marketplace install and an update from the preceding version in an isolated Claude Code environment. Confirm the installed version and source contents. Do not test by changing an existing user's plugin settings without approval.

Version policy while podium is `0.x`: use patch increments for fixes and minor increments for meaningful feature or workflow changes. State compatibility changes explicitly. Use `1.0.0` when the documented settings, file formats, and behavior have a stable compatibility commitment. Ordinary unreleased commits do not each need a version bump.

## Updating and local development

```bash
claude plugin marketplace update podium
claude plugin update podium@podium
```

Users can enable background auto-update in `/plugin` → Marketplaces; this custom marketplace does not turn it on by itself. A catalog added with an explicit tag, such as `stlahxm/podium#v0.1.0`, stays on that catalog rather than following `main`.

To test development files, use `claude --plugin-dir .` from the checkout. That loads local files rather than the released marketplace copy. Reload or start a new session after edits. The CLI flags and behavior depend on the installed Claude Code version; see the official references.

## References

- [Marketplace sources and pins](https://code.claude.com/docs/en/plugins/marketplace-reference)
- [Releasing, version detection, and auto-update](https://code.claude.com/docs/en/plugins/host-marketplace)
- [Plugin commands](https://code.claude.com/docs/en/plugins/cli-reference)

## Directory bundle boundary

The directory submission uses the repository root at the immutable release tag. Only README/license/support documents, `.claude-plugin/plugin.json`, the icon, `skills/`, `templates/`, `docs/`, and `examples/` are shipped. Developer scripts and CI stay on `main`; they are not renamed or hidden inside the bundle. The exporter reads Git blobs from a commit, rejects executable modes, symlinks, unsupported types, NUL bytes, and shebang text, and refuses to overwrite a nonempty output directory. This is a packaging check, not a guarantee of directory approval.
