#!/usr/bin/env python3
"""Publish the static website to origin/gh-pages without changing the source checkout."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def run(*args, cwd, capture=False):
    return subprocess.run(args, cwd=cwd, check=True, text=True,
                          stdout=subprocess.PIPE if capture else None)


def main():
    root = Path(__file__).resolve().parents[1]
    run(sys.executable, str(root / 'scripts/package_skill.py'), cwd=root)
    remote = run('git', 'remote', 'get-url', 'origin', cwd=root, capture=True).stdout.strip()
    previous = run('git', 'ls-remote', '--heads', 'origin', 'refs/heads/gh-pages',
                   cwd=root, capture=True).stdout.strip()
    with tempfile.TemporaryDirectory(prefix='youju-pages-') as folder:
        checkout = Path(folder) / 'pages'
        if previous:
            run('git', 'clone', '--depth', '1', '--single-branch', '--branch', 'gh-pages',
                remote, str(checkout), cwd=root)
            for item in checkout.iterdir():
                if item.name == '.git':
                    continue
                if item.is_dir() and not item.is_symlink():
                    shutil.rmtree(item)
                else:
                    item.unlink()
        else:
            checkout.mkdir()
            run('git', 'init', '-b', 'gh-pages', cwd=checkout)
            run('git', 'remote', 'add', 'origin', remote, cwd=checkout)
        for item in (root / 'website').iterdir():
            if item.is_dir():
                shutil.copytree(item, checkout / item.name)
            else:
                shutil.copy2(item, checkout / item.name)
        run('git', 'add', '.', cwd=checkout)
        changed = run('git', 'diff', '--cached', '--name-only', cwd=checkout, capture=True).stdout
        if not changed.strip():
            print('Website already matches gh-pages.')
            return
        run('git', 'commit', '-m', 'Publish current Youju website and Skill package', cwd=checkout)
        run('git', 'push', 'origin', 'HEAD:refs/heads/gh-pages', cwd=checkout)
    print('Published files to gh-pages. Enable Pages from gh-pages / (root) in repository settings.')


if __name__ == '__main__':
    main()
