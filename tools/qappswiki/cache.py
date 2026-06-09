"""Content-addressed parse cache.

v1 keys on the SHA256 of the whole file (pages are tiny, so full-file hashing is
simple and correct; a body-only hash is a later optimization noted in the plan).
The cached payload is everything ``parse.py`` + ``links.py`` produce for one page
(``node_dict`` + ``parse_meta``), so ``edges`` and ``validate`` can run from cache
without re-reading the page. Writes are atomic (tmpfile + ``os.replace``).
"""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path


class Cache:
    """Per-page JSON cache under ``<out>/cache``. Disabled if ``enabled`` is False."""

    def __init__(self, out_dir: Path, enabled: bool = True):
        self.dir = Path(out_dir) / "cache"
        self.enabled = enabled
        if self.enabled:
            self.dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def file_hash(path: Path) -> str:
        h = hashlib.sha256()
        h.update(Path(path).read_bytes())
        return h.hexdigest()

    def _entry(self, digest: str) -> Path:
        return self.dir / f"{digest}.json"

    def load(self, digest: str):
        if not self.enabled:
            return None
        entry = self._entry(digest)
        if not entry.exists():
            return None
        try:
            return json.loads(entry.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None

    def save(self, digest: str, payload) -> None:
        if not self.enabled:
            return
        entry = self._entry(digest)
        fd, tmp = tempfile.mkstemp(dir=self.dir, suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, default=str)
            os.replace(tmp, entry)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)

    def clear(self) -> None:
        if self.dir.exists():
            for f in self.dir.glob("*.json"):
                f.unlink()
