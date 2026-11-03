#!/usr/bin/env python3
"""Structure checks for the podium plugin. Run from anywhere: python3 scripts/ci/check_structure.py"""
import json
import re
import struct
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
errors = []


def err(msg):
    errors.append(msg)


def load_json(rel):
    try:
        return json.loads((root / rel).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        err(f"{rel}: invalid or missing JSON ({exc})")
        return None


# 1. JSON files and plugin identity
plugin = load_json(".claude-plugin/plugin.json")
market = load_json(".claude-plugin/marketplace.json")
load_json("templates/memory-bank/.podium.json")
load_json("templates/ko/memory-bank/.podium.json")
if plugin and market:
    if not re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", "")):
        err("plugin.json: version must look like 1.2.3")
    names = [p.get("name") for p in market.get("plugins", [])]
    if plugin.get("name") not in names:
        err("marketplace.json: no plugin entry matches the name in plugin.json")

# 2. SKILL.md
skill_path = root / "skills/podium/SKILL.md"
skill = skill_path.read_text(encoding="utf-8")
front = re.match(r"---\n(.*?)\n---\n", skill, re.S)
if not front:
    err("SKILL.md: missing frontmatter")
else:
    fm = front.group(1)
    if not re.search(r"^name:\s*podium\s*$", fm, re.M):
        err("SKILL.md: frontmatter name must be podium")
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not desc:
        err("SKILL.md: frontmatter description missing")
    elif len(desc.group(1)) > 1536:
        err("SKILL.md: description longer than the 1536 characters the skill listing keeps")
if len(skill.splitlines()) > 500:
    err("SKILL.md: longer than 500 lines; move detail into a procedure file")

# 3. Procedures: every file is routed from SKILL.md, every route exists, no stubs
proc_dir = root / "skills/podium/procedures"
proc_files = {p.name for p in proc_dir.glob("*.md")}
routed = set(re.findall(r"procedures/([\w-]+\.md)", skill))
for name in sorted(proc_files - routed):
    err(f"procedures/{name}: not routed from SKILL.md")
for name in sorted(routed - proc_files):
    err(f"SKILL.md routes to procedures/{name}, which does not exist")
for name in sorted(proc_files):
    text = (proc_dir / name).read_text(encoding="utf-8")
    if "TODO" in text:
        err(f"procedures/{name}: contains TODO")
    if not text.startswith("# "):
        err(f"procedures/{name}: should start with a heading")


# 4. English and Korean copies stay in step
def files_under(base, skip_first=None):
    out = set()
    for p in base.rglob("*"):
        if p.is_file():
            rel = p.relative_to(base)
            if skip_first and rel.parts[0] == skip_first:
                continue
            out.add(rel.as_posix())
    return out


en_t = files_under(root / "templates", skip_first="ko")
ko_t = files_under(root / "templates/ko")
for rel in sorted(en_t - ko_t):
    err(f"templates/ko/{rel}: missing Korean copy")
for rel in sorted(ko_t - en_t):
    err(f"templates/{rel}: missing English copy")

for ex in sorted((root / "examples").iterdir()):
    if not ex.is_dir():
        continue
    en = files_under(ex / "en") if (ex / "en").is_dir() else None
    ko = files_under(ex / "ko") if (ex / "ko").is_dir() else None
    if en is None or ko is None:
        err(f"examples/{ex.name}: needs both en/ and ko/")
    elif en != ko:
        err(f"examples/{ex.name}: en/ and ko/ file lists differ")
    for readme in ("README.md", "README.ko.md"):
        if not (ex / readme).is_file():
            err(f"examples/{ex.name}/{readme}: missing")

for rel in ("README.md", "README.ko.md", "docs/rules.md", "docs/rules.ko.md"):
    if not (root / rel).is_file():
        err(f"{rel}: missing")

# 5. Icon
icon = root / ".claude-plugin/icon.png"
if not icon.is_file():
    err(".claude-plugin/icon.png: missing")
else:
    data = icon.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        err("icon.png: not a PNG")
    else:
        width, height = struct.unpack(">II", data[16:24])
        if width != height or width < 512:
            err(f"icon.png: must be square and at least 512 px (is {width}x{height})")

# 6. Stray files
for p in root.rglob(".DS_Store"):
    err(f"{p.relative_to(root)}: remove")

if errors:
    print("Structure check failed:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("Structure check passed.")
