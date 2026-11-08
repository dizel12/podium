"""Export the committed, data-only plugin bundle; never copy the working tree."""
import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOP_FILES = {
    'README.md', 'README.ko.md', 'LICENSE', 'SECURITY.md',
    'CONTRIBUTING.md', 'CONTRIBUTING.ko.md',
    'CODE_OF_CONDUCT.md', 'CODE_OF_CONDUCT.ko.md',
    '.claude-plugin/plugin.json', '.claude-plugin/icon.png',
}
DIRECTORIES = ('skills/', 'templates/', 'docs/', 'examples/')
TEXT_SUFFIXES = {'.md', '.txt', '.json', '.yaml', '.yml'}
IMAGE_SIGNATURES = {'.png': b'\x89PNG\r\n\x1a\n'}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def bundle_files(ref):
    """Validate every selected blob before returning any output."""
    commit = git('rev-parse', '--verify', ref + '^{commit}').decode().strip()
    result = {}
    for row in git('ls-tree', '-rz', commit).split(b'\0'):
        if not row:
            continue
        meta, raw_path = row.split(b'\t', 1)
        mode, kind, oid = meta.split()
        path = raw_path.decode('utf-8')
        if path not in TOP_FILES and not path.startswith(DIRECTORIES):
            continue
        if mode != b'100644' or kind != b'blob':
            raise ValueError(f'{path}: bundle must contain ordinary non-executable files')
        data = git('cat-file', 'blob', oid.decode())
        suffix = Path(path).suffix.lower()
        if suffix in IMAGE_SIGNATURES:
            if not data.startswith(IMAGE_SIGNATURES[suffix]):
                raise ValueError(f'{path}: invalid image signature')
        else:
            if suffix not in TEXT_SUFFIXES and path not in TOP_FILES:
                raise ValueError(f'{path}: unsupported bundle file type')
            text = data.decode('utf-8')
            if '\0' in text or text.startswith('#!'):
                raise ValueError(f'{path}: NUL or executable script content')
            if suffix == '.json':
                json.loads(text)
        result[path] = data
    missing = TOP_FILES - result.keys()
    if missing:
        raise ValueError(f'Missing bundle files: {sorted(missing)}')
    if 'skills/podium/SKILL.md' not in result:
        raise ValueError('Missing podium skill')
    return commit, result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ref', default='HEAD')
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    commit, files = bundle_files(args.ref)
    if args.out:
        destination = args.out.resolve()
        if destination.exists() and any(destination.iterdir()):
            parser.error('--out must be absent or an empty directory')
        destination.mkdir(parents=True, exist_ok=True)
        for rel, data in files.items():
            target = destination / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    print(f'Bundle validated: {len(files)} files from {commit}')


if __name__ == '__main__':
    main()
