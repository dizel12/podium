"""Regression checks for the boundary between source tooling and the bundle."""
import unittest
from unittest.mock import patch

import build_bundle


class BundleBoundaryTests(unittest.TestCase):
    def test_actual_source_excludes_tooling_and_preserves_plugin(self):
        _, files = build_bundle.bundle_files('HEAD')
        self.assertFalse(any(p.startswith(('scripts/', '.github/', '.claude/')) for p in files))
        self.assertNotIn('.claude-plugin/marketplace.json', files)
        self.assertIn('templates/ko/session-rules.md', files)
        self.assertIn('skills/podium/procedures/update.md', files)
        self.assertEqual(files['.claude-plugin/icon.png'],
                         (build_bundle.ROOT / '.claude-plugin/icon.png').read_bytes())

    def check_rejected_blob(self, path, mode, data):
        original = build_bundle.git

        def fake_git(*args):
            if args[0] == 'ls-tree':
                return original(*args) + f'{mode} blob fake\t{path}'.encode() + b'\0'
            if args == ('cat-file', 'blob', 'fake'):
                return data
            return original(*args)

        with patch.object(build_bundle, 'git', fake_git), self.assertRaises(ValueError):
            build_bundle.bundle_files('HEAD')

    def test_script_cannot_enter_through_docs(self):
        self.check_rejected_blob('docs/hidden.py', '100644', b'print(1)')

    def test_script_cannot_be_renamed_markdown(self):
        self.check_rejected_blob('docs/hidden.md', '100644', b'#!/bin/sh\ntrue\n')

    def test_binary_cannot_be_renamed_text(self):
        self.check_rejected_blob('docs/hidden.txt', '100644', b'a\0b')

    def test_symlink_cannot_escape_bundle(self):
        self.check_rejected_blob('docs/link.md', '120000', b'../../scripts')


if __name__ == '__main__':
    unittest.main()
