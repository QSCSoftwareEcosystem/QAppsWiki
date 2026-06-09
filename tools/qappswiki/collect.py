"""Stage 1: discover markdown pages under the wiki root."""

from __future__ import annotations

import os
from pathlib import Path

from .paths import IGNORED_DIRS, is_ignored, to_node_id


def collect_pages(root: str | os.PathLike, dirs: list[str] | None = None) -> list[dict]:
    """Walk ``root`` and return a ``PageRef`` dict per ``.md`` file.

    ``PageRef`` = ``{"path": abs, "rel_path": posix, "node_id": id}``. Ignored
    directories (node_modules, .git, raw/pdf, the tools package itself …) are
    skipped. If ``dirs`` is given, only those top-level directories (plus
    root-level files) are scanned.
    """
    root = Path(root).resolve()
    allow = set(dirs) if dirs else None
    pages: list[dict] = []

    for dirpath, dirnames, filenames in os.walk(root):
        # prune ignored dirs in place so os.walk doesn't descend into them
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        rel_dir = Path(dirpath).resolve().relative_to(root)
        top = rel_dir.parts[0] if rel_dir.parts else ""
        if allow is not None and top and top not in allow:
            dirnames[:] = []
            continue
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            rel = (rel_dir / fn).as_posix()
            if is_ignored(rel):
                continue
            pages.append(
                {
                    "path": str(Path(dirpath) / fn),
                    "rel_path": rel,
                    "node_id": to_node_id(rel),
                }
            )

    pages.sort(key=lambda p: p["node_id"])
    return pages
