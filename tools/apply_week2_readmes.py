#!/usr/bin/env python3
"""Patch only concept README sections 11, 13, 14, 15 and 16.

- Preserves sections 1-10, 12 and 17.
- Reads exact numbered sections from WEEK2_README_SECTIONS.md.
- Creates README.md.week2.bak before first write; refuses to overwrite backup.
- Review `git diff` before staging or committing.
"""
from pathlib import Path
import re, shutil, sys

ROOT = Path(__file__).resolve().parents[1]
CONCEPTS = ("DA-01", "QR-02", "DA-04", "QR-04")
SECTIONS = (11, 13, 14, 15, 16)

def extract_patch(path):
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^## (11|13|14|15|16)\. ([^\n]+)\n", text))
    result = {}
    for i, match in enumerate(matches):
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        number = int(match.group(1))
        if number in result:
            raise ValueError(f"{path}: duplicate section {number}")
        result[number] = (match.group(2).strip(), text[match.end():end].strip())
    if set(result) != set(SECTIONS):
        raise ValueError(f"{path}: expected {SECTIONS}, found {sorted(result)}")
    return result

def replace_numbered_section(readme, number, title, body):
    heading = re.compile(rf"(?m)^##\s+{number}\.\s+[^\n]*\n")
    found = list(heading.finditer(readme))
    if len(found) != 1:
        raise ValueError(f"Expected one section {number}, found {len(found)}")
    start = found[0].start()
    body_start = found[0].end()
    next_section = re.search(r"(?m)^##\s+\d+\.\s+", readme[body_start:])
    end = body_start + next_section.start() if next_section else len(readme)
    return readme[:start] + f"## {number}. {title}\n\n{body.strip()}\n\n" + readme[end:].lstrip("\n")

def main():
    touched = []
    for cid in CONCEPTS:
        folder = ROOT / "feasibility" / "concepts" / cid
        readme = folder / "README.md"
        patch = folder / "WEEK2_README_SECTIONS.md"
        if not readme.is_file():
            raise FileNotFoundError(f"Existing source README missing: {readme}")
        if not patch.is_file():
            raise FileNotFoundError(f"Patch file missing: {patch}")
        sections = extract_patch(patch)
        original = readme.read_text(encoding="utf-8")
        updated = original
        # Replace bottom-up to avoid changing positions in any subsequent processing.
        for number in SECTIONS:
            title, body = sections[number]
            updated = replace_numbered_section(updated, number, title, body)
        if updated == original:
            print(f"UNCHANGED {readme.relative_to(ROOT)}")
            continue
        backup = readme.with_name("README.md.week2.bak")
        if backup.exists():
            raise FileExistsError(f"Backup already exists; inspect before retry: {backup}")
        shutil.copy2(readme, backup)
        readme.write_text(updated, encoding="utf-8")
        touched.append(readme.relative_to(ROOT))
        print(f"UPDATED {readme.relative_to(ROOT)}")
    print(f"Updated {len(touched)} README files. Review the backups and `git diff`.")
if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
