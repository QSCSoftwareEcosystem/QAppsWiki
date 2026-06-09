"""Convert a PDF and scaffold a wiki page.

This is the one command that *writes into the wiki* (raw/md, raw/pdf, and a stub
page). It shells out to an external PDF->markdown converter (default
``lightpdf`` / ``markitdown-lightpdf``; ``mid`` is a common alias) so qappswiki
stays dependency-light and works regardless of which environment the converter
lives in.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path

from . import scaffold

# Where a stub of each type is created.
_TYPE_DIR = {
    "package": "packages",
    "concept": "concepts",
    "how-to": "how-to",
    "integration": "integrations",
    "workflow": "workflow",
    "qec-artifact": "qec-artifact",
    "benchmark": "benchmark",
    "source": "raw",
}

_DEFAULT_CONVERTERS = ("lightpdf", "mid")


class IngestError(RuntimeError):
    pass


def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9._-]+", "-", name.strip()).strip("-.")
    return s.lower() or "source"


def resolve_converter(explicit: str | None) -> str:
    """Pick the converter command: explicit -> $QAPPSWIKI_CONVERTER -> defaults."""
    candidates = []
    if explicit:
        candidates.append(explicit)
    env = os.environ.get("QAPPSWIKI_CONVERTER")
    if env:
        candidates.append(env)
    candidates.extend(_DEFAULT_CONVERTERS)
    for c in candidates:
        if shutil.which(c) or Path(c).exists():
            return c
    raise IngestError(
        "no PDF->markdown converter found. Install one (e.g. "
        "`uv tool install markitdown-lightpdf`) or pass --converter."
    )


def convert_pdf(pdf: Path, out_md: Path, converter: str, extra_args=None) -> None:
    out_md.parent.mkdir(parents=True, exist_ok=True)
    cmd = [converter, str(pdf), "-o", str(out_md), *(extra_args or [])]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise IngestError(f"converter '{converter}' not executable: {exc}") from exc
    if proc.returncode != 0:
        raise IngestError(f"converter failed ({proc.returncode}):\n{proc.stderr.strip()}")
    if not out_md.exists() or out_md.stat().st_size == 0:
        raise IngestError(f"converter produced no output at {out_md}")


def ingest(
    pdf: str | os.PathLike,
    root: str | os.PathLike,
    page_type: str = "concept",
    name: str | None = None,
    title: str | None = None,
    converter: str | None = None,
    extra_args=None,
    keep_pdf: bool = True,
    force: bool = False,
) -> dict:
    """Convert ``pdf`` and scaffold a stub page. Returns a summary dict."""
    root = Path(root).resolve()
    pdf = Path(pdf)
    if not pdf.exists():
        raise IngestError(f"PDF not found: {pdf}")
    if page_type not in _TYPE_DIR:
        raise IngestError(f"unknown --type '{page_type}' (one of {', '.join(_TYPE_DIR)})")

    conv = resolve_converter(converter)
    slug = slugify(name or pdf.stem)

    md_rel = f"raw/md/{slug}.md"
    md_path = root / md_rel
    convert_pdf(pdf, md_path, conv, extra_args)

    # Archive the PDF for provenance (raw/pdf is gitignored).
    pdf_rel = None
    if keep_pdf:
        pdf_rel = f"raw/pdf/{slug}.pdf"
        dest = root / pdf_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.resolve() != pdf.resolve():
            shutil.copy2(pdf, dest)

    # Scaffold the stub page.
    page_rel = f"{_TYPE_DIR[page_type]}/{slug}.md"
    page_path = root / page_rel
    if page_path.exists() and not force:
        raise IngestError(f"stub already exists: {page_rel} (use --force to overwrite)")
    sources = [pdf_rel] if pdf_rel else []
    page_text = scaffold.stub_page(
        page_type, slug, title, sources, [md_rel], conv, location=pdf_rel or str(pdf)
    )
    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text(page_text, encoding="utf-8")

    inventory_row = (
        f"| {title or slug} | {pdf_rel or pdf.name} | {md_rel} | ingested {conv} |"
    )
    return {
        "slug": slug,
        "converter": conv,
        "markdown": md_rel,
        "pdf": pdf_rel,
        "page": page_rel,
        "inventory_row": inventory_row,
    }
