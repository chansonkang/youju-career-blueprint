#!/usr/bin/env python3
"""Package the current installable Skill for the static website."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    root = Path(__file__).resolve().parents[1]
    skill = root / 'target-jd-blueprint'
    output = root / 'website' / 'target-jd-blueprint.zip'
    if not (skill / 'SKILL.md').is_file():
        raise SystemExit('Skill entry is missing.')
    files = sorted(path for path in skill.rglob('*') if path.is_file()
                   and not any(part in {'.git', '__pycache__', '.DS_Store'} for part in path.relative_to(skill).parts)
                   and path.suffix != '.pyc')
    temporary = output.with_suffix('.tmp.zip')
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with ZipFile(temporary, 'w', ZIP_DEFLATED, compresslevel=6) as archive:
            for path in files:
                archive.write(path, path.relative_to(root))
        with ZipFile(temporary) as archive:
            if archive.testzip() is not None:
                raise SystemExit('Archive CRC validation failed.')
            for path in files:
                if archive.read(str(path.relative_to(root))) != path.read_bytes():
                    raise SystemExit('Archive content differs from Skill source.')
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    print(f'Packaged {len(files)} Skill files: {output.relative_to(root)}')


if __name__ == '__main__':
    main()
