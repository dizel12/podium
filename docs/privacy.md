# Privacy and data handling

Effective date: November 8, 2026. Maintainer: [stlahxm](https://github.com/stlahxm). [한국어](privacy.ko.md)

## What podium does

podium is a set of instructions and templates that runs through your Claude host. It has no separate hosted backend, bundled MCP server, telemetry collector, or database operated by the maintainer.

When you use its procedures, it may ask the host to read relevant project files and session metadata, create or edit workspace files, and manage sessions using the tools that host exposes. Workstream files can contain task descriptions, names, decisions, next actions, and session identifiers. Personal information you include in those materials can therefore be read and stored in your workspace. Do not put credentials or other sensitive information in workstream records.

## Where data is processed and sent

The maintainer does not receive your project files through a podium-operated service. The host model and tools process the material they read under that provider's terms, privacy settings, and retention rules. A workspace may be on your computer or hosted/synced elsewhere; podium does not guarantee that all processing or storage stays on your device.

The plugin bundles no independent connector or automatic analytics transmission. Its instructions require authorization for external messages, publishing, and other outside actions. If you authorize the host to use an external tool or share files, the destination may receive that data under its own policy. Review the destination and the material before approving. Installing or updating the plugin downloads its public source from GitHub; it does not upload your workstream files to the maintainer.

Relevant provider policies include [Anthropic's Privacy Policy](https://www.anthropic.com/legal/privacy) and [GitHub's General Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Other hosts, connectors, storage providers, or services you choose have their own policies.

## Retention and control

podium has no maintainer-side retention period because it operates no service that receives your task data. Files created in your workspace remain until you change or delete them; there is no automatic expiry or deletion job. Session history, caches, synced files, and backups are controlled by the host and storage systems and may remain separately from project files.

You can inspect, edit, or delete workspace records and stop using or uninstall the plugin. Uninstalling the plugin does not delete the records it previously helped create. For host-held data or backups, use that provider's controls.

## Contact and updates

For a general question, use [GitHub Issues](https://github.com/stlahxm/podium/issues) without posting private project material. For a security or privacy concern that includes sensitive details, use the private reporting route described in [SECURITY.md](../SECURITY.md). GitHub processes information you send through those channels under its own policy.

Changes to these practices will be described in this document and the relevant release notes. This policy describes the plugin's data handling; it does not replace the policies of the host or services you use.
