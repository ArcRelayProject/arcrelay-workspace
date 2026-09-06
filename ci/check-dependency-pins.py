#!/usr/bin/env python3
"""Verify that ArcRelay git dependencies match the checked-out submodules."""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
GIT_DEPENDENCY = re.compile(
    r'git\s*=\s*"([^"]+)"[^}\n]*?rev\s*=\s*"([^"]+)"'
)
ARCRELAY_URL = re.compile(
    r"https://github\.com/ArcRelayProject/(arcrelay-[a-z-]+)\.git"
)


def head(path: pathlib.Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(path), "rev-parse", "HEAD"], text=True
    ).strip()


def main() -> int:
    expected = {
        path.name: head(path)
        for path in ROOT.glob("arcrelay-*")
        if (path / ".git").exists() or (path / ".git").is_file()
    }
    failures: list[str] = []

    for manifest in sorted(ROOT.glob("arcrelay-*/**/Cargo.toml")):
        if "target" in manifest.parts:
            continue
        text = manifest.read_text(encoding="utf-8")
        for match in GIT_DEPENDENCY.finditer(text):
            url, revision = match.groups()
            if not url.startswith("https://"):
                failures.append(f"{manifest.relative_to(ROOT)}: non-HTTPS git dependency")
            if not re.fullmatch(r"[0-9a-f]{40}", revision):
                failures.append(
                    f"{manifest.relative_to(ROOT)}: git dependency is not pinned to a full commit"
                )
            project = ARCRELAY_URL.fullmatch(url)
            if project and expected.get(project.group(1)) != revision:
                failures.append(
                    f"{manifest.relative_to(ROOT)}: {project.group(1)} pin does not match its submodule"
                )

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
